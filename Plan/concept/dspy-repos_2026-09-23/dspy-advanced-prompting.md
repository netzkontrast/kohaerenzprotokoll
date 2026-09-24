# Scan report: `dspy-advanced-prompting` for kohaerenzprotokoll

Repo: `/home/user/dspy-advanced-prompting` (read-only scan; local git history present,
9 commits, org `evalops`, no CI file found).

## 1. What it is

A demo/portfolio repo: 11 "prompting techniques used by top AI startups," each as a
`dspy.Module` wrapping mostly prompt text plus Pydantic schemas, with a Jupyter-notebook
tour and two validation scripts. **It is a toy.** "FULLY VALIDATED ✨" in the README means
"all classes import and instantiate," not "outputs are correct" — no test asserts model
output quality. `setup.py`/`requirements.txt` pin `dspy-ai>=2.4.0` (the retired PyPI name),
but I confirmed by running the actual code (`uv run --with dspy==3.3.1 …`) that every
module in `src/` imports cleanly and runs its non-LM code paths under DSPy **3.3.1**, the
version the target has installed — the version pin in the metadata is simply stale/wrong,
not a real incompatibility. No committed test suite (`pytest` is a dependency but nothing
under `tests/`); `test_notebooks.py` and `validate_with_dspy.py` are the only checks, both
offline/no-key. `validate_with_real_api.py` needs `OPENAI_API_KEY` and calls `gpt-4o-mini`
— never run here.

## 2. Every good idea (techniques in `src/techniques/` + `src/prompts/`)

Format: name — description — evidence — tag.

1. **Manager-style hyper-specific prompt** — a Jinja2 template turns a `RolePersona`-like
   config (title, responsibilities, metrics, escalation, examples-of-excellence) into a
   multi-page onboarding-doc prompt. `src/prompts/manager_style.py:1-70` (template),
   `MANAGER_PROMPT_TEMPLATE`. **Prompt text**, real mechanism only in the sense that Jinja2
   renders it. `[catalogue]` — verbose persona prompts are exactly what the target's
   PRINCIPLES forbid speculating about without instances (P3/P4); the target has no
   "manager" job.
2. **Role prompting / persona library** — `RolePersona` Pydantic model +
   `PersonaAgent.forward`; personas carry `knowledge_boundaries` (what the persona doesn't
   know). `src/techniques/role_prompting.py:23-31,44-60`. **Prompt text.**
   `[catalogue]` — the `knowledge_boundaries` field is a nice small idea (an explicit
   "may not" list baked into the persona) that echoes the target's "may not" construct
   convention; not needed as a runtime module.
3. **Task planning / decomposition** — `TaskPlan`/`SubTask` Pydantic schema with
   dependencies, acceptance criteria, `potential_issues`; `TaskPlanner.forward` asks the
   model for `task_plan_json` and (per validate script) presumably parses it.
   `src/techniques/task_planning.py:27-56,71-90`. **Prompt text + schema; the model is
   asked to invent the dependency graph itself**, nothing verifies acceptance criteria
   were met. `[skip]` for the target — the target's DAG (fetch→census→note→reconcile) is
   already fixed and script-driven; a model-planned DAG would violate P1 (decidable things
   are programs).
4. **Structured output validators — the one real mechanism in the repo.**
   `validate_xml` wraps output in `<root>` and calls `ET.fromstring` (real parse, real
   failure mode); `validate_json` calls `json.loads` in a try/except; `validate_hybrid`
   uses a regex `##\s*{tag}.*?<{tag}>(.*?)</{tag}>` and reports **which required section is
   missing** rather than silently returning partial credit.
   `src/techniques/structured_output.py:111-137,174-217`. `[adapt]` — this is the closest
   thing here to the target's "guard reports what it could NOT check" (P23): a validator
   that names the missing section, not a score. Directly relevant to entity-list output
   parsing if a model is ever asked to emit XML/JSON instead of free text (see §3).
5. **Meta-prompting / self-optimization** — `PromptAnalysis`/`PromptOptimizationResult`
   schemas; `MetaPromptOptimizer` asks the model to critique then rewrite its own prompt,
   returns `analysis_json` as an opaque string with no parsing/validation shown.
   `src/techniques/meta_prompting.py:15-30,73-103`. **Prompt text, ungrounded** — the
   "analysis" is whatever JSON-shaped string the model returns; nothing checks it parses.
   `[skip]` — DSPy's own optimizers (BootstrapFewShot/GEPA, already on the target's ladder)
   do this properly with a real metric; this hand-rolled version has none.
6. **Few-shot with quality tiers** (`GOLD`/`SILVER`/`BRONZE`/`CHALLENGING`) and a
   `select_examples` that always includes challenging cases first.
   `src/techniques/few_shot.py:16-20,77-92`. **Real, simple selection logic** (not just
   prompt text) but the "quality" labels are asserted by the author, not measured.
   `[adapt]` — the *tiering idea* (mark a labelled example as "challenging" and guarantee
   it is included) is directly useful for `Plan/trainsets/surface-pairs.jsonl`'s
   `Negentropie`/`Entropie` never-merge case: force known hard negatives into every
   few-shot prompt rather than relying on random/similarity selection.
7. **Prompt folding** (recursive/pipeline/branching/parallel/adaptive strategies; a model
   generates sub-prompts from a parent prompt). `src/techniques/prompt_folding.py:16-22,
   44-51`. **Prompt text generating more prompt text**, no verification the children are
   sound. `[skip]` — directly conflicts with "never reached != answered badly" (P15) style
   caution; a model deciding its own next steps is exactly the kind of undecidable-treated-
   as-decidable pattern the target avoids.
8. **Escape hatches / uncertainty guidelines** — an 8-point prompt telling the model how to
   hedge, paired with `UncertaintyDetector.detect_uncertainty`, a **keyword-matching**
   classifier over phrases like "might"/"I don't know" that maps to a hand-picked
   confidence number (0.0/0.2/0.5/0.7/0.95). `src/techniques/escape_hatches.py:60-96,
   158-203`. **Half prompt text, half fake mechanism**: the "confidence score" is not
   calibrated to anything, it is a lookup table keyed on which hedge word appeared first.
   `[skip]` as a scoring mechanism (would violate P24, "done is a measurement" — this
   measurement measures word choice, not correctness); `[catalogue]` the *prompt text
   itself* (the "ADMISSION OF UNCERTAINTY … never make up facts" guidelines block,
   lines 161-203) as a possible instruction fragment for a future entity-list prompt that
   asks the model to skip entities it isn't sure about, rather than to guess. The target
   already has a stronger, code-side version of the underlying idea: `read.py --find`
   refuses and names the nearest line instead of a model self-reporting confidence.
9. **`GracefulDegradation`** — if the (fake) confidence is below a threshold, swap in a
   templated "here's what I know / don't know / need" response instead of the model's
   answer. `src/techniques/escape_hatches.py:229-293`. `[skip]` — built on idea 8's
   ungrounded confidence number, so the trigger condition is unreliable; the *shape*
   (fallback template on low confidence) is already superseded by the target's `--find`
   pattern which refuses deterministically rather than via a learned/heuristic threshold.
10. **`HallucinationPreventer`** — regex-scans a response for suspicious patterns (bare
    years, `%`, `$amounts`, "according to", "study shows", >2 absolute words like
    always/never) and appends a disclaimer if found. `src/techniques/escape_hatches.py:
    296-339`. **Real (if crude) static check**, but it flags shape, not truth, and never
    blocks anything — the disclaimer is emitted alongside the unverified claim rather than
    withholding it. `[catalogue]` as a "things that look like citations but weren't
    checked" pattern-list — mildly relevant to the target's insight that "a citation that
    looks precise around a sentence the document never contained is the worst shape a
    defect takes" (quotes.py's whole reason for existing), but this module doesn't verify
    against a source, it only flags surface form.
11. **Domain-keyword disclaimers** (`ContextualEscapeHatch`) — regex/keyword-detect
    medical/legal/financial/safety/personal domain and prepend a canned disclaimer.
    `src/techniques/escape_hatches.py:371-407`. **Prompt text + keyword lookup.**
    `[skip]` — no analogue needed; the target's corpus is not advice-giving.
12. **Model distillation pipeline** — `DistillationConfig`, `ModelProfile` cost/latency
    table, `DistillationStrategy` enum (direct/synthetic/chain/selective/ensemble), async
    `distill_and_deploy`. `src/techniques/model_distillation.py:20-52,90-131,472+`.
    **Mostly scaffolding/dataclasses; the actual distillation is more prompt text** (ask
    the teacher model to produce training examples, no real fine-tuning or verified
    transfer). `[catalogue]` only the *cost/latency profile table idea* (`ModelProfile`)
    — a "which model for which job, with real measured tokens/sec and $/1k" table is
    exactly the accounting the target wants for LM calls (open problem: "cost/trace
    visibility of LM calls") but this repo's version has example numbers, not measured
    ones.
13. **Thinking traces / debug logging** — a small real parser: `parse_thinking_trace`
    splits lines and matches literal tag prefixes (`[THOUGHT]`, `[HYPOTHESIS]`,
    `[VERIFICATION]`, `[DECISION]`, `[ERROR]`, `[INSIGHT]`) into a `ThoughtNode` tree with
    hand-assigned confidence per tag type (e.g. hypothesis=0.7, insight=0.9 — again
    asserted, not measured). `src/techniques/thinking_traces.py:166-210`. **Real, simple
    string parsing** (a legitimate small mechanism), rendered with `rich.Tree` for
    display. `[adapt]` — the *parsing pattern* (fixed tag vocabulary → typed node) is
    reusable as a code-side format for a model's rationale-before-decision output in the
    one-term-or-two judgement (job 1), as long as it stays a debug/display aid and the
    confidence numbers are never treated as real probabilities (they aren't here).
14. **Evaluation framework — test-cases-as-first-class-artifact idea (good), scoring
    machinery (broken).** `EvaluationSuite`/`TestCase` with `TestCaseType`
    (functional/edge_case/adversarial/performance/regression/consistency/robustness) is a
    genuinely useful taxonomy and the README's stated philosophy ("test cases are more
    valuable than prompts") matches the target's P27 (score against human ceiling).
    `src/evaluations/evaluation_framework.py:24-58,320-393`. `[adopt]` the *taxonomy and
    "test suite is a first-class saved artifact"* idea — maps onto the target's
    `Plan/runs/<slug>/` "every step keeps its artifact" convention and
    `Plan/trainsets/surface-pairs.jsonl`'s labelled-example format. See §4 for the parts
    to explicitly avoid.
15. **A/B test framework with a t-test approximation** for comparing two prompt variants
    over N runs. `src/evaluations/evaluation_framework.py:396-445`. Uses `pooled_std` and
    a fixed `|t|>2.0` cutoff, no real degrees-of-freedom correction, `num_runs` default 5.
    `[skip]` at n=5 — the target's own brief says "n=26 is small data; anything needing
    100+ examples is irrelevant," and this A/B tester is even more sample-starved and
    invents its own ad hoc significance test rather than using a real one (e.g.
    `scipy.stats`). Not worth borrowing; if significance testing is ever wanted, use a
    real library, not this.
16. **Regression test runner against a JSON baseline file**, 5%-drift threshold triggers
    "regression"/"improvement" per metric. `src/evaluations/evaluation_framework.py:
    448-503`. `[adapt]` — the *idea* (persist a baseline result file, diff future runs
    against it, name each metric that moved) is close in spirit to `judgements.py`'s
    replay-and-diff pattern already in the target, and to `state.py --check`'s
    drift-detection framing. The target already does this better (named judgements with
    `agrees`/`DISAGREES`/`judgement` rather than a numeric ±5% band), so treat this as
    confirmation of an approach already chosen, not new code to take.
17. **`create_evaluation_report`** — renders results to Markdown with per-metric numbers
    and a "Failed Tests" section (first 5 only, silently truncated).
    `src/evaluations/evaluation_framework.py:506-538`. `[catalogue]` — truncating to 5
    without saying "and N more" is a small anti-pattern (silently hides how many failed);
    if adapted, keep a total count visible — the target's own quotes.py/state.py convention
    of "say how many you could not check" is stricter and better.
18. **Offline-first validation script pattern** — `validate_with_dspy.py` never calls an
    LM; it (a) checks deps, (b) instantiates every module, (c) runs one keyword-based
    function (`detect_uncertainty`) and one string parser (`parse_thinking_trace`) as
    "functionality," (d) reports whether API keys are present, without requiring them to
    pass. `validate_with_dspy.py:11-266`. `[adapt]` the *shape* — "one script, no key
    required, exercises real code paths without hitting the network" matches the target's
    P5 (every workflow ships an offline, no-key fixture) — but note in §4 that this script
    overstates what it proves ("FULLY VALIDATED" for zero LM calls).
19. **Real-API validation script with response-quality heuristics** (keyword checks like
    "has_empathy"/"has_solution" on the manager-style response).
    `validate_with_real_api.py:44-83`. `[skip]` — keyword-presence is not a real
    correctness check, and this needs a live `OPENAI_API_KEY`/`gpt-4o-mini`, which the
    target's rules forbid running with real key without the author's explicit yes for
    corpus text; also not offline so it can't serve as a CI fixture.
20. **Notebook self-test** (`test_notebooks.py`) — parses `.ipynb` JSON directly (no
    nbclient/execution), checks for `sys.path.append`+`load_dotenv` boilerplate and an
    `if not api_key` guard string in source. `test_notebooks.py:10-58`. **Structural check
    only — never executes a cell.** `[skip]` — too weak to be worth adapting; a "does the
    notebook literally contain this substring" check is not a test.

## 3. Directly reusable for the target's jobs 1-4 / open problems

- **Job 1 (one-term-or-two, `fold()` + judgements ladder)**: idea 6 (few-shot tiering that
  force-includes challenging/hard-negative examples) is the one piece worth lifting
  conceptually — apply it to `surface-pairs.jsonl` so `Negentropie`/`Entropie` and any
  other known-hard negative is always in the few-shot context, not left to
  similarity-based sampling. Nothing here should be copied as code (DSPy's own
  `LabeledFewShot`/`BootstrapFewShot`, already on the ladder, subsumes it); take the
  *policy* — "always include the labelled hard negatives" — not the module.
- **Job 2 (entity lists — model names entities, code finds lines)**: idea 4's
  XML/JSON structured-output validators are the most directly transferable *code*: if the
  entity-naming prompt is ever changed to ask for `<entity>…</entity>` or a JSON list
  instead of free text, `validate_json`/`validate_xml` (real `json.loads`/`ET.fromstring`,
  real failure reporting) are a fine drop-in parse-and-report step — small, dependency-free
  beyond stdlib `xml.etree`. Idea 8's uncertainty-admission *prompt text* (not the fake
  confidence scorer) could be adapted into the entity-naming prompt as "list only entities
  you can point to in the text; omit ones you are guessing at" — this is compatible with
  P12/P26 (model never types a line number, only names) and reduces false positives.
  Nothing here does what the target's `entities.py verify` does (checking a claimed entity
  against a specific cited line) — that mechanism does not exist in this repo at all.
- **One-term-or-two / judgement UI**: idea 13's tag-based parser (`[THOUGHT]`,
  `[VERIFICATION]`, `[DECISION]`) is a reasonable, cheap format if a judgement DSPy module
  is ever asked to show its reasoning in a fixed, code-parseable shape rather than free
  prose — but it must stay a debug/inspection aid, never a source of a written rule (the
  target's own record is `Plan/runs/judgements.jsonl`, which already has `rule` in words
  written by a person).
- **Job 3 (`rlm_ingest.py`, RLM-based census)**: nothing here targets multi-candidate
  extraction with verified line citations; idea 4's structured-output validators are again
  the only piece that would help — reporting "required section X missing" if the census
  output format is ever XML/JSON-tagged instead of Markdown.
- **Job 4 (skill-description optimization via GEPA)**: nothing in this repo touches GEPA
  or skill descriptions at all; idea 5 (meta-prompting) is a naive hand-rolled analogue
  with no real metric, and the target's plan (GEPA's `optimize_anything` on the
  `description` field via `dspy-book-coding-agents`, per the target CLAUDE.md) is already
  the correct, better-grounded approach.
- **Open problem — cost/trace visibility of LM calls**: idea 12's `ModelProfile`
  (cost-per-1k-tokens, tokens/sec fields) is a plausible schema shape for a future
  accounting table, but this repo's numbers are illustrative, not measured — would need
  to be rebuilt from real target LM calls, not copied with its example values.
- **Open problem — reviewed-page-vs-new-source conflicts, stale reconciliations**: nothing
  in this repo addresses either; no analogue exists.

## 4. Conflicts with the target's principles (traps to name, not to copy)

- **A metric that cannot fail** (P24 violation, matches the target's own retired-pipeline
  cautionary tale about `coverage()` returning 1.0 with no gold fragments):
  `EvaluationMetrics._calculate_metrics` sets `edge_case_performance = 1.0` and
  `robustness_score = 1.0` whenever the suite happens to contain **zero** test cases of
  that type (`evaluation_framework.py:235-236`), and `consistency_score = 1.0` whenever
  there are fewer than 2 same-typed scores to compare (`:238-243`). A suite with no edge
  cases silently reports perfect edge-case performance. This is exactly the shape the
  target's own SIGNAL 987/967-on-nothing-passed story warns against.
- **`test_coverage` measures nothing**: computed as
  `len(results) / len(suite.test_cases)` where `results` is built by iterating
  `suite.test_cases` in the same call (`evaluation_framework.py:113-127,267`) — it is
  always 1.0 by construction. A vacuous number presented as a real metric.
- **Model types identifiers/confidence, code trusts it** (P12/P26-style violation): the
  entire escape-hatches "confidence" number (idea 8) is a keyword lookup dressed as a
  probability, then fed into `GracefulDegradation`'s threshold logic as if it were
  calibrated. Nothing verifies the mapping; a model's hedge-word choice silently becomes a
  numeric decision boundary.
- **Silent truncation, not a refusal**: `create_evaluation_report` and
  `_display_results` both hard-cut failed-test lists to `[:5]` with no "N more omitted"
  note (`evaluation_framework.py:305-317,530-535`) — the opposite of the target's P23
  ("a guard reports what it could NOT check"): here the guard just stops looking and says
  nothing about it.
- **Caching is not addressed at all** (target's P18: "repeats, cache off"): `.env.example`
  sets `DSPY_CACHE_DIR=.dspy_cache` as a default, on by default, with no discussion of when
  to disable it for repeat-run evaluation; the evaluation/A-B/regression code never
  mentions cache state, so a "5 runs" A/B test (idea 15) could be measuring 1 real call and
  4 cache hits without anyone noticing.
- **"FULLY VALIDATED" overclaim**: README and `validate_with_dspy.py` label the project
  validated after only import + one keyword function + one string parser, with **zero**
  LM calls (confirmed: no `dspy.settings.configure(lm=...)` anywhere in that script).
  `validate_with_real_api.py` is the only script that ever calls a model, needs a live
  OpenAI key, and is not run automatically. This is the "claim outran what exists" failure
  mode the target's own CLAUDE.md names directly.
- **No offline fixture for the one real-API path**: `validate_with_real_api.py` cannot run
  without `OPENAI_API_KEY` and makes real, priced calls (`gpt-4o-mini`) — there is no mock
  LM or recorded-response fixture, unlike the target's P5 requirement that every workflow
  ship an offline, no-key fixture.
- **Ungrounded confidence scores throughout** — idea 8's mapping (LOW=0.7, MEDIUM=0.5,
  HIGH=0.2, UNABLE=0.0) and idea 13's per-tag confidence (hypothesis=0.7, insight=0.9) are
  both hand-picked constants presented as if measured, with no calibration data behind
  them anywhere in the repo.

## 5. Dependencies & cost

- **Runtime deps** (`requirements.txt`/`setup.py`): `dspy-ai>=2.4.0` (old PyPI name; I
  verified the actual code runs unmodified on `dspy==3.3.1`, the current name/version, so
  this is a stale label, not a real blocker), `openai>=1.0.0`, `anthropic>=0.18.0`,
  `pydantic>=2.0.0`, `jinja2>=3.1.0`, `pytest>=7.0.0`, `python-dotenv>=1.0.0`,
  `rich>=13.0.0`, `loguru>=0.7.0`, `jsonschema>=4.0.0`, plus `jupyter`, `matplotlib` for
  the notebooks. `python_requires=">=3.8"`.
- Everything except the two real-API scripts is **standard-library + pydantic + jinja2 +
  rich + loguru**, all pure-Python, small installs, no compiled deps beyond numpy (used
  only in `evaluation_framework.py` for `np.mean`/`np.std`, trivially replaceable with
  stdlib `statistics`). I confirmed a clean `uv run --with dspy==3.3.1 --with pydantic
  --with jinja2 --with rich --with loguru --with numpy --with pytest` import of every
  module in `src/` with no errors and no network access — this can live comfortably
  inside (or alongside, in a scratch venv) the target's `.venv-dspy` (DSPy 3.3.1) without
  moving that pin, if any single idea above is ever lifted as code.
- **API keys**: only `validate_with_real_api.py` and `main.py`'s live paths need
  `OPENAI_API_KEY` (optionally `ANTHROPIC_API_KEY`); nothing else in the repo calls a
  model. I did not set or use any key.
- **Cost to adopt anything here is near zero** (no new heavy dependency), but the
  *value* is almost entirely in ideas/patterns (§2 items 4, 6, 13, 14, 18), not in code
  worth vendoring wholesale — most modules are prompt-text wrappers the target's own
  DSPy signatures would need to reimplement from scratch anyway to keep P12/P26/P19 (quote
  don't paraphrase, German assertion) compliance, which this English-only repo never
  addresses (no non-English test case anywhere, no German handling at all).

## 6. Verdict

The single most valuable thing to take is the **structured-output validator pattern**
(idea 4: real `json.loads`/`ET.fromstring` parsing that names the specific missing
section rather than scoring it) combined with the **few-shot hard-negative tiering idea**
(idea 6) — both are small, dependency-free, and slot into jobs 1 and 2 without importing
any of this repo's code. Leave the evaluation framework's metrics (broken by
vacuous-1.0 defaults and a fabricated test_coverage), every "confidence score" (idea 8,
13 — all hand-picked constants, none calibrated), the A/B t-test approximation (n=5,
homemade stats), and the "FULLY VALIDATED" framing entirely — none of it would survive
the target's own PRINCIPLES, and copying the framing risks reintroducing the exact
metric-that-cannot-fail failure the target has already learned to avoid once.
