---
title: "Authority matrix — Canon/Codex/Wiki/NCP/graph"
status: final — all 13 rows decided (2 by author sign-off 2026-09-16)
date: 2026-09-16
scope: "todo.md item 2 of 10 — 'Autoritätsmatrix beschließen'"
---

# Authority matrix

Builds on [codex-inventory_2026-09-16.md](codex-inventory_2026-09-16.md)
(item 1). For each information kind: exactly one named authority, per the
task's acceptance criterion ("Für jede Informationsart gibt es genau eine
benannte Autoritätsquelle"). Most rows below **formalize a rule this repo
already enforces** (cited to its source) rather than deciding something new
— those are marked **settled**. Two rows (6, 7) were genuinely new calls
this inventory surfaced; the author decided both 2026-09-16 — see
"Decisions taken" below. **Naming the concrete new entity types is not done
here** — that's `todo.md` item 4 ("Stabile Codex-Entitäten und Pflichtfelder
definieren"), which this row now has explicit direction for.

| # | Information kind | Authority | Everything else is | Status |
|---|---|---|---|---|
| 1 | Structural/storyform meaning (throughlines, signposts, dynamics, story points, which Storyform is heterodox-by-design) | **`Canon/…storyform-und-outline…`** | `ncp.json`/`ncp-b.json` = validated *encoding* of it (must match; drift = bug, not a second opinion) | settled — `CLAUDE.md` Rule 0: "the storyform/outline document is normative" |
| 2 | Encoded storyform state for engine checks (which NCP slot holds which element, do the 11 coherence checks pass) | **`ncp.json`** (Storyform A) / **`ncp-b.json`** (Storyform B) | `Storyform` graph node mirrors it for gate verbs (`novel_coherence_check` etc.) | settled — `CLAUDE.md` §6; never hand-edit, only via `ncp-author`/`storyform-build` |
| 3 | World rules (hard/soft axioms) | **`Canon/…kernwelten-vollständig…`, `…welt-sensorik-drafting…`** | `WorldAxiom` graph nodes are the extracted/validated form; `Codex/WORLD-AXIOMS.md` is a pure render of those nodes | settled — extraction pipeline (`scripts/ingest_canon.py`), confirmed generated-only in inventory §1 |
| 4 | Dated facts / chronology | **`StoryTimeEvent` graph nodes** (not prose narration directly) | Canon prose is the source claim; `Codex/MASTER-TIMELINE.md` is a pure render | settled — same pattern as axioms; MASTER-TIMELINE confirmed 100% generated (inventory §1) |
| 5 | Locations, factions, artefacts, minor-characters (the 4 non-`concept` CodexEntry kinds — 97 entries) | **`CodexEntry` graph nodes**, sourced from Canon extraction | `Codex/GLOSSARY.md` render | settled — clean, already-typed subset of §1's finding, no drift risk |
| 6 | Domain vocabulary / world rules / motifs / themes / voice / technique (the `kind=concept` CodexEntry bucket — 505 of 602 entries, 16 `Kategorie:` values found) | **`CodexEntry` graph nodes**, but the flattened `kind=concept` bucket is retired in favor of real entity types derived from the 16 `Kategorie:` values (candidates: `NarrativeConstraint` ← rule/guidance/defect, `Motif` ← motif/theme/voice, `PhilosophyEntry` ← philosophy, `Technique` ← technique/system; `note` and the 186 `Kategorie:`-less entries need triage first) | `Codex/GLOSSARY.md` render | **settled 2026-09-16 (author)** — direction only; concrete type list + required fields is item 4's job |
| 7 | Character knowledge / reveal state (who knows what fact, as of which scene) | **`KnownFact` graph nodes + `KNOWS`/`LEARNED_IN` edges**, adopted going forward via `record_character_learns` (already documented as scene-writing-loop step 5 in `CLAUDE.md` §4 — it was written but never actually followed) | `what_does_X_know_as_of(character_id, scene_id)` becomes a real knowledge fence, not a documented-but-unused capability | **settled 2026-09-16 (author)** — adopt; not retroactive for existing scenes unless a later session backfills them |
| 8 | Manuscript prose (already-written chapters) | **`Manuscript/…/chapters/*.md`** | nothing outranks it for what's already on the page | settled — `CLAUDE.md`/`PROJECT_REFERENCES.md` top of the source hierarchy |
| 9 | Chapter intent, scene planning, drafting decisions, provisional `[V]` choices | **`Plan/drafting/*` arc plans + decision logs** | — | settled — `PROJECT_REFERENCES.md` §"Source hierarchy" |
| 10 | Research claims about the outside world (physics, philosophy, etc. not yet canon) | **`Wiki/sources/`, `Wiki/concepts/`** (once populated — currently 0 pages) | Canon is `unverified` against them until checked; conflict = open question, no default winner | settled — `CLAUDE.md` §"Wiki compass": D-W12, 2026-09-16 |
| 11 | Operational/process vocabulary (engine terms, workflow terms — not story content) | **`Wiki/GLOSSARY.md`** | `Codex/GLOSSARY.md` stays domain-only | settled — `CLAUDE.md` §"Wiki compass", already stated in prose; this row just adds it to the matrix |
| 12 | Wiki-internal relations (page↔page) vs. novel provenance (chapter↔scene↔axiom↔claim) | two separate stores by design: **`Wiki/graph/edges.jsonl`** for the former, **`.agency/session.db`** for the latter | neither merges into the other | settled — `CLAUDE.md`: "'the graph' always means the provenance graph … it never receives wiki page bodies (D-W2)" |
| 13 | Any `Codex/*.md` or Wiki rendered file (`index.md`, `concept-table.md`, `context-map.md`, partition `README.md`s, `coverage.json`) | **never** an authority — pure projection | source is always the graph/schema behind it | settled — write-denied (Codex) / `writers.yaml` tools-only (Wiki); inventory §1/§2 |

## Decisions taken (2026-09-16, author sign-off)

Both surfaced directly by the inventory, not invented here. Per Rule 0 —
naming new entity types and deciding whether to adopt an existing-but-unused
mechanism are exactly the kind of scope calls that shouldn't be assumed, so
both were put to the author via `AskUserQuestion` before being marked
settled above.

- **Q1 — concept-bucket split**: commit to splitting `kind=concept` into
  real entity types along the `Kategorie:` lines found in the inventory,
  rather than keeping the flattened bucket. The concrete type list, field
  definitions, and a triage plan for the 186 `Kategorie:`-less entries are
  deferred to `todo.md` item 4 — this decision only fixes the *direction*
  so item 4 isn't reopening the question from scratch.
- **Q2 — adopt knowledge-tracking**: `record_character_learns` /
  `KNOWS`/`LEARNED_IN` go from documented-but-unused to actually used going
  forward. This does not retroactively backfill the 15 existing Kap-0
  scenes; whether/how to backfill them is open for whoever next runs the
  scene-writing loop on already-drafted chapters.

## What this settles vs. what it doesn't

This matrix answers "which layer is authoritative," not "what the target
folder/entity structure looks like" (`todo.md` items 4–7) or "how existing
overlaps/drift get resolved" (item 3). Item 3 checked the corpus against
this matrix's rulings, item 4 named the concrete entity types row 6 only
pointed at a direction for, and item 5 mapped the knowledge dimensions row
7's adoption enables — see
[overlaps-drift_2026-09-16.md](overlaps-drift_2026-09-16.md),
[entity-model-proposal_2026-09-16.md](entity-model-proposal_2026-09-16.md),
and [knowledge-dimensions_2026-09-16.md](knowledge-dimensions_2026-09-16.md).
