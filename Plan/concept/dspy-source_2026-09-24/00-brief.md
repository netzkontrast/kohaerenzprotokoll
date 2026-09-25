# Brief — read one slice of DSPy 3.3.1 or GEPA 0.1.4 itself, and say what the `dspy` skill lacks

You are one of nine readers. Each reads one slice of the **primary sources** —
the DSPy and GEPA code this repository has installed, their tests and their
official documentation. Your slice, your map and your output file are in your
task.

## Why this read, when a skill already exists

`/home/user/kohaerenzprotokoll/.agents/skills/dspy/` teaches DSPy to this
repository. It was built on 2026-09-24 from **nine third-party repositories**
that use DSPy, and its claims were checked against the installed package where a
probe could run. Nobody has read DSPy itself, or its documentation, end to end.
The author asked for „all there is about dspy". Your job is to extract **all the
knowledge in your slice** and to say, precisely, **where the skill is missing it,
states it wrongly, or states it without a check**.

## The target, in 12 lines

`/home/user/kohaerenzprotokoll` turns a German research corpus into a wiki of term
pages by a heavily checked, mostly manual process. Standard-library scripts do
everything decidable. DSPy 3.3.1 is pinned in `.venv-dspy` (Python 3.11), with
GEPA 0.1.4. The DSPy toolchain that exists there:

- `scripts/lmrun.py` — every DSPy model call: `cache=False`, one JSONL record per call, status `answered|refused|unparsed|unreachable` (never a score), a real LM refused without `approval=`.
- `scripts/lm_fixture.py` — offline `FixtureLM(dspy.BaseLM)`, `fill()`, `offline()` that hides `*_API_KEY` and makes `litellm.completion` raise.
- `scripts/baseline.py` — append-only ledger `Plan/runs/baselines.jsonl`; a candidate must beat a floor; a `vetoed` row fails.
- `scripts/pairs.py` — the one optimizer ladder: „one term or two" over 63 labelled surface pairs; a deterministic rule first, a model only on its residual, a never-merge canary veto, stratified folds, repeats; `LabeledFewShot → BootstrapFewShot → InferRules → SIMBA → GEPA`; a five-argument metric returning `dspy.Prediction(score, feedback)`.
- `scripts/rlm_ingest.py` — `dspy.RLM` reads one document, with tools `find_line` and `count`.
- `scripts/graphrag.py` — retrieval over the wiki graph; `--answer` lets a model choose evidence numbers only.
- `scripts/check_dspy_surface.py` asserts the DSPy parameters the scripts pass; `scripts/check_dspy_skill.py` asserts what the skill teaches (its `surface` blocks and its `[checked: <id>]` probes).

Principles that decide what the skill may teach (`PRINCIPLES.md`): anything
decidable is a program (P1); every workflow has an offline, no-key fixture (P5);
a model never types an identifier or line number — code does (P26); never merge
two sources' readings (P13); „never reached" is not „answered badly" (P15);
repeats with the cache off (P18); assert non-empty output and the language (P19);
a guard reports what it could not check (P23). **No corpus text leaves the
container without the author's yes for that run.**

## The sources

| what | where |
|---|---|
| DSPy 3.3.1, the git tag | `<src>/dspy-3.3.1/` — `dspy/` (the package), `tests/`, `docs/docs/` (the official documentation) |
| DSPy 3.3.1, installed | `/home/user/kohaerenzprotokoll/.venv-dspy/lib/python3.11/site-packages/dspy/` — identical to the tag's `dspy/` except `__metadata__.py` (checked with `diff -rq`) |
| GEPA 0.1.4, the git tag | `<src>/gepa-0.1.4/` — `src/gepa/`, `tests/`, `docs/docs/`, `examples/`, `README.md` |
| GEPA 0.1.4, installed | `.venv-dspy/lib/python3.11/site-packages/gepa/` — identical to `src/gepa/` in its Python files |

`<src>` is `/tmp/claude-0/-home-user-kohaerenzprotokoll/a2e3b1c0-0873-50c6-be3a-bb4d50bd8e11/scratchpad/src`.
**Cite paths relative to the tag's root**, e.g. `dspy/teleprompt/simba.py:120`,
`docs/docs/api/modules/RLM.md:40`, `gepa:src/gepa/optimize_anything.py:300`.

## Your map

Your task names one or more files of the skill under
`/home/user/kohaerenzprotokoll/.agents/skills/dspy/`. **Read them first**, fully.
They are what this repository already believes. Then read your slice **fully** —
every file in it, code and tests included, not excerpts; docs notebooks may be
skimmed past their output cells.

## Output — one Markdown file, the path given in your task

### 1. Header
Slice, files read (count and lines), what you ran to verify, and in ≤5 lines what
this part of DSPy/GEPA is.

### 2. Knowledge items, under these headings (exactly these; omit empty ones)

`## API` · `## OPT` · `## MET` · `## DATA` · `## RLM` · `## RAG` · `## AGENT` ·
`## PROD` · `## TEST` · `## PAT` · `## SKILL` · `## TRAP`

(the same headings the skill's evidence notes use: API = signatures, fields,
types, modules, adapters, LM config, cache, history, Example/Prediction, save/load,
callbacks, async/streaming, tools; OPT = optimizers; MET = metrics and evaluation;
DATA = datasets and splits; RLM = `dspy.RLM` and long context; RAG = retrieval;
AGENT = ReAct, tools, MCP, memory, History; PROD = cache, cost, tracing, logging,
serving, errors, security; TEST = offline testing; PAT = patterns; SKILL =
optimizing text artifacts such as `SKILL.md`; TRAP = silent defaults, checks that
cannot fail, documented behaviour the code does not have).

Each item is one bullet:

`- **<short name>** — <statement: exact names, parameters, defaults, numbers and
their conditions>. <evidence: path:line or path:start-end> [api|recipe|number|trap|pattern|claim]
(verified: <what you ran, or "read">) · skill: <new | wrong: <file> says … | unchecked: <file> | same>`

The last field is the point of this read: **new** — the skill does not have it;
**wrong** — the skill says something the source contradicts, quote the skill;
**unchecked** — the skill has it but no probe or surface block holds it;
**same** — already there and held (list these briefly; do not pad).
`[claim]` means the documentation asserts it and you could not verify it in code.
Where docs and code disagree, the code wins and the disagreement is a `TRAP`.
Small facts count: a default, an error message, an ordering constraint, a renamed
parameter, a deprecation. One item per distinct fact. Be exhaustive — the author
of the skill will select; they cannot select what you did not write down.

### 3. `## Code worth keeping`
Verbatim snippets (≤40 lines each) the skill should show — each with
`path:start-end` and whether you ran it on the installed package.

### 4. `## Probes worth adding`
Behaviours the skill should hold with a `[checked: <id>]` mark. For each: a
proposed id (lowercase, hyphens), the sentence the skill would carry, and a
self-contained offline probe — a Python function that returns `None` when the
behaviour holds and a string naming the failure when it does not — that you
**ran** on `.venv-dspy/bin/python` and saw hold. Use
`sys.path.insert(0, "/home/user/kohaerenzprotokoll/scripts"); from lm_fixture import FixtureLM, chat, fill, offline`
for any LM (read `scripts/lm_fixture.py` first), or `dspy.utils.DummyLM`.

### 5. `## Surface worth asserting`
Call-shaped lines for the skill's `surface` blocks, e.g.
`dspy.SIMBA(metric, bsize=32, num_candidates=6, max_steps=8)` — every parameter
and default taken from `inspect.signature` on the installed package, which you ran.

### 6. `## Ten things the skill must say`
The ten most important items from your slice for **this** repository, one line
each, pointing at the item.

## Rules

- **Do not modify any repository.** Write only your one output file. Scratch
  files go under `<src>/../readers/<your-slice>/`.
- **Line numbers must be real.** Get them with `grep -n`, `sed -n` or `nl`. If
  unsure, cite the file without a line. Never invent one.
- **Offline only.** Prefix every command that runs Python with
  `env -u OPENROUTER_API_KEY -u TYPESAFE_API_KEY -u OPENAI_API_KEY -u ANTHROPIC_API_KEY`.
  Never configure a real LM; use the fixture. Do not run the DSPy or GEPA test
  suites wholesale — read them; run a single test only if it needs no network
  and no package that is not installed. Never `pip install` into the system
  Python or into `.venv-dspy`; if you need a package, use `uv run --with …` in a
  scratch directory. Skip anything that takes more than 3 minutes.
- Web access only if your task says so, and then only to read public pages.
- English. German only inside quotations.
- No padding, no praise. If something is broken, does not run, or contradicts
  its documentation, say so.
- Length: as long as the knowledge needs — 500–1500 lines is normal for a slice.
- When finished, reply with the output path and a 5-line summary only.
