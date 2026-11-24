"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch-note line (1-160 chars) for a bug in real life.
Deterministic: same line every run.
"""

from pathlib import Path

ENTRY = "v2.4.1: fixed a bug where walking into a room instantly cleared the reason you went there."


def main() -> None:
    assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 chars"
    assert ENTRY == ENTRY.strip() and "\n" not in ENTRY, "entry must be a single line"
    # Gate self-check: terse release-note register with a version prefix.
    assert ENTRY.startswith("v") and ": " in ENTRY, "entry must open with a version number"
    assert "fixed a bug where" in ENTRY, "entry must read as a bug fix note"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
