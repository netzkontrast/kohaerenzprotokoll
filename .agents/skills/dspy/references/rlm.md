# dspy.RLM and long-context reading

## Three things called "RLM"

- The academic idea `dspy.RLM` implements: "Recursive Language Models" (Zhang,
  Kraska, Khattab, 2025) — an outer model that treats a long context as a
  variable in a code environment instead of as prompt text (`dspy:predict/rlm.py:1-9`).
- **`dspy.RLM`**, the DSPy 3.3.1 module this file documents, used by
  `scripts/rlm_ingest.py`. It is marked `@experimental`, which injects
  "Experimental: This class may change or be removed in a future release
  without warning." into its own docstring (`dspy:predict/rlm.py:115`,
  `dspy:utils/annotation.py:53-56`).
- A third, unrelated thing: before this repository adopted `dspy.RLM`, a
  different, non-DSPy reference implementation (`pip install rlms`) was read
  once, on 2026-09-17, for a corpus-scale idea that was never built. It is not
  installed, nothing in `scripts/` depends on it, and it is history, not
  mechanism — see *Not taken, or waiting*.

Only the second exists in this repository. The rest of this file is about it.

## In this repository — `scripts/rlm_ingest.py`

`rlm_ingest.py` reads one landed document with `dspy.RLM`, carrying this
repository's own `ingest` skill instructions into the model's task, and writes
one candidate list. Three pieces, and the joins between them are the point
(`scripts/rlm_ingest.py`):

- **`dspy_skills`** loads `.agents/skills/` the way Claude Code does:
  `SkillManager` discovers every skill, renders the `<available_skills>` block
  from the `description` field alone, and `activate` reads one skill's full
  `SKILL.md`. `briefing()` calls it (`scripts/rlm_ingest.py`), so the
  model reading the document is handed the same `ingest` instructions a person
  here follows, from the same file, with no second copy to drift.
- **`dspy.RLM`** runs the reading inside a sandboxed REPL. That matters more
  than context length here: a census is counting, and a model that can
  *compute* over the text — count a word, resolve a line — does not have to be
  believed about the answer.
- **`scripts/read.py`** supplies the document already prefixed `NNN| `
  (`numbered()`, `scripts/rlm_ingest.py`). Left to count for itself the
  model reported 690 lines where this project counts 691 — the two-line-bases
  trap, frontmatter against file. Handing it the numbering removes the
  question instead of hoping.

```bash
.venv-dspy/bin/python scripts/rlm_ingest.py <slug> --approval "<decision>" \
    [--model M] [--iters N] [--calls N] [--sub-model M]
.venv-dspy/bin/python scripts/rlm_ingest.py <slug> --score      # against the human list
python3 scripts/rlm_ingest.py --selftest                        # tools and reach, offline
```

Defaults: `--model openrouter/nvidia/nemotron-3-super-120b-a12b:free`,
`--iters 12`, `--calls 40` (this is `max_llm_calls`), `--sub-model` none
(`scripts/rlm_ingest.py`). The default model is free and answers a
structured-output request — "18 of the 24 free models on OpenRouter do not,
and `RLM` needs one, so the choice is narrower than it looks." The first
default, `nex-agi/nex-n2.5-pro:free`, returns its final answer inside
`reasoning_content` with `text: None`, which DSPy's adapter rejects as an
empty response (`scripts/rlm_ingest.py`).

**`--approval` is a hard `SystemExit` gate, not a convention.** With none
given, `run()` refuses before building any `dspy.LM`: "this sends a whole
corpus document to OpenRouter. Name the author's decision that allows it"
(`scripts/rlm_ingest.py`). Unlike every other model-calling step here,
`run()` does **not** go through `lmrun.call` — it builds `dspy.LM(model,
api_key=..., api_base=..., cache=False)` itself and calls `dspy.RLM` directly:

```python
rlm = dspy.RLM("document: str, task: str -> candidates: str",
               max_iters=iters, max_llm_calls=calls,
               tools=tools_for(slug), sub_lm=sub)
```

(`scripts/rlm_ingest.py`). It therefore never writes an `lmrun`
per-call JSONL record; the header of its own output file is the record it
keeps instead.

**Every header field, in `Plan/runs/<slug>/03-candidates-rlm.md`:**

| field | what it means |
|---|---|
| `written_by:` | `dspy.RLM, model <m>, <n> iterations, <s>s — <verdict>`. The verdict clause is `judge()`'s string. `scripts/state.py`'s `trainset.gold_candidate_lists` measure reads a `written_by:` line to tell a reader's list from a reconstruction — but only on files named `03-candidates.md` (below), so this file is excluded from that glob before the line is ever read |
| `ran:` | today's date |
| `verified:` | tier 1 — `good` of `total` candidates whose cited line, checked by the same comparison `quotes.py` uses, actually contains the term (`verified()`, `scripts/rlm_ingest.py`) |
| `reach:` | tier 2 — the furthest verified citation's line as a share of the document's own span, and how many of ten equal-width "tenths" of that span at least one verified citation falls in (`reach()`, `scripts/rlm_ingest.py`) |
| `forced:` | tier 3 — `yes`/`no`, whether `max_iters` ran out and DSPy extracted the answer from the trajectory instead of the model submitting it (see *Failure modes*) |
| `cost:` | token usage from `dspy.track_usage()`, per model |
| `approval:` | the `--approval` string verbatim |

The body lists the verified candidates, then `## Unverified` (cited line does
not hold the term), `## Uncited` (no line given at all), and `## The model
said it did not read:` (any `- UNREAD …` line the model wrote itself)
(`scripts/rlm_ingest.py`). `judge()` turns the three tiers into one
verdict, forced beating everything else (`scripts/rlm_ingest.py`).

**`--score`** compares the model's file against a reader's `03-candidates.md`
through `drg.evaluation._runner._score_sets`, keyed by this project's own
`fold()` (`scripts/rlm_ingest.py`). It raises `SystemExit` if either
file is missing or `drg-kg` is not installed in that interpreter. It prints
precision/recall/F1 and both difference lists by name, then the same P27
caveat the code itself states: "A miss is not automatically an error and an
invention is not automatically wrong: the reader's list is one reader. Two
independent readings of one document differed by 109 against 143 candidates"
(`scripts/rlm_ingest.py`).

**`--selftest`** runs under plain `python3` — it never imports `dspy` — and
checks six offline cases with no model and no key: `find_line` on real words,
its refusal on absent ones, `count`, `reach` separating an early-only set from
a full-coverage one, and `judge()` on a forced case versus a complete one
(`scripts/rlm_ingest.py`).

**What it may not do** (`scripts/rlm_ingest.py`):

- **Write `03-candidates-rlm.md`, never `03-candidates.md`.** "The gold list
  is written by a reader while reading; a model's list is the thing gold is
  used to score, and the two must never be able to become each other." Two
  guards enforce it, not one: the filename keeps `state.py`'s glob from ever
  matching the model's file, and `written_by:` is the second, in-file check.
- **Propose and stop.** No page, no judgement, no conflict, no census is
  written from here — those are decisions, and an ingest proposes rather than
  resolves.

## Installing the sandbox

`dspy.RLM`'s default `interpreter_factory` needs Deno. Installed DSPy 3.3.1
declares the extra `deno<3.0.0,>=2.4.5; extra == "deno"` in its own package
metadata (verified in `.venv-dspy` here, 2026-09-24). This repository's line:

```bash
uv venv --python 3.11 .venv-dspy
uv pip install --python .venv-dspy/bin/python 'dspy[deno,numpy]==3.3.1'   # numpy: SIMBA; deno: dspy.RLM
```

**`which deno` can read empty while `dspy.RLM` still runs.**
`_find_deno_executable()` prefers the Deno binary the `deno` PyPI package
manages (`from deno import find_deno_bin`) over anything on `PATH`, and falls
back to `shutil.which("deno")` only if that import fails
(`dspy:primitives/python_interpreter.py:84-94`). Verified in this
container: `deno` 2.9.7 is installed as a Python package inside `.venv-dspy`,
its binary sits at `.venv-dspy/bin/deno`, the system `which deno` is empty,
and `dspy.RLM` runs anyway. The runtime check is looser than the pip pin —
`MIN_DENO_VERSION = (2, 0, 0)`, `MAX_DENO_VERSION = (3, 0, 0)` exclusive, so
any Deno `2.x` passes (`dspy:primitives/python_interpreter.py:39-41,124-138`).
Without a working Deno at all: `CodeInterpreterError: Unable to determine the
Deno version from 'deno'. PythonInterpreter requires Deno >=2.0.0,<3.0.0.
Install a compatible runtime with pip install "dspy[deno]", or pass a custom
deno_command.` (`dspy:primitives/python_interpreter.py:124-138`).

**A cold sandbox needs network once, for the sandbox itself, not for the
model.** The bundled runner fetches Pyodide from npm and a small std-io
module from deno.land on first start:

```
import pyodideModule from "npm:pyodide@0.29.4/pyodide.js";
import { readLines } from "https://deno.land/std@0.186.0/io/mod.ts";
```

(`dspy:primitives/runner.js:3-4`). After that the Deno cache is warm and
later starts need no network. Measured by the `dspy-agent-skills` reader in
its own container, 2026-09-24, warm cache, no real LM: a fresh interpreter
start plus first execution took 2.9s, and a whole 6-iteration scripted RLM run
took 3.3s (`dspy-agent-skills`'s own real-sandbox measurement; not re-timed
here). A `PythonInterpreter` instance is single-thread: reusing one from a
second thread raises `RuntimeError("PythonInterpreter is not thread-safe and
cannot be shared across threads. ...")` (`dspy:primitives/python_interpreter.py:391`).

## The module

Every parameter `dspy.RLM(...)` takes, precisely (`dspy:predict/rlm.py:139-166`;
asserted against the installed package by `api.md`'s `surface` block and
pinned narrower by `check_dspy_surface.py:38-39`, which asserts only the five
names `rlm_ingest.py` actually passes — `signature`, `max_iters`,
`max_llm_calls`, `tools`, `sub_lm`):

| parameter | default | what it is |
|---|---|---|
| `signature` | required | a DSPy signature, string or class; every input/output name is fixed by it |
| `max_iters` | `20` | outer REPL iterations; each is one `generate_action` (reasoning + code) call |
| `max_llm_calls` | `50` | sub-LM budget for `llm_query`/`llm_query_batched` **only**, reset fresh every `forward()` |
| `max_output_chars` | `10_000` | truncates only what a step's *printed output* shows the outer LM, head+tail; the stored trajectory keeps the full text |
| `verbose` | `False` | logs each iteration's reasoning/code/output to **stderr**, through the `dspy.predict.rlm` logger — not stdout |
| `tools` | `None` | a **list** of callables or `dspy.Tool` — a dict raises `TypeError`; a duplicate name raises `ValueError` |
| `sub_lm` | `None` | the model `llm_query`/`llm_query_batched` calls; falls back to `dspy.settings.lm` at call time, and raises `dspy.LMNotConfiguredError` if neither is set |
| `interpreter_factory` | `PythonInterpreter` | a zero-argument callable building a fresh sandbox per `forward()`; DSPy shuts down every interpreter it creates |

`rlm_ingest.py` overrides only `max_iters`, `max_llm_calls`, `tools` and
`sub_lm` — it takes the defaults for `max_output_chars`, `verbose` and
`interpreter_factory`.

**`max_iters` and `max_llm_calls` cap different things, and confusing them
costs a run.** `max_iters` bounds the outer loop, shown to the model as
`f"{iteration+1}/{self.max_iters}"` (`dspy:predict/rlm.py:680`).
`max_llm_calls` bounds only calls the sandboxed *code* makes through
`llm_query`/`llm_query_batched` — checked and incremented **before** the
sub-call runs (`dspy:predict/rlm.py:263-274`). It does not count the
outer action calls, and it does not count the one `extract` call a forced
ending makes. **Worst case per `forward()` is therefore `max_iters` action
calls + 1 extract call + `max_llm_calls` sub-calls, plus an adapter retry for
each unparsable action** — the note this repository read from
`dspy-agent-skills` found its own skill's `reference.md:43` calls
`max_llm_calls` a "hard cap across the whole RLM invocation," which does not
hold (`dspy-agent-skills:skills/dspy-rlm-module/reference.md:43`, corrected
against `dspy:predict/rlm.py:261-325,543-562`).

`forward(self, interpreter: CodeInterpreter | None = None, /, **input_args) ->
Prediction` — the `/` makes `interpreter` **positional-only**. Passing it as a
keyword raises `TypeError("To use a caller-owned interpreter, pass it as the
first positional argument when calling the module.")`
(`dspy:predict/rlm.py:427-430,701`). `rlm_ingest.py` never passes one; it
lets `dspy.RLM` build and shut down its own sandbox every call.

**Inputs must match the signature exactly, in both directions.** An input the
signature does not declare raises `ValueError("Unexpected inputs not declared
in the signature: [...]")`; a declared input left out raises
`ValueError("Missing required inputs: [...]")`
(`dspy:predict/rlm.py:425-438`). This is the rule a `History`-carrying
wrapper breaks — see *Failure modes*.

**Reserved names.** A name may be used for at most one role:

| may not be named | reserved for | error |
|---|---|---|
| a tool, or an input field | `llm_query`, `llm_query_batched`, `SUBMIT`, `print` | `ValueError("Tool name '<x>' conflicts with built-in sandbox function")` / `ValueError("Input fields conflict with built-in sandbox functions: [...]")` |
| an input field that is also a tool name | — | `ValueError("Input fields conflict with user tools: [...]")` |
| an output field | `trajectory`, `final_reasoning` | `ValueError("Output fields conflict with RLM result metadata: [...]")` |

(`dspy:predict/rlm.py:189-190,219-238`). `rlm_ingest.py`'s own names
clear all of it: inputs `document`/`task`, tools `find_line`/`count`, output
`candidates`. A `tools=` dict instead of a list raises `TypeError("tools must
be a list, not a dict. Change tools={'name': func} to tools=[func] ...")`
(`dspy:predict/rlm.py:197-202`). **A tool is not sandboxed by the
sandbox**: "If you pass custom `tools` that do I/O, your tools' security
posture is yours. Never hand raw `subprocess.run` to the RLM."
(`dspy-agent-skills:skills/dspy-rlm-module/SKILL.md:109-111`).
`rlm_ingest.py`'s own tools, `find_line` and `count`
(`scripts/rlm_ingest.py`), are read-only host-side lookups: each
re-opens the same landed file the sandbox's `document` string was built from,
via `subject.document(slug)`, and answers one question about it. Neither
touches the filesystem beyond that, and neither is sandboxed code — like
`llm_query`, a tool call leaves the sandbox and runs on the host.

**Outputs.** Every `Prediction` carries the signature's own declared fields
plus two more, always:

| field | on a real `SUBMIT` | on a forced ending |
|---|---|---|
| `trajectory` | every step so far as `{"reasoning", "code", "output"}` dicts, **full text, never truncated**; the last entry's `output` is `"FINAL: {parsed_outputs}"` | the same, minus the `"FINAL: ..."` entry |
| `final_reasoning` | that step's own `reasoning` text | the literal string `"Extract forced final output"` |

(`dspy:predict/rlm.py:558-562,634-641,755`).

## What each iteration sends

Every `generate_action` call — one per iteration — receives three things, and
sends back `reasoning` and `code`
(`dspy:predict/rlm.py:359-369`):

- **`variables_info`** — one formatted block per input: name, type, optional
  `desc`/`constraints`, `"Total length: N characters"`, and a **preview**: up
  to 1000 characters, head 500 + `"..."` + tail 500 when longer, JSON-dumped
  with indent 2 for dicts and lists
  (`dspy:primitives/repl_types.py:38-95`). Roughly 1 KB of every input —
  including the whole document `rlm_ingest.py` passes — reaches the outer
  LM's prompt on **every** iteration, whatever `find_line`/`count` and P26
  say about not retyping values.
- **`repl_history`** — every past step, rendered `"=== Step N ==="` with its
  reasoning, code and output, the output itself truncated head+tail at
  `max_output_chars` with an explicit `"(N characters omitted)"` note
  (`dspy:primitives/repl_types.py:111-125`). Only the *prompt view* is
  cut; the stored entry and `result.trajectory` keep the full text.
- **`iteration`** — the literal string `f"{iteration+1}/{self.max_iters}"`
  (`dspy:predict/rlm.py:680`).

**Inputs are re-injected into the sandbox on every iteration, not just the
first.** `_execute_code` calls `repl.execute(code, variables=dict(input_args))`
on every step (`dspy:predict/rlm.py:654-664,694`). A name the model
reassigns — `context = context.upper()` — reverts on the next iteration,
while other state the model creates persists; the `dspy-agent-skills` reader
demonstrated exactly this in the real sandbox (step 1 printed `ALPHA`, step 2
`alpha`; `dspy-agent-skills`'s own probe, not rerun here).

**`SUBMIT` is a typed function generated per signature**, inside the sandbox:
`def SUBMIT(<output field names>): raise _DSPyFinalOutput({...})`
(`dspy:primitives/runner.js:23,74-88`). It raises a `BaseException`
subclass, not `Exception`, so a model's own `except Exception:` cannot
swallow it. The host's `execute()` catches it and returns `FinalOutput(dict)`
(`dspy:primitives/code_interpreter.py:32-48`); `_process_final_output`
then checks the value is a dict, checks every declared output field is
present — else `[Error] Missing output fields: [...]. Use SUBMIT(...)` — and
parses each one against its declared type, reporting `[Type Error]: ...` back
into the history rather than crashing the run
(`dspy:predict/rlm.py:564-598`). Both failures go back as this step's
`output`, and the loop continues: the model gets to retry. A trailing
expression, not only `print()`, can also become a step's non-final output —
the runner returns the last expression's value when it is not `None`
(`dspy:primitives/runner.js:342-346`), so `print('x')` followed by
`len(context)` reports the length and the print is lost.

## Failure modes and traps

| trap | what happens | evidence |
|---|---|---|
| **forced final output** | `max_iters` runs out with no `SUBMIT`; `_extract_fallback` calls a second, code-free predictor (`extract`) over `variables_info` and `repl_history` and returns a normal-shaped `Prediction` with every declared field filled and `final_reasoning="Extract forced final output"` — the only tell. [checked: rlm-forced-final-output] | `dspy:predict/rlm.py:543-562,735-757` |
| **budget exceeded inside the sandbox** | over `max_llm_calls`, `RuntimeError("LLM call limit exceeded: ...")` is raised **inside** the sandbox; `_execute_code` catches it and turns it into `[Error] RuntimeError: [...]` in the history. The loop continues and the model can still `SUBMIT` — nothing stops the run from the outside | `dspy:predict/rlm.py:267-274,654-664` |
| **interpreter state leaks between documents** | a caller-owned interpreter, passed positionally, is never reset or shut down between calls: "may be reused sequentially with the same RLM instance, but must not be shared by overlapping invocations" | `dspy:predict/rlm.py:127-128,519-537` |
| **an input named `json`** | the default sandbox's variable injection rejects the literal key `"json"` with a terminal `CodeInterpreterError("Invalid variable name: 'json'")` — the module still constructs; only a call with that input name fails | `dspy:primitives/python_interpreter.py:695-696` |
| **History wrapper, DSPy 3.1.3** | wrapping `dspy.RLM` in a session/history layer adds an extra `history` input; on 3.1.3 `_validate_inputs` checked only for *missing* inputs, so `history` reached the REPL as an unhandled type and every one of 20 iterations failed with `„[Error] Unsupported value type: History"` — yet the run still ended in the same forced-answer shape | `dspy-session:docs/rlm.md:5-29` |
| **History wrapper, DSPy 3.3.1** | 3.3.1 validates both directions; the same wrapper now fails at once with `ValueError: Unexpected inputs not declared in the signature: ['history']`, before any LM or sandbox work | `dspy:predict/rlm.py:425-438`; re-checked here 2026-09-24, `scripts/lmrun.py` |
| **experimental status** | `@experimental` injects "This class may change or be removed in a future release without warning" into the class docstring; nothing pins that it will not | `dspy:predict/rlm.py:115` |
| **the 3.2 → 3.3 renames** | `max_iterations` → `max_iters`, `interpreter=` → `interpreter_factory=` with a caller-owned instance moved to `forward()`; both are hard `TypeError`s on the wrong version, not a silent no-op | `check_dspy_surface.py` pins the current names; `dspy-agent-skills:skills/dspy-rlm-module/reference.md:25-35` records both versions |

**No exception ever tells you a reading was forced or incomplete — the
`Prediction` looks exactly like a normal answer unless `final_reasoning` is
checked.** That is the reason `rlm_ingest.py`'s `FORCED` constant exists
(`scripts/rlm_ingest.py`) and the reason `judge()` checks it first,
ahead of the citation tiers (`scripts/rlm_ingest.py`).

## When RLM pays

The book's own threshold: "RLM | a sandboxed REPL with your context as
variables, plus a cheap sub-model | the context is too long to reason over
directly, roughly 50,000 tokens and up"
(`dspy-agent-skills:skills/dspy-book-modules/SKILL.md:80`). Below that:
`Predict`/`ChainOfThought`. External tools: `ReAct`. Math or code that must
run: `ProgramOfThought`. All three sandboxed modules run on Deno plus
Pyodide, restricted by default, "which is why an RLM cannot read host files
and you must pass contents as input values"
(`dspy-agent-skills:skills/dspy-book-modules/SKILL.md:86-89`,
`reference.md:74`).

**This repository's own documents are far under that threshold**, and that is
worth stating plainly: a landed source document is roughly 6,700 words
(`Plan/concept/rlm-the-real-one_2026-09-17.md`) — a few thousand tokens,
not fifty thousand. By the book's own rule a single document does not need
RLM's REPL to fit; it fits directly. `rlm_ingest.py` reads one document at a
time through `dspy.RLM` anyway, and the reason stated for it is not length —
it is that a census is a counting task, and the REPL plus `find_line`/`count`
exist so the model can verify its own claim rather than be trusted on it
(`scripts/rlm_ingest.py`).

**Where the book's threshold is actually crossed here is the corpus, not the
document.** `corpus.py plan`'s own estimate for one term across the whole
landed corpus, computed from the manifest without reading anything:

```
AEGIS — 315 documents, 14,676,980 chars
41 sub-calls at 400,000 chars each
```

(`Plan/concept/rlm-the-real-one_2026-09-17.md`). That corpus-scale loop
is catalogued, not built — see *Not taken, or waiting*.

**The one live measurement this project has, with its caveats.** On
2026-09-17 — before `rlm_ingest.py`'s current design existed: no cache-off
wrapper, no `find_line`/`count` tools, no reach/forced tiers, `max_iters=4` —
`dspy.RLM` was run once against a document known to be tricky:
`guardians-und-kern-welten-konzept` states "die vier zentralen Hüter" and
"die vier Guardian/Welt-Paare" while actually naming five Guardians,
reconciled only in one parenthetical
(`Plan/concept/rlm-measured-on-the-trap_2026-09-17.md`). The RLM run
named four, missing the one hidden in the parenthesis; two direct prompts
with the full document in context, no RLM, named five in one shot
(`Plan/concept/rlm-measured-on-the-trap_2026-09-17.md`). The note's own
reading is narrower than "RLM failed" — "both failures are partly mine": a
tight iteration budget and a token cap, not a proof against the method
(`:41-43`). **The lesson kept is about counts, not about RLM**: a count
question needs cross-checking structural signals a slicing pass has no reason
to connect, which is what a document's own census step is for (`:48-70`).

A second, on-topic recipe from the book: discovering a skill from past agent
transcripts. Point an RLM at a directory of session texts — passed as an
input value, since the sandbox cannot read host files — summarise each,
cluster the summaries, and write a candidate `SKILL.md` for the largest
cluster, skipping groups smaller than two sessions; the output is a draft for
human review, never installed directly
(`dspy-agent-skills:skills/dspy-book-coding-agents/SKILL.md:132-139`,
`reference.md:113-129`). Not built here; there is no transcript corpus to
point it at yet.

## Verification

**This repository's own three tiers**, all in `rlm_ingest.py`:

1. **Cited line** — every candidate came back as `- term  ^[Lnn]`; a
   candidate is `good` only if its cited line, run through the same
   normalisation `quotes.py` uses, actually contains the term
   (`verified()`, `scripts/rlm_ingest.py`).
2. **Reach** — a candidate whose cited line holds it still passes tier 1 even
   if the whole list comes from the first third of the document. `reach()`
   reports the furthest verified citation as a share of the document and how
   many of ten "tenths" the verified citations fall in; a list that never
   cites past 90% of a document did not read to the end, whatever it says
   (`scripts/rlm_ingest.py`).
3. **Forced** — outranks the other two entirely: `judge()` checks `forced`
   first and returns "PARTLY RECONSTRUCTED" regardless of how good the
   citations look (`scripts/rlm_ingest.py`).

A list earns "a reading" only when `share ≥ 0.9`, no `UNREAD` lines, no
uncited candidates, `reach ≥ 0.9`, and not forced — all at once
(`scripts/rlm_ingest.py`).

**`dspy-rlm-workflow`'s cascade, for contrast.** A different pattern, for
verifying a *synthesised answer* rather than a candidate list: a
five-argument metric returning `dspy.Prediction(score, feedback)`, fail-fast
over three tiers weighted 0.3/0.4/0.3 — syntactic, semantic, pragmatic
(`dspy-agent-skills:skills/dspy-rlm-workflow/SKILL.md:118-134`,
`reference.md:92-102`). **What its own shipped example actually checks is
thinner than the prose promises**: Tier 1 is binary (schema-valid or not),
Tier 2 is a case-insensitive substring test of each `success_criteria` item
against the answer, and Tier 3 — "the pragmatic tier" — is a hard-coded
constant, "the smoke test treats it as passed"
(`dspy-agent-skills:skills/dspy-rlm-workflow/example_rlm_workflow.py:113-137`,
quoted at `:136-137`). Two things the prose promises and the code does not
implement at all: a check that every sub-answer id appears somewhere in the
final answer, and a check that `contradictions` is non-empty whenever
sub-results disagree (`dspy-agent-skills:skills/dspy-rlm-workflow/reference.md:143`,
`SKILL.md:178`).

The shape is sound and reusable — fail fast, weight cheap checks first, and a
verifier's feedback must name which sub-problem or module failed, "so GEPA
has something to learn from"
(`dspy-agent-skills:skills/dspy-rlm-workflow/reference.md:104-106`,
`SKILL.md:176`) — but the part that would let a model *resolve* a
disagreement, not only report one, is exactly what P13 forbids here: a term
page holds every reading, attributed, and never merges. Nothing here compiles
this cascade; it is catalogued as a pattern for the day a synthesis step
exists — see *The rlm-workflow pattern*, next.

## The rlm-workflow pattern

`dspy-rlm-workflow` ports a prose plan into DSPy: **distill → decompose →
solve → synthesize → verify → iterate**, recursing on sub-problems marked
`complexity: "high"` while depth remains
(`dspy-agent-skills:skills/dspy-rlm-workflow/SKILL.md:20-30`).

| phase | what it does |
|---|---|
| Initialize | a `WorkflowPlan` fixes `complexity` (`constant`/`linear`/`quadratic`) and `depth` (1–3) |
| Distill | ≤~100k tokens: a `Distill` signature per chunk, rated 0–3, keep/summarise/drop; >~100k tokens: `dspy.RLM("context, query -> distilled", sub_lm=cheap, max_llm_calls=30)`. Either way the distilled text is itself an **input** to the rest of the workflow, so it is testable with a hand-written distillation |
| Decompose | a list of typed `SubProblem`s (`id, description, dependencies, complexity, success_criteria`), ordered and checked by `validate_dag` |
| Solve | in topological order, injecting each dependency's own result; recurses only when `complexity == "high"` and depth remains |
| Synthesize | agreements, contradictions, gaps, answer, confidence — its own docstring says "Never resolve a contradiction silently" |
| Verify | the fail-fast cascade above |
| Iterate | `dspy.Refine`/`GEPA` on the same metric |

(`dspy-agent-skills:skills/dspy-rlm-workflow/SKILL.md:20-30`, `reference.md:10-42`)

**`validate_dag` is the one piece worth lifting whole**: plain Python, no LM,
rejecting duplicate ids, unknown dependencies and cycles (naming the cycle
path), returning topological order — "Do not ask the LM to order the work —
it will get it wrong on the day it matters"
(`dspy-agent-skills:skills/dspy-rlm-workflow/reference.md:44-69`,
`SKILL.md:101-103`):

```python
def validate_dag(sub_problems: list[SubProblem]) -> list[SubProblem]:
    """Return sub-problems in dependency order; raise ValueError on bad graphs."""
    by_id = {sp.id: sp for sp in sub_problems}
    if len(by_id) != len(sub_problems):
        raise ValueError("duplicate sub-problem ids")
    unknown = {d for sp in sub_problems for d in sp.dependencies if d not in by_id}
    if unknown:
        raise ValueError(f"dependencies on unknown ids: {sorted(unknown)}")
    order: list[SubProblem] = []
    state: dict[int, int] = {}

    def visit(sid: int, stack: tuple[int, ...]) -> None:
        if state.get(sid) == 2:
            return
        if state.get(sid) == 1:
            raise ValueError(f"cycle: {' -> '.join(map(str, stack + (sid,)))}")
        state[sid] = 1
        for dep in by_id[sid].dependencies:
            visit(dep, stack + (sid,))
        state[sid] = 2
        order.append(by_id[sid])

    for sp in sub_problems:
        visit(sp.id, ())
    return order
```

(`dspy-agent-skills:skills/dspy-rlm-workflow/example_rlm_workflow.py:30-54`;
runs on DSPy 3.3.1, dry-run asserts order `[1, 2, 3, 4]` and a raised cycle) —
the same principle as this repository's P1: whether work can be ordered by a
rule decides whether it is code or judgement, and ordering sub-problems is
squarely the former.

**Its own example undercuts itself, twice**, worth knowing before borrowing
it: the canonical `solve()` recurses on a `high`-complexity sub-problem with
`self.forward(sp.description, distilled_context, depth + 1)`, **without the
computed `deps`** — its own sample plan has a `high` sub-problem depending on
two others, so a live run would solve it blind
(`dspy-agent-skills:skills/dspy-rlm-workflow/SKILL.md:89-93`,
`example_rlm_workflow.py:100-103`); and calling `self.forward(...)` directly
on every recursion, rather than `self(...)`, bypasses `Module.__call__` and
logs a warning each time (`dspy:primitives/module.py:336-348` per the
note; not reread here).

**Not taken.** Nothing here compiles this pipeline. A landed document is
small enough that the census reads it whole, in order, by design — "the
census rule is that a reader proposes candidates before anything counts.
Counting first decides what gets seen"
(`Plan/concept/rlm-the-real-one_2026-09-17.md`) — which is exactly the
premise `distill`/`decompose` exist to avoid needing. The pattern waits for a
task shaped like synthesis over several already-read sources, which is not
what `rlm_ingest.py` does today.

## Hooks and speculation — not taken

`dspy-rlm-hooks` (0.1.14, MIT, `Requires-Python >=3.12`, taught by the
`dspy-agent-skills:skills/dspy-rlm-hooks/` skill,
`dspy-agent-skills:skills/dspy-rlm-hooks/SKILL.md:18-20`) monkeypatches a
**live** `dspy.RLM` instance with four keyword-only hook points, one callable
each:
`pre_iteration(iteration, variables, history, input_args)`,
`pre_execution(iteration, code, variables, history, input_args)`,
`post_execution(iteration, code, result, variables, history, input_args)`,
`post_iteration(iteration, pred, code, result, history)`
(`dspy-agent-skills:skills/dspy-rlm-hooks/SKILL.md:54-63`,
`reference.md:20-37`). `PreIterationOutput` can inject extra variables for one
iteration, prepend code, replace the interpreter's persistent globals, or
append free text to the prompt
(`dspy-agent-skills:skills/dspy-rlm-hooks/SKILL.md:65-68`).

**Why it is not installed here:**

- **It needs a real, running `dspy.RLM` instance to patch, and none has run
  yet.** Nothing here has called `dspy.RLM` against a real model (`NOW.md`
  — three model runs, `rlm_ingest.py` among them, wait on the author's yes) —
  there is nothing to attach a hook to.
- **`stop=True` looks exactly like hitting `max_iters`.**
  `PostIterationOutput(stop=True)` calls the same `_extract_fallback` and
  produces the same `final_reasoning="Extract forced final output"` marker —
  a hook-stopped run and a budget-exhausted one are indistinguishable in the
  result (`dspy-agent-skills:skills/dspy-rlm-hooks/SKILL.md:92-94`, per the
  pack's own reading of its patcher). This repository's forced-output check
  would correctly refuse either as "not a reading" either way, but a hook
  could never be trusted to mean something *different* from running out of
  budget.
- **Enable order matters and half-patches silently.** Enabling speculation
  then hooks leaves speculation inactive while its streaming wrapper stays
  in place; the reverse order leaves both active
  (`dspy-agent-skills:skills/dspy-rlm-hooks/SKILL.md:92-94`). A package whose
  own two features interact by enable order is the kind of hidden state P6
  exists to keep out of a skill's prose rather than restate.
- **`(dspy, dspy-rlm-hooks)` would have to be pinned as one version unit.**
  The package carries its own copy of the iteration loop and of code-fence
  stripping; a DSPy release that changes either is silently shadowed on a
  patched instance
  (`dspy-agent-skills:skills/dspy-rlm-hooks/reference.md:47-48`,
  `SKILL.md:31-36`).
- **Hooks widen what a terminal error looks like.** DSPy's own `_execute_code`
  catches only `(CodeExecutionError, SyntaxError)`
  (`dspy:predict/rlm.py:661-664`); the hooks package's copy of the same
  method catches every `Exception` instead, by `dspy-agent-skills`'s own
  reading of both sources (not reread here). With hooks enabled, a genuinely
  terminal sandbox failure becomes a recoverable step output, and the loop
  keeps spending outer-LM calls against a dead interpreter.

**Speculation** (`enable_rlm_speculation`, same package) runs
`llm_query`/`llm_query_batched` ahead of the model asking for them, to hide
their latency. **The specific reason it is refused**: a speculative
`llm_query` call is registered `pure=True` and does **not** count against
`max_llm_calls` even though it is a real, paid call — a rule the package's
own skill states for user tools ("Tool costs money per call; evicted
speculations are paid for and thrown away") and then breaks for its own
built-in tool
(`dspy-agent-skills:skills/dspy-rlm-hooks/SKILL.md:105-107`, per the note's
read of the speculation registry). `max_llm_calls` is the one cost guard
`rlm_ingest.py` sets explicitly and treats as a parameter rather than a
surprise (*The module*, above); a feature whose speculative path spends
outside that counter defeats the reason the counter exists. Disposal is also
not free: by the package's own account, `disable_rlm_speculation` must be
called every time because speculation "spawns subprocesses, threads and an
asyncio loop" (`dspy-agent-skills:skills/dspy-rlm-hooks/SKILL.md:105-107`;
this specific claim is the skill's own, not independently re-verified by its
reader).

## An offline RLM run

The verified recipe pairs `lm_fixture` with the **real** Deno/Pyodide
sandbox — not a mock — and a scripted `code` cell that calls `SUBMIT` itself:

```python
from lm_fixture import FixtureLM, chat, offline
import dspy

step = chat(reasoning="Ich lese.", code="SUBMIT(candidates='- Kern-Welt  ^[L1]')")
with offline(FixtureLM(lambda messages: step)):
    out = dspy.RLM("document: str, task: str -> candidates: str", max_iters=2, max_llm_calls=3)(
        document="L1| Die Kern-Welt ist eine Welt.", task="list the terms")
# out.candidates == "- Kern-Welt  ^[L1]"
```

This is `check_dspy_skill.py`'s own probe (`scripts/check_dspy_skill.py`),
run here today and held: `dspy.RLM` reaches the sandbox, executes the
scripted `SUBMIT(...)` call, and returns the normal `Prediction` — with no
network, no API key, and no litellm call, because `offline()` hides every
`*_API_KEY` and makes `litellm.completion` raise
(`scripts/lm_fixture.py`). [checked: rlm-runs-offline]

**The gate is Deno, not the model.** The probe requires `import deno` to
succeed first, and reports `NotRun` — never "held" — if it cannot
(`scripts/check_dspy_skill.py`), per P15/P23: a probe that cannot run
says so rather than passing silently. Once Deno works (*Installing the
sandbox*), the model side of the recipe is free: no key, no network, and the
FixtureLM's `fill()` helper can answer whatever fields an unscripted step of
the loop asks for, which is exactly how `p_rlm_forced_final_output` drives a
model that never calls `SUBMIT` (`scripts/check_dspy_skill.py`,
`scripts/lm_fixture.py`).

**A second recipe exists and needs no Deno at all**, offered by
`dspy-agent-skills` as "Code worth keeping" rather than something built here:
a small host-side `CodeInterpreter` implementing `tools`/`start()`/`execute()`/
`shutdown()` in plain Python (`exec` on the host, for tests only), returning
`FinalOutput(dict)` on `SUBMIT` and raising `CodeExecutionError` on a code
error. Passed as `interpreter_factory`, it lets a scripted `DummyLM`/
`FixtureLM` drive a full RLM loop with no sandbox dependency at all
(`dspy-agent-skills`'s own condensed probe, re-run by that reader as
`probe/condensed_check.py`). This repository's own probes do not use it — they
test the real sandbox on purpose, because a fixture that never touches the
real interpreter would not catch a Deno-version regression or a
sandbox-protocol change.

**What `rlm_ingest.py` itself does not have.** Unlike `pairs.py` and
`graphrag.py`, it carries no `--dry-run` flag. `--selftest` exercises
`find_line`/`count`/`reach`/`judge()` without a model, but there is no path
that drives an actual `dspy.RLM` call through `lm_fixture` the way the probe
above does. That gap is real, and it is a next step, not a hidden feature —
nothing in `scripts/rlm_ingest.py` claims otherwise.

## Not taken, or waiting

| idea | status | why, or what it waits for |
|---|---|---|
| Hooks, speculation | refused | see above |
| The full rlm-workflow pipeline | catalogued, not built | waits for a synthesis task over several already-read sources; a document here is read whole, by design |
| GEPA compiling the RLM itself | catalogued, not built | an RLM has exactly two predictors, `generate_action` and `extract`; GEPA on it would rewrite DSPy's own REPL template, not only a task instruction (`dspy-agent-skills:skills/dspy-rlm-module/SKILL.md:80-97`). Waits on the same gate as any real RLM run: "two or three more hand-read documents" before extraction is trainable (`Plan/concept/dspy-toolchain_2026-09-23.md`, `.claude/skills/tools/SKILL.md`) |
| A corpus-scale RLM loop ("idea E") | catalogued, not built | `llm_query_batched` over many documents for one term — "What does the corpus say about AEGIS?" is exactly the RLM case, sized at 315 documents / 41 sub-calls without reading anything (`Plan/concept/rlm-the-real-one_2026-09-17.md`). Explicitly "not worth doing before the hand pass finishes" (`:98-101`) |
| Making a term, not a document, the unit of work ("idea D") | rejected | "a term-first pass reads many documents through one lens, which is exactly the contamination the census exists to prevent. The unit stays the document" (`Plan/concept/rlm-transfer_2026-09-17.md`) |
| `SHOW_VARS()`-style self-report | catalogued, not built | telling a reader what the derived cache already knows, the way an RLM's REPL can inspect its own environment (`Plan/concept/rlm-the-real-one_2026-09-17.md`) |
| The pre-2026-09-23 `rlm` package (`pip install rlms`) | superseded | read once, 2026-09-17, before this repository adopted `dspy.RLM`; its `context`/`llm_query`/`rlm_query`/`SHOW_VARS` shape is where "idea E" and `SHOW_VARS()` above came from, but the package was never installed and nothing in `scripts/` depends on it |
| History-wrapping `dspy.RLM` | refused | fails immediately on 3.3.1 anyway — see *Failure modes* |

`optimizers.md` has GEPA and the rest of the ladder in depth;
`patterns.md` has `Refine`/`BestOfN` and composition patterns beyond RLM;
`repos.md` has what each of the nine repositories is, for weighing an idea
against its source.
