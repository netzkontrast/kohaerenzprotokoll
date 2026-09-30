# GraphQLite CLI

Upstream: https://github.com/colliery-io/graphqlite — MIT. Python distribution
`graphqlite==0.8.0`, installed in `.venv-graphqlite` by `scripts/install.sh`.
No server or provider credentials are required.

| command after `.venv-graphqlite/bin/python scripts/kg.py` | result |
|---|---|
| `index` | Build `Plan/derived/ask.db`; report `unchanged` if input hashes match. Rebuild fully from authoritative files after a change. |
| `check` | Check input freshness; nonzero on an absent or stale database. |
| `search "words" --limit 10` | FTS5/BM25 over verified quotations. Literal words, not Cypher or FTS syntax. |
| `context "question" --max-bytes 12000` | Existing personalized PageRank and MMR; whole quotations, IDs, conflicts and questions; UTF-8 JSON size capped. |
| `around term:nexus --hops 2 --limit 30` | Parameterized Cypher traversal of the core graph with `via` provenance. Hops 1–3; limit capped at 100; truncation reported. |
| `evidence evidence:<hash>` | Complete verified evidence by ID, including the source file line and wiki section. |

All successful output is compact JSON. Refusals are JSON on stderr with exit 1.
`--db Plan/derived/other.db` before the command selects another derived database.
No arbitrary Cypher mutation interface is exposed.

The projection retains core nodes and parallel typed edges from `graph.py`.
Evidence is separately addressable and linked to its term and cited source.
Evidence IDs hash the attributed record; the same record keeps its ID across
rebuilds, while a changed quote, citation or page location changes it.

Source text, manifest, term/conflict/question pages and derivation code are hashed
before serving. A changed or deleted input invalidates the index. Reads check
again after querying. Rebuilds publish atomically and keep the old index on failure.

`context` considers up to 64 MMR-selected quotations on the existing retriever's
top eight terms. It does not promise exhaustive coverage. The byte cap retains
all returned conflict/question metadata and refuses if metadata alone cannot fit.
It never truncates a quotation, and marks incomplete selection. FTS search can
find evidence outside those eight terms; search rank is not a verdict on canon.

GraphQLite's global PageRank is not personalized: use `graphrag.py`'s existing
implementation, not the extension's algorithm as a drop-in replacement.

Fixtures: `scripts/kg_selftest.py` runs the real native extension offline and
checks parallel edges, Cypher provenance, verified-only retrieval, IDs, freshness,
atomic failure, unchanged-index reuse and byte-budget refusal.

Not built: per-file partial updates, semantic reranking, impact analysis of
chapter beats, automatic batch planning or model-token counting.

`export` writes a human-readable Markdown atlas under `Graph/`. Topic pages separate Wiki links, source readings, citation references, conflicts and questions. There is no import or restore, and the database builder never reads the atlas. Open and cite source lines only when needed for a concrete statement.
