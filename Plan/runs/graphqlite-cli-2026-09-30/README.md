# GraphQLite CLI integration — 2026-09-30

Base: `ef5eeddf67cc2cd8b38d9ed49343d55fbaa317d6`. The author asked for
GraphQLite integrated into a local CLI with repo skills. No source or wiki page
was edited, no source newly ingested, and no model was called.

## What ran

| check | result |
|---|---|
| `scripts/install.sh graphqlite`, then `--check graphqlite` | installs the pinned 0.8.0 package in `.venv-graphqlite`; native extension opens |
| `.venv-graphqlite/bin/python scripts/kg_selftest.py` | 10 real-extension fixture tests pass |
| `python3 scripts/graph.py --selftest` | 7/7 cases hold |
| `python3 scripts/graphrag.py selftest` | 9/9 cases hold |
| `python3 scripts/check_skills.py` | 21/21 project skills clean; existing vendored warnings remain advisory |
| `bash -n scripts/install.sh`; `git diff --check`; Python compilation | pass |
| `kg.py index` against the real repo | 181 core nodes, 4,418 core edges, 9,022 evidence records, all verified |
| Native graph roundtrip | nodes, edge order, evidence and attribution exactly equal to `graph.build()` |
| Existing retrieval cases | complete `graphrag.retrieve` output equal for live vs stored graphs on all 24 cases |
| Repeated index | `unchanged`; graph extraction not repeated |

The graph equivalence check is reproducible:

```python
import sys
sys.path.insert(0, "scripts")
import graph, graphrag, kg
live = graph.build()
stored = kg.read_graph(kg.DATABASE)
assert live == stored
assert list(live["nodes"]) == list(stored["nodes"])
for case in graphrag.cases(live):
    assert graphrag.retrieve(case["query"], graph=live) == graphrag.retrieve(case["query"], graph=stored)
```

## What the fixtures cover

Distinct READS/CITES edges on the same pair, node and double-digit edge order,
parameterized Cypher with provenance and truncation, verified-only FTS search,
evidence IDs, context output IDs, changed/deleted source refusal, atomic rebuild
failure, unchanged-index reuse and budget refusal with whole quotations and
conflict metadata retained.

GraphQLite 0.8.0 sorts returned numeric properties lexically. Padded ordinals
preserve the existing graph's iteration order; otherwise equal-score seed order
changes (observed on Q4). The extension's global PageRank has no personalized
restart input, so retrieval intentionally keeps `graphrag.py`'s implementation.

## Full-suite limits

`scripts/selftests.py`: 26 suites held, 1 failed, 12 not run, of 39. The failed
suite was prose-number consistency: 14 stale claims. A separate unmodified
worktree at the base commit reports the identical 14 claims (including 51 vs
59 censuses, `order.holds`, gold-list counts and one unresolved quotation).
These are pre-existing; this integration does not repair unrelated ingest state.

The 12 unrun suites need DSPy, TypeSafe or Hyper-Extract environments absent
in this validation container. They have not passed. The GraphQLite suite ran
through the shared runner and again separately after final changes.

## Scope and remaining work

The index avoids repeated graph extraction for unchanged input; source hashing
still scans input bytes. Changed input triggers a full, atomic rebuild, not a
partial per-file update. Context has a hard UTF-8 byte cap including JSON and
the trailing newline, not an exact model-token count. No percentage of token
savings was measured. Impact analysis, automatic batch planning and semantic
reranking remain unimplemented.
