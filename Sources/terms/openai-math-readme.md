---
source: Sources/drive/openai-math-readme.md
drive_id: "github:openai/math@adc7f12/README.md"
title: "OpenAI math — Readme"
category: theorie-mathematik
index_date: "2026-10-06"
extracted: "2026-10-07"
candidates: 51    # the terms capture.py counted
---

# Term census — OpenAI math — Readme

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py openai-math-readme`

```
  lines                59  (frontmatter ends at 9)
  body words           498
  headings             5   bold-only lines 0
  table rows           12   code fences 0
  question marks       0
  backslash escapes    0
  typographic marks    2   ascii quotes 0
  invisible characters none
  math symbol lines    0
  glued ref numbers    0
  repeated labels      none
  longest line         430 chars
```

## Stance, read per passage

The document is one voice, an unnamed „we“ that speaks for the repository's authors, and it names no person. It does not label its passages with tags; its own section headings are the only labels (L11, L22, L31, L48, L54). Each passage below is read for what it does.

**L13, the opening statement (report).** It says what the repository holds: „This repository contains mathematical manuscripts and supporting proof artifacts produced by an internal OpenAI model.“ ^[L13]

**L15, how the work came about (report).** „As part of model development, we evaluate our models on open research problems.“ ^[L15] The same line reports a change of practice and gives its reason in the document's words: „We expanded these evaluations after performance on our existing mathematical evaluations saturated.“ ^[L15]

**L17 to L20, a caveat and promises (plan).** The caveat is „This collection includes results at different stages of verification.“ ^[L17] The promises are in the future tense: „We will continue to update this repository with Lean formalizations as we obtain them.“ ^[L17] and „We will endeavor to fix any such issues quickly.“ ^[L19] A third is a possibility, not a commitment: „We are also exploring community-hosted repositories for these materials.“ ^[L20] The warning about quality is „Some of the unformalized results could have issues.“ ^[L19]

**L22 to L29, navigation (instruction).** Imperative bullets say where to start and what each part of the repository holds. The description of the unit of organisation is in the document's voice: „A family groups related papers, which may include a principal result, companion arguments, consequences, or alternative proofs.“ ^[L24] The bullets are markdown links, so a term often stands twice on its line, as link text and as file name.

**L31 to L46, a release with a table (report).** „We are also releasing abridged summaries of the model's reasoning, covering the following results:“ ^[L33] The table that follows has ten rows, each a family number and a subject written as a link title (L37 to L46). The table is a list of titles; it contains no sentence about any result.

**L48 to L52, how the results were produced (report, with exceptions).** The procedure is stated as a single one: „The vast majority of results were obtained with the same procedure using an unreleased internal OpenAI model.“ ^[L50] The paragraph on exceptions opens „Exceptions to this fixed procedure include work on a zero-free region for the Riemann zeta function and proof of the Hodge Conjecture for CM abelian varieties.“ ^[L52]

**L54 to L58, versions and citation (plan).** „We will preserve the public release history of this collection.“ ^[L56] and „To cite the individual manuscript, use the BibTeX block in its directory.“ ^[L58]

## Candidates and counts

51 candidates, written while reading and frozen by the count (`Plan/runs/openai-math-readme/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `openai-math-readme.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `OpenAI` ^[openai-math-readme.md:#2] | 2 | 2 | 13, 50 |  |
| `internal OpenAI model` ^[openai-math-readme.md:#2] | 2 | 2 | 13, 50 |  |
| `unreleased internal OpenAI model` ^[openai-math-readme.md:#1] | 1 | 1 | 50 |  |
| `ChatGPT Pro` ^[openai-math-readme.md:#1] | 1 | 1 | 50 |  |
| `thinking compute` ^[openai-math-readme.md:#1] | 1 | 1 | 50 |  |
| `open research problems` ^[openai-math-readme.md:#1] | 1 | 1 | 15 |  |
| `saturated` ^[openai-math-readme.md:#1] | 1 | 1 | 15 |  |
| `manuscripts` ^[openai-math-readme.md:#4] | 4 | 4 | 13, 24, 29, 50 |  |
| `supporting proof artifacts` ^[openai-math-readme.md:#1] | 1 | 1 | 13 |  |
| `catalogue` ^[openai-math-readme.md:#2] | 2 | 2 | 24, 29 |  |
| `families` ^[openai-math-readme.md:#3] | 3 | 3 | 24, 26, 50 |  |
| `family` ^[openai-math-readme.md:#2] | 2 | 2 | 24 |  |
| `mathematical discipline` ^[openai-math-readme.md:#1] | 1 | 1 | 24 |  |
| `principal result` ^[openai-math-readme.md:#1] | 1 | 1 | 24 |  |
| `companion arguments` ^[openai-math-readme.md:#1] | 1 | 1 | 24 |  |
| `alternative proofs` ^[openai-math-readme.md:#1] | 1 | 1 | 24 |  |
| `manuscript map` ^[openai-math-readme.md:#1] | 1 | 1 | 27 |  |
| `overview` ^[openai-math-readme.md:#2] | 2 | 2 | 26 |  |
| `preprints` ^[openai-math-readme.md:#2] | 2 | 2 | 28 |  |
| `Lean` ^[openai-math-readme.md:#3] | 3 | 3 | 17, 29 |  |
| `Lean formalizations` ^[openai-math-readme.md:#2] | 2 | 2 | 17 |  |
| `Lean library` ^[openai-math-readme.md:#1] | 1 | 1 | 29 |  |
| `formalization catalogue` ^[openai-math-readme.md:#1] | 1 | 1 | 29 |  |
| `Comparator instructions` ^[openai-math-readme.md:#1] | 1 | 1 | 29 |  |
| `unformalized results` ^[openai-math-readme.md:#1] | 1 | 1 | 19 |  |
| `Reasoning summaries` ^[openai-math-readme.md:#1] | 1 | 1 | 31 |  |
| `abridged summaries` ^[openai-math-readme.md:#1] | 1 | 1 | 33 |  |
| `same procedure` ^[openai-math-readme.md:#1] | 1 | 1 | 50 |  |
| `fixed procedure` ^[openai-math-readme.md:#1] | 1 | 1 | 52 |  |
| `human edited for readability` ^[openai-math-readme.md:#1] | 1 | 1 | 52 |  |
| `BibTeX` ^[openai-math-readme.md:#1] | 1 | 1 | 58 |  |
| `zero-free region` ^[openai-math-readme.md:#2] | 2 | 2 | 52 |  |
| `Riemann zeta function` ^[openai-math-readme.md:#2] | 2 | 2 | 52 |  |
| `Hodge Conjecture` ^[openai-math-readme.md:#1] | 1 | 1 | 52 |  |
| `CM abelian varieties` ^[openai-math-readme.md:#1] | 1 | 1 | 52 |  |
| `Ordinary two-point correlations of multiplicative functions` ^[openai-math-readme.md:#1] | 1 | 1 | 37 |  |
| `The irrationality exponent of π` ^[openai-math-readme.md:#1] | 1 | 1 | 38 |  |
| `Symmetric and general Mahler conjectures` ^[openai-math-readme.md:#1] | 1 | 1 | 39 |  |
| `Ordinary NP-hardness at the basic semidefinite threshold` ^[openai-math-readme.md:#1] | 1 | 1 | 40 |  |
| `Quasipolynomial bounds for arithmetic progressions` ^[openai-math-readme.md:#1] | 1 | 1 | 41 |  |
| `Kaplansky's direct-finiteness conjecture in characteristic two` ^[openai-math-readme.md:#1] | 1 | 1 | 42 |  |
| `The Mézard–Parisi formula for diluted spin glasses` ^[openai-math-readme.md:#1] | 1 | 1 | 43 |  |
| `Spontaneous magnetization in the quantum Heisenberg ferromagnet` ^[openai-math-readme.md:#1] | 1 | 1 | 44 |  |
| `Isomorphism of free group factors` ^[openai-math-readme.md:#1] | 1 | 1 | 45 |  |
| `The three-dimensional relativistic Vlasov–Maxwell system` ^[openai-math-readme.md:#1] | 1 | 1 | 46 |  |
| `multiplicative functions` ^[openai-math-readme.md:#1] | 1 | 1 | 37 |  |
| `diluted spin glasses` ^[openai-math-readme.md:#1] | 1 | 1 | 43 |  |
| `quantum Heisenberg ferromagnet` ^[openai-math-readme.md:#1] | 1 | 1 | 44 |  |
| `free group factors` ^[openai-math-readme.md:#1] | 1 | 1 | 45 |  |
| `arithmetic progressions` ^[openai-math-readme.md:#1] | 1 | 1 | 41 |  |
| `semidefinite threshold` ^[openai-math-readme.md:#1] | 1 | 1 | 40 |  |

## What the extraction ran into

No candidate counts zero, so there is no inflection, export damage or true absence to explain among the 51. The facts the draft lists are both empty: nothing is at 0 word, and no term stands alone less often than it stands with compounds.

What the reading met, each from the lines and counts named.

**Nested surfaces.** `OpenAI` ^[openai-math-readme.md:#2] and `internal OpenAI model` ^[openai-math-readme.md:#2] stand on L13 and L50, and the longer `unreleased internal OpenAI model` ^[openai-math-readme.md:#1] stands on L50 inside the same sentence as the shorter one, so its line is counted in all three rows. `Lean` ^[openai-math-readme.md:#3] counts the two uses on L17 and the one on L29 (`Lean library`); `Lean formalizations` ^[openai-math-readme.md:#2] stands twice on L17. The same holds for `zero-free region` ^[openai-math-readme.md:#2] and `Riemann zeta function` ^[openai-math-readme.md:#2] on L52, which the line writes twice.

**Link syntax.** The bullets of L26 to L29 and the table of L37 to L46 are markdown links. `overview` ^[openai-math-readme.md:#2] stands on L26 as link text and again as the file name `overview.pdf`; `preprints` ^[openai-math-readme.md:#2] stands on L28 as link text and as the directory in the link target. A count of two for these is the link, not two uses in the prose.

**Singular and plural kept apart.** `family` ^[openai-math-readme.md:#2] stands on L24 twice; `families` ^[openai-math-readme.md:#3] stands on L24, L26 and L50. The table column header is `Family` ^[openai-math-readme.md:#1], capitalised, and is not one of the two counted rows. The count is case-sensitive, so the header is a third form of the same word.

**Two spellings of one word.** The document writes `catalogue` ^[openai-math-readme.md:#2] on L24 and L29, and `catalog` ^[openai-math-readme.md:#1] once on L50. `catalog` is not a row of the table; it is recorded here as a variant spelling of `catalogue`, because the two stand in different passages (L24 and L29 against L50).

**The table rows are titles, not terms with a definition.** The ten rows (L37 to L46) are listed as written, each in full; the shorter subject nouns inside them (`multiplicative functions` ^[openai-math-readme.md:#1], `diluted spin glasses` ^[openai-math-readme.md:#1], `quantum Heisenberg ferromagnet` ^[openai-math-readme.md:#1], `free group factors` ^[openai-math-readme.md:#1], `arithmetic progressions` ^[openai-math-readme.md:#1], `semidefinite threshold` ^[openai-math-readme.md:#1]) stand only inside those titles, and each has no sentence about it anywhere in the document. Two of the ten (Mahler and Kaplansky) are named as conjectures in their titles; the document writes the word `conjecture` ^[openai-math-readme.md:#1] and `conjectures` ^[openai-math-readme.md:#1] only there, and `Conjecture` ^[openai-math-readme.md:#1] once, in the sentence of L52 about the Hodge Conjecture.

**Formulas and symbols.** The profile counts no math symbol lines; the one formula-like span, on L52, is plain text and is not quoted. The π in the title on L38 is a Unicode character, and the two en-dashes of the profile's typographic marks are the ones in `The Mézard–Parisi formula for diluted spin glasses` ^[openai-math-readme.md:#1] and `The three-dimensional relativistic Vlasov–Maxwell system` ^[openai-math-readme.md:#1].

**The document's claims about its own standing.** It says the results are „at different stages of verification“ ^[L17] and that „Some of the unformalized results could have issues.“ ^[L19] That is the document's own caution; it is recorded here and decides nothing. Words such as `proved` ^[openai-math-readme.md:#0], `refuted` ^[openai-math-readme.md:#0] and `peer` ^[openai-math-readme.md:#0] stand zero times: the document describes its results with `produced` and `obtained` and, in two places, with `proof`, and never calls any of them proved or refuted.

**Zeros:** 0.

**Standing alone less often than with compounds:** 0.
