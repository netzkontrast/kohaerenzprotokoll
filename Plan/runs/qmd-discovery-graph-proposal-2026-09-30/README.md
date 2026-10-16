# Discovery graph query fixture

<!-- readme-context:start -->
Dated run/design record. Results and commands below refer to its recorded inputs
and environment, not current test status. Use NOW.md for authorized next work and
SPEC.md for the adopted architecture. Preserved measurements are not re-run by this refresh.

[Project](../../../README.md) · [Current work](../../../NOW.md) · [Plan guide](../../README.md)
<!-- readme-context:end -->

See [the proposal](../../concept/qmd-discovery-graph_2026-09-30.md).

Run `verify_queries.py` with GraphQLite 0.8.0. All rows and graph additions are synthetic; five recipes target kg.py on main and seven require proposed schema additions. The optional --db target must be new. No production database is modified.
