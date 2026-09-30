---
name: graph-context
description: Retrieve source-attributed wiki evidence with the local GraphQLite CLI, explore graph neighbours, refresh stale indexes and fetch exact evidence IDs. Use for questions across sources or gathering a small context before a wiki review. Never use before freezing a new document's independent extraction.
---

# Retrieve only the context the task needs

Run from the repository root. Use the pinned interpreter:

```bash
scripts/install.sh graphqlite
.venv-graphqlite/bin/python scripts/kg.py index
.venv-graphqlite/bin/python scripts/kg.py context "<question>" --max-bytes 12000
```

Read the returned evidence, conflicts and questions. `incomplete: true` means
selection or the size cap left candidates out; it is never a completeness claim.
Increase the byte cap or ask a narrower question when the missing coverage matters.
The cap includes serialized JSON and metadata. It is not a model-token count.

For lexical discovery, run `search "<words>" --limit 10`. For a cited graph
neighbourhood, run `around term:<slug> --hops 1 --limit 30`. Fetch complete
quotes with `evidence <returned-id> ...`; take identifiers from output.

If a command reports a stale or absent index, run `index` and retry. An unchanged
index is a no-op; changed inputs rebuild the projection. Edit authoritative
files, never the database. A returned conflict is a record to read, not a
resolved position. The CLI makes no model call and does not infer conflicts.

Keep independent source extraction on the ingest skill's path. This tool serves
existing wiki evidence after extraction, not a substitute for reading a source.

Read `references/cli.md` for command details and limits. Validate changes with:

```bash
.venv-graphqlite/bin/python scripts/kg_selftest.py
python3 scripts/check_skills.py
```

Both graph CLIs share `Plan/derived/ask.db` (schema 2). Initialization builds it once. `:Core` is an alias on typed nodes, not a duplicated graph. Core traversals must filter `r.core = true`; raw corpus queries should name their intended relation types. Old databases require rebuilding; no authored data is migrated.
