# 004 — Format is measured, stance is read per passage, and neither is a document kind

**Date:** 2026-09-16 · **Decided by:** Claude, at the author's direction · **Status:** chosen, applied

## What was chosen

The three-value field `kind: brief | critique | result` is **removed**.

Three things it was conflating are separated:

| what | how it is established | where it lives |
|---|---|---|
| **format** | measured, mechanically, the same probes every time | `scripts/profile.py` |
| **stance** | read, **per passage**, and often labelled by the document itself | the census and the note |
| **provenance** — why the document exists, what it was asked | read, and frequently unknowable | one descriptive line, no enum |

**No closed list of document types.** A document is described by what it is, not
sorted into a bin.

## Why — the evidence, not the principle

**1. The format does not follow from the purpose.**

| | doc 1 | doc 2 | doc 3 |
|---|--:|--:|--:|
| headings | **0** | 34 | 24 |
| table rows | 0 | 19 | 9 |
| math symbol lines | 0 | 36 | 0 |
| zero-width spaces | 0 | 100 | 0 |

Three documents, one category, five days apart, and no two share a shape. A
commission could as easily have arrived as a table as as prose. Nothing about
*why* a document was written predicts *how* it is built, and every time the
census explained a structural fact by the document's purpose it was telling a
story about a coincidence.

**2. A document carries several stances at once, and marks them itself.**

Document 2 labels its own passages **38 times**, with six distinct labels:

| label | n |
|---|--:|
| Beschreibung | 8 |
| Kritik des Formalismus | 8 |
| Vergleich | 8 |
| Bewertung | 6 |
| Plausibilität | 4 |
| Probleme | 4 |

Calling that document `critique` throws away 38 explicit markers, including the
eight passages where it neutrally *describes* the thing it later rejects.

Document 3 marks **25 passages** with `[User Query]` — premises quoted back from
its commission, sitting inside what a single enum value would call a finding.

**So stance is a property of a passage, and the documents already say so.** The
enum could only ever record the loudest one.

**3. The one signal that looked like it separated kinds does not.** Question
marks: 22, 25, 23 across the three documents. A "brief is the one full of
questions" reading survives only as density (1.67% against 0.38% and 0.34%), on
one sample each, and density is a measurement, not a type.

## What was rejected, and why

**Keeping the enum and adding values.** The failure is not that three is too few.
It is that one value per document cannot hold what the documents mark per
passage, and that sorting into bins invites explaining format by bin.

**An enum per passage instead.** Document 2's six labels are *its* vocabulary.
Another document will have different ones or none — document 1 labels nothing at
all. A shared enum would either erase that or grow until it is a list of every
phrase any author ever used.

**Dropping the idea entirely.** The original finding stands and is not the part
being corrected: *reading a refutation as a definition inverts its meaning.* That
remains true. What changes is where the distinction is recorded — beside the
passage, not on the file.

## What this costs

The notes said `kind: brief` in one line and now say more. That is the point: the
one line was cheap because it was lossy.

`Wiki/README.md` explained how to read a source by its kind. It now explains it
by stance, which is where the documents put it.

## What this cost, and what should have happened

**The objection was „don't commit to fixed document types". This decision
deleted the field instead, in the same turn.** That is two steps past what was
asked, and it is the failure the `Changing your mind` rule in `CLAUDE.md` now
exists to prevent: *a construct is demoted, not deleted.*

What a demotion would have looked like:

```yaml
kind: brief          # provisional — a first-pass guess, not established
                     # may not: explain format, decide how a passage is read
                     # retire when: 20 documents show it predicts nothing
```

The `may not` line carries the whole objection. Everything this decision argues —
that format does not follow from purpose, that stance belongs to a passage —
stays true and stays enforced, and the guess survives to be useful elsewhere.

**Because it was useful elsewhere.** The sharpest cross-document finding in the
corpus so far is *a result closes a question an earlier brief asked* — three of
`entropie-aegis`'s 2025-04-17 questions answered on 2025-04-19. That finding
needs the commission/answer distinction to be **sayable at all**, and
`answers: unknown-brief` in one note still depends on it.

**The decision stands, at the author's direction.** It is recorded this way
rather than reversed, because the rule it produced is worth more than the field
it removed — and because reverting a reversal would be the same reflex again.

### Shelved, not discarded

> **A first-pass guess at what a document is for** — a commission, an answer, an
> analysis of something else. **Provisional, never load-bearing.** It may not
> explain format and may not decide how a passage is read. Its use is
> *sequencing and routing*: finding which document answers which, which
> commissions are still open, which documents are worth reading in what order.
> `PRINCIPLES.md` carries it in the catalogue.

## What would change our mind

**Twenty documents in which stance never varies within a document, and the
document-level label predicts its format.** Then the enum was right and three
documents were a bad sample. Nothing so far points that way — the variation
showed up in the second document read and the third marked it explicitly.

**Or: one question that can only be asked with a document-level guess.** There is
already a candidate above.
