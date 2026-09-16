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

Four moves, in order, each cheap and each producing evidence for the one after.
Reasoning and the measurements behind it:
`Plan/concept/next-step_2026-09-16.md`.

1. **Nineteen more pages by hand.** `Entropie` (three senses) and `Emergenz`
   next — `Emergenz` is the one that forces the conflict record to exist, since
   its conflict already sits on two pages. Twenty pages before any schema, per
   P3.
2. **Then the citation checker, and nothing else.** `scripts/wiki.py check`:
   citations resolve, quotes are in the lines they cite, `MISSING` computed.
   **Run against the twenty hand-written pages first** — if it reports errors on
   careful work, the checker is wrong, and that calibration is free here and
   expensive later.
3. **Then measure one model on the read-source step** against the three
   hand-written notes as a gold set. Cheap models first, OpenRouter where no
   DSPy is needed. Unreachable models report as `NEVER REACHED`, never as 0%.
4. **Then the budget is the author's call**, priced from real numbers rather
   than from the retired system's $2.79 per document.

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
