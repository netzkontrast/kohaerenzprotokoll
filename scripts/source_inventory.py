#!/usr/bin/env python3
"""Build the raw-source manifest from the Google-Drive index (Phase A, deterministic).

    python3 scripts/source_inventory.py            # write Sources/manifest.jsonl
    python3 scripts/source_inventory.py --stats    # print counts only
    python3 scripts/source_inventory.py --check    # exit 1 when the manifest is stale
    python3 scripts/source_inventory.py --include-out-of-scope   # keep the appendix rows

Reads ``Plan/research/koharenz-protokoll_google-drive-quellenindex_2026-09-15.md``
(693 bullets: title, Drive id, date, optional "N Kopien") and writes one JSON
line per document with a stable slug, the category (index section), the
deterministic tier (T3/T2 by section) and empty export fields the fetch step
fills in (``export_path``, ``sha256``, ``exported_at``, ``truncated``) or the
dedup step sets (``duplicate_of``, ``superseded_by``, tiers T0/T1). No LLM,
no network.

D-W9: the 13 appendix rows (tier ``T4-out-of-scope``) are dropped from the
manifest by default, so it carries 680 records. Slugs are disambiguated over
the full 693-row list *before* the drop, so surviving ids never change.

The export and dedup fields of an existing manifest are carried over by
``drive_id`` on every rebuild: the index owns title/slug/category/tier,
the fetch step owns the export fields, ``scripts/source_dedup.py`` owns
the T0/T1 tiers and the ``duplicate_of`` / ``superseded_by`` links.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from tools.kpwiki import wiki_schema  # noqa: E402

INDEX = ROOT / "Plan/research/koharenz-protokoll_google-drive-quellenindex_2026-09-15.md"
MANIFEST = ROOT / "Sources/manifest.jsonl"
# Filled by the fetch step and scripts/source_dedup.py, never by the index.
EXPORT_FIELDS = ("export_path", "sha256", "exported_at", "duplicate_of", "superseded_by", "truncated")

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
# D-W9: the appendix tier is dropped from the manifest unless asked for.
OUT_OF_SCOPE_TIER = CATEGORIES["Anhang"][1]
# Tiers the index can never assign belong to the dedup step (T0/T1) and survive a rebuild.
DEDUP_TIERS = frozenset(wiki_schema.enum_values("tier")) - {tier for _, tier in CATEGORIES.values()}
SLUG_MAX = 60
# Some Drive documents carry their first paragraph as title; the index copied
# them verbatim (up to ~9.5k chars). The manifest keeps a title, not a body.
TITLE_MAX = 160


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


def clip_title(title: str) -> tuple[str, bool]:
    """Return (title, truncated); long first-paragraph titles are cut at TITLE_MAX."""
    if len(title) <= TITLE_MAX:
        return title, False
    return title[:TITLE_MAX].rstrip() + "…", True


def make_record(entry: re.Match, section: str, category: str, tier: str) -> dict:
    title, truncated = clip_title(entry.group("title"))
    return {
        "drive_id": entry.group("id"),
        "title": title,
        "title_truncated": truncated,
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
        "superseded_by": "",
        "truncated": False,
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
        while _suffixed(base, n) in taken or _suffixed(base, n) in assigned:
            n += 1
        rec["slug"] = _suffixed(base, n)
        assigned.add(rec["slug"])


def _suffixed(base: str, n: int) -> str:
    """``base-n`` trimmed so the result never exceeds SLUG_MAX."""
    suffix = f"-{n}"
    return base[: SLUG_MAX - len(suffix)].rstrip("-") + suffix


def select_in_scope(records: list[dict], include_out_of_scope: bool) -> list[dict]:
    """D-W9: drop the appendix rows; call only after :func:`disambiguate_slugs`."""
    if include_out_of_scope:
        return list(records)
    return [rec for rec in records if rec["tier"] != OUT_OF_SCOPE_TIER]


def load_manifest(path: Path) -> list[dict]:
    """Records of an existing manifest (empty when the file is absent)."""
    if not path.is_file():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def carry_over_export_state(records: list[dict], existing: list[dict]) -> None:
    """Keep what the fetch and dedup steps wrote: export fields and T0/T1 tiers, by drive_id."""
    by_id = {rec["drive_id"]: rec for rec in existing}
    for rec in records:
        old = by_id.get(rec["drive_id"])
        if old is None:
            continue
        for field in EXPORT_FIELDS:
            if field in old:
                rec[field] = old[field]
        if old.get("tier") in DEDUP_TIERS:
            rec["tier"] = old["tier"]


def validate_mapping() -> None:
    """Fail loudly when the section table drifts from Wiki/schema/entities.yaml."""
    categories = set(wiki_schema.enum_values("category"))
    tiers = set(wiki_schema.enum_values("tier"))
    unknown = [pair for pair in CATEGORIES.values() if pair[0] not in categories or pair[1] not in tiers]
    if unknown:
        raise SystemExit(f"CATEGORIES not in Wiki/schema/entities.yaml enums: {unknown}")


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
    parser.add_argument("--include-out-of-scope", action="store_true",
                        help="keep the T4-out-of-scope appendix rows (dropped by default, D-W9)")
    args = parser.parse_args(argv)
    validate_mapping()
    all_records = parse_index(INDEX.read_text(encoding="utf-8"))
    disambiguate_slugs(all_records)
    records = select_in_scope(all_records, args.include_out_of_scope)
    carry_over_export_state(records, load_manifest(MANIFEST))
    if args.stats:
        print(stats(records))
        print(f"dropped as {OUT_OF_SCOPE_TIER} (D-W9): {len(all_records) - len(records)}")
        return 0
    rendered = render(records)
    if args.check:
        current = MANIFEST.read_text(encoding="utf-8") if MANIFEST.is_file() else ""
        print("manifest up to date" if current == rendered else "manifest STALE — run scripts/source_inventory.py")
        return 0 if current == rendered else 1
    write_atomic(MANIFEST, rendered)
    print(f"wrote {MANIFEST.relative_to(ROOT)}\n{stats(records)}")
    return 0


def write_atomic(target: Path, text: str) -> None:
    """Write via a sibling temp file + rename so readers never see a partial manifest."""
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_name(target.name + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, target)


if __name__ == "__main__":
    sys.exit(main())
