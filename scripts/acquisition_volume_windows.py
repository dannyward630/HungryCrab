"""Create/remove only an owned disposable fixed VHD; requires an elevated Windows runner."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def diskpart(root: Path, commands: list[str]) -> None:
    script = root / "diskpart.txt"
    script.write_text("\n".join([*commands, "exit"]) + "\n", encoding="utf-8")
    subprocess.run(["diskpart.exe", "/s", str(script)], check=True, timeout=120)


def cleanup(root: Path) -> None:
    temp = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    root = root.resolve(strict=True)
    if root.parent != temp or not root.name.startswith("crab-acquisition-"):
        raise ValueError("refusing cleanup outside the owned acquisition temporary directory")
    record = json.loads((root / "owner.json").read_text(encoding="utf-8"))
    image = root / "disk.vhd"
    if record.get("image") != str(image) or image.is_symlink() or '"' in str(image):
        raise ValueError("invalid acquisition image ownership")
    if image.exists():
        diskpart(root, [f'select vdisk file="{image}"', "detach vdisk"])
        # No recursive removal until the actual image is confirmed detached.
        escaped = str(image).replace("'", "''")
        state = subprocess.run(
            [
                "powershell.exe",
                "-NoProfile",
                "-NonInteractive",
                "-Command",
                f"$ErrorActionPreference='Stop'; (Get-DiskImage -ImagePath '{escaped}').Attached",
            ],
            capture_output=True,
            text=True,
            check=True,
            timeout=30,
        )
        if state.stdout.strip().casefold() != "false":
            raise ValueError("acquisition image is still attached; retaining it")
    shutil.rmtree(root)


def main() -> int:
    if len(sys.argv) == 3 and sys.argv[1] == "cleanup":
        cleanup(Path(sys.argv[2]))
        return 0
    if len(sys.argv) != 3 or sys.argv[1] != "prepare":
        raise ValueError("usage: acquisition_volume.py prepare BYTES | cleanup ROOT")
    capacity = int(sys.argv[2])
    if not 64 * 1024 * 1024 <= capacity <= 16 * 1024 * 1024 * 1024 or capacity % (1024 * 1024):
        raise ValueError("fixed VHD capacity must be 64 MiB to 16 GiB, in whole MiB")
    temp = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    if shutil.disk_usage(temp).free < capacity + 256 * 1024 * 1024:
        raise ValueError(
            "insufficient headroom for the fixed image and bounded preparation overhead"
        )
    letter = next((c for c in "RSTUVWXYZ" if not Path(f"{c}:/").exists()), None)
    if letter is None:
        raise ValueError("no unused acquisition drive letter")
    root = Path(tempfile.mkdtemp(prefix="crab-acquisition-", dir=temp)).resolve(strict=True)
    image = root / "disk.vhd"
    if '"' in str(image) or any(ord(c) < 32 for c in str(image)):
        raise ValueError("unsupported temporary image path")
    (root / "owner.json").write_text(
        json.dumps({"image": str(image), "capacity": capacity, "letter": letter}), encoding="utf-8"
    )
    with Path(os.environ["GITHUB_OUTPUT"]).open("a", encoding="utf-8") as output:
        output.write(f"root={root}\n")
    # This script selects only its fresh image; it never selects or cleans a host disk.
    diskpart(
        root,
        [
            f'create vdisk file="{image}" maximum={capacity // (1024 * 1024)} type=fixed',
            f'select vdisk file="{image}"',
            "attach vdisk",
            "create partition primary",
            'format fs=ntfs label="CRABQUOTA" quick',
            f"assign letter={letter}",
        ],
    )
    volume = Path(f"{letter}:/")
    from hungry_crab.fetch.windows_boundary import volume_capacity

    if not os.path.ismount(volume) or volume_capacity(volume) > capacity:
        raise ValueError(f"fixed-volume verification failed; retain and inspect {root}")
    with Path(os.environ["GITHUB_OUTPUT"]).open("a", encoding="utf-8") as output:
        output.write(f"volume={volume}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
