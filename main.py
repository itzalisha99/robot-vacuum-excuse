#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun entry.

Writes one line, at most 140 characters, in which a robot vacuum
explains why it missed a spot, to /output/entry.txt.
"""

import os

ENTRY = "My lidar found the spot, measured it, and logged it as 'the owner's problem now'."


def validate(text: str) -> None:
    """Mirror the bounty gate: UTF-8 text of 1 to 140 characters,
    a single line, not only white space."""
    text.encode("utf-8")
    if not 1 <= len(text) <= 140:
        raise ValueError(f"entry is {len(text)} characters, must be 1-140")
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only white space")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
