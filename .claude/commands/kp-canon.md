---
description: >-
  Fold Canon/ documents into Graph/ — the author-locked provenance layer — by
  way of the extraction manifests, then re-render the Codex views. Re-running
  is safe; the ingest is idempotent.
argument-hint: "[--dry-run]"
---

# Canon → Graph

`Graph/` holds the novel's facts: codex entries, world axioms, chapters,
scenes, beats, story-time events, research claims, recorded decisions. They are
seeded from `Canon/` through the extraction manifests in `Plan/ingest/`.

```bash
python3 scripts/ingest_canon.py        # manifests -> Graph/nodes/*.jsonl
python3 scripts/render_codex_views.py  # Graph/ -> Codex/*.md
python3 scripts/kp_check.py            # confirm nothing broke
```

Re-running is safe. Every node id is derived from its label and natural key —
a codex slug, a chapter number, an axiom's text — so an operation that ran
before finds its record instead of minting a second one. A clean re-run reports
zero new nodes and zero new edges.

## When to run it

Only when a `Canon/` document changed, and only after the change is the
author's decision. `Canon/**` is author-owned; this command reads it and never
writes it.

## Adding one fact by hand

`Graph/nodes/*.jsonl` is plain text the author owns. A new codex entry is one
line, and `tools/kpgraph/writer.py` does the id minting and edge threading:

```python
from tools.kpgraph.writer import GraphWriter
w = GraphWriter(".")
w.apply("create_codex_entry", {"slug": "…", "name": "…", "kind": "concept",
                               "body": "…", "novel_id": "novel:9d170c31"})
w.flush()
```

`kind` is a closed set: `concept`, `location`, `faction`, `artefact`,
`minor-character`. Anything else is stored as `concept` with its original
category as the first body line, `**Kategorie:** <kind>`. Re-render the Codex
views afterwards and commit both.

## What this command never does

- It never promotes research into Canon. That path is
  `/research-ingest` → `/kp-promote` → an author decision.
- It never edits `Codex/*.md` by hand. Those are generated; change the graph
  record and re-render.
- It never resolves a contradiction it finds. That is `/kp-decide`.
