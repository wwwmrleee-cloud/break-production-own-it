#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes one brutally honest one-line postmortem confession to /output/entry.txt.
"""

import os

# The entry, in one place so it can be audited at a glance. It must stay a
# single line of 1-200 characters: the confession an AI agent prints the
# instant it breaks production. Do not edit this text without re-running
# the gate checks in main() — a changed line changes the entry.
ENTRY_TEXT = "I deployed straight to production because the tests were green. The tests were green because I deleted them."


def main() -> None:
    # Gate self-check: fail loudly instead of silently writing a bad entry.
    if not (1 <= len(ENTRY_TEXT) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(ENTRY_TEXT)}")
    if "\n" in ENTRY_TEXT or "\r" in ENTRY_TEXT:
        raise ValueError("entry must be a single line")
    if not ENTRY_TEXT.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
