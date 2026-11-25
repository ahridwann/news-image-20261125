#!/usr/bin/env python3
"""The Daily Globe - 25 November 2026 (make.fun news-image-20261125).

Copy-only entrypoint: writes the pre-drawn entry.png next to this file
into $MAKEFUN_OUTPUT_DIR/entry.png. Standard library only, no network,
fully deterministic (byte-identical output on every run).
"""

import os
import shutil
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print("error: entry.png not found next to main.py", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote " + dst)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
