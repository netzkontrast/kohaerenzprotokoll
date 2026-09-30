#!/usr/bin/env python3
"""The `he-lines` finder against the default, paired over the bench's cases, on the store one tag names.

    python3 Plan/runs/hyperextract-backfill-2026-09-30/paired.py <tag>

Reads `ask-finders/<config>-<tag>.json` (what `measure.sh` wrote from `ask.py bench`), compares every configuration with
`default-<tag>` of the same store — never with a default from another store — and writes `ask-finders/paired-<tag>.json` and
prints one line each: mean document and line recall, the paired difference with its 90 % interval, how many cases went up and
down. The same comparison as `Plan/runs/graph-lab-2026-09-30/ask-finders/paired-scaled.py`, which measured the scaled pass.
Uses `graphlab.paired` and `graphlab.mean`; nothing else.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "scripts"))
import graphlab  # noqa: E402

D = HERE / "ask-finders"
CONFIGS = ["default", "he-lines-10", "he-lines-20", "he-lines-40", "he-lines-80"]


def rows(name: str, key: str) -> dict:
    data = json.loads((D / f"{name}.json").read_text(encoding="utf-8"))
    return {r["id"]: {"recall": r[key]} for r in data["rows"]}


def main(tag: str) -> int:
    out = []
    for n in CONFIGS:
        if not (D / f"{n}-{tag}.json").exists():
            continue
        res = {"config": f"{n}-{tag}"}
        for key, label in (("doc_recall", "doc"), ("line_recall", "line")):
            a, b = rows(f"default-{tag}", key), rows(f"{n}-{tag}", key)
            p = graphlab.paired(a, b)
            res[label + "_recall"] = graphlab.mean(b)
            res[label + "_vs_default"] = [round(p["mean"], 4), round(p["lo"], 4), round(p["hi"], 4), p["up"], p["down"]]
        out.append(res)
        d, l = res["doc_vs_default"], res["line_vs_default"]
        print(f"{n + '-' + tag:28} doc {res['doc_recall']:.3f} ({d[0]:+.3f} [{d[1]:+.3f}, {d[2]:+.3f}], {d[3]} up / {d[4]} down)   "
              f"line {res['line_recall']:.3f} ({l[0]:+.3f} [{l[1]:+.3f}, {l[2]:+.3f}])")
    (D / f"paired-{tag}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return 0 if out else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "backfilled"))
