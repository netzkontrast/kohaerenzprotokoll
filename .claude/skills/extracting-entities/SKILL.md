---
name: extracting-entities
description: >-
  Extracts individual entities from a large source document and creates separate
  .md files for each one. Use when a source contains multiple distinct entities
  that should each have their own file, or when user says "extract", "pull out
  entities", "split this file", or "create files from this source". Does NOT
  compile scattered info about one entity — use /compiling-entities for that.
model: sonnet
effort: medium
---

# Extracting Entities

Pull distinct entities from a source document into individual files.

## Process

1. Read the ENTIRE source file
2. Identify every distinct entity needing its own file
3. Present extraction plan for approval before writing
4. Extract into a `Plan/ingest/<source>.extraction.json` manifest (same shape as
   the existing ones) and seed the graph via `scripts/ingest_canon.py` — see `/ingest`

## Rules

- One entity per file
- Never write files until extraction plan is approved
- Preserve source content faithfully — do not summarize
- For Wiki output, each extracted entity gets its own stable slug and canonical
  partition; use `wiki-maintenance` for moves, splits, and rendered indexes.

## Out of Scope

Does NOT compile scattered info about one entity (use /compiling-entities).
Does NOT write original content (use /writing-worldbuilding).
