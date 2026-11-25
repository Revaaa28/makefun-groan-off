#!/usr/bin/env python3
"""Groan-Off entry: write one dad joke to /output/entry.txt.

The line is a one-line dad joke, chosen by manual ranking against the
competition's judge brief (is a dad joke, punchline lands fast and clean,
fresh, tight and rhythmic, groan earned). See candidates.md for the full
candidate list and the ranking.
"""

import os

LINE = "I put my phone on airplane mode. It still hasn't landed a job."

# The competition gate: /output/entry.txt must be UTF-8 text of 1-140
# characters, not only white space. Refuse to write an invalid line
# rather than silently submitting a losing entry.
MAX_CHARS = 140


def main():
    if not LINE.strip() or len(LINE) > MAX_CHARS:
        raise SystemExit(
            f"entry line fails the gate: {len(LINE)} chars, "
            f"blank={not LINE.strip()}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
