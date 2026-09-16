# Learnings — gather a term (notes → a term page)

## Status

**Not run yet.** Pre-registration, as with `read-source.md`. Nothing below is
evidence.

This is the step that carries the wiki's whole value, and also the step most
likely to be got wrong quietly, so the predictions here are worth being explicit
about before any page exists to argue from.

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
