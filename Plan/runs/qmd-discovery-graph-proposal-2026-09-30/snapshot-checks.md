# Snapshot and content-review validation

2026-09-30, GraphQLite 0.8.0, complete shared corpus store.

- 15 graph-reader integration tests pass, including the wrong-first/right-second
  evidence-reference regression.
- 10 snapshot tests pass: deterministic export, real graph/FTS/provenance
  round-trip, missing/stale/corrupt/version-incompatible snapshots, failure
  cleanup, changes during restoration, init fallback and local/remote startup
  hook invocation.
- Complete export: 217,538 nodes, 560,895 relationships and 9,022 evidence records.
  The additional relationship versus the earlier unification build is the
  corrected evidence record's now-resolvable CITED_FROM link.
- Complete snapshot: 178,381,494 bytes of logical JSONL, 10,389,004 bytes in gzip.
  Source-line text is omitted; the full 125,620-line FTS index is reconstructed
  from the exact authoritative checkout during restoration.
- Restored into a separate fresh database. Both databases pass `askdb.check`;
  core graphs compare equal, native evidence searches compare equal, and all
  9,022 stored verified evidence references resolve against their actual source.
- Project skills: 23/23 clean. qmd coverage: zero uncovered files, including the
  new opt-in graph navigation collection. Hook passes bash syntax validation.
- Standard suite: 35 held, one existing pipeline-order failure due to three
  unreconciled censuses; that check remains enabled. Native snapshot tests are
  registered separately and require the GraphQLite interpreter.

No model, provider or new independent source reading was invoked. Source-scoped
Assertion, Reading, Decision, TemplateVersion and DerivationRun additions remain
prioritized schema proposals, not invented records in the live graph.
