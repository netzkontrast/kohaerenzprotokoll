"""`novelgraph bench`: recall@k on the `ask.py bench` cases, query latency, sizes. No model call.

Recall uses the frozen cases (`benchset.cases`, `Plan/eval/retrieval-cases-v1.json`) — the 24 conflict and
question records, gold = the (slug, file line) each cites. Two numbers per case:

- **document recall** — gold documents that some top-k chunk comes from;
- **line recall** — gold lines that lie inside some top-k chunk's range.

Line recall rewards large chunks (a `section@v1` chunk covers far more lines than a
`heading@v1` one), so the mean lines per returned chunk is printed beside it.
The gold's known bias (`Plan/concept/evaluation-audit_2026-09-30.md`): 92 % of it
are lines wiki pages also quote, found by lexical search — BM25 is favoured.
"""

from __future__ import annotations

import json
import os
import statistics
import time
from pathlib import Path

from . import store
from .repo import ROOT, bench_cases
from .search import MODES, Index


def recall(k: int = 8, methods: list[str] | None = None) -> dict:
    cases = [c for c in bench_cases() if c["gold"]]
    out = {}
    for m in methods or list(store.chunkers()):
        ix = Index(m)
        for mode in MODES:
            rows = []
            for c in cases:
                hits = ix.search(c["question"], k, mode)
                docs = {d for d, _ in c["gold"]}
                got = {h["slug"] for h in hits}
                line_hit = sum(1 for d, n in c["gold"]
                               if any(h["slug"] == d and h["line_start"] <= n <= h["line_end"] for h in hits))
                rows.append({"id": c["id"], "doc_recall": len(docs & got) / len(docs),
                             "doc_ceiling": min(k, len(docs)) / len(docs),
                             "line_recall": line_hit / len(c["gold"]),
                             "lines_per_hit": statistics.mean(h["line_end"] - h["line_start"] + 1 for h in hits) if hits else 0})
            out[f"{m}/{mode}"] = {
                "cases": len(rows),
                "doc_recall": round(statistics.mean(r["doc_recall"] for r in rows), 3),
                "doc_ceiling": round(statistics.mean(r["doc_ceiling"] for r in rows), 3),
                "line_recall": round(statistics.mean(r["line_recall"] for r in rows), 3),
                "lines_per_hit": round(statistics.mean(r["lines_per_hit"] for r in rows), 1),
                "rows": rows}
    return out


def latency_queries(n: int = 50) -> list[str]:
    """The bench questions, then term-page names in file order, to n — fixed, so a rerun asks the same."""
    qs = [c["question"] for c in bench_cases()]
    for p in sorted((ROOT / "Wiki" / "candidates").glob("*.md")):
        if len(qs) >= n:
            break
        qs.append(p.stem.replace("-", " "))
    return qs[:n]


def latency(method: str = "heading@v1", mode: str = "hybrid", k: int = 8, n: int = 50) -> dict:
    t0 = time.perf_counter()
    ix = Index(method)
    ix.search("Aufwärmen", k, mode)  # loads the model; everything after is warm
    load = time.perf_counter() - t0
    times = []
    for q in latency_queries(n):
        t = time.perf_counter()
        ix.search(q, k, mode)
        times.append((time.perf_counter() - t) * 1000)
    times.sort()
    p = lambda f: round(times[min(len(times) - 1, int(round(f * (len(times) - 1))))], 1)  # noqa: E731
    return {"method": method, "mode": mode, "queries": len(times), "p50_ms": p(0.5), "p95_ms": p(0.95),
            "max_ms": round(times[-1], 1), "load_s": round(load, 2)}


def du(path: Path, pattern: str = "*") -> float:
    return round(sum(f.stat().st_size for f in path.rglob(pattern) if f.is_file()) / 1e6, 1) if path.exists() else 0.0


def sizes() -> dict:
    from .repo import read_jsonl
    out = {"chunks": {}, "tokens_mean": {}, "over_max": {}}
    slugs = [r["slug"] for r in read_jsonl(store.MANIFEST)]
    for m, params in store.chunkers().items():
        toks = [r["tokens"] for s in slugs for r in read_jsonl(store.chunks_path(s, m))]
        out["chunks"][m] = len(toks)
        out["tokens_mean"][m] = round(statistics.mean(toks), 1)
        out["tokens_median"] = out.get("tokens_median", {}) | {m: statistics.median(toks)}
        if "max" in params:
            out["over_max"][m] = sum(1 for t in toks if t > params["max"])
            out.setdefault("under_min", {})[m] = sum(1 for t in toks if t < params["min"])
    out["mb"] = {"vec": du(store.SOURCES, "*.npy") + du(store.SOURCES, "vec/*.json"),
                 "_build": du(store.BUILD),
                 "chunks (committed)": du(store.SOURCES, "*/chunks/*.jsonl"),
                 "lex (ignored)": du(store.SOURCES, "*/lex/*.jsonl"),
                 "source.json (committed)": du(store.SOURCES, "source.json")}
    return out
