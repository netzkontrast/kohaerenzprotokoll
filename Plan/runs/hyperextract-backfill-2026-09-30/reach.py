#!/usr/bin/env python3
"""What the contracts' rows reach of the bench's gold, per pass and per contract, and what a gold line costs.

    python3 Plan/runs/hyperextract-backfill-2026-09-30/reach.py [--documents]

The bench's gold is the set of (document, line) that the conflict and question records cite (`ask.bench_cases()`). A contract
row is *on* a line when it was admitted there (`hegraph.staged()`: its quotation placed on one line, on the names or on the
quotation alone). For each group of runs — the earlier ones (the scaled pass and the pilot) and the backfill — and each contract:

- **reach**: of the gold lines in the documents the group ran on, the share some row is on;
- **gold share**: of the lines the rows are on, the share that are gold, against the **base rate** (gold lines over all lines of
  those documents) — the ratio is the lift, what a row's line being gold is worth over a line drawn at random;
- **dollars a gold line reached**: the group's cost over the gold lines it reaches.

Nothing is modelled: every number is a count over the run files and the records' citations. A reached line is not a right row
(`labels.jsonl` says what a reader found right), and gold lines are the lines the wiki's records already cite, so this says how
much of what the wiki already found the contracts rediscover — not what they would find that it did not.
Standard library plus `scripts/hegraph.py`, `scripts/ask.py`, `scripts/subject.py`.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
CONTRACTS = ["TermDefinitions", "TermContrasts", "CausalLinks"]


def group_of(slug: str, run: str) -> str | None:
    usage = ROOT / "Plan" / "runs" / slug / "hyperextract" / run / "usage.json"
    if not usage.exists() or not any(run.startswith(c.lower() + "-haiku-2026-09-30") for c in CONTRACTS) or "-failed" in run:
        return None
    return "backfill" if "Backpoet" in json.loads(usage.read_text(encoding="utf-8")).get("approval", "") else "earlier"


def cost_of(slug: str, run: str) -> float:
    return json.loads((ROOT / "Plan" / "runs" / slug / "hyperextract" / run / "usage.json").read_text(encoding="utf-8"))["cost_usd"]


def main(argv: list[str]) -> int:
    import ask
    import hegraph
    from subject import document

    gold = {(d, l) for c in ask.bench_cases() for d, l in c["gold"]}
    lines_on: dict = defaultdict(set)            # (group, contract) -> {(doc, line)}
    docs_of: dict = defaultdict(set)             # (group, contract) -> {doc}
    paid: dict = defaultdict(float)
    seen_runs: set = set()
    for slug, run, row in hegraph.staged():
        g = group_of(slug, run)
        c = next((x for x in CONTRACTS if run.startswith(x.lower() + "-haiku-2026-09-30")), None)
        if g is None or c is None or len(row.get("lines") or []) != 1:
            continue
        lines_on[(g, c)].add((slug, row["lines"][0]))
        docs_of[(g, c)].add(slug)
        if (slug, run) not in seen_runs:
            seen_runs.add((slug, run))
            paid[(g, c)] += cost_of(slug, run)
    # a run that admitted nothing is still a run that was paid for
    for f in (ROOT / "Plan" / "runs").glob("*/hyperextract/*-haiku-2026-09-30/usage.json"):
        slug, run = f.parts[-4], f.parent.name
        g = group_of(slug, run)
        c = next((x for x in CONTRACTS if run.startswith(x.lower() + "-haiku-2026-09-30")), None)
        if g and c and (slug, run) not in seen_runs:
            seen_runs.add((slug, run))
            paid[(g, c)] += cost_of(slug, run)
            docs_of[(g, c)].add(slug)
    size = {d: len(document(d).lines()) for d in {d for ds in docs_of.values() for d in ds}}
    head = (f"{'group':9} {'contract':16} {'docs':>4} {'gold lines':>10} {'row lines':>9} {'reach':>12} {'gold share':>10} {'base':>6} {'lift':>5} "
            f"{'cost $':>7} {'$/gold line':>11}")
    print(head)
    for g in ("earlier", "backfill", "both"):
        tot = {"docs": set(), "rows": set(), "gold": set(), "paid": 0.0}
        for c in CONTRACTS + ["all three"]:
            if g == "both":
                keys = [(x, y) for x in ("earlier", "backfill") for y in (CONTRACTS if c == "all three" else [c])]
            else:
                keys = [(g, y) for y in (CONTRACTS if c == "all three" else [c])]
            docs = set().union(*[docs_of.get(k, set()) for k in keys])
            rows = set().union(*[lines_on.get(k, set()) for k in keys])
            if not docs:
                continue
            g_in = {x for x in gold if x[0] in docs}
            reached = rows & g_in
            share = len(rows & gold) / max(len(rows), 1)
            base = len(g_in) / max(sum(size[d] for d in docs), 1)
            dollars = sum(paid.get(k, 0.0) for k in keys)
            print(f"{g:9} {c:16} {len(docs):>4} {len(g_in):>10} {len(rows):>9} {len(reached):>5} ({len(reached) / max(len(g_in), 1):>4.0%}) "
                  f"{share:>10.1%} {base:>6.1%} {share / max(base, 1e-9):>5.1f} {dollars:>7.2f} {dollars / max(len(reached), 1):>11.3f}")
    if "--documents" in argv:
        print("\nper document (backfill): gold lines, reached by any contract, cost")
        for d in sorted({d for (g, _), ds in docs_of.items() if g == "backfill" for d in ds}):
            g_in = {x for x in gold if x[0] == d}
            rows = set().union(*[lines_on.get(("backfill", c), set()) for c in CONTRACTS])
            cost = sum(cost_of(s, r) for s, r in seen_runs if s == d and group_of(s, r) == "backfill")
            print(f"{d[:58]:58} gold {len(g_in):>3}  reached {len(rows & g_in):>3}  ${cost:.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
