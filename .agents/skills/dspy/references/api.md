# The DSPy 3.3.1 surface, as installed here

Everything on this page was read off the installed package
(`.venv-dspy`, DSPy 3.3.1, gepa 0.1.4, litellm 1.102.1) or run against it, on
2026-09-24. Two kinds of mark carry that:

- a line in a **`surface` block** — every parameter named exists on the installed
  callable and every default given is the installed default;
- **`[checked: <id>]`** after a sentence — a probe of that name in
  `scripts/check_dspy_skill.py` runs the behaviour offline and fails when it
  stops holding.

`.venv-dspy/bin/python scripts/check_dspy_skill.py` runs both. When DSPy moves,
that command names the sentence that became false; fix the sentence, not the
probe. What the scripts here *call* is a different, shorter list, asserted by
`scripts/check_dspy_surface.py`.

Evidence from the nine repositories is written `repo:path:line` at the commits
in `repos.md`. It is what that repository says, not what was run here, unless a
mark says otherwise.

## The surface this skill teaches

```surface
# language models and settings
dspy.LM(model, model_type="chat", temperature=None, max_tokens=None, cache=True, callbacks=None, num_retries=3, provider=None, use_developer_role=False)
dspy.BaseLM(model, model_type="chat", temperature=None, max_tokens=None, cache=True, callbacks=None, num_retries=3)
dspy.utils.DummyLM(answers, follow_examples=False, reasoning=False, adapter=None)
dspy.configure_cache(enable_disk_cache=True, enable_memory_cache=True, disk_size_limit_bytes=30000000000, memory_max_entries=1000000, restrict_pickle=False, safe_types=None)
dspy.inspect_history(n=1, file=None)
dspy.make_signature(signature, instructions=None, signature_name="StringSignature", custom_types=None)
dspy.load(path, allow_pickle=False)
dspy.Module.save(path, save_program=False, modules_to_serialize=None)
dspy.Module.load(path, allow_pickle=False, allow_unsafe_lm_state=False)
dspy.Module.batch(examples, num_threads=None, max_errors=None, return_failed_examples=False, provide_traceback=None, disable_progress_bar=False, timeout=120, straggler_limit=3)
# adapters
dspy.ChatAdapter(callbacks=None, use_native_function_calling=False, use_json_adapter_fallback=True)
dspy.JSONAdapter(callbacks=None, use_native_function_calling=True)
dspy.XMLAdapter(callbacks=None, use_native_function_calling=False, use_json_adapter_fallback=True)
dspy.TwoStepAdapter(extraction_model)
# modules
dspy.Predict(signature, callbacks=None)
dspy.ChainOfThought(signature, rationale_field=None)
dspy.ReAct(signature, tools, max_iters=20)
dspy.ReActV2(signature, tools, max_iters=20)
dspy.ProgramOfThought(signature, interpreter_factory, max_iters=3)
dspy.CodeAct(signature, tools, interpreter_factory, max_iters=5)
dspy.RLM(signature, interpreter_factory, max_iters=20, max_llm_calls=50, max_output_chars=10000, verbose=False, tools=None, sub_lm=None)
dspy.Flex(signature, interpreter_factory, tools=None, max_predictor_calls=100)
dspy.Refine(module, N, reward_fn, threshold, fail_count=None)
dspy.BestOfN(module, N, reward_fn, threshold, fail_count=None)
dspy.MultiChainComparison(signature, M=3, temperature=0.7)
dspy.Parallel(num_threads=None, max_errors=None, access_examples=True, return_failed_examples=False, provide_traceback=None, disable_progress_bar=False, timeout=120, straggler_limit=3)
dspy.PythonInterpreter(deno_command=None, enable_read_paths=None, enable_write_paths=None, enable_env_vars=None, enable_network_access=None, sync_files=True, tools=None)
dspy.Tool(func, name=None, desc=None, args=None, arg_types=None, arg_desc=None)
# retrieval
dspy.Embedder(model, batch_size=200, caching=True)
dspy.Embeddings(corpus, embedder, k=5, callbacks=None, cache=False, brute_force_threshold=20000, normalize=True)
# evaluation
dspy.Evaluate(devset, metric=None, num_threads=None, display_progress=False, display_table=False, max_errors=None, provide_traceback=None, failure_score=0.0, save_as_csv=None, save_as_json=None)
dspy.bootstrap_trace_data(program, dataset, metric=None, num_threads=None, raise_on_error=True, capture_failed_parses=False, failure_score=0, format_failure_score=-1, log_format_failures=False, capture_crashes=False)
# optimizers — optimizers.md has what each does and costs
dspy.LabeledFewShot(k=16)
dspy.LabeledFewShot.compile(student, trainset, sample=True)
dspy.BootstrapFewShot(metric=None, metric_threshold=None, teacher_settings=None, max_bootstrapped_demos=4, max_labeled_demos=16, max_rounds=1, max_errors=None)
dspy.BootstrapFewShot.compile(student, trainset, teacher=None)
dspy.BootstrapFewShotWithRandomSearch(metric, teacher_settings=None, max_bootstrapped_demos=4, max_labeled_demos=16, max_rounds=1, num_candidate_programs=16, num_threads=None, max_errors=None, stop_at_score=None, metric_threshold=None)
dspy.KNNFewShot(k, trainset, vectorizer)
dspy.KNNFewShot.compile(student, teacher=None)
dspy.InferRules(num_candidates=10, num_rules=10, num_threads=None, teacher_settings=None)
dspy.InferRules.compile(student, trainset, teacher=None, valset=None)
dspy.COPRO(prompt_model=None, metric=None, breadth=10, depth=3, init_temperature=1.4, track_stats=False)
dspy.MIPROv2(metric, prompt_model=None, task_model=None, teacher_settings=None, max_bootstrapped_demos=4, max_labeled_demos=4, auto="light", num_candidates=None, num_threads=None, max_errors=None, seed=9, init_temperature=1.0, verbose=False, track_stats=True, log_dir=None, metric_threshold=None)
dspy.MIPROv2.compile(student, trainset, teacher=None, valset=None, num_trials=None, minibatch=True, minibatch_size=35, minibatch_full_eval_steps=5, requires_permission_to_run=None)
dspy.SIMBA(metric, bsize=32, num_candidates=6, max_steps=8, max_demos=4, prompt_model=None, teacher_settings=None, demo_input_field_maxlen=100000, num_threads=None, temperature_for_sampling=0.2, temperature_for_candidates=0.2)
dspy.SIMBA.compile(student, trainset, seed=0)
dspy.GEPA(metric, auto=None, max_full_evals=None, max_metric_calls=None, reflection_minibatch_size=3, candidate_selection_strategy="pareto", reflection_lm=None, skip_perfect_score=True, add_format_failure_as_feedback=False, instruction_proposer=None, component_selector="round_robin", use_merge=True, max_merge_invocations=5, num_threads=None, failure_score=0.0, perfect_score=1.0, log_dir=None, track_stats=False, use_wandb=False, track_best_outputs=False, warn_on_score_mismatch=True, use_mlflow=False, seed=0, gepa_kwargs=None)
dspy.GEPA.compile(student, trainset, teacher=None, valset=None)
dspy.BetterTogether(metric)
dspy.BetterTogether.compile(student, trainset, teacher=None, valset=None, num_threads=None, max_errors=None, seed=None, valset_ratio=0.1, shuffle_trainset_between_steps=True, strategy="p -> w -> p", optimizer_compile_args=None)
dspy.BootstrapFinetune(metric=None, multitask=True, train_kwargs=None, adapter=None, exclude_demos=False, num_threads=None)
dspy.Ensemble(reduce_fn=None, size=None, deterministic=False)
dspy.AvatarOptimizer(metric, max_iters=10, lower_bound=0, upper_bound=1, max_positive_inputs=None, max_negative_inputs=None, optimize_for="max")
# text artifacts — text-artifacts.md
gepa.optimize_anything.optimize_anything(seed_candidate=None, evaluator=None, batch_evaluator=None, dataset=None, valset=None, objective=None, background=None, config=None)
```

## Importing

**Import `numpy.typing` before `dspy`, never after.** In `.venv-dspy`,
`import dspy` followed by `import numpy.typing` fails with a circular import.
The other order works. [checked: numpy-typing-after-dspy] Anything that
imports `numpy.typing` on the way in hits the same wall: pandas, pyarrow,
lancedb. The dspy-agents reader found it when `Agentic-Dspy-Rag`'s app only
started with numpy imported first. No script here imports numpy after dspy
today; a new one that needs both imports numpy first.

## Signatures

A signature is the whole prompt contract: input fields, output fields, and
instructions. Two spellings, one object:

```python
from typing import Literal
import dspy

class SameTerm(dspy.Signature):
    """Sind die beiden Oberflächenformen derselbe Begriff …"""   # the docstring IS the instructions
    first: str = dspy.InputField()
    second: str = dspy.InputField(desc="the other surface")
    decision: Literal["one-term", "two-terms"] = dspy.OutputField()
    rule: str = dspy.OutputField(desc="die Regel, in einem Satz")

dspy.Signature("question: str, context: list[str] -> answer: str")   # string form, typed
```

- **The docstring is the instructions** and `with_instructions("…")` returns a
  copy with new ones and the same fields — which is all `InferRules` and `GEPA`
  change. `input_fields`, `output_fields`, `fields`, `instructions`, and
  `append` / `prepend` / `insert` / `delete` / `with_updated_fields` edit the
  rest.
- **A `Literal` output is enforced at parse time.** A value outside the set is
  not a wrong answer, it is an unparseable one: both adapters refuse it and the
  call raises `AdapterParseError`, which `lmrun.call` records as `unparsed`.
  [checked: literal-out-of-set-unparsed] That is why `pairs.py`'s decision is a
  `Literal` and never free text: `Agentic-Dspy-Rag` routes on
  `"Comparative" in user_intent`, a substring test on whatever the model wrote
  (`Plan/concept/dspy-toolchain_2026-09-23.md`, job 1).
- **Pydantic types work through the default adapter.** `dspy.settings.adapter`
  is `None`, which means `ChatAdapter`; it writes the field's JSON schema into
  the prompt and parses a `list[Entity]` back into model instances. Nothing
  switches to `JSONAdapter` on its own.
- A custom type in a *string* signature needs
  `make_signature(..., custom_types={...})`; the class form resolves it
  normally.

**In this repository** the signatures are German where the model reads them —
`pairs.py`'s `SameTerm` docstring — and the output a person will read is
asserted German by `lmrun.call(german=[...])` (P19).

## Modules

| module | what it adds | here |
|---|---|---|
| `Predict` | one call: signature → prompt → parse | `pairs.py`, `graphrag.py --answer` |
| `ChainOfThought` | a `reasoning` output field placed **before** the declared outputs | nothing yet |
| `ReAct`, `ReActV2` | a tool loop, `max_iters=20` | nothing; `ReActV2` is marked experimental |
| `ProgramOfThought`, `CodeAct` | the model writes code, a sandbox runs it (Deno) | nothing |
| `RLM` | a REPL over a long input, sub-LM calls, tools — `rlm.md` | `rlm_ingest.py` |
| `Flex` | new in 3.3.0, experimental: a module whose *source* GEPA may rewrite; runs optimizer-written code in the Deno sandbox | nothing |
| `Refine`, `BestOfN` | N attempts scored by `reward_fn(args: dict, pred)` against a `threshold`; `Refine` also writes advice between attempts | nothing |
| `MultiChainComparison` | compares M completions | nothing |
| `Parallel`, `Module.batch` | threads over `(module, example)` pairs, `timeout=120`, straggler handling | nothing |

**`reward_fn` is not a metric.** It is called `(kwargs_dict, prediction)`, not
`(example, prediction, trace, …)`; a metric passed as a reward function fails
(`dspy-agent-skills:skills/dspy-book-eight-steps/SKILL.md`, see `metrics.md`).

A module's own API: `predictors()` and `named_predictors()` (what an optimizer
edits), `deepcopy()` and `reset_copy()` (what an optimizer compiles — `pairs.py`
compiles `program.deepcopy()` per fold), `dump_state()` / `load_state()` (what
`baseline.digest` hashes), `set_lm()` / `get_lm()` (a per-module LM), `batch()`.

## Adapters — how a signature becomes a prompt

- **`ChatAdapter`** is the default: `[[ ## field ## ]]` sections, ending in
  `[[ ## completed ## ]]` — the format `lm_fixture.chat()` writes.
- **It falls back to `JSONAdapter` when its own parse fails**
  (`use_json_adapter_fallback=True`), so a model that answers in JSON is still
  parsed. [checked: chat-adapter-json-fallback] One unparseable answer can
  therefore cost two calls, which is why the `unparsed` case in
  `lmrun.py`'s selftest scripts three answers.
- **When both fail, `dspy.AdapterParseError`** — a `DSPyError`, not an
  `LMError`. [checked: unparseable-is-adapter-error] `lmrun.call` records it as
  `unparsed`, never as a wrong answer.
- `JSONAdapter` uses native structured output where the provider has it;
  `XMLAdapter` writes tags; `TwoStepAdapter(extraction_model)` lets one model
  answer freely and a second extract the fields.

## The language model

```python
lm = dspy.LM("openrouter/<provider>/<model>", cache=True, num_retries=3, temperature=None)
```

- **`cache=True` is the default.** A cached call replays its first completion
  for identical input, so repeats measure nothing (P18). Here every real LM is
  built by `lmrun.make_lm()`, which forces `cache=False`, and `lmrun.call`
  refuses an LM whose cache is on. `check_dspy_surface.py` fails if the default
  ever changes.
- `num_retries=3` is litellm's retry; after it, DSPy raises its own error.
- `model_type` is `"chat"`, `"text"` or `"responses"`; extra keyword arguments
  (`api_base`, `api_key`, `max_tokens`, `temperature`, `reasoning_effort`, …)
  are passed through to litellm. `rlm_ingest.py` passes `api_base` and the key
  explicitly for OpenRouter.
- **`lm.history`** keeps one dict per call: `prompt`, `messages`, `kwargs`,
  `response`, `outputs`, `usage`, `cost`, `model`, `model_type`,
  `response_model`, `timestamp`, `uuid`. `lmrun.call` reads the raw text and
  `finish_reason` from `response` before any parsing.
- `dspy.inspect_history(n)` prints the last `n` rendered prompts and answers —
  the first thing to read when a model "ignored an instruction"
  (`dspy-agent-skills:skills/dspy-production/SKILL.md`).
- `with dspy.track_usage() as usage:` … `usage.get_total_tokens()` returns
  tokens per model; `lmrun.call` records it per call.
- **`track_usage` sees only the calls made in the thread that entered it.**
  `Evaluate(num_threads=4)` inside it records no tokens at all, where
  `num_threads=1` records every call. [checked: track-usage-misses-threads]
  `dspy-agents` logged 765 tokens against 7,230 real for exactly this reason
  (`Plan/concept/dspy-extract_2026-09-24/agents-rag.md`). `lmrun.call` is
  single-threaded, so its record is complete. `dspy.RLM`'s
  `llm_query_batched` copies the context into its worker threads, so
  `rlm_ingest.py`'s cost line sees the sub-calls
  (`dspy:predict/rlm.py:312-315`).

### Settings

`dspy.configure(lm=…, adapter=…, track_usage=…)` sets them process-wide;
`with dspy.context(lm=…):` overrides them for a block, per thread — which is
how every script here sets its LM and how `lm_fixture.offline()` installs the
fixture. The settings keys in 3.3.1 are `adapter`, `lm`, `max_errors` (default
10), `num_threads`, `track_usage`, `usage_tracker`, `callbacks`, `trace`,
`disable_history`, `max_history_size`, `max_trace_size`, `provide_traceback`,
`async_max_workers`, `allow_tool_async_sync_conversion`, `warn_on_type_mismatch`,
`send_stream`, `stream_listeners`, `rm`, `caller_modules`, `caller_predict`,
`branch_idx`.

### Errors — new in 3.3

DSPy 3.3 wraps every provider and network failure in its own types, so code
that matched litellm's names no longer sees them:

```
DSPyError
├── AdapterParseError                      the answer could not be parsed
└── LMError
    ├── LMProviderError                    the provider answered with an error
    │   ├── LMAuthError, LMBillingError, LMRateLimitError, LMServerError, LMTimeoutError
    │   └── LMInvalidRequestError
    │       ├── ContextWindowExceededError
    │       └── LMUnsupportedModelError
    ├── LMTransportError                   nothing came back — a refused connection
    ├── LMConfigurationError
    │   └── LMNotConfiguredError
    ├── LMUnexpectedError
    └── LMUnsupportedFeatureError
```

A refused connection arrives as `LMTransportError`, with litellm's and openai's
exceptions underneath as its cause. [checked: refused-connection-is-transport-error]
`dspy.is_retryable_lm_error(e)` says which are worth retrying.
**Found by this check:** `lmrun.call` matched only litellm's names and re-raised
`LMTransportError` instead of recording `unreachable`; its selftest had only
ever raised the fixture's own `NetworkRefused`. Fixed 2026-09-24 — every
`LMProviderError` and `LMTransportError` is now `unreachable`, and a
configuration error is still raised, because it is this repository's mistake.

## Examples and predictions

```python
ex = dspy.Example(first="Riss", second="Risse", decision="one-term").with_inputs("first", "second")
ex.inputs()    # Example(first, second)          — what the program is given
ex.labels()    # Example(decision)               — what the metric compares
ex.toDict()
```

- **`with_inputs` is the one place inputs are declared.** A field left out
  starves the program; a label left in leaks the answer
  (`dspy-agent-skills:skills/dspy-book-datasets/SKILL.md`, `data.md`).
- `Prediction` is an `Example` with `completions`, `get_lm_usage()` and
  arithmetic on `score` — which is why a metric may return
  `dspy.Prediction(score=…, feedback=…)` and `Evaluate` still sums it.

## Evaluate

```python
result = dspy.Evaluate(devset=dev, metric=metric, num_threads=1)(program)
result.score      # a PERCENTAGE: 100.0 when every example is right
result.results    # [(example, prediction, score), …]
```

- **`score` is a percentage, not a fraction.** [checked: evaluate-score-percent]
  `baseline.py` stores fractions; convert, never mix.
- **A program that raises is scored `failure_score`, 0.0 by default, and
  counted.** [checked: evaluate-failure-is-zero] An unreachable model therefore
  scores 0% — "never reached" folded into "answered badly", the exact thing P15
  forbids. After `max_errors` (default 10) failures it raises instead. **Nothing
  here reads `Evaluate`'s aggregate as a measurement:** `pairs.py` scores each
  held-out example through `lmrun.call` and writes `null` for one that could not
  be scored. `InferRules` still uses `Evaluate` internally to choose between its
  candidates (`optimizers.md`).
- **A metric that returns a dict crashes it**:
  `TypeError: unsupported operand type(s) for +: 'int' and 'dict'`.
  [checked: metric-dict-crashes] A metric returning
  `dspy.Prediction(score, feedback)` aggregates. [checked: metric-prediction-aggregates]
- `display_table`, `save_as_csv`, `save_as_json` write the per-example table;
  `provide_traceback=True` shows why an example failed.

## Saving and loading

- `program.save("x.json")` writes **state only** — `traces`, `train`, `demos`,
  `signature`, `lm`, `metadata` — and `program.load("x.json")` reads it into a
  program built by the same code. This is the only form to keep here.
- `save(dir, save_program=True)` pickles the whole program with cloudpickle.
  **`dspy.load` refuses it unless `allow_pickle=True`**, because unpickling runs
  code. [checked: load-refuses-pickle]
- The saved LM state records model, cache, retries and sampling settings and
  **not the API key**. [checked: saved-state-has-no-key] On load,
  `allow_unsafe_lm_state=False` drops `api_base`, `base_url` and `model_list`
  from the state, so a saved file cannot silently redirect calls.
- `metadata.dependency_versions` is stored and compared on load; a program
  saved under another DSPy version warns.

## Cache

`dspy.configure_cache(...)` controls the process cache: disk under
`~/.dspy_cache` (30 GB limit) and memory (1,000,000 entries), both on, and
**`restrict_pickle=False`** — the disk cache deserialises with pickle unless
restricted (`safe_types` widens the allow-list). The per-LM `cache=` flag
decides whether a call consults it. Measure cost at least once with the cache
off: a warm-cache benchmark "looks free and tells you nothing"
(`dspy-agent-skills:skills/dspy-production/SKILL.md`). Here the cache is off for
every real call, so neither question arises until something turns it on.

## Asynchronous and streamed calls

`program.acall(...)`, `dspy.asyncify(program)`, `dspy.syncify(program)`,
`dspy.streamify(program, stream_listeners=[...])`. Nothing here uses them;
`lmrun.call` is synchronous on purpose, one call, one record.

## Tools

`dspy.Tool(func, name=None, desc=None, args=None, arg_types=None, arg_desc=None)`
wraps a function; its name, docstring and type hints become the tool
description. `Tool.from_mcp_tool` and `Tool.from_langchain` exist. `dspy.RLM`
takes plain callables in `tools=[...]` — `rlm_ingest.py` passes `find_line` and
`count`, both with docstrings, because the docstring is what the model reads.
