# 009 — Which candidate lists are gold is decided by rule, in `scripts/gold.py`

**Date:** 2026-09-24 · **Decided by:** this session, on the author's instruction · **Status:** chosen, enforced by `scripts/gold.py`

## What was chosen

The author, 2026-09-24, verbatim: "You Can yourself Decide Which one Are Gold —
Build a Tool for that so that you Decide in a way that is repeatable".

A candidate list, `Plan/runs/<slug>/03-candidates.md`, is gold when it passes
five criteria, each checked by code:

1. **a list** — it has at least one `- term` line;
2. **not reconstructed** — it does not carry the declaration every
   reconstruction carries;
3. **counted** — `counts.json` exists, and `capture.py --count` refuses to run
   before a list does, so the list existed before its counts;
4. **frozen since the count** — its terms are exactly the terms the count
   recorded, so nothing was added or dropped with the counts in view;
5. **of the document** — at least 90% of its terms occur in the document, the
   bar `rlm_ingest.py` already sets for a model's list.

`scripts/gold.py` is the one encoding. `state.py`, `trainset.py`,
`entities.py score` and `rlm_ingest.py --score` ask it, and the last two refuse
to score against a list it does not rule gold.

On the day it was decided, 9 of the 13 lists were gold: documents 5 to 13. The
four reconstructions, documents 1 to 4, were not, and one of them had also
dropped three terms after its count.

That answers the question the tool review left open the same day: „How many of
the other nine are usable gold was not measured here"
(`Plan/concept/tool-review_2026-09-24.md`). All nine are.

## Who wrote a list does not decide it

Two of the gold lists say they were written by "a reader"; seven name the
session that read the document. Every criterion is about the artifact — when it
was written relative to its count, and whether it describes the document — so
both kinds are gold. Each verdict keeps the `written_by:` line verbatim, so a
score can say which kind of reading its gold is.

This departs from the tool review's phrase „gold is a person's list written
while reading". The author gave the call to this session. A session that reads a
document and writes its list before any count produces the same artifact a
person does.

## What was rejected

- **Only a person's list is gold.** That would leave two lists, and the author
  gave the decision to this session. What it protected stays visible: the
  reader is in every verdict.
- **Tests of wording**: the word "reader" in `written_by:`, the word
  "reconstruct" in the first 300 characters. They tested how a header reads,
  not what a list is — and they disagreed: `state.py` counted 2 gold lists
  while `trainset.py` counted 9 usable.
- **Reach by first occurrence.** The gazetteer, document 6, is a full reading
  that introduces its names early; its terms' first occurrences reach only 5 of
  the document's 10 tenths.
- **Reading order.** Document 5's list follows the document's order no better
  than two reconstructions do: rank correlation 0.57, against 0.58 and 0.60.

## What would change our mind

- **A second, independent reading** of a document whose gold the session wrote,
  disagreeing with it far more than two readings of one document disagreed
  before (F1 0.66, P27). Then who read would decide after all, and the reader
  would become a criterion.
- **A list shown to have been written after its count** although its terms
  match `counts.json`. Then matching terms is not evidence enough, and the count
  must record a fingerprint of the list it counted.
