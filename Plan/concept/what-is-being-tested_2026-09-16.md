# What is actually being tested

*Written 2026-09-16, after four documents, because the prototype has grown steps
nobody designed and it is time to say what they are.*

Four documents have been processed by hand. That was never the point — **the
point is to find out what a workflow over 409 of them has to do**, and the only
honest way to find that out was to do a few without one.

This document states what the prototype is, what it has measured, and — the part
that matters most — **what it is not capturing and should be.**

---

## The steps that emerged

Nobody designed these. Each appeared because the work needed it.

| # | step | who | state |
|--:|---|---|---|
| 1 | **fetch** | script | done, 409 of 680 |
| 2 | **profile** | script | `scripts/profile.py`, identical probes per document |
| 3 | **brief** | *read* a document, before opening it | `Plan/briefings/extract.md`, v4 |
| 4 | **extract** → census | a person | 4 done |
| 5 | **read** → note | a person | 3 done |
| 6 | **compare** n censuses | semi-mechanical | 3 done, each superseded by the next |
| 7 | **corpus-check** | script | run ad hoc; **not yet a step** |
| 8 | **gather** → candidate page | a person | 14 pages |
| 9 | **review** → promote | a person | 0 |

**Steps 2, 3, 6 and 7 did not exist when the process was written down.** Step 3 —
a briefing read *before* the document — is the newest, and it is the one that
turns accumulated learning into something the next extraction actually uses
instead of something a later reader might find.

## The boundary that makes this work

**Cross-document knowledge is forbidden in extraction and required everywhere
else.** That sounds like a contradiction and is not:

| step | may use other documents? | why |
|---|---|---|
| **selection** — which document next | **yes** | picking `worldbuilding` because its heading median is 2 against 23 is a measurement, not a bias |
| **brief** | **only procedural** | „German inflection defeats exact matching" is about the language; „`Überwelt` appeared in document 1" decides in advance what matters |
| **extract** | **no** | the whole point |
| **compare** | **yes** | it is the step where documents meet |
| **corpus-check** | **all 409** | a comparison of n documents cannot answer a question about the corpus, and confusing the two produced one wrong conclusion already |

The briefing is safe to read first because it is written as **questions about the
document in front of you**, never as facts about others. That is checkable by
reading it: no slug, no count, no term from any document appears in it.

## What has been measured

### New special cases per document

The briefing grows by whatever a document finds that no question anticipated.
That count is the prototype's main signal.

| document | category | new findings |
|---|---|--:|
| 1 `entropie-aegis` | theorie-physik | **8** |
| 2 `aegis-emergenz-aus-der-leere` | theorie-physik | **6** |
| 3 `kohaerenzprotokoll-aegis-und-systementropie` | theorie-physik | **2** |
| 4 `guardians-und-kern-welten-konzept` | **worldbuilding** | **5** |

**Within one category it falls — 8, 6, 2. Changing category brought it back up.**

n=4, so this is a shape, not a law. But it makes a prediction worth writing down
before the next document:

> **Pre-registration.** Document 5, if also `worldbuilding`, yields **fewer than
> 5** new findings. A fifth document from a *new* category yields **4 or more**.
>
> If both hold, the cost of the whole corpus is roughly *(categories × a burst) +
> (documents × a tail)* rather than *(documents × a constant)* — and 12 categories
> is a very different number from 409 documents.
>
> If the count does not fall inside a category, the briefing is not carrying the
> method and the whole approach needs rethinking.

### What the comparisons measured

Each comparison superseded the one before — 001 → 002 → 003 — which is now a
pattern rather than an accident, and one rule got corrected by it: **a criterion
keyed to "shared by every document" weakens with each document added**, because
the intersection shrinks. Keyed to "three or more" it strengthens.

## The step-by-step reconciliation, which is the open design question

Three comparisons exist and **each superseded the one before**. That was recorded
as a pattern; it is better read as a **defect in the step**.

`001` compared two documents, `002` re-compared all three, `003` re-compared all
four. Every one re-did the work of the last. At 409 documents that is not slow,
it is impossible — and the supersession was the symptom saying so.

### Document against state, not document against all documents

The accumulated state already exists: **`Wiki/candidates/` is it.** Every term
page holds the readings landed so far. So the step is not *compare n censuses*,
it is:

```
census (frozen) × current pages → a diff
```

and the diff names exactly four things:

| | what it means |
|---|---|
| **new term** | a candidate no page covers → a page is created |
| **new reading** | a term that has a page, and this document says something about it → the page gains a reading |
| **new surface** | a term that has a page, under a different name → an alias, or a question about whether it is the same thing |
| **new conflict** | a reading that cannot stand beside one already on the page → a conflict record (decision 003) |

The record is **per document and append-only.** Nothing supersedes anything,
because nothing is re-derived. Document 5 is reconciled against the state
document 4 left, and the state is the pages themselves rather than a file that
has to be rewritten.

### Why this is safe, and why it was not safe before

Reconciling against accumulated state means the state shapes what you look for —
which is exactly the contamination the census exists to prevent.

**It is safe only because extraction already happened.** The census is frozen
before the state is ever consulted. The independence of step 4 is not a purity
rule for its own sake: **it is the precondition that makes an incremental
reconciliation trustworthy at all.** Without it, every document would be read
through the accumulated wiki and the wiki would stop being able to be surprised.

That is the argument the first three comparisons were circling and never stated.

### What it makes measurable

Four numbers per document, all derivable from the diff, none of them a judgement:

- **new terms** — should fall, and its curve says when the vocabulary is covered
- **new readings** — should *not* fall; it is the wiki filling in
- **new surfaces** — the aliasing rate, which decides whether alias handling is
  urgent or cosmetic
- **new conflicts** — the interesting one, and nobody knows its shape

> **Pre-registration.** New terms per document falls; new readings does not. If
> new terms does **not** fall across ten documents, the corpus has no shared
> vocabulary to speak of and a term wiki is the wrong structure for it.

## What is **not** being captured, and should be

This is the part the prototype is currently failing at.

### 1 · Effort per census — nothing, and it is the number that decides everything

The retired pipeline's cost is known exactly: **$2.79 and 18 minutes per
document.** The hand process has **no equivalent number at all.**

So the comparison that the whole plan turns on — *is a person cheaper than a
model here, and where* — cannot currently be made. Four documents have been done
and not one was timed.

**Start capturing:** wall-clock from opening the document to committing the
census, per document, in the census frontmatter. It costs one line and it is the
only way step 4 ever gets a budget.

### 2 · Which briefing questions fired

The briefing has ~25 questions. **Nothing records which ones produced a finding
in a given document**, so there is no way to tell a question that earns its place
from one that has never once fired.

**Start capturing:** in each census, the questions that produced a row. A question
that fires in zero of twenty documents gets deleted — which is the same discipline
`PRINCIPLES.md` applies to checks.

### 3 · The candidate count is a hand number nothing can verify

`candidates: 58` is typed. Nothing counts it, nothing checks it, and it is used in
prose. Either it becomes derivable from the census's own tables, or it stops being
quoted as if it were measured.

### 4 · Which findings a model would have missed

The eventual question is what to automate. Roughly half the special cases so far
are invisible to a regex, and **that proportion is exactly what decides whether
step 4 can be a model at all** — but it has never been measured against an actual
model. Three hand-written censuses are a gold set of three, and unused.

## What is deliberately not being tested yet

- **Whether the census format survives a fifth genre.** It has held over four.
- **Whether term pages scale.** 14 exist, one has four readings, none is promoted.
- **Whether conflict records work.** Decision 003 chose the design; nothing is built.
- **Anything about the novel.** It rests.

## The honest summary

What is being tested is a claim: **that doing a handful of documents carefully,
with every surprise written down, produces a better specification than designing
the workflow up front.**

Four documents in, that claim is holding — 21 special cases, of which roughly
half would have been guessed by nobody, and three of which silently break a check
the plan intended to build.

What it is **not** yet doing is producing the numbers that turn a specification
into a decision. That is the gap, and the four items above close it.
