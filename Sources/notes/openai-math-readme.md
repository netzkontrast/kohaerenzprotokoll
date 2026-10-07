---
source: Sources/drive/openai-math-readme.md
read: "2026-10-07, the whole document (L1 to L59) through read.py with line numbers; by a document-reader subagent (Sonnet)"
stance_markers: ["Reasoning summaries", "fixed procedure", "unformalized results", "human edited for readability"]
stance_marker_count: 4
reads_as: "a short repository readme, in the voice of an unnamed „we“, that says what the collection holds, how it is organised, how far its results are verified and how they were produced"
---

# Note — OpenAI math — Readme

What this document says about the terms that matter in it. Every quotation carries its file line on the same line of this note; a number about the whole document is a count mark that `quotes.py` checks. Where the note says **observed**, no quotation is possible (a structure, a gap) and the claim rests on the lines or counts it names. The document speaks for its authors in the first person plural and states no standing for itself beyond describing its results as being at different stages of verification.

## 1 · What kind of text this is, and how it marks itself

- The document opens by saying what the repository holds: „This repository contains mathematical manuscripts and supporting proof artifacts produced by an internal OpenAI model.“ ^[L13]
- **Observed:** it carries no labels on its passages; the only markers are the section headings of L11, L22, L31, L48 and L54, and the four markers listed in the frontmatter (`Reasoning summaries` ^[openai-math-readme.md:#1], `fixed procedure` ^[openai-math-readme.md:#1], `unformalized results` ^[openai-math-readme.md:#1], `human edited for readability` ^[openai-math-readme.md:#1]) are a heading and three phrases of its own prose, not tags.
- **Observed:** the speaker is the first person plural and is never named: `We` ^[openai-math-readme.md:#6] opens six sentences and `we` ^[openai-math-readme.md:#2] stands twice more inside sentences. The only institution named is `OpenAI` ^[openai-math-readme.md:#2], in the phrase for the model.

## 2 · The model, and what producing a result cost

- The document names the producer of the results only as an internal model; for the greater part of them it says „The vast majority of results were obtained with the same procedure using an unreleased internal OpenAI model.“ ^[L50]
- It states the cost of one result: „On average, each result used three hours of ChatGPT Pro thinking compute with that model.“ ^[L50] The count marks for the words are `ChatGPT Pro` ^[openai-math-readme.md:#1] and `thinking compute` ^[openai-math-readme.md:#1].
- It states how many problems the model was posed: „Over the course of the evaluation, the model was posed approximately 4,000 problems.“ ^[L50]
- It says how the output was reduced to the catalogue: „Aggregating the output into result families and manuscripts and requiring an appropriate level of significance led to the catalog outlined above.“ ^[L50]
- **Observed:** no model name, version or release date is given. `GPT` ^[openai-math-readme.md:#0] stands zero times as a whole word, and `ChatGPT` ^[openai-math-readme.md:#1] stands once, in the phrase about compute.

## 3 · Why the work was done, and on what

- The document says it evaluates its models on a class of problems it calls open research problems: „As part of model development, we evaluate our models on open research problems.“ ^[L15]
- It gives the reason for having widened the evaluations: „We expanded these evaluations after performance on our existing mathematical evaluations saturated.“ ^[L15]
- It says that results can rest on earlier results: „Some outputs build upon earlier results produced by the models.“ ^[L15]

## 4 · Verification, and the Lean formalizations

- The collection is described as uneven: „This collection includes results at different stages of verification.“ ^[L17]
- Formal proofs exist for some results only: „Not all have accompanying Lean formalizations.“ ^[L17] and, on the line that lists the Lean parts, „Many, but not all, of the manuscripts have been formalized.“ ^[L29]
- The document promises further formalizations: „We will continue to update this repository with Lean formalizations as we obtain them.“ ^[L17]
- It warns about results without one: „Some of the unformalized results could have issues.“ ^[L19] and promises „We will endeavor to fix any such issues quickly.“ ^[L19]
- It names the checking apparatus as parts of the repository: the `Lean library` ^[openai-math-readme.md:#1], the `formalization catalogue` ^[openai-math-readme.md:#1] and the `Comparator instructions` ^[openai-math-readme.md:#1]. The line says the first two „describe the available formal proofs, their associated papers, and verification configurations“ ^[L29] and that the third gives „additional checking instructions“ ^[L29].
- **Observed:** the document names no result as formalized or as unformalized. The table of ten results (L37 to L46) carries no marker for Lean, and the word `Lean` ^[openai-math-readme.md:#3] stands only on L17 and L29.

## 5 · How the collection is organised: manuscripts, families, the catalogue

- The size of the collection and its unit of grouping are given in one sentence: „The current catalogue contains 722 manuscripts organized into 372 families.“ ^[L24] The count marks are `manuscripts` ^[openai-math-readme.md:#4] and `families` ^[openai-math-readme.md:#3] over the whole document; the numbers themselves are `722` ^[openai-math-readme.md:#1] and `372` ^[openai-math-readme.md:#1].
- A family is defined: „A family groups related papers, which may include a principal result, companion arguments, consequences, or alternative proofs.“ ^[L24]
- Families are classified: „Each family is classified by mathematical discipline.“ ^[L24]
- The document points the reader to the `overview` ^[openai-math-readme.md:#2], to the `manuscript map` ^[openai-math-readme.md:#1] and to the directory `preprints` ^[openai-math-readme.md:#2]; the line on the third says it „contains PDFs, source files, and manuscript-specific citation and build instructions“ ^[L28].
- It says how a manuscript is cited: „To cite the individual manuscript, use the BibTeX block in its directory.“ ^[L58]

## 6 · The reasoning summaries and the ten named results

- The document releases summaries of the model's reasoning for some results only: „We are also releasing abridged summaries of the model's reasoning, covering the following results:“ ^[L33]
- **Observed:** ten rows follow, each a family number and a subject written as a link title (L37 to L46, ten rows by `grep`, see `05-verify.txt`). The subjects are named by title only. The document writes no sentence about any of them: it says nothing of what was found, whether a problem was solved or in which direction.
- The titles, each copied from its line, name these problems and objects: `Ordinary two-point correlations of multiplicative functions` ^[openai-math-readme.md:#1], `The irrationality exponent of π` ^[openai-math-readme.md:#1], `Symmetric and general Mahler conjectures` ^[openai-math-readme.md:#1], `Ordinary NP-hardness at the basic semidefinite threshold` ^[openai-math-readme.md:#1], `Quasipolynomial bounds for arithmetic progressions` ^[openai-math-readme.md:#1], `Kaplansky's direct-finiteness conjecture in characteristic two` ^[openai-math-readme.md:#1], `The Mézard–Parisi formula for diluted spin glasses` ^[openai-math-readme.md:#1], `Spontaneous magnetization in the quantum Heisenberg ferromagnet` ^[openai-math-readme.md:#1], `Isomorphism of free group factors` ^[openai-math-readme.md:#1] and `The three-dimensional relativistic Vlasov–Maxwell system` ^[openai-math-readme.md:#1].
- The first row of the table reads „Ordinary two-point correlations of multiplicative functions“ ^[L37] and the last reads „The three-dimensional relativistic Vlasov–Maxwell system“ ^[L46].

## 7 · The exceptions to the procedure

- The document says the procedure was not the same for all results: „Exceptions to this fixed procedure include work on a zero-free region for the Riemann zeta function and proof of the Hodge Conjecture for CM abelian varieties.“ ^[L52] The count marks are `zero-free region` ^[openai-math-readme.md:#2], `Riemann zeta function` ^[openai-math-readme.md:#2], `Hodge Conjecture` ^[openai-math-readme.md:#1] and `CM abelian varieties` ^[openai-math-readme.md:#1].
- One writeup is said to have had a human hand: the line says the writeup for the zero-free region of the Riemann zeta function „was human edited for readability“ ^[L52].
- **Observed:** the document does not say what the procedure of the exceptions was. `fixed procedure` ^[openai-math-readme.md:#1] and `same procedure` ^[openai-math-readme.md:#1] each stand once, and no sentence describes the other one.

## 8 · Versions, and where else the materials may go

- The document promises to keep earlier versions: „We will preserve the public release history of this collection.“ ^[L56] and says „Corrections and revisions will be recorded as new versions, with previously released versions remaining accessible.“ ^[L56]
- It says it is looking at a further home: „We are also exploring community-hosted repositories for these materials.“ ^[L20]

## 9 · Said two ways, or left open — recorded, not resolved

- The document spells one word two ways: `catalogue` ^[openai-math-readme.md:#2] on L24 and L29, and `catalog` ^[openai-math-readme.md:#1] on L50, where the line speaks of „the catalog outlined above“ ^[L50].
- The document says its results are „at different stages of verification“ ^[L17] and, separately, that the formalized part is „Many, but not all“ ^[L29]; it gives no number for either, so the share of results with a Lean formalization is open in this document.
- The hedge on quality is the document's own: „Some of the unformalized results could have issues.“ ^[L19] It is recorded as the document's caution and decides nothing here.

## 10 · Absent, counted

**Observed:** the document does not call any of its results proved, refuted or reviewed. `proved` ^[openai-math-readme.md:#0], `refuted` ^[openai-math-readme.md:#0], `disproved` ^[openai-math-readme.md:#0], `peer` ^[openai-math-readme.md:#0], `reviewed` ^[openai-math-readme.md:#0] and `checked` ^[openai-math-readme.md:#0] each stand zero times. `proof` ^[openai-math-readme.md:#2] stands twice, on L13 (`supporting proof artifacts`) and on L52 (the Hodge sentence). No author, editor or contributor is named: the proper names that stand are the institution, a product and the names inside the titles of mathematical subjects.
