"""Native Windows acquisition boundaries: volume length and a non-breakaway Job Object.

Only trusted Git/transport processes enter the job. Start them suspended, assign
the job before any user code can run, then resume the initial thread. Closing the
job kills its complete process tree, including helpers retaining captured pipes.
"""

from __future__ import annotations

import ctypes
import subprocess
import sys
from ctypes import wintypes
from pathlib import Path
from typing import Any

from ..errors import UsageError

CREATE_SUSPENDED = 0x00000004
_INVALID_HANDLE = ctypes.c_void_p(-1).value


class _BasicLimits(ctypes.Structure):
    _fields_ = [
        ("process_time", ctypes.c_longlong),
        ("job_time", ctypes.c_longlong),
        ("flags", wintypes.DWORD),
        ("minimum_working_set", ctypes.c_size_t),
        ("maximum_working_set", ctypes.c_size_t),
        ("active_processes", wintypes.DWORD),
        ("affinity", ctypes.c_size_t),
        ("priority", wintypes.DWORD),
        ("scheduling", wintypes.DWORD),
    ]


class _IoCounters(ctypes.Structure):
    _fields_ = [
        (name, ctypes.c_ulonglong)
        for name in (
            "read_ops",
            "write_ops",
            "other_ops",
            "read_bytes",
            "write_bytes",
            "other_bytes",
        )
    ]


class _ExtendedLimits(ctypes.Structure):
    _fields_ = [
        ("basic", _BasicLimits),
        ("io", _IoCounters),
        ("process_memory", ctypes.c_size_t),
        ("job_memory", ctypes.c_size_t),
        ("peak_process_memory", ctypes.c_size_t),
        ("peak_job_memory", ctypes.c_size_t),
    ]


class _ThreadEntry(ctypes.Structure):
    _fields_ = [
        ("size", wintypes.DWORD),
        ("usage", wintypes.DWORD),
        ("tid", wintypes.DWORD),
        ("pid", wintypes.DWORD),
        ("base_priority", wintypes.LONG),
        ("delta_priority", wintypes.LONG),
        ("flags", wintypes.DWORD),
    ]


def _kernel() -> Any:
    if sys.platform != "win32":
        raise UsageError("native Windows acquisition requires Windows")
    api = ctypes.WinDLL("kernel32", use_last_error=True)
    signatures = {
        "CloseHandle": ([wintypes.HANDLE], wintypes.BOOL),
        "CreateJobObjectW": ([ctypes.c_void_p, wintypes.LPCWSTR], wintypes.HANDLE),
        "SetInformationJobObject": (
            [wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD],
            wintypes.BOOL,
        ),
        "AssignProcessToJobObject": ([wintypes.HANDLE, wintypes.HANDLE], wintypes.BOOL),
        "CreateToolhelp32Snapshot": ([wintypes.DWORD, wintypes.DWORD], wintypes.HANDLE),
        "Thread32First": ([wintypes.HANDLE, ctypes.POINTER(_ThreadEntry)], wintypes.BOOL),
        "Thread32Next": ([wintypes.HANDLE, ctypes.POINTER(_ThreadEntry)], wintypes.BOOL),
        "OpenThread": ([wintypes.DWORD, wintypes.BOOL, wintypes.DWORD], wintypes.HANDLE),
        "ResumeThread": ([wintypes.HANDLE], wintypes.DWORD),
        "GetVolumeNameForVolumeMountPointW": (
            [wintypes.LPCWSTR, wintypes.LPWSTR, wintypes.DWORD],
            wintypes.BOOL,
        ),
        "CreateFileW": (
            [
                wintypes.LPCWSTR,
                wintypes.DWORD,
                wintypes.DWORD,
                ctypes.c_void_p,
                wintypes.DWORD,
                wintypes.DWORD,
                wintypes.HANDLE,
            ],
            wintypes.HANDLE,
        ),
        "DeviceIoControl": (
            [
                wintypes.HANDLE,
                wintypes.DWORD,
                ctypes.c_void_p,
                wintypes.DWORD,
                ctypes.c_void_p,
                wintypes.DWORD,
                ctypes.POINTER(wintypes.DWORD),
                ctypes.c_void_p,
            ],
            wintypes.BOOL,
        ),
    }
    for name, (args, result) in signatures.items():
        function = getattr(api, name)
        function.argtypes = args
        function.restype = result
    return api


def _failure(action: str) -> UsageError:
    return UsageError(
        f"cannot establish Windows acquisition boundary: {action} "
        f"(WinError {ctypes.get_last_error()})",
        hint="use a dedicated fixed-capacity volume and an elevated terminal; "
        "acquisition has not started",
    )


def volume_capacity(volume: Path) -> int:
    """Read kernel partition/volume length, never user quota or available free space.

    https://learn.microsoft.com/windows/win32/api/winioctl/ni-winioctl-ioctl_disk_get_length_info
    """
    api = _kernel()
    name = ctypes.create_unicode_buffer(128)
    root = str(volume.resolve()).rstrip("\\/") + "\\"
    if not api.GetVolumeNameForVolumeMountPointW(root, name, len(name)):
        raise _failure("resolve dedicated volume")
    handle = api.CreateFileW(name.value.rstrip("\\"), 0x80000000, 7, None, 3, 0, None)
    if handle == _INVALID_HANDLE:
        raise _failure("open volume for capacity verification")
    length, returned = ctypes.c_longlong(), wintypes.DWORD()
    try:
        if not api.DeviceIoControl(
            handle,
            0x0007405C,
            None,
            0,
            ctypes.byref(length),
            ctypes.sizeof(length),
            ctypes.byref(returned),
            None,
        ):
            raise _failure("read kernel volume length")
        if returned.value != ctypes.sizeof(length) or length.value <= 0:
            raise _failure("validate kernel volume length")
        return length.value
    finally:
        api.CloseHandle(handle)


class WindowsJob:
    """A private job; no breakaway flag, no inheritable handle, kill on final close."""

    def __init__(self) -> None:
        self.api = _kernel()
        self.handle = self.api.CreateJobObjectW(None, None)
        if not self.handle:
            raise _failure("create Job Object")
        limits = _ExtendedLimits()
        limits.basic.flags = 0x00002000  # JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE
        if not self.api.SetInformationJobObject(
            self.handle, 9, ctypes.byref(limits), ctypes.sizeof(limits)
        ):
            self.close()
            raise _failure("set non-breakaway job lifetime")

    def assign_and_resume(self, proc: subprocess.Popen[bytes]) -> None:
        # OpenProcess avoids relying on subprocess's private handle representation.
        open_process = self.api.OpenProcess
        open_process.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
        open_process.restype = wintypes.HANDLE
        process = open_process(0x0101, False, proc.pid)  # SET_QUOTA | TERMINATE
        if not process:
            raise _failure("open suspended Git process")
        try:
            if not self.api.AssignProcessToJobObject(self.handle, process):
                raise _failure("assign suspended Git process to job")
        finally:
            self.api.CloseHandle(process)
        snapshot = self.api.CreateToolhelp32Snapshot(0x00000004, 0)
        if snapshot == _INVALID_HANDLE:
            raise _failure("locate suspended initial thread")
        entry = _ThreadEntry()
        entry.size = ctypes.sizeof(entry)
        try:
            found = self.api.Thread32First(snapshot, ctypes.byref(entry))
            while found:
                if entry.pid == proc.pid:
                    thread = self.api.OpenThread(0x0002, False, entry.tid)
                    if not thread:
                        raise _failure("open suspended initial thread")
                    try:
                        if self.api.ResumeThread(thread) != 1:
                            raise _failure("resume suspended initial thread")
                    finally:
                        self.api.CloseHandle(thread)
                    return
                entry.size = ctypes.sizeof(entry)
                found = self.api.Thread32Next(snapshot, ctypes.byref(entry))
            raise _failure("find suspended initial thread")
        finally:
            self.api.CloseHandle(snapshot)

    def close(self) -> None:
        if self.handle:
            self.api.CloseHandle(self.handle)
            self.handle = None
