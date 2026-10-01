# 021 — `SPEC.md` is the project's architecture; E4 may run; `GOAL.md` is annotated

**Date:** 2026-10-01 · **Decided by:** the author · **Status:** in use

## What was asked

The architecture session (PR #139) wrote `SPEC.md` as a recommendation and put three questions in
`Plan/questions-for-the-author.md`: adopt the spec, allow its one model experiment (E4), and what to do with
`GOAL.md`. The author:

> Plan/questions-for-the-author.md ja zu allem

asked which „alles" meant, and chose **the three architecture questions only** (2026-10-01). Every other line of
that file stays open as it was: the novel's questions, the reading pause, and every consent to send text to a
third party.

## What was chosen

1. **`SPEC.md` is adopted.** Its migration order (§9) is binding. Each step is one PR, offline, and reverted by a
   revert. Step 1 is built (`scripts/benchset.py`, `Plan/eval/retrieval-cases-v1.json`). Its marks keep their
   meaning: what was marked *[migrate]* becomes *[built]* only when the step lands.
2. **E4 may run** (§9 step 8): fixed pack against bounded expansion against RLM over chunks, on the same questions,
   at equal total cost. Only evidence an agent actually read is scored, and invented evidence is refused. Limits:
   - Claude through `claude -p` only (decision 011), one call at a time, every call recorded;
   - **$20 for the whole experiment**, checked before each call; the run stops when the next call could pass it;
   - not before steps 2 and 4 have landed, so that it scores against the frozen set through the one pack contract.
     Running it earlier would measure the defects §4 repairs.
3. **`GOAL.md` is annotated, not rewritten.** It stays the author's brief of 2026-09-23. A dated block at its head
   names what has changed since: decision 006 suspends its tiers and „newer wins"; the working agreement replaces
   automatic adjudication; the agency spec it points to was superseded on 2026-06-09; `SPEC.md` is the architecture.
   Its line „`SPEC.md` existiert nicht" is corrected in place.

## What was rejected

- **A blanket yes to the whole file.** It would have lifted the reading pause and sent corpus text to OpenRouter, Jev
  and a speech service with no named recipient. It would also have run HyperExtract over 528 documents (about $190 a
  contract), and it would have answered novel questions that have options, not a yes. None of that was meant.
- **Running E4 now.** Without the frozen set and the single pack it would compare controllers on a moving gold and
  three budget units.

## What would change our mind

- E4 finding that an adaptive controller reaches more read gold at equal cost, with no invented evidence admitted, on
  cases outside the circular bench. Then §8's main choice is reversed, as the spec says.
- A migration step that cannot meet its acceptance without widening. Then it goes back to the author before it lands.
