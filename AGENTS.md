# Kohärenz Protokoll — agent rules

## Wiki compass

Read `Wiki/SCHEMA.md` before changing `Wiki/**`; the YAML under `Wiki/schema/`
is the machine-readable authority.

- Start navigation at `Wiki/index.md`; every content root and occupied
  partition has a rendered `README.md`.
- Page entities are `source`, `concept`, `question`, and `synthesis`. Keep one
  semantic entity or one focused question per page.
- Store pages at exactly one canonical partition:
  `sources/<category>/`, `concepts/<kind_detail>/`, `questions/<axis>/`, and
  `syntheses/<YYYY>/`. Candidates mirror this below `candidates/<kind-dir>/`.
- Prefer a small linked page over a large mixed page. Budgets live in
  `Wiki/schema/entities.yaml`; exceeding `max_words` fails the wiki lint.
- `index.md`, `concept-table.md`, `context-map.md`, `graph/**`, and navigation
  `README.md` files are rendered. Edit pages, then run
  `python3 scripts/render_wiki_views.py`.
- Use `[[slug]]` for wiki pages, `codex:<slug>` for the generated domain
  glossary, and `canon:<file>#<heading>` for Canon. See `Wiki/GLOSSARY.md` for
  the small operational vocabulary.
- For manuscript work, read `Wiki/context-map.md` first. Filter for the target
  chapter, require `spoiler_until <= target chapter`, then load only matching
  headings. Open cited source lines only for evidence; do not load full raw
  sources by default.
- Wiki maintenance changes navigation and structure, never authority. Do not
  silently change `Canon/`, NCP files, or manuscript facts.
- Finish with `python3 scripts/wiki_lint.py --health`,
  `python3 scripts/render_wiki_views.py --check`, and relevant tests.
- Treat `duplicate-slug`, `navigation-link`, `page-location`, `page-size`,
  `context-window`, and `index-sync` findings as structural blockers.

For moves, splits, index repair, or schema evolution, use
`.claude/skills/wiki-maintenance/SKILL.md`.
