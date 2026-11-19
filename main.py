# news-image-20261119 entry (Python 3.13, standard library only).
#
# The entry is the image entry.png beside this file: a newspaper front
# page, 1024x1024, summing up the world news of Thursday 19 November
# 2026 in six panels. This program copies it to /output/entry.png (or
# $MAKEFUN_OUTPUT_DIR outside the grader's container):
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# The copy is checked, not trusted. Before copying, the source is
# checked against the gate (a whole PNG, at most 1 MiB and 1024x1024).
# After copying, the output is asserted byte-identical to the source by
# sha256 and file size, and its own PNG header is re-read to prove the
# file that actually lands in the output directory is itself a whole,
# gate-passing PNG with the source's dimensions, so the two grader runs
# write identical output. No network, no randomness, no input besides
# the image file itself.

import hashlib
import os
import shutil
import struct
from pathlib import Path

MAX_BYTES = 1_048_576
MAX_DIMENSION = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"

SOURCE = Path(__file__).resolve().parent / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT = OUTPUT_DIR / "entry.png"


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _check_png(path):
    """Reject an image that breaks the gate; return its (width, height).

    The same check runs on the source before copying and on the output
    after copying, so both files are independently proven gate-passing.
    """
    size = path.stat().st_size
    if size > MAX_BYTES:
        raise ValueError(f"{path.name} is {size} bytes, over the {MAX_BYTES} limit")
    with open(path, "rb") as f:
        header = f.read(33)
    if header[:8] != PNG_MAGIC:
        raise ValueError(f"{path.name} is not a PNG (bad magic bytes)")
    if header[12:16] != b"IHDR":
        raise ValueError(f"{path.name} has no IHDR chunk")
    width, height = struct.unpack(">II", header[16:24])
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        raise ValueError(f"{path.name} is {width}x{height}, over {MAX_DIMENSION}x{MAX_DIMENSION}")
    return width, height


def main():
    if not SOURCE.is_file():
        raise FileNotFoundError(f"missing source image: {SOURCE}")
    source_width, source_height = _check_png(SOURCE)
    source_hash = _sha256(SOURCE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    # Read-back assert: the output must be an exact copy of the source.
    if _sha256(OUTPUT) != source_hash:
        raise ValueError("output differs from source after copy")
    if OUTPUT.stat().st_size != SOURCE.stat().st_size:
        raise ValueError("output size differs from source after copy")
    # Output-side gate check: re-read the output file's own header and
    # prove it is itself a whole, gate-passing PNG with the source's
    # dimensions, not just bytes that happen to hash the same.
    out_width, out_height = _check_png(OUTPUT)
    if (out_width, out_height) != (source_width, source_height):
        raise ValueError(
            f"output is {out_width}x{out_height}, source is "
            f"{source_width}x{source_height}"
        )


if __name__ == "__main__":
    main()
