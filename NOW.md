# Now

*What is open. One page, hard limit. Finished work leaves this file — git
remembers it. If this does not fit on a page, too much is open at once.*

**Updated:** 2026-09-16

## Doing

**Reading sources by hand, to decide the note format before writing a tool.**
Three read, all `theorie-physik`, all within two days of each other in the source
chronology — and they turned out to be one of each kind:

| slug | kind | what it gave |
|---|---|---|
| `entropie-aegis` | `brief` | AEGIS as Entropic Gatekeeper; 20 unanswered questions |
| `aegis-emergenz-aus-der-leere` | `critique` | two more AEGIS expansions, and a rejection of both |
| `kohaerenzprotokoll-aegis-und-systementropie` | `result` | answers three of the brief's questions, two days later |

The format needed exactly one field added — `kind` — and then held across all
three. `Plan/learnings/read-source.md` has the predictions and what falsified
them.

## Next

**Document by document, in order, each one finished completely before the next.**
The point is not speed — it is that a term obviously important in document 1 and
mentioned once in document 2 is exactly where a conflict hides, and only doing
them in order with a carry-forward list catches it.

1. ~~**Term census per document.**~~ **Four documents have one**, each written
   from its own document only — 46, 94, 71 and 58 candidates, twenty-one special
   cases. Three comparisons in `Wiki/compare/`, **each superseded by the next**.
   Next: **write the 13 new pages and 3 new readings** that
   `Wiki/compare/004` names.

2. **`reconcile` replaced `compare`.** One frozen census against the current
   pages, not against every earlier document — per document, append-only. The
   first three comparisons each superseded the last, which was the step saying it
   did not scale. `Plan/concept/what-is-being-tested_2026-09-16.md` has the
   design and what it makes measurable.

3. **Every step keeps its artifact** — `Plan/runs/<slug>/`, written by
   `scripts/capture.py`. **The first four documents lost their candidate list**,
   so they cannot be the gold set that three hand-read documents were supposed to
   provide. Document 5 onward is captured properly.

4. **Start timing a census.** The retired pipeline cost $2.79 and 18 minutes per
   document; the hand process has **no equivalent number at all**, so the
   comparison the whole plan turns on cannot be made. Four documents done, none
   timed.
5. ~~**Then the conflict records.**~~ **`C1` and `C2` exist** — AEGIS' three
   expansions and Entropie's two senses, append-only, in `Wiki/conflicts/`.
   Decision 003 is real rather than chosen. `blinder-fleck` is the next, with two
   bearers and no document that knows both.
6. **Then the counter** — not an extractor. The first document showed the tool
   the work actually wants: *given a list of candidates, report occurrences,
   lines, substring collisions and frontmatter contamination.* Proposing and
   judging stay with the reader. `Plan/learnings/extract-terms.md` has the
   derivation, step by step.
7. **Then the citation checker**, calibrated against the hand-written pages
   first — if it reports errors on careful work, the checker is wrong.
8. **Then measure one model** against the hand-written censuses and notes as a
   gold set, and **then** the budget is yours to decide, priced from real
   numbers rather than from the retired system's $2.79 per document.

Reasoning and the measurements behind 4–5: `Plan/concept/next-step_2026-09-16.md`.

## Worth acting on soon

**`[User Query]` is a provenance marker and 24 documents use it.** It separates
what the project asserted from what the research concluded, inline, mechanically
extractable. A `premise` / `finding` flag per reading is the cheapest
high-value signal found so far. Recorded in `read-source.md` §f; not yet built.

**A result can close an earlier document's open question.** Nothing in the corpus
links a brief to its answer, and one result's brief is not among the landed
documents at all. `MISSING` is a property of a term *at a date*, not of a term.

**A conflict gets one home, not one per term** — decision 003. The emergence
conflict on the AEGIS page belongs equally to `Emergenz`. The retired system hit
this live: 2 of its 7 conflicts were the same argument reached from two
different concepts.

**Conflicts live on terms the project owns, not on terms it shares.** Of the five
terms in all three documents, the three project-owned ones each carry a conflict
and the two borrowed ones carry none. The test — *does this word mean something
outside this project?* — costs no reading and is made once per term.

**`Wiki/candidates/juna.md` is titled by a name none of the four sources uses.**
Zero occurrences of `Juna` across all four. Document 4 adds a **third** surface —
`Partnerin`, 30 times — and the four read documents never link it to `Julia`.
**The corpus does, in 17 documents**, which only a check outside the comparison
could establish. Either rename the page to what its readings say, or carry the
name with the count that justifies it.

**A comparison answers questions about the documents it compares, never about the
corpus.** Anything of the form *does the corpus ever…* is a separate check
against all 409 and has to be said separately.

**A source claiming authority over other sources must not be granted it.** One
document in the corpus declares every document that disagrees with it
deprecated. The retired pipeline believed it and silently dropped that concept
out of its own contested count. A gather step proposes; it never resolves.

## Deliberately deferred

**39 `md` rows and 1 `mp3` stay unfetched** by the author's decision
(2026-09-16). Nothing depends on them. Four `md` rows did land, so the
connector's supported-types list is not the whole truth — revisit together.

**247 `plot-outline` rows** rest with the novel.

## Waiting on the author

- **`Plan/concept/` review** — three documents describe what is being built.
  Nothing blocks on it, but building against an unread plan is how the last one
  went wrong.
- **PR #45** — the first three notes and the corrections they forced.

## Closed since last update

- ~~Fetching the corpus.~~ **409 of 680 landed**, every category the wiki needs
  complete, no model in the loop at any point.
- ~~The flat-heading question (`fetch.md` §7).~~ **It was never a problem.**
  Google Docs carry a median of 17 real headings, identical to `.docx`. The
  claim came from one atypical document and stood through three learnings
  before anything counted the other 359. `fetch.md` §7c has the numbers.
