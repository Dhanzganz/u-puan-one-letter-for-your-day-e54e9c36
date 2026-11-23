#!/usr/bin/env python3
"""One Letter for Your Day — make.fun bounty entry.

Writes exactly one character, "W", to /output/entry.txt with no trailing
newline or extra whitespace. Python 3 standard library only.

The single letter sums up the whole day: W — for a win.
"""

import os

# The entire entry: one letter, "W", for a winning day.
ENTRY = "W"
OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
