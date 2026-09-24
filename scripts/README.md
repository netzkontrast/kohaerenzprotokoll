# `scripts/` — every tool, by the job it does

Each row is the script's own first docstring line, or close to it; the script's
docstring says what it guarantees, and `CLAUDE.md` says how the tools fit
together. The standard-library scripts need no virtualenv. A script that needs
one says which — `.venv-dspy`, `.venv-typesafe` — and `scripts/install.sh`
builds it.

**This page is checked, not remembered.** 0 <!--state:readme.scripts_drift-->
files in `scripts/` are missing from it or listed here without existing, and
`python3 scripts/state.py --prose` fails the day that number is not 0.

## Sources — landing the corpus and knowing its shape

| script | what it does |
|---|---|
| `sources.py` | Manage the source corpus: fetch documents from Drive, land them, and see what is missing |
| `dedupe.py` | Fold each group of near-identical exports down to one file |
| `duplicates.py` | Whether any landed document is a near-copy of another |
| `subject.py` | The one place the corpus becomes addressable; every other script asks here |
| `profile.py` | Structural profile of one landed source document |
| `corpus.py` | Ask questions about every landed document without reading any of them |
| `derive.py` | Apply every rule to every document, once, into `Plan/derived/` |
| `rules/__init__.py` | The rule set — where this project's learned structure lives |
| `rules/attribution.py` | Where a document attributes a claim to something outside itself |
| `rules/export_damage.py` | What the Drive conversion did to the text, and what it costs a check |
| `rules/structure.py` | How the document is built: headings, tables, formulas, length |
| `rules/surfaces.py` | Every capitalised token, with its count and the file lines it appears on |

## Reading one document

| script | what it does |
|---|---|
| `read.py` | Hand the reader the document the way a citation will be checked; `--find` answers with the line |
| `capture.py` | Capture every artifact of an extraction run into `Plan/runs/<slug>/`, not only the finished census |
| `quotes.py` | Verify that every quoted passage still resolves to the line it cites |
| `entities.py` | Search every landed document for the entities a per-document model read named |
| `jev_entities.py` | Entity list by script plus Jev — a test of a route, not a pipeline step |
| `bilingual.py` | German and English names for the same entity, across the whole corpus |
| `rlm_ingest.py` | Read one document with `dspy.RLM`, carrying this repository's own skills |

## The wiki

| script | what it does |
|---|---|
| `wiki_index.py` | Build `Wiki/index.json` from page frontmatter, so reconciling never has to read the wiki |
| `reconcile.py` | Pre-classify a document's candidates against the wiki, without reading it |
| `judgements.py` | Replay every recorded judgement against the code that now claims to handle it |
| `account.py` | One operation: give an account of a subject |
| `relations.py` | What the wiki says relates to what, and what it says it does not know |
| `link.py` | Mark the links the prose already makes, without touching a single quotation |
| `graph.py` | The wiki as a typed knowledge graph, every edge carrying the line that states it |
| `graphrag.py` | Graph retrieval over the wiki: a question in, attributed evidence out, never an answer |

## Calling a model

The ones that call a model refuse to send corpus text without the author's yes
for that run. The `dspy` skill (`.agents/skills/dspy/`) is how to work with them.

| script | what it does |
|---|---|
| `lmrun.py` | Every DSPy model call goes through this, and leaves its evidence on disk |
| `lm_fixture.py` | An offline language model, so every model step can run with no key and no network |
| `route.py` | One door for every model call a tool makes — priced, consented and recorded before it is sent |
| `baseline.py` | The score of every program on every task, append-only, compared against a floor |
| `pairs.py` | One term or two — the harness every rule and every model is scored through |
| `trainset.py` | The judgement ledger as a trainset, and the baseline any model must beat |

## Checks

`python3 scripts/selftests.py` runs every suite, one line each; a suite that
could not run says `not run`, never `held`.

| script | what it does |
|---|---|
| `selftests.py` | Run every self-test in the repository, and report each one on its own line |
| `selftest.py` | Prove the checkers can fail, with defects whose exact shape is asserted |
| `state.py` | The repository's state, measured rather than remembered; `--prose` checks every marked number |
| `check_skills.py` | Validate the project's skills against the agent-skills spec, and against each other |
| `check_dspy_surface.py` | Assert the DSPy surface this repository calls, and fail loudly when it moves |
| `check_dspy_skill.py` | Assert what the `dspy` skill teaches, against the DSPy installed here |
| `templates.py` | Check Hyper-Extract templates against Hyper-Extract and against this project |

## Search

| script | what it does |
|---|---|
| `qmd.py` | Talk to qmd from Python, and hand what it finds to the tools that answer |
| `qmd_coverage.py` | Which markdown in this repository qmd can find, and which it cannot |
| `setup_qmd.sh` | Rebuild the qmd setup from nothing |

## Setup, and the project app

| script | what it does |
|---|---|
| `install.sh` | Install everything a fresh container lacks; the session-start hook runs it |
| `ui.py` | The whole project as one interactive app, derived into the files of a claude.ai Design canvas |
| `ui.html` | The app's markup, with the macros `ui.py` expands |
| `ui.js` | The app's component |
