# Codex architecture

## Purpose

`Codex/` is a generated, context-efficient projection of the provenance graph.
It is not an independently edited knowledge base and it is not the normative
source for story facts.

## Authority matrix

| Layer | Owns | Must not own |
|---|---|---|
| `Canon/` | approved world, plot, character and terminology decisions | research uncertainty |
| `.agency/session.db` | structured entities, relationships, provenance and versions | a second prose canon |
| `Codex/` | generated, small operational views of graph entities | hand-authored facts |
| `Wiki/` | sourced research, interpretations, questions and syntheses | silent Canon changes |
| NCP | chapter plans and writing constraints | universal world truth |
| Manuscript | the narrated realization | project-wide reference data |

When layers disagree, surface the conflict. Do not repair it by editing a
generated Codex page.

## Generated layout

```text
Codex/
  README.md
  GLOSSARY.md                 compact compatibility index
  MASTER-TIMELINE.md          compact compatibility index
  WORLD-AXIOMS.md             compact compatibility index
  glossary/
    README.md
    <CodexEntry.kind>/
      README.md
      <slug>.md               one graph entity
  timeline/
    README.md
    <phase>.md
  worlds/
    README.md
    <world-slug>.md
  context/
    README.md                 safety limits and missing metadata
```

Directories are derived only from stable graph fields. The renderer may use a
phase as a navigational view, but the phase is explicitly non-normative because
`StoryTimeEvent.when_story` is free text.

## Retrieval contract

1. Build the shared heading index with `python3 scripts/wiki_fts.py build`.
2. For chapter work, route through `Wiki/context-map.md`, then run
   `python3 scripts/codex_context.py "<terms>" --chapter N`.
3. For explicit whole-novel work, use `--whole-novel`.
4. Open only returned files and line ranges.
5. Treat a Codex entry without explicit safety metadata as whole-novel context;
   absence of a spoiler boundary is never permission to load it early.

Root compatibility files exist for old links and human orientation. They must
not grow back into omnibus content.

## Entity boundaries

- `CodexEntry`: one page by stable `kind` and `slug`.
- `StoryTimeEvent`: rendered into a phase view; event identity remains its graph
  ID, not its table row.
- `WorldAxiom`: rendered beneath its related `World`; orphan axioms remain
  visibly unassigned.
- `World`: one page containing its current axioms.

The current graph has no reliable chapter/spoiler properties on CodexEntry or
WorldAxiom. The renderer records this limitation rather than inferring values
from prose. A later graph migration may add `true_from`, `true_until`,
`introduced_in`, `revealed_in`, and `writer_safe_from` after their semantics
are approved.

## Compatibility and migration

The three historical Root files remain generated indices. Consumers that need
content must use FTS, detail pages, or graph verbs. The renderer owns all files
under `Codex/`, detects missing or stale pages, and removes only stale Markdown
inside its declared generated subdirectories.

Validation:

```bash
python3 scripts/render_codex_views.py
python3 scripts/render_codex_views.py --check
python3 scripts/wiki_fts.py build
python3 scripts/wiki_fts.py doctor
```
