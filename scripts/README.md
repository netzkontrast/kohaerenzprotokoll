# scripts/ — what does what

Every tool the wiki is built with. Each runs from the repository root:

    python3 scripts/<name>.py …

Most are standard library and need nothing installed. The ones that need a venv
or a tool name it below, and `scripts/install.sh <name>` installs it.

This page is the map: one entry per file, what it is for, and what it writes.
It is not the manual:

- **A script's docstring is its documentation** — why it exists, what it
  measured, how to call it. Read the top of the file before running it.
- **`.agents/skills/tools/references/commands.md`** has every flag and every
  artifact.
- **`.agents/skills/tools/SKILL.md`** has the order they run in, and what a red
  check means.

A script not listed as writing only prints, and is safe to run at any time.

**This page is checked, not remembered.** 0 <!--state:readme.scripts_drift-->
files in `scripts/` are missing from it or listed here without existing, and
`python3 scripts/state.py --prose` fails the day that number is not 0.

## Setting up a container

| file | does | writes |
|---|---|---|
| `knowledge.py` | Initializes reader/research/full tool capabilities through the existing installers and independent graph/qmd CLIs; workers use `init --check`, which writes nothing. | existing installers/indexes; only init writes a lock under `Plan/derived/`; no model extraction |
| `contracts.py` | What every HyperExtract contract did on every source, from the run directories: one outcome per run — `yielded`, `refused`, `found nothing` (every call answered, the list empty: knowledge about the document), `not staged`, `failed` (not knowledge) — and `stale` when the contract changed since. Writes `Plan/runs/<slug>/contracts.{json,md}` per source and the matrix `Plan/runs/contracts.md`; `--check` fails when one is stale. | `Plan/runs/<slug>/contracts.*`, `Plan/runs/contracts.md` |
| `modelpick.py` | Which model reads a contract on a source (`Plan/hyperextract/models.json`): about a fifth of runs explore a model from the pool at random — drawn from the hash of contract, source and run, so a choice is re-derivable — the rest take the model with the best **labelled** precision for the contract (in the source's category, else anywhere), never the one with the most admitted rows; with too few labels, the default. `he_claude.py run --model auto` (the default) asks here and records the choice. | — |
| `hx.py` | HyperExtract, ported (decision 020): loads a template (a YAML subset, refused outside it), builds its prompt and JSON schema, cuts a document into LangChain's chunks, checks a reply as pydantic would, merges as upstream merges (list append; set and graph by identifiers, never with a model). `parity` compares every template and every landed document's chunks with the upstream package when it is installed; `selftest` holds the same on a pinned record of it. | — |
| `reading_extract.py` | Runs offline template smoke fixtures on `hx.py` and stages HyperExtract passage/relation candidates with source/template hashes, quotation placement and refusals. A name stands when a quotation of it does, or, under four characters, when it is a word on its own on some line (`Lex`, `Nyx`, `KW1`); a contract's word for no name (`unlabelled`) needs no line. | `Plan/runs/<slug>/hyperextract/<new-run>/`; no Sources/wiki/database writes |
| `hegraph.py` | HyperExtract candidates in the shared store, and the report on what each contract yielded. Loads staged rows as `P_HE_<KIND>` edges (never in the core) from the line the quotation is on to its contract node and to each page or entity its names, or its quotation, contain — on two footings, *names* (every name stands in the document) and *quote* (a slot is the model's own wording; the pages are found by code); an alias without an alias word and an order without an order word are not admitted. Grades by code and reports, per contract, the yield, refusals, cost, the precision of the rows a reader labelled, the agreement with the lines the pages cite, and what each document's contracts together find. `gate` keeps the paragraphs a contract's cue words are in. Standard library. | `Plan/runs/hyperextract-templates-2026-09-30/yield.md`; the store's one build |
| `install.sh` | Installs everything a fresh container lacks — `Plan/derived/`, every venv, the uv tools, qmd's package — one named component at a time; skips what is present. `--check` reports and changes nothing; `--list` names the components. The cloud session-start hook runs it. | the venvs, the tools, `Plan/derived/`, `.install.log` |
| `setup_qmd.sh` | qmd alone: the package and a shim on the path, then its models, index and embeddings, which `install.sh` leaves out by default. `--package` stops after the shim; `--check` changes nothing. | `.tools-node/`, qmd's index, `/usr/local/bin/qmd` |

## Shared modules

Imported by the others. Call these rather than writing a second copy: two
encodings of one rule drift apart on the first edit (P6).

| file | owns |
|---|---|
| `subject.py` | The substrate: repository paths, reading and writing a JSONL file, the manifest rows and the rows folded out of it, every landed document with its body and the **file** line that body starts on, a document's derived facts, the judgement ledger, and `cli()`, which runs a script's `main`. The one implementation of where a source document's frontmatter ends. Imported, never run. |
| `wiki_index.py` | `fold()` — whether two surfaces are one term — `mention()` — where a term stands alone as a word, for every script that counts or marks one — and wiki-page frontmatter. Run, it writes `Wiki/index.json`, the lookup `reconcile.py` answers from; `--check` reports what the index cannot see. |
| `quotes.py` | `normalise()`, `pairs()` and `verdict()`: which citation belongs to which quotation, and whether it resolves. `tally()` counts the outcome over every file; `state.py` and `ui.py` take the count from there. Run, it checks every „…" ^[Lnn] in the repository, or in one file. |
| `rules/__init__.py` | The contract every rule keeps — a module with `NAME`, `VERSION`, `applies()` and `derive()` — and `load()`, which `derive.py` applies them through. |
| `rules/structure.py` | How a document is built: headings, tables, formulas, length. `profile.py` counts with its patterns. |
| `rules/surfaces.py` | Every capitalised token, with its count and lines — the index `corpus.py` answers from. |
| `rules/attribution.py` | Where a document attributes a claim to something outside itself. |
| `rules/export_damage.py` | What the Drive conversion did to the text. `capture.py` and `profile.py` count with its patterns. |

## Fetching the corpus

| file | does | writes |
|---|---|---|
| `sources.py` | `status` and `check` compare the manifest with the disk; `next` names the `drive_id`s to fetch; `land` turns a Drive result into a landed document without a model reading it; `fetch` fetches and lands straight from Drive. `land` shells out to `.venv-tools` for markitdown. | `land`, `fetch`: `Sources/drive/<slug>.md` and the row's checksums in the manifest |
| `duplicates.py` | Whether any landed document is a near-copy of another — the check that should keep saying none. | a cache, `Plan/derived/duplicates.json` |
| `dedupe.py` | Folds each group of near-copies down to one export, ranked first by whether anything already cites it, then by the source URLs it keeps. Dry run by default. | `--apply`: deletes the copies, moves their rows to `Sources/duplicates.jsonl` and the decision to `Plan/runs/dedupe.json` |
| `overview.py` | Every landed document with its most important names, counted and normalised to the wiki's page names through page surfaces and translation pairs; `scan` asks qmd for each page's name first. `doc <slug>` shows one document's weights. | the generated end of `Sources/README.md`; `scan`: `Plan/runs/qmd-scan/pages.json` |

## Asking the whole corpus

| file | does | writes |
|---|---|---|
| `derive.py` | Applies every rule in `rules/` to every landed document, cached by (document sha256, rule version). The first thing to run in a fresh container. | `Plan/derived/<slug>.json` |
| `corpus.py` | Counts, timelines, co-occurrence and the earliest or densest documents for a term, answered from the derived facts — counts and slugs, never document text. | — |
| `profile.py` | The structural profile of one document, the same probes in the same order for every document. `--frontmatter` prints a census header drawn from the manifest. | — |

## Reading one document

| file | does | writes |
|---|---|---|
| `capture.py` | Opens a document's run: profile and probes first, then — only once `03-candidates.md` has been written by hand — the counts. | `Plan/runs/<slug>/01-profile.txt`, `02-probes.txt`, `probes.json`, a `03-candidates.md` header if none exists; `--count`: `04-counts.txt`, `counts.json` |
| `read.py` | The document with every line prefixed by the file line a citation names. `--find "<words>"` answers with the citation, or refuses and names the nearest line. | — |
| `agree.py` | Two or more candidate lists of one document compared pairwise, as P27 says: F1, how much of each list the other holds, the terms one list holds only inside a longer surface of the other, and the forms a list writes that the document does not. `--names` prints who has what. | — |

## Reconciling against the wiki

| file | does | writes |
|---|---|---|
| `reconcile.py` | Pre-classifies a document's census against `Wiki/index.json`: new term, new reading, already there, or needs judgement. Then sweeps the document for every page surface the census does not list (decision 012). `--sweep-open` lists the hits in read documents that no reading and no row in `Plan/runs/sweep.jsonl` settles. | `Plan/runs/<slug>/reconcile-pre.json` |
| `judgements.py` | Replays every recorded one-term-or-two decision against `fold()`: agrees, DISAGREES, or still a person's call. | `Plan/runs/judgements.md`, re-rendered on every full run |
| `account.py` | The one verb: an account of a `document`, a `term`, a `pair`, the `corpus`, or the pipeline's `order` — the invariant that fails while any document is half-processed, and exits 1 when it does (`--summary`: one line). `selftest` builds each violation on purpose. | — |
| `digest.py` | What a reader needs of a page to add a reading: the lead, `## Where the sources differ`, `## Open`, one line per existing reading, and with `--doc` that document's readings whole — not the page. `--size` compares bytes. | — |
| `census.py` | Drafts a census where it is mechanical — frontmatter, structural profile, every candidate row with its counts, surfaces and count mark, the facts a reader must explain — and leaves two sections marked `<!-- reader:` for judgement. `check` fails on a mark left, a missing section, or a table row that is not, cell for cell, the one `draft` writes from `counts.json` and the document — counts, lines and surfaces, a row doubled or dropped; it reads only censuses it drafted. A candidate written with „…“ cites its quotation's line, so `quotes.py` checks it. | `Plan/runs/<slug>/census-draft.md` |
| `readings.py` | Turns reading files (`Plan/runs/<batch>/readings/<page>--<doc>.md`) into pages: places every `^[?]` by `read.py`'s comparison or refuses with the nearest lines, inserts by date (records: appended), appends difference lines. Refuses a file whose date or heading is not its document's (the heading is `## Reading —`, singular: the plural is counted by no frontmatter), whose document has no census, note or `reconcile-pre.json`, whose link points at no page, or whose quotation has no citation. Derives the frontmatter in memory and runs quotations, count marks, links, frontmatter, chapter rules and lint on the final text of every page, each reported apart; writes nothing if one fails. `check` writes nothing; `apply` also refuses while `Wiki/` has uncommitted changes. | the pages named in the reading files |
| `record.py` | Drafts a reconciliation's record where it is mechanical: `reconcile.json` and the compare page from the lookup (`reconcile-pre.json`, with the pages it ran against), the pages' `## Reading` sections and the lines each cites, the chapter pages, `plot.md`, the records' entries, the ledgers' rows, the state left and, with `.venv-dspy`, the decision sheets `askdb.py touches` finds. What stays judgement is marked `<reconciler: …>`. `check` compares a saved record with the pages; `measure` runs it over every record — documents 29–51: 19 of 23 agree, the rest drifted by later corrections. | `Plan/runs/<slug>/reconcile-draft.json`, `record-draft.md` |
| `brief.py` | The readings brief, drafted where it is mechanical: the documents with their dates and lengths (the manifest), the pages a reading may go on and the lines their surfaces stand on (`reconcile-pre.json` and `counts.json`), the sweep's hits, and the candidates that stand near a page's surface without being a reading. What only the reconciler can say — what each document is and how its readings must be worded, what it says about each page, which near matches are occurrences — is a `<brief: …>` mark, and `check` fails on a mark left or on a page that does not exist. A batch that skips a document number names it (`slug@59`). Standard library. | `Plan/runs/<batch>/brief-draft.md` |
| `crossdoc.py` | Cross-document retrieval for a reconciliation: for each page a document reads onto, the documents read onto it, the read ones that write its names and are not on it, and the unread ones that write them — whole-word counts from `corpus.py`, never a search rank — and three `P_BM25` lines each that share the page's words and write none of its names. `coverage` does it for every page and open record and ranks the unread documents touching most open records. Reads the shared store once, when it is fresh. | `Plan/runs/<slug>/crossdoc.json`, `crossdoc.md`; `coverage`: `Plan/runs/coverage-<date>/`; new relations into `Plan/runs/bm25/relations.jsonl` |
| `bm25rel.py` | The BM25 relation: a body line that shares a name's words without writing it — „Große Stille“ and „Das große Schweigen“ — kept as a `P_BM25` proposal the store's one build loads, judged `tension`, `parallel`, `same` or `noise` by a named reader, and ranked by a logistic model once `fit` has twelve verdicts of each kind, by the raw BM25 score until then. Refuses a stale store; leaves frontmatter lines out. | `Plan/runs/bm25/relations.jsonl`, `verdicts.jsonl`, `ranker.json` |
| `claims.py` | Every cited sentence of a note and of a census's two hand-written sections beside the line it cites: `draft` writes one row per citation — the sentence up to it, the line's opening words, code's cues that the line reports another source (`Das Protokoll …`, `Laut …`, `argumentiert`) or that the sentence calls something open — and the reader fills *who says it* and *holds?*; `check` fails on a dropped row, an empty cell or a value outside `document`/`source: <who>`/`yes`/`fixed`, and cautions where the line reports a source and the speaker is `document`; `show` prints each sentence with its whole line for a reviewer. Written after `quotes.py` could not see what the sentence around a quotation says. | `Plan/runs/<slug>/claims-draft.md`; the reader saves `claims.md` |
| `graphlab.py` | What each relation type is worth to retrieval, measured on the wiki's own 24 labelled cases (each retrieving its pages, its own node left out), and on a second set of 91: `diagnose` says whether a miss is a missing seed, an unreachable page or a page reached and outranked; `core` runs the seven stated types uniform, alone, one off and learned with cross-validation; `enrich` and `comention` add the relations the corpus supplies — co-occurrence and the counted co-mention relation, raw and normalised, sparsified and at every weight, with a leave-one-out choice; `hub` tries a degree correction of the walk; `he` adds the page pairs the HyperExtract contracts read; `links` asks the same of a second label set, the wiki's own `[[links]]` (91 pages, each seeded alone with its links removed), and lists the co-mentioned pairs no page links. Every configuration is a `baselines.jsonl` row, and each table gives the paired difference to the floor with a bootstrap interval. It decides no weight. | `Plan/runs/graph-lab-2026-09-30/`; `baselines.jsonl` |
| `lint_readings.py` | Lints reading sections and record entries: a comparison with another document whose paragraph cites none (a flag for the reviewer, never a failure), an empty code span, an empty quotation, a straight `"` between two quotations, a doubled space in prose, a `[…]` join across a line range. `--doc <slug>` limits it to one document's sections; `--strict` fails on any class but comparisons. | — |
| `runlog.py` | Records what a run costs: phases with the clock, each reader's model, tokens, tool uses and minutes as the Agent notification reports them (the last call's size, not the consumption — `Plan/runs/reader-lab-2026-09-30/transcripts.py` measures that), the transcript a reader row names (`--agent`), and every change the review makes to a reader's output, by class and, with `--document`, by document. Refuses an end with no start, a reader with no usage, an unclassed correction. `summary` says „not recorded" rather than 0. | `Plan/runs/<run>/run.jsonl`, `corrections.jsonl` |

## Links, graph and retrieval

| file | does | writes |
|---|---|---|
| `relations.py` | The page graph from `[[links]]`: broken links, orphans, open statements, and `--unmarked` mentions the markup does not mark. | — |
| `link.py` | Marks the links the prose already makes, and never inside a quotation, heading, blockquote or citation line. Dry run by default; `--only <page> …` limits a pass to a reading batch's own pages. | `--apply`: pages in `Wiki/candidates/` |
| `chapters.py` | The chapter pages in `Wiki/chapters/` (decision 013): checks each against its frontmatter, the read documents and its links; `overview` derives `Wiki/overview/chapters.md` from them; `missing` names every read document that writes `Kap N` with no reading on that chapter's page; `index N` lists the lines. | `overview`: `Wiki/overview/chapters.md` |
| `chapter_sources.py` | Navigation for the chapter pages: each chapter's questions — eight basic ones every author asks (`basic-questions.json`), then its own (`questions/kap-NN.json`), written first — asked of qmd's vectors one at a time, and the unread landed documents they return, fused by rank. `write` replaces each page's summary, `## Questions for this chapter`, `## Candidate sources` and `## Raw qmd answers` sections; `run --terms` asks the same of every term page into the run only. A hit is a place to look, never a reading or a number. | `Plan/runs/qmd-chapters-2026-09-26/` |
| `graph.py` | The typed knowledge graph — terms, documents, conflicts, questions — each edge carrying the file line that states it. Exports JSON, GraphML, triples or Mermaid. | — |
| `graph_export.py` | Human-readable graph atlas: term neighborhoods, source-reading/citation relationships, conflicts, questions, decision dependencies and targeted CLI recipes. No source passage dump, binary snapshot, import or restore. `kg.py export --check` writes nothing and fails when `Graph/` is not what an export would write (`drift`: stale, missing, orphaned pages). | generated Markdown under `Graph/` |
| `graph_export_selftest.py` | Offline fixtures for readable relationships, authority separation, no quote/row dump, output-only derivation, deterministic rendering and session startup. | temporary fixtures only |
| `kg.py` | Local GraphQLite CLI: atomically build the shared corpus/wiki graph and FTS store, freshness check, FTS5 evidence search, bounded Cypher neighbours, evidence IDs and byte-capped context using the existing personalized PageRank/MMR. Needs `.venv-graphqlite`; no model call. Its freshness check and evidence ids are `askdb.py`'s (`askdb.fresh`, `askdb.evidence_rows`), the store's one record. | `index`: disposable `Plan/derived/ask.db` |
| `kg_selftest.py` | Offline fixtures against the real GraphQLite extension: parallel edges, provenance, verified-only retrieval, freshness, atomic publication and context limits. Needs `.venv-graphqlite`. | temporary fixture databases only |
| `graphrag.py` | `ask`: a question in, verified quotations out, ranked by personalized PageRank over `graph.py`'s graph — never prose. `bench` scores retrieval against the wiki's own labels. `--comention W` (`ask` and `bench`, off) walks the counted co-mention relation of the shared store beside the stated ones at weight W: on the 24 cases recall@8 rises from 0.69 to 0.79 at W = 30 and to 0.75 leaving each case out (`graphlab.py comention`), a difference whose interval still includes zero. `--answer` needs `.venv-dspy` and the author's approval. | `bench --record`: `Plan/runs/baselines.jsonl` |
| `benchset.py` | The retrieval cases of `ask.bench_cases()`, frozen and hashed (`freeze`), so a score is read against a fixed answer; `check` proves the file (hash, gold lines inside landed bodies) and reports, without failing, how the live records drifted; `clusters` measures whether a held-out split exists (cases sharing gold documents). `cases()` is what every line-gold bench reads (`ask.py bench`, `novelgraph bench`/`rlm`, the evaluation audit): the frozen cases, refused if the file fails its hash; `live=True` (`ask.py bench --live`) reads the records. Standard library. | `freeze`: `Plan/eval/retrieval-cases-v<N>.json`, never rewritten |
| `askdb.py` | The store `ask` answers from: `Plan/derived/ask.db`, one SQLite file with a GraphQLite graph (`graph.py`'s nodes and edges with their `via` line, every landed document, chapters, the decision sheets; entity lists as `P_` proposals) and FTS5 tables over every source line and every verified quotation. `build`, `check`, `bm25`, `ppr`, `path`, `cypher`, `sheets` (the sheets' dependency graph: unlocks, cycles, missing), `touches <slug>` (document → pages and records that read or cite it → sheets naming them). The store records a hash of its inputs, code included, and of its content; `Store()` refuses a stale one. Needs `.venv-dspy`, so the std-only CI does not run its suite. | `Plan/derived/ask.db` |
| `ask.py` | Asks the sources a question (decision 017): routes by code, builds one pack for every backend, runs `claude-cli` (default), `route`, `session` or `jules`, places every quotation on its line or rejects it, and lands the rendered answer once in `Sources/ask/`, tier `M-ask`, where `subject.document` resolves it so it is cited like a source. Packs are immutable and a repeat is `--attempt N`; a quotation stands only on a line the pack sent. Pack recall on the 24 records is document 0.30, line 0.10 (`bench`; `--without` and `--with` ablate a finder, `--comention N` limits the co-mention finder, whose default fell from 40 to 10 paragraphs on 2026-09-30, `--pr-comention W` puts the counted co-mention relation into the walk that ranks pages, off; `--with he-lines --he-lines N` adds the lines the HyperExtract contracts read, off, +0.029 document recall at 40 lines where the contracts have read the gold; a result file's name ends with the store's hash): a placed answer is sound, not complete. Needs `.venv-dspy`. | `Plan/runs/ask/<id>/`, `Sources/ask/` |
| `askextract.py` | What `askdb.py build` extracts mechanically from every landed document: sections, paragraphs, lines with `NEXT` order, term mentions (the surface on the edge), chapter names, URLs, entity names, and learned hyperedges — `cooccur` (term sets per paragraph in 5+ documents, lift ≥ 1.5) and `parallel` (12-word shingles shared across documents) — and the counted `P_COMENTION` relation (page pairs that stand in one paragraph in two documents or more, with their documents and normalised PMI). Standard library. | into `Plan/derived/ask.db` |
| `aliases.py` | Alias learning for graph maintenance: which surfaces name one concept. Methods `fold`, `plural`, `gloss`, `bilingual`, `chars`, `context`, `vote`; `experiment` scores them on the judgement ledger and the never-merge canaries, `pages` on page-surface pairs; a threshold is the lowest with no false merge. Proposes, never merges. Needs `.venv-dspy`. | `Plan/runs/aliases-2026-09-30/` |

## Measuring and checking

| file | does | writes |
|---|---|---|
| `state.py` | Every number about the repository, measured. `--prose` fails on a number in any markdown that contradicts its measurement, `--check` on a drifted `Plan/state.json`, `--get KEY` prints one. | without a flag: `Plan/state.json` |
| `gold.py` | Which candidate lists are gold, by five criteria checked in code (decision 009): a list, not a reconstruction, counted, unchanged since its count, and at least 90% of its terms in the document. `<slug>` prints one list's evidence. `state.py`, `trainset.py` and both scorers ask it. | — |
| `goldeval.py` | Every automated reading of a gold document — HyperExtract contracts, entity lists, blind re-readings — scored against its gold list by `agree.compare`: recall, recall counting a gold term inside a longer surface, precision, precision counting a label one of whose parts is gold, and the extras split into verbatim and not in the text. `--by-doc`, `--extras <extractor>`, `--record` appends to `Plan/runs/gold-eval/runs.jsonl`. | — |
| `goldrel.py` | Gold relations: `Plan/runs/<slug>/03-relations.md`, one reader's definitions, contrasts and causes in the HyperExtract contracts' own ten types, written blind to every extractor. `check` holds when each row parses and its cited line holds its surfaces; `freeze` writes `relations.json`; `score` matches TermDefinitions, TermContrasts and CausalLinks rows by endpoint (fold or inside, contrasts unordered): recall, precision, type and line agreement. | — |
| `selftest.py` | Proves `quotes.py`, `read.py --find` and `fold()` can fail, each case carrying the exact defect it must name. | — |
| `selftests.py` | Runs every self-test in the repository, four at a time, one line each: held, FAILED, or not run. `run()` hands `ui.py` the same rows. | — |
| `check_skills.py` | Checks `.agents/skills/` against the agent-skills spec, and that each `.claude/skills/<name>` is a symlink to it. | — |

## Entity lists and language pairs — a model's proposals

| file | does | writes |
|---|---|---|
| `entities.py` | Verifies and searches the per-document entity lists in `Plan/entities/`. `place` turns a model's names into a list whose lines are found by code. | `place`: `Plan/entities/<slug>.md`; `matrix`: `Plan/derived/entities-matrix.json` |
| `bilingual.py` | German and English surfaces of one entity across the corpus: glosses the corpus states, found by code; Jev and free models for the rest. Needs `.venv-typesafe`; `--replay` reruns from the cache with no key and no network. | `Plan/runs/bilingual/`, `Plan/entities/bilingual.md` and `.jsonl` |
| `jev_entities.py` | A test of one route to an entity list: code finds every candidate and its line, Jev judges each. Needs `.venv-typesafe`; `--replay` as above. | `Plan/runs/jev/<slug>/` |

## Calling a model

No corpus text is sent to a model without the author's decision, and every model
step runs offline — a `--dry-run`, a `--replay`, or a `selftest`. The rule has
three encodings, `lmrun.py`, `rlm_ingest.py` and `route.py`, and decision 008
keeps them apart until one changes its rule and the others do not. The `dspy`
skill (`.agents/skills/dspy/`) is how to work with the DSPy ones.

| file | does | writes |
|---|---|---|
| `route.py` | One door for a third-party tool's model calls and for direct ones: free OpenRouter models only, the consent file naming which documents may be sent, every call recorded and replayable offline. `serve` is an OpenAI-compatible proxy a tool is pointed at; `guard <slug>` says whether a document's text would be refused. Jev calls need `.venv-typesafe`. | `Plan/runs/route/` — `ledger.jsonl`, `calls/`, `models.json` |
| `lmrun.py` | How `pairs.py` and `graphrag.py` call a model through DSPy: cache off, one record per call, a real model refused without `approval=`; `make_lm` builds `claude-cli/…`, `route/…` (a free model through `route.py`, pinned) or a LiteLLM string. Needs `.venv-dspy`. | `Plan/runs/<subject>/lm/<step>.jsonl` |
| `lm_fixture.py` | An offline `dspy.BaseLM`, and `offline()`, which also hides every API key and makes `litellm` refuse. Needs `.venv-dspy`. | — |
| `claude_lm.py` | Claude as a `dspy.BaseLM` through `claude -p`: no tools, no settings, no session, an empty working directory, thinking off unless asked; `lmrun.make_lm("claude-cli/haiku")` builds it (decision 011). Needs `.venv-dspy`. | — (the calls are recorded by `lmrun.py`) |
| `claude_cli.py` | One headless `claude -p` call, shut in an empty directory, thinking off, its JSON reply whole — the one encoding (P6) `claude_lm.py` and `he_claude.py` share, standard library only. | — |
| `he_claude.py` | HyperExtract's model: Claude through `claude -p` (decision 011), standard library only. `run <slug> <template>` is the pipeline's HyperExtract pass on one document after its census and note are frozen: `reading_extract.extract` on `hx.py`, then `stage` into `Plan/runs/<slug>/hyperextract/<run>/` with `calls.jsonl` and `usage.json`; list, set and graph templates. A German `„…"` a model closes with a straight quote is put back to `„…“` and counted. `selftest` runs the whole path with a fake `claude` and checks the message it is sent. | `Plan/runs/<slug>/hyperextract/<run>/` |
| `jules.py` | Spawns and drives a Google Jules session on a GitHub repository, ported from `netzkontrast/agency`: `dispatch` refuses without `--approval` and refuses a prompt that does not name `submit`; `plan`, `approve`, `activities`, `message`, `patch`; `verify` reads COMPLETED as done only when `git ls-remote` finds the branch, and `triage` says what a session's state means and what to do next. Standard library; `JULES_API_KEY` from the environment. | `Plan/runs/jules/ledger.jsonl` |
| `check_dspy_skill.py` | Asserts what the `dspy` skill teaches against the DSPy installed here: every parameter and default it writes down, one offline probe per behaviour it marks checked, every path it names. Needs `.venv-dspy`. | — |
| `check_dspy_surface.py` | Asserts each DSPy parameter this repository passes, by `inspect.signature`. Needs `.venv-dspy`. | — |
| `trainset.py` | The judgement ledger as labelled pairs, and the `fold()` baseline any model has to beat. | `--export`: `Plan/trainsets/` |
| `pairs.py` | One term or two: scores a rule (`fold`, or `plural`, decision 010), or a compiled program on what the rule leaves, and asks every candidate the never-merge canaries. `score` and `selftest` are standard library; `run` needs `.venv-dspy`. | `--record`: `Plan/runs/baselines.jsonl` |
| `baseline.py` | The append-only score ledger. `compare` fails a candidate that does not beat the floor, taken as the floor candidate's newest row on the same trainset. | `Plan/runs/baselines.jsonl`, for its callers |
| `rlm_ingest.py` | Reads one document with `dspy.RLM`, carrying this repository's skills. A real run needs `.venv-dspy` and `--approval`; `--selftest` is standard library. | `Plan/runs/<slug>/03-candidates-rlm.md` |
| `rlm_retrieval.py` | Bounded RLM retrieval trial on the two benchmark cases with no lexical seed (`C10`, `Q2`). Removes each case node so its gold edges cannot leak; validates page IDs against the graph. `search_quotes` finds cited evidence beyond the first six quotations on a page. `--selftest` and `--dry-run` are offline. A real run goes to Claude only (`claude-cli/haiku`, `--approval "decision 011"`); it prints a comparison but writes no wiki pages. The same agent over the chunk index is `novelgraph rlm`. | stdout only |

## Third-party extraction

| file | does | writes |
|---|---|---|
| `templates.py` | Checks the Hyper-Extract templates in `Plan/hyperextract/` against Hyper-Extract's validator, against loading them as `he parse` does, and against this project's rules — no line field, no model merge, the provisional header, no corpus name in a prompt. `selftest` shows each check failing on its defect. `parse` is `he parse` able to load a template by path, which the installed CLI cannot; only `parse` needs `he`. | — |

## Search

`setup_qmd.sh` installs qmd; it is under *Setting up a container*.

| file | does | writes |
|---|---|---|
| `qmd.py` | qmd from Python. A hit carries where to look, and `Hit.document()` hands it back to `subject.py`. | — |
| `qmd_coverage.py` | Which markdown no qmd collection covers — a file there is absent from every search. | — |

## The project app

| file | does | writes |
|---|---|---|
| `ui.py` | Derives the whole project into one interactive app — pages, conflicts, questions, the graph, the manifest, the invariants as they ran — as the files of a claude.ai Design canvas. `--check` reads them back the way the canvas does. | `Plan/derived/ui/` |
| `ui.html`, `ui.js` | The app's markup and its component logic. `ui.py` fills them with the data; nothing else reads them. | — |
