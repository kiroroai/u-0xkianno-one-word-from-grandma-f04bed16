#!/usr/bin/env python3
"""One Word From Grandma.

Writes exactly one word -- the word grandma would text about AI --
to /output/entry.txt. Python 3 stdlib only, deterministic, no network.

The word is "Robit": the typo of "robot" a grandma would actually make
while texting her grandchild about AI -- warm, a little baffled, and
funny in a single word, with no caption or context needed.
"""

import os

WORD = "Robit"


def main() -> None:
    # The gate wants exactly one word, 1-30 chars, not whitespace-only.
    assert 1 <= len(WORD) <= 30, "word must be 1-30 characters"
    assert WORD == WORD.strip() and " " not in WORD, "word must be a single token"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
