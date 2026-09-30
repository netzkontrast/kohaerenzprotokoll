# Graph — portable snapshots and navigation

The authoring layers remain `Sources/`, `Wiki/` and `Plan/`. This directory is a
versioned handover of their derived graph, not a second place to edit knowledge.

```bash
python3 scripts/knowledge.py init --profile reader
.venv-graphqlite/bin/python scripts/kg.py export
.venv-graphqlite/bin/python scripts/kg.py restore
```

Initialization calls `kg.py index`: keep a fresh database; otherwise restore a
matching snapshot; otherwise rebuild from authoritative files and report why
restoration was unavailable. Export is explicit, so starting a session never
rewrites tracked snapshots or makes the working tree dirty. Delegated agents
use `knowledge.py init --profile reader --check` and do not export or restore.

`manifest.json` is an atomic pointer to an immutable
`snapshots/<sha256>.jsonl.gz` archive. Gzip is transport compression: decompression
produces UTF-8 JSONL with external node IDs, every label, typed named properties,
ordered parallel edges and the evidence indexes. No native SQLite row IDs, SQL
statements, embeddings, credentials or executable expressions are exported.
Internal IDs and FTS backing tables are recreated in a fresh GraphQLite database.

The full source text is **not copied into the archive**. Source-line FTS is
rebuilt from the checkout's exact, hashed source files. Line nodes hold locations,
not passages. Markdown navigation gives links and bounded relationship lists;
source lines are retrieved and cited only when needed for a particular claim.
Existing verified quotations remain evidence records and retain their IDs.

A snapshot restores only when all authoritative input hashes, derivation code,
format version, schema version and GraphQLite pin match. Archive checksum,
logical checksum, record counts and a logical re-export of the restored graph
must agree. Inputs are checked again before atomic database replacement.
Failure preserves the existing database. Missing source files invalidate a
snapshot even if its archive contains evidence from those files.

The logical format preserves property types explicitly: `text`, `int`, `real`,
`bool`, `json`. A node record has `record`, `id`, `labels`, `props`; an edge record
has `record`, `source`, `target`, `type`, `props`. Property values are `[type,value]`.
Other records contain the rows of `quotes`, `kp_evidence` and `kp_fts`. Row order
is retained, so repeated edges and FTS ties survive restoration. The first
record contains the export schema, input manifest and graph metadata.

[index.md](index.md) is a generated, bounded navigation view of the semantic core.
It is **not** the restore format and is not an input to derivation. Deleting or
editing it cannot change a stored claim. Snapshot archives are content-addressed;
retain the current manifest's archive when pruning superseded generations.

For a given database, export is deterministic. It is a cache bound to its source
checkout, not an independent backup of the entire project. Keep `Sources/` with
it. Compression changes file size, not what counts as knowledge.

The content/schema review and priorities are in
[the graph schema audit](../Plan/concept/graph-schema-audit_2026-09-30.md).
