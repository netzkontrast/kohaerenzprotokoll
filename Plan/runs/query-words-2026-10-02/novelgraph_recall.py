"""novelgraph's recall@8 on the frozen cases with its old query words and with `askdb.query_words`, paired.

The index is the same; only the words its BM25 side asks change (the vector side never saw them). No model.

    .venv-novelgraph/bin/python Plan/runs/query-words-2026-10-02/novelgraph_recall.py
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import words  # noqa: E402  the old builders, verbatim
from novelgraph import bench, search  # noqa: E402

out = {}
for label, fn in (("old", lambda q: words.OLD["novelgraph Index.bm25"](q)), ("new", None)):
    saved = search.query_words
    if fn:
        search.query_words = fn
    try:
        r = bench.recall(8, ["heading@v1"])
    finally:
        search.query_words = saved
    out[label] = {k: {m: v[m] for m in ("doc_recall", "line_recall")} | {"rows": v["rows"]} for k, v in r.items()}
for key in out["new"]:
    o, n = out["old"][key], out["new"][key]
    worse = sum(a["doc_recall"] > b["doc_recall"] for a, b in zip(o["rows"], n["rows"]))
    better = sum(a["doc_recall"] < b["doc_recall"] for a, b in zip(o["rows"], n["rows"]))
    print(f"{key:22} doc {o['doc_recall']:.3f} -> {n['doc_recall']:.3f}  line {o['line_recall']:.3f} -> {n['line_recall']:.3f}"
          f"  cases better {better} worse {worse}")
(HERE / "novelgraph_recall.json").write_text(json.dumps(
    {lab: {k: {m: v[m] for m in ("doc_recall", "line_recall")} for k, v in res.items()} for lab, res in out.items()},
    indent=1) + "\n", encoding="utf-8")
