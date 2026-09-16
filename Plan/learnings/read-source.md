# Learnings — read a source (source → its notes)

## Status

**2 documents read by hand, 2026-09-16** — `entropie-aegis` (1,331 w) and
`aegis-emergenz-aus-der-leere` (6,568 w), both `theorie-physik`, two days apart
in the source chronology. Notes in `Sources/notes/`.

The predictions below were written before either was opened. Results are
recorded under each, and the section after them holds what no prediction
anticipated — which turned out to be the more valuable half.

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

## Results against those predictions

1. **Context — confirmed.** 6,568 words read in two passes with room to spare.
   No chunking needed, no document has forced a split.

2. **Quoting — confirmed, and cheap.** Quoting with line numbers took no more
   effort than paraphrasing and made every claim checkable. Untested against a
   *weak* model, which is where the prediction actually bites.

3. **Line numbers — falsified for a human reader.** The prediction was that
   citing lines would be the hard part. Reading a file whose lines are numbered
   makes it trivial. The prediction may still hold for a model at scale, so it
   stays open rather than closed — but it is not the difficulty it looked like.

4. **Flat headings — falsified in the good direction.** Both documents came
   through the markitdown route and carry real headings, so notes cite section
   context freely. The problem is confined to Google Docs, as `fetch.md` §7b
   records.

5. **Uneven across categories — confirmed, and stronger than expected.** The two
   documents are different *genres*, not just different topics. And yet the same
   note fields fitted both, which is the useful half of the finding: the shape
   held, the content varied.

## What no prediction anticipated

**a. Document kind is the single most important field, and it was not in the
format.** The corpus contains at least three kinds, and reading one as another
inverts its meaning:

| kind | what it is | how it must be read |
|---|---|---|
| `brief` | a research commission — states premises, asks questions | its terms are *premises*, not findings |
| `critique` | an adversarial analysis of a proposal | its **verdicts** are claims about terms |
| `result` | a research answer | not yet encountered in these two |

`entropie-aegis` is a brief: it defines AEGIS and then asks 20 questions it does
not answer. `aegis-emergenz-aus-der-leere` is a critique that largely *rejects*
what it describes. A note that recorded only "what this source says about X"
would present a refutation as a definition.

**So `kind` goes in the frontmatter, and the note opens by saying what reading
the document requires.**

**b. A critique's verdicts are content.** „ECR scheint im Widerspruch zu
etablierten Prinzipien der Thermodynamik zu stehen" is a claim about ECR and
belongs on ECR's term page. The note format needs a section for judgements, not
only for definitions.

**c. Names are superseded across the corpus.** The 2025-04-17 document calls the
protagonist **Michael** and the external connection **Julia**; current canon uses
Kael and Juna. This is not an error to fix — it is a fact about the source, and
without the date a reading under the old name looks like a different claim about
a different figure.

**d. A real conflict appeared in the first two documents.** AEGIS is expanded
three ways — twice inside one document. `gather-term.md` predicted apparent
conflicts would vastly outnumber real ones; the first real one arrived
immediately, and it is not resolvable by rewording.

**e. `theorie-physik` is upstream of the story.** The critique never uses
Guardians, Überwelt, Risse or Kern-Welten. The theory tier argues about
mechanisms; the novel's own vocabulary lives elsewhere. Useful for sequencing:
theory documents define the roots, story documents use them.

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
