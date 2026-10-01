# novelgraph index — the measurement of 2026-10-01

What `novelgraph bench --record` kept: `bench.json` (recall@8, latency, sizes) and `bench-k50.json` (recall@50, the
same latency and sizes). The cases are `ask.py bench_cases()`, unchanged. No model call; the static embedder
(`minishlab/potion-multilingual-128M`, revision pinned in `Index/methods.toml`) runs locally.

The reading of the numbers, the decisions taken while building, and the open questions are in `docs/novelgraph-index.md`.

    .venv-novelgraph/bin/novelgraph bench --record Plan/runs/novelgraph-index-2026-10-01
