# Learnings — read a source (source → its notes)

## Status

**3 documents read by hand, 2026-09-16** — `entropie-aegis` (1,331 w),
`aegis-emergenz-aus-der-leere` (6,568 w) and
`kohaerenzprotokoll-aegis-und-systementropie` (6,730 w), all `theorie-physik`,
all within two days of each other in the source chronology. Notes in
`Sources/notes/`.

The three read very differently — a commission, an adversarial analysis, an
answer — which was luck, not design, and is the reason the note format was
tested at all. They are **not** three types: see the correction under (a).

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

**a. What kind of statement a passage is turned out to be the missing field.**
`entropie-aegis` reads as a commission: it defines AEGIS and then asks 20
questions it does not answer. `aegis-emergenz-aus-der-leere` largely *rejects*
what it describes. A note that recorded only "what this source says about X"
would present a refutation as a definition.

> **Corrected 2026-09-16 — decision 004.** This was written up as a
> document-level field, `kind: brief | critique | result`, and that was wrong two
> ways.
>
> **Stance belongs to a passage.** Document 2 labels its own passages **38
> times** with six different labels, eight of them *describing* the postulate it
> goes on to reject; document 3 marks **25** passages `[User Query]` as premises
> quoted back from its commission. A single value per file records the loudest
> stance and discards the rest — including the case that matters most, where a
> document restates someone else's claim without asserting it.
>
> **And the enum invited explaining format by purpose.** It does not follow:
> three documents in one category, five days apart, have 0, 34 and 24 headings,
> and 0, 36 and 0 lines carrying mathematical symbols. Question marks are 22, 25
> and 23. Nothing about why a document exists predicts how it is built.
>
> What survives is the finding itself: **reading a verdict as a definition
> inverts its meaning.** Only the boundary moved — inside the document, not
> around it.

**b. A critique's verdicts are content.** „ECR scheint im Widerspruch zu
etablierten Prinzipien der Thermodynamik zu stehen" is a claim about ECR and
belongs on ECR's term page. The note format needs a section for judgements, not
only for definitions.

**c. Names are superseded across the corpus.** The 2025-04-17 document calls the
protagonist **Michael** and the external connection **Julia**; later sources use
Kael and Juna. This is not an error to fix — it is a fact about the source, and
without the date a reading under the old name looks like a different claim about
a different figure.

> **Corrected 2026-09-16, and the correction is the lesson.** This finding was
> extended, from three documents, into „the two names changed at different
> times". Counting all 346 landed documents refuted it: **both changed on one
> day.** 2025-04-17 is six documents with Michael/Julia and zero Kael/Juna;
> 2025-04-18 is seven with Kael/Juna and zero Michael/Julia; no document on
> either day mixes them. The mixing that suggested two dates is **incomplete
> enforcement afterwards** — 16 documents still say Michael, nine of them exactly
> once, the last in 2026-06. Three documents looked like a timeline and a count
> showed a cliff. This is P18 again, on the third occasion in this file.

**d. A real conflict appeared in the first two documents.** AEGIS is expanded
three ways — twice inside one document. `gather-term.md` predicted apparent
conflicts would vastly outnumber real ones; the first real one arrived
immediately, and it is not resolvable by rewording.

**e. `theorie-physik` is upstream of the story.** The critique never uses
Guardians, Überwelt, Risse or Kern-Welten. The theory tier argues about
mechanisms; the novel's own vocabulary lives elsewhere. Useful for sequencing:
theory documents define the roots, story documents use them.

## The third document, and what it corrected

`kohaerenzprotokoll-aegis-und-systementropie` is the answer to a commission, and
the first document read that states conclusions rather than asking for them.
Reading it changed four things.

**f. `[User Query]` is an inline provenance marker, and it is the highest-value
field found so far.** The document marks 26 passages with it, and every one is a
premise the brief supplied rather than a finding the research produced. **12 of
the 346 landed documents use the marker**, so it is a corpus convention.

> Corrected from „24 of the 409" once `dedupe.py` folded Drive's duplicate
> exports away. The probe never changed — the corpus did. See the correction in
> `Sources/notes/kohaerenzprotokoll-aegis-und-systementropie.md`.

This makes a distinction decidable that looked like judgement: for each reading,
*did the project assert this, or did the research conclude it?* A term page that
recorded a `[User Query]` passage as a finding would be citing the project as
evidence for its own premise. It is mechanical to extract and it changes what a
reading means — the best combination available.

**g. The corpus answers its own questions across documents.** Three of the
questions `entropie-aegis.md` posed on 2025-04-17 are answered here on
2025-04-19, and one — the alters' „Entropie-Signatur" — is not. So `MISSING` is
not a property of a term; it is a property of a term *at a date*, and it can be
closed by a later document. A note should record which earlier open question a
result closes, because nothing else in the corpus links them.

The brief this document answers, though, is **not in the three read**: it cites
thirteen questions and `entropie-aegis.md` asks a different set. A result whose
brief is missing cannot be checked for completeness, so `answers:` went into the
frontmatter with the value `unknown-brief`.

**h. Absence of a definition is itself a reading.** This document never expands
AEGIS — not once in 330 lines — after two documents expanded it three ways. That
is not missing data. A document that uses a contested acronym as a bare proper
name while taking a side in substance is making a choice, and the term page
should show it beside the three expansions rather than omit it.

**i. Finding (e) was too fast, and this document falsifies it.** "`theorie-physik`
is upstream of the story" was drawn from two documents. This one is
`theorie-physik`, is about Kael and Julia by name, and uses Überwelt and
Kern-Welten throughout. **Category does not predict whether a document touches
the novel; the document does.** Two samples were not enough to generalise from —
which is P18 landing on our own note-taking rather than on a model benchmark.

Finding (c) looked like it needed the same correction and got the wrong one:
this document says *Kael* and *Julia*, which was read as the two names changing
at different times. **They did not.** See the correction under (c) — the mixing
is later slippage, not a second rename, and only counting the corpus could tell
the two apart.

**What did not change:** the note format needed no new field for the third
document. The stance distinction absorbed it — though the *shape* that
distinction should take took one more correction to get right (decision 004).

## What we will watch for

- How many terms a typical document yields, and the spread.
- Whether "defines" and "merely uses" can be told apart reliably, or whether the
  distinction collapses in practice.
- Whether German terms with English surroundings (or the reverse) confuse the
  extraction. The corpus is German; some source documents are English.
- ~~Whether the note format survives three documents from three categories
  without needing a field added.~~ **Survived three documents from three
  *genres*, same category.** Still untested across categories — an `audit` and a
  `charaktere` document are the next real test.
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
