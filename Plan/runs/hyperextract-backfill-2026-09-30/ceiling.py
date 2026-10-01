#!/usr/bin/env python3
"""How much could the rest of the backfill still add to the `he-lines` finder? The ceiling, from the bench's own packs.

    .venv-graphqlite/bin/python Plan/runs/hyperextract-backfill-2026-09-30/ceiling.py [--lines 40]

For each of the bench's labelled cases, builds the pack twice — the default finders, and with `he-lines` at N lines — and sorts
the case's gold documents into four sets:

- **found by the default**: already in the default pack, nothing for `he-lines` to add;
- **recovered**: missing from the default pack, in the `he-lines` pack — what the finder earns;
- **missed, contracts have read it**: in neither pack although a contract run covers the document — more runs cannot help, the
  finder's ranking or its seeds did not reach the gold line there;
- **missed, no contract has read it**: in neither pack and no run covers it — the only gold documents more runs could even try
  to reach. A case's *ceiling* is the document recall it would score if every one of these were recovered.

Mean document recall is over cases, as `ask.py bench` computes it. The ceiling is an upper bound the finder does not come near:
a contract row must also be about the question's seed pages and rank into N lines. Needs the store (`kg.py index`) and its
interpreter. Standard library plus `scripts/ask.py`, `scripts/askdb.py`, `scripts/graph.py`, `scripts/graphrag.py`.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
CONTRACTS = ("termdefinitions", "termcontrasts", "causallinks")


def covered_documents() -> dict[str, str]:
    """Document -> which pass read it ('earlier', 'backfill' or both), for every document a contract run covers."""
    out: dict[str, set] = {}
    for f in (ROOT / "Plan" / "runs").glob("*/hyperextract/*-haiku-2026-09-30/usage.json"):
        run = f.parent.name
        if "-failed" in run or not run.startswith(CONTRACTS):
            continue
        u = json.loads(f.read_text(encoding="utf-8"))
        out.setdefault(f.parts[-4], set()).add("backfill" if "Backpoet" in u.get("approval", "") else "earlier")
    return {d: "+".join(sorted(v)) for d, v in out.items()}


def main(argv: list[str]) -> int:
    import ask
    import askdb
    import graph as kg
    import graphrag

    lines = int(argv[argv.index("--lines") + 1]) if "--lines" in argv else 40
    covered = covered_documents()
    s, g = askdb.Store(), kg.build()
    ask.HE_LINES = lines
    base = tuple(ask.DEFAULT_FINDERS)
    tot = {"cases": 0, "default": 0.0, "he": 0.0, "ceiling": 0.0, "found": 0, "recovered": 0, "read_missed": 0, "unread_missed": 0, "gold_docs": 0}
    by_pass: dict[str, int] = {}
    listed: list[tuple[str, str, str]] = []
    print(f"{'case':5} {'gold docs':>9} {'default':>8} {'+he-lines':>9} {'recovered':>9} {'missed, read':>12} {'missed, unread':>14} {'ceiling':>8}")
    for c in ask.bench_cases():
        if not c["gold"]:
            continue
        docs = {d for d, _ in c["gold"]}
        gr = graphrag.without(g, c["key"])
        _, m0 = ask.build_pack(c["question"], "position", ask.BUDGET, s, gr, finders=base, comention=ask.COMENTION)
        _, m1 = ask.build_pack(c["question"], "position", ask.BUDGET, s, gr, finders=base + ("he-lines",), comention=ask.COMENTION)
        s0, s1 = set(m0["shown"]) & docs, set(m1["shown"]) & docs
        recovered = s1 - s0
        missed = docs - s1
        read_missed = {d for d in missed if d in covered}
        unread_missed = missed - read_missed
        n = len(docs)
        ceiling = (len(s1) + len(unread_missed)) / n
        print(f"{c['id']:5} {n:>9} {len(s0) / n:>8.3f} {len(s1) / n:>9.3f} {len(recovered):>9} {len(read_missed):>12} {len(unread_missed):>14} {ceiling:>8.3f}")
        tot["cases"] += 1
        tot["default"] += len(s0) / n
        tot["he"] += len(s1) / n
        tot["ceiling"] += ceiling
        tot["found"] += len(s0)
        tot["recovered"] += len(recovered)
        tot["read_missed"] += len(read_missed)
        tot["unread_missed"] += len(unread_missed)
        tot["gold_docs"] += n
        for d in recovered:
            by_pass[covered.get(d, "?")] = by_pass.get(covered.get(d, "?"), 0) + 1
            listed.append((c["id"], d, covered.get(d, "?")))
    k = tot["cases"]
    print(f"\n{k} cases, {tot['gold_docs']} gold documents over them (a document counted once per case):")
    print(f"  mean document recall: default {tot['default'] / k:.3f}; with he-lines {lines}: {tot['he'] / k:.3f}; "
          f"the ceiling if every unread gold document were recovered: {tot['ceiling'] / k:.3f}")
    print(f"  found by the default {tot['found']}; recovered by he-lines {tot['recovered']} (by the pass that read the document: {by_pass}); "
          f"missed though a contract has read the document {tot['read_missed']}; missed, no contract has read it {tot['unread_missed']}")
    if "--recovered" in argv:
        print("\nrecovered document slots (case, document, pass that read it with these three contracts):")
        for cid, d, p in sorted(listed):
            others = sorted({f.parent.name.split("-haiku")[0].split("-r")[0] for f in (ROOT / "Plan" / "runs" / d / "hyperextract").glob("*/usage.json")})
            print(f"  {cid:4} {d[:60]:60} {p:9} runs of: {', '.join(others)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
