# Now

*What is open, and what a person still has to decide. **No counts live on this page**: numbers come from `python3 scripts/state.py`.*

```bash
python3 scripts/state.py            # everything, derived now
python3 scripts/state.py --prose    # fail on any stale number in prose
python3 scripts/account.py order    # the pipeline's order; red means something is half-done
python3 scripts/selftests.py        # every self-test; a suite that says `not run` has not passed
```

This page is the handover between sessions, and it is meant to be **one page**: what is open now, in the order to act on it. A thing that
is done leaves it — git holds what happened (`git log -- NOW.md`; the long version of this page, as it stood before its rewrite of
2026-09-30, is `git show 8b8fde3:NOW.md`, and a merge of 2026-10-01 had put most of it back, 613 lines, `git show 7e361e3:NOW.md`),
decisions go to `Plan/decisions/`, measurements to `Plan/runs/` and `Plan/concept/`. The questions the sources and the process leave to
the author are collected, verbatim, in `Plan/questions-for-the-author.md`.

## The author's standing instructions

In force until the author says otherwise; newest first.

- 2026-09-30 **„Is the backfill usefull? If not - stop it"** — it was not, and it is stopped (`Plan/decisions/019-…`); a committed `STOP` file keeps it so.
- 2026-09-30 **„achte auf mein Nutzungslimit - starte diese nicht parallel"** — model runs go one at a time, each recorded; Claude calls draw on the author's usage.
- 2026-09-30 **„stop Reading document - you should Improve the Pipeline"**, and 2026-09-28 **„Dont start any new documents"** — no document is read until the author says so.
- 2026-09-29 **„The novel in Legacy is Not the quality I want"** — the parked draft is never a voice reference or canon. Drafting waits on the plan's four questions, below.
- 2026-09-26 **„Those arent Texts for the novel - only Research"**, and „Yes, 22 and 23 are research too" — narrative texts among the sources are research, never the novel's prose.
- 2026-09-24 **„Notiere in Zukunft einfach deine Fragen und setze fort"** — questions are noted and the work continues. **Decision 006**: every draft is back in question;
  no date or claim to be canon settles anything. Decided: **C6**, five Guardians (LogOS, Mnemosyne, Cerberus, Kairos, Sophia); **C9**, the Konstrukt-Stadt is KW1.
- No corpus text leaves the container — to Jev, OpenRouter or any third party — without the author's decision (decisions 007, 008, 011).

## Questions for the author — noted, not waited on

None of these blocks the pipeline. The full context of each is where it is named.

1. **The novel-writing plan** (`Plan/concept/novel-writing-plan_2026-09-29.md`; nothing in it is decided). Four questions come first, options and the case for each in its §11:
   **A** who writes the prose (the session whole chapters / scene by scene on beats the author approved / the author, with the writing skills critiquing — recommended: not whole chapters);
   **B** the September draft's ideas (land its premise and drafting record as research, or leave all of it parked — recommended: land them);
   **C** where the book lives (a new top-level `Novel/` / inside `Wiki/` / a repository of its own — recommended: `Novel/`);
   **D** reading on demand while writing (for the chapter in hand / each document on the author's yes / none until the first draft — recommended: each document on the author's yes).
   Then the sixteen Weichen W1–W16 in four rounds: sheets for W1–W10, W12, W15 and WP stand in `Plan/weichen/` (options, gains, costs, a recommendation, dependencies; none is a decision),
   and `Plan/concept/treatment-probe_2026-09-30.md` makes the recommendations concrete; W11, W13, W14 and W16 have no sheet yet. The plot question of 2026-09-29
   („I dont Like that the novel does Not Flow Like a scifi novel - i want more Action - its a question of the Plot") opens round 1 at W2.
2. **Six graph questions** (`Plan/concept/graph-contracts_2026-09-30.md` §8): (1) the normalised co-mention relation in `graphrag`'s walk — on at weight 3, at 10–30 for conflicts and questions only, off, or wait for more labelled cases;
   (2) which HyperExtract contracts may run on which of the 528 documents nobody has read (about $190 a contract for the corpus; the backfill over the read ones was stopped, decision 019);
   (3) who labels — every contract's precision rests on one reader's labels; (4) the finders' defaults in `ask.py` — `he-lines` at 40 lines (+0.029 document recall, off) and the co-mention finder's 10 paragraphs (at 3, the pack is 13 % smaller with the same gold lines: `Plan/runs/architecture-session-2026-10-01/packs/`);
   (5) 40 pages the corpus holds together and the wiki does not link (`Plan/runs/graph-lab-2026-09-30/e2c-links.md`) — any wanted; (6) whether the wiki holds the writing engine's vocabulary (the Narrative Context Protocol is written in 37 documents, the Collapse Susceptibility Index in 7).
3. **`Coherence Protocol.mp3`**, the one row not landed: markitdown can only transcribe it by sending the audio to a third-party speech service. A yes, and a service the author is content with, lands it.
4. **Entity lists and translation pairs for the 215 plot outlines landed on 2026-09-26.** `entity-lists` sends text to Haiku and `bilingual.py` to free OpenRouter models and Jev, so both wait on a yes; until then a name that occurs only in those documents has no entry in `Sources/README.md`.
5. **Process decisions** (context in `Plan/questions-for-the-author.md`, Part 2): whether DSPy runs on Claude through `claude -p` stand (decision 011) and whether SIMBA (about $8) runs; whether `fold()` adopts the plural rule of decision 010;
   the rule for a reviewed page that a new source contradicts (needed before the first promotion); chapter-level differences as conflict records, chapters in the graph and the app, and when the app is rebuilt;
   `GOAL.md` against the working agreement; whether the new tools read every document as second readers; which session reads which document when several run.
6. **An independent gold for the retrieval bench** (`Plan/concept/evaluation-audit_2026-09-30.md` §3). The bench's gold is 92 % lines the pages already quote and no unread document can score, so it tests the wiki's own graph, not discovery. What only you can give: grades on about 60 lines (to calibrate a judge), and, if you will, 20–30 questions with the lines you would point to; and a yes to a small first-party Claude spend (a few dollars) for pooled judging.
7. **The novel's open content questions** — where the sources disagree (conflict records C1–C15, question pages Q1–Q9) and what no source settles — are in `Plan/questions-for-the-author.md`, Part 1.

## Half-done — where the next session starts

- **The architecture is [`SPEC.md`](SPEC.md), adopted by the author** (decision 021, 2026-10-01). The deterministic question-to-evidence path stays; one hit and pack contract goes under every finder; RLM and novelgraph stay optional finders until E4. Steps 1 and 2 are built: the retrieval cases are frozen (`Plan/eval/retrieval-cases-v1.json`) and every line-gold bench reads them (`benchset.cases`). **Next: step 3**, one owner for the store (`askdb.py` keeps freshness and `evidence_rows`, `kg.py` imports them), then steps 4–7, all offline, one PR each (`SPEC.md` §9). **E4 is approved**: Claude only, serial, $20 for the whole run, and not before steps 2 and 4. The ask-pack measurement (`Plan/runs/architecture-session-2026-10-01/packs/`) found that the pack already sends 98 % of what the route finds, so recall work goes to the route.
- **Step 6 of the pipeline plan (decision 015) is paused by the author.** Its sample is the two newest unread documents in each of six categories; seven of the twelve are read and reconciled. **Five are unread**:
  `textanalyse-existenz-system-und-leid`, `kohaerenz-protokoll-hard-sf-horror-thriller`, `hard-sci-fi-cosmic-horror-research-questions`, `ki-assistent-romanwelt-kohaerenz-und-aegis-spec`, `aegis-persona-and-manifest-generation`.
  When the author says go: one reader at a time, marked by model (the lab's clean reader, `claude -p` with no tools, cost about 9 thousand tokens a call against a subagent's 67 thousand — `Plan/runs/reader-lab-2026-09-30/`),
  each document reconciled as it lands so that `account.py order`, which CI runs, stays green, and **claim before reading**: an open pull request naming the slug under a `Claim` heading (two sessions once followed one handover and read documents 16, 17 and 20 twice).
- **The HyperExtract work is measured and nothing is adopted.** 32 contracts (`Plan/hyperextract/`), run by `he_claude.py` on `hx.py` — HyperExtract ported to the standard library, byte for byte what upstream sends (decision 020) — and loaded by `hegraph.py` as `P_HE_*` proposal edges, never into the core graph; `he-lines` and the co-mention relation are off.
  The backfill over the read documents stopped after 14 of 137 runs because five more gold documents moved `he-lines` by nothing (decision 019). To resume it, only with the author's word: delete `Plan/runs/hyperextract-backfill-2026-09-30/STOP`; `backfill.py status` names the rest.
- **Gold for learnings** (PR #131, `Plan/runs/gold-2026-09-30/README.md`). Six more documents have a gold candidate list and nothing else — steps 1–3 only,
  no census, note or reconciliation, so `account.py order` is untouched and step 6's pause stands. `scripts/goldeval.py` scores every extractor (the HyperExtract
  contracts, entity lists, blind re-readings) against every gold list, and `scripts/goldrel.py` holds a blind reader's relations in the contracts' own types,
  piloted on three documents. **Open:** a second blind relation reader on those three documents — the ceiling a relation score has to be read against, one model
  run, one at a time — and only then more documents. What it adds to the evaluation audit: `Plan/concept/evaluation-audit_2026-09-30.md` §5.
- **Entity lists**: `scripts/entities.py` works, lists exist for five documents (`python3 scripts/state.py --get entities.lists`), and the full run over the landed documents has not happened — it waits on the yes above.
- **The branch** `claude/elegant-ramanujan-onfl2w` carries the session's work, and the author merges its pull requests while a session runs. After a merge: `git merge origin/main` into the branch (never a rebase, never `checkout -B`), then open a new pull request.
- **Every check runs on GitHub** (`.github/workflows/checks.yml`) on every pull request and every push to `main`; a pull request with a merge conflict is not checked at all.

**Known failing:** nothing is known to be. A red check names itself; `python3 scripts/selftests.py` runs them all.

## Where things are

- `CLAUDE.md` the working agreement; `PRINCIPLES.md` the rules we follow and the evidence for each; `GOAL.md` the author's brief, which describes the target, not the repository.
- `Plan/decisions/` one file per decision; `Plan/concept/` notes and proposals; `Plan/runs/` what every run kept; `Plan/learnings/` what each step taught; `Plan/weichen/` the decision sheets for the novel.
- The skills in `.agents/skills/` (the pipeline: `tools`, `ingest`, `reader-tools`, `graph-context`, `qmd`, `hyperextract-learning`); the graph: `Plan/concept/graph-contracts_2026-09-30.md`.
