"""Roast the Smart Fridge entry.

Writes a single one-line roast of a smart fridge to /output/entry.txt.
Deterministic, offline, standard library only.
"""

import os

ENTRY = (
    "My fridge auto-ordered $86 of kale, then locked the crisper and "
    "left a note: 'You bought me to eat better. I bought this to watch you try.'"
)


def main():
    # Gate: the entry must be 1-160 characters of non-whitespace UTF-8 text.
    assert 1 <= len(ENTRY) <= 160, "entry length %d out of gate" % len(ENTRY)
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
