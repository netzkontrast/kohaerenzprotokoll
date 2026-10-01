"""Where the `ask` pack's evidence comes from: the route's ceiling, and what each finder's anchors yield — offline.

`pack_variants.py` showed that no packing variant moves gold recall; this asks why. For each frozen case (its own
record removed from the graph, as `ask.py bench` does), with **no budget and no per-document cap**:

- **ceiling** — the gold lines and gold documents inside any anchor's widened span: the most any packer could send
  from this route;
- **per finder** — anchors, characters its spans cost, gold lines inside them, and gold lines **only** it reaches;
- **waste** — characters spent on documents with no gold line at all.

    .venv-graphqlite/bin/python Plan/runs/architecture-session-2026-10-01/packs/finder_yield.py
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(HERE))
import ask  # noqa: E402
import askdb  # noqa: E402
import graph as kg  # noqa: E402
import graphrag  # noqa: E402
from pack_variants import spans_of  # noqa: E402


def main() -> dict:
    frozen = json.loads((ROOT / "Plan" / "eval" / "retrieval-cases-v1.json").read_text(encoding="utf-8"))
    s, g = askdb.Store(), kg.build()
    total = defaultdict(lambda: {"anchors": 0, "chars": 0, "gold": 0, "only": 0, "cases_with_gold": 0})
    rows = []
    for c in frozen["cases"]:
        gold = {tuple(x) for x in c["gold"]}
        r = ask.route(c["question"], "position", s, graphrag.without(g, c["key"]))
        lines_by = defaultdict(set)          # finder -> {(doc, line)} its spans cover
        chars_by = defaultdict(int)
        for a in r["anchors"]:
            lo, hi = a.get("span") or spans_of(s, a["doc"], [a["line"]])[0]
            got = s.window(a["doc"], lo, hi)
            lines_by[a["finder"]] |= {(a["doc"], n) for n, _ in got}
            chars_by[a["finder"]] += sum(len(t) + 8 for _, t in got)
            total[a["finder"]]["anchors"] += 1
        covered = set().union(*lines_by.values()) if lines_by else set()
        gold_docs = {d for d, _ in gold}
        doc_chars = defaultdict(int)
        for d, n in covered:
            doc_chars[d] += 1
        row = {"id": c["id"], "gold": len(gold), "ceiling_line": round(len(gold & covered) / len(gold), 3),
               "ceiling_doc": round(len(gold_docs & {d for d, _ in covered}) / len(gold_docs), 3),
               "lines_sent_unbounded": len(covered),
               "lines_on_docs_without_gold": sum(v for d, v in doc_chars.items() if d not in gold_docs)}
        for f, ls in lines_by.items():
            others = set().union(*[v for k, v in lines_by.items() if k != f]) if len(lines_by) > 1 else set()
            total[f]["chars"] += chars_by[f]
            total[f]["gold"] += len(gold & ls)
            total[f]["only"] += len((gold & ls) - others)
            total[f]["cases_with_gold"] += bool(gold & ls)
        rows.append(row)
        print(f"{c['id']:4} ceiling line {row['ceiling_line']:.3f} doc {row['ceiling_doc']:.3f}  "
              f"lines {row['lines_sent_unbounded']:5}  on gold-less docs {row['lines_on_docs_without_gold']:5}", flush=True)
    n = len(rows)
    out = {"cases": rows, "finders": {f: {**v, "gold_per_10k_chars": round(10_000 * v["gold"] / v["chars"], 2) if v["chars"] else None}
                                      for f, v in total.items()},
           "mean_ceiling_line": round(sum(r["ceiling_line"] for r in rows) / n, 3),
           "mean_ceiling_doc": round(sum(r["ceiling_doc"] for r in rows) / n, 3),
           "share_lines_on_goldless_docs": round(sum(r["lines_on_docs_without_gold"] for r in rows)
                                                 / sum(r["lines_sent_unbounded"] for r in rows), 3),
           "frozen_sha256": frozen["sha256"]}
    (HERE / "finder_yield.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return out


if __name__ == "__main__":
    res = main()
    print(f"\nroute ceiling (no budget, no cap): line {res['mean_ceiling_line']}, doc {res['mean_ceiling_doc']}; "
          f"{res['share_lines_on_goldless_docs']:.0%} of anchored lines lie in documents with no gold line")
    for f, v in sorted(res["finders"].items(), key=lambda kv: -(kv[1]["gold_per_10k_chars"] or 0)):
        print(f"  {f:15} anchors {v['anchors']:5} chars {v['chars']:8} gold {v['gold']:4} only-it {v['only']:4} "
              f"cases {v['cases_with_gold']:2}  gold/10k chars {v['gold_per_10k_chars']}")
