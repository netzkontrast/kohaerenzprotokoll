# Optimizing text that is not a DSPy program

A `SKILL.md`, a skill's `description:` field, a prompt string embedded in a
script, a Pydantic field description — none of these compile into a
`dspy.Module`. There is no signature, no predictor, no
`pred.signature.instructions` for `dspy.GEPA` to rewrite. `gepa.optimize_anything`
is the entry point built for exactly that shape: a candidate is a string or a
`dict[str, str]`, scored by a plain Python function against data, evolved by
the same reflective-mutation loop GEPA runs internally, with no DSPy program
wrapped around it. This repository calls this work **job 4**
(`Plan/concept/dspy-toolchain_2026-09-23.md:307-323`).

`api.md` has the one-line, mechanically-checked call signature (under the
comment naming this file). This file has the mechanics behind it, what fails
and how, and what job 4 is waiting for.

Citations to the installed `gepa` 0.1.4 package are written `gepa:<path>:<line>`,
relative to `.venv-dspy/lib/python3.11/site-packages/gepa/` — the same
evidence tier as `api.md`'s `dspy:<path>:<line>`: read or run here, 2026-09-24,
not a repository's claim.

```surface
gepa.optimize_anything.EngineConfig(raise_on_exception=True, parallel=True, cache_evaluation=False, max_metric_calls=None, max_candidate_proposals=None)
gepa.optimize_anything.ReflectionConfig(reflection_lm="openai/gpt-5.1", reflection_minibatch_size=None, skip_perfect_score=False)
gepa.optimize_anything.GEPAConfig(merge=None, refiner=None)
gepa.optimize_anything.EvaluatorWrapper(evaluator_fn, single_instance_mode, capture_stdio=False, str_candidate_mode=False, raise_on_exception=True)
```

## In this repository

| exists | where | what it does |
|---|---|---|
| the frontmatter validator | `scripts/check_skills.py` | spec-only fields (`name`, `description`, `when_to_use`, `argument-hint`, `disable-model-invocation`, `user-invocable`, `allowed-tools`, `model`, `effort`, `context`, `agent`, `hooks`, `paths`, `shell`, plus the spec's `license`/`metadata`/`compatibility`); rejects `triggers`, `version`, `dspy-compatibility`, `dspy-version`; fails a `description` + `when_to_use` over 1536 characters; requires `name == <folder>` and the filename to be exactly `SKILL.md`; enforces P6 — `.claude/skills/<name>` must be a symlink into `.agents/skills/`, never a second real folder; checks the vendored `jev*` folders but never fails the run on them, reporting them under their own heading |
| the evaluator-signature guard | `scripts/check_dspy_surface.py`'s `example_param_ok()` | the one assertion any job-4 evaluator must pass before it is handed to `optimize_anything` |
| the live consumer of the field job 4 would optimize | `scripts/rlm_ingest.py`'s `briefing()` | builds the `<available_skills>` block from every skill's `description` field alone — the same mechanism Claude Code and Codex use to choose a skill |
| the behavioural check | `scripts/check_dspy_skill.py`, probe `example-reaches-evaluator-by-name` | runs `gepa.optimize_anything.EvaluatorWrapper` offline against a correctly- and a wrongly-named evaluator and fails if either stops behaving as described below |

**What does not exist: a dataset, an evaluator, a run.** `scripts/check_dspy_surface.py`'s
`example_param_ok()` is the whole of job 4 today —
`Plan/concept/dspy-toolchain_2026-09-23.md:307-323` records it as "guard only —
no routing failures recorded, so no dataset (P4)". `NOW.md`'s handover, item 4:
"**Record routing failures** — each time an agent loaded the wrong skill or
none. Five to twenty of them are job 4's dataset; there are none, so it has
not started." (`NOW.md:235-237`). The number is not arbitrary: it is the
chapter's own rule for the benchmark job 4 would build —
"**The dataset is 5 to 20 hand-captured real failures**, not synthetic volume.
You are encoding what actually goes wrong."
(`dspy-agent-skills:skills/dspy-book-coding-agents/SKILL.md:55`). By P4 ("no
page type, field or check without instances"), recording those failures is the
next action, and it is free — it needs no model, no key, no `.venv-dspy`.

`check_skills.py` is also why job 4 has a validator to run its output through
before it has a dataset: "job 4 optimizes exactly this field; a validator must
exist before anything rewrites it"
(`Plan/concept/dspy-toolchain_2026-09-23.md:150-151`).

## The recipe: `optimize_anything` step by step

```python
from gepa.optimize_anything import optimize_anything, GEPAConfig, EngineConfig, ReflectionConfig

def evaluator(candidate: str, example: dict) -> tuple[float, dict]:
    response = TASK_LM(messages=[{"role": "system", "content": candidate},
                                 {"role": "user", "content": example["prompt"]}])[0]
    score, verdict = judge(response, example)
    return score, {"Prompt": example["prompt"], "Response": response,
                   "JudgeReasoning": verdict}          # the reflector's only window into why

result = optimize_anything(
    seed_candidate=open("SKILL.md").read(),
    evaluator=evaluator,
    dataset=CASES,
    objective="Rewrite the skill so ... Output ONLY the SKILL.md text.",
    config=GEPAConfig(engine=EngineConfig(max_metric_calls=80),
                      reflection=ReflectionConfig(reflection_lm=REFLECTION_MODEL)),
)
print(result.best_candidate)      # the new file text
```
`dspy-agent-skills:skills/dspy-book-coding-agents/SKILL.md:26-51`. Names
verified against `gepa` 0.1.4 here; an LM called with `messages=` returns a
list of strings (`gepa:optimize_anything.py:1215-1219` shows the same shape).
The book pins `gepa==0.1.1`; DSPy 3.3.1 declares `gepa[dspy]==0.1.4` as a
dependency, so this repository already has 0.1.4 in `.venv-dspy` with no extra
install, and everything below is checked against **0.1.4**, not the book's
0.1.1 — where the two disagree, 0.1.4 is what actually runs here.

### The seed candidate, and three search modes

`seed_candidate` is a `str` (the evaluator receives a `str`), a
`dict[str, str]` (named parameters — a `SKILL.md` plus a separate
`description` string could be one candidate), or `None` ("seedless mode": the
reflection LM writes the first draft from `objective`, which then becomes
required) (`gepa:optimize_anything.py:1150-1159`). The mode is read from
`dataset`/`valset`, never stated separately
(`gepa:optimize_anything.py:1132-1148,1281-1294`):

| `dataset` | `valset` | mode | job-4 shape |
|---|---|---|---|
| `None` | `None` | single-task: the candidate *is* the solution, evaluator called **without** `example` | not this — job 4 needs a dataset |
| given | `None` | multi-task: `valset` defaults to `dataset` — candidate selection and reflection share the same cases | the book's own recipe: `dataset=CASES` only |
| given | given | generalization: reflection sees `dataset`, selection is scored on the held-out `valset` | what job 4 should do once the 5–20 cases exist — the book's recipe has no held-out set, so its own regressions (below) are expected |

### The evaluator, and its name trap

The evaluator returns `(score, side_info)` or a bare `score`
(`gepa:optimize_anything.py:414-420`). `side_info` is a dict of whatever the
reflection LM should see — the reflector never runs the candidate itself, so
"**The side-info dict is load-bearing.** The reflection LM sees only the score
and that dict. Always include the judge's reasoning, or it is optimizing
blind." (`dspy-agent-skills:skills/dspy-book-coding-agents/SKILL.md:56`). The
keys `"log"`, `"stdout"`, `"stderr"` are reserved for GEPA's own capture
(`oa.log()`, `EngineConfig(capture_stdio=True)`); a colliding key is renamed
`_gepa_<key>` with a warning (`gepa:optimize_anything.py:442-446,1082-1091`).

**`EvaluatorWrapper` builds its call by inspecting the evaluator's signature
once, at construction, and injects the dataset item by the literal keyword
`example`** (`gepa:optimize_anything.py:994-1021`):

```python
sig = inspect.signature(evaluator_fn)
accepted_params = set(sig.parameters.keys())          # unless **kwargs, which takes everything
...
all_kwargs = {"example": example, **kwargs}            # single_instance_mode=False
filtered = {k: v for k, v in all_kwargs.items() if k in accepted_params}
result = evaluator_fn(eval_candidate, **filtered)
```
(`gepa:optimize_anything.py:995-1005,1016-1023,1044`.) `example` is filtered
**out** before the call unless the evaluator's own second parameter is
literally named `example`. What happens next depends on two things: whether
that parameter has a default, and `EngineConfig.raise_on_exception` (default
`True`, `gepa:optimize_anything.py:468`):

| 2nd parameter | `raise_on_exception` | result |
|---|---|---|
| `example` | either | the real value reaches the evaluator |
| anything else, no default | `True` (the default) | `TypeError: <fn>() missing 1 required positional argument`, raised straight out of the call |
| anything else, no default | `False` | the same `TypeError` is caught and turned into `(0.0, None, {"error": "<fn>() missing ... argument: '<name>'"})` — a normal-shaped zero score, the real cause sitting in a `side_info` key nothing is obliged to read |
| anything else, **with a default** | either | no exception, ever — the evaluator runs on the default forever and returns whatever plausible score it computes, having never seen the example |

The first two rows are exactly what
`scripts/check_dspy_skill.py`'s `example-reaches-evaluator-by-name` probe
checks, offline, against the installed `EvaluatorWrapper`: that an evaluator
named `(candidate, example)` receives the value it was given, and that one
named `(candidate, task)` is never silently run with the real data — under
`EvaluatorWrapper`'s own default it raises instead.
[checked: example-reaches-evaluator-by-name] The last two rows were confirmed
the same way, offline, against 0.1.4, this session
(`gepa:optimize_anything.py:1044,1056-1066`) — no probe carries them, so they
are not continuously re-checked. `scripts/check_dspy_surface.py`'s guard exists
for exactly the loud case:

```python
def example_param_ok(evaluator) -> bool:
    """`gepa.optimize_anything` introspects its evaluator: the second parameter
    must be named `example`, or the data is dropped silently and the crash comes
    layers later (dspy-book-coding-agents/SKILL.md:59). Call this before handing
    any evaluator over."""
    names = list(inspect.signature(evaluator).parameters)
    return len(names) >= 2 and names[1] == "example"
```
(`scripts/check_dspy_surface.py:56-62`.) Its docstring names the shape most
worth remembering: "the data is dropped silently and the crash comes layers
later" describes the loud row above from the outside — the drop happens at
the filter, the crash surfaces however many frames later the exception is
allowed to propagate. Whether it propagates at all is the row below it, which
`example_param_ok()` cannot see: **the guard catches a misnamed parameter, not
a defaulted one.** A job-4 evaluator with a default on its second parameter
(`def evaluate(candidate, example=None):`) still passes `example_param_ok()`
and would still run silently unscored in single-task mode — name it `example`
with no default, and let `dataset`/`valset` supply it.

`batch_evaluator` is the alternative: GEPA hands it every pending
`(candidate, example)` pair in one call instead of calling `evaluator` per
pair, useful for a provider batch job; `oa.log()` and stdio capture do not
work on this path, so diagnostics must go straight into the returned
`side_info` (`gepa:optimize_anything.py:1170-1195`). Not used by anything
sourced for job 4; recorded because `evaluator=` and `batch_evaluator=` are the
only two ways in — at least one is required
(`gepa:optimize_anything.py:1297-1302`).

### Objective and background

`objective` and `background` are rendered into the reflection prompt as
`## Optimization Goal` and `## Domain Context & Constraints`, above
`## Current Component` (the candidate, inside a plain ``` fence),
`## Evaluation Results` (the rendered `side_info`), `## Your Task` and
`## Output Format`, which reads: "Provide ONLY the improved version within
\`\`\` blocks. ... Do not include explanations, commentary, or markdown
outside the \`\`\` blocks."
(`gepa:optimize_anything.py:520-614`, the template builder in full; the exact
instruction at `gepa:optimize_anything.py:608-610`). `seed_candidate=None`
("seedless mode") requires `objective` and a reflection LM
(`gepa:optimize_anything.py:1266-1274`).

**The template already wraps the candidate and the answer in one ``` fence
each — a second, hand-written "no markdown fences" instruction fights it, not
helps it.** The book's own recipe says exactly that in its objective
(`dspy-agent-skills:skills/dspy-book-coding-agents/example_artifact_optimizer.py`
docstring references it; stated directly at
`dspy-agent-skills:skills/dspy-book-coding-agents/SKILL.md:57`). The extraction
is naive about which fence is which:

```python
start = lm_out.find("```") + 3         # the FIRST ``` anywhere in the answer
end = lm_out.rfind("```")              # the LAST ``` anywhere in the answer
content = lm_out[start:end]            # everything strictly between them
```
(`gepa:strategies/instruction_proposal.py:127-146`, trimmed.) **A `SKILL.md`
that itself contains a fenced code block — every file in this skill does — is
exactly the input this breaks.** If the reflection model reproduces the whole
file, including its own internal ```bash example, wrapped in the outer fence
the template asks for, `find()`/`rfind()` can land on the *file's own* inner
fence instead of the outer one, and everything outside that inner pair —
frontmatter, prose, the rest of the file — is discarded before it is ever
scored. For job 4: never repeat "no markdown fences"; instead check the
recovered `result.best_candidate` mechanically (parse the frontmatter, check
for `SKILL.md:`'s own required sections) before it is treated as a candidate
at all, the same way `check_skills.py` would refuse a malformed file.

### Config and budgets

`GEPAConfig` nests `EngineConfig` (budget, parallelism, stopping),
`ReflectionConfig` (the LM and its minibatch), and optionally `MergeConfig`
and `RefinerConfig`, both off unless set
(`gepa:optimize_anything.py:887-945`). **At least one stopping condition is
required**, or construction raises before any call is made: "At least one
stopping condition must be provided via config.engine.max_metric_calls or
config.stop_callbacks."
(`gepa:optimize_anything.py:1433-1436`). `run_dir` additionally adds a file
stopper on `<run_dir>/gepa.stop`, so a run can be told to stop from outside the
process (`gepa:optimize_anything.py:1405-1406`).

### What runs in parallel

`EngineConfig.parallel` defaults to `True`, with
`max_workers = os.cpu_count() or 32`
(`gepa:optimize_anything.py:490-491`), threaded straight into the adapter that
calls the evaluator (`gepa:optimize_anything.py:1344-1347`). **An evaluator
that mutates shared state, writes to one file, or calls a rate-limited API
needs `EngineConfig(parallel=False)` or its own lock** — nothing here
serialises calls for it. `capture_stdio=True` is explicitly documented as
thread-safe via per-thread `sys.stdout`/`stderr` replacement
(`gepa:optimize_anything.py:501-512`), which is the one piece of state GEPA
does guard.

### The reflection LM

**`ReflectionConfig.reflection_lm` defaults to `"openai/gpt-5.1"`**
(`gepa:optimize_anything.py:742`), converted through `make_litellm_lm` the
moment it is a string — a **live, paid call to OpenAI** the instant a
`GEPAConfig()` is built without overriding it, even if every other field is
set (the docstring's own example only overrides `engine.max_metric_calls`;
`gepa:optimize_anything.py:894-900`). **This is the opposite of `dspy.GEPA`,
which asserts `reflection_lm is not None` at *construction* and has no default
model to fall back to** — already stated in `SKILL.md`'s facts-that-bite,
item 5, whose behavioural probe belongs to `optimizers.md`. `optimize_anything`
will run without a word said about the key, until the network call fails or succeeds.
For every dry run and fixture here: pass a plain Python callable
`prompt -> str` as `reflection_lm`; it is wrapped in `TrackingLM` and never
touches litellm (`gepa:optimize_anything.py:1391-1394`) — the same shape
`lm_fixture.py` gives every other model step (P5).

### What fails silently — the checklist

- **The `example` name trap**, three of its four shapes are silent (table
  above).
- **The fence trap** (above): a truncated candidate parses as valid text.
- **A candidate that is never actually re-run.** This is not a `gepa` trap but
  a shape worth refusing on sight, because it looks identical from outside:
  `dspy-advanced-prompting`'s own "prompt optimizer" builds a
  `quality_score=8.0` for every test case without ever calling the candidate
  prompt, so its `best_prompt` never changes and `avg_score` is always 8.0
  (`dspy-advanced-prompting:src/techniques/meta_prompting.py:149-193`).
  `optimize_anything` does not have this defect — the evaluator is always
  called — but nothing stops a job-4 evaluator from having it, and the score
  curve would look exactly as healthy either way. Assert the evaluator was
  actually invoked (a call counter) before trusting a "score went up."
- **A metric exception swallowed by `raise_on_exception=False`** (table
  above) turns any evaluator bug into a plausible zero, not a crash — P23:
  count what the guard could not read, do not let "could not score" read as
  "scored badly."

### The regression list to read before applying

```python
regressed = [c.antipattern for c, b, o in zip(cases, baseline, optimized) if b > o]
```
(`dspy-agent-skills:skills/dspy-book-coding-agents/example_artifact_optimizer.py:97-100`,
prose at `SKILL.md:116-130`.) "GEPA drops rules that did not fire during the
evaluation. That is correct behaviour for the benchmark and wrong for your
repository, because your file also encodes rules no case exercised." The
recipe: measure the baseline before optimizing, re-score every case after
(not only the ones that improved), print the regression list, hand-restore
what the optimizer discarded, then diff against the current file — the
optimizer never knew about rules the benchmark did not cover. "Keep the old
artifact. ... the artifact is the only way to diagnose regressions."
Running the chapter's own dry run here reproduces the shape exactly: one
candidate scored a net **+1.0** against five held cases while regressing on
one of them (`new module when one exists`) —
[`dspy-agent-skills:skills/dspy-book-coding-agents/example_artifact_optimizer.py --dry-run`,
run offline in this session]. A net gain and a real regression are not
mutually exclusive, and only the per-case list tells them apart.

## Scoring a text artifact

**Weight mechanical checks above judged ones.** The landing-page notebook's
own metric: `score = 0.5 * mechanical + 0.25 * visual_win + 0.25 * voice_win`,
where `mechanical` is the mean of five zero-model checks — the page renders,
every brand colour appears, the brand font is referenced, nothing overflows at
375px, the section count matches the brief
(`dspy-agent-skills:skills/dspy-book-coding-agents/SKILL.md:96-108`). "Noise-free
signal is worth more per unit than judge signal." For a `SKILL.md`, the
noise-free half already exists here: `check_skills.py`'s frontmatter checks
(spec fields, the name, the 1536-character limit) are exactly the "renders /
fits the brief" layer, at zero LM cost, and belong in the evaluator before any
judge call runs.

**Make the quality bar a 20-case adversarial benchmark, not a rubric.** Each
case is three fields (`dspy-agent-skills:skills/dspy-book-coding-agents/SKILL.md:66-89`):

| field | what it is |
|---|---|
| `task` | a terse, deliberately under-specified request — "that's when the model's defaults leak" |
| `antipattern` | the specific habit the task is designed to elicit |
| `tell` | the concrete observable the judge looks for |

"Under-specification is the design principle. A fully specified task tests
whether the model can follow instructions; an under-specified one tests what
it does when the instructions run out, which is what a conventions file is
for." For job 4, a case is not invented from a rubric — it is a real
transcript where an agent picked the wrong skill or none, which is exactly
what item 4 of `NOW.md`'s handover is collecting (above).

**The verdict is binary, and an unparseable one raises rather than scoring
zero:**
```python
VERDICT_RE = re.compile(r"VERDICT:\s*(PASS|FAIL)", re.IGNORECASE)

def parse_verdict(text: str) -> bool:
    """Binary verdict; an unparseable judge raises rather than scoring zero."""
    match = VERDICT_RE.search(text)
    if not match:
        raise ValueError(f"judge returned no parseable verdict: {text[:60]!r}")
    return match.group(1).upper() == "PASS"
```
(`dspy-agent-skills:skills/dspy-book-coding-agents/example_artifact_optimizer.py:23,82-86`.)
"Carried over from running tests to checking conventions — binary, no Likert
scale to drift on" (`SKILL.md:91-94`). This is the same rule P15 states for
this repository generally: a judge that cannot parse its own verdict has not
scored the candidate, and folding that into 0 makes an unreachable judge look
exactly like a candidate that failed the check.

**Composite score, weighted 0.5 mechanical / 0.5 judged:**
```python
def evaluator_signature_ok(fn) -> tuple[bool, str]:
    """optimize_anything reads the evaluator's parameter NAMES, not positions."""
    params = list(inspect.signature(fn).parameters)
    if len(params) < 2:
        return False, "evaluator needs (candidate, example)"
    if params[1] != "example":
        return False, f"second parameter is {params[1]!r}, must be 'example'"
    return True, "signature accepted"

def composite_score(mechanical_checks: list[bool], judge_wins: list[bool]) -> float:
    mech = sum(mechanical_checks) / len(mechanical_checks) if mechanical_checks else 0.0
    judged = sum(judge_wins) / len(judge_wins) if judge_wins else 0.0
    return 0.5 * mech + 0.5 * judged
```
Both functions run unmodified on 3.3.1, pure Python, no `dspy`/`gepa` import —
verified with `example_artifact_optimizer.py --dry-run` in this session
(`dspy-agent-skills:skills/dspy-book-coding-agents/example_artifact_optimizer.py:61-69,90-94`).
A dict returned as `side_info` in place of a plain reason is also worth
guarding directly: `side_info_is_useful()` there accepts a dict only if some
key's name contains "reason" or "judge" — a naming heuristic, not a content
check (`example_artifact_optimizer.py:103-106`); do not mistake passing it for
having supplied a real judge rationale.

**Steps, applied to a skill pack**
(`dspy-agent-skills:skills/dspy-book-coding-agents/reference.md:146-158`):
capture real routing failures; write each as task/antipattern/tell,
under-specified; score binary with a judge that raises on an unparseable
verdict; add every deterministic check (frontmatter, length, required
sections — `check_skills.py`) and weight it above the judge; optimize,
re-score, read the regressions, restore what the benchmark did not cover.
"Steps 1, 2 and 4 are worth doing even if you never run the optimizer: a
convention file with a benchmark attached is falsifiable, and one without is
an opinion." That is true here before job 4 has a dataset at all — the first
three of those five steps need no model and no key.

## `dspy.GEPA` versus `optimize_anything`

| | `dspy.GEPA` | `gepa.optimize_anything` |
|---|---|---|
| evolves | `pred.signature.instructions` of each predictor in a `dspy.Module` (`api.md`) | a `str` or `dict[str, str]` — no DSPy program underneath |
| evaluator / metric | 5-argument metric, `(gold, pred, trace, pred_name, pred_trace)`, returning a float or `dspy.Prediction(score, feedback)` (`api.md`) | a plain callable `(candidate, example) -> (score, side_info)` |
| `reflection_lm` | required at **construction**, or `AssertionError` — no default (`SKILL.md`, facts-that-bite item 5) | defaults to `"openai/gpt-5.1"` — a live call unless overridden (above) |
| package | `dspy.teleprompt.gepa` (part of `dspy`) | the standalone `gepa` package, imported directly, not through `dspy` |

**"A `SKILL.md` is not a program"** — job 4's own framing for why it needs the
second row rather than the first
(`Plan/concept/dspy-toolchain_2026-09-23.md:307-314`). The `dspy-agent-skills`
reader's version of the same rule: "When the artifact is prose rather than a
DSPy program, there is nothing to compile, so GEPA's standalone entry point
takes the file's text as the candidate." "If you do have signatures, use
`dspy.GEPA` instead so each predictor gets its own instruction slot" — its
own worked counter-example is a notebook with real DSPy signatures, correctly
routed to `dspy.GEPA`, not `optimize_anything`
(`dspy-agent-skills:skills/dspy-book-coding-agents/SKILL.md:26-32,61-64`).

**`dspy-auto-gepa` cannot do this job at all.** It drives `dspy.GEPA` over a
`dspy.Module` end to end and nothing else —
`dspy.GEPA(metric=self.load_metric(), auto=..., reflection_lm=...).compile(task_module, trainset=..., valset=...)`
is the whole optimize step
(`dspy-auto-gepa:src/dspy_auto_gepa/runner.py:330-343`) — so it has no path
for a bare text artifact
(`Plan/concept/dspy-toolchain_2026-09-23.md:309-311`).

**`dspydantic` cannot drive GEPA either, in the other direction: its own
metric shape does not fit GEPA's contract.** Its field-description optimizer's
metric is
```python
def single_field_metric(
    example: dspy.Example, prediction: dspy.Prediction, trace: Any = None
) -> float:
```
(`dspydantic:src/dspydantic/optimizer.py:702-704`) — three arguments, no
`pred_name`/`pred_trace`, so it cannot bind against `dspy.GEPA`'s 5-argument
protocol and carries no `feedback` for a reflector to read even if it could.
It drives `BootstrapFewShot`/`MIPROv2` instead (next section). Neither package
reaches `optimize_anything` — one has no text-artifact path, the other has no
GEPA-shaped metric.

## Field descriptions and schemas as prompts (`dspydantic`)

`dspydantic` optimizes Pydantic field descriptions with DSPy's classic
optimizers, not GEPA. For each field it builds a fresh `dspy.Signature`
*class*, at runtime, naming it after the model:
```python
docstring = (
    f"Improve a field description for {model_name} structured data extraction. "
    f"Output ONLY the improved description — a short descriptive phrase, "
    f"not instructions."
)

# Dynamic class name gives the proposer domain signal for free
cls = type(f"Optimize{model_name}FieldDescription", (dspy.Signature,), {
    "__doc__": docstring,
    "field_name": dspy.InputField(desc="Name of the field being optimized"),
    "field_description": dspy.InputField(desc="The current field description to improve"),
    "field_type": dspy.InputField(desc="The data type of the field"),
    "optimized_field_description": dspy.OutputField(desc="..."),
})
```
(`dspydantic:src/dspydantic/module.py:67-92`, trimmed.)

**The comment is wrong, measured.** "Dynamic class name gives the proposer
domain signal for free" claims the class name (`OptimizeInvoiceFieldDescription`)
carries context at no cost. It does not: **in DSPy 3.3.1 a signature's class
name never reaches the LM, in any call the proposer or the task predictor
makes** — only the docstring and the input field values do
(`dspydantic:src/dspydantic/module.py:73`, contradicted by its own repository's
measurement of every proposer request). For job 4 the rule is the same shape
in reverse: **put the skill's domain in the instruction text — the `objective`
string, the docstring, an input field — never in a Python identifier, a
variable name, or a dynamically-built class name.** Nothing downstream reads
those.

**Which optimizer, chosen purely by example count, with no model call:**
```python
def _auto_select_optimizer(self) -> str:
    num_examples = len(self.examples)
    if num_examples <= 2:
        return "miprov2zeroshot"       # avoids a BootstrapFewShot bug
    elif num_examples < 20:
        return "bootstrapfewshot"
    else:
        return "bootstrapfewshotwithrandomsearch"
```
(`dspydantic:src/dspydantic/optimizer.py:512-533`, trimmed; runs on 3.3.1.)
No branch reaches GEPA — consistent with the metric shape above. For 5 to 20
job-4 cases this rule would pick `bootstrapfewshot`, which is not what job 4
needs: BootstrapFewShot tunes **demos** for a program, it does not rewrite the
instruction text itself, so it is the wrong tool for optimizing a
`description` string even before the metric-arity mismatch rules it out.

**What its own numbers show: nothing measured.** The headline claims —
"Typical improvement: 10-30% higher accuracy", "Accuracy: 68% → 94%" — carry
no run, seed, or log. Its `ABLATION_RESULTS.md` looks like a benchmark but its
source script says otherwise in its own comment: `examples/ablation_benchmark_mock.py`
never calls `optimize()` ("We're not actually running optimize()"), and
hardcodes `baseline_score = 0.75`, a `quality_factor = 1.2` for the sequential
mode, and the compile counts it reports
(`dspydantic:examples/ablation_benchmark_mock.py:169,177,181,224-227`). This is
not "the repository's claim; not run here" — it is the repository's own script
admitting it did not run what it reports. The lesson for job 4 carries
directly: a benchmark script that never calls the optimizer is invisible from
its printed output, which is exactly why `optimize_anything`'s own regression
list (above) is read from a real second scoring pass, never from the
optimizer's internal cached numbers alone.

## Prompt patching loops (`dspy-optimizer`), and why identifiers must be `Literal`s built by code

`patterns.md` has the full mechanism and this repository's verdict on
`dspy-optimizer`'s critique-repair loop — Evaluator → Refiner →
`BlockBasedMerger` → Validator, patching a `### Block`-structured prompt
string by name, refused for job 4 because it validates on the same set it
optimizes against and its validators pass on an empty comparison. One of its
own defects is worth developing on its own here, because the lesson is
general to any job-4 loop that asks a model to name something, not only to
this one package's loop:

```python
# dspy_optimizer/refiner/signature.py:137 — the field the model fills in
operation: str = dspy.OutputField(desc="The operation to perform: 'append' or 'replace'.")

# dspy_optimizer/optimizer.py:141 — where the string is trusted
patch = PromptPatch(target_block=refiner_output.target_block,
                     operation=PatchOperation(refiner_output.operation),   # "Append" -> ValueError
                     content=refiner_output.content)
```
`PatchOperation.APPEND`/`.REPLACE` are the lowercase strings `"append"`/`"replace"`
(`dspy-optimizer:dspy_optimizer/models.py:22-25`); `operation` is a bare `str`,
so nothing stops the model writing `"Append"`, and nothing in `optimize()`
catches the `ValueError` that follows — one bad field crashes the whole run
(`dspy-optimizer:dspy_optimizer/optimizer.py:139-146`,
`dspy_optimizer/refiner/signature.py:137-138`). **A bare `str` field lets a
close-enough answer through the type system and crash somewhere else
instead.** Declared as `Literal["append", "replace"]`, the same wrong value
would fail at **parse time** — an `unparsed` result, the same status
`lmrun.call` already gives any out-of-set `Literal` answer (`api.md`'s
Literal-parsing rule) — never a raised `ValueError` deep inside application
code. The fix is not "ask the model more carefully": build the `Literal`'s
members from what the document's real choices are, in code — block names
read off the actual file, never hand-typed or guessed (P26, the same shape as
`read.py --find`: ask for the identifier, do not type it) — and let the
adapter refuse anything else.

Not adopted here as a loop. The `Literal`-built-identifier lesson applies to
any structured field a job-4 evaluator or refiner would ask a model to fill
in.

## `dspytools` and `dspy-skills-implementation` — what each does here

Two separate packages make a `SKILL.md` reachable by a ReAct agent instead of
only by a person, installed for that purpose and not yet called by anything
(`CLAUDE.md:716-719`, "Installing anything").

**The runtime half — `dspy-skills-implementation-`, installed `--no-deps` into
`.venv-dspy`, plus `strictyaml`.** `dspy_skills.SkillManager([Path(".agents/skills")])`
discovers every skill here; `generate_skills_prompt_block(manager)` renders
the `<available_skills>` block a ReAct agent is given, **built from the
`description` field and nothing else**; `activate(name)` reads one skill's
full `SKILL.md` (`CLAUDE.md:695-700`). This repository's one live caller is
`scripts/rlm_ingest.py`:
```python
def briefing(skill: str = "ingest") -> tuple[str, str]:
    """(the skills block every agent sees, the one skill's full instructions)."""
    from dspy_skills import SkillManager, generate_skills_prompt_block, read_instructions
    manager = SkillManager([SKILLS])
    manager.discover()
    loaded = manager.activate(skill)
    return generate_skills_prompt_block(manager), read_instructions(loaded.path)
```
(`scripts/rlm_ingest.py:155-161`.) This is why the description is job 4's
target and not the body of the file: it is the only part of a skill any agent
sees before choosing it — `SkillManager` never reads further until `activate`
is called. `--no-deps` matters because the package declares
`dspy-ai>=2.5.0`, the pre-3.x distribution name, and resolving it normally
would move `.venv-dspy` off the pinned DSPy 3.3.1.

**P6 has a direct consequence here.** The vendored `jev*` folders under
`.claude/skills/` are real, unlinked folders specifically so that
`SkillManager`'s discovery — which walks `.agents/skills/`, not
`.claude/skills/` — never renders them into an agent's prompt at all
(`CLAUDE.md:664-668`; `scripts/check_skills.py:15-21`). A project skill that
were a real folder instead of the required symlink would have the opposite
problem: `check_skills.py`'s `links()` check would fail it, but nothing about
`SkillManager` itself would notice either copy drifting from the other.

**The management half — `dspytools`, its own venv (`.venv-dspytools`, Python
3.12 — it refuses 3.11).** List, search, compile and optimize skills as
artifacts:
```bash
DSPYTOOLS_SKILLS_DIR=$PWD/.agents/skills .venv-dspytools/bin/dspytools skills list
```
(`CLAUDE.md`, "Installing anything".) Installed, reachable, not called by
anything here — "Nothing in the pipeline calls any of the three yet. They are
installed, reachable, and measured against this repository."
(`CLAUDE.md:716-718`; the third is `drg-kg`, unrelated to job 4).

**A naming collision worth flagging.** `dspy-agent-skills` also ships a skill
called `dspy-tools-cli` (`skills/dspy-tools-cli/`), teaching an agent to call
a different, hypothetical "DSPy Tools" service — a per-command lookup of
which backing service a command needs
(`dspy-agent-skills:skills/dspy-tools-cli/example_tools_cli.py:22-61`). It
shares nothing but the name with the `dspytools` package installed here; do
not conflate the two when reading the notes.

## Not taken, or waiting

| idea | from | waits for |
|---|---|---|
| running `optimize_anything` on `.agents/skills/dspy`'s own descriptions | `dspy-agent-skills` | 5–20 recorded routing failures (P4) — `NOW.md:235-237`, above |
| `dspy-auto-gepa` for this job | — | nothing: it only drives `dspy.GEPA` over a `dspy.Module`, and job 4's artifact is not one |
| `dspydantic`'s optimizer stack (`BootstrapFewShot`/`MIPROv2ZeroShot`) for a `description` field | `dspydantic` | nothing planned: its metric cannot drive GEPA and its own numbers are unmeasured; `optimize_anything` already fits without it |
| block-structured patching of `SKILL.md`'s own `##` sections, instead of regenerating the whole file | `dspy-optimizer` | a job-4 loop that exists at all; the `Literal`-built-block-name lesson applies regardless of whether patching itself is adopted |
| `dspy.RLM`-based skill discovery — cluster past session transcripts, write a candidate `SKILL.md` for the largest cluster, skip groups under 2 sessions, hand the result to a person before install | `dspy-agent-skills:skills/dspy-book-coding-agents/SKILL.md:132-139` | a corpus of session transcripts to point it at; none is collected here today |
| a smoke budget (`max_metric_calls=3`) beside the real run, to catch the `example` trap and the fence trap before spending the full budget | `dspy-agent-skills:skills/dspy-book-coding-agents/reference.md` | a first real `optimize_anything` run |

**What job 4's own numbers, once it runs, should not be compared against:**
the chapter's are "small budgets producing real but bounded gains, on
benchmarks the authors built" — one persona run reached 0.962 composite
rubric adherence at 50 metric calls in about 19 minutes, the landing-page loop
used 200 metric calls in about 30 minutes
(`dspy-agent-skills:skills/dspy-book-coding-agents/SKILL.md:141-147`). "Measure
your own baseline; do not import theirs" — the same rule P17 states for this
repository generally (benchmark the real thing, not a number carried over
from someone else's task, model, and data).
