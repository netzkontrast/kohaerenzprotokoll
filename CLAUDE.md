# Kohärenz Protokoll — working agreement

A German hard-SF novel and its research corpus. **The wiki is being built, and the first chapter is being drafted in `Manuscript/`** on the author's request (decision 023). A plan for writing the novel is proposed and not yet decided
(`Plan/concept/novel-writing-plan_2026-09-29.md`; its four questions for the author are in `NOW.md`).

**Canon prose is German and is never translated. Engineering and work language is English.**

## Read this first

1. **`NOW.md`** — what is open right now, the author's standing instructions, the questions that wait, what is half-done. It is the handover between sessions, and it is one page.
   If it names a next-session mandate, follow that mandate before selecting pipeline work; its linked briefing owns the task and its completion criteria.
2. **`PRINCIPLES.md`** — the rules we follow, each with the evidence that produced it, and a catalogue of ideas kept but not yet built. Read it before writing a new skill, command, script, check or page type.
3. **`SPEC.md`** — the architecture, adopted by the author (decision 021): modules and who owns what, the hit and pack contracts, the evaluation gates, and the migration order. Each step is marked *[built]* or *[migrate]*.
4. **`GOAL.md`** — the author's brief (2026-09-23, German): a git-versioned knowledge graph and wiki that helps write the novel — sources tiered by precedence, conflicts found and never silently
   smoothed, self-generated questions, the plot model as checkable rules. It describes the *target*, not the repository: where it names paths or tools that do not exist here, this page says what exists.

**Everything on this page describes what currently exists. A statement here that is not true of the repository is the defect — fix it in the same change, or delete it.** A description that outran what
existed is how the previous version of this project failed. The detail behind each section lives where it is maintained: a script's docstring is its documentation, `scripts/README.md` is the map of the
folder, and the skills in `.agents/skills/` hold the procedures (the table at the end of this page says which).

### A fresh container has none of the derived things

A cloud session starts from a clean clone, and everything git-ignored is absent. `.claude/hooks/session-start.sh` runs `python3 scripts/knowledge.py init --profile research` synchronously at every Claude
session start (Codex coordinators run it by `AGENTS.md`); it calls `scripts/install.sh --session` — `derived`, `tools`, `dspy`, `graphqlite`, `typesafe`, `qmd` — and builds or refreshes the graph
store, and it never blocks the session on a failed component. `scripts/install.sh --check` says what is present, `--list` names the components, `scripts/install.sh <name>` installs one; the log is `.install.log`.
A second run takes seconds; the first took about a minute with uv's cache warm.

| absent at start | rebuild | needed for |
|---|---|---|
| `Plan/derived/ask.db` | `python3 scripts/knowledge.py init --profile reader` (or `.venv-graphqlite/bin/python scripts/kg.py index`) | both graph CLIs; reads refuse a stale store |
| `Plan/derived/` | `install.sh derived` (`python3 scripts/derive.py`, about 3 s) | `corpus.py`'s index path |
| `.venv-tools`, `.venv-typesafe`, `.venv-dspy`, `.venv-dspytools`, `.venv-grawiki`, `.venv-semantica`, `.venv-mflow`, `.venv-graphqlite` | `install.sh <name>` | only the step that names each; `scripts/kg.py` needs `graphqlite` (pinned `graphqlite==0.8.0`) |
| `he`, `he-mcp` (upstream Hyper-Extract) | `install.sh hyperextract`, pinned to `395039e` — **not** at session start | `hx.py parity`, `templates.py parse`, the vendored `hyper*` design skills; a contract run uses the port, `scripts/hx.py` (decision 020) |
| `jev-decide`, `graphify`, `cgr`, OpenCode + oh-my-openagent | `install.sh jev` / `graphify` (pinned `4c73561`) / `cgr` / `omo` | the vendored skills; nothing in the pipeline |
| qmd package and the `/usr/local/bin/qmd` shim | `install.sh qmd` (`scripts/setup_qmd.sh --package`) | searching; nothing in the pipeline |
| qmd's models (~2.1 GB), index and embeddings | `install.sh qmd-models` (`scripts/setup_qmd.sh`) — **not** run at session start | vector search and `qmd query` |
| `OPENROUTER_API_KEY`, `TYPESAFE_API_KEY` | the environment's settings, never a file or the chat | a real Jev or OpenRouter call |
| `Plan/derived/ui/` | `python3 scripts/ui.py` | the project app's canvas files, to publish |
| `Plan/derived/web/` | `python3 scripts/web.py` (runs `ui.py`, about 90 s) | the project app as a website; Vercel builds it itself |
| `.venv-novelgraph`, `Index/sources/*/vec/`, `Index/sources/*/lex/`, `Index/_build/`, the embedder (~0.5 GB in the Hugging Face cache) | `UV_PROJECT_ENVIRONMENT=$PWD/.venv-novelgraph uv sync --project novelgraph`, then `.venv-novelgraph/bin/novelgraph build` (about 3 minutes from nothing) — not at session start | `novelgraph search`; `ask`'s `novelgraph` finder, which is off by default |

The standard-library scripts — `state.py`, `quotes.py`, `read.py`, `reconcile.py`, `account.py`, `entities.py`, `ui.py`, `hx.py`, `he_claude.py` — need none of these. **Every dependency goes into a virtualenv, never into the system
Python** (`pip install --break-system-packages` once broke `cryptography` for the whole container); `.agents/skills/tools/references/install.md` has every venv, vendored skill and third-party tool and how each is installed.

## Two layers, and the manuscript

| layer | what it is | who writes it |
|---|---|---|
| `Sources/` | research documents fetched from Drive, immutable once landed | `scripts/sources.py`, nothing else |
| `Wiki/` | term pages derived from those sources, promoted by a human | a person, for now |
| `Manuscript/` | the novel's workspace (decisions 023, 024): the canon ledger `kanon.md`, the drafts one folder per chapter, plot drafts in `plot/`, cards for cast and world in `figuren/` and `welt/` — only canon and working drafts, never a reading: nothing is canon unless `kanon.md` lists it, and nothing in `Wiki/` or `Sources/` reads it | the author, or a session on the author's explicit request, named in each draft's head |

`Manuscript/` is not a third research layer: it is what the two layers are for. The writing skills' findings about a draft go to `Plan/runs/writing/`, never into `Manuscript/`. Everything else the project used to have is parked under `Legacy/` and read by nothing. `Sources/manifest.jsonl` is the spine: each row has `drive_id`, `title`, `slug`, `category`,
`tier` and, once landed, `export_path` and two checksums. Anything derived traces back to a `drive_id`. `Sources/duplicates.jsonl` holds the rows that left it — Drive holds up to five exports of one document, and
`scripts/dedupe.py` folds the extra ones away — so that „not in the manifest" never has to mean „nobody knows" (`Plan/learnings/fetch.md` has which copy survives, and why it is not the longest).

## State — measured, never stored

**587 <!--state:sources.total--> rows in the manifest, 586 <!--state:sources.landed--> landed** — 586 <!--state:sources.distinct--> distinct documents, 93 <!--state:sources.folded--> duplicate exports folded away, 0 <!--state:sources.near_copies--> near-copies left
(`scripts/duplicates.py` keeps saying so). The one row not landed is `Coherence Protocol.mp3`: markitdown can only transcribe it by sending the audio to a third-party speech service, which waits on the author's yes.
All 33 <!--state:sources.canon_era--> rows dated May 2026 or later (the canon era) are landed (33 <!--state:sources.canon_era_landed-->) and read.

**72 <!--state:documents.with_census--> documents have a term census** in `Sources/terms/`, 72 <!--state:documents.with_note--> a note in `Sources/notes/`, 72 <!--state:documents.reconciled--> a reconciliation in `Wiki/compare/`.
`python3 scripts/account.py order` holds — `true` <!--state:order.holds--> — when every document with a census has a note and a reconciliation, each ran against the state the previous one left, and the wiki
matches what the newest run recorded leaving; when it does not, it says so with exit status 1. What each document added is in its reconciliation record `Wiki/compare/reconcile-NN-<slug>.md` and, up to document 51,
in `Plan/runs/reading-log.md`. `Plan/runs/judgements.jsonl` holds 121 <!--state:judgements.total--> judgements about near matches, 8 <!--state:judgements.mechanised--> mechanised and replaying green,
0 <!--state:judgements.disagree--> disagreeing.

**The wiki**: `Wiki/candidates/` holds 106 <!--state:wiki.pages--> term pages, `Wiki/conflicts/` 16 <!--state:wiki.conflicts-->, `Wiki/questions/` 9 <!--state:wiki.questions-->, `Wiki/chapters/`
41 <!--state:wiki.chapters--> chapter pages (Kap 0–40, 644 <!--state:chapters.readings--> readings, decision 013), and `Wiki/compare/` the reconciliation record per document. The schema follows the pages rather than
preceding them, so `Wiki/terms/` does not exist and nothing has been promoted. A term page collects every source's reading of one term, **attributed and unmerged**: where sources disagree the page says so and stops.
Which reading is right is the author's call, never the page's.

**Every number on this page carries a `<!--state:key-->` marker naming the measurement it came from, and `python3 scripts/state.py --prose` fails if any of them contradicts the repository.** It reads every markdown
file outside `Legacy/` and the vendored clones. That check exists because this section went stale four times — 27 of 680 landed, 3 documents read, 32 wiki pages, a reconciliation of 19/12/7 — each true when written, each wrong
within a day, each caught by a person rather than a command. **State is derived, never stored**: `scripts/state.py` measures the repository, `Plan/state.json` is the artifact of a run and not the source of truth, and a new
measurement is a decorated function.

```bash
python3 scripts/state.py            # derive everything, write Plan/state.json
python3 scripts/state.py --prose    # fail on any stale number in prose
python3 scripts/state.py --check    # fail if Plan/state.json has drifted
python3 scripts/state.py --get wiki.pages
```

## The process — one operation at several scales

    account(subject, question) -> account

| subject | the account |
|---|---|
| a document | the census, the note |
| a term | the page |
| two surfaces | one term or two — `Plan/runs/judgements.jsonl` |
| the corpus | a count, a plan, a timeline |

Each decomposes into the same operation on smaller subjects. One recursive operation needs one rule set and grows a library of decompositions in `scripts/rules/` — the part a project actually learns; a pipeline of
N steps needs N of everything. `scripts/account.py` is the verb and `scripts/subject.py` the substrate every script asks (the frontmatter boundary has one implementation). The steps as actually done, in
`Plan/concept/wiki-process_2026-09-16.md` and the `ingest` and `tools` skills:

```
Drive ──fetch──→ Sources/drive/*.md ──┬──extract──→ Sources/terms/*.md
                                      │                    │
                                      └──read─────→ Sources/notes/*.md
                                                           │
                                                      reconcile ──→ Wiki/compare/*.md
                                                           │
                                                        gather
                                                           ▼
                                                Wiki/candidates/*.md
                                                           │
                                                   review (a person)
                                                           ▼
                                                   Wiki/terms/*.md ──→ ask
```

- **A census lists the candidate terms of one document by a written rule** — what it names in the novel's world, the words it uses as its own terms, the borrowed concepts it applies (decision 012). **A note**
  harvests what that document says about the terms that matter, quoting with line numbers. **A census describes one document and nothing else**: no count, comparison or expectation from another source.
  `Plan/briefings/extract.md` is read before the document and carries **procedural** knowledge (what German Drive exports do), never **document** knowledge (what some other file said). The census is frozen before the
  wiki is consulted, so the accumulated state cannot decide in advance what a new document is allowed to say — that independence is what makes reconciliation safe.
- **Reconciliation never reads the wiki.** `scripts/wiki_index.py` derives `Wiki/index.json` from page frontmatter and `scripts/reconcile.py` answers by lookup, printing only what no lookup settles: cost per document
  is `O(census) + O(judgement)`, not `O(wiki)` (`Plan/concept/reconciliation-by-lookup_2026-09-17.md`). It also **sweeps the text for everything the wiki already knows** (decision 012): each page the text names without a
  matching candidate is decided as a reading, which goes on the page, or an occurrence (a title, a reference, another sense) — recorded in `Plan/runs/sweep.jsonl`: 188 <!--state:sweep.decided--> decided,
  105 <!--state:sweep.readings--> of them readings the lookup had missed, 0 <!--state:sweep.open--> open (`reconcile.py --sweep-open`).
- **A reference on a wiki page names its document.** A bare `^[Lnn]` resolves against the page's single `ingested:` entry and stops being checked when a second arrives — adding one document's readings to seventeen
  pages once moved 95 verified quotations into the unchecked bucket silently. A census and a note carry `source:` and may use the bare form; a page may not.
- **Conflict detection is never mechanised.** Two readings can only be compared by reading them, and a program that guessed would reproduce the `Zero-Trust` false conflict.
- **Every step keeps its artifact.** `Plan/runs/<slug>/` holds one directory per document: the profile, the probes, **the candidate list written while reading**, the counts, the verification runs and the timings.
  `scripts/capture.py` refuses to count before a candidate list exists, because counting first decides what gets seen. The candidate list is the one artifact a program cannot produce and the baseline anything automated
  is scored against; `scripts/gold.py` decides by rule which lists are gold (decision 009) — the first four documents' reconstructions are not. Every reader so far has been Claude; no reading by the author is recorded.
- **Learnings**: `Plan/learnings/` holds one file per step — what was learned, what the tool must handle, what stays judgement, real measurements. Write in them as you go.

## The rules that always hold

### A quotation is checked against its line

`python3 scripts/quotes.py` verifies that every „…" `^[Lnn]` in a census, note or wiki page still resolves to the line it cites — every cited quotation, however short, and every number a
quotation writes, in order. It says how many it could not check rather than counting them as passed. `python3 scripts/read.py <slug>` prints a document with every line prefixed by the file line a citation names;
`--find "<the words>"` answers with `^[Lnn]` or refuses, naming the nearest line, and both run the same comparison on the same normalised line — **ask for the citation, never type it**. `python3 scripts/selftest.py`
proves the checkers can fail (each case carries the exact defect it must name), and `python3 scripts/selftests.py` runs every self-test in the repository, one line per suite: `held`, `FAILED`, or `not run` — which is not a pass.
**GitHub runs the checks on every push to `main` and every pull request** (`.github/workflows/checks.yml`), one step each: prose numbers, pipeline order, quotations, frontmatter, the judgement replay, chapter pages, the Sources
overview, and `selftests.py --only std`. The venv suites (dspy, typesafe, GraphQLite, Hyper-Extract) run in a session, not on GitHub; a pull request with a merge conflict is not checked at all.

### The wiki links, and a link is not a mention

`` `Nexus` `` names the term, `[[nexus]]` points at the page, `[[nexus|Nexus-Vorstufe]]` points at it leaving the prose as it read (decision 005). `scripts/relations.py` derives the graph from `[[…]]`
and nothing else and reports a link pointing at no page; `scripts/link.py [--apply]` marks the mentions the prose already makes — a page links a term once, and **a link is never inferred**. There are 681 <!--state:wiki.relations--> links
across the 106 <!--state:wiki.pages--> pages, 19 <!--state:wiki.orphans--> of them with nothing pointing in, and 561 <!--state:wiki.unmarked--> mentions left unmarked because every one sits inside a quotation, a citation line or a
heading. Run `link.py` after any reconciliation that created pages.

### A mechanised rule stays checkable

Every decision about a near match is in `Plan/runs/judgements.jsonl` with the two surfaces, the decision, the rule, and whether code now claims it; `python3 scripts/judgements.py` replays them
all against the current code (`agrees`, `DISAGREES` — go and look, `judgement` — still a person's call). Run it after touching `fold()` or any matching rule. **A green replay says the recorded decisions still hold, not that
the code around them is right.**

### Model calls, and what may leave the container

No corpus text leaves the container — to Jev, OpenRouter or any third party — without the author's decision. `lmrun.py` (`approval=`), `rlm_ingest.py` (`--approval`) and `scripts/route.py` (the consent file of decision 007)
each encode that rule (decision 008 keeps the three as they are until one changes its rule and the others do not); a model call is recorded, cache off, and a real model is refused without an approval naming the decision.
Claude through `claude -p` is first party (decision 011, `claude_cli.py`, `claude_lm.py`, `he_claude.py`: no tools, no settings, no session, an empty working directory, thinking off unless asked); free OpenRouter models go
through `route.py`, pinned. **Changing what a model's output may do is measured on labels, not argued**: a proposal layer — `P_*` relations, entity lists, glosses, HyperExtract `P_HE_*` edges — sits **beside the graph, never in
it**, and nothing a model chose becomes a judgement, a page or a link until a person says so.

## Changing your mind

Two different things get corrected here, and treating them the same way is how this project has gone wrong in both directions at once.

### A claim is measured, or marked unmeasured

A claim says something is true of the repository or the corpus; it is backed by a count or explicitly marked as not yet counted, and when a measurement contradicts it, it is
simply wrong: change it and leave the correction beside it with how it went wrong. The failure mode is **too slow** — the heading claim was generalised from one document and survived three learnings before anything
counted the other 359. **A search result never becomes a number**: qmd ranks and does not enumerate (`Kernwelt` is in 144 landed documents and a forty-hit list is not a census of that); every number comes from `corpus.py`,
`duplicates.py` or a count, which say what they counted and how.

### A construct is demoted, not deleted

A construct — a field, a category, a name, a folder, a template — is not true or false; it is useful or it is not, and its test is use, not argument. The failure mode is **too fast**:
when `kind: brief | critique | result` drew the objection *don't commit to fixed document types* it was removed outright in the same turn, and the finding that *a result closes a question an earlier brief asked* lost the
distinction it needed. So a construct is never deleted on first objection; it is demoted in place:

```yaml
kind: brief          # provisional — a first-pass guess, not established
                     # may not: explain format, decide how a passage is read
                     # retire when: 20 documents show it predicts nothing
```

**`provisional`** says it is a guess, so nothing downstream leans on it without saying so; **`may not`** is the objection kept, as the reach it loses; **`retire when`** names the evidence that would end it, so the next argument is a
measurement. A construct that has carried a `may not` for twenty documents without once being useful can go, quietly, with no decision file. One that is **actively wrong** — keeping it would make someone assert something false —
leaves with a decision file, and its idea is written down in `PRINCIPLES.md`'s catalogue. **Be quick to measure a claim and slow to remove a construct**: they feel like one virtue and are opposites — a claim that survives
because nobody counted is a lie the repository tells itself, and a construct that dies on first objection takes with it every question it was the only way to ask.

## Committing a wiki page

**Every revision of a page in `Wiki/` is committed immediately, and the commit message names the source document the change came from.** One page changed is one commit, and the first line says which document caused it:

```
aegis: second expansion from aegis-emergenz-aus-der-leere
entropie: schöpferische Matrix from aegis-emergenz-aus-der-leere, conflict C2
guardians: five named bearers from guardians-und-kern-welten-konzept
```

Several pages may share a commit **only when one source document caused all of them in one reconciliation**, and the message still names that document. `git log --oneline Wiki/candidates/aegis.md` is then the page's
provenance, and a wrong reading is removable — every page a misread document touched is one `git log --grep=<slug>` away. **A commit that changes a page without naming a source document is the defect.** Two exceptions,
each naming what it is instead: **a corpus-wide re-measurement** (a landing batch, or `dedupe.py` folding copies away, makes every page that wrote a denominator like „among the 409 landed" wrong; such a commit changes
a number, never a reading), and **the navigation on the chapter pages** — `## What this chapter is about`, `## Questions for this chapter`, `## Candidate sources` and `## Raw qmd answers` are written by
`scripts/chapter_sources.py` from a run in `Plan/runs/qmd-chapters-2026-09-26/`, carry no citation or reading, are replaced whole on every run, and their commit names the run (the raw answers are copied by code into
```` ```qmd ```` fences in `Plan/runs/qmd-chapters-2026-09-26/raw/kap-NN.md`; `quotes.py` skips that info string and no other).

## Where the detail lives

| area | what to know | where |
|---|---|---|
| **The loop**, which command runs when, what a red check means | invariants first and last; `ingest` one document at a time with its refusals | skills `tools`, `ingest`; `Plan/concept/wiki-process_2026-09-16.md` |
| **Fetching** | the one automated step; bytes never pass through a model: `sources.py next`, then `mcp__Google_Drive__read_file_content` (the result spills to a file — the good path), then `sources.py land --drive-id <id> --consume`; never open the spill. `md` rows come through the text route (`fetch --include-md`); the `mp3` has none | `Plan/learnings/fetch.md`, `scripts/sources.py` |
| **Chapters and the plot** (decision 013) | `Wiki/chapters/kap-NN.md` collects every read source's reading of one chapter, attributed and unmerged, with `## Where the sources differ`; `Wiki/overview/` places (`chapters.md`, `plot.md`); 101 <!--state:chapters.missing--> chapter mentions in read documents have no reading yet | `Wiki/chapters/README.md`, `scripts/chapters.py` |
| **The knowledge graph and retrieval** | `graph.py` builds 202 <!--state:graph.nodes--> nodes and 5141 <!--state:graph.edges--> typed edges from frontmatter, `[[links]]` and `^[slug.md:Lnn]`, every edge carrying the file line that states it; 10536 <!--state:graph.evidence--> quotations as evidence, 10536 <!--state:graph.evidence_verified--> verified by `quotes.verdict`. `graphrag.py ask` returns verified quotations, the conflicts and questions touching them and the documents the rank reached — never prose. `kg.py` serves the same graph from a disposable GraphQLite projection `Plan/derived/ask.db` (a cache, not an authoring input); `kg.py export` writes the `Graph/` atlas, output only, never imported, and `kg.py export --check` fails when it is stale. `bench` scores retrieval on the 25 <!--state:graphrag.cases--> labelled cases, recall@8 53 <!--state:graphrag.recall_seeds-->% from seeds alone and 68 <!--state:graphrag.recall_ppr-->% with PageRank (the same hand wrote question and label, and 92 % of its gold lines are lines term pages also quote: a regression test, not a measure of discovery — `Plan/concept/evaluation-audit_2026-09-30.md`) | skill `graph-context`, `Graph/README.md`, `Plan/learnings/ask.md`, `Plan/concept/graphrag_2026-09-23.md` |
| **Changing the graph** | measured on the labels, not argued: `graphlab.py`; one relation — normalised co-mention — helped and is off until the author turns it on; 32 HyperExtract contracts (`Plan/hyperextract/`, each `provisional`/`may not`/`retire when`) are run by `he_claude.py` on `hx.py` — HyperExtract's engine ported to the standard library, byte for byte what upstream sends (decision 020) — and loaded by `hegraph.py`; the `he-lines` finder is off; the backfill was stopped (decision 019) | `Plan/concept/graph-contracts_2026-09-30.md`, skill `hyperextract-learning` |
| **The proposal layer** | 300 <!--state:proposals.entities--> entities from verified entity lists (53 <!--state:proposals.entities_paged--> fold to a page), 195 <!--state:proposals.glosses--> glosses from `A (B)` written in two documents — unjudged, routing an English question to a German page, merging nothing | `scripts/graph.py --proposals`, `Plan/runs/bilingual/` |
| **The chunk index** | `novelgraph/` (its own uv project) chunks every landed source three ways into line ranges under `Index/` — no text stored, every hit a `slug.md:Lnn–Lmm` — with `fold()` surfaces and lemmata, static Model2Vec vectors, BM25, and hybrid search by RRF in milliseconds once loaded; incremental by sha256 and chunk id. `ask.py` can use it as a finder (`--with novelgraph`, off by default): on the frozen cases it adds +0.016 document and +0.018 line recall at the same byte budget, at about 10 s per cold call (`Plan/runs/novelgraph-finder-2026-10-02/`); turning it on is the author's call. `Index/` stays committed as chunk rows (SPEC.md §5). `novelgraph rlm` puts a `dspy.RLM` agent over it (Claude, decision 011); its run chose the chunk size, `heading@v1` | `docs/novelgraph-index.md`, `Plan/runs/rlm-chunks-2026-10-01/README.md` |
| **Searching** | qmd indexes seven collections named for purpose and answers a German phrase with a file and a line; **nothing in the pipeline depends on it** (reconciliation answers by lookup); a file in no collection is absent from every search, so `python3 scripts/qmd_coverage.py` is checked; **never run `qmd init`** (it overwrites `.qmd/index.yml`); a document landed after the index was built is in no search until `qmd update` | skill `qmd`, `scripts/setup_qmd.sh` |
| **Sources at a glance** | `python3 scripts/overview.py` writes the end of `Sources/README.md` — every landed document by category with its most important names, a count each, ranked by tf-idf; `--check` fails when stale | `scripts/overview.py` |
| **Entity lists** | `Plan/entities/<slug>.md`: one model's list of the 50–100 most important entities of a document, each citing a line code placed (`entities.py place` refuses a name the document does not contain). They may not seed a census, create a page, supply a count or merge two surfaces. `bilingual.py` maps German and English surfaces — proposals, no pair is a judgement | `scripts/entities.py`, `.claude/workflows/entity-lists.js`, `Plan/concept/entity-lists_2026-09-23.md` |
| **Gold lists, and scoring against them** | `gold.py` decides by rule which candidate lists are gold (decision 009); `goldeval.py` scores every extractor — HyperExtract contracts, entity lists, blind re-readings — against the gold list of each document it read; `goldrel.py` holds a blind reader's relations in the contracts' own types and scores the three contracts' pairs against them, piloted on three documents. A gold list is one reading, not the truth, and the ceiling for a relation list — two blind readers' agreement — is not yet measured | `Plan/runs/gold-2026-09-30/README.md`, `scripts/README.md` |
| **The project app** | `python3 scripts/ui.py` derives the pages, conflicts, questions, the novel's workspace in `Manuscript/` with the writing findings and the Weichen (screen „Manuscript“ in seven tabs, decisions 023, 024), graph, manifest, invariants, decisions, `NOW.md` and `GOAL.md` into the files of a claude.ai Design canvas in `Plan/derived/ui/`; it infers nothing. A script cannot publish it: a Claude session does, with the Artifact tool, to https://claude.ai/artifact/1EyhQkX3MpiRTw3TxjTjYL (private to the author); a data refresh sends `project/Main.dc.html` alone, so the canvas keeps the author's arrangement. The app is a snapshot and names its commit. **It is also a website** (decision 022): Vercel project `kohaerenzprotokoll`, connected to this repository, runs `python3 scripts/web.py` on every push — the frames beside the canvas's runtime, vendored as `scripts/web/support.js` — behind the author's Vercel login | `scripts/ui.py` (`--check`, `selftest`), `scripts/ui.html`, `scripts/ui.js`, `scripts/web.py`, `vercel.json`, `Plan/concept/vercel-app_2026-10-02.md` |
| **The project app** | `python3 scripts/ui.py` derives the pages, conflicts, questions, graph, manifest, invariants, decisions, `NOW.md` and `GOAL.md` into the files of a claude.ai Design canvas in `Plan/derived/ui/`; it infers nothing. A script cannot publish it: a Claude session does, with the Artifact tool, to https://claude.ai/artifact/1EyhQkX3MpiRTw3TxjTjYL (private to the author); a data refresh sends `project/Main.dc.html` alone, so the canvas keeps the author's arrangement. The app is a snapshot and names its commit. **It is also a website** (decision 022): Vercel project `kohaerenzprotokoll`, connected to this repository, runs `python3 scripts/web.py` on every push — the frames beside the canvas's runtime, vendored as `scripts/web/support.js` — behind the author's Vercel login; there every page, conflict, question, document and graph node has an address (`#/wiki/aegis`, `#/conflicts/C2`), checked both ways by `ui.py --check` | `scripts/ui.py` (`--check`, `selftest`), `scripts/ui.html`, `scripts/ui.js`, `scripts/web.py`, `vercel.json`, `Plan/concept/vercel-app_2026-10-02.md` |
| **Calling a model — DSPy** | `lmrun.py` (cache off, one record per call, status `answered`/`refused`/`unparsed`/`unreachable`, never a score), `claude_lm.py`, `lm_fixture.py` (offline), `baseline.py` (`Plan/runs/baselines.jsonl`, append-only), `pairs.py` (a rule first, a model only on the residual; 89 <!--state:pairs.labelled--> labelled pairs, `fold()` decides 48 <!--state:pairs.fold_correct-->, the plural rule of decision 010 57 <!--state:pairs.plural_correct-->), `check_dspy_surface.py`, `check_dspy_skill.py`, `check_skills.py` | skill `dspy`, `scripts/README.md`; no model's decision has entered `judgements.jsonl` |
| **The writing skills** | thirteen augmentation-only fiction skills adapted from `netzkontrast/writing-skills` (commit `2fad031`, MIT, © Rhymenoceros s. r. o.): editorial, character, critique and craft — **none writes or rewrites the author's prose**; canon is the author's decisions and approved chapters, never the wiki's readings; findings go to `Plan/runs/writing/` | skill `writing-skills`, `Plan/concept/novel-writing-plan_2026-09-29.md` |
| **Readers that are agents** | `document-reader` (steps 1–4 of the ingest), `wiki-reader` (readings files that `readings.py` turns into pages), `corpus-researcher`, `hyperextract-template-agent`; never choosing documents, creating pages or deciding conflicts | `.claude/agents/`, skill `reader-tools` |

## Tracking work

`NOW.md` holds what is open right now, one page, and things leave it when they are done. **Questions for the author are noted there, and in `Plan/questions-for-the-author.md`, and work continues without waiting for the
answer** — the author's instruction of 2026-09-24. `Plan/decisions/` holds one short file per decision, permanently: what was chosen, what was rejected, what would change our mind. Git holds everything that happened.
There is no board, no status field and no backlog.

## `Legacy/`

The novel, the graph, the codex, the old planning record and the retired commands are parked there. No script reads it, nothing in `Wiki/` or `Sources/` mentions it, and it is not part of any workflow; `README.md` says in one
sentence what it holds. It is a shelf, not a layer — if it starts being referenced, it has become a layer again, and that is the thing being removed. **One exception, deliberate:** `Plan/` cites it where a measurement came
from there — the two live pilot runs of the retired pipeline are the only data on what this work costs at scale — because citing where a fact came from is not depending on the file. Nothing is read from `Legacy/` at run time.
