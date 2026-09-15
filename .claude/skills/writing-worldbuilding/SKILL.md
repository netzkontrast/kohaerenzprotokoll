---
name: writing-worldbuilding
description: >-
  Writes new worldbuilding content: civilizations, characters, locations, factions,
  events, languages, or narrative elements. Use when creating new entries, expanding
  existing ones, or when user says "create", "write", "add", "flesh out", "build",
  or "expand" for any non-science content. Does NOT write science files — use
  /writing-science for that.
model: sonnet
effort: high
---

# Writing Worldbuilding

Write new non-science worldbuilding content following repo conventions.

## Prerequisites

1. Read CLAUDE.md, `WRITING.md` and `.claude/skills/PROJECT_REFERENCES.md`
2. Read `references/writing-standards.md` for prose anti-patterns
3. Read the project skill that owns the topic: novel-architect-world (Kernwelten,
   sensorics, axioms), novel-architect-character (Anteile, Sprach-DNA),
   novel-architect-scene (chapter prose — this skill does NOT draft chapters)
4. Search `Codex/GLOSSARY.md` and grep Canon/ + Plan/ for existing entries —
   no new lore to patch a continuity problem an existing source already resolves
5. Check `Codex/WORLD-AXIOMS.md` for the rules the content must obey

## Process

1. Worldbuilding content is a **codex entry**, not a loose file: mint it with
   `create_codex_entry(novel_id, slug, name, kind, body, triggers)` in an
   `execute` block. `kind` ∈ {concept, location, faction, artefact, minor-character};
   the original category goes in the first body line `**Kategorie:** <kind>`
2. Body in German, first line after Kategorie: `## Quelle: <file>`; mark
   provenance `[K]`/`[V]`/`[L]` — new lore is `[V]` until the author locks it
3. kebab-case slugs (ASCII: ä→ae, ö→oe, ü→ue, ß→ss); triggers = the surface
   forms prose actually uses, so `match_codex_entries` fires
4. Re-render `Codex/` with `python3 scripts/render_codex_views.py`
5. Flag potential contradictions in a Plan/ note with
   `<!-- REVIEW: potential conflict with [file] -->` — never edit Canon/ silently
6. Worldbuilding must serve a chapter action (world skill operating rule)

## Derivation-First Builds

For civilizations being built from scratch — especially in novel environments
or with non-human species — use `/civilization-build` instead of the scaffold
below. The scaffold's categories (governance, economy) are useful shorthand
for human civilizations in familiar contexts, but they can import assumptions
when applied to novel situations. The `/civilization-build` command ensures
every social structure is derived from biology and environment first.

The scaffold below remains useful for quick expansions of existing civilizations
or for human civilizations in Earth-like contexts where the derivation has
already been done (implicitly, by history).

## Civilization Scaffold

When creating a civilization, address: governance, cultural identity,
economy, technology, internal tensions, external relations, and how
they interpret the universe's fundamental forces.

## After Writing

- `python3 scripts/render_codex_views.py` (refreshes GLOSSARY / MASTER-TIMELINE / WORLD-AXIOMS)
- Dated story facts → `record_story_event`; rules → `create_world_axiom`
- Update `.claude/skills/PROJECT_REFERENCES.md` if the data map changed
- Present for author review — do NOT commit

## Out of Scope

Does NOT write science files (use /writing-science).
Does NOT audit content (use /auditing-canon).
Does NOT design physical world foundations (use /designing-worlds).
