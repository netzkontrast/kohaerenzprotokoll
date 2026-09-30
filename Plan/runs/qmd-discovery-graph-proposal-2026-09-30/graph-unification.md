# Shared graph implementation

Both `kg.py` and `askdb.py` now use `Plan/derived/ask.db`, schema 2, GraphQLite 0.8.0. `knowledge.py init` builds it once for every profile; research/full additionally validate the corpus view.

The database contains typed wiki, corpus, chapter, decision-sheet, proposal and evidence nodes alongside source-line, quotation and verified-evidence FTS indexes. Wiki nodes also carry a `Core` label on the same node. Original graph relationships carry `core: true`, padded ordinals and their complete original payload. Existing evidence IDs and PPR/MMR context behavior remain compatible. Both kinds of relationship can coexist between the same node pair.

Builders stage a complete database beside the previous snapshot and replace it atomically. Source bytes and derivation code share one input manifest. Inputs are checked before publication and again immediately before replacement. Failed builds preserve the previous snapshot. Old schemas are refused and rebuilt from authoritative files; legacy `graphqlite.db` files are unused disposable artifacts. Authoring files are untouched.

Core ranking uses the original weighted personalized PageRank. Corpus paths and communities exclude `P_` relationships and evidence attachment links. Raw Cypher can inspect proposals explicitly; the reader Store enforces SQLite query-only mode. Integrity checking hashes graph labels/properties/parallel edges and logical FTS rows, detecting changes even when counts stay equal.

## Validated

- Real GraphQLite integration: 14 tests pass, including stable IDs, ordering beyond ten edges, parallel relationships, dual labels, source changes/deletion, atomic failure and changes during publication, property tampering, proposal isolation and read-only queries.
- `askdb.py selftest` and `knowledge.py selftest` pass.
- Full source build: 217,538 nodes, 560,894 relationships, 125,620 source lines; core projection: 181 nodes and 4,418 relationships; 9,022 indexed evidence records.
- Standard project suite: 35 held, one existing failure. The live pipeline-order check reports three unreconciled source censuses. That safeguard remains enabled.

The qmd discovery/claim-import schema in the adjacent query catalogue remains a fixture proposal. Unifying the existing graph stores does not import qmd hits or promote learned HyperExtract claims to stated facts. No model training or provider calls were performed.
