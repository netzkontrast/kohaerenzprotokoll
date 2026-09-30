#!/usr/bin/env python3
"""The configurations of run4.sh, run5.sh and run6.sh against the default, paired over the cases: mean, 90 % interval, who moved."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts"))
import graphlab
D = Path(__file__).resolve().parent
def rows(name, key):
    return {r["id"]: {"recall": r[key]} for r in json.loads((D / f"{name}.json").read_text(encoding="utf-8"))["rows"]}
names = ["default-scaled", "without-graph-evidence-scaled", "without-bm25-lines-scaled", "without-parallel-scaled",
         "without-entity-unread-scaled", "without-co-mention-scaled", "he-lines-10-scaled", "he-lines-20-scaled",
         "he-lines-40-scaled", "he-lines-80-scaled"]
out = []
for n in names:
    if not (D / f"{n}.json").exists():
        continue
    res = {"config": n}
    for key, label in (("doc_recall", "doc"), ("line_recall", "line")):
        a, b = rows("default-scaled", key), rows(n, key)
        p = graphlab.paired(a, b)
        res[label + "_recall"] = graphlab.mean(b)
        res[label + "_vs_default"] = [round(p["mean"], 4), round(p["lo"], 4), round(p["hi"], 4), p["up"], p["down"]]
    out.append(res)
    print(f"{n:30} doc {res['doc_recall']:.3f} ({res['doc_vs_default'][0]:+.3f} [{res['doc_vs_default'][1]:+.3f}, {res['doc_vs_default'][2]:+.3f}], "
          f"{res['doc_vs_default'][3]} up / {res['doc_vs_default'][4]} down)   line {res['line_recall']:.3f} ({res['line_vs_default'][0]:+.3f} "
          f"[{res['line_vs_default'][1]:+.3f}, {res['line_vs_default'][2]:+.3f}])")
(D / "paired-scaled.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
