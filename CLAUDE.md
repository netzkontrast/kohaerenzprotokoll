# Kohärenz Protokoll — session contract

A German hard-SF novel and its research corpus. German manuscript prose stays German; engineering and planning use English. This file contains standing operating rules. `NOW.md` contains current work; `PRINCIPLES.md` contains the reasons and design principles. Do not duplicate their histories or measured counts here.

## Start a session

1. Read `AGENTS.md`, `NOW.md`, this file and `PRINCIPLES.md`. The author's current instruction wins; follow NOW.md's named mandate and linked briefing before choosing unrelated work. Read `SPEC.md` before architecture changes.
2. Run `python3 scripts/knowledge.py init --profile reader` as coordinator (`research` for DSPy work). Claude's SessionStart hook already runs the research initializer; inspect its result before repeating it. Workers use the matching `--check` profile and never rebuild shared stores. Report unavailable capabilities; a source-only task can continue with `read.py` when those capabilities are irrelevant. Install dependencies in virtualenvs, never system Python.
3. Run `python3 scripts/sessions.py board`. Read active branches and open PRs before selecting work. Unknown live state is not free. Claim work with an open PR whose body has `Session: <id>`; a branch name is not a claim. For source ingest also name the source slugs under `Claim`.
4. Load only the skill for the operation below and its needed references. Enumerate current files instead of assuming an old chapter variant, source count or branch remains current.

## Authority and writes

| Input | Authority | Write path |
|---|---|---|
| `Sources/manifest.jsonl`, `Sources/drive/` | Immutable landed research, including narrative-looking sources | `sources.py` only; never model-rewrite bytes |
| `Sources/terms/`, `Sources/notes/`, `Wiki/` | Independent source readings, disagreements and human reviews; not novel canon | Ingest/reconciliation procedures; preserve attribution |
| `Manuscript/kanon.md`, dated author decisions and approved material | Decided content; later explicit corrections win | Author-authorized change only; no automatic promotion |
| `Plan/storyform/a.json`, `b.json`, `weave.json` | Approved structure with provenance | `storyform` workflow; do not change an answer to pass a check |
| `development.json`, cards, drafts, scene lists and simulation runs | Proposals or working bases unless explicitly approved | Preserve their status and assumptions |
| `Plan/derived/`, `Graph/`, generated NCP and overview | Disposable derived views | Regenerate from authoritative inputs; never hand-edit or import the Graph atlas |

`Sources/` and `Wiki/` are the two research layers; `Manuscript/` is what they serve. A source calling itself canon cannot promote itself. `Legacy/` is parked, never runtime input, canon or a prose reference; historical measurements may cite it without reading it at runtime. `GOAL.md` describes the target; it does not certify implemented features.

## Evidence and model calls

- Freeze a document's independent census/note before loading wiki or cross-document context. Reconcile by the existing lookup procedure. Readings remain attributed and unmerged; semantic conflicts remain judgement, not a program's verdict.
- Obtain source lines with `read.py` and `--find`; never invent identifiers or reconstruct quotations. Wiki references name the source slug. `quotes.py` verifies them; uncheckable is not passed. Search ranking is discovery, never a corpus count.
- Model output proposes; it does not decide canon, conflicts, judgements or links. Keep proposal relations out of the core graph. Record actual inputs, outputs, status, usage and cost through the existing compatible model path; evaluation caches stay off.
- No corpus text goes to a third party without the author's decision for that run (007/008/011). Claude CLI's isolated first-party path remains as specified by decision 011. Do not infer a new provider permission from this AEGIS plan.
- Model calls are serial, except up to two Sonnet ingest readers allowed by NOW.md; their reconciliation and commits remain sequential. Do not interpret multiple fictional figures as permission for parallel paid runs.
- Every workflow needs an offline fixture. Name separate mechanical checks and human judgements; `not run`, unavailable and incomplete are not success.

For claim correction, provisional constructs and source-named wiki commits, read [session-method](Plan/concept/session-method.md). Never collapse different sources into one reading or delete a construct merely because its first use is disputed.

## Select the workflow

| Task | Read next |
|---|---|
| Ingest/reconcile a source | `.agents/skills/ingest/SKILL.md`, `tools`; workers: `reader-tools` |
| Bounded research or evidence lookup | `reader-tools` (research scope), `graph-context` or `qmd`; discovery alone is not ingest |
| Plot, casting or NCP | `storyform`; chapter execution: `scene-architecture` planning/review mode |
| Manuscript critique, voice or continuity | `writing-skills`, then the relevant specialist; findings in `Plan/runs/writing/` |
| AEGIS agent implementation | The next section and `Plan/briefings/aegis-agent-pilot.md` |
| Model/template experiment | `dspy` or `hyperextract-learning`; approvals and STOP files still apply |
| NOW/app changes | `app-refresh`; build from sources, keep routes and agent exports consistent |

Project skills live in `.agents/skills/`; `.claude/skills/` links to them. Do not edit two copies or rewrite pinned vendored skills. The coding coordinator implements software; editorial skills critique prose; fictional agents act only inside their scenario. A review skill's no-rewrite rule does not ban an explicitly authorized separate drafting task.

## AEGIS implementation mandate
**535 <!--state:documents.with_census--> documents have a term census** in `Sources/terms/`, 535 <!--state:documents.with_note--> a note in `Sources/notes/`, 535 <!--state:documents.reconciled--> a reconciliation in `Wiki/compare/`.
`python3 scripts/account.py order` holds — `true` <!--state:order.holds--> — when every document with a census has a note and a reconciliation, each ran against the state the previous one left, and the wiki
matches what the newest run recorded leaving; when it does not, it says so with exit status 1. What each document added is in its reconciliation record `Wiki/compare/reconcile-NN-<slug>.md` and, up to document 51,
in `Plan/runs/reading-log.md`. `Plan/runs/judgements.jsonl` holds 121 <!--state:judgements.total--> judgements about near matches, 8 <!--state:judgements.mechanised--> mechanised and replaying green,
0 <!--state:judgements.disagree--> disagreeing.

**The wiki**: `Wiki/candidates/` holds 106 <!--state:wiki.pages--> term pages, `Wiki/conflicts/` 17 <!--state:wiki.conflicts-->, `Wiki/questions/` 9 <!--state:wiki.questions-->, `Wiki/chapters/`
41 <!--state:wiki.chapters--> chapter pages (Kap 0–40, 2344 <!--state:chapters.readings--> readings, decision 013), and `Wiki/compare/` the reconciliation record per document. The schema follows the pages rather than
preceding them: a promoted page stays in `Wiki/candidates/` with `status: reviewed` (decision 026), 1 <!--state:wiki.reviewed--> so far, and only a reviewed candidate gets a term page in `Wiki/terms/` (decision 027), 1 <!--state:wiki.terms--> so far. A term page collects every source's reading of one term, **attributed and unmerged**: where sources disagree the page says so and stops.
Which reading is right is the author's call, never the page's.

The author requested the plan on 2026-10-13 and this PR/instruction update. The implementation below is the next proposed coding task, not a claim that a runtime exists or a new canon decision.

Read the [pilot briefing](Plan/briefings/aegis-agent-pilot.md) before coding; the full rationale and source review are in [the plan](Plan/concept/aegis-agent_2026-10-13.md). Start with two manual cases, AEGIS and one counterfigure, then an offline standard-library implementation. Reuse the existing canon, storyforms, pack contracts and model adapters where they fit. A fictional AEGIS is not the research pipeline's canon checker.

Keep perception filtering outside the model. Characters receive only scenario-visible facts and allowed actions, with no repository tools. AEGIS proposes typed actions; deterministic code validates prerequisites, state version and resource costs before committing one event. Preserve mistaken beliefs separately from facts. Pause/reactivate figures from persisted events; replay uses frozen responses and never calls a model. Simulation events and literary logs are separate artifacts.

Keep manuscript/canon untouched. Model integration, Ink/inkjs play, public backend and alternative endings are later steps, each earning its scope through pilot evidence. Do not add a graph database, MCP server, controller framework or swarm before the offline cases need it. The briefing owns deliverables and acceptance criteria; update it when implementation proves a design assumption wrong.

## Finish a change

Run the checks appropriate to the changed inputs and every required CI step from `.github/workflows/checks.yml`. Standard checks include `state.py --prose`, `account.py order --summary`, `quotes.py`, `wiki_index.py --check`, `promote.py check`, `terms.py check`, `judgements.py --open`, `chapters.py`, `overview.py --check`, `storyform.py --check` and `selftests.py --only std`; run `derive.py` first. Skill edits also run `check_skills.py`. Report venv suites separately.

NOW.md changes affect the session UI: derive sessions and run `ui.py --check` / `web.py --no-build --check` using `app-refresh`. The pre-PR app hook was removed on 2026-10-06; do not reintroduce a mandatory hook or claim deployment from a local build. Visual/deployment checks require their actual environment; report any unavailable verification.

Commit complete work with provenance, keep PR descriptions current, and preserve unrelated work. After the author merges an active branch, merge `origin/main` into it rather than rebasing or resetting it; open a new PR when continuing. Decisions belong in `Plan/decisions/`, evidence in `Plan/runs/`, questions in `Plan/questions-for-the-author.md`, next steps in NOW.md, and history in git. The session board derives from NOW.md and live GitHub; do not create a second persistent backlog.
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
                                                 review (the author)
                                                           ▼
                                          status: reviewed, pinned ──→ ask
                                                           │
                                               write (a session or the author)
                                                           ▼
                                      Wiki/terms/*.md, German, approved by the author
```

- **A census lists the candidate terms of one document by a written rule** — what it names in the novel's world, the words it uses as its own terms, the borrowed concepts it applies (decision 012). **A note**
  harvests what that document says about the terms that matter, quoting with line numbers. **A census describes one document and nothing else**: no count, comparison or expectation from another source.
  `Plan/briefings/extract.md` is read before the document and carries **procedural** knowledge (what German Drive exports do), never **document** knowledge (what some other file said). The census is frozen before the
  wiki is consulted, so the accumulated state cannot decide in advance what a new document is allowed to say — that independence is what makes reconciliation safe.
- **Reconciliation never reads the wiki.** `scripts/wiki_index.py` derives `Wiki/index.json` from page frontmatter and `scripts/reconcile.py` answers by lookup, printing only what no lookup settles: cost per document
  is `O(census) + O(judgement)`, not `O(wiki)` (`Plan/concept/reconciliation-by-lookup_2026-09-17.md`). It also **sweeps the text for everything the wiki already knows** (decision 012): each page the text names without a
  matching candidate is decided as a reading, which goes on the page, or an occurrence (a title, a reference, another sense) — recorded in `Plan/runs/sweep.jsonl`: 1875 <!--state:sweep.decided--> decided,
  860 <!--state:sweep.readings--> of them readings the lookup had missed, 0 <!--state:sweep.open--> open (`reconcile.py --sweep-open`).
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
and nothing else and reports a link pointing at no page; `scripts/link.py [--apply]` marks the mentions the prose already makes — a page links a term once, and **a link is never inferred**. There are 745 <!--state:wiki.relations--> links
across the 106 <!--state:wiki.pages--> pages, 17 <!--state:wiki.orphans--> of them with nothing pointing in, and 908 <!--state:wiki.unmarked--> mentions left unmarked because every one sits inside a quotation, a citation line or a
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
| **Chapters and the plot** (decision 013) | `Wiki/chapters/kap-NN.md` collects every read source's reading of one chapter, attributed and unmerged, with `## Where the sources differ`; `Wiki/overview/` places (`chapters.md`, `plot.md`); 307 <!--state:chapters.missing--> chapter mentions in read documents have no reading yet | `Wiki/chapters/README.md`, `scripts/chapters.py` |
| **The plot's structure** (decision 025) | two Dramatica storyforms, A (Kael) and B (AEGIS), under one premise; `Plan/storyform/a.json` and `b.json` hold every value with its provenance, `scripts/storyform.py` refuses what the chart rejects and checks the storyweaving scaffold `weave.json` and writes `overview.md` and one NCP 3.0.0-rc.1 document, `scripts/dramatica.py` holds the chart and the engine rules rebuilt from the Dramatica forum; signposts are the author's, their function is not published | skill `storyform`, `Plan/storyform/overview.md` |
| **The plot's proposed execution** | `Plan/storyform/development.json` holds chapter goals, actions, costs, knowledge, timing, sources and open choices; `storyform.py` validates it and generates overview and NCP Moment fields, and the storypoints line under every paragraph of the treatment (`Manuscript/plot/treatment.md`). Every row is a proposal, never an override of `a.json`, `b.json`, `weave.json` or canon. Drafts A–I supply techniques, not authority. | skills `storyform`, `scene-architecture`, `writing-skills`; `Plan/runs/writing/book/plot-development_2026-10-06.md` |
| **The knowledge graph and retrieval** | `graph.py` builds 595 <!--state:graph.nodes--> nodes and 16510 <!--state:graph.edges--> typed edges from frontmatter, `[[links]]` and `^[slug.md:Lnn]`, every edge carrying the file line that states it; 31399 <!--state:graph.evidence--> quotations as evidence, 31391 <!--state:graph.evidence_verified--> verified by `quotes.verdict`. `graphrag.py ask` returns verified quotations, the conflicts and questions touching them and the documents the rank reached — never prose. `kg.py` serves the same graph from a disposable GraphQLite projection `Plan/derived/ask.db` (a cache, not an authoring input); `kg.py export` writes the `Graph/` atlas, output only, never imported, and `kg.py export --check` fails when it is stale. `bench` scores retrieval on the 26 <!--state:graphrag.cases--> labelled cases, recall@8 55 <!--state:graphrag.recall_seeds-->% from seeds alone and 64 <!--state:graphrag.recall_ppr-->% with PageRank (the same hand wrote question and label, and 92 % of its gold lines are lines term pages also quote: a regression test, not a measure of discovery — `Plan/concept/evaluation-audit_2026-09-30.md`) | skill `graph-context`, `Graph/README.md`, `Plan/learnings/ask.md`, `Plan/concept/graphrag_2026-09-23.md` |
| **The MCP server** (decision 029) | the retrieval tools as a FastMCP server on Vercel, `main` only: `search` (BM25 over the read documents' lines, the verified quotations, the wiki's records), `ask` (graph retrieval as `graphrag.py`, plus source lines), `read_lines`, `verify_quote`, `item`, `list_items`, `document`, `state`, `sessions` — evidence with document and line, never prose. `scripts/rag.py` (standard library) builds the serving index at deploy time (`web.py`) and holds the logic; `api/rag_server.py` is the transport (`requirements.txt`, `.venv-mcp` via `install.sh mcp`); `vercel.json` rewrites `/mcp` to it. Unread documents, documents whose note marks personal material, and every line with a figure's earlier name or the trauma symbol are withheld. Access: the project's own login, `middleware.js` — the site behind HTTP Basic (`SITE_PASSWORD`), `/mcp` behind a bearer token (`RAG_MCP_TOKEN`, checked again by the server), each path closed (503) while its variable is unset (`scripts/auth_selftest.js`) | `Plan/concept/mcp-server_2026-10-16.md`, `scripts/rag.py`, `api/rag_server.py` |
| **The website's static pages and the build cache** | `web.py` also writes every wiki record as a plain HTML page (`scripts/static_pages.py`, `static/` on the website, only changed pages rewritten); `ui.py` keeps the rail's invariants and self-tests per tree in `Plan/derived/checks/` (key: HEAD's tree and the bytes of every changed or untracked file), so a second build of the same files skips them; `--fresh-checks` runs them anyway | `scripts/static_pages.py`, `scripts/ui.py` |
| **Promoting a page** (decision 026) | the author's review of a term page, recorded in place: `status: reviewed`, the reviewed part pinned by sha256 in `Plan/runs/promotions.jsonl` with the author's words; a review of the account, never a choice of reading. `promote.py sheet <page>` measures what can be measured (quotations, every source read through, frontmatter, links refuse; readings waiting, open conflicts, coverage are noted) and lists what a person judges; a source read later lands under `## Since review` (`readings.py`), `link.py` leaves a reviewed part alone, and `promote.py check` — on GitHub — fails when one changed. 1 <!--state:wiki.reviewed--> page reviewed; the rule is provisional until the author answers the concept's §7 | `Plan/concept/promotion_2026-10-08.md`, `scripts/promote.py`, `Plan/runs/promotion-2026-10-08/` |
| **Term pages** (decision 027) | `Wiki/terms/<slug>.md`: the author's German page for one term, written from a reviewed candidate — what is decided (`[K]`, linked to a decision, an answered Weiche, `kanon.md` or a decided conflict), what sources say (`[S]`, cited), proposals, gaps and derivations, every bullet tagged; an author's block no tool writes. `terms.py finds` lists where the project's records name a term, `scaffold` refuses an unreviewed candidate, `check` (on GitHub) enforces the tags, sections, links, German and the pin of an approved page, `approve` records the author's words. 1 <!--state:wiki.terms--> page, 0 <!--state:wiki.terms_approved--> approved; the app shows it before the candidate | `Wiki/terms/README.md`, `Plan/concept/wiki-terms_2026-10-08.md`, `scripts/terms.py` |
| **Changing the graph** | measured on the labels, not argued: `graphlab.py`; one relation — normalised co-mention — helped and is off until the author turns it on; 32 HyperExtract contracts (`Plan/hyperextract/`, each `provisional`/`may not`/`retire when`) are run by `he_claude.py` on `hx.py` — HyperExtract's engine ported to the standard library, byte for byte what upstream sends (decision 020) — and loaded by `hegraph.py`; the `he-lines` finder is off; the backfill was stopped (decision 019) | `Plan/concept/graph-contracts_2026-09-30.md`, skill `hyperextract-learning` |
| **The proposal layer** | 300 <!--state:proposals.entities--> entities from verified entity lists (53 <!--state:proposals.entities_paged--> fold to a page), 195 <!--state:proposals.glosses--> glosses from `A (B)` written in two documents — unjudged, routing an English question to a German page, merging nothing | `scripts/graph.py --proposals`, `Plan/runs/bilingual/` |
| **The chunk index** | `novelgraph/` (its own uv project) chunks every landed source three ways into line ranges under `Index/` — no text stored, every hit a `slug.md:Lnn–Lmm` — with `fold()` surfaces and lemmata, static Model2Vec vectors, BM25, and hybrid search by RRF in milliseconds once loaded; incremental by sha256 and chunk id. `ask.py` can use it as a finder (`--with novelgraph`, off by default): on the frozen cases it adds +0.016 document and +0.018 line recall at the same byte budget, at about 10 s per cold call (`Plan/runs/novelgraph-finder-2026-10-02/`); turning it on is the author's call. `Index/` stays committed as chunk rows (SPEC.md §5). `novelgraph rlm` puts a `dspy.RLM` agent over it (Claude, decision 011); its run chose the chunk size, `heading@v1` | `docs/novelgraph-index.md`, `Plan/runs/rlm-chunks-2026-10-01/README.md` |
| **Searching** | qmd indexes seven collections named for purpose and answers a German phrase with a file and a line; **nothing in the pipeline depends on it** (reconciliation answers by lookup); a file in no collection is absent from every search, so `python3 scripts/qmd_coverage.py` is checked; **never run `qmd init`** (it overwrites `.qmd/index.yml`); a document landed after the index was built is in no search until `qmd update` | skill `qmd`, `scripts/setup_qmd.sh` |
| **Sources at a glance** | `python3 scripts/overview.py` writes the end of `Sources/README.md` — every landed document by category with its most important names, a count each, ranked by tf-idf; `--check` fails when stale | `scripts/overview.py` |
| **Entity lists** | `Plan/entities/<slug>.md`: one model's list of the 50–100 most important entities of a document, each citing a line code placed (`entities.py place` refuses a name the document does not contain). They may not seed a census, create a page, supply a count or merge two surfaces. `bilingual.py` maps German and English surfaces — proposals, no pair is a judgement | `scripts/entities.py`, `.claude/workflows/entity-lists.js`, `Plan/concept/entity-lists_2026-09-23.md` |
| **Gold lists, and scoring against them** | `gold.py` decides by rule which candidate lists are gold (decision 009); `goldeval.py` scores every extractor — HyperExtract contracts, entity lists, blind re-readings — against the gold list of each document it read; `goldrel.py` holds a blind reader's relations in the contracts' own types and scores the three contracts' pairs against them, piloted on three documents. A gold list is one reading, not the truth, and the ceiling for a relation list — two blind readers' agreement — is not yet measured | `Plan/runs/gold-2026-09-30/README.md`, `scripts/README.md` |
| **The project app** | `python3 scripts/ui.py` derives the pages, conflicts, questions, the novel's workspace in `Manuscript/` with the writing findings and the Weichen (screen „Manuscript“ in seven tabs, decisions 023, 024), graph, manifest, invariants, decisions, `NOW.md` and `GOAL.md` into the files of a claude.ai Design canvas in `Plan/derived/ui/`; it infers nothing. A script cannot publish it: a Claude session does, with the Artifact tool, to https://claude.ai/artifact/1EyhQkX3MpiRTw3TxjTjYL (private to the author); a data refresh sends `project/Main.dc.html` alone, so the canvas keeps the author's arrangement. The app is a snapshot and names its commit. **It is also a website** (decision 022): Vercel project `kohaerenzprotokoll`, connected to this repository, runs `python3 scripts/web.py` on every push to `main` and on no other branch (`vercel.json`'s `git.deploymentEnabled`, the author's instruction of 2026-10-16) — the frames beside the canvas's runtime, vendored as `scripts/web/support.js` — behind the author's Vercel login; there every page, conflict, question, document and graph node, and every item of the novel's workspace, has an address (`#/wiki/aegis`, `#/conflicts/C2`, `#/manuscript/cast/kael`), checked both ways by `ui.py --check`. **Agents read it too**: beside the frames it serves `llms.txt` and `agents/` (`sessions.json`, `index.json` with every item's repository path and address, `state.json`, `data.json`), and the Now screen holds **a start-prompt editor** for **the next sessions** — `scripts/sessions.py` reading NOW.md § Half-done, nothing stored, each session's prompt as blocks to switch on and off, the author's own instruction, free editing, copy and save (empty prompts and incomplete free sessions are refused; manual edits lock the fields until “Use fields again”, which keeps their values), drafts in the browser only (`#/now/session/<id>`, `#/now/session/free`), and **a session editor** — title, next step and files give a prompt, the claim line and a NOW.md § Half-done entry that `sessions.py` reads back as the same session (checked both ways by `ui.py --check`); the page also shows **the session board** (claims and active branches from GitHub, automatically refreshed at most every five minutes while Now is visible; failed or timed-out requests report unknown claims). **No hook gates a pull request on the app** — the author removed the pre-PR hook on 2026-10-06; `ui.py --check` still writes the stamp `scripts/appstamp.py verify` reads, and the skill `app-refresh` is the procedure | skill `app-refresh`, `scripts/ui.py` (`--check`, `selftest`), `scripts/ui.html`, `scripts/ui.js`, `scripts/web.py`, `scripts/sessions.py`, `scripts/appstamp.py`, `vercel.json`, `Plan/concept/vercel-app_2026-10-02.md`, `Plan/concept/agent-sessions_2026-10-05.md` |
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
