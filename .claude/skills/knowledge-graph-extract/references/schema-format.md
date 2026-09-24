# Graph Schema Format

The schema constrains what the agent extracts and what the validator accepts.
It is optional — without one, extraction is open-ended and validation only checks structure.

The schema can come from three places; all end up as `<output_dir>/schema.json`:

1. **As a file** — pass a path; the agent copies it into the output directory.
2. **Inline in the prompt** — e.g. "entities: Person, Organization; relations: WORKS_AT, FOUNDED";
   the agent writes the equivalent `schema.json` and shows it to the user for confirmation.
3. **Inferred by the agent** — when the user has no schema, the agent samples the documents,
   proposes types, and writes the confirmed result with an extra marker field:
   `"generated_by": "agent"`. Validation treats an inferred schema exactly like an authored one.

## schema.json

```json
{
  "entity_types": ["Person", "Organization", "Location", "Technology"],
  "relation_types": [
    "LOCATED_IN",
    {"name": "WORKS_AT", "subject_types": ["Person"], "object_types": ["Organization"]},
    {"name": "FOUNDED",  "subject_types": ["Person"], "object_types": ["Organization", "Technology"]}
  ],
  "max_triplets_per_doc": 100
}
```

- `entity_types` — allowed values for `subject_type` / `object_type`. Use CamelCase
  (they become Neo4j node labels).
- `relation_types` — each entry is either a plain string (no endpoint constraints) or an object
  with `name` and optional `subject_types` / `object_types` (domain/range constraints).
  Use UPPER_SNAKE_CASE (they become Neo4j relationship types).
- `max_triplets_per_doc` — optional; a prompt-supplied cap overrides it.
- All fields are optional. An empty/absent `entity_types` means any type is allowed;
  same for `relation_types`.

## Semantics of the cap

`max_triplets_per_doc` is a **salience budget**, not a hard stop: the budget is divided evenly
across a document's chunks (minimum 5 per chunk), and within each chunk the agent extracts only
the most important facts up to that budget. The whole document is always read; minor facts are
what gets dropped, not trailing content.
