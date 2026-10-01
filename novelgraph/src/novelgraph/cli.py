"""novelgraph — a file-based chunk and vector index over `Sources/`, every hit a line range.

    novelgraph build  [--source SLUG] [--method heading@v1] [--force]
    novelgraph search "query" [-k 8] [--method heading@v1] [--mode bm25|vec|hybrid] [--json]
    novelgraph verify [--no-rechunk]
    novelgraph bench  [--k 8] [--record DIR]      # recall@k on ask.py's cases, latency, sizes
    novelgraph selftest
    novelgraph rlm    [--selftest | --dry-run | --report | --approval "decision 011"] [--methods A,B] [--cases C1,Q2]

Run from the repository root: `.venv-novelgraph/bin/novelgraph …`, the venv made once by
`UV_PROJECT_ENVIRONMENT=$PWD/.venv-novelgraph uv sync --project novelgraph`.
`docs/novelgraph-index.md` has the design and the measurements.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="novelgraph", description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build")
    b.add_argument("--source")
    b.add_argument("--method", action="append")
    b.add_argument("--force", action="store_true")
    s = sub.add_parser("search")
    s.add_argument("query")
    s.add_argument("-k", type=int, default=8)
    s.add_argument("--method", default="heading@v1")
    s.add_argument("--mode", default="hybrid", choices=("bm25", "vec", "hybrid"))
    s.add_argument("--json", action="store_true")
    v = sub.add_parser("verify")
    v.add_argument("--no-rechunk", action="store_true")
    be = sub.add_parser("bench")
    be.add_argument("--k", type=int, default=8)
    be.add_argument("--record")
    sub.add_parser("selftest")
    r = sub.add_parser("rlm", help="a dspy.RLM agent searches the index for a bench question's evidence (rlm.py)")
    r.add_argument("--selftest", action="store_true")
    r.add_argument("--dry-run", action="store_true")
    r.add_argument("--report", action="store_true")
    r.add_argument("--methods", default=None)
    r.add_argument("--cases", default=None)
    r.add_argument("--model", default="claude-cli/haiku")
    r.add_argument("--approval")
    a = ap.parse_args(argv)

    if a.cmd == "build":
        from .build import build
        build(a.source, a.method, a.force)
        return 0
    if a.cmd == "search":
        from .search import Index, as_json, show
        hits = Index(a.method).search(a.query, a.k, a.mode)
        print(as_json(hits, a.method) if a.json else show(hits, a.method))
        return 0
    if a.cmd == "verify":
        from .verify import verify
        fails, info = verify(rechunk=not a.no_rechunk)
        for f in fails[:50]:
            print(f"  FAIL  {f}")
        if len(fails) > 50:
            print(f"  … and {len(fails) - 50} more")
        print(f"coverage: {info['coverage']}")
        print("catalogue: " + json.dumps(info["catalogue"], ensure_ascii=False))
        print("chunks:   " + ", ".join(f"{m} {n}" for m, n in info["chunks"].items()))
        print("verify: " + ("ok" if not fails else f"{len(fails)} failures"))
        return 1 if fails else 0
    if a.cmd == "bench":
        from .bench import latency, recall, sizes
        from . import store
        result = {"recall": recall(a.k), "latency": [latency(m) for m in store.chunkers()], "sizes": sizes()}
        print(f"recall@{a.k} on {next(iter(result['recall'].values()))['cases']} cases (ask.py bench_cases)")
        print(f"  {'method/mode':<22} {'doc':>6} {'ceiling':>8} {'line':>6} {'lines/hit':>10}")
        for key, r in result["recall"].items():
            print(f"  {key:<22} {r['doc_recall']:>6} {r['doc_ceiling']:>8} {r['line_recall']:>6} {r['lines_per_hit']:>10}")
        for l in result["latency"]:
            print(f"latency {l['method']} {l['mode']}: P50 {l['p50_ms']} ms, P95 {l['p95_ms']} ms, "
                  f"max {l['max_ms']} ms over {l['queries']} warm queries (load {l['load_s']} s)")
        print("sizes: " + json.dumps(result["sizes"], ensure_ascii=False))
        if a.record:
            out = Path(a.record)
            out.mkdir(parents=True, exist_ok=True)
            (out / "bench.json").write_text(json.dumps(result, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        return 0
    if a.cmd == "rlm":
        from . import rlm
        if a.selftest:
            fails = rlm.selftest()
            for f in fails:
                print(f"  FAIL  {f}")
            print(f"novelgraph rlm selftest: {'held' if not fails else f'{len(fails)} failed'}")
            return 1 if fails else 0
        if a.report:
            print(json.dumps(rlm.report(), ensure_ascii=False, indent=1))
            return 0
        methods = a.methods.split(",") if a.methods else list(rlm.METHODS)
        only = a.cases.split(",") if a.cases else None
        rlm.run(methods, only, a.model, a.approval, a.dry_run)
        return 0
    if a.cmd == "selftest":
        from .selftest import gates, publication_gates, selftest
        fails = selftest() + gates() + publication_gates()
        for f in fails:
            print(f"  FAIL  {f}")
        print(f"novelgraph selftest: {'held' if not fails else f'{len(fails)} failed'}")
        return 1 if fails else 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
