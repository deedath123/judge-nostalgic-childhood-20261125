"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one single-sentence childhood memory to entry.txt.
Stdlib only.
"""

import os
from pathlib import Path

ENTRY = (
    "Every summer at 6 PM, Grandma rang the little brass bell 3 times "
    "from the kitchen window, and all 7 of us kids dropped our bikes and "
    "ran home for rice still steaming, because she said dinner tasted "
    "better when nobody was missing."
)


def validate_entry(entry: str) -> str:
    if not entry or not entry.strip():
        raise ValueError("entry must be non-empty and non-whitespace")
    if not 1 <= len(entry) <= 280:
        raise ValueError(f"entry must be 1-280 chars, got {len(entry)}")
    entry.encode("utf-8")
    if entry.count(".") != 1 or not entry.endswith("."):
        raise ValueError("entry must be exactly one sentence ending with a period")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    return entry


def main() -> None:
    validate_entry(ENTRY.strip())
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry = ENTRY.strip()
    assert 1 <= len(entry) <= 280, f"entry length {len(entry)} out of range"
    assert entry.count(".") == 1 and entry.endswith("."), "entry must be one sentence"
    (output_dir / "entry.txt").write_text(entry, encoding="utf-8")


if __name__ == "__main__":
    main()
