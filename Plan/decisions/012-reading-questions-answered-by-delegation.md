# 012 — The three questions the measurements of 2026-09-24 raised, answered by the session on the author's delegation

**Date:** 2026-09-25 · **Decided by:** the session, because the author said „Beantworte die Fragen selber- und fahre fort" · **Status:** chosen, and applied (below); each answer is reversible by the author at any time

## How these were answered

As in decision 008. Each answer takes the conservative side unless the evidence
clearly argues otherwise. None of them is a promotion or a user-facing flag, the
two decisions P0 never leaves to a session. The evidence is the blind
re-readings (`Plan/learnings/extract-terms.md`, *Blind re-readings*), the
record audit (`Plan/runs/record-audit-2026-09-24/`), and the sweep this
decision built (answer 2).

## 1 · Does the author read one document blind, as the first human anchor? — No.

- **The anchor would measure the least consequential step.** Blind readers hold
  97–100 % of a committed list's content, so they see the same things. What
  differs is how much each lists. Answer 2 makes that difference harmless for
  every term the wiki already has, and the record audit checks the step that
  matters to the author: whether a record holds each document's position. That
  step was 95 % faithful.
- **The author's judgement already sits where it decides something:** the
  conflicts (C6 and C9 decided) and the questions. Reading candidate lists would
  spend the scarcest resource on an intermediate artifact.
- **So P27 stays a two-reader ceiling.** A census is measured three ways:
  agreement between blind Claude readers, the sweep, and the record audit.

*Would change it:* an author decision or a record audit that finds a kind of
passage the author treats as a position and no Claude reader listed. Then a
human reading of that document is the next step.

## 2 · How exhaustive is a census? — Selective, by a written rule. Exhaustiveness for what the wiki already knows is reconciliation's job, done by code.

- **The rule** is in `Plan/briefings/extract.md`, *What goes on the list*. List
  what the document names in the novel's world, and the words it uses as its own
  terms: defined, marked, bold, or heading a section or a column. List borrowed
  concepts it applies to the world, marked as lens. Leave out nouns in their
  ordinary sense and the titles of cited works. Keep each surface as written,
  and split joined names as well.
- **The sweep.** `scripts/reconcile.py` now searches every read document,
  standing alone, for every surface of every page. It lists each page the text
  names that no candidate matches, *after* the census is frozen, so extraction
  stays independent (`CLAUDE.md`, *The process*). Each hit is decided and
  recorded in `Plan/runs/sweep.jsonl`, and `reconcile.py --sweep-open` lists
  what is undecided.
- **Measured the same day over the fifteen read documents:** 24 hits. 10 were
  readings the lookup had missed, now on their pages. Among them, `Guardian`
  had been listed where the page's surface is `Guardians`, and emotional
  Kohärenz as Mnemosyne's charge. 14 were occurrences: the novel's title (4),
  `Simulation`, which J39 keeps apart from the Überwelt (3), a book title, words
  in their ordinary sense, a chapter title a page had chosen not to attach, and
  a term a document's own rule keeps out. So the censuses missed about one
  reading every one and a half documents, and code now catches it.
- **Why not truly exhaustive.** Blind readers told "exhaustively" list 90–235
  candidates per 100 lines, so 700–1,250 per document. Judgement took 17–46 %
  of the decisions on documents 4–15 (`reconcile-pre.json`). At that share,
  700–1,250 candidates would give about 120–575 judgements per document, where
  those documents needed 4–230. The sweep delivers the recall an exhaustive
  list was for, at no reading cost.

*Would change it:* the sweep finding many readings in a new document, which
means the rule is too narrow. Or blind readers applying the rule and disagreeing
far below the 0.82 they reached without it.

## 3 · What must a conflict or question record hold? — One entry for every document that takes a position on its question. Passages that support a position it already holds may stay on the pages it links.

- **An entry** is the position, attributed, with at least one citation from
  `read.py --find`. The record is what the author discusses (decision 006). It
  must show every source's position without the author having to open pages.
- **A supporting passage** for a position the record already holds from the
  same document stays on the linked pages. This is how the audit's skeptics
  refuted 44 of 83 findings, and that stays correct.
- **`sources:`** in a conflict's frontmatter counts the documents with an entry.
- **Held going forward** by ingest step 6 (every open record read against the
  document), and checked afterwards by `.claude/workflows/record-audit.js`. The
  audit has covered documents 7–13. Its written entries under this rule are C2,
  C4 and C7, plus Q4 from document 15, found through the sweep.

*Would change it:* records growing past what the author can read. Then one line
per document in the record, with the detail on the pages.

## What was rejected

- **Truly exhaustive censuses**, for the judgement cost above.
- **Removing `Simulation` from the `ueberwelt` page's aliases.** J39 calls the
  mapping doubtful, and the reconciliation that wrote J39 recorded it and did not
  change it. The sweep's three hits on it are occurrences, each citing J39. It
  stays a question for a future reading, not something to decide here.
- **A human reading in place of the sweep.** Code can decide whether a known
  surface occurs. Only whether the occurrence is a reading needs a reader.
