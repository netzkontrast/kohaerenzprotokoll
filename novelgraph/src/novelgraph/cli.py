"""novelgraph build/search/verify/measure; all computations stay local."""
import argparse
import json
import os
import time
import numpy as np
from .index import Index, atomic_json
from .search import Search
from .verify import verify


def measure(index):
    import ask
    cases = ask.bench_cases()  # Repository questions/gold unchanged.
    results = {}
    for method in index.config["chunkers"]:
        search = Search(index, method)
        scores = {}
        for mode in ("bm25", "vec", "hybrid"):
            per_case = []
            for c in cases:
                hits = search.query(c["question"], k=8, mode=mode)
                gold = c["gold"]
                line_hits = sum(any(h["slug"] == d and h["line_start"] <= n <= h["line_end"] for h in hits) for d, n in gold)
                docs = {d for d, _ in gold}
                per_case.append(dict(id=c["id"], question=c["question"], gold_lines=len(gold),
                                     line_recall=line_hits / len(gold) if gold else None,
                                     document_recall=len(docs & {h["slug"] for h in hits}) / len(docs) if docs else None,
                                     document_ceiling_at_8=min(8, len(docs)) / len(docs) if docs else None,
                                     lines_per_hit=float(np.mean([h["line_end"] - h["line_start"] + 1 for h in hits])) if hits else 0))
            scores[mode] = dict(recall_at_8=float(np.mean([c["line_recall"] for c in per_case if c["line_recall"] is not None])),
                                document_recall_at_8=float(np.mean([c["document_recall"] for c in per_case if c["document_recall"] is not None])), document_ceiling_at_8=float(np.mean([c["document_ceiling_at_8"] for c in per_case if c["document_ceiling_at_8"] is not None])),
                                lines_per_hit=float(np.mean([c["lines_per_hit"] for c in per_case])), cases=per_case)
        # Warm session: query embedding included; initialization excluded and reported separately elsewhere.
        search.query(cases[0]["question"], mode="hybrid")
        latency = []
        for i in range(50):
            start = time.perf_counter()
            search.query(cases[i % len(cases)]["question"], mode="hybrid")
            latency.append((time.perf_counter() - start) * 1000)
        results[method] = dict(chunks=len(search.rows), scores=scores, queries=50,
                               hybrid_ms_p50=float(np.percentile(latency, 50)), hybrid_ms_p95=float(np.percentile(latency, 95)),
                               latency_ms=latency,
                               vec_mb=sum(p.stat().st_size for p in (index.path / "sources").glob(f"*/vec/{method}*.npy")) / 1e6,
                               build_mb=sum(p.stat().st_size for p in (index.path / "_build").glob(f"{method}*")) / 1e6)
        search.close()
    out = dict(cases=len(cases), evaluation="unchanged ask.bench_cases; macro source-line overlap recall@8",
               methods=results, no_llm_calls=True)
    atomic_json(index.root / "novelgraph/measurements/retrieval.json", out)
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    build = sub.add_parser("build")
    build.add_argument("--source")
    build.add_argument("--method", default="heading@v1")
    build.add_argument("--force", action="store_true")
    search = sub.add_parser("search")
    search.add_argument("query")
    search.add_argument("-k", type=int, default=8)
    search.add_argument("--method", default="heading@v1")
    search.add_argument("--mode", choices=("bm25", "vec", "hybrid"), default="hybrid")
    check = sub.add_parser("verify")
    check.add_argument("--method")
    sub.add_parser("measure")
    args = parser.parse_args()
    try:
        index = Index()
        if args.command == "build":
            result = index.build(args.method, args.source, args.force)
        elif args.command == "search":
            engine = Search(index, args.method, vectors=args.mode != "bm25")
            try:
                result = engine.query(args.query, args.k, args.mode)
            finally:
                engine.close()
        elif args.command == "verify":
            reports = [verify(index, m) for m in ([args.method] if args.method else index.config["chunkers"])]
            result = dict(ok=all(r["ok"] for r in reports), methods=reports)
        else:
            result = measure(index)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1 if isinstance(result, dict) and result.get("ok") is False else 0
    except (ValueError, OSError, KeyError) as exc:
        parser.exit(2, f"novelgraph: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
