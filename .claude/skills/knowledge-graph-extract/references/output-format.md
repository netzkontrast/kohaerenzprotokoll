# Output Directory Format

All extraction state lives in a single user-specified output directory (`<output_dir>`).
Everything is plain JSON/JSONL so any tool (or human) can inspect it.

```
<output_dir>/
  manifest.json     # run config + chunk plan + progress (the resume anchor)
  schema.json       # graph schema (copied/written here during setup, if provided)
  triples.jsonl     # append-only extracted triplets
  entities.jsonl    # append-only entity registry
  rejected.jsonl    # triplets quarantined by validation (created by validate_triples.py)
  cypher/           # 00_constraints_{neo4j,memgraph}, 01_entities, 02_relations (created by generate_cypher.py)
```

## manifest.json

```json
{
  "version": 1,
  "created": "2026-07-15T14:00:00Z",
  "docs_dir": "/abs/path/to/documents",
  "schema_file": "schema.json",
  "max_triplets_per_doc": 100,
  "documents": [
    {
      "path": "notes/curie.md",
      "unit": "line",
      "lines": 2840,
      "status": "in_progress",
      "chunks": [
        {"id": 1, "start_line": 1,    "end_line": 1187, "status": "done",        "triplets": 18},
        {"id": 2, "start_line": 1188, "end_line": 2400, "status": "in_progress", "triplets": 0},
        {"id": 3, "start_line": 2401, "end_line": 2840, "status": "pending",     "triplets": 0}
      ]
    },
    {
      "path": "papers/nobel.pdf",
      "unit": "page",
      "status": "pending",
      "chunks": [
        {"id": 1, "start_page": 1,  "end_page": 10, "status": "pending", "triplets": 0},
        {"id": 2, "start_page": 11, "end_page": 18, "status": "pending", "triplets": 0}
      ]
    }
  ]
}
```

Rules:

- `documents[].path` is relative to `docs_dir`. `schema_file` is relative to `<output_dir>`; `null` when no schema.
- `unit` is `"line"` (chunks carry `start_line`/`end_line`) or `"page"` (chunks carry
  `start_page`/`end_page`). Defaults to `"line"` if absent.
- Chunk `status`: `pending` → `in_progress` → `done`. A document is `done` when all its chunks are.
- **The chunk plan (boundaries + ids) is immutable once written.** Progress fields
  (`status`, `triplets`) are the only fields ever updated, and only via
  `scripts/kg_mark.py`, which rewrites the manifest atomically.
- `max_triplets_per_doc` is `null` when the user set no cap.

## triples.jsonl

One JSON object per line, append-only:

```json
{"doc": "notes/curie.md", "chunk": 1, "subject": "Marie Curie", "subject_type": "Person", "relation": "WORKS_AT", "object": "Sorbonne", "object_type": "Organization"}
```

- `doc` matches `documents[].path` in the manifest; `chunk` matches a chunk `id`.
- `subject_type` / `object_type` may be omitted only when no schema is in use.
- `subject`, `relation`, `object` are non-empty strings. `relation` is UPPER_SNAKE_CASE.

## entities.jsonl

One JSON object per line, append-only. First mention of an entity defines its canonical name;
later surface forms are recorded by appending a new line for the same `name` with extra aliases
(readers merge lines by `name`, union the aliases):

```json
{"name": "Marie Curie", "type": "Person", "aliases": ["M. Curie", "Madame Curie"], "first_seen_doc": "notes/curie.md"}
```

## rejected.jsonl

Original triple object plus a `reason` field, written by `validate_triples.py`:

```json
{"doc": "notes/curie.md", "chunk": 2, "subject": "radium", "subject_type": "Element", "relation": "DISCOVERED_BY", "object": "Marie Curie", "object_type": "Person", "reason": "subject_type 'Element' not in schema entity_types"}
```

Rejected triples are quarantined, never deleted — they can be re-admitted by editing the schema
and re-running validation, or fixed by hand and appended back to triples.jsonl.
