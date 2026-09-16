---
name: compiling-entities
description: >-
  Compiles a comprehensive entry for a named entity by scanning ALL files,
  gathering every mention, and assembling a structured profile. Use when building
  out a full entry for any character, species, location, or concept, or when user
  says "compile", "flesh out", "full entry for", or "everything about [entity]".
  Does NOT extract multiple entities from one source — use /extracting-entities.
model: sonnet
effort: high
context: fork
---

# Compiling Entities

Assemble all information about a named entity from across the entire repo.

## Process

1. Search `python3 scripts/wiki_fts.py search "<entity>" --scope codex --limit
   5`, open the matching detail page and query the graph body when needed; then
   grep Canon/, Plan/ and chapter prose; carry `[K]/[V]/[L]` markers per fact
2. Read FULL content of every file mentioning the entity
3. Compile into structured profile with sources cited
4. Flag contradictions between sources
5. Present for author review — do NOT write without approval

When the approved target is a research-wiki concept, hand structural writing
to `wiki-maintenance`: use the canonical `concepts/<kind_detail>/<slug>.md`
path, respect the concept page budget, and split distinct entities instead of
building an omnibus page.

## Out of Scope

Does NOT extract multiple entities from one source (use /extracting-entities).
Does NOT write original content (use /writing-worldbuilding).
