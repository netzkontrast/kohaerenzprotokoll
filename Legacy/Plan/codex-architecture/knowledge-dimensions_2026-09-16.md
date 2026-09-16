---
title: "Knowledge dimensions — objective truth, character/reader knowledge, reveal, temporal validity"
status: final — 4 of 5 dimensions already covered by item 4; 1 real gap found, not fixed
date: 2026-09-16
scope: "todo.md item 5 of 10 — 'Wissensdimensionen sauber trennen'"
---

# Knowledge dimensions

`todo.md` names 5 dimensions to separate cleanly: objektive Wahrheit,
Figurenwissen, Leserwissen, erzählerische Enthüllung, zeitliche Gültigkeit.
[entity-model-proposal_2026-09-16.md](entity-model-proposal_2026-09-16.md)
(item 4) already designed fields/mechanisms that map onto 4 of the 5 — this
formalizes that mapping rather than re-deriving it, and states the one real
gap found in the process.

| dimension | mechanism | already exists? |
|---|---|---|
| **Objektive Wahrheit** (objective truth — what's actually canonically true, independent of any character or reader) | the `CodexEntry`/`WorldAxiom`/`StoryTimeEvent` itself, `source` field pointing at its Canon citation | yes — this is what the whole Codex layer already is |
| **Figurenwissen** (character knowledge — what a specific character knows, as of a specific scene) | `KnownFact` node + `KNOWS`/`LEARNED_IN` edges, queried via `what_does_X_know_as_of(character_id, scene_id)` | yes, mechanism exists; **adopted for actual use** in item 2 (previously designed but zero instances) |
| **Zeitliche Gültigkeit** (temporal validity — when a rule/fact is actually in force, independent of when it's revealed) | item 4's `valid_chapters` field | yes — item 4 |
| **Erzählerische Enthüllung** (narrative reveal — the event/mechanism by which something becomes known to the reader) | item 4's `revealed_in` field (which scene discloses this entity) + the existing `reveal_in_scene` verb (event → scene edge) | yes — item 4, plus an already-existing verb |
| **Leserwissen** (reader knowledge — the reader's *cumulative* knowledge state as of a given scene, i.e. "everything revealed up to here") | — | **gap, see below** |

## The gap: no reader-knowledge-as-of query

Character knowledge has a real, queryable aggregate:
`what_does_X_know_as_of(character_id, scene_id)`. Reader knowledge has no
equivalent — only the per-entity `revealed_in` field (item 4) and the
existing `list_reveals_in(scene_id)` verb (what *one* scene discloses)
exist. Neither aggregates "everything the reader has been told by the time
they reach scene N," which is a different, narrower question than
character knowledge (the reader typically knows less than any POV
character, and — critically for spoiler-safety — different from what a
*drafting agent* should be shown, which is `writer_safe_from`, an authorial
constraint, not a reader-experience one).

This matters concretely for the guiding practice test ("Kapitel 3
bearbeiten, ohne Wissen aus Kapitel 20 zu verwenden"): `writer_safe_from`
already answers *what an agent may be shown*. It does not answer *what the
reader would already know at this point*, which is a craft question
(pacing, dramatic irony, foreshadowing payoff) editorial work on a chapter
still needs. `writer_safe_from` is a stricter, mechanical fence;
reader-knowledge-as-of is the softer question `novel-architect-scene` /
`scene-bridge-auditor` implicitly reason about today without a queryable
aggregate behind it.

**Not fixed here** — this is a new capability (a verb, e.g.
`what_does_reader_know_as_of(scene_id)`, aggregating `revealed_in` edges
across all entities up to the given scene's narrative position, the same
way `list_story_events_up_to` aggregates `StoryTimeEvent`s) that would need
engine-side implementation, out of scope for a Plan/ document. Recorded as
a candidate for item 10 ("Separaten `codex-maintenance`-Skill... entwerfen")
or a future engine capability request — not for items 6–9, which build the
structure this gap doesn't block.

## What this settles

All 5 dimensions now have a named mechanism or a named, scoped gap — no
dimension is left conflated with another. Items 6–9 can proceed using
item 4's field set without re-opening this question.
