---
title: "Stable entity types + required fields"
status: final — author sign-off 2026-09-16 on all 3 forks; fork 3 explicitly deferred to item 9
date: 2026-09-16
scope: "todo.md item 4 of 10 — 'Stabile Codex-Entitäten und Pflichtfelder definieren'"
---

# Entity model proposal

Builds on item 2 (authority matrix — direction already set: retire the
flattened `kind=concept` bucket) and item 3 (drift findings — the stale
Slot-16 entry, the `R-N`/`DR-N` naming collision). This is the design step
todo.md's migration rules explicitly gate before any folder gets created —
nothing here moves a file or touches the graph.

## A real constraint this proposal has to design around

`CodexEntry.kind` is a **closed engine-level enum** (Spec 132: `{concept,
location, faction, artefact, minor-character}`), not a repo config value —
`CLAUDE.md` §3 states it as a hard constraint, not a convention. Whether
this repo can request a 6th `kind` value from the engine, or whether the
enum is truly fixed, could not be checked this session (no agency MCP/CLI
access — same limitation as item 3's deferred fix). So this proposal is
**two-phase by design**, not a guess about engine internals:

- **Phase A (ships now, no engine change needed)**: replace the free-text
  `**Kategorie:**` body convention with a **structured, closed-vocabulary
  `entity_type` field** stored the same way `Kategorie:` is today (first
  body line, machine-parseable) — same mechanism, just formalized:
  enumerated values instead of freeform text, and a defined "which type"
  decision per entry instead of 89 entries with no marker at all.
- **Phase B (needs verification next session)**: run `agency_doctor` /
  `get_schema` on `create_codex_entry` to check whether `kind` itself is
  extensible. If yes, migrate `entity_type` values into real `kind` values
  over time. If no, Phase A is the permanent structure, which is fine — the
  authority matrix only requires *stable, queryable* entity types, not that
  they live in one specific engine field.

## Proposed entity types (Phase A: `entity_type` values)

Derived from the 16 `Kategorie:` values found in item 1's census (416
entries carried one; 89 more `concept`-kind entries carried none — see
Fork 2 below), collapsed where two labels described the same underlying
thing:

| `entity_type` | absorbs (Kategorie: label → count) | what it is |
|---|---|---|
| `narrative-constraint` | rule (99), guidance (25), defect (15) | a binding drafting rule — the R-/DR-rule series, R-rules referenced from `lint_chapter.py`, "never do X" constraints |
| `motif` | motif (24), theme (14), voice (10) | a recurring image, thematic thread, or voice/register marker tracked across chapters |
| `philosophy-entry` | philosophy (35) | DKT/philosophical substrate concepts (never dumped directly into prose per `CLAUDE.md` §8) |
| `technique` | technique (8), system (7) | a craft/mechanism note — narrative technique or an in-world system description that isn't itself a `WorldAxiom` |
| `note` | note (86) | genuinely miscellaneous — kept as its own type rather than forced into one of the above; candidate for a later pass to re-triage individually, not blocked on this proposal |
| `sensorik` | sensorik (3) | sensory-palette entries (already called out by name in `CLAUDE.md` §4/§8 as `sensorik`/world entries) |
| `structural-note` | structure (11), question (8) | open structural questions and structure-adjacent notes — kept together since both are working-notes rather than locked content |
| `unclassified` | *(none — 89 `concept`-kind entries with no `Kategorie:` marker)* | real, queryable "needs triage" state — makes the gap visible and countable instead of a silent blank; not a blocker on shipping Phase A |
| *(unchanged)* | `location`, `faction`, `artefact`, `minor-character` | the 4 existing clean `kind` values (97 entries) — not touched by this proposal |

`character` (19 entries, lowercase, distinct from the `minor-character`
`kind`) is **not** given a new `entity_type` here — it's evidence for the
still-pending Character ontology (Spec 132 "Slice 2," an engine-level
change, out of this repo's hands) and should stay flagged as `concept` /
`entity_type: character-note` until that ships, not quietly folded into
`minor-character` (which is a different, already-working thing).

## Required fields

**Universal** (every `CodexEntry`, unchanged from today): `id`, `slug`,
`name`, `kind`, `novel`, `triggers`. Adding: **`entity_type`** (Phase A,
required, closed enum above) and **`source`** (already present as a
`## Quelle: <path>` body line for most entries — promoting it to a
first-class required field, since item 3's drift finding exists specifically
*because* there's no structured way to ask "which entries cite this Canon
file" without parsing body text).

**Knowledge-dimension fields** (`todo.md` architecture question 3 —
`introduced_in`, erzählerische Gültigkeit, `writer_safe_from`, `revealed_in`,
Figurenwissen), mapped concretely:

| todo.md term | field | applies to | meaning |
|---|---|---|---|
| `introduced_in` | `introduced_in: <chapter/scene id>` | entities with a canon origin point (locations, factions, axioms, narrative-constraints, motifs) | where the entity is first canonically established — authorial fact, not reader-facing |
| erzählerische Gültigkeit | `valid_chapters: <range \| "all">` | entities whose rule/fact only holds for part of the book (e.g. the Akt-I AEGIS-naming-ban from item 3, valid Kap 1–13 only) | when the entity's stated content is actually in force — distinct from when it's revealed |
| `revealed_in` | `revealed_in: [<scene id>, …]` | entities that are a plot disclosure, not backstage rule (events, some motifs) | which scene(s) disclose this to the **reader** |
| `writer_safe_from` | `writer_safe_from: <chapter number>` | any entity with reveal-timing sensitivity | earliest chapter a **drafting agent** may be shown this entity — the actual knowledge-fence field the practice test ("Kapitel 3 bearbeiten … ohne Wissen aus Kapitel 20") needs |
| Figurenwissen | *(no new field — already solved)* | facts a **character** knows | this is a relationship, not an entity attribute: item 2 already adopted `KnownFact` + `KNOWS`/`LEARNED_IN` edges for exactly this. A `CodexEntry` doesn't need a "who knows this" field; a fact does, via the graph edge |

`writer_safe_from` is not optional-in-name-only: it's the field the
project's own practice test depends on, and today **no entity has one** —
every existing knowledge fence (`what_does_X_know_as_of`) works off
`StoryTimeEvent`/`Scene`/`KnownFact`, not off `CodexEntry`. A
`narrative-constraint` or `motif` entity (e.g. "Slot-16 Hard-B lock") has no
mechanism today to say "don't surface this before Kap 5" — it's either
fully visible or not, which is exactly the "no normal workflow loads the
full 292 KB glossary" problem item 1 measured.

## Decisions taken (2026-09-16, author sign-off)

1. **Entity-type list**: accepted as proposed (the 8 new `entity_type`
   values + 4 unchanged `kind` values above). This is now the target
   structure for items 6–10.
2. **The 89 `concept`-kind entries with no `Kategorie:` marker**: given the
   real `entity_type: unclassified` value (added to the table above) rather
   than silently defaulting into `note` or blocking the rollout on manual
   triage. `unclassified` is itself queryable, so a future session can find
   and triage all 89 in one pass without them having been invisible in the
   meantime.
3. **`R-N` vs `drafting-rule-dr-N`**: **deferred to item 9** ("Bestehende
   Skills, Commands und Skripte gegen das neue Modell prüfen"). Neither
   merging nor renaming is decided yet — item 9 needs to see how
   `lint_chapter.py`, `CLAUDE.md`, `drafting-brief.md` and the skills
   actually use each series before that call is safe to make. Until then,
   both series continue to exist as-is; only the mis-citation found in item
   3 was fixed (that was a factual error, not a structural decision).
