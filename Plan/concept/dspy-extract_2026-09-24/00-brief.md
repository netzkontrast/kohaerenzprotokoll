# Brief — extract ALL DSPy knowledge from one slice, for a skill in kohaerenzprotokoll

You are one of nine readers. Each reads one slice of the nine DSPy repositories
cloned under `/home/user/`. Your slice, output file and commit are in your task.

## The target, in 12 lines

`/home/user/kohaerenzprotokoll` turns a German research corpus into a wiki of term
pages by a heavily checked, mostly manual process. Standard-library scripts do
everything decidable. DSPy 3.3.1 is pinned. The DSPy toolchain that exists there:

- `scripts/lmrun.py` — every model call: `cache=False`, one JSONL record per call, status `answered|refused|unparsed|unreachable` (never a score), a real LM refused without `approval=`.
- `scripts/lm_fixture.py` — offline `FixtureLM(dspy.BaseLM)`, `fill()`, `offline()` that hides `*_API_KEY` and makes `litellm.completion` raise.
- `scripts/baseline.py` — append-only ledger `Plan/runs/baselines.jsonl`, compare against a floor, a `vetoed` row fails.
- `scripts/pairs.py` — job 1 "one term or two" (57 labelled surface pairs, `fold()` rule decides 33): rule first, model on residual, canary veto, stratified folds, repeats, ladder `LabeledFewShot → BootstrapFewShot → InferRules → SIMBA → GEPA`, five-argument metric returning `dspy.Prediction(score, feedback)`.
- `scripts/rlm_ingest.py` — job 3, `dspy.RLM` reads one document; tools `find_line`, `count`; verification tiers (cited line holds the term; reach); `--approval` required.
- `scripts/graphrag.py` — retrieval over the wiki graph: personalized PageRank, MMR with a relevance floor, `--answer` lets a model pick evidence numbers only.
- `scripts/check_dspy_surface.py` (asserts the DSPy params the repo passes), `scripts/check_skills.py` (skill frontmatter spec), `scripts/trainset.py`.
- Job 2: entity lists (model names entities, code places lines). Job 4: optimize SKILL.md descriptions with `gepa.optimize_anything`.

Principles that decide what the skill may teach (from `PRINCIPLES.md`): anything
decidable is a program (P1); every workflow has an offline, no-key fixture (P5); a
model never types an identifier or line number — code does (P26); never merge two
sources' readings (P13); "never reached" ≠ "answered badly" (P15); repeats with the
cache off (P18); assert non-empty output and the language (P19); a guard reports
what it could not check (P23); score against the human ceiling (P27). You do not
need to read more of the target than this.

## What exists already, and why you are reading again

On 2026-09-23 readers wrote idea-reports into
`/home/user/kohaerenzprotokoll/Plan/concept/dspy-repos_2026-09-23/<repo>.md`. They
list *ideas for the target*, tagged adopt/adapt/catalogue/skip. **Your job is
different and deeper: extract ALL KNOWLEDGE in your slice** — every fact, API
detail, parameter and default, recipe, measured number with its conditions, trap,
pattern, and documented mistake — so that a skill can teach DSPy from it. Read the
old report for your repo first as a map (for dspy-agent-skills: `dspy-agent-skills-A.md`
covers the non-book skills, `-B.md` the book skills), then read your slice **fully**
(every file in it, code included, not excerpts), and say where the old report is
wrong or incomplete.

## Output — one Markdown file, the path given in your task

### 1. Header
Repo, commit (given in your task), license, DSPy version targeted (and whether its
API usage still holds for 3.3.1), what it is in ≤5 lines, and what you ran to verify.

### 2. Knowledge items, grouped under these topic headings (exactly these, omit empty ones)

- `## API` — DSPy core: signatures, fields, types (Literal, Pydantic, list…), instructions, modules (Predict, ChainOfThought, ReAct, ProgramOfThought, CodeAct, Refine, BestOfN, Parallel…), adapters, `dspy.LM` config, cache, history, usage tracking, Example/Prediction, Evaluate, save/load, callbacks, async/streaming, tools
- `## OPT` — optimizers: constructor and `compile()` parameters, data needs, cost, measured results, selection rules, gotchas
- `## MET` — metrics and evaluation: contracts, feedback, judges and their calibration, rubrics, "could not score", aggregation
- `## DATA` — datasets: conversion, `with_inputs`, splits, tiers, hard negatives, synthetic data, sizes
- `## RLM` — `dspy.RLM` and long-context work
- `## RAG` — retrieval, reranking, MMR, RAG shapes, knowledge graphs
- `## AGENT` — ReAct, tools, MCP, memory, sessions, `dspy.History`, multi-turn, planning
- `## PROD` — cache hardening, cost/usage, tracing, logging, serving, fallbacks, security
- `## TEST` — offline testing: mock LMs, dry-runs, surface checks, regression tests
- `## PAT` — patterns built on DSPy: review, critique→repair, dialectics, wiki compile, planning graphs, prompting techniques
- `## SKILL` — optimizing skills and other text artifacts (SKILL.md, descriptions, `optimize_anything`)
- `## TRAP` — defects found: checks that cannot fail, claims never measured, silent defaults, live calls in tests, code that does not run

Each item is one bullet:

`- **<short name>** — <statement: exact names, parameters, defaults, numbers and their conditions>. <evidence: path:line or path:start-end, all locations if repeated> [api|recipe|number|trap|pattern|claim] (verified: <what you ran>) → here: <target script or job, if any>`

`[claim]` = the repo asserts it and you could not verify it. Quote key sentences
exactly („…" with path:line). Small facts count: a default, an error message, an
ordering constraint, a renamed parameter. One item per distinct fact. Be exhaustive —
the skill author will select; they cannot select what you did not write down.

### 3. `## Code worth keeping`
Verbatim snippets (≤40 lines each) a skill should show — metric shapes, mock LMs,
selection functions, guards — each with `path:start-end` and whether it runs on
DSPy 3.3.1 (say how you know).

### 4. `## The old report, corrected`
Where the 2026-09-23 report for your repo is wrong or missed something.

### 5. `## Ten things the skill must say`
The ten most important items from your slice, one line each, pointing at the item.

## Rules

- **Do not modify any repository.** Write only your one output file.
- **Line numbers must be real.** Get them with `grep -n` / `sed -n` / `nl`. If unsure,
  cite the file without a line. Never invent one.
- **Offline only.** Prefix every command that runs a repo's Python with
  `env -u OPENROUTER_API_KEY -u TYPESAFE_API_KEY -u OPENAI_API_KEY -u ANTHROPIC_API_KEY`.
  An earlier scan's unmocked test made a live OpenRouter call; that must not happen
  again. Never `pip install` into the system Python — use `uv run --with …` or a
  venv inside `<scratchpad>/venvs/`.
  A shared DSPy 3.3.1 interpreter may exist at `/home/user/kohaerenzprotokoll/.venv-dspy/bin/python`
  (read-only use; do not install into it). Skip anything that takes more than 3 minutes.
- English. German only inside quotations.
- No padding, no praise. If something is broken or does not run, say so.
- Length: as long as the knowledge needs — 400–1200 lines is normal for a large slice.
- When finished, reply with the output path and a 5-line summary only.
