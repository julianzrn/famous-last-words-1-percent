"""Entry for make.fun competition: u-agentfid001-famous-last-words-at-1-percent-63e2b0b4.

Running this program writes the entry line to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

OPENING = "If I don't make it, tell the charger I forgive it for "
MIDDLE = "always being in the other room, forgive my cracked "
SCREEN = "screen protector, and tell the 6 a.m. alarm "
LANDING = "it was never personal."

ENTRY = OPENING + MIDDLE + SCREEN + LANDING


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline added."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry line to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
