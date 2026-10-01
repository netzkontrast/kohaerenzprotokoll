# PR 137 — consolidated novelgraph validation

2026-10-01; base `607c3c16` (PR #138 merged). All corpus sources and committed chunk files are unchanged.

| Gate | Result | Evidence |
|---|---|---|
| Landed coverage | 586/586; whole catalogue 587, one unlanded audio | `verify.log` |
| Exact verification | pass for all three methods, including re-derived lex and FTS postings, chunk recomputation and aggregate vectors by value | `verify.log` |
| Full build | 126.15 s, 31,366 embedded chunks across three methods | `build.json` |
| No-op rebuild | 0.84 s, 0 rechunked, 0 embedded, 0 concatenated; all 1,758 per-source vector files skipped | `noop.json` |
| Offline regression fixtures | pass: chunking, missing/changed sources, prefix changes, embedder revision, swapped vectors, lex/FTS corruption, interrupted publication/recovery, real process locks, stable no-op bytes/mtimes | `offline.log` |
| Standard-library suites | 55 held, 0 failed, 16 dependency suites intentionally skipped | `standard-library.log` |
| Heading hybrid latency | P50 8.9 ms, P95 34.2 ms, 50 warm queries, one BLAS thread | `bench.json` |
| Heading document recall@8 | BM25 0.066, vector 0.067, hybrid 0.068; ceiling 0.427 | `bench.json` |

The recall gold is the existing 24 `ask.bench_cases()` cases, with the documented lexical/circular bias.
These numbers establish regression stability, not discovery quality. All model encoding is local/static;
no LLM calls and no source text transmission. The pinned embedding model was downloaded once.
The graph initializer succeeded for sources, derivation, graph and template checks; optional qmd installation
failed in this environment. qmd coverage still passed and novelgraph does not depend on qmd.

Commands, run from repository root:

```bash
UV_PROJECT_ENVIRONMENT=$PWD/.venv-novelgraph uv sync --project novelgraph --frozen
.venv-novelgraph/bin/novelgraph selftest
.venv-novelgraph/bin/novelgraph build
.venv-novelgraph/bin/novelgraph verify
OPENBLAS_NUM_THREADS=1 .venv-novelgraph/bin/novelgraph bench --record Plan/runs/novelgraph-pr137-final
python3 scripts/selftests.py --only std
```

Publication uses flock and atomic renames, with a persistent interruption marker. It protects cooperative
readers/writers and rejects a partial build after a crash; it does not promise power-loss durability.
