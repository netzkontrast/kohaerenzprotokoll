#!/usr/bin/env python3
"""Build the raw-source manifest from the Google-Drive index (Phase A, deterministic).

    python3 scripts/source_inventory.py            # write Sources/manifest.jsonl
    python3 scripts/source_inventory.py --stats    # print counts only
    python3 scripts/source_inventory.py --check    # exit 1 when the manifest is stale

Reads ``Plan/research/koharenz-protokoll_google-drive-quellenindex_2026-09-15.md``
(one bullet per document: title, Drive id, date, optional "N Kopien") and writes
one JSON line per document with a stable slug, the category (index section),
the deterministic tier (T4 for the appendix, T3/T2 by section, T0 for byte-equal
copies the index reports), and empty export fields the fetch step fills in
(``export_path``, ``sha256``, ``exported_at``). No LLM, no network.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "Plan/research/koharenz-protokoll_google-drive-quellenindex_2026-09-15.md"
MANIFEST = ROOT / "Sources/manifest.jsonl"

ENTRY = re.compile(
    r"^- \[(?P<title>.+?)\]\(https://drive\.google\.com/open\?id=(?P<id>[\w-]+)\)"
    r" · (?P<date>\d{4}-\d{2}-\d{2})(?: · (?P<copies>\d+) Kopien)?\s*$"
)
SECTION = re.compile(r"^## (?P<name>.+?)\s*$")

# Index section → (category enum of tools/kpwiki/schema.py, deterministic tier)
CATEGORIES = {
    "Kernkonzept": ("kernkonzept", "T3-work"),
    "Plot, Outline": ("plot-outline", "T3-work"),
    "Charaktere": ("charaktere", "T3-work"),
    "Worldbuilding": ("worldbuilding", "T3-work"),
    "Dramatica": ("storyform", "T3-work"),
    "Audits": ("audit", "T3-work"),
    "Theorie — Mathematik": ("theorie-mathematik", "T2-theory"),
    "Theorie — Logik": ("theorie-logik", "T2-theory"),
    "Theorie — Physik": ("theorie-physik", "T2-theory"),
    "Theorie — Psychologie": ("theorie-psychologie", "T2-theory"),
    "Theorie — Philosophie": ("theorie-philosophie", "T2-theory"),
    "Theorie — Genre": ("theorie-genre", "T2-theory"),
    "AEGIS": ("aegis", "T3-work"),
    "Anhang": ("unzugeordnet", "T4-out-of-scope"),
}
SLUG_MAX = 60


def slugify(title: str) -> str:
    """ASCII, lowercase, hyphenated; German umlauts transliterated."""
    text = title.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return text[:SLUG_MAX].rstrip("-") or "untitled"


def category_for(section: str) -> tuple[str, str]:
    for prefix, mapping in CATEGORIES.items():
        if section.startswith(prefix):
            return mapping
    return ("unzugeordnet", "T4-out-of-scope")


def guess_format(title: str) -> str:
    match = re.search(r"\.(md|docx|pdf|mp3|txt)$", title, re.IGNORECASE)
    return match.group(1).lower() if match else "gdoc"


def parse_index(text: str) -> list[dict]:
    """Return one record per index bullet, in index order."""
    records: list[dict] = []
    section = ""
    for line in text.splitlines():
        heading = SECTION.match(line)
        if heading:
            section = heading.group("name")
            continue
        entry = ENTRY.match(line)
        if not entry:
            continue
        category, tier = category_for(section)
        records.append(make_record(entry, section, category, tier))
    return records


def make_record(entry: re.Match, section: str, category: str, tier: str) -> dict:
    title = entry.group("title")
    return {
        "drive_id": entry.group("id"),
        "title": title,
        "slug": slugify(title),
        "index_section": section,
        "category": category,
        "tier": tier,
        "format": guess_format(title),
        "index_date": entry.group("date"),
        "byte_equal_copies": int(entry.group("copies") or 0),
        "export_path": "",
        "sha256": "",
        "exported_at": "",
        "duplicate_of": "",
    }


def disambiguate_slugs(records: list[dict]) -> None:
    """Make slugs unique in index order; a suffix is only used if no record owns it.

    Checked against the full set of base slugs too, so a title whose own slug
    is ``foo-2`` never collides with the second ``foo``.
    """
    taken: set[str] = {rec["slug"] for rec in records}
    assigned: set[str] = set()
    for rec in records:
        base = rec["slug"]
        if base not in assigned:
            assigned.add(base)
            continue
        n = 2
        while f"{base}-{n}" in taken or f"{base}-{n}" in assigned:
            n += 1
        rec["slug"] = f"{base}-{n}"
        assigned.add(rec["slug"])


def render(records: list[dict]) -> str:
    return "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records)


def stats(records: list[dict]) -> str:
    lines = [f"documents: {len(records)}"]
    for key in ("tier", "category", "format"):
        counts: dict[str, int] = {}
        for rec in records:
            counts[rec[key]] = counts.get(rec[key], 0) + 1
        lines.append(f"{key}: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    lines.append(f"byte-equal copies reported by the index: {sum(r['byte_equal_copies'] for r in records)}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stats", action="store_true", help="print counts, write nothing")
    parser.add_argument("--check", action="store_true", help="exit 1 when Sources/manifest.jsonl is stale")
    args = parser.parse_args(argv)
    records = parse_index(INDEX.read_text(encoding="utf-8"))
    disambiguate_slugs(records)
    if args.stats:
        print(stats(records))
        return 0
    rendered = render(records)
    if args.check:
        current = MANIFEST.read_text(encoding="utf-8") if MANIFEST.is_file() else ""
        print("manifest up to date" if current == rendered else "manifest STALE — run scripts/source_inventory.py")
        return 0 if current == rendered else 1
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(rendered, encoding="utf-8")
    print(f"wrote {MANIFEST.relative_to(ROOT)}\n{stats(records)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
