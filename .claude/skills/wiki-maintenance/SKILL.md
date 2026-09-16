---
name: wiki-maintenance
description: >-
  Maintains the Kohärenz Protokoll research wiki structure, navigation, page
  boundaries, indexes, links, and schema alignment. Use for wiki cleanup,
  moving or splitting pages, fixing navigation, evolving page kinds or
  partitions, full wiki audits, context-loading improvements, or repairing
  wiki lint drift. It may plan a Codex migration, but never restructures the
  generated Codex as part of routine Wiki maintenance. Does not decide Canon
  or rewrite research claims.
---

# Wiki Maintenance

Maintain a small-page, locally navigable wiki without changing epistemic
authority.

## Read first

1. `AGENTS.md` — compact repository rules.
2. `Wiki/SCHEMA.md` and the relevant files in `Wiki/schema/` — authoritative
   structure and policy.
3. `Wiki/GLOSSARY.md` — operational terminology.
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
- `Codex/**` is renderer-owned and outside routine Wiki maintenance. Record
  Codex defects and migration proposals, but do not move or split those files
  unless the user explicitly starts a separate Codex migration.

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
- **Codex migration** — separate, explicitly requested project. First produce
  an inventory and migration plan; do not combine it with Wiki cleanup.

## Workflow

1. Run `python3 scripts/wiki_lint.py --health`; inspect `index.md`, every
   affected local index, and the root system pages (`overview.md`,
   `GLOSSARY.md`, `SCHEMA.md`, `log.md`, `concept-table.md`).
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
7. Finish with `python3 scripts/wiki_lint.py --health`,
   `python3 scripts/render_wiki_views.py --check`, and the wiki test suite.

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
