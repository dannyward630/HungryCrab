# Bounded local acquisition

`crab catch` can enforce the same finite storage and shared TLS budget as Feeder:

```text
crab --cache-dir R:/cache catch owner/repo --shallow --acquisition-volume R:/ --max-acquisition-disk-bytes 1073741824 --max-download-bytes 314572800
```

Use a dedicated fixed-capacity Linux block-device mount or Windows volume. The kernel
bounds objects, expansion/checkout, main and independent wiki, staged metadata, temporary
files and retained old cache data together. A directory, Docker bind mount, remote size,
free-space observation or post-clone sampler is not a quota. The CLI verifies capacity
before network acquisition and refuses unsupported mounts/process boundaries. If a byte
limit is explicitly requested without a volume, catch refuses an unbounded fallback.
Legacy catch without a volume remains unbounded; use the explicit bounded invocation for
foreign acquisition. The Python API exposes the same fields on `CatchOptions`.

Linux uses the backing block-device capacity and a new process session, killed as a group.
Windows uses `IOCTL_DISK_GET_LENGTH_INFO` on the volume handle and a private Job Object.
Git starts suspended, enters the non-breakaway job, then its initial thread resumes. A
timeout, captured-output overflow or supervisor cleanup closes the job and terminates
descendants. A trusted no-op process verifies that the host's enclosing-job policy permits
assignment before any acquisition network request. The volume/process APIs require their
normal Windows access rights; volume verification may require an elevated terminal.

A fixed VHD is supported without Docker, WSL or Hyper-V tooling. The repository's disposable
CI provisioner uses built-in DiskPart and an unused drive letter. In an elevated Windows
terminal, set `RUNNER_TEMP` to a dedicated temporary parent and `GITHUB_OUTPUT` to an output
file, then run `python scripts/acquisition_volume.py prepare 1073741824`. Keep its returned
root for `python scripts/acquisition_volume.py cleanup <root>`. The provisioner selects
only its newly created image, records ownership, checks host headroom, and confirms detach
before deleting that owned directory. It never cleans/selects an existing host disk. A
failed detach retains the image for recovery. Provisioning/mounting is an operator action;
the CLI never elevates or silently installs a backend.

The fixed VHD's footer and the small preparation/control logs live outside its filesystem;
reserve host headroom for this bounded overhead and the fixed image itself. Docker image,
daemon and bind-mount storage are not part of this native backend. A production Docker
backend would need separately demonstrated quotas for all those writes. Do not treat merely
installing Docker as proof of containment. Long-term retained cache growth is separate from
an invocation's quota; full collection remains #213. Keep enough volume space for old data
plus replacement staging, or explicitly provision a larger dedicated domain.

A volume lock serializes acquisitions sharing the same finite domain; a competing attempt
refuses before network access. Separate domains can operate independently. The relay meters
server bytes across Git's main/wiki TLS connections, retries and reference discovery; TLS
stays end to end. At most one sentinel byte is read beyond the allowance and never forwarded.
Socket buffers/wire traffic and provider REST requests retain their separately documented
limits. No disk/download fallback is enabled after a refusal.

Handled failures preserve the prior complete cache and remove owned partial staging.
Interrupted publication rolls back; failed rollback preserves an owned journal/backup.
Machine termination cannot run cleanup handlers: inspect retained bounded staging and do
not promote it to a reusable cache. An abrupt supervisor death before Windows job assignment
can leave a suspended, never-resumed child; this is not a running acquisition. Inspect and
reap such a child before recovering that owned volume.

CI runs real HTTPS Git clone/refresh, compressible checkout expansion, incompressible wiki
pack overflow and cleanup on both Windows and Linux fixed volumes. Independent connection
accounting, cancellation and contention controls also run in the regular tests. Synthetic
source/server fixtures are owned test data; donor programs are never executed.

API references: [volume length](https://learn.microsoft.com/en-us/windows/win32/api/winioctl/ni-winioctl-ioctl_disk_get_length_info),
[Job Objects](https://learn.microsoft.com/en-us/windows/win32/procthread/job-objects),
[fixed VHD provisioning](https://learn.microsoft.com/en-sg/windows-hardware/manufacture/desktop/boot-to-vhd--native-boot--add-a-virtual-hard-disk-to-the-boot-menu?view=windows-11).
