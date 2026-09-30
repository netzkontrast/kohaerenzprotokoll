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

## The retrieval bench, document by document

*Moved from `CLAUDE.md` on 2026-09-30, verbatim; the numbers are as of the last document it names and no longer checked — `python3 scripts/graphrag.py bench` measures now, and `Plan/runs/baselines.jsonl` has every row.*

`bench` scores retrieval on the 24 cases the wiki
already labels (each question's `raised_by`, each conflict's `pages`), with the
case's own node removed first. Recall@8 is
**53% from the seeds alone and
69% with PageRank** — the graph earns its
step, on cases whose labels were written by the same hand as the
pages. Documents 7–9 added seven of them (C6–C12), the author's C6
decision an eighth (Q5), document 16 a ninth (C13) and document 17 two
more (C14, C15); on the original nine the numbers were 40 and 58.
Document 19 moved them from 48 and 67 by giving C11 three more pages: its
gold set grew from two pages to five, and the case fell from 1.0 to 0.6 with
PageRank. The fall is that label growing; on the labels that did not change,
retrieval rose — C6 from 0.29 to 0.43.
The eleven pages of the 2026-09-25 scan moved PageRank recall from 0.659 to 0.649,
measured against the tree before them. The only case that fell was C11, from 0.6
to 0.4: `vortex` and `thermodynamischer-phaenomenalismus` both concern C11 and now
rank in its top eight, and neither is in its record's `pages`. That is the label
lagging the graph. It is not retrieval getting worse.
Document 21 moved it back to 0.659, and again only C11 moved, from 0.4 to 0.6:
its reading went onto `hitze-polaritaetsregel`, which is in C11's `pages`.
Documents 23 and 24 left it at 0.659: their 29 readings each moved no case.
Document 27 moved it to 0.643: C11 from 0.6 to 0.4 and Q3 from 0.375 to 0.25, and in both the
pages crowding the gold out of the top eight are the central ones it gave a reading — `aegis`,
`juna`, `kael`, `coheron`, `vortex`, `alters`. The hubs grew faster than the pages around them.
Document 28 moved it to 0.637, only C4, from 0.556 to 0.444: `cerberus` left its top eight and `alters`
entered it, linked from the new readings on `cerberus`, `guardians` and `kern-welten`. Document 29 moved nothing, and neither did document 30. Document 31 moved it to 0.644, only Q5, from 0.286 to 0.429. Document 32 moved it to 0.654, only C11, 0.4 to 0.6; documents 33–39, measured together, moved it back to 0.644, again only C11 — the hubs again. Documents 40–43, measured together, moved it to 0.660: C11 from 0.4 to 0.6 and C4 from 0.444 to 0.556. Documents 44–46 moved nothing, and neither did document 47, nor documents 48–50. Document 51 moved it to 0.654, only C4, from 0.556 to 0.444. The four question pages of 2026-09-29, Q6–Q9, added four cases and moved it to 0.694 over 24, and seeds alone from 0.466 to 0.531; the twenty earlier cases scored exactly as before. The new cases score high because each question is worded in the terms of the pages that raise it — Q7 and Q9 1.0, Q6 0.833, Q8 0.75 with PageRank — which is the caveat above, the same hand writing question and label, four times more. Documents 52–54, measured together, moved it to 0.689, only Q5, from 0.429 to 0.286.
Documents 55–58, the four of the Haiku reader lab, measured together, moved nothing: seeds 0.531, PageRank 0.6885, no case.
`bench --record` appends both to `Plan/runs/baselines.jsonl`.
