---
name: codex-maintenance
description: >-
  Maintains or migrates the generated Kohärenz Protokoll Codex structure,
  renderers, compatibility indexes, graph-to-file projections, retrieval paths,
  and Codex consumers. Use for Codex cleanup, splitting generated views,
  renderer drift, Codex search, or Codex schema migration. Do not use for
  research Wiki organization or for deciding Canon facts.
---

# Codex Maintenance

Keep `Codex/` a small-page, context-efficient, reproducible projection of the
provenance graph.

## Read first

1. Root `todo.md` and `CLAUDE.md`.
2. `docs/codex-architecture.md`.
3. `scripts/render_codex_views.py` and every affected consumer.

## Invariants

- `.agency/session.db` supplies entities and provenance; `Canon/` remains
  normative prose. `Codex/` is a generated view, never a third authority.
- Never hand-edit a Codex page. Change graph data through capability verbs or
  change the renderer, then regenerate all affected views.
- One CodexEntry renders to one `glossary/<kind>/<slug>.md` page. Root files are
  compact compatibility/navigation indexes, not content stores.
- Directory names come from stable graph fields. Do not derive durable folders
  from guessed themes or incidental prose.
- Missing spoiler or chapter metadata is a safety gap. Expose it; never infer a
  safe value from absence.
- Preserve legacy Root paths until every consumer has migrated and a separate
  decision authorizes removal.
- A migration updates renderer, retrieval, protections, consumers,
  documentation, and tests together.

## Modes

- **Audit:** inventory files, graph labels/properties, sizes, generators and all
  consumers before proposing a structure.
- **Renderer change:** modify projections, regenerate, reject unexpected paths,
  and verify a second render is identical.
- **Consumer migration:** replace omnibus reads with FTS, exact detail pages or
  graph verbs; retain compatibility links where useful.
- **Graph schema migration:** stop for author approval of field semantics and
  migration/backfill rules before writing graph data.

## Workflow

1. Confirm the operation mode and authority boundary.
2. Inventory current graph fields and repository consumers; do not design from
   filenames alone.
3. Make the smallest compatible renderer change. Keep Root indexes compact.
4. Regenerate with `python3 scripts/render_codex_views.py`.
5. Build and check retrieval with `python3 scripts/wiki_fts.py build` and
   `doctor`; test a narrow `--scope codex` query and a chapter-gated
   `scripts/codex_context.py` query.
6. Run `python3 scripts/render_codex_views.py --check`, relevant tests,
   compilation, link checks and `git diff --check`.
7. Report generated/moved/removed views, consumer changes, retrieval evidence,
   and unresolved graph metadata gaps.

## Stop and ask

Ask before changing Canon, assigning authority, defining the semantics of a new
graph field, backfilling spoiler/knowledge values, or deleting compatibility
paths. A renderer refactor does not authorize any of those decisions.
