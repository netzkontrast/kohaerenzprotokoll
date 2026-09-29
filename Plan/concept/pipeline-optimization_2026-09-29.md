# The reading pipeline, measured on its last twenty runs — and what to change

> **A plan. Nothing in it is built, and no document is read to build it.** The
> author, 2026-09-29: „Schau dir die letzten Runs an und plane die Optimierung
> der Pipeline" — a day after „Dont start any new documents" (2026-09-28). Every
> step below can be built and proved on documents already read.

*Every number comes from `Plan/runs/pipeline-2026-09-29/measure.txt` (its
`measure.py`, standard library, about 4 s), from the commands named in that
folder's `README.md`, or from the run notes in `NOW.md`. Pages are measured at
today's size.*

## In one screen

1. **The readings step reads the wiki again.** Reconciliation was built never to
   load a page, and it still does not: `reconcile.py` answers by lookup in about
   a second. But since document 25 the readings are written by readers who edit
   pages, and an edit reads the whole page first. For documents 32–51 the pages
   one document touches total **0.5–1.8 MB, against a document of 7–372 KB**,
   and **89 % of a term page is other documents' readings**. Pages grow with
   every document read, so this cost grows with the wiki — the `O(wiki)` that
   `Wiki/index.json` was built to avoid, one step further on.
2. **The session carries its own history, and so does every reader.** CLAUDE.md
   is 112,437 characters and 34 % of it is a table row and a paragraph per
   document read; NOW.md is 132,113 and 41 % of it is „Previous document"
   sections. Both restate `Wiki/compare/reconcile-NN-*.md`. CLAUDE.md is in every
   subagent's context: a Sonnet subagent that used no tool but its reply and
   answered in eight lines cost **96,427 tokens**.
3. **The review catches what no check sees, and three of its catches recur and
   have a decidable part**: absence counts that were not zero, comparisons with
   documents the reading does not quote, and words a shell ate. **1,284 absence counts
   stand on 121 wiki files and no check reads one.**
4. **Nothing records what a run costs.** `run.md` exists for documents 1–4. For
   5–51 there is no duration, no token count and no list of what the review
   corrected, so nothing below can be scored until step 1 exists.
5. **Two shortcuts were measured and do not work.** Giving a reader only the lines
   around a page's names would have lost 38 % of the lines the committed readings
   cite. And the unread corpus is not copies of the read one: 530 of 534 unread
   documents share less than a fifth of their text with it.
6. **What works stays**: batching documents by page group (documents 33–39
   loaded 5.3× fewer page bytes than one at a time), the session reading the next
   document while readers write the last, reconciliation by lookup, and
   invariants that ran all green in about 80 s.

## 1 · What the last twenty runs were

The process changed three times, each time by hand and each time for a reason
the run notes give: **the session alone** up to document 24; **Claude readers per
document** for 25–32 (three to eight, each file reviewed by the session); **readers
split by page group over a batch of documents** from 33 on, so that no two
readers edit one file. Since the middle of documents 40–43 every reader is
Sonnet — the author's rule after a usage limit stopped six readers there.

| documents | readers | what the run notes record as corrected (`NOW.md`, `CLAUDE.md`) |
|---|---|---|
| 32–39 (32 alone, then 33–39 as one batch) | 3 for 32; 6 by page group for 33–39 | readers ran a read-only `git` command; two re-derived `Wiki/index.json` mid-run; a shared scratch helper was overwritten and wrote wrong frontmatter on `kohaerenz-kernel` |
| 40 | 3 | the other way round: a reader corrected the session's census — cold stands four times, not two |
| 41–43 | by page group | a usage limit stopped six readers mid-run; a straight `"` between two quotations; a chapter link written as a path |
| 44–46 | 4 Sonnet | an altered quotation, „temporäre Entitäten", cited by a line range in parentheses — caught only because 0 unchecked is enforced |
| 47 (50k words) | 6 Sonnet | difference lines that overreached: a Wächterin made into Juna, positions on C7 and C11 the chapters do not take, ordinals nobody counted, two passages joined with `[…]`; `quotes.py` passed every one |
| 48–50 | 5 Sonnet | three absence counts that were not zero; comparisons with documents no quotation carried |
| 51 | 4 Sonnet | comparisons with documents no quotation carried, „even with the rule in the brief" |

**What they yielded.** No page from any of the 30 documents since document 21
(`formel-inversion`); readings on 9–49 pages each; J104–J120; an entry in most
conflict and question records every time; `account.py order` holding after every
run. Candidate lists ran 60–330 terms for these twenty, and 16–142 of each went
to judgement (measure §2).

**How long.** Commit times bound only the readers' half, from the brief to the
reconciliation record: 22 minutes for document 31 (eight readers, 57 pages), 74
for document 51 (four readers, 42 pages). The reading half is bounded by
nothing, because the session read each next document while the last one's
readers wrote.

## 2 · Where the effort goes

### 2.1 The readings step reads the wiki

A reading is an edit of a page, and an edit reads the page first (the Edit tool
refuses a file that was not read). So for every one of these twenty documents the
pages its readings touch outweigh the document:

| | documents 32–51, per document |
|---|---|
| the document | 7–372 KB |
| the term pages it gives a reading | 9–49 pages, **508–1,826 KB** |
| the same pages as a digest — lead, `## Where the sources differ`, `## Open`, one line per reading heading | **66–339 KB** |
| the conflict and question records it enters | 207–536 KB |
| the chapter pages it reads onto | 0–3,010 KB |

**A term page is 89 % other documents' readings** (lead 6 %, differences 2 %, open
questions 1 %). `aegis` is 111 KB with 48 readings, and its digest 11 KB. **A
chapter page is 61 % raw qmd answers**, copied source text for navigation, and
21 % readings; documents 41–43 read onto all 39 chapter pages, 3.0 MB. The
records are append-only by design and grow the same way.

**Each reader also reads the whole document**, and that turns the balance for a
long one: document 47 (372 KB, six readers) was read 2.2 MB worth against 1.0 MB of
pages, while documents 33–39 (88 KB together, six readers) were read 0.5 MB worth
against 1.95 MB of pages. Short documents in a batch pay for pages; a long one pays
for its readers.

**And every run makes the next one dearer.** Document 47 added 740 lines to 62
wiki files, documents 48–50 735 lines to 71, document 51 611 to 55. `aegis` lists
48 of the 51 read documents in its `ingested:`.

**Batching already divides the cost**, because page-group readers load a page
once for the whole batch:

| documents | page bytes, one document at a time | once per batch | as digests |
|---|--:|--:|--:|
| 33–39 | 10.23 MB | 1.95 MB (5.3×) | 0.37 MB |
| 41–43 | 3.72 MB | 1.72 MB (2.2×) | 0.32 MB |
| 44–46 | 2.88 MB | 1.55 MB (1.9×) | 0.29 MB |
| 48–50 | 3.05 MB | 1.69 MB (1.8×) | 0.31 MB |
| 32–51, had they been one batch | 24.63 MB | 2.15 MB (11.4×) | 0.42 MB |

### 2.2 The fixed context

| file | characters | history that `Wiki/compare/` already records |
|---|--:|---|
| CLAUDE.md | 112,437 | 34 % — the per-document table and a paragraph per document; another 16 % is *Installing anything* |
| NOW.md | 132,113 | 41 % — „Previous document" sections, one per run |

Both grow with every document: CLAUDE.md from 36,180 bytes to 113,433 and NOW.md
from 14,137 to 133,665 between 2026-09-23 and 2026-09-28. The session reads both
before it starts. **CLAUDE.md is also in every subagent's context**: the
probe quoted its first heading and the section that names `Coherence
Protocol.mp3`, and said NOW.md was not there. That probe, with no tool but its reply
and an eight-line answer, cost 96,427 tokens — the fixed price of one reader before it
reads anything, with this session's tool set. How much of it is CLAUDE.md was not
separated.

**Each document's summary is written three times** — its reconciliation record,
a CLAUDE.md paragraph, a NOW.md section — which is P6's drift waiting to happen,
and the session's time.

### 2.3 What the review catches, and what could catch it instead

| defect | runs | caught by | the decidable part |
|---|---|---|---|
| a count in prose that was wrong — an absence that was not one (case, a path that did not resolve, `kalt` three times where the census said nothing is cold), cold four times where the census said two | 21, 40, 48–50 | the session recounting; once a reader | all of it: a count is code's |
| a comparison with a document the reading does not quote („no other read source", „as in document 3") | 48–50, 51 | the session, reading | whether the paragraph cites the other document |
| a difference line claiming a position the text does not take, or counting what nobody counted | 47 | the session, reading | none — judgement |
| two passages joined with `[…]` | 47 | the session | whether the pieces stand on one line |
| an altered quotation with an unqualified citation | 44–46 | the 0-unchecked rule | held |
| a straight `"` between two quotations | 40–43 | a reader | all of it |
| a chapter link written as a path | 40–43 | a reader | held: `relations.py` reports a link to no page |
| words a shell ate (an unquoted heredoc) | 22, 28 | the session, after the fact | empty code spans and quote pairs; better, no prose through a shell at all |
| readers running `git`, re-deriving the index, sharing a scratch file | 32–39 | the session | all of it, as a tool list rather than a sentence |
| a usage limit stopping readers mid-file | 40–43 | — | per-page output files make it resumable |

**Checks that are green over drift today** (measure §8, §9):

- **1,284 absence counts on 121 files**, none read by any check. Three were wrong
  in one batch.
- **124 comparison phrases** in 2,765 reading sections and record entries — what
  survived review, rightly or not.
- **Hand-kept frontmatter counts disagree with the body on two pages**: `aegis`
  says 49 readings and has 48, `kern-welten` says 38 sources for 39 `ingested:`
  entries and 37 readings for 38. Ten more keep `readings:` in a format older than
  the `## Reading` heading, and 14 pages cite, qualified, a read document their
  `ingested:` does not list (17 pairs) — whether that is wrong is a rule nobody
  has written.
- **`account.py order` passes a `reconcile.json` with no census beside it**
  (decision 014).

### 2.4 Two shortcuts that do not work

**Windows instead of the document.** If a reader got only the lines within k of a
line naming the page (its surfaces from `Wiki/index.json`), how many of the lines
the committed readings cite would it have seen?

| k | cited lines inside the window | the window's share of the document |
|--:|--:|--:|
| 0 | 0.50 | 0.01 |
| 5 | 0.62 | 0.09 |
| 25 | 0.71 | 0.23 |

A third of the evidence stands where the page's name does not: English names,
pronouns, a paragraph's context. **Readers need the whole document; the saving
has to come from the pages.**

**Skipping near-copies.** `dedupe.py` folded the copies away: of 534 unread
documents with text, 530 share less than a fifth of their 8-word shingles with
the 51 read. There is no large block of the corpus that is already read in
another file.

### 2.5 Where the corpus stands

535 documents are landed and unread, 23.7 MB — 8.3× the 2.85 MB read. Document
30's record was committed at 2026-09-27 12:07 and document 51's at 2026-09-28
09:31: 21 documents in 21.4 hours of wall-clock, the night included. At that
pace the 535 are about 23 days of uninterrupted runs — an extrapolation, not a
measurement — so *what* is read decides more than any step below. The read
documents come from few categories:

| category | read | unread | unread MB |
|---|--:|--:|--:|
| plot-outline | 13 | 205 | 8.55 |
| kernkonzept | 10 | 70 | 2.60 |
| theorie-psychologie | 1 | 42 | 2.41 |
| aegis | 1 | 37 | 1.53 |
| theorie-physik | 5 | 32 | 1.69 |
| charaktere | 6 | 31 | 1.51 |
| storyform | 6 | 28 | 1.27 |
| theorie-logik | 1 | 23 | 1.22 |
| worldbuilding | 5 | 17 | 0.96 |
| theorie-mathematik | 2 | 17 | 0.88 |
| theorie-philosophie | 1 | 16 | 0.55 |
| audit | 0 | 15 | 0.40 |
| theorie-genre | 0 | 2 | 0.10 |

Six categories have one read document or none. That is P10's `MISSING` at the
scale of the corpus.

## 3 · The plan, in order

| step | what | size | depends on | the author's |
|---|---|---|---|---|
| 1 | record what a run costs | one script, a selftest | — | no |
| 2 | write each document's history once | text moves, no code | — | **yes** |
| 3 | five checks for what the review keeps catching | code, selftests | — | one rule (3c) |
| 4 | readers return readings, code writes the pages | two scripts, an agent definition, a pilot | 1, 3 | **yes** |
| 5 | batches by shared pages; read ahead | practice | 4 | no |
| 6 | what to read, and how deep | a decision, then a sample | 1–5 | **yes** |

### Step 1 — Record what a run costs

**What.** `Plan/runs/<slug or batch>/run.json`: per phase — read, list, count,
census, note, reconcile, brief, readers, review, record — when it started and
ended; per reader its model and the `subagent_tokens`, `tool_uses` and
`duration_ms` the Agent notification reports; and `corrections.jsonl`, one row per
thing the review changed in a reader's output: `{class, page, before, after}`. A
small `scripts/runlog.py` appends events with the clock, so no one types a
timestamp (P26), and `state.py` measures `runs.*` from it.

**Why.** Every choice below is a guess about where time and tokens go until this
exists. The project's only token numbers are for second readers and entity lists
(`NOW.md`); the corrections vanish before commit, so the review's catch rate —
the thing step 3 wants to shrink — has never been counted.

**Proof.** `runlog.py selftest`: an event out of order, a reader with no usage,
a correction with no class — each refused.

**May not.** Fill a gap with an estimate. A phase not logged is „not recorded",
never 0 (P15, P23).

### Step 2 — Write each document's history once

**What.** CLAUDE.md keeps what exists — the state with its markers, the process,
the rules — and its per-document table and paragraphs move, word for word, to
`Wiki/compare/README.md`, where the records they summarise live. *Installing
anything* moves to `.agents/skills/tools/references/install.md`; the table at the
top of CLAUDE.md stays and points there. NOW.md loses its „Previous document"
sections, which the records and git already hold, and keeps what is open. From
then on a document's story is written once, in its reconciliation record.

**Why.** 34 % + 16 % of CLAUDE.md and 41 % of NOW.md, in the session's context
at every start and CLAUDE.md in every reader's. CLAUDE.md would go from 112k
characters to about 57k, NOW.md from 132k to about 78k — and stop growing with
every document.

**Proof.** `state.py --prose` holds before and after. None of CLAUDE.md's 48
markers is in the per-document history; one is in *Installing anything* and moves
with it, and NOW.md's „Previous document" sections carry two, which leave with
them. Whether `state.py` should measure the two files' size, and fail above a
budget, is the author's (P4).

**May not.** Rewrite or drop a sentence. Every paragraph moves as it is, the
author's quoted words with it.

**Needs** the author's yes: CLAUDE.md is the working agreement.

### Step 3 — Five checks for what the review keeps catching (P1)

Each ships with selftest cases that fail on today's code, as `quotes.py`'s did.

- **3a Absence counts are asked, then checked.** `read.py <slug> --count
  "<words>"` answers with the whole-word count, the case-insensitive count and
  the compounds — `capture.count_both`'s normalisation — so a reader asks for a
  count and never types one. A count that goes onto a page carries a mark
  `quotes.py` can check, for example `` `Flight` ^[slug.md:#0] ``, and a claimed 0
  whose case-insensitive count is not 0 is named as exactly that — the
  `Dekanonisiert` case. `quotes.py` also reports how many absence phrases carry no
  mark, so the 1,284 are a measured backlog and not a silent gap (P23).
- **3b A comparison names what it compares with.** In a section added for
  document D, a sentence with a comparison phrase — „only", „no other", „every
  other", „the first read …", „earliest", an ordinal of positions — and no
  citation of another document in its paragraph is listed for the reviewer. A
  flag, not a failure: whether the comparison is true stays judgement.
- **3c Frontmatter counts are derived.** `sources:` and `readings:` follow from
  the body, and `wiki_index.py --check` says where they do not. One rule first:
  does a citation in a difference line make a document `ingested` on that page?
  (14 pages, 17 pairs.) And what the ten pages in the older format count.
- **3d `account.py order` refuses a `reconcile.json` with no census or note**
  beside it — the gap decision 014 found.
- **3e Shell damage and stray quotes.** On added lines: an empty code span, a
  quotation mark pair with nothing between, a straight `"` between two „…"
  quotations. And the rule under two of them: prose is never written through an
  unquoted heredoc — step 4's renderer writes files from files.

### Step 4 — Readers return readings; code writes the pages

The largest change, and the one the measurements point at.

- **What a reader writes.** One file per page it reads for,
  `Plan/runs/<batch>/readings/<page>.md`: the heading's fields (document, date,
  prose name, what it adds), its prose with each quotation in „…" followed by
  `^[?]`, its difference lines, its „not read: why" verdicts, and absence counts
  as `--count` answers. **It edits nothing in `Wiki/`.**
- **What code does with it** — `scripts/readings.py apply <batch>` or similar:
  resolves every `^[?]` with `read.py`'s find, the same comparison `quotes.py`
  runs, so what it places cannot fail the check, and what it cannot place it
  refuses and names the nearest line. This is the rule that made the entity lists
  verify — names in, lines by code (P26). It inserts the section by date,
  writes the frontmatter (3c), runs `quotes.py`, `link.py` and `relations.py` on
  the pages it touched, and prints the diff the session reviews. Commits stay one
  per page or page group, naming the document.
- **A digest instead of the page.** `digest.py <page>`: the lead,
  `## Where the sources differ`, `## Open`, one line per reading heading, and this
  document's own readings if a scan left some. Measured: 11 KB for `aegis` instead
  of 111 KB; 0.07–0.34 MB per document instead of 0.5–1.8 MB; 0.29–0.42 MB per
  batch instead of 1.55–2.15 MB.
- **A reader agent.** `.claude/agents/wiki-reader.md`, Sonnet by the author's
  rule, with a short tool list — reading, searching, writing its own folder — so
  „never run git" and „edit only your files" become the tool list rather than a
  sentence in a brief (P26: a prompt is not somewhere to ask). How far an agent
  definition can restrict a path is to be checked when it is built, not assumed.
- **One brief.** The rules repeated in every readers' brief — nine rules, the
  record rules, the chapter rules — live once, in the agent definition; a brief
  carries only what this document says (P6).

**Proof.** A fixture page and a fixture reading file render to an expected page;
selftest cases: a quotation its line does not hold (refused, the nearest line
named), a section out of date order, the frontmatter after insertion, a straight
quote, a link to no page, a `[…]` across two lines.

**The pilot needs no new document.** Documents 48–50, on a worktree at `3d97d39`
— their censuses, notes and readers' brief committed, no reading yet, and no
`Wiki/` file changed since `4e27331` — with the output compared to what `7f11861`
committed: which pages got a reading from each document, which lines they cite,
what the session would have corrected (step 1's ledger), and tokens and minutes
per reader. Its bar, set now so the pilot cannot choose it: 0 unresolved and 0
unchecked quotations; no more corrections than the original run noted; the pages
with a reading agreeing with the committed set at F1 ≥ 0.8.

**May not.** Create a page, merge two readings, write prose, or decide a
conflict. Record entries go the same way: a file per record, appended by code at
the end.

**Needs** the author's yes for the pilot's Sonnet usage (three documents, 102 KB
of text) and for readers no longer editing pages themselves.

### Step 5 — Batches by shared pages, and the next batch read while the last is written

- **Choose a batch by the pages its documents touch.** Each document's
  pre-classification and sweep name them before any reader starts. Documents
  32–51 as one batch would have needed 0.42 MB of digests where one at a time
  loaded 24.6 MB of pages.
- **Make the overlap the rule**: the session reads and lists batch N+1 while
  readers write batch N. It happened on 2026-09-28, by hand.
- **A usage limit costs a page, not a reader.** With a file per page, a stopped
  reader's finished pages stand, and the batch's list names what is left.
- **Fewer, longer readers**, if step 1 shows the fixed context dominates: every
  reader pays it once (96,427 tokens in the probe), whatever it then reads.

### Step 6 — What to read, and how deep

Decision 001's scope and P0, so a proposal only:

- **Sample before choosing.** With the pipeline of steps 1–5, two documents from
  each of the six categories with one read document or none, and step 1's
  numbers per category: readings, record entries, positions a record did not
  have. Then a rule for the rest, from what paid.
- **Depth as a choice.** A full ingest; or readings only, for a document whose
  terms all have pages, its candidate list written for a sample to keep gold data
  growing; or a scan whose lines are placed by code — the 2026-09-25 scan cited 44
  of 152 quotations to lines that did not hold them.
- **A claim before a read.** Documents 16, 17 and 20 were each read twice by two
  sessions following one handover. A claim file, or an open pull request named
  for the slug, before reading starts.

## 4 · What stays as it is

The census describes one document; the candidate list is written while reading
and ruled gold by decision 009; reconciliation answers by lookup and never
through qmd; conflict detection is never mechanised; `quotes.py` stays strict;
one commit per page or page group names its document; nothing is promoted; no
corpus text goes to a third party — the readers stay Claude.

## 5 · Questions for the author

1. **Step 2** — may the per-document history leave CLAUDE.md and NOW.md for
   `Wiki/compare/README.md`, word for word?
2. **Step 4** — may readers write reading files that code turns into pages, and
   may the pilot on documents 48–50 spend the Sonnet usage it needs?
3. **The raw qmd answers are 61 % of the chapter pages.** Keep them there, or
   beside their run in `Plan/runs/qmd-chapters-2026-09-26/`, linked?
4. **3c** — does a citation in a difference line make a document `ingested` on
   that page?
5. **When reading resumes** — by which rule, how deep, and who claims what?
6. **The candidate list** is the gold artifact and stays. Since document 22, 30
   documents with full lists made no page. Whether every document still needs its
   list to decision 012's full rule, or a sample does, is yours.
7. **The session-start install** builds seven virtualenvs, about 3.5 GB (`du`,
   2026-09-29). Four of them — `.venv-grawiki` (1.6 GB), `.venv-dspytools`,
   `.venv-mflow`, `.venv-semantica`, 2.9 GB together — serve nothing the pipeline
   or `selftests.py` calls; landing needs `.venv-tools`, the self-tests
   `.venv-dspy`, `.venv-typesafe` and `he`. Only those at start, the rest on
   demand? A cold container's install time is unmeasured.

## 6 · What would change the plan

- **If step 1 shows the session's own reading dominates the time**, step 4 saves
  tokens, not hours, and question 6 is where the time is.
- **If the pilot's digest misses what the whole page would have shown** — a lead
  the original run corrected and the pilot does not — the digest gains the last
  few readings.
- **If a reader agent with a short tool list costs no less than the probe**,
  fewer and longer readers is the only lever on fixed context.
- **If the corrections ledger shows a recurring class no check can hold**, that
  class goes into the reader's definition in words — and only then would an
  optimiser on the reader's instructions be worth running. `pairs.py` measured
  GEPA at fourteen times the cost of eight labelled demos, for a lower score
  (`Plan/concept/dspy-optimization_2026-09-25.md`).
