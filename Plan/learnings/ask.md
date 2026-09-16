# Learnings — ask (a question → a cited answer)

## Status

**Not run yet.** Pre-registration. There are no term pages to ask.

This is the step the whole wiki exists for, which makes it the one most likely
to be deferred until "the wiki is ready". It should be tried on twenty pages,
not on six hundred, because a retrieval path that fails at twenty fails worse at
six hundred.

## What the step is

Answer a question from the term pages, with the file and line each claim came
from, and never from memory.

## Predictions to test

1. **`grep` is enough for a long time.** A few hundred short markdown pages is
   not a retrieval problem. Predicted: an index earns its existence only when
   grep stops being pleasant, and that point arrives later than instinct
   suggests. The old system built full-text search over a layer with two pages.

2. **The failure mode is a confident answer from memory.** The model knows a lot
   about this project from its context. Predicted: the hard discipline is
   refusing to answer beyond what the pages say, and this needs to be structural
   rather than an instruction — every claim carries a path and a line, and a
   claim that cannot is marked as absent rather than smoothed over.

3. **"The wiki cannot answer this" is the most valuable output.** It names a
   term needing a page, or a source needing fetching. Predicted: early on, most
   questions land here, and that is a working system rather than a failing one.

4. **Answers will want to merge readings, and must not.** P13 forbids merging on
   the page; the same temptation returns at answer time, where it is less
   visible. Predicted: an answer that says "Coheron means X" where two sources
   disagree is the most likely quiet failure of the whole design.

## What we will watch for

- How often an answer needs a source that was never fetched — this is the
  strongest signal for what to fetch next, and it is free.
- Whether citations in answers survive a spot check, or drift by a few lines.
- Whether the author ends up asking questions the term structure cannot serve —
  "what happened in chapter 12" is not a term question, and enough of those
  would mean the unit is wrong.
- Whether answers are worth keeping. The old system had a `Plan/queries/`
  directory with a README and zero filed answers, which suggests the answer is
  usually no.

## Open questions

- **Does an answer become a page?** A synthesis across terms is a new kind of
  artefact. The old schema had a `synthesis` type that was barely used, so the
  default is no — it earns existence by being wanted twice.
- **When does an index become worth it?** The honest trigger is friction, not a
  page count. Recording the moment grep first feels slow is more useful than
  guessing a threshold now.
- **Who asks — the author, or an agent building something?** Different callers
  want different shapes, and the second is the case that justifies structure.

## What stays judgement

- Whether an answer is good enough to act on.
- Whether a disagreement between sources changes the answer or is beside the
  point.
- Whether a gap the wiki reveals is worth closing.
