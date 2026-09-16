---
description: >-
  Ingest new source material into the Kohärenz Protokoll codex: extract
  entities, write an extraction manifest, seed the provenance graph through
  capability verbs, re-render Codex/ views, update indexes.
  Usage: /ingest [source file or directory]
argument-hint: "[source file path or directory]"
---

# Ingest — Source → Manifest → Graph → Codex views

You are processing new source material into the project's codex. In this repo
the "wiki" is the provenance graph (`.agency/session.db`, ~600 CodexEntries,
StoryTimeEvents, WorldAxioms) plus `Canon/` as the normative corpus; the
Markdown views in `Codex/` are rendered from the graph, never written by hand.
A single source may touch dozens of entries. Follow this sequence exactly.

## Step 1: Read the Source Fully

Read the ENTIRE source document — no skimming, no 200-line cutoff. Use
`/deep-reading` for a content map if it is long. Note the source path: it
becomes `source_uri` on claims and the `## Quelle:` line in codex bodies.
Determine where the source sits in the hierarchy (PROJECT_REFERENCES.md):
Manuscript > Plan/drafting > Canon (storyform-und-outline wins) > NCP > Legacy.
A source below an existing document cannot overrule it — flag, don't overwrite.

## Step 2: Entity Extraction

List every distinct entity that should have a codex entry, axiom, event or claim:

| Entity | Kind | Kategorie | Exists in graph? | Action |
|--------|------|-----------|------------------|--------|
| [name] | concept / location / faction / artefact / minor-character | term / rule / motif / voice / … | yes / no / partial | create / update / skip |

`kind` is the closed 5-value enum (CLAUDE.md §3); the original category goes
into the first body line as `**Kategorie:** <kind>`. Check existence against
ground truth, not memory: `scripts/wiki_fts.py search "<terms>" --scope codex`,
`list_codex_entries(novel_id)`, or read-only SQL on `.agency/session.db`.
World rules → `WorldAxiom` (severity hard|soft, under the right World).
Dated story facts → `StoryTimeEvent` (`when_story`, optional scene).
Verifiable real-world facts → `NovelClaim` (domain from the 10 RESEARCH_DOMAINS).

Pause here. Present the extraction plan before writing anything.

## Step 3: Write the Manifest (after approval)

Write `Plan/ingest/<source-slug>.extraction.json` in the same shape as the
existing manifests (see `Plan/ingest/begriffe.extraction.json`). Preserve the
source's wording faithfully — German stays German; do not summarise, do not
merge two entities into one entry. Keep `[K]/[V]/[S]/[L]` markers in bodies.

## Step 4: Seed the Graph

Preferred: `python3 scripts/ingest_canon.py` (idempotent against existing slugs,
retries transient engine failures). Fallback for small batches: an `execute`
block chaining `capability_novel_create_codex_entry` / `update_codex_entry` /
`create_world_axiom` / `record_story_event` / `capture_claim` (≤45 calls per
block; a failed call aborts the rest but earlier writes persist — re-query
before re-running).

## Step 5: Re-render and Cross-Link

- `python3 scripts/render_codex_views.py` → refreshes `Codex/GLOSSARY.md`,
  `MASTER-TIMELINE.md`, `WORLD-AXIOMS.md`.
- Tune noisy triggers with `update_codex_entry` so `match_codex_entries` stays useful.
- If the source is a new canon document: add it to `Canon/README.md`'s table
  and to `.claude/skills/PROJECT_REFERENCES.md` (that file first, then skills).

## Step 6: Verification

Run `/verifying-completion` on everything created or modified. Run
`/cross-checking` on every new term that already appears in chapter prose.

## Step 7: Log

Append one line per source to `Plan/sessions/<YYYY-MM-DD>-learnings.md`
(create the file if the session has none) and record a `reflect_note`
(scope `project`) so the graph carries the lesson.

## Rules

- Do NOT summarise source content — preserve faithfully
- Do NOT merge two entities into one entry
- Flag contradictions with `<!-- REVIEW: conflicts with [file] -->` in Plan/ docs,
  or as a `[V]` note in the manifest — never silently "fix" Canon
- Present the extraction plan before writing anything
- New entries are proposals until the author promotes them; Canon stays normative
