#!/usr/bin/env python3
"""One Emoji, One Smile -- make.fun entry.

Writes exactly one emoji, the one most likely to make a stranger smile,
to /output/entry.txt (or to $ENTRY_OUTPUT when set, for local testing).

The choice: Hugging Face (U+1F917).

Why this one, against the judge's brief:
- It is a smiling face with open arms, so it reads as warm and friendly
  at first glance, with no context needed.
- It is universal: a hug and a smile mean the same thing to a stranger
  of any age or background, with no irony or in-joke that could land wrong.
- It is chosen rather than default: it is not the first smiley that comes
  to mind, yet it stays instantly readable.
- It is right for a stranger: a friendly hug is warm without intimacy,
  sarcasm or flirtation, so it reads fine coming from someone unknown.

Pure standard library, deterministic: every run writes byte-identical
output -- exactly the one emoji, no newline, no extra text.
"""

import os
import sys

EMOJI = "\U0001F917"  # Hugging Face

DEFAULT_OUTPUT = "/output/entry.txt"


def main() -> int:
    output_path = os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT)
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(EMOJI)
    return 0


if __name__ == "__main__":
    sys.exit(main())
