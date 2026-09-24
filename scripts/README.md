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
| `dedupe.py` | Folds each group of near-copies down to one export, ranked by the source URLs it keeps. Dry run by default. | `--apply`: deletes the copies, moves their rows to `Sources/duplicates.jsonl` and the decision to `Plan/runs/dedupe.json` |

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
| `reconcile.py` | Pre-classifies a document's census against `Wiki/index.json`: new term, new reading, already there, or needs judgement. | `Plan/runs/<slug>/reconcile-pre.json` |
| `judgements.py` | Replays every recorded one-term-or-two decision against `fold()`: agrees, DISAGREES, or still a person's call. | `Plan/runs/judgements.md`, re-rendered on every full run |
| `account.py` | The one verb: an account of a `document`, a `term`, a `pair`, the `corpus`, or the pipeline's `order` — the invariant that fails while any document is half-processed. | — |

## Links, graph and retrieval

| file | does | writes |
|---|---|---|
| `relations.py` | The page graph from `[[links]]`: broken links, orphans, open statements, and `--unmarked` mentions the markup does not mark. | — |
| `link.py` | Marks the links the prose already makes, and never inside a quotation, heading, blockquote or citation line. Dry run by default. | `--apply`: pages in `Wiki/candidates/` |
| `graph.py` | The typed knowledge graph — terms, documents, conflicts, questions — each edge carrying the file line that states it. Exports JSON, GraphML, triples or Mermaid. | — |
| `graphrag.py` | `ask`: a question in, verified quotations out, ranked by personalized PageRank over `graph.py`'s graph — never prose. `bench` scores retrieval against the wiki's own labels. `--answer` needs `.venv-dspy` and the author's approval. | `bench --record`: `Plan/runs/baselines.jsonl` |

## Measuring and checking

| file | does | writes |
|---|---|---|
| `state.py` | Every number about the repository, measured. `--prose` fails on a number in any markdown that contradicts its measurement, `--check` on a drifted `Plan/state.json`, `--get KEY` prints one. | without a flag: `Plan/state.json` |
| `gold.py` | Which candidate lists are gold, by five criteria checked in code (decision 009): a list, not a reconstruction, counted, unchanged since its count, and at least 90% of its terms in the document. `<slug>` prints one list's evidence. `state.py`, `trainset.py` and both scorers ask it. | — |
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
| `lmrun.py` | How `pairs.py` and `graphrag.py` call a model through DSPy: cache off, one record per call, a real model refused without `approval=`. Needs `.venv-dspy`. | `Plan/runs/<subject>/lm/<step>.jsonl` |
| `lm_fixture.py` | An offline `dspy.BaseLM`, and `offline()`, which also hides every API key and makes `litellm` refuse. Needs `.venv-dspy`. | — |
| `check_dspy_skill.py` | Asserts what the `dspy` skill teaches against the DSPy installed here: every parameter and default it writes down, one offline probe per behaviour it marks checked, every path it names. Needs `.venv-dspy`. | — |
| `check_dspy_surface.py` | Asserts each DSPy parameter this repository passes, by `inspect.signature`. Needs `.venv-dspy`. | — |
| `trainset.py` | The judgement ledger as labelled pairs, and the `fold()` baseline any model has to beat. | `--export`: `Plan/trainsets/` |
| `pairs.py` | One term or two: scores a rule (`fold`, or `plural`, decision 010), or a compiled program on what the rule leaves, and asks every candidate the never-merge canaries. `score` and `selftest` are standard library; `run` needs `.venv-dspy`. | `--record`: `Plan/runs/baselines.jsonl` |
| `baseline.py` | The append-only score ledger. `compare` fails a candidate that does not beat the floor, taken as the floor candidate's newest row on the same trainset. | `Plan/runs/baselines.jsonl`, for its callers |
| `rlm_ingest.py` | Reads one document with `dspy.RLM`, carrying this repository's skills. A real run needs `.venv-dspy` and `--approval`; `--selftest` is standard library. | `Plan/runs/<slug>/03-candidates-rlm.md` |
| `rlm_retrieval.py` | Bounded RLM retrieval trial on the two benchmark cases with no lexical seed (`C10`, `Q2`). Removes each case node so its gold edges cannot leak; validates page IDs against the graph. `--selftest` and `--dry-run` are offline. A real run needs a model key and `--approval`; it prints a comparison but writes no wiki pages. | stdout only |

## Third-party extraction

| file | does | writes |
|---|---|---|
| `templates.py` | Checks the Hyper-Extract templates in `Plan/hyperextract/` against Hyper-Extract's validator, against loading them as `he parse` does, and against this project's rules — no line field, no model merge, the provisional header, no corpus name in a prompt. `selftest` shows each check failing on its defect. Needs `he`. | — |

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
