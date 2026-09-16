# Learnings — read a source (source → its notes)

## Status

**Not run yet.** This file is a pre-registration: what we expect, what we will
watch for, and what would count as a surprise. Written before the first run on
purpose — comparing a prediction to an outcome sharpens a learning far more than
writing the outcome alone.

Nothing below is evidence. Everything below is a claim to be checked.

## What the step is

Read one source document and write `Sources/notes/<slug>.md`: the terms it
defines or uses, each with the exact lines that support it, quoted rather than
paraphrased.

A note harvests. It does not decide, merge or interpret.

## Predictions to test

1. **One document fits one context comfortably.** The largest seen so far is
   ~78 KB ≈ 20k tokens. Predicted: a single note costs one call and no
   chunking. *Falsified if* any document forces a split.

2. **Quoting is cheap and paraphrasing is the default failure.** P12 exists
   because the one real pilot run's most-broken rule was a paraphrase presented
   as a quotation. Predicted: the instruction "quote, with line numbers" is
   followed poorly by weaker models and well by stronger ones, and this is the
   sharpest discriminator between them.

3. **Line numbers will be the hard part, not the terms.** Identifying that
   "Coheron" is a term is easy; citing the lines that define it is where models
   fabricate. Predicted: citation accuracy, not term recall, is what the metric
   must measure.

4. **The flat-heading problem (fetch learning 7) bites here first.** With one
   real heading per document, a note cannot say "section 3 defines this". It can
   only give line ranges. Predicted: line ranges are sufficient and headings are
   not missed — *falsified if* notes become hard to read without section
   context.

5. **Terms will be wildly uneven across documents.** An `audit` document and a
   `theorie-physik` document share almost no vocabulary. Predicted: notes from
   different categories will look like different genres, and a single note
   template will strain.

## What we will watch for

- How many terms a typical document yields, and the spread.
- Whether "defines" and "merely uses" can be told apart reliably, or whether the
  distinction collapses in practice.
- Whether German terms with English surroundings (or the reverse) confuse the
  extraction. The corpus is German; some source documents are English.
- Whether the note format survives three documents from three categories without
  needing a field added. If it needs one on the first document, the format was
  guessed too early.
- Token cost and wall clock per document, for the 654-document projection.

## Open questions

- **Markdown or JSON?** Markdown while a person writes notes; JSON once a
  program does. The switch is cheap and the answer becomes obvious once this
  step is automated, so it stays open deliberately.
- **One note per source, or one note per source per category of term?** Starting
  with one, because P4 says no structure without instances.
- **Does a note record what the source does *not* say?** The kb-builder
  `limitations` field argued yes, and it feeds `MISSING` automatically. Untested
  whether it produces signal or noise.

## What stays judgement

- Whether a term is worth recording at all.
- Whether two spellings are the same term.
- Whether the document means a word as a technical term or in ordinary use —
  this is the distinction no rule will settle, and it is the whole reason a
  person reads the first ones.
