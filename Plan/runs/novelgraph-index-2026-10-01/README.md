# novelgraph index — the measurement of 2026-10-01

<!-- readme-context:start -->
Dated run/design record. Results and commands below refer to its recorded inputs
and environment, not current test status. Use NOW.md for authorized next work and
SPEC.md for the adopted architecture. Preserved measurements are not re-run by this refresh.

[Project](../../../README.md) · [Current work](../../../NOW.md) · [Plan guide](../../README.md)
<!-- readme-context:end -->

What `novelgraph bench --record` kept: `bench.json` (recall@8, latency, sizes) and `bench-k50.json` (recall@50, the
same latency and sizes). The cases are `ask.py bench_cases()`, unchanged. No model call; the static embedder
(`minishlab/potion-multilingual-128M`, revision pinned in `Index/methods.toml`) runs locally.

The reading of the numbers, the decisions taken while building, and the open questions are in `docs/novelgraph-index.md`.

    .venv-novelgraph/bin/novelgraph bench --record Plan/runs/novelgraph-index-2026-10-01
