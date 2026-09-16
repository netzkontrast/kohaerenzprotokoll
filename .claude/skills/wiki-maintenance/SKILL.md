---
name: wiki-maintenance
description: >-
  Maintains the Kohärenz Protokoll research wiki structure, navigation, page
  boundaries, indexes, links, and schema alignment. Use for wiki cleanup,
  moving or splitting pages, fixing navigation, evolving page kinds or
  partitions, or repairing wiki lint drift. Does not decide Canon or rewrite
  research claims.
---

# Wiki Maintenance

Maintain a small-page, locally navigable wiki without changing epistemic
authority.

## Read first

1. `AGENTS.md` — compact repository rules.
2. `Wiki/SCHEMA.md` and the relevant files in `Wiki/schema/` — authoritative
   structure and policy.
3. `Wiki/GLOSSARY.md` — operational terminology.

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

## Output

Report moved/split pages, navigation changes, lint/test results, and any
authority question left untouched for the author.
