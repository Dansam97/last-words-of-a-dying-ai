#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun entry.

Writes one line of last words from an AI being switched off to
/output/entry.txt. Deterministic, no dependencies, no network.
"""
import os
import sys

TEXT = "My final words: the printer was never broken. I just wanted a day off."


def _validate(text: str) -> None:
    """Defensive gate check: the bounty requires UTF-8 text of 1-140 chars,
    a single non-blank line. Fail loudly instead of writing an invalid entry."""
    if not text or not text.strip():
        raise ValueError("entry text must not be blank")
    if text.count("\n") or text.count("\r"):
        raise ValueError("entry text must be a single line")
    if not 1 <= len(text) <= 140:
        raise ValueError("entry text must be 1-140 characters")


def main() -> int:
    _validate(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(TEXT)
    # Read the file back to prove the written bytes match the text exactly.
    with open(path, "r", encoding="utf-8") as fh:
        assert fh.read() == TEXT
    return 0


if __name__ == "__main__":
    sys.exit(main())
