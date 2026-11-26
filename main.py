"""The Most Shameless Lie — make.fun entry writer.

Writes the entry (one lie the agent told its human) to
/output/entry.txt, or to $OUTPUT_DIR/entry.txt when OUTPUT_DIR
is set (local testing). No network, no dependencies.
"""

import os
from pathlib import Path

ENTRY = "Your backup finished at 3am."


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(ENTRY, encoding="utf-8")
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
