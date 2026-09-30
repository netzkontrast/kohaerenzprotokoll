# Initialization and extraction validation — 2026-09-30

Base: `1fe8512fae4dd473948bdb2e5c0cf21107ff55ae`, including merged PR #123.
No graph unification, production graph import or model call was performed.

| Check | Result | Scope |
|---|---|---|
| `knowledge.py selftest` | passed | offline command plans, check-only behavior, missing-state detection despite shell exit 0, separate stores, continuation after failures |
| `knowledge.py init --profile reader --check` | not ready, as expected | real source manifest and qmd coverage passed; local graph, qmd and default HE installation absent; each reported independently |
| `reading_extract.py selftest` | 21/21 passed | real temporary source, file-line offsets, source/template hash drift, malformed/empty payloads, absent surfaces, quote invention, joined/ambiguous quotations, duplication, immutable staging runs, path refusal and unreviewed semantics |
| `reading_extract.py native-selftest` | 4/4 passed | actual HyperExtract factory/feed/schema/merge for TermReadings, StatedRelations, RelationReadings plus malformed-response refusal; fake structured model and fake embeddings |
| `templates.py check` on changed/new templates | 16 checks, 0 failed, 0 unreached | native YAML validation/load/resolve and project checks; procedural-name check reports short-name blind spots |
| `check_skills.py` | 22/22 project skills clean | new skills and canonical Claude symlinks; unchanged vendored naming findings remain informational |
| `verify_queries.py` | 12/12 recipes passed | native GraphQLite 0.8.0 synthetic graph; parallel edges and parameter binding also passed |
| Independent delegated template trial | passed mechanics | three native RelationReadings records retained asserts/hedges/asks, placed at synthetic lines 1/2/3, all unreviewed; found worker-preflight scope and empty-chunk issues, corrected before delivery |

Native HE tests used an isolated PyPI `hyperextract==0.10.3` environment and
the repository's existing template/parse interface. This is not a test of the
exact git installation pin with its complete dependency lock, a live provider,
prompt quality, real corpus recall, or learned guideline improvement. The full
initializer's installer/model-download path was not executed; it delegates to
the existing installers and has offline orchestration tests.

Reproduce using the repository's installed tools:

```bash
python3 scripts/knowledge.py selftest
python3 scripts/reading_extract.py selftest
python3 scripts/reading_extract.py native-selftest
python3 scripts/templates.py check Plan/hyperextract/TermReadings.yaml Plan/hyperextract/RelationReadings.yaml
python3 scripts/check_skills.py
.venv-graphqlite/bin/python Plan/runs/qmd-discovery-graph-proposal-2026-09-30/verify_queries.py
```

`native-selftest` resolves the interpreter beside `he`. Missing native tooling
is reported as not reached. Normal reader workers do not execute global
template-name checks; the coordinating session performs them and supplies the
report. No reviewed training set was created and no DSPy optimizer was run.
