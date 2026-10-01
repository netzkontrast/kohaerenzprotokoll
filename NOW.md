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
2026-09-30, is `git show 8b8fde3:NOW.md`), decisions go to `Plan/decisions/`, measurements to `Plan/runs/` and `Plan/concept/`. The
questions the sources and the process leave to the author are collected, verbatim, in `Plan/questions-for-the-author.md`.

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
Every chapter page now opens with **what the chapter is about** — its readings
summarised and placed in the Heldinnenreise, Heldenreise, cycles, Kishōtenketsu,
acts, Vortex, brackets and Dramatica A/B, each source named where they differ — and
ends with **eight basic questions filled with its plot, 10–12 of its own, a table of
twelve unread candidate sources, and qmd's raw answers**
(`Plan/runs/qmd-chapters-2026-09-26/README.md`). The table is a place to look,
never a reading or a number.

**Read next, in this order:**

1. ~~`koharenz-protokoll-kapitel-0-v2-md`~~ — read 2026-09-26, document 25 (*Next
   document*, below). No Kap 0 question had returned it: the method's limit, measured.
2. ~~`worldbuilding-konzept-kohaerenzprotokoll-md`~~ — read 2026-09-26, document 26.
3. ~~`kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md`~~ — read 2026-09-26, document 27; it names Kap 11, 12, 15,
   24, 25 and every chapter from Vortex 1 to the end, 35–40.
4. ~~`2026-09-14-kap25-vertiefung-md`~~ and ~~`kp-kap25-2026-09-14-md`~~ — read 2026-09-26,
   documents 28 and 29: the log of a drafting run on Kap 25, and the chapter file it revised.
5. ~~`kohaerenz-protokoll-philosophischer-bericht-md`~~ — read 2026-09-27, document 31. The tables
   had listed it for Kap 3, 6, 7, 17, 24, 32, 35, 36, 38; it names only Ch 35–36 and Kapitel 13.
6. ~~`dual-storyform-hintergruende-md`~~ — read 2026-09-27, document 30, before item 5 on the
   author's „das übernächste"; it names Kap 1, 13, 28, 33 and 35–39, no Kap 22 and no Kap 40.

Four whole-novel plans from before May 2026 — read 2026-09-27, documents 40–43 — are in more than half the tables and marked *in most
chapters* there — `monstergruppe-primzahlen-plot-blueprint`,
`hard-sf-roman-outline-dkt-physik-cosmic-horror`,
`dramatica-storyform-synthese-aegis-analyse-2`,
`roman-konzept-dualitaet-kohaerenz-spannung` — as is the worldbuilding concept.
They are reading for the book's shape, not for one chapter. For a single chapter,
its own table below the shared ones is the list; `chapter_sources.py across`
prints every document with its chapters.

**Noticed, not settled:** for Kap 24, four read sources write „B: OS-Psychology,
Host-System-Verstrickung", where GOAL.md §5.2 has B's OS in Physics and its RS in
Psychology; Kap 29's readings give B's line as RS-Psychology. The summaries repeat
the readings; whether the sources mislabel a throughline or GOAL.md does is the
author's.

## Handover — the next session starts here

**The pipeline plan of 2026-09-29 is built through step 5** (decision 015; the plan's last section
lists what exists). The next session starts on **step 6, the sample**: the two newest unread documents in
each of the six categories with one read document or none, read with the new readings step
(`wiki-reader` files, `readings.py apply`, `runlog.py` from the first phase):

- audit: `technical-audit-research-mandate-the-kohaerenz-pro…`, `kohaerenz-protokoll-audit-und-verifizierung`
- theorie-logik: `ki-narrative-kollaps-kohaerenz-paradoxie`, `kohaerenz-protokoll-meta-foreshadowing-beobachter-…`
- theorie-psychologie: `angst-bei-komplexen-traumafolgen`, `flow-zustaende-und-dissoziative-identitaet`
- theorie-philosophie: `ontologische-inversion-von-aegis-kritisches-framew…`, `textanalyse-existenz-system-und-leid`
- theorie-genre: `kohaerenz-protokoll-hard-sf-horror-thriller`, `hard-sci-fi-cosmic-horror-research-questions`
- aegis: `ki-assistent-romanwelt-kohaerenz-und-aegis-spec`, `aegis-persona-and-manifest-generation`

Slugs are cut here; `python3 scripts/sources.py status` and the manifest have them whole. **Claim before
reading**: an open pull request whose title or body names the slug under a `Claim` heading, checked for in the
open pull requests first — two sessions following one handover read documents 16, 17 and 20 twice.
**Claimed 2026-09-29 by netzkontrast/kohaerenzprotokoll#110, all twelve; the claim passes to the pull
request that follows it.** #110 was merged on 2026-09-30 with two of the twelve extracted,
`ontologische-inversion-von-aegis-kritisches-framework` and `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`.
The other ten readers ran in parallel and were stopped by the session's usage limit. Their candidate
lists and counts are complete and gold (`gold.py`). Whatever they had written of a census or note is
in `Plan/runs/<slug>/partial-2026-09-29/`, moved out of `Sources/` so that no tool counts a fragment
as a census.

The author, 2026-09-30: „starte diese nicht parallel … beobachte jeden der zehn … versuche diese als
lernlabor zu verstehen … gib ihnen unterschiedliche Anweisungen … versuche auch die letzten paar prs
zu verstehen und passe und erweitere die Pipeline entsprechend an". So the ten are read one at a time,
each under its own instruction, and each run is recorded in `Plan/runs/reader-lab-2026-09-30/`.
What the first twelve readers cost is measured there from their transcripts.

**Each document is reconciled as it lands**, not all twelve after the last extraction. So
`account.py order`, which CI runs, is red only between an extraction and its reconciliation.

**Step 6 is paused by the author, 2026-09-30:** „stop Reading document - you should Improve the
Pipeline". Nothing reads a document until the author says so.
- The readings reader for documents 52 and 53 was stopped before it wrote a file. Their lookups and
  the readings brief stay in `Plan/runs/step6-readings-52-53/`, and document 54's in
  `Plan/runs/step6-readings-54/`.
- Three documents had a census and a note and no reconciliation: 52, 53, and the technical audit
  R1 extracted, so `pipeline order` was red and CI failed on `main`. On 2026-09-30 the author chose
  to reconcile them to fix CI: two `wiki-reader` runs from the two briefs, `readings.py apply`, and
  `Wiki/compare/reconcile-53` to `-55`. No page was added; C2, Q3 and Q8 gained entries. The order
  holds. The pause stands for every other document.
- The work now is the pipeline itself, measured offline on what is already read:
  - the reconciliation record drafted by code;
  - the readings brief drafted by code;
  - the census draft wired into the reader's definition.
  - **Later the same day:** the four reader-lab documents are reconciled (see *PR #126 CI repair*, below), one Sonnet `wiki-reader` for the three
    that had pages to speak to, and step 6 is paused again; five of the twelve sample documents (`textanalyse-existenz-system-und-leid`, the two theorie-genre documents and the two aegis documents) are still unread.

**A parallel session builds `ask` (PR #119, decisions 016 and 017), and #120 carries it merged in.**
Two things from it change this lab:
- Its claude-cli backend, `claude -p` with no `CLAUDE.md`, no tools beyond those named and no
  thinking, is the lab's biggest lever. Tried on 2026-09-30, it was about 9 thousand tokens a
  call against a subagent's 67 thousand. `Plan/runs/reader-lab-2026-09-30/clean_reader.py` runs
  a reader that way, shut in its own directory; code checks its files and puts them in place.
- Decision 017 lets OpenRouter's free models and Jules answer `ask` packs as trials. Decision
  014 lets Jules ingest one document.

The comment on #119 asked that session for three things:
- a Jules extraction of `kohaerenz-protokoll-hard-sf-horror-thriller` as a comparison arm, written
  only under that document's `jules-2026-09-30/`;
- `askdb.py touches <slug>`, so each reconciliation record can name the Weichen its document
  bears on (one encoding, rather than a lens for readers);
- a pack, verify and render that take parameters, for an extraction pack.

**A qmd search over all 347 unread landed documents ran on 2026-09-26** (`Plan/runs/qmd-scan-2026-09-26/`): one to four short queries per open record, hits only, no reading. It placed all fifteen unread canon-era documents and found two the earlier scan had not: a second Kap 0 draft and a philosophischer Bericht. It also showed the stemmer turning „Mira“ into „miracle“ — six hits, none of them the name.

**Ten documents have a triage scan, and three of them are now read** (`Plan/runs/haiku-scan-2026-09-25/`,
chosen by qmd searches over the open records). A scan is not a reading. Its
verdict column says nothing either, since nine of ten said READ NEXT. Each scan
does name the records its document speaks to, with lines. The pages
`vortex`, `goedel-gambit`, `ouroboros-struktur`, `chaitin-konstante`,
`kishotenketsu`, `tsdp`, `thermodynamischer-phaenomenalismus`, `komponente-734`
and `vermittler-stimme` already quote these ten documents. Reading one of them in
full, by `ingest`, would give it the census and reconciliation it lacks — as document
21, `kap0-kap40-doppelklammer-abhandlung-2026-05-08-md`, and document 23,
`kap0-v1-annotiert-md`, now have. The four readings the scan had written from the first
needed no correction; of the six it wrote from the second, one sentence was false — that
the annotated draft came before any Kap 40 — and is corrected on `genesis-klammer`.

Run `python3 scripts/selftests.py` first; it builds nothing and says in one line
per suite what holds. In a fresh container the DSPy suites report `not run`
with the command that creates `.venv-dspy`.

**The tool review has run** (`Plan/concept/tool-review_2026-09-24.md`). The four
Hyper-Extract templates it could not run, because `he parse` cannot load a template
from a path, now load: `python3 scripts/templates.py parse` is `he parse` with that
one lookup extended, and `templates.py check` has a `resolve` check that fails when
it would not (2026-09-30). Measured offline against a local stand-in for the model,
all four parse, save, and answer `he search`; none has run on a document, which
waits on a model under decision 007. Its question 2 — patch the fork or copy the
templates into the installed package — needed neither. The three `route.py` defects it found are fixed, and what
was worth porting from the tools is decided — the review's closing section.

In order, and none of it needs a model:

1. **More retrieval cases.** `graphrag.py bench` has
   24 <!--state:graphrag.cases--> cases, all written by the hand that wrote the
   pages. The `## Open` sections (`relations.py --open`) are a second source;
   write `(question, gold pages)` by hand first. `Plan/concept/graphrag_2026-09-23.md`
   has why and the next four steps after it.
2. **The evidence into the pair input.** The plural rule is on the ledger
   (decision 010); what it leaves was decided from passages the program is not
   shown (above). Each judgement's `action` names its lines, and `read.py`
   serves them — as input, never as a label.
3. **qmd as a second seed source for `graphrag.py`**, measured on the bench
   against folded seeding — the floor row is already in `Plan/runs/baselines.jsonl`.
4. **Record routing failures** — each time an agent loaded the wrong skill or
   none. Five to twenty of them are job 4's dataset; there are none, so it has
   not started.
5. **English retrieval cases, to measure the glosses.** `graphrag.py ask --gloss`
   routes `Core Worlds` to `kern-welten` through a gloss the corpus writes, and
   the bench cannot see it — every case names a German term. The four questions
   asked in English, by hand, are the cheapest honest test.
6. **The entity layer grows with the entity lists, not by itself.** Only lists
   that verify as readings feed `graph.proposals()`, and only one unread
   document has one. The full entity run (above, *Half-done*) is what makes
   `graphrag.py`'s unread-document routes worth having.
7. **The record audit for the documents it has not covered** (decision 012, rule
   3). It ran on documents 7–13. Documents 1–6 were reconciled before ingest
   step 6, and 14–15 after it; `.claude/workflows/record-audit.js` takes them as
   args. The rule for what enters a record is in
   `Plan/runs/record-audit-2026-09-24/README.md`.
8. **Every reconciliation ends with `reconcile.py --sweep-open` printing
   nothing** (decision 012, rule 2). Every read document is settled:
   131 <!--state:sweep.decided--> hits, 68 <!--state:sweep.readings--> of them
   readings, in `Plan/runs/sweep.jsonl`.

Two things the build found, fixed in place:

- `Plan/trainsets/surface-pairs.jsonl` had gone stale — 17 rows against a
  ledger that had grown. Re-exported then; it has drifted again since (below),
  and `pairs.py` reads the ledger live, never the export.
- `graph.py`'s first pairing of quotations to citations disagreed with
  `quotes.py` (14 unresolved against 4). The pairing moved into
  `quotes.pairs` / `quotes.verdict` and both use it; `quotes.py`'s own numbers
  did not change.

## Gold for learnings — 2026-09-30, PR #131

The author: „Extract more Gold for learnings“, then „Maybe we need to extend the Gold List with
additional Relation types like the ones defined in the hyperextract contracts“ and „Lets improve our
evaluations“. `Plan/runs/gold-2026-09-30/README.md` has all of it.
- **Six new gold candidate lists.** This is steps 1–3 only: no census, note or reconciliation, so
  step 6's pause on full readings stands and `account.py order` is untouched.
- **`scripts/goldeval.py`** scores every extractor (the HyperExtract contracts, entity lists, blind
  re-readings) against every gold list.
- **`scripts/goldrel.py`** holds gold relations in the contracts' own types. It was piloted on three
  documents and scores TermDefinitions, TermContrasts and CausalLinks.
- **Open:** a second blind relation reader on the same three documents, to measure the ceiling a
  relation score must be read against. Only after that, more documents.

## The new tools as second readers — document 14, 2026-09-24

The author's instruction for this session was „nutze die neuen Tools". Of the
tools installed on 2026-09-24, two could be used on a new document without asking
anew: **graphify** and **knowledge-graph-extract** are driven by the agent itself,
so with Claude as the model no corpus text goes to a third party (decision 007
covers only documents 5 and 6 for the rest). Both, and the Haiku entity list,
read document 14 **after** its candidate list was committed, as second readers.
`Plan/runs/koharenz-protokoll-strukturierter-outline-2026-05-18-md/second-readers/README.md` has everything; the short of it:

- **knowledge-graph-extract reached a result** where the tool review's free models
  could not: 174 entities, 200 triplets, F1 **0.37** against the reader's list
  (precision 0.80), the best of the three. graphify 0.24, the entity list 0.19 —
  low recall by construction against a 572-entry list.
- **graphify's AMBIGUOUS edges found four of the document's inner tensions on its
  own**, and its reader three the census had missed (now in the census, checked
  and attributed).
- **Speed** (the author asked): 35 minutes was one agent on one chunk, not token
  volume. Four Haiku readers in parallel took 91 seconds for the same tokens and
  kept the rules worse (F1 0.16–0.21); a template parser got every chapter's
  fields with lines in 6 ms. The session model in parallel blocks is unmeasured.
- Nothing any of them produced entered a page, link, count or judgement.

## The `dspy` skill — landed, and what checking it against the code left open

**DSPy itself was read on 2026-09-24/25**: nine readers over the installed 3.3.1
package, its tests and docs, GEPA 0.1.4 and the papers
(`Plan/concept/dspy-source_2026-09-24/`). Three claims of the skill were wrong and
are corrected with probes; `lmrun.call` re-raised an unparseable answer that DSPy's
JSON fallback lets escape, and records it now. The folder's `README.md` lists what
they found that nothing here acts on yet — start there before changing anything
that imports `dspy` or `gepa`.

`.agents/skills/dspy` (netzkontrast/kohaerenzprotokoll#60) holds what the nine
DSPy repositories contain, re-read in full on 2026-09-24 and sorted by the job
at hand; `scripts/check_dspy_skill.py` holds it to the installed DSPy 3.3.1.
Building it fixed, in place: `lmrun.call` re-raised DSPy 3.3's own
`LMTransportError` instead of recording `unreachable`; `rlm_ingest.py` could
call an answer DSPy forced out of an exhausted REPL a reading; `graphrag.py`'s λ
comment compared two opposite conventions; `trainset.py`, `pairs.py` and
`check_dspy_surface.py` stated numbers two ledgers old; and `install.sh` built
`.venv-dspy` without the numpy and Deno extras. Every quotation in the skill
was checked once against its source, and each whose words were not the
source's was corrected; that check is not a standing one, because the nine
clones it reads are not in a fresh container. Open, none of it needing a
model:

- **`rlm_ingest.py` has no offline run of its RLM loop.** Its selftest covers
  the tools and the reach. `dspy[deno]` now installs the sandbox, and
  `check_dspy_skill.py`'s `rlm-runs-offline` probe is the shape one would take
  (P5).
- **Folds move as the ledger grows.** `folds()` deals round-robin over hash
  order, and one appended judgement moved 15 of 57 rows to another fold
  (measured). Whether a stable assignment is worth less balanced folds is open.
- **The export holds 36 rows.** Nothing reads `Plan/trainsets/surface-pairs.jsonl`;
  refreshing it by hand or demoting it is a construct question.
- **The DSPy surface has two encodings.** `check_dspy_surface.py`'s `USED` list
  and the skill's `surface` blocks both assert parameters by
  `inspect.signature` (P6).
- **The path check covers one skill.** Extending it to every skill needs a
  convention first: `ingest` and `tools` name `Wiki/contradictions/` and
  `Wiki/terms/`, which do not exist, on purpose.
- **Gold is decided by rule, and the rule rests on one untested assumption.**
  `scripts/gold.py` (decision 009) rules 65 <!--state:trainset.gold_candidate_lists-->
  candidate lists gold. On 2026-09-24, eight of them were written by the session
  that read the document, and none of those eight has a second reading of the
  same kind — document 14's three second readers were models asked for 50 to 200
  names or triplets, not an exhaustive list, so their F1 (best 0.37) does not
  test it. The
  assumption is that a session's reading disagrees with another reading no more
  than two readings did before (F1 0.66, P27). One second, independent reading
  of a document from 7 to 14 would test it. The lists of documents 5 and 6 have
  been scored against by the tool review (best F1 0.16), and document 14's by its
  second readers.

## Half-done — the entity lists

`scripts/entities.py` works; the lists it searches exist for five documents.
5 <!--state:entities.lists--> lists exist and 4 <!--state:entities.readings-->
pass verification — 395 <!--state:entities.rows_verified--> of
395 <!--state:entities.rows--> rows cite a line holding the entity.

**Revision 3 made the rule structural, and it held.** The reader returns names
only, into `Plan/entities/names/<slug>.json`; `entities.py place` writes every
line and refuses a name the document does not contain word for word. Re-piloted
on the same four slugs, 2026-09-23:

| list | rows placed | names refused | | F1 (rev 2 → 3) |
|---|--:|--:|---|--:|
| `aegis-subplots-kapitelweise-system-exploration-docx` | 70 | 14 | reading | 0.28 → 0.25 |
| `kohaerenz-protokoll` | 82 | 13 | **one line unread** | — |
| `ki-agenten-kohaerenz-und-prompt-generierung` | 68 | 22 | reading | — |
| `roman-lokalitaeten-konzept-und-ausarbeitung` | 97 | 0 | reading | 0.67 → 0.69 |
| `koharenz-protokoll-strukturierter-outline-2026-05-18-md` (2026-09-24, document 14) | 78 | 2 | reading | — → 0.19 |

- **Document 14's list was made after its reader's list was committed**, with the
  workflow's prompt verbatim, as a second reader. Of its two refusals one is a
  translation (`Landauer warmth`) and one is a term **the document does not
  contain at all**, `Persistenzgleichung` — named from outside the document, and
  stopped by `place`. Its reader reported 98 entities; the file holds 80. F1 0.19
  against a reader's list of 572 is a recall of 0.11 by construction; its
  precision is 0.81.
- **Every row verifies because no row was typed.** The refusals are the forms
  revision 2 would have written anyway: `McLaughlin-Graph` where the text has
  `McLaughlin-Graphen`, `Nicht-Lokalität`, `Koherentz Lücke`. They are listed in
  each file's `refused:` line rather than lost.
- **`kohaerenz-protokoll` is not a reading by one line.** Its reader reported
  `read_to_line` 2497 of 2498. `verify` treats any stated gap as disqualifying,
  and that rule was left alone: whether a one-line gap should demote a list is a
  decision, not a fix. Also: `read_to_line` is still the reader's claim. `place`
  prints the furthest line any name landed on beside it, which is code's — but a
  lower bound only, since a name is placed at its first occurrence.
- **Revision 3 found a defect in the checker, not only in the reader.**
  `quotes.normalise` drops a one- or two-digit number glued to a word (footnote
  debris), so on the line `(KW2),` became `(KW),` while the name stayed `KW2` —
  a name ending in a digit could never verify. Revision 2's gazetteer lost
  `KW2`–`KW4`, `Kern-Welt 1`–`4` and `Silent Hill 2` to it and blamed the reader.
  `entities.py` now asks one question for placing and verifying, `holds()`:
  whole word, one line, the normalisation minus the footnote rule. It is
  stricter than revision 2's substring test (`Kontakt` no longer passes on
  `Kontaktaufnahme`), and `selftest` carries seven cases that prove it can fail.
  Quotations are untouched: there the footnote rule is symmetric.
- The four readers cost 423,531 subagent tokens and about 75 s wall-clock, run
  in parallel as four Haiku agents with the workflow's prompt verbatim, not
  through the Workflow tool.

**Jev was tested on the same two documents, and it lost on quality.**
`scripts/jev_entities.py` takes candidates from a script (every capitalised
token, compound and bold/code/table-cell span, with its first file line) and asks
Jev one Noul per candidate over the 40-line window it first occurs in. Recorded
in `Plan/runs/jev/<slug>/`; `--replay` reruns it with no key.

| | gazetteer F1 | `aegis-subplots` F1 | lines right | time / doc | input tokens / doc |
|---|--:|--:|--:|--:|--:|
| Haiku, revision 1/2 | 0.67 | 0.28 | 85–95% | ~2 min | ~110k |
| Jev, top 100 by p | 0.47 | 0.10 | 99% — by code | 6 s | ~410k |
| every script candidate | 0.09 | 0.04 | — | — | — |

- **Faster by about 20×, cheaper by about 4× in money, not in tokens.** Jev is
  $0.042 per million input tokens and output is free (OpenRouter, 2026-09-23);
  Haiku is $1/$5. The whole corpus, 110,796 lines, is roughly $3 with Jev.
  The token count is high because each of ~2,100 questions per document repeats
  its wording; the state is paid once per window.
- **The candidate script caps recall at 0.80 and 0.63.** It misses multi-word
  names with a space in them (`Externe Ebene`, `Kern-Welt 1`) and splits none of
  the slashed forms (`Juna/V`). That ceiling is code's, and fixable.
- **Jev says yes to 20% of candidates** and ranks cited authors highest
  (`Sartre`, `Camus`, `Chinese_room` from footnote URLs) on `aegis-subplots`. It
  did what the question asked — the definition includes „a cited work or
  author" — which is the same open question the Haiku pilot raised, answered
  more sharply: the definition decides the list, not the model.
- Near-duplicates crowd the top 100 (`Neuromancer`, `Neuromancer (Roman, 1984)`);
  folding parentheticals is code, not judgement.

**What this means:** Jev is not a replacement for a reader here, but it is a
cheap filter behind a better candidate script. The gold lists are noisy too —
each carries a reader's notes as `- ` lines, which no list can match.

**Next, in this order:**

1. Decide whether a one-line stated gap disqualifies a list (above), or have the
   reader of `kohaerenz-protokoll` finish the line.
2. The other landed documents. Four readers cost about 424k subagent tokens; at
   that rate 342 more documents are roughly 36M, scaled by length rather than
   count. Say what the full run costs before starting it, and ask.
3. Then `entities.py matrix`, `missing`, and `doc` on the candidates for the next
   document below.

**Open question the pilot raised:** on `aegis-subplots` the model took the
research vocabulary where the reader took the world (F1 0.13, against 0.67 on the
gazetteer). Which of the two a corpus-wide entity list should hold is the
author's call, and the prompt's definition of an entity is where it would be
written. `Plan/concept/entity-lists_2026-09-23.md` has the argument.

## German and English names — mapped, not merged

`scripts/bilingual.py` maps the German and English surfaces of one entity across
the whole corpus. `Plan/entities/bilingual.md` holds the pairs and
`Plan/entities/bilingual.jsonl` holds every judged entity with its counterparts.

- **stated**: code found 12,526 glosses the corpus writes itself, `A (B)` and `A/B`,
  8,129 of them with at least one side an entity.
- **entities**: Jev accepted 6,989 of 18,026 surfaces as entities or key terms.
  The spot check was sound: `Wächter` 0.83, `Guardian` 0.93, `Ziel` 0.17, `Die` 0.11.
  One article got through, `Das` at 0.73, and the write stage now drops bare articles.
- **propose**: four free models, given names only, proposed counterparts.
  2,312 entities have one the corpus contains, and 34 names were never answered.
- **pairs**: Jev chose one relation for each of the 11,277 pairs:
  3,785 translation (2,474 at p ≥ 0.8), 989 abbreviation, 250 variant,
  2,465 role or part, 3,783 distinct.
- **Cost**: 1,015 Jev calls and 10.9M input tokens, about $0.46. Plus 99 free
  calls, which took 70 minutes, because only `nemotron-3-super` and
  `dots-3-note` answered a batch of 80 reliably.

**What needs a person.** The high tier reads right on the pairs the wiki cares
about: `Kernwelten`/`Core Worlds` in 8 documents, `Überwelt`/`Overworld` in 5,
`Risse`/`Rifts` in 3, `Handlungsfähigkeit`/`Agency`, `Erleben`/`Qualia` in 15.
Even there it holds naming relations Jev called translations: `Logik`/`LogOS` 0.85
is a guardian named for its domain. Below 0.8 the list is noisy, with
`Signposts`/`Transits` 0.63. No pair has entered `judgements.jsonl`. Reviewing the
high tier into it is the next step, and it is a person's.

## Question pages Q6–Q9 — 2026-09-29

On the author's „Read the Wiki and Create new questions in the Wiki“, four questions
that two or more term pages raise, or that the sources name as open themselves, were
promoted to `Wiki/questions/`. Each gathers quotations the term pages already hold; no
document was read, and none was started (the author's word of 2026-09-28 stands).

- **Q6** — the Nexus, the Überraum and the Überwelt: one space, one in another, or three
  (J18, J36, J63, J103). The 2025 Guardians take a form in the Nexus, the worldbuilding
  concept's reside in the Überwelt, the philosophischer Bericht's in KW3 `Überwelt / Nexus`.
- **Q7** — what 734 names: the component, the dwelling, both on purpose (J80).
- **Q8** — AEGIS after the Vortex's fifth beat, and Oblivion taking over its function
  (Appendix C.1 and C.5, OQ-A, OQ-G, as the sources cite them).
- **Q9** — the Moonshine-Link's boundary: what crosses, who feels it, whose it is
  (Appendix C.2, OQ-B, OQ-F).

**What they point at, if reading resumes.** Q8 and Q9 both send the reader to
`kohaerenz-protokoll-struktur-kanon-reset-2026-04-30-md` (792 lines, landed, unread),
whose Appendix C has eight headings, C.1–C.8 (orientation only). Q6 points at
`roman-blueprint-seelen-kohaerenz-protokoll` (2025-04-17; `Überraum` 17, `Nexus` 41 by a
whole-word count) and Q7 at `romanplot-uberarbeitung-kohaerenz-protokoll-teil-1`
(2025-04-18; `Einheit 734` 18). A suggestion, not a start: the author decides when
reading resumes.

**Measured.** `graphrag.py bench` went from 20 cases to 24; the twenty scored as before,
and the four new ones score high because each question names the pages that raise it
(`CLAUDE.md`, *The knowledge graph*).

## Next document — none: the author asked that no new document be started (2026-09-28)

**„Dont start any new documents"** — the author, 2026-09-28, while document 51 was already being read. It
was finished and nothing after it was begun. `chapter_sources.py across` has not been run again, and no next
document is named here. The next session starts from the author's word, not from a reading suggestion.

**Document 51 is done, 2026-09-28**: `an-inquiry-into-the-unresolved-questions-and-thematic-tensio`, the
Inquiry file, about fourteen English reports of 2025, the last of the 2026-09-25 scans. `reconcile-52` is the
record. **No page**; J119 (Dr. Aris Thorne on `lex`), J120 (the English world names on the paged worlds);
readings on 42 pages and `plot.md`; entries in C1, C3, C6, C9, C12, C13, C15 and Q1, Q3, Q5. Retrieval 0.660 →
0.654, only C4. Four Sonnet readers, split by page group; `account.py order` holds again.
- **The file disagrees with itself about the cast**: eight alters with Praetor and Oblivion in four reports,
  eleven with Alex, Lia, Isabelle, Moros and Argus in two, each set calling itself canonical; the last report
  names its sources for the split (Q3). Nyx is „Her" in one report and „his" in the rest. KW4 is the Garden of
  Possibilities in one table and of Potential in another.
- **Readers kept writing comparisons with documents they had not quoted** even with the rule in the brief — „no
  other read source has it", „a year earlier than the 2026 sources", „the only name common to every roster"
  (false: five names stand in both rosters). The session removed each before committing. The rule in a brief
  is not enough; a check that flags „only / no other / first / every other" in a new reading would be.
- **Noticed, no record holds it:** the Inquiry asks what became of the other fragments of AEGIS'
  self-mutilation (L78, on `genesis`); the Assessment's partitioning isolates Juna's resonance from Kael rather
  than splitting AEGIS' Ursprungs-Ich (on `trennungsprotokoll`).

## Postponed, and safe to postpone because the record proves it

**`orte-konzept-fuer-kohaerenz-protokoll` was reconciled twice and both are
stale.** Each recorded `state_before: 46`; the chain now ends at 56, so both must
be redone against the current wiki. The work is not lost — the censuses, notes
and candidate lists in the two worktree branches stand, and only the
reconciliation depends on the state that moved.

Nothing has to remember this: `Plan/runs/<slug>/reconcile.json` holds
`state_before` → `state_after` for every document and `account.py order` compares
them. **Done is a measurement here, not a tick**, which is what makes postponing
a task safe rather than a promise.

That case is also what `Plan/concept/task-queue_2026-09-17.md` is for. Merging
document 6 invalidated those two reconciliations, left ten pages unlinked and
moved the `fold()` baseline from 65% to 58% — three consequences of one
intended change, none of them written down by anyone. The concept's whole
premise is that a task is derived from measured state, so it cannot be forgotten
and cannot go stale in a list.

## Known failing

**`account.py order` holds again.** It was red from the 2026-09-25 scan, whose eleven
pages were written outside a reconciliation, until document 21 started from the 105
pages they left and recorded 106.

**The qmd coverage check reads collection patterns.** The previous version
treated a collection rooted at `.` as covering all descendants, even when its
pattern excluded them. It now checks `.qmd/index.yml`'s path and glob for each
collection, with an offline test that exposes this exact defect. Tool and agent
instructions under `scripts/`, `.agents/skills/` and `.claude/skills/` are
explicit exclusions: qmd searches the novel corpus and process records, while
those files are read directly when working on code. The check needs no qmd
binary; it checks configured coverage, not the contents of an installed index.

**Citation resolution is complete:** 0 <!--state:quotes.unresolved-->
quotations fail `scripts/quotes.py`, and 0 <!--state:quotes.unchecked-->
research-source quotations lack a resolvable citation. The checker audits
research-source wording; an author's recorded decision links to its decision
record and is not treated as a quotation from a research document.

## Landed

**The rest of the manifest, 2026-09-26, on the author's „Download all of the Rest
from the Manifest".** `sources.py fetch --include-md --limit 1000` landed the 241
remaining routable rows in about four minutes, none failing, no model reading any:
227 pre-May-2026 `plot-outline` gdocs, 13 `md`, one `pdf`. `dedupe.py --apply`
folded 26 copies among them (20 groups, `Plan/runs/dedupe.json`), so 215 new
documents stand, and `duplicates.py` reports 0 near-copies again. `dedupe.py` now
never folds a document something cites. It also appends its decision instead of
writing over the last one, which is how the first run's 31 groups were lost.
`qmd update` indexed the new files; embeddings were not built.
**`Sources/README.md` now ends with every document and its most important names**,
written by `scripts/overview.py` after a qmd first scan (*Sources at a glance* in
`CLAUDE.md`). **None of the 215 is read.** The plot outlines were deferred with
the novel, and landing them decides nothing about reading them.

**The canon-era documents, 2026-09-24, on the author's yes.** `sources.py fetch
--since 2026-05-01 --include-md` landed the 29 remaining rows dated May 2026 or
later, none failing. 26 were `md`, which `fetch` skipped before: the two new flags
are opt-in, and `md` takes the same text route that landed the four `md` rows on
2026-09-16. `dedupe.py --apply` then folded four copies — three `-2` exports two
bytes apart, and `25-wegkreuzung-md`, the chapter-25 text of `kp-kap25-2026-09-14-md`
in another escaping — so 37 canon-era rows became 33, all landed. **Eighteen are read**, documents 7 to 24; the first eight were
`kohaerenz-protokoll-storyform-und-outline-2026-06-10-md`, `kohaerenz-protokoll-charakter-bibel-2026-05-08-md`,
`koharenz-protokoll-konzept-konsolidiert-2026-05-08-md`, `kapitel-kompendium-gather-2026-05-31-md`, `kohaerenz-protokoll-kernwelten-vollstaendig-2026-06-10-md`, `dramatica-dual-storyform-status-2026-05-07-md`,
`kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md` and `koharenz-protokoll-strukturierter-outline-2026-05-18-md`, as documents 7 to 14 — see *Next document* for the rest.
(This line said „Five are read" over a list of seven until 2026-09-24.) The copy under `Legacy/Canon/` (six of the 2026-06-10
documents) has not been compared against the landed files.

Pull request netzkontrast/kohaerenzprotokoll#52 merged on 2026-09-23: the TypeSafe
SDK and project skill (`.agents/skills/typesafe`), the Jev concept, the vendored
`jev*` skills, `scripts/entities.py`, the entity pilot and the saved workflow.
Nothing from it is in flight; what it left open is under the headings above.

## Not open

Drafting the novel, until the author has answered the plan's four questions (*Writing the
novel — a plan*, above). The `Legacy/` shelf. Reading the 215 plot outlines landed on
2026-09-26: they are on disk and searchable, and still deferred with the novel
as reading material. The one `mp3` is a question above, not a backlog.

## PR #126 CI repair — 2026-09-30

The four Haiku lab extractions (R2–R5) are preserved under
`Plan/runs/reader-lab-2026-09-30/staged/Sources/{terms,notes}/`. They have not
been reconciled and are excluded from production ingest counts. Resume from
these staged artifacts when completing their reconciliation; no wiki reading
or reconciliation was fabricated to make the order check pass.

**Resumed the same day, and done.** A pair goes back to `Sources/{terms,notes}/` in the commit that carries
its reconciliation record, and not before. All four are reconciled and back: R4, `angst-bei-komplexen-traumafolgen`
(`Wiki/compare/reconcile-58-…`, no page and no reading, because no page speaks to a clinical review), then R2, R3 and R5
(`reconcile-56-…`, `-57-…`, `-59-…`: 48 readings by one Sonnet reader, 9 more and 5 record entries by the reconciler,
every page its own commit). The order holds at 58 documents; `staged/` is gone, and the claims selftest reads `Sources/` again.

## PR #126 review fixes — 2026-09-30

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
   (3) who labels — every contract's precision rests on one reader's labels; (4) the finders' defaults in `ask.py` — `he-lines` at 40 lines (+0.029 document recall, off) and the co-mention finder's 10 paragraphs;
   (5) 40 pages the corpus holds together and the wiki does not link (`Plan/runs/graph-lab-2026-09-30/e2c-links.md`) — any wanted; (6) whether the wiki holds the writing engine's vocabulary (the Narrative Context Protocol is written in 37 documents, the Collapse Susceptibility Index in 7).
3. **`Coherence Protocol.mp3`**, the one row not landed: markitdown can only transcribe it by sending the audio to a third-party speech service. A yes, and a service the author is content with, lands it.
4. **Entity lists and translation pairs for the 215 plot outlines landed on 2026-09-26.** `entity-lists` sends text to Haiku and `bilingual.py` to free OpenRouter models and Jev, so both wait on a yes; until then a name that occurs only in those documents has no entry in `Sources/README.md`.
5. **Process decisions** (context in `Plan/questions-for-the-author.md`, Part 2): whether DSPy runs on Claude through `claude -p` stand (decision 011) and whether SIMBA (about $8) runs; whether `fold()` adopts the plural rule of decision 010;
   the rule for a reviewed page that a new source contradicts (needed before the first promotion); chapter-level differences as conflict records, chapters in the graph and the app, and when the app is rebuilt;
   `GOAL.md` against the working agreement; whether the new tools read every document as second readers; which session reads which document when several run.
6. **An independent gold for the retrieval bench** (`Plan/concept/evaluation-audit_2026-09-30.md` §3). The bench's gold is 92 % lines the pages already quote and no unread document can score, so it tests the wiki's own graph, not discovery. What only you can give: grades on about 60 lines (to calibrate a judge), and, if you will, 20–30 questions with the lines you would point to; and a yes to a small first-party Claude spend (a few dollars) for pooled judging.
7. **The novel's open content questions** — where the sources disagree (conflict records C1–C15, question pages Q1–Q9) and what no source settles — are in `Plan/questions-for-the-author.md`, Part 1.

## Half-done — where the next session starts

- **Step 6 of the pipeline plan (decision 015) is paused by the author.** Its sample is the two newest unread documents in each of six categories; seven of the twelve are read and reconciled. **Five are unread**:
  `textanalyse-existenz-system-und-leid`, `kohaerenz-protokoll-hard-sf-horror-thriller`, `hard-sci-fi-cosmic-horror-research-questions`, `ki-assistent-romanwelt-kohaerenz-und-aegis-spec`, `aegis-persona-and-manifest-generation`.
  When the author says go: one reader at a time, marked by model (the lab's clean reader, `claude -p` with no tools, cost about 9 thousand tokens a call against a subagent's 67 thousand — `Plan/runs/reader-lab-2026-09-30/`),
  each document reconciled as it lands so that `account.py order`, which CI runs, stays green, and **claim before reading**: an open pull request naming the slug under a `Claim` heading (two sessions once followed one handover and read documents 16, 17 and 20 twice).
- **The HyperExtract work is measured and nothing is adopted.** 32 contracts (`Plan/hyperextract/`), staged by `he_claude.py` and loaded by `hegraph.py` as `P_HE_*` proposal edges, never into the core graph; `he-lines` and the co-mention relation are off.
  The backfill over the read documents stopped after 14 of 137 runs because five more gold documents moved `he-lines` by nothing (decision 019). To resume it, only with the author's word: delete `Plan/runs/hyperextract-backfill-2026-09-30/STOP`; `backfill.py status` names the rest.
- **Entity lists**: `scripts/entities.py` works, lists exist for five documents (`python3 scripts/state.py --get entities.lists`), and the full run over the landed documents has not happened — it waits on the yes above.
- **The branch** `claude/elegant-ramanujan-onfl2w` carries the session's work, and the author merges its pull requests while a session runs. After a merge: `git merge origin/main` into the branch (never a rebase, never `checkout -B`), then open a new pull request.
- **Every check runs on GitHub** (`.github/workflows/checks.yml`) on every pull request and every push to `main`; a pull request with a merge conflict is not checked at all.

**Known failing:** nothing is known to be. A red check names itself; `python3 scripts/selftests.py` runs them all.

## Where things are

- `CLAUDE.md` the working agreement; `PRINCIPLES.md` the rules we follow and the evidence for each; `GOAL.md` the author's brief, which describes the target, not the repository.
- `Plan/decisions/` one file per decision; `Plan/concept/` notes and proposals; `Plan/runs/` what every run kept; `Plan/learnings/` what each step taught; `Plan/weichen/` the decision sheets for the novel.
- The skills in `.agents/skills/` (the pipeline: `tools`, `ingest`, `reader-tools`, `graph-context`, `qmd`, `hyperextract-learning`); the graph: `Plan/concept/graph-contracts_2026-09-30.md`.
