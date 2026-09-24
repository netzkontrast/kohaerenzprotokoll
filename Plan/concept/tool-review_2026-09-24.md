# Tool review, 2026-09-24: what the main workflows could take from today's tests

*The review the author asked for. Built from the eight per-tool reviews in
`Plan/concept/tool-review_2026-09-24/`, Jev's check of every recommendation in
`Plan/runs/tooltest/check.json`, and `python3 scripts/route.py ledger`. Nothing
here has been adopted into the pipeline. This page proposes; the author decides.*

## What was tested, on what, at what cost

Eight tool groups were tested: `knowledge-graph-extract` + `semantica`, `grawiki`,
Hyper-Extract (`he`, `he-mcp`, the four templates in `Plan/hyperextract/`),
`graphify` + `cgr`, Jev as a judge, OpenCode + oh-my-openagent, the Notion
connector and its four skills, and `install.sh` with the session hook. Under
decision 007, the corpus text that went to a model came from two documents
only: `aegis-subplots-kapitelweise-system-exploration-docx` (document 5, 619
lines, reader list of 60 names) and `roman-lokalitaeten-konzept-und-ausarbeitung`
(document 6, 630 lines, reader list of 124). Every call went through
`scripts/route.py`.

**Cost: $0.000000 over 339 priced calls** (`route.py ledger`: 403 rows,
2026-09-24T18:31 to 19:23 UTC). Seven more calls answered but have no price:
Jev reports input tokens, not cost. Those are 4 `jev-judgements` calls with
46,182 tokens and 3 `tool-review-check` calls with 8,074 tokens, 54,256 in
total. The ledger says not to read "unpriced" as free, and neither does this
page. No call was refused and no call was charged.

| purpose | ok | cached | unreached | in tok | out tok |
|---|--:|--:|--:|--:|--:|
| `hyperextract` chat / embed | 241 / 28 | 24 / 0 | 0 | 76,619 | 113,405 |
| `grawiki` chat / embed | 20 / 14 | 29 / 0 | 0 | 34,146 | 68,621 |
| `opencode-omo` chat | 31 | 3 | 0 | 1,029,216 | 4,143 |
| `jev-judgements` | 4 | 0 | 0 | 46,182 | 0 |
| `tool-review-check` (Jev) | 3 | 0 | 0 | 8,074 | 0 |
| `kge` / `kge-probe` | 0 / 1 | 0 | 1 / 0 | 0 / 27 | 0 / 16 |
| `graphify` | 0 rows | | | | |

Two things in this table need saying. OpenCode used 1,029,216 input tokens on
a five-sentence question that involved no corpus text, which is about thirteen
times the input of the entire Hyper-Extract run, 76,619 (ledger). And `cohere/north-mini-code:free`
answered 296 of the chat calls, so in practice "the free pool" was mostly
one model.

**How to read the Jev score.** Every recommendation was given to Jev
(`check.json`, 24 of 24 answered, `jev-1.13.0`) with one question: *is the
proposal supported by the evidence it cites (measured facts from runs) rather
than by expectation?* The levels are 0 = not supported, 1 = partly
supported / rests on one run, 2 = supported. The score is the expected level.
It is shown beside each proposal and no proposal was dropped because of it.
It judges how well the evidence covers the claim, not whether the tool is
good.

---

## 0 · Check (invariants)

| proposal | evidence | tool | Jev | limit it must respect | verdict |
|---|---|---|--:|---|---|
| Keep the session hook running `install.sh` synchronously, and use `--check` as the pre-flight gate one layer below `account.py order` | `--check` finds 14 of 15 components ok, and the one missing, `qmd-models`, is missing by design. A forced `jev` reinstall took 1.795 s real against the script's own 2 s. `selftests.py` reports 18 held, 0 failed, 0 not run, in 59.08 s (`install.md`) | `install.sh` | 1.17 (partly .83) | it makes no claim about cold-container cost, which CLAUDE.md already flags as unmeasured | **adopt** (already running) |
| Time one real cold container start from beginning to end | the caches were warm, so no cold number could be taken (`install.md`) | `install.sh` | 0.53 (not .54) | it names a measurement and does not supply one | **trial** |
| Make `qmd-models`' `present()` check direct instead of shelling out to `setup_qmd.sh --check` | `--check` takes 8.438 s in total, and this component's share of that was never isolated | `install.sh` | 0.47 (not .54) | speculative until the component is timed on its own | **park** |
| After each `scripts/` change, run `graphify extract scripts --code-only` as a no-model architecture snapshot | 3.3 s. 781 nodes, 1685 edges, 24 communities. `subject.py` has 100 edges, which puts it in the top 10 files and backs CLAUDE.md's "substrate" claim in code (`graphify-cgr.md`) | `graphify` | 1.75 (supported .75) | 40 of the 1685 edges are INFERRED (`indirect_call` 26, `calls` 9, `uses` 5) even with no model. They are guesses, so they may not be used as fact, and the output never touches `Wiki/` or `Sources/` | **trial** |
| Run `cgr index` + `verify-index` on `scripts/` as a second, independently built cross-check | 14.7 s. 1315 nodes, 3464 relationships, and the sha256 manifest verified (`graphify-cgr.md`) | `cgr` | 1.59 (supported .61) | `cgr` cannot read markdown, so it only ever describes `scripts/` | **trial** |
| Add `cgr check` as another red/green invariant | none measured, only a reading of `cgr --help`. Memgraph was unreachable | `cgr` | **0.15** (not .86) | it may not replace any of the existing checks, all of which are stateless scripts | **park** |

The only item here that could join the invariant list now is the graphify
code-only snapshot. Following the tools skill's rule ("write no command for a
step that has not been done by hand twice"), it should be run by hand once
more after a `scripts/` change before it earns a line in the list.

## 1 · Choose

**Nothing tested today bears on this phase.** No tool was pointed at
`Wiki/questions/` or `Wiki/conflicts/`, and none ranked unread documents
against an open question. The one tool with a documented fit is Jev, whose
typesafe skill lists "choosing the next document" as a use. That was not
tested, and doing it would send corpus text beyond decision 007's two
documents. See *What is missing* below.

## 2 · Ingest

| proposal | evidence | tool | Jev | limit it must respect | verdict |
|---|---|---|--:|---|---|
| Use `knowledge-graph-extract` triples as candidate terms and relations for a person to read. Re-test it with no other testers running | extraction was never reached: 20 attempts were all rate-limited and took 510.3 s. A 27-token probe on the same path answered in 1.2 s. `validate_triples.py` and `generate_cypher.py` behave correctly on empty input (`kge-semantica.md`) | `knowledge-graph-extract` | 1.79 (supported .79) | may not create a page, a `[[link]]` or a count, merge surfaces, or detect a conflict. It is never the census and never `03-candidates.md` | **trial** (re-run first) |
| Do not use `grawiki`'s `GraphRAG.ingest_text` as a census | 3 of 3 ingests left 0 entity nodes. Every chunk failed with `InstructorRetryException` ("does not support multiple tool calls"), while 61, 61 and 53 structural nodes were written (`grawiki.md`) | `grawiki` | 1.99 (supported .99) | even once fixed, it is a model's reading | **park** |
| Once a file-path template can load, re-run `TermCensus` and score it with `entities.py score --names` | 8 of 8 `he parse -t <path>` calls failed at once with "Template not found" (`cli.py:331` resolves only gallery names). The built-in `general/set` template ran end to end: 259 items in 153 s at $0, F1 **0.16** (precision 0.11, recall 0.37; 209 names verified, 48 refused). Batch log: 67 of 126 chunk calls returned nothing (`hyperextract.md`) | Hyper-Extract | 1.04 (partly .65) | a second reader to score against a person's list after that list exists. It never seeds or replaces the list | **trial** |
| Keep the four project templates out of the loop until `he parse` can load them | same 8 of 8 failures. `templates.py check` stayed green because it only calls `validate` | Hyper-Extract | 1.98 (supported .99) | — | **park** |
| graphify document mode through the router | two attempts, neither answered, 0 ledger rows, document 6 never tried (`graphify-cgr.md`) | `graphify` | 1.27 (partly .51) | a model's reading | **park** |

**Scores against the two reader lists.** The two-reader ceiling is F1 0.66
(P27), and the Haiku entity list scored 0.25 on document 5
(`grawiki.md`, `hyperextract.md`). Measured today:

| source of names | doc | model names verified | shared | refused | P | R | F1 |
|---|---|--:|--:|--:|--:|--:|--:|
| Hyper-Extract `general/set` (stand-in, not `TermCensus`) | 5 | 209 | 22 | 48 | 0.11 | 0.37 | 0.16 |
| grawiki raw completion, attempt 0 | 5 | 7 | 5 | 1 | 0.71 | 0.08 | 0.15 |
| grawiki raw completion, attempt 1 | 5 | 8 | 3 | 3 | 0.38 | 0.05 | 0.09 |
| grawiki raw completion, attempt 0 | 6 | 19 | 1 | 2 | 0.05 | 0.01 | 0.01 |
| knowledge-graph-extract (no output reached) | 5 / 6 | 0 | 0 | 0 | 0 | 0 | 0 |

The grawiki names are one chunk each and were pulled from completions that
`grawiki` itself failed to parse, so they are not a score of `grawiki`. Every
extraction that ran scored below the Haiku floor. Nothing measured today is a
candidate for the ingest step.

**The part of phase 2 that did improve is the scoring harness.**
`entities.py score --names` now scores any names file. It refused
non-verbatim names (48 in one run) and gave an honest 0.00 on empty input. The
harness can be used now. No tool can.

## 3 · Reconcile

| proposal | evidence | tool | Jev | limit it must respect | verdict |
|---|---|---|--:|---|---|
| Before the `judgement` bucket, make one batched Score + Noul call per document and use it **only to order** the bucket | on the 26 recorded near matches from documents 5 and 6, Jev agreed with the person on 16 (0.615). On the `judgement` class itself it agreed on 2 of 5 (0.40). Two fresh attempts gave the same answer on 25 of 26 (0.962), and the one change, J20 `Wächter`/`Guardian`, sits on the 1.5 boundary. 8 of the 10 disagreements landed on the middle level. 46,182 tokens (`jev.md`) | Jev via `route.py jev` | 1.74 (supported .74) | may not decide a near match or be written as `mechanised_by`, because it is neither code nor deterministic. It creates no page, link, count or conflict, and runs only on consented documents | **trial** |
| Keep `score_location_registry.py` for the day a `LocationRegistry` output exists | it parses document 6's 51-row table from L185. That was checked by eye, not run against any output (`hyperextract.md`) | Hyper-Extract | 0.90 (partly .72) | scores nothing until the template runs | **trial** |
| Run semantica's `DuplicateDetector` / `ConflictDetector` offline, only to print a list for a person | a synthetic 3-entity test flagged `AEGIS`~`Aegis` (similarity 0.9, confidence 1.0) and found 0 conflicts. With no model output, 0 real entities were loaded (`kge-semantica.md`) | `semantica` | 1.41 (partly .55) | may not merge, write to `Wiki/conflicts/`, or gate a decision | **park** |

**The Jev trial only helps if the context grows.** Jev saw one line either
side of each surface and disagreed with the person where the person had
knowledge of the whole document. The retirement condition in `jev.md` still
holds: stop the trial if 20 more `judgement`-class rows stay under 50%
agreement.

## 4 · Re-measure

**Nothing new.** The one related measurement is `selftests.py` passing all 18
of its suites (`install.md`), which is the existing gate. The graphify and
`cgr` snapshots under phase 0 could be re-run here to show whether a change
moved the code graph. That is a code check, not a wiki measurement, and it
supplies no count to `state.py`.

## ask

| proposal | evidence | tool | Jev | limit it must respect | verdict |
|---|---|---|--:|---|---|
| `he info` / `he search` / `he-mcp` as a read layer | tested only on the `general/set` stand-in: index built in 7.4 s, search answered in 2.7 s with local embeddings. `info` reported `raw_items: 0` for a Knowledge Abstract holding 259 items, and that is unexplained (`hyperextract.md`) | Hyper-Extract | 1.58 (supported .58) | there is nothing in this project's shape to serve. `ask`/`talk` were not exercised | **park** |

`graphrag.py ask` stays the only retrieval, and it returns verified
quotations. No tool tested today writes an answer that meets the rule that
sources are never merged.

## promote

**Nothing tested today bears on this phase.** It is a person's gate, and no
tool claims to be one.

## Side tracks

**route (the router), where today's run found real defects:**

| proposal | evidence | Jev | limit it must respect | verdict |
|---|---|--:|---|---|
| Stop `scripts/route.py` shadowing the stdlib `profile` module. Its `sys.path.insert(0, ROOT/"scripts")` (L67) puts `scripts/profile.py` ahead of it, and that breaks `/v1/embeddings` through sentence-transformers → torch → `cProfile` | reproduced directly. `grawiki` got embeddings only through a wrapper that pre-imported the module (`grawiki.md`) | 1.93 (supported .94) | a code fix. It changes no consent or free-only rule | **trial**, and should be fixed |
| Give each model attempt a hard deadline so a broad `except Exception` in `_post` cannot absorb it | one `kge` call took 510.3 s against the tester's 45–70 s setting. `route.py`'s own default is `TIMEOUT = 180` (L75), and it tries each model twice (L316) (`kge-semantica.md`) | 1.77 (supported .77) | changes only how fast an "unreached" verdict arrives | **trial** |
| Write one ledger row per model attempt (or a progress line), not one per call | graphify ran for about 10 minutes with 0 ledger rows, because the ledger is written only once the call finishes (`graphify-cgr.md`, L293–360) | not in `check.json` (a finding, not a numbered recommendation) | — | **trial** |
| Treat a partly empty batch as a failure mode the ledger cannot see | in one batch, 67 of 126 Hyper-Extract chunk calls returned nothing while the ledger showed all `ok` (`hyperextract.md`) | not in `check.json` | — | noted |

**OpenCode + oh-my-openagent:**

| proposal | evidence | Jev | verdict |
|---|---|--:|---|
| Never run oh-my-openagent unsupervised against this repository; use `OPENCODE_PURE=1` only | with the plugin loaded, the agent ran `find /` and read a file outside its working directory with no prompt. Without the plugin, the same read was auto-rejected (`opencode-omo.md`) | 1.56 (supported .57) | **adopt** (one prompt's evidence) |
| OpenCode's `provider.route` block works as a front end to `route.py serve` | 34 of 34 calls went through the router at $0, and `-m route/free` held even under the plugin's own agent. The shingle guard was not exercised | 1.78 (supported .79) | **trial**, non-corpus tasks only |
| Keep OpenCode + omo out of every phase that touches `Sources/` or `Wiki/` | the plugin tried to reach a remote `grep_app` server by itself, and file reads were not gated | 1.21 (partly .77) | **park** |

**Notion:**

| proposal | evidence | Jev | verdict |
|---|---|--:|---|
| No repository artifact goes to Notion as a second original. If Notion is ever used, it gets only a mechanical one-way push of committed markdown | `search("Kohärenz")` returned 10 pages under one root. 9 are from 2026-03-26, and the page describes itself as not an archive or wiki (`notion.md`) | 1.31 (partly .62) | **park** |
| Decisions and questions stay in `Plan/decisions/` and `NOW.md`, not in `knowledge-capture` / `research-documentation` | both skills assume an API token and database IDs the project does not have, and their output would sit outside git and outside `state.py` | 0.96 (partly .56) | **park** |
| No trial of `meeting-intelligence` / `spec-to-implementation` | the project has no board and no meeting database | 0.57 (not .65) | **park** |

**search:**

| proposal | evidence | Jev | verdict |
|---|---|--:|---|
| FalkorDBLite as a second local graph and vector index beside qmd, once extraction fills it | the store started and served in all 3 runs, but it holds only document and chunk nodes (`grawiki.md`) | 0.87 (partly .81) | **trial** in the review, but there is nothing to query yet |

## Rejected: proposals that would break a limit

These are uses the tools offer or the reviews considered. Each is rejected
because a model's output may not supply a page, a link or a count, or because
conflict detection is never mechanised:

- **semantica's `ConflictDetector` in any step that writes to `Wiki/conflicts/`
  or gates reconciliation.** It mechanises conflict detection. P14: known-good
  classes would be reported forever.
- **semantica's `EntityMerger` or `GraphBuilder(merge_entities=True)` applied to
  project entities.** They merge surfaces (P13). The test only ran them on an
  empty set.
- **Jev's Score written into `judgements.jsonl` as `mechanised_by`, or deciding
  the `judgement` bucket.** It is not code and not deterministic (0.962 on
  repeat), and it agreed 0.40 of the time on that class.
- **Any model extraction (grawiki, Hyper-Extract `TermCensus`,
  knowledge-graph-extract, graphify) standing in for `03-candidates.md` or a
  census.** The candidate list is the one artifact a program cannot produce.
  A model list may only be scored against it.
- **Hyper-Extract `StatedRelations` or graphify INFERRED edges becoming
  `[[links]]` or graph edges.** A guessed edge cannot be told apart from a
  stated one once it is in the graph.
- **Using the entity or triple counts of any of these tools as a number on a
  page.** Every number comes from `corpus.py`, `duplicates.py` or a named count.

## What is missing: can anything tested close it?

**"Phase 1 is not automated."** **No.** No tool was run against the open
questions or conflicts. Knowledge-graph-extract and Hyper-Extract could at best
propose candidate terms from a document that has already been chosen. They
do not choose one, and neither reached output on project templates. A
reasonable next test is Jev ranking a short list of unread documents against
one open question, which is the typesafe skill's own suggestion. That needs
consent for every document it sees.

**"ask does not exist" (retrieval, but no answer).** **No.** `he-mcp` `ask`
was not exercised, FalkorDBLite holds no entities, and OpenCode was kept away
from the corpus. Turning quotations into prose would merge sources whichever
tool did it, so this is the author's call, as the skill says. Nothing
measured today changes that.

**"Extraction is not trainable: one usable gold list."** **No.** No tool adds
gold, and none can: gold is a person's list written while reading. Every model
score today (best F1 0.16) is below the Haiku floor of 0.25 and far below the
two-reader ceiling of 0.66. What today did add is the scorer: `entities.py
score --names` scores any tool's names against a reader list, so the moment a
tool produces output, it can be measured. One inconsistency surfaced along
the way. The skill says *one* usable gold list. Decision 007 says documents 5
and 6 both have a genuine reader's list, and the tests scored against both
(60 and 124 names). 13 `Plan/runs/*/03-candidates.md` exist, and
`Plan/runs/README.md` marks the first four as reconstructed. How many of the
other nine are usable gold was not measured here. The skill's statement
should be checked and corrected.

## Not reached (P15)

| what | why | what would reach it |
|---|---|---|
| knowledge-graph-extract, a full extraction of either document | a 619-line single chunk was killed after about 13 minutes. A 150-line retry came back "unreached" after 20 attempts, all rate-limited, because hyperextract (241 calls) and grawiki were using the same free rotation at the same time | run it alone, or with a wider free rotation |
| graphify document mode | two attempts, neither answered, 0 ledger rows. Document 6 was not attempted (time budget) | isolate the slow layer with `route.py complete` on a short excerpt, then retry graphify alone |
| Hyper-Extract `TermCensus`, `LocationRegistry`, `TermReadings`, `StatedRelations` | the CLI cannot load a template from a file path (`Template.get()`, `cli.py:331`). 8 of 8 failed with no model call | a file-path option upstream (the fork is `netzkontrast/Hyper-Extract`), or copying templates into the installed presets directory, which was not done because it edits a shared install |
| Hyper-Extract `ask`/`talk` | out of time budget | a run after a project template loads |
| `cgr check`/`stats`/`dead-code`/`duplicates`/`export` | no Memgraph on :7687. The docker CLI is present, but `/var/run/docker.sock` is absent | an environment with a running Docker daemon or a reachable Memgraph |
| install cold-container timing | the caches were already warm, and purging them was out of scope | time a fresh cloud environment from start to finish |
| Notion write tools | not called on purpose: read-only, no corpus text | — |
| OpenCode with corpus text | not sent on purpose, so the shingle guard is unexercised for OpenCode | — |

Answered, but unusable. This is not the same as "not reached": grawiki reached
the model on every call, and the model answered, but `instructor` failed to
parse every answer on the client side. The next thing to try, from
`grawiki.md`, is `kg_extractor_kwargs={"mode": instructor.Mode.JSON}`.
grawiki document 6 had only one attempt, so P18's second attempt is missing
there. The Hyper-Extract `general/set` run was also a single attempt.

## Questions for the author (P0)

Work continues without these answers, per the instruction of 2026-09-24.

1. **May documents 5 and 6 be sent again, once each tool is run alone?**
   Decision 007 says "any later use of these two" is to be asked again. The
   runs that would benefit are knowledge-graph-extract (rate-limited today),
   graphify document mode (unanswered), and grawiki with `instructor` in JSON
   mode. All would use free models and cost $0.
2. **Hyper-Extract templates: patch the fork, or copy the templates?** The
   `he parse -t <path>` limitation is in `netzkontrast/Hyper-Extract`. Should
   file-path loading be added there, or should `install.sh hyperextract` copy
   `Plan/hyperextract/*.yaml` into the installed presets directory, or should
   the templates wait?
3. **Jev as triage for the judgement bucket: widen the consent?** The trial
   is only useful on documents beyond 5 and 6, and each needs its own consent
   row. Should Jev also get more context per pair (more than one line either
   side), which sends more text?
4. **The Notion workspace "📖 Kohärenz Protokoll" (2026-03-26).** Is it
   retired, or does the author want the one-way, read-only mirror of `NOW.md`
   described in `notion.md`?
5. **oh-my-openagent on the author's own machine.** With the plugin loaded, it
   read a file outside its working directory without asking, and it contacts
   a remote `grep_app` server by itself. Does the author run it against this
   repository where it is signed in?
6. **A Docker daemon in the cloud environment?** It is needed only for `cgr
   check` and the other Memgraph-backed commands. The expected value is low
   (Jev 0.15 on that recommendation), so the question is whether it is worth
   an environment change at all.

## What was ported, 2026-09-24 — and what was not

The author asked for the tools worth it to be ported. Measured against this
page's own evidence and the tools skill's rule — *write no command for a step
that has not been done by hand twice* — one thing earned it.

| candidate | decision | why |
|---|---|---|
| `scripts/route.py`, the three defects above | **fixed** | every future model call goes through it. `profile` now loads from the standard library before `scripts/` is on the path — reproduced as a 501 before, 384-dimensional embeddings after; each attempt has a hard deadline and a call a total one of 600 s; every failed attempt writes its own ledger row, shown as `retries`. `selftest`: 29 cases hold, three new |
| `entities.py score --names` | **already in** | ported during the test; it reproduced the Haiku lists exactly |
| Jev ordering the `judgement` bucket | **not ported** | done by hand once, by the tester. Its only permitted input, documents 5 and 6, is already decided; a second instance needs a new document and a consent row (question 3 above). A command waits for that |
| graphify's code-only snapshot | **not ported** | run by hand a second time: 862 nodes and 1,848 edges, against 781 and 1,685 in the test — `scripts/` changed between. It describes; nothing in it can fail. The one rule it could hold, that no script reads `Legacy/` (P21), is a `grep` |
| `cgr`, semantica, grawiki, knowledge-graph-extract, Hyper-Extract, Notion, OpenCode | **not ported** | nothing usable measured — the sections above |

## Later the same day — two of the unreached, reached with Claude as the model

knowledge-graph-extract and graphify's document mode are **not reached** above
because the free-model router could not serve them. Both skills have the host
agent read, so with Claude as the model they need no router and send no text to a
third party. Run that way on document 14 — a new canon-era document, after its
reader's list was committed — both reached a result: knowledge-graph-extract
200 triplets, F1 0.37 against the reader's list (precision 0.80); graphify 674
edges, F1 0.24, with four of the document's inner tensions as AMBIGUOUS edges.
That changes this page's „not reached" for those two, and none of its other
verdicts. `Plan/runs/koharenz-protokoll-strukturierter-outline-2026-05-18-md/second-readers/README.md` has the measurements,
including what made the 35-minute run faster.
