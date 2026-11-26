"""Rejected Olympic Sports — make.fun entry.

Writes one funny single-line sport the Olympics turned down to
<MAKEFUN_OUTPUT_DIR>/entry.txt (or /output/entry.txt by default).
"""

import os

ENTRY = (
    "Competitive Queueing: athletes stand in a single file for six hours; "
    "gold goes to whoever reaches the front without once asking "
    "what the queue is for."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-200")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in ENTRY):
        raise SystemExit("entry must not contain control characters")
    if not ENTRY.strip():
        raise SystemExit("entry must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
