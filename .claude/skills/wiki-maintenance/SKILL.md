---
name: wiki-maintenance
description: >-
  Maintains the Kohärenz Protokoll research wiki structure, navigation, page
  boundaries, indexes, links, and schema alignment. Use for wiki cleanup,
  moving or splitting pages, fixing navigation, evolving page kinds or
  partitions, full wiki audits, context-loading improvements, or repairing
  wiki lint drift. Never hand-edits the generated Codex: its structure is
  declared in Graph/schema.yaml and written by the renderer. Does not decide
  Canon or rewrite research claims.
---

# Wiki Maintenance

Maintain a small-page, locally navigable wiki without changing epistemic
authority.

## Read first

1. `AGENTS.md` — compact repository rules.
2. `Wiki/SCHEMA.md` and the relevant files in `Wiki/schema/` — authoritative
   structure and policy.
3. `Wiki/GLOSSARY.md` — operational terminology.
   To find a page rather than guess its path: `python3 scripts/wiki_fts.py
   search "…"` searches Wiki, Canon and Sources at heading level.
4. For a full audit, read `references/audit-runbook.md`; for any move, split,
   new partition, or migration, also read `references/structure-contract.md`.

## Invariants

- One page represents one semantic entity or one focused question.
- A promoted page has exactly one partition:
  `sources/<category>/<slug>.md`,
  `concepts/<kind_detail>/<slug>.md`,
  `questions/<axis>/<slug>.md`, or
  `syntheses/<YYYY>/<slug>.md`.
- Candidates use `candidates/<kind-dir>/<partition>/<slug>.md`.
- Slugs remain globally unique and stable across moves.
- `index.md`, `concept-table.md`, `graph/**`, and navigation `README.md` files
  are renderer-owned. Never hand-edit them.
- A structural move preserves frontmatter, citations, lifecycle state, log
  history, and wiki links. A split preserves every claim and citation and
  introduces explicit links between the resulting pages.
- Never use maintenance as permission to resolve contradictions, promote a
  page, or change Canon/NCP/manuscript facts.
- Every Markdown link in the navigation surface resolves, and no rendered
  partition `README.md` remains after its partition disappears.
- Pages used for manuscript work expose a ≤40-word context summary, scope,
  priority, chapter window, and spoiler ceiling. The context map contains
  routing metadata only, never page bodies.
- Directory names encode only schema-defined partitions, never ad-hoc topics.
  A topic is a page, tag, or link unless `Wiki/schema/*.yaml` defines it as a
  partition dimension.
- `Codex/**` is renderer-owned. It is partitioned and navigable — root files
  route, `entries/`, `axioms/` and `timeline/` hold one retrievable unit per
  file — but every one of those files is written by
  `scripts/render_codex_views.py` from `Graph/`. Never move, split or edit one.
  To change the structure, change the rules in `Graph/schema.yaml` and
  `tools/kpcodex`, then re-render; to change content, change the record. A file
  under `Codex/entries/_misfiled/` is a record whose `**Kategorie:**` is not in
  the schema — report it, and fix the record rather than the rendering.
  Background and measurements: `Plan/wiki/codex-context-inventory_2026-09-16.md`.

## Choose the operation

- **Audit** — inspect every Wiki Markdown page, rendered view, schema file,
  template, and structural rule; use the full audit runbook.
- **Move** — use only when kind/partition and path disagree. Preserve the slug
  and repair all inbound links in the same change.
- **Split** — use when a page crosses its hard budget or contains independently
  addressable entities. Keep one semantic entity per result page.
- **Schema change** — use when no existing kind or partition can represent the
  content. Update YAML, implementation, templates, documentation, and tests as
  one atomic contract change.
- **Navigation repair** — change source pages or the renderer; never patch a
  generated index directly.
- **Codex structure change** — a change to `Graph/schema.yaml` plus
  `tools/kpcodex`, never to the rendered files. Add the category or the rule,
  re-render, and prove it with `scripts/render_codex_views.py --check` and
  `tests/test_kpcodex.py`. Do not combine it with Wiki cleanup.

## Workflow

1. Run `python3 scripts/wiki_lint.py --health` for the tight loop; inspect
   `index.md`, every affected local index, and the root system pages
   (`overview.md`, `GLOSSARY.md`, `SCHEMA.md`, `log.md`, `concept-table.md`).
2. Classify each affected file by kind and derive its partition from
   frontmatter. Do not invent topical folders.
3. If a page exceeds its hard budget, split it at a stable semantic boundary;
   if it exceeds only the warning threshold, prefer splitting when sections
   have independent identities or inbound links.
4. Make page/schema/tool changes together. When the contract changes, update
   YAML first, then parsers/renderers/tests and concise human documentation.
5. Run `python3 scripts/render_wiki_views.py`; do not edit rendered output.
6. Confirm there are no duplicate slugs, dead navigation links, stale local
   indexes, mispartitioned pages, invalid context windows, or pages above
   their hard budget.
7. Finish with `python3 scripts/kp_check.py`, which runs wiki health, both
   view renderers, the source manifest, claim provenance, both storyforms,
   the world axioms and chapter drift in one command. Then the tests that
   cover what you touched:
   `pytest tests/test_wiki_lint.py tests/test_wiki_views.py tests/test_wiki_schema.py tests/test_wiki_fts.py tests/test_research_ingest.py -q`.

For manuscript-context work, follow the retrieval ladder in
`references/context-loading.md`. Stop if the target chapter is unknown and a
spoiler boundary would change what may safely be loaded.

## Stop and ask

Ask the author before continuing when a structural choice would change a
claim's authority, a split cannot preserve claim-to-citation provenance, two
pages appear to represent the same entity but disagree, or a new partition
would be based on editorial taste rather than stable metadata.

## Output

Report the operation mode, files inspected, moved/split pages, navigation and
contract changes, exact validation commands/results, and every authority or
migration question deliberately left untouched.
