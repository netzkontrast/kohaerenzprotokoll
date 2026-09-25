# Learnings — gather a term (notes → a term page)

## Status

**One page written by hand, 2026-09-16** — `Wiki/candidates/aegis.md`, gathered
from the three notes in `Sources/notes/`. Four readings, three sources.

The predictions below were written before it existed. Results are under them.
One page is not a sample: predictions 1, 3 and 5 are untouched because a single
term cannot speak to a distribution, to aliasing, or to tier precedence. They
stay open rather than being answered thinly.

This is the step that carries the wiki's whole value, and also the step most
likely to be got wrong quietly, so the predictions here are worth being explicit
about before more pages exist to argue from.

## What the step is

Collect every note that mentions one term and write
`Wiki/candidates/<term>.md`: one reading per source, attributed and cited, with
disagreements named and left unresolved.

## Predictions to test

1. **Most terms will have one reading, and the interesting ones will have
   five.** Predicted: a long tail of terms mentioned once, and a small core
   (AEGIS, Kernwelt, Coheron, DKT, the alters) carrying most of the corpus's
   disagreement. *If* the distribution is flat instead, the term page is the
   wrong unit and domain bundling deserves reconsideration.

2. **Apparent conflicts will vastly outnumber real ones.** This is why the five
   "by design, not a contradiction" cases lead the catalogue in
   `PRINCIPLES.md`. Predicted: without that filter, the first hundred pages
   produce enough false conflicts to make the author stop reading them — which
   is the failure mode, not the false positives themselves.

3. **The same term will be spelled several ways.** German compounds, hyphenation
   drift, and English/German pairs. Predicted: alias handling is needed on the
   first real batch, not later.

4. **Chronology will matter more than expected.** The manifest carries
   `index_date` spanning 2025-05 to 2026-06. Predicted: many "conflicts" are one
   idea evolving, and a reading without its date is misleading. Date belongs on
   every reading, prominently.

5. **Tier will predict authority, and that will be a trap.** `T2-theory` looks
   more authoritative than `T3-work`, but the work documents are later.
   Predicted: no automatic precedence by tier survives contact with the corpus,
   and precedence stays a human call — P13 already forbids merging, which keeps
   this from mattering as much as it would otherwise.

## Results from the first page

**Prediction 2 — apparent conflicts outnumber real ones — is not yet supported,
and the first evidence runs the other way.** Four readings produced *two* real
conflicts and no false ones: three incompatible acronym expansions, and two
incompatible senses of "emergence". Neither dissolves on rewording, and one is
flagged as a defect by the document that contains it. n=1 term, and AEGIS was
chosen *because* it looked contested, so this is selection, not refutation —
but the filter the prediction called for was not needed once.

**Prediction 4 — chronology matters more than expected — confirmed, and
sharpened.** All three sources fall within two days. Date did not separate the
readings; **kind and provenance did.** A brief's premise, a critique's verdict
and a result's finding can be same-day and still not be the same kind of claim.
So the field that carries the weight on a page is `kind`, with date second — the
reverse of what the prediction assumed.

### What the page needed that no prediction named

**a. A reading can be the *absence* of a definition.** The third source never
expands AEGIS in 330 lines, while taking a side in substance. Recorded as
reading 4. A gather step that collected only text matching a definition pattern
would have found three readings and missed the one that shows the corpus never
resolved the conflict.

**b. `premise` / `finding` has to be per reading, not per page.** Within one
source, `[User Query]` passages are premises quoted back from the brief and the
rest are the research's own. Reading 4's striking claims are mostly premises; its
blind-spot argument is the finding. Marking the page's kind is not enough.

**c. A conflict can sit underneath another and be missed.** The acronym conflict
is loud. The emergence conflict — emergence *from nothing* versus emergence
*within the simulation* — uses one word correctly in both places and decides
whether AEGIS can be wrong about its own world. **Nothing surfaces it except
reading both sources for what they entail**, which is the judgement this step
rests on and the reason the first pages are written by hand.

**d. `MISSING` arrived with more force than expected.** Three items on one page:
four sub-functions used as known and defined nowhere, an escalation protocol
named as undefined by the document depending on it, and a brief that is not in
the corpus. This suggests `MISSING` is not a reporting afterthought but a
primary output of the gather step.

**e. The page is long — 144 lines for one term — and that is not obviously
wrong.** Prediction: it stops being readable somewhere past six readings. The
structure that held was *one section per reading*, not one section per aspect.

## What the retired system already measured

Not our evidence — two live runs of the pipeline that was thrown out, read back
from `Legacy/Plan/wiki/` on 2026-09-16. Recorded here because it is the only
measurement of this step at scale that exists, and re-deriving it costs money.

| | pilot (3 docs) | probe (4 docs, cheap merge model) |
|---|---|---|
| claims | 141 | 150 |
| concepts | 46 | 41 |
| unassigned claims | 0 | 0 |
| cost | **$8.38** — $2.79/doc, 18 min/doc | — |
| conflicts found | 2 (one concept) | 8 (seven concepts) |

**Prediction 1 gets a first answer from someone else's data:** 141 claims
clustered into 46 concepts, and the concepts read like the project's own
vocabulary. Not the flat distribution that would have made the term the wrong
unit.

**Prediction 2 gets its first real test, and loses again.** Eight disagreements
across seven concepts in the probe, every one of them genuine enough to survive
an audit. Combined with our two-from-one-page, the "apparent conflicts vastly
outnumber real ones" prediction now has no supporting evidence at all and two
runs against it. It stays recorded rather than deleted, because the corpus is
still mostly unread.

**Two of the seven were the same argument from different concepts.** This is
the evidence behind decision 003.

**The dominant defect is quoting.** 16–19 of 141 claims put a term in quotation
marks that does not appear in the lines cited — typically a German paraphrase of
an English source with a German term in quotes. P12 already forbids it; this is
the rate at which it happens anyway, and it is the thing the gather step must be
scored on before anything else.

## What we will watch for

- The real distribution of readings per term.
- How often two readings are genuinely incompatible versus differently worded.
- Whether "where they disagree" can be written mechanically from two readings,
  or whether it always needs a person.
- Whether a page stays readable past four or five readings, or needs structure.
- Whether the `foundationality` idea (foundational / important / derivative /
  unclear) adds signal or just a field nobody fills.

## Open questions

- **What creates a page — a term appearing once, or twice?** Once risks a wiki
  of singletons; twice risks losing a term defined in exactly one place, which
  may be the most valuable kind. Leaning towards once, with `MISSING` reporting
  singletons so the author can see them.
- **Where do aliases live?** On the page, or in a shared list a tool reads? The
  second is a schema value under P1 and is probably right, but no instances
  exist yet.
- **Does a candidate page get rewritten on re-run, or appended to?** Rewriting
  loses author edits; appending accumulates. The kb-builder "update mode that
  preserves prior work" idea applies directly here.

## What stays judgement

- **Whether a disagreement matters.** The page names it; the author weighs it.
- **Which reading is right.** Never the page's call, by P13.
- **Whether two readings are the same idea in different words.** This is the
  judgement the whole step rests on, and it is not automatable — a tool can
  surface candidates for it and must never settle them.
- **Whether a term deserves to exist as a concept at all**, or is just a phrase
  the author used twice.

## Adding a reading is a moment to compare — document 16, 2026-09-25

`externe-ebene` held five readings from five documents, each attributed, two
saying Köln 2026 lies „jenseits der Simulation" and three „Kein „außerhalb der
Simulation"". No conflict record held it; the page's own frontmatter said
`conflict: none yet`. It surfaced only because document 16 added a sixth reading
and its words were read against the page's earlier ones — now C13.

**Reconciliation walks from a census to pages; nothing walks a page against
itself.** A disagreement between two readings that arrived months apart on one
page is invisible to every check here, and the step that adds a reading is the
only one that reads the others. What would make it visible without mechanising
the judgement (P1, `CLAUDE.md` *Conflict detection is never mechanised*): list,
per page, the readings no conflict record cites, so a person reads them against
each other. Not built.

