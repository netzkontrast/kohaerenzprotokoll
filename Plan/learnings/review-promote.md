# Learnings — review and promote (candidate → `Wiki/terms/`)

## Status

**Not run yet.** Pre-registration. No candidate pages exist.

This is the only step that is a person by definition, so its learnings are about
what makes a human review *fast* — a review that is slow does not happen, and a
review that does not happen is how 56 candidates sat unread.

## What the step is

A person reads a candidate term page and decides: promote, send back, or drop.
Promotion moves the file to `Wiki/terms/` and flips its status. Nothing else
happens automatically.

## Predictions to test

1. **Review speed decides whether the wiki lives.** The old system produced 56
   candidates and promoted 2. Predicted: the binding constraint is not
   generation but attention, so every design choice should be measured against
   "does this make a page faster to judge".

2. **A page that takes more than two minutes will not be reviewed.** Predicted:
   pages need to be short enough to hold in one screen. *If* the average
   candidate runs long, the term unit is too coarse.

3. **Machine checks must run before the person, not after.** Citations that do
   not resolve, quotes that are not in the cited lines, readings without a
   source — all decidable. Predicted: a human should never spend attention on
   something a check could have caught, and the review is where that principle
   pays or fails visibly.

4. **Sending back will be rarer than expected.** Predicted: most rejections are
   "this term is not worth a page" rather than "this page is wrong" — which
   means the interesting signal is about term *selection*, and feeds back into
   gather rather than into the page.

## What we will watch for

- Time per page, honestly measured on the first twenty.
- The ratio promote / send back / drop.
- Which of the four review questions actually catches things, and which is
  ceremony. Any that never catches anything gets removed, per P4.
- Whether the author trusts the conflict flags after twenty pages, or starts
  skimming past them — the latter means the false-positive filter is missing or
  wrong.
- What the author edits by hand on promotion. Repeated edits of the same kind
  are a specification for the gather step.

## Open questions

- **Does promotion need a command at all?** It is a file move and a status flip.
  A person with an editor can do it. A command earns existence only if the move
  is error-prone in practice.
- **What happens to a rejected candidate?** Deleted, or kept with a reason? A
  reason is the more valuable artefact, and it is the kind of thing nobody can
  reconstruct later — the argument for keeping it is the same one that justifies
  `Plan/decisions/`.
- **Does a promoted page ever go back?** New sources will arrive with readings
  that contradict a promoted page. Untested, and it is the case that will
  matter most in six months.

## What stays judgement

All of it. This step is the human act, and the four review questions are
prompts, not a checklist a program could run:

1. Does every reading actually say what the page claims?
2. Does every citation point at real lines? *(the one part a check does first)*
3. Is the disagreement real, or an artefact of wording?
4. Is anything important missing?

Question 4 is the one no tool will ever answer, and it is the reason a person
reads at all.
