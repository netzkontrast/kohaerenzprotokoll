"""Apply every rule to every document, once, and never again until something changes.

Documents are immutable -- `Sources/drive/**` is write-denied and every row carries
a `sha256`. So a derived fact stays true until either the document changes (it
will not) or the rule that produced it changes (it will, constantly).

That makes the cache key `(sha256, rule version)` and the invalidation exact:
bump a rule's VERSION and only that rule re-runs, on every document; add a rule
and only the new rule runs. Nothing re-reads a document to answer a question that
was already answered.

    python3 scripts/derive.py              # bring the cache up to date
    python3 scripts/derive.py --stale      # what would re-run, and why
    python3 scripts/derive.py --force      # ignore the cache

Exceptions live in Plan/rules/exceptions.jsonl, one object per
(document, rule, reason). A rule skipped by an exception is reported on every run
-- a document that does not fit is a question, not a silent gap.
"""

from __future__ import annotations

import json
import sys
import time
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCEPTIONS = ROOT / "Plan" / "rules" / "exceptions.jsonl"

sys.path.insert(0, str(ROOT / "scripts"))
import subject  # noqa: E402
from rules import load  # noqa: E402
from subject import DERIVED  # noqa: E402


def documents() -> list[dict]:
    """Every landed document as a plain dict, from the one place that finds them."""
    return [
        {"slug": d.slug, "category": d.category, "date": d.date, "format": d.format,
         "sha256": d.sha256, "path": str(d.path), "body": d.body, "offset": d.offset}
        for d in subject.documents()
    ]


def exceptions() -> dict[tuple[str, str], str]:
    """(document, rule) -> reason. A skip nobody can see is a skip nobody fixes."""
    if not EXCEPTIONS.exists():
        return {}
    return {(row["document"], row["rule"]): row.get("reason", "no reason recorded")
            for row in subject.read_jsonl(EXCEPTIONS)}


def stale_reason(cached: dict, doc: dict, rule) -> str | None:
    """Why this rule must run for this document, or None if it need not."""
    entry = cached.get(rule.NAME)
    if entry is None:
        return "not derived yet"
    if entry.get("version") != rule.VERSION:
        return f"rule version {entry.get('version')} -> {rule.VERSION}"
    if entry.get("sha256") != doc["sha256"]:
        return "document checksum changed"
    return None


def run(force: bool = False, dry: bool = False) -> dict:
    rules = load()
    skips = exceptions()
    counts = defaultdict(int)
    plan = []
    started = time.time()

    for doc in documents():
        cached = subject.derived(doc["slug"])
        changed = False
        for rule in rules:
            key = (doc["slug"], rule.NAME)
            if key in skips:
                counts["excepted"] += 1
                continue
            if not rule.applies(doc):
                counts["out_of_scope"] += 1
                continue
            reason = "forced" if force else stale_reason(cached, doc, rule)
            if reason is None:
                counts["cached"] += 1
                continue
            counts["derived"] += 1
            plan.append((doc["slug"], rule.NAME, reason))
            if not dry:
                cached[rule.NAME] = {
                    "version": rule.VERSION,
                    "sha256": doc["sha256"],
                    "facts": rule.derive(doc),
                }
                changed = True
        if changed and not dry:
            DERIVED.mkdir(parents=True, exist_ok=True)
            (DERIVED / f"{doc['slug']}.json").write_text(
                json.dumps(cached, ensure_ascii=False, separators=(",", ":")) + "\n",
                encoding="utf-8",
            )

    return {"counts": dict(counts), "plan": plan, "seconds": round(time.time() - started, 2),
            "rules": [(r.NAME, r.VERSION) for r in rules], "exceptions": skips}


def main(argv: list[str]) -> int:
    dry = "--stale" in argv
    result = run(force="--force" in argv, dry=dry)
    counts = result["counts"]
    print("rules: " + ", ".join(f"{n}@{v}" for n, v in result["rules"]))
    if result["exceptions"]:
        print(f"\n{len(result['exceptions'])} exceptions, honoured and reported:")
        for (slug, rule), reason in result["exceptions"].items():
            print(f"  {rule:16} {slug[:44]:46} {reason}")
    if dry and result["plan"]:
        print(f"\n{len(result['plan'])} derivations would run:")
        by_reason = defaultdict(int)
        for _, rule, reason in result["plan"]:
            by_reason[(rule, reason)] += 1
        for (rule, reason), n in sorted(by_reason.items()):
            print(f"  {n:4} x {rule:16} {reason}")
    print(f"\n{'would derive' if dry else 'derived'} {counts.get('derived', 0)}, "
          f"reused {counts.get('cached', 0)}, "
          f"excepted {counts.get('excepted', 0)}, "
          f"out of scope {counts.get('out_of_scope', 0)}"
          f"  —  {result['seconds']}s")
    return 0


if __name__ == "__main__":
    subject.cli(main)
