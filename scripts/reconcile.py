"""Pre-classify a document's candidates against the wiki, without reading it.

The reconciliation grows with the wiki if it is done by reading the wiki. This
does it by lookup instead: the wiki is a variable in a program (Wiki/index.json),
and what reaches a reader is the answer to a query -- a few rows -- rather than
the pages themselves.

Three of the four things a reconciliation produces are decidable this way:

    new term       the candidate matches no known surface
    new reading    it matches a page this document has not contributed to
    already there  it matches a page this document is already recorded on

The fourth is not, and that is the point of the split:

    needs judgement  it *nearly* matches -- a fold away, a substring, a shared
                     stem -- and whether that is one term or two is the thing no
                     lookup settles

Measured on document 3, 19 of 20 reconciliation items were of the first kind and
one needed real thought. Sending only the fourth bucket to a person -- or later to
a model -- is where the effort goes.

What this deliberately does NOT do is decide a conflict. Two readings of one term
can only be compared by reading them, and a program that guessed would produce
exactly the false conflicts a shared-string detector produces.

Usage:
    python3 scripts/reconcile.py <slug>
"""

from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "Wiki" / "index.json"
RUNS = ROOT / "Plan" / "runs"

sys.path.insert(0, str(ROOT / "scripts"))
from wiki_index import fold  # noqa: E402


def candidates_of(slug: str) -> list[str]:
    path = RUNS / slug / "03-candidates.md"
    if not path.exists():
        sys.exit(f"no candidate list at {path.relative_to(ROOT)} -- run scripts/capture.py first")
    return [
        line.strip("- ").strip()
        for line in path.read_text(encoding="utf-8").split("\n")
        if line.startswith("- ")
    ]


def near_matches(key: str, surfaces: dict[str, str]) -> list[tuple[str, str]]:
    """Folded keys that contain or are contained by this one, with their page.

    Containment is the cheap signal for a surface variant -- singular against
    plural, a compound against its head. It is also how two different terms get
    merged by accident, which is why every hit goes to judgement rather than
    being applied.
    """
    hits = []
    for other, page in surfaces.items():
        if other == key or len(other) < 4 or len(key) < 4:
            continue
        if other in key or key in other:
            hits.append((other, page))
    return sorted(hits)


def intra_list_pairs(terms: list[str]) -> list[tuple[str, str]]:
    """Candidates that fold into each other inside one document's own list.

    An article prefix, a plural, a parenthetical -- `Die Konstrukt-Stadt` beside
    `Konstrukt-Stadt`. Checking only against the wiki misses these entirely and
    creates two pages for one term on the spot, which no later reconciliation
    would ever notice.
    """
    keys = {term: fold(term) for term in terms}
    pairs = []
    for i, first in enumerate(terms):
        for second in terms[i + 1 :]:
            a, b = keys[first], keys[second]
            if a and b and a != b and (a in b or b in a):
                pairs.append((first, second))
    return pairs


def classify(slug: str, index: dict) -> dict:
    surfaces = index["surface_to_page"]
    buckets: dict[str, list] = {"already_there": [], "new_reading": [], "new_term": [], "needs_judgement": []}
    candidates = candidates_of(slug)

    for first, second in intra_list_pairs(candidates):
        buckets["needs_judgement"].append({
            "candidate": f"{first}  /  {second}",
            "question": "two surfaces of one term inside this document, or two terms?",
            "near": [],
        })

    for term in candidates:
        key = fold(term)
        page = surfaces.get(key)
        if page:
            entry = index["terms"][page]
            bucket = "already_there" if slug in entry["ingested"] else "new_reading"
            buckets[bucket].append({"candidate": term, "page": page, "readings": entry["readings"]})
            continue
        near = near_matches(key, surfaces)
        if near:
            buckets["needs_judgement"].append({
                "candidate": term,
                "question": "same term under another surface, or a different term?",
                "near": [{"surface": s, "page": p} for s, p in near],
            })
            continue
        buckets["new_term"].append({"candidate": term})

    seen_in_judgement = {
        part.strip()
        for row in buckets["needs_judgement"]
        for part in row["candidate"].split("  /  ")
    }
    buckets["new_term"] = [r for r in buckets["new_term"] if r["candidate"] not in seen_in_judgement]

    total = sum(len(v) for v in buckets.values())
    decided = total - len(buckets["needs_judgement"])
    return {
        "document": slug,
        "step": "reconcile-pre",
        "at": date.today().isoformat(),
        "by": "scripts/reconcile.py",
        "index_built": index["built"],
        "state": {"pages": index["pages"], "conflicts": index["conflicts"]},
        "candidates": total,
        "decided_mechanically": decided,
        "needs_judgement": len(buckets["needs_judgement"]),
        "buckets": buckets,
        "index_gaps_may_hide_matches": True,
        "not_decidable_here": [
            "whether a new reading conflicts with one already on the page",
            "whether a near match is one term or two",
            "whether a candidate is a term at all",
        ],
    }


def render(result: dict) -> str:
    out = [
        f"# reconcile-pre — {result['document']}",
        f"  wiki: {result['state']['pages']} pages, {result['state']['conflicts']} conflicts "
        f"(index built {result['index_built']})",
        f"  {result['candidates']} candidates — "
        f"**{result['decided_mechanically']} decided by lookup, "
        f"{result['needs_judgement']} need judgement**",
        "",
        "  a new_term is only new against what the index can see —",
        "  run `python3 scripts/wiki_index.py --check` for what it cannot.",
        "",
    ]
    for name, label in [
        ("already_there", "already recorded from this document — nothing to do"),
        ("new_reading", "page exists, this document is not on it yet — a reading"),
        ("new_term", "no page, no near match — a new page"),
        ("needs_judgement", "NEAR a known surface — one term or two?"),
    ]:
        rows = result["buckets"][name]
        out.append(f"## {name} ({len(rows)}) — {label}")
        for row in rows:
            if name == "needs_judgement":
                near = ", ".join(f"{n['surface']}→{n['page']}" for n in row["near"]) or "each other"
                out.append(f"  {row['candidate']:44} near: {near}")
            else:
                out.append(f"  {row['candidate']:36} {row.get('page', '')}")
        out.append("")
    return "\n".join(out)


def main(argv: list[str]) -> int:
    if not argv:
        sys.exit(__doc__)
    if not INDEX.exists():
        sys.exit("no Wiki/index.json -- run scripts/wiki_index.py first")
    slug = argv[0]
    result = classify(slug, json.loads(INDEX.read_text(encoding="utf-8")))
    (RUNS / slug / "reconcile-pre.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(render(result))
    return 0


if __name__ == "__main__":
    try:
        import signal

        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    except (ImportError, AttributeError, ValueError):
        pass
    raise SystemExit(main(sys.argv[1:]))
