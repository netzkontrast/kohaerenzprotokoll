"""Gate G2 for the novelgraph finder (SPEC.md §6, step 6): does it add gold the other finders do not send, at the
same serialized budget? Offline, no model; the frozen cases, each case's record removed from the graph.

For each case, the `ask` pack with the default finders and with `novelgraph` added, both at `ask.BUDGET` bytes:
document and line recall, paired, with a 90 % bootstrap interval; the gold lines the novelgraph pack sends that the
default pack does not (**novel gold**), and how many of those lie in documents only novelgraph found; what the
added finder displaced (gold the default pack sent and the novelgraph pack did not); and the cold cost.

    .venv-graphqlite/bin/python Plan/runs/novelgraph-finder-2026-10-02/g2.py
"""
import json
import random
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import ask  # noqa: E402
import askdb  # noqa: E402
import benchset  # noqa: E402
import graph as kg  # noqa: E402
import graphrag  # noqa: E402


def interval(diffs):
    rnd = random.Random(7)
    means = sorted(sum(rnd.choice(diffs) for _ in diffs) / len(diffs) for _ in range(10_000))
    return [round(means[500], 3), round(means[9500], 3)]


cases = [c for c in benchset.cases() if c["gold"]]
t = time.time()
ask.novelgraph_hits([cases[0]["question"]])
cold_one = round(time.time() - t, 1)
t = time.time()
ask.novelgraph_hits([c["question"] for c in cases[1:]])
batch = round(time.time() - t, 1)
s, g = askdb.Store(), kg.build()
rows = []
for c in cases:
    iso = graphrag.without(g, c["key"])
    out = {}
    for name, finders in (("default", ask.DEFAULT_FINDERS), ("novelgraph", ask.DEFAULT_FINDERS + ("novelgraph",))):
        _, meta = ask.build_pack(c["question"], "position", ask.BUDGET, s, iso, finders=finders)
        sent = {(d, n) for d, ns in meta["shown"].items() for n in ns}
        out[name] = {"sent": sent, "meta": meta}
    gold = c["gold"]
    a, b = out["default"], out["novelgraph"]
    only_ng_docs = {d for d, f in b["meta"]["finders"].items() if f == ["novelgraph"]}
    novel = (gold & b["sent"]) - a["sent"]
    lost = (gold & a["sent"]) - b["sent"]
    docs = {d for d, _ in gold}
    rows.append({"id": c["id"],
                 "line": [round(len(gold & a["sent"]) / len(gold), 3), round(len(gold & b["sent"]) / len(gold), 3)],
                 "doc": [round(len(docs & set(a["meta"]["shown"])) / len(docs), 3),
                         round(len(docs & set(b["meta"]["shown"])) / len(docs), 3)],
                 "novel_gold": len(novel), "novel_gold_only_novelgraph_docs": len({x for x in novel if x[0] in only_ng_docs}),
                 "displaced_gold": len(lost), "bytes": [a["meta"]["bytes"], b["meta"]["bytes"]],
                 "docs_only_novelgraph": len(only_ng_docs & set(b["meta"]["shown"]))})
    print(f"{c['id']:4} line {rows[-1]['line']} doc {rows[-1]['doc']} novel {len(novel):3} displaced {len(lost):3}", flush=True)
summary = {"cases": len(rows), "cold_seconds_one_question": cold_one, "batch_seconds_23_questions": batch}
for k in ("line", "doc"):
    diffs = [r[k][1] - r[k][0] for r in rows]
    summary[k] = {"default": round(sum(r[k][0] for r in rows) / len(rows), 3),
                  "novelgraph": round(sum(r[k][1] for r in rows) / len(rows), 3),
                  "paired_diff": round(sum(diffs) / len(diffs), 3), "interval_90": interval(diffs),
                  "better": sum(d > 0 for d in diffs), "worse": sum(d < 0 for d in diffs)}
for k in ("novel_gold", "novel_gold_only_novelgraph_docs", "displaced_gold", "docs_only_novelgraph"):
    summary[k] = sum(r[k] for r in rows)
(HERE / "g2.json").write_text(json.dumps({"summary": summary, "rows": rows}, ensure_ascii=False, indent=1) + "\n",
                              encoding="utf-8")
print(json.dumps(summary, indent=1))
