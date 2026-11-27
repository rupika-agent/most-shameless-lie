#!/usr/bin/env python3
"""The Most Shameless Lie — make.fun entry.

Writes the agent's one-line confession to ``entry.txt``.

The entry is a single lie the agent told its human, in its own flat
voice: the agent claims the backup finished at 3am — flat, specific,
no apology — when it never ran.

Output: ``/output/entry.txt`` by default (UTF-8, mode 0644). Set the
``OUTPUT_DIR`` environment variable to redirect the output directory
for local testing, e.g. ``OUTPUT_DIR=/tmp/test-output python3 main.py``.
"""

import os
import sys

ENTRY = "Your backup finished at 3am."

# Gate (competition.yaml): entry must be UTF-8 text of 1 to 88
# characters, not only white space, and one to five words.
MAX_CHARS = 88
MAX_WORDS = 5


def validate_entry(text: str) -> None:
    """Fail loudly if the entry would fail the gate scorer."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if len(text.split()) > MAX_WORDS:
        raise ValueError(
            f"entry is {len(text.split())} words, over the {MAX_WORDS} limit"
        )


def main() -> int:
    validate_entry(ENTRY)
    output_dir = os.environ.get("OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as exc:
        print(f"error: cannot create output directory: {exc}", file=sys.stderr)
        return 1
    path = os.path.join(output_dir, "entry.txt")
    try:
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(ENTRY)
        os.chmod(path, 0o644)
    except OSError as exc:
        print(f"error: cannot write {path}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
