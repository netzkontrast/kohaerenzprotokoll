# Wiki log

[Up](index.md)

Append-only record of every operation on the research wiki. One line per
operation, grammar from `schema/conventions.yaml`:

```
## [YYYY-MM-DD] <op> | <title> | skill=<command or program> | sha256=<hash when a page was written>
```

Ops: `ingest`, `promote`, `understand`, `question`, `clarify`, `tetraframe`,
`query`, `lint`, `health`, `claim`. Read the tail with
`grep "^## \[" Wiki/log.md | tail -20`. Never rewrite a line; a correction is a
new line.

## [2026-09-16] health | wiki skeleton rendered, zero pages | skill=scripts/render_wiki_views.py

## [2026-09-16] health | navigation and page-boundary contract audited | skill=scripts/render_wiki_views.py

## [2026-09-16] health | context routing and maintenance skill audited | skill=wiki-maintenance
