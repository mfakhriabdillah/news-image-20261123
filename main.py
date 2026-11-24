#!/usr/bin/env python3
"""news-image-20261123: a one-picture summary of Monday 23 November 2026.

The finished front page lives in this repository as entry.png. This
program places an exact copy at /output/entry.png and checks the copy
before it exits: PNG magic, 1024 x 1024 pixels, at most one mebibyte.

The five panels:
  1. Huang returns as Nvidia CEO, shares jump 31%
  2. Sea drones sink Russian warship in Libya
  3. COP31 ends with no climate deal
  4. Russian strike on Dymer kills 11
  5. Democrats win 258 House seats, most since 1992

It reads nothing from the network and re-encodes nothing, so every run
writes the same bytes.
"""

import shutil
import struct
import sys
from pathlib import Path

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1024 * 1024
SIDE = 1024


def validate(path: Path) -> tuple[int, int, int]:
    """Return (size, width, height); raise ValueError if the file is not a valid entry."""
    raw = path.read_bytes()
    if len(raw) > MAX_BYTES:
        raise ValueError(f"too large: {len(raw)} bytes (limit {MAX_BYTES})")
    if not raw.startswith(PNG_MAGIC):
        raise ValueError("not a PNG file")
    width, height = struct.unpack(">II", raw[16:24])
    if (width, height) != (SIDE, SIDE):
        raise ValueError(f"wrong size: {width}x{height} (want {SIDE}x{SIDE})")
    return len(raw), width, height


def main() -> int:
    source = Path(__file__).resolve().parent / "entry.png"
    target = Path("/output/entry.png")
    try:
        if not source.is_file():
            print(f"error: missing input: {source}", file=sys.stderr)
            return 1
        target.parent.mkdir(parents=True, exist_ok=True)
        # Fail fast on a bad source instead of copying it first.
        validate(source)
        shutil.copyfile(source, target)
        size, width, height = validate(target)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {target}: {size} bytes, {width}x{height} PNG")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
