# The DSPy 3.3.1 surface, as installed here

Every statement about DSPy on this page was read off the installed package
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
# A line names the parameters this skill teaches, not every parameter a callable
# takes. Names come before keywords, and a default that is a class is left out.
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
dspy.Tool.from_mcp_tool(session, tool, result_mode="text")
dspy.Tool.from_langchain(tool)
dspy.Image.from_url(url, verify=True, timeout=30.0)
dspy.Image.from_path(file_path)
dspy.Audio.from_array(array, sampling_rate, format="wav")
# async and streaming
dspy.asyncify(program)
dspy.syncify(program, in_place=True)
dspy.streamify(program, status_message_provider=None, stream_listeners=None, include_final_prediction_in_output_stream=True, is_async_program=False, async_streaming=True)
dspy.streaming.StreamListener(signature_field_name, predict=None, predict_name=None, allow_reuse=False)
dspy.track_usage()
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
  not a wrong answer, it is an unparseable one: `ChatAdapter` refuses it and the
  call raises `AdapterParseError`, which `lmrun.call` records as `unparsed`.
  [checked: literal-out-of-set-unparsed] **The JSON fallback does not**: when the
  reply is valid JSON holding a value outside the set, `JSONAdapter.parse()`
  lets a bare `ValueError` escape unwrapped — its text pydantic's validation
  message or „'maybe' is not one of …", depending on the path.
  [checked: json-fallback-literal-is-valueerror] `lmrun.call` records that as
  `unparsed` too since 2026-09-25, by the frame it was raised in; before, it
  re-raised it and one such answer would have ended a run
  (`Plan/concept/dspy-source_2026-09-24/adapters-and-types.md`; this line said
  „both adapters" until then). That is why `pairs.py`'s decision is a
  `Literal` and never free text: `Agentic-Dspy-Rag` routes on
  `"Comparative" in user_intent`, a substring test on whatever the model wrote
  (`Plan/concept/dspy-toolchain_2026-09-23.md`, job 1).
- **Pydantic types work through the default adapter.** `dspy.settings.adapter`
  is `None`, which means `ChatAdapter`; it writes the field's JSON schema into
  the prompt and parses a `list[Entity]` back into model instances. Nothing
  switches to `JSONAdapter` on its own.
- A custom type in a *string* signature needs
  `make_signature(..., custom_types={...})`; the class form resolves it
  normally. A file with `from __future__ import annotations` hands a class
  body's annotations to DSPy as strings, so a field typed with a variable
  never becomes that type; build such a signature with `make_signature`,
  as `check_dspy_skill.py`'s History probe had to.
- **A string signature is never without instructions.** DSPy writes
  „Given the fields `x`, produce the fields `y`." for it, and that sentence is
  what `InferRules` and `GEPA` start rewriting from.
- **The class name never reaches the model.** Only the docstring, the field
  names and their values do. `dspydantic` names its signature classes for
  context, `OptimizeMedicalRecordFieldDescription`, and the name appeared in 0
  of 92 requests (`dspydantic:src/dspydantic/module.py:67-71`, measured by its
  reader).
- **An unannotated field is a `str`**, marked `IS_TYPE_UNDEFINED`; adding
  `: str` changes neither the prompt nor the parse. `braid-dspy`'s commit
  „Add type hints to signatures for structured output compatibility" produced
  byte-identical prompts on DSPy 2.6.27, 3.0.4 and 3.3.1
  (`braid-dspy:braid/signatures.py:6-89`, measured by its reader).
- `prefix=`, `format=` and `parser=` on a field are deprecated and do nothing
  but warn (`dspy:signatures/field.py:10-24`). Use `desc=` and a real type.

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
(`dspy-agent-skills:skills/dspy-book-eight-steps/SKILL.md:72`, `metrics.md`).
Three more things `Refine` and `BestOfN` do that their names do not say:

- every attempt runs on a copy of the module's LM at `temperature=1.0`, and
  `mod.set_lm()` puts that copy on *every* predictor — a judge with its own
  cheap LM does not survive being wrapped; a module whose predictors use
  different LMs raises "Multiple LMs are being used in the module"
  (`dspy:predict/refine.py:107-109`, `dspy:primitives/module.py:216`);
- `Refine`'s advice between attempts comes from a `dspy.Predict(OfferFeedback)`
  call on the global LM, fed the module's source and the reward function's
  source, so a reward function without retrievable source raises `OSError`
  at construction, and a judge's findings never reach the writer — only the
  number does (`patterns.md`);
- when every attempt raises and N ≤ 2, both return `None`; at N = 3 they
  raise (`patterns.md`).

A module's own API: `predictors()` and `named_predictors()` (what an optimizer
edits), `deepcopy()` and `reset_copy()` (what an optimizer compiles — `pairs.py`
compiles `program.deepcopy()` per fold), `dump_state()` / `load_state()` (what
`baseline.digest` hashes), `set_lm()` / `get_lm()` (a per-module LM), `batch()`.

- **Setting `submodule._compiled = True` hides its predictors** from the
  parent's `named_predictors()`, so an optimizer walking the parent skips them.
  `BetterTogether` sets it on the program it returns, which freezes that program
  against further prompt optimization (`dspy:teleprompt/bettertogether.py:304`,
  re-run by the api reader).
- **Compiling again does not stack demos**: an optimizer compiles
  `student.reset_copy()`, so three `LabeledFewShot(k=4)` compiles leave 4 demos,
  not 12. `BootstrapFewShot` on a program already marked compiled raises
  „Student must be uncompiled" (`dspy:teleprompt/bootstrap.py:96-102`).
- **`dspy.Parallel` accepts `(module, dict)` pairs as well as `(module,
  Example)`**, and an `Example` never passed through `with_inputs` is not an
  error there: its slot in the results is `None`, and only a logged line says
  why (`dspy:predict/parallel.py:94-100`).
- `dspy.majority(completions, normalize=default_normalize, field=None)` votes
  over several completions after lowercasing and stripping punctuation and
  English articles; it needs `n > 1` completions from the call itself
  (`dspy:predict/aggregation.py:5-50`).
- `CodeAct` takes only plain functions as tools — a bound method, a
  callable object or a `functools.partial` raises at construction — where
  `ReAct` also accepts objects and `dspy.Tool` (`dspy:predict/code_act.py:64-65`).

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
- **The `Literal` check is case-sensitive**, and an off-list value fails both
  parses, so it costs two calls before the error: `Agentic-Dspy-Rag`'s
  classifier answering `comparative` for `Comparative` would fail loudly this
  way, where its substring routing misrouted it silently
  (`Agentic-Dspy-Rag:src/agentic_rag/components/agents.py:109-123`, re-run by its reader on 3.3.1).
- `JSONAdapter` uses native structured output where the provider has it;
  `XMLAdapter` writes tags; `TwoStepAdapter(extraction_model)` lets one model
  answer freely and a second, which must be a `dspy.BaseLM`, extract the
  fields — through a demo-less adapter, so that step „cannot learn or get
  optimized" (`dspy:adapters/two_step_adapter.py:17-18`).
- `dspy.BAMLAdapter` is not a top-level name:
  `from dspy.adapters.baml_adapter import BAMLAdapter`.
- **The adapter is process-global.** `Predict`, `ReAct` and `Refine` each use
  `settings.adapter or ChatAdapter()`; there is no per-predictor adapter, and
  `with dspy.context(adapter=…):` is how one call gets another
  (`dspy:predict/predict.py:254,268`).
- To change formatting without replacing the adapter, subclass `ChatAdapter`
  and override `format_field_with_value`, `user_message_output_requirements`
  or `parse`.

## History — conversations as an input field

`dspy.History(messages=[...])` is a frozen pydantic model whose messages are
dicts **keyed by the signature's own field names**, never `role`/`content`.

- **An adapter recognises it only when the field's annotation is exactly
  `dspy.History`.** Then each stored message becomes its own `user` and
  `assistant` turn before the current question. `Optional[dspy.History]`, an
  `Annotated` form or a subclass is formatted like any other input: the whole
  history dumped as JSON into the current message.
  [checked: history-exact-annotation]
- In a turn, missing input fields are skipped, and every output field is
  written, a missing one as the text `None`. A history of `{"role": …,
  "content": …}` dicts therefore renders as assistant turns reading `None`, and
  the conversation never reaches the prompt, with no error
  (`dspy:adapters/chat_adapter.py:150-217`,
  `dspy-agent-skills:skills/dspy-book-agents/SKILL.md:54-56`).
- Demos are formatted against the signature *with* the history field, so a
  demo recorded before the field existed is marked incomplete in the prompt
  (`dspy:adapters/base.py:542-590`).
- **A keyword the signature does not declare is dropped with a log line, not
  an error**: `history=` passed to `Predict("question -> reply")` never reaches
  the prompt (`dspy:predict/predict.py:195`). It is `logging`, not `warnings`,
  so `-W error` does not catch it.
- A keyword that is not a field at all, passed when constructing `Predict`,
  becomes part of its config and is sent to the provider with every call
  (`dspy-session:docs/multiple-signatures.md:11-17`).

Nothing here keeps a conversation; `patterns.md` has what `dspy-session`
learned about wrapping modules in one, including why `dspy.RLM` must never be.

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
- **Sampling settings live in `lm.kwargs`, not on the object**:
  `dspy.LM(…, temperature=0.3)` has no `.temperature` attribute, so code that
  reads or sets `lm.temperature` silently does nothing.
  [checked: lm-has-no-temperature-attribute] Two of the nine repositories
  shipped exactly that defect (`braid-dspy:braid/generator.py:55-75`,
  `dspy-agents:tools/runtime_diag_tool.py:155`).
- **Calling an LM directly returns a list of strings**, one per completion,
  not a `Prediction`. [checked: lm-call-returns-list] `braid-dspy` read the
  list's `repr` as the answer (`braid-dspy:braid/generator.py:109-136`).
- A reasoning model (an `o1`/`o3`/`o4`/`o5` id or `gpt-5…`) is checked at
  construction: `temperature` must be 1.0 or None and `max_tokens` at least
  16,000, or `LMConfigurationError`. The test is `if temperature and …`, so
  `temperature=0.0` slips through (`dspy:clients/lm.py:48-53,125-133`).
- `lm.copy(rollout_id=n)` gives calls their own cache key — at any
  temperature, 0 included. [checked: rollout-id-busts-cache-at-zero-temperature]
  At 0 DSPy still warns „rollout_id has no effect when temperature=0; set
  temperature>0 to bypass the cache", and the warning is wrong about the cache:
  two ids are two real calls. What temperature 0 leaves unchanged is the
  provider's answer. The copy starts with an empty history
  (`dspy:clients/lm.py:98-102,165-170`). This line said the opposite until
  2026-09-25, taken from the warning (`Plan/concept/dspy-source_2026-09-24/lm-and-retrieval.md`).
- With no LM configured, a call raises „No LM is loaded. Please configure the
  LM using `dspy.configure(lm=dspy.LM(...))`" (`dspy:predict/predict.py:154`).
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

### Writing your own LM

A `dspy.BaseLM` subclass declares which of two contracts its `forward`
implements, in the class attribute `forward_contract`:

- `"legacy"`, the default — `forward(prompt=None, messages=None, **kwargs)`
  returns an OpenAI-shaped object; `.choices[i].message.content` and `.model`
  are read, `.usage` and `._hidden_params` are optional. `lm_fixture.FixtureLM`
  is this kind.
- `"typed_lm"` — `forward(request: dspy.LMRequest) -> dspy.LMResponse`, the
  contract DSPy is migrating to.

`BaseLM` records usage itself, so a subclass must not add it again or it
counts twice — which is the defect the local-runtime `ClaudeLM` shipped
(`dspy:clients/base_lm.py:57-165`, `operations.md`). `dspy.utils.DummyLM` is
DSPy's own offline LM: answers from a list, then „No more responses" forever,
formatted through the adapter so they parse at the first try; `testing.md`
compares it with the fixtures here.

### Settings

`dspy.configure(lm=…, adapter=…, track_usage=…)` sets them process-wide;
`with dspy.context(lm=…):` overrides them for a block, per thread — which is
how every script here sets its LM and how `lm_fixture.offline()` installs the
fixture. The settings keys in 3.3.1 are `adapter`, `lm`, `max_errors` (default
10), `num_threads`, `track_usage`, `usage_tracker`, `callbacks`, `trace`,
`disable_history`, `max_history_size`, `max_trace_size`, `provide_traceback`,
`async_max_workers`, `allow_tool_async_sync_conversion`, `warn_on_type_mismatch`,
`send_stream`, `stream_listeners`, `rm`, `caller_modules`, `caller_predict`,
`branch_idx`. Their defaults: `track_usage=False`, `num_threads=8`,
`async_max_workers=8`, `warn_on_type_mismatch=True`, `adapter=None`.

**The first thread to call `dspy.configure` owns the settings.** Another
thread calling it raises „dspy.settings can only be changed by the thread that
initially configured it"; `dspy.context` is the way to set an LM or an adapter
for a worker thread or for one call (`dspy:dsp/utils/settings.py:127`). Three of
the nine repositories met this.

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
`dspy.is_retryable_lm_error(e)` says which are worth retrying: rate limit,
timeout, server and transport errors, not auth, billing or an invalid request.
A bare exception raised inside the call path — a test's patched
`litellm.completion`, as in `lm_fixture.offline()` — surfaces as
`LMUnexpectedError` with the original as its cause, which is why `lmrun`
still matches `NetworkRefused` by name (`dspy:clients/lm.py:261`).
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
  (`dspy-agent-skills:skills/dspy-book-datasets/SKILL.md:45`, `data.md`).
- **`with_inputs` does not check the names it is given.**
  `Example(text=…, label=…).with_inputs("question")` raises nothing, and
  `.inputs()` is then empty: a starved program, not a `KeyError`.
  [checked: with-inputs-typo-silent] Code that builds examples from column
  names asserts the input keys itself.
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
- **`save_as_json` with a Prediction-returning metric crashes after the whole
  run**: the score prints, every call is paid for, and then „Object of type
  Prediction is not JSON serializable". [checked: save-as-json-prediction-crashes]
  It also does not create its directory. This is what killed the README's
  headline command in `dspy-agent-skills` before GEPA started
  (`dspy-agent-skills:skills/dspy-advanced-workflow/example_pipeline.py:113-120`).
- **An empty devset raises `ZeroDivisionError`**; refuse it before calling,
  because an empty comparison is not a score of 0.
  [checked: evaluate-empty-devset]
- `Evaluate` takes `**kwargs`, so a misspelled keyword — `num_thread=64` — is
  accepted and ignored.
- Who calls a metric with what differs by caller: `Evaluate` passes
  `(example, pred)`, `BootstrapFewShot` a real `trace`, `GEPA` also `pred_name`
  and `pred_trace` — so a metric branches on `pred_name`, never on `trace`
  (`metrics.md`).
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
  saved under another DSPy version warns — and loads: state saved on 3.1.3 or
  3.2.0 loads into 3.3.1 (`Plan/concept/dspy-extract_2026-09-24/das-core.md`).
- A whole-program pickle carries whatever the optimizer attached. MIPROv2's
  output holds `trial_logs` and every candidate program it tried: 29,621 bytes
  pickled against 733 as state JSON, for one trivial program
  (`dspy-agents`, measured by its reader).

## Cache

`dspy.configure_cache(...)` controls the process cache: disk under
`~/.dspy_cache` (30 GB limit) and memory (1,000,000 entries), both on, and
**`restrict_pickle=False`** — the disk cache deserialises with pickle unless
restricted (`safe_types` widens the allow-list). The per-LM `cache=` flag
decides whether a call consults it. Measure cost at least once with the cache
off: a warm-cache benchmark "looks free and tells you nothing"
(`dspy-agent-skills:skills/dspy-production/SKILL.md:74`). Here the cache is off for
every real call, so neither question arises until something turns it on.

A cache hit reports empty usage — the cached response's `usage` is cleared
before the tracker sees it — so code reading `response.usage` directly reads
nothing on a hit (`dspy:clients/cache.py:149-157`). The cache directory comes
from `DSPY_CACHEDIR`; `dspy-advanced-prompting`'s `DSPY_CACHE_DIR` does
nothing.

## Asynchronous and streamed calls

`program.acall(...)`, `dspy.asyncify(program)`, `dspy.syncify(program)`,
`dspy.streamify(program, stream_listeners=[...])`. Nothing here uses them;
`lmrun.call` is synchronous on purpose, one call, one record.

`asyncify` runs the program in a worker thread and carries the caller's
`dspy.context` into it; cancelling the awaiting task does not stop the call
underneath (`dspy:utils/asyncify.py:36,46-58,63`). `pred.get_lm_usage()` depends on
the context: `None` without `track_usage`, and `None` again inside a
`with dspy.track_usage()` block, which takes the usage instead
(`dspy:primitives/module.py:102-103,121-122`).

## Tools

`dspy.Tool(func, name=None, desc=None, args=None, arg_types=None, arg_desc=None)`
wraps a function; its name, docstring and type hints become the tool
description. `Tool.from_mcp_tool` and `Tool.from_langchain` exist. `dspy.RLM`
takes plain callables in `tools=[...]` — `rlm_ingest.py` passes `find_line` and
`count`, both with docstrings, because the docstring is what the model reads.

**A synchronous `ReAct` call into an `async def` tool does not raise.** The
tool's refusal becomes the step's observation text, Python warns that a
coroutine was never awaited, and the agent still answers — without the tool.
[checked: react-async-tool-swallowed] An agent with async tools is called with
`await agent.acall(...)`. MCP tools are async: `dspy.Tool.from_mcp_tool` wraps
one (`dspy-agent-skills:skills/dspy-book-agents/SKILL.md:38-41`).

## Media types

`dspy.Image` takes a URL, a data URI, bytes or a PIL image; a local path is
refused — "Local files must be loaded with Image.from_path()"
(`dspy:adapters/types/image.py:206`). [checked: image-refuses-local-path]
`dspy-agent-skills`' chapter says the constructor accepts a path
(`dspy-agent-skills:skills/dspy-book-modules/SKILL.md:55`); on 3.3.1 it does
not. `Image.from_url` downloads, and its own docstring says it "will reach
private, loopback, or cloud-metadata hosts" (`dspy:adapters/types/image.py:116-124`).
`dspy.Audio.from_array` needs `soundfile`. In a string signature the type is
written `dspy.Image`. Nothing here sends media to a model.

## Names that moved, and an optimizer that cannot be built

Checked against DSPy 3.3.1 before writing an import.
[checked: names-absent]

| name | on 3.3.1 |
|---|---|
| `dspy.TypedPredictor` | gone; a typed `Predict` signature does the job |
| `dspy.OpenAI` | gone; `dspy.LM("openai/<model>")` |
| `dspy.Assert`, `dspy.Suggest` | gone; `dspy.Refine` replaced them |
| `dspy.BAMLAdapter` | not at top level; `dspy.adapters.baml_adapter` |
| `from dspy.datasets import GSM8K` | fails; `from dspy.datasets.gsm8k import GSM8K` works |

**`dspy.AvatarOptimizer` cannot be constructed on 3.3.1**: it builds a
`dspy.TypedPredictor` inside, and raises `AttributeError` whatever its
arguments. [checked: avatar-optimizer-unconstructible] Its surface line above
still holds, because the signature is intact; a signature that exists is not
a class that works. The other construction-time refusals of the optimizers —
GEPA's single budget, BetterTogether's strategy names, MIPROv2's `optuna`,
SIMBA's `bsize` — are in `optimizers.md`.
