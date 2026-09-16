#!/usr/bin/env python3
"""Mark byte-equal and superseded exports in Sources/manifest.jsonl (Phase A, deterministic).

    python3 scripts/source_dedup.py             # rewrite the manifest in place
    python3 scripts/source_dedup.py --dry-run   # print the planned changes, write nothing
    python3 scripts/source_dedup.py --check     # exit 1 when the manifest would change
    python3 scripts/source_dedup.py --stats     # exported / duplicate / superseded counts
    python3 scripts/source_dedup.py --root DIR  # another tree (tests)

Only records whose ``export_path`` is set, whose file exists and whose
``truncated`` flag is false are hashed (a truncated export is re-fetched, never
compared). Two rules, both over the file contents:

* byte-equal (same sha256): the newer record — ordered by ``index_date``, then
  ``slug`` — gets ``tier: T0-duplicate`` and ``duplicate_of: <earliest slug>``;
* near-duplicate (8-word shingle Jaccard >= 0.8) or the same normalised
  title, in both cases with a strictly newer ``index_date``: the OLDER record
  gets ``tier: T1-superseded`` and ``superseded_by: <nearest newer slug>``, so
  a chain of drafts reads oldest -> newest. Records with the same date are
  never ordered against each other by this rule.

The tier names come from ``Wiki/schema/entities.yaml``. Records that are not
exported are left untouched, the run is idempotent, and the manifest is written
atomically. No LLM, no network.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import unicodedata
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from tools.kpwiki import wiki_schema  # noqa: E402

MANIFEST_RELATIVE = Path("Sources/manifest.jsonl")
SHINGLE_WORDS = 8
JACCARD_THRESHOLD = 0.8
WORD = re.compile(r"\w+", re.UNICODE)


def tier_named(prefix: str) -> str:
    """The schema tier starting with ``prefix`` (``T0`` -> ``T0-duplicate``)."""
    matches = [tier for tier in wiki_schema.enum_values("tier") if tier.startswith(prefix + "-")]
    if len(matches) != 1:
        raise SystemExit(f"Wiki/schema/entities.yaml has no single tier {prefix}-*: {matches}")
    return matches[0]


DUPLICATE_TIER = tier_named("T0")
SUPERSEDED_TIER = tier_named("T1")


def load_manifest(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def render(records: list[dict]) -> str:
    return "".join(json.dumps(rec, ensure_ascii=False) + "\n" for rec in records)


def write_atomic(target: Path, text: str) -> None:
    tmp = target.with_name(target.name + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, target)


def exported_records(records: list[dict], root: Path) -> list[dict]:
    """Records whose export exists on disk and is not truncated."""
    return [rec for rec in records
            if rec.get("export_path") and not rec.get("truncated") and (root / rec["export_path"]).is_file()]


def order_key(rec: dict) -> tuple[str, str]:
    return (rec.get("index_date", ""), rec["slug"])


def normalise_title(title: str) -> str:
    text = unicodedata.normalize("NFKC", title).lower()
    return " ".join(WORD.findall(text))


def shingles(text: str) -> frozenset[tuple[str, ...]]:
    words = WORD.findall(text.lower())
    if len(words) <= SHINGLE_WORDS:
        return frozenset({tuple(words)}) if words else frozenset()
    return frozenset(tuple(words[i:i + SHINGLE_WORDS]) for i in range(len(words) - SHINGLE_WORDS + 1))


def jaccard(a: frozenset, b: frozenset) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def could_reach_threshold(a: frozenset, b: frozenset) -> bool:
    """Jaccard is bounded by min/max set size, so unequal sizes are skipped cheaply."""
    if not a or not b:
        return False
    return min(len(a), len(b)) / max(len(a), len(b)) >= JACCARD_THRESHOLD


def byte_equal_plan(exported: list[dict], root: Path) -> dict[str, str]:
    """slug -> earliest slug with the same sha256 (the earliest record is absent)."""
    groups: dict[str, list[dict]] = {}
    for rec in exported:
        digest = hashlib.sha256((root / rec["export_path"]).read_bytes()).hexdigest()
        groups.setdefault(digest, []).append(rec)
    plan: dict[str, str] = {}
    for members in groups.values():
        members.sort(key=order_key)
        for rec in members[1:]:
            plan[rec["slug"]] = members[0]["slug"]
    return plan


def superseded_plan(candidates: list[dict], root: Path) -> dict[str, str]:
    """slug -> slug of the nearest strictly newer near-duplicate or same-title record."""
    ordered = sorted(candidates, key=order_key)
    text = {rec["slug"]: shingles((root / rec["export_path"]).read_text(encoding="utf-8", errors="replace"))
            for rec in ordered}
    plan: dict[str, str] = {}
    for older, newer in combinations(ordered, 2):
        if older["slug"] in plan or older.get("index_date", "") >= newer.get("index_date", ""):
            continue
        if related(older, newer, text):
            plan[older["slug"]] = newer["slug"]
    return plan


def related(older: dict, newer: dict, text: dict[str, frozenset]) -> bool:
    if normalise_title(older["title"]) == normalise_title(newer["title"]):
        return True
    a, b = text[older["slug"]], text[newer["slug"]]
    return could_reach_threshold(a, b) and jaccard(a, b) >= JACCARD_THRESHOLD


def apply_plan(records: list[dict], duplicates: dict[str, str], superseded: dict[str, str]) -> list[str]:
    """Mutate records in place; returns one line per changed record."""
    changes: list[str] = []
    for rec in records:
        before = (rec["tier"], rec.get("duplicate_of", ""), rec.get("superseded_by", ""))
        if rec["slug"] in duplicates:
            rec["tier"], rec["duplicate_of"] = DUPLICATE_TIER, duplicates[rec["slug"]]
        elif rec["slug"] in superseded:
            rec["tier"], rec["superseded_by"] = SUPERSEDED_TIER, superseded[rec["slug"]]
        after = (rec["tier"], rec.get("duplicate_of", ""), rec.get("superseded_by", ""))
        if before != after:
            changes.append(f"{rec['slug']}: {before[0]} -> {after[0]}"
                           + (f" duplicate_of={after[1]}" if after[1] else "")
                           + (f" superseded_by={after[2]}" if after[2] else ""))
    return changes


def plan_for(records: list[dict], root: Path) -> tuple[dict[str, str], dict[str, str], int]:
    """(duplicates, superseded, exported count) computed from disk ground truth."""
    exported = exported_records(records, root)
    duplicates = byte_equal_plan(exported, root)
    candidates = [rec for rec in exported if rec["slug"] not in duplicates]
    return duplicates, superseded_plan(candidates, root), len(exported)


def stats_lines(records: list[dict], exported_count: int) -> list[str]:
    tiers: dict[str, int] = {}
    for rec in records:
        tiers[rec["tier"]] = tiers.get(rec["tier"], 0) + 1
    return [f"records: {len(records)}", f"exported files: {exported_count}",
            f"{DUPLICATE_TIER}: {tiers.get(DUPLICATE_TIER, 0)}",
            f"{SUPERSEDED_TIER}: {tiers.get(SUPERSEDED_TIER, 0)}",
            "tiers: " + ", ".join(f"{k}={v}" for k, v in sorted(tiers.items()))]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root (default: this repo)")
    parser.add_argument("--dry-run", action="store_true", help="print planned changes, write nothing")
    parser.add_argument("--check", action="store_true", help="exit 1 when the manifest would change")
    parser.add_argument("--stats", action="store_true", help="print counts, write nothing")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    manifest = root / MANIFEST_RELATIVE
    if not manifest.is_file():
        print(f"no manifest at {manifest}")
        return 2
    records = load_manifest(manifest)
    duplicates, superseded, exported_count = plan_for(records, root)
    changes = apply_plan(records, duplicates, superseded)
    print(f"{exported_count} exported files hashed; {len(changes)} record(s) would change")
    for line in changes:
        print("  " + line)
    if args.stats:
        print("\n".join(stats_lines(records, exported_count)))
        return 0
    if args.check:
        print("manifest up to date" if not changes else "manifest STALE — run scripts/source_dedup.py")
        return 0 if not changes else 1
    if args.dry_run or not changes:
        return 0
    write_atomic(manifest, render(records))
    print(f"wrote {manifest.relative_to(root)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
