# dspy-session + dspy-optimizer — extracted DSPy knowledge

## 1. Header

| | dspy-session | dspy-optimizer |
|---|---|---|
| Repo | `/home/user/dspy-session` (github.com/netzkontrast/dspy-session; upstream named in `pyproject.toml:33-35` is github.com/maximerivest/dspy-session) | `/home/user/dspy-optimizer` (github.com/netzkontrast/dspy-optimizer) |
| Commit | `eb67e76` (2026-02-26; 32 commits since 2026-02-23) | `a07b3b7` (2025-07-27; 25 commits since 2025-07-24) |
| License | MIT, © 2026 Maxime Rivest | MIT, © 2025 Niels van Galen Last |
| DSPy targeted | `dspy>=2.6` (`pyproject.toml:28`); `uv.lock:396-397` pins **3.1.3** | `dspy>=2.6.27` (`pyproject.toml:12`); `uv.lock:745-746` pins **2.6.27** |
| Python | `>=3.10` (`pyproject.toml:11`) | `>=3.12` (`pyproject.toml:9`; `.python-version` = 3.12) |
| Holds on 3.3.1? | The library imports and its suite passes, but three things behave differently or wrongly on 3.3.1: wrapping `dspy.RLM` fails immediately with a `ValueError`; a deep-copied or forked Session still runs the original predictor, so optimizers get 0 demos; and composed programs receive `None`-filled history turns. | The code and 38 of 43 tests run unmodified. The other 5 (the MLflow tests) need `mlflow` installed; with mlflow 3.16.1 all 43 pass. |

**What they are.** *dspy-session* (`dspy_session/session.py`, 1512 lines) wraps any `dspy.Module` in `Session(dspy.Module)`. The Session records every call as a `Turn` and builds a `dspy.History` from past turns. It injects that history into every nested predictor through a contextvar, and it turns the turns into `dspy.Example`s. `with_memory` adds per-node memory policies (isolated/shared, persistent/episodic/stateless, consolidator), and `SessionState` adds per-user state for serving. An MLflow add-on is included. *dspy-optimizer* (≈700 lines of code) runs an Evaluator→Refiner→Merger→Validator loop that patches one `### Block`-structured prompt string. It uses string-keyed strategy registries, a callback protocol, and a hand-written `MockLLM`. It is not a DSPy teleprompter, and its invoice example is absent.

**What I ran (all offline; every command prefixed `env -u OPENROUTER_API_KEY -u TYPESAFE_API_KEY -u OPENAI_API_KEY -u ANTHROPIC_API_KEY`):**
- Venv `scratchpad/venvs/sessopt312`: Python 3.12.3, `dspy==3.3.1`, pytest, anyio. Venv `sessopt312mlf`: the same plus `mlflow==3.16.1`. Venv `dspy313src`: `dspy==3.1.3 --no-deps`, used only to read its source.
- `pytest dspy_session/tests` → **102 passed, 1 skipped** (5.2 s). The skip is `test_readme_usage.py:135`: `dspy_template_adapter` is not installed.
- `pytest tests` (optimizer) → **38 passed, 5 failed** without mlflow (the failures are `AssertionError` at `mlflow_callback.py:56`), and **43 passed** (6.26 s) with mlflow 3.16.1.
- Probe scripts, all using DummyLM, fake forwards or MagicMock and never a real LM, are in `scratchpad/sessopt/`:
  - `render.py`: what history looks like on the wire
  - `session_misc.py`: RLM, annotations, `score()`, save/load, `max_turns`, hooks, consolidation, predictor names
  - `session_opt.py`: a Session inside `BootstrapFewShot`
  - `session_copy.py`: routing after `deepcopy`/`fork`
  - `session_threads.py`: contextvars under `dspy.Parallel`
  - `optimizer_checks.py`: MockLLM call counts, scorers, validators, loop events, MLflowCallback
  - plus inline checks for ReAct, `append_history`, extra inputs, child-ledger persistence and replay pollution.
- Read-only queries: `sqlite3` on the committed `/home/user/dspy-session/mlflow.db`, and `git show 19fb8d2^:…` on the deleted invoice optimizer. `git status` is clean in both repos afterwards.

---

## 2. Knowledge items

## API

- **[session] `dspy.History` shape (3.3.1)** — `class History(pydantic.BaseModel)` with `messages: list[dict[str, Any]]` and `model_config = ConfigDict(frozen=True, str_strip_whitespace=True, validate_assignment=True, extra="forbid")`. Each message dict is keyed by the consuming signature's field names. `dspy/adapters/types/history.py:61-68` [api] (verified: read 3.3.1 source) → here: any multi-turn signature; `check_dspy_surface.py`
- **[session] Adapters recognise history by exact annotation only** — `_get_history_field_name` returns a field only if `field.annotation == History` (`dspy/adapters/base.py:604-608`). An input annotated `Optional[History]`, `Annotated[History, …]` or a `History` subclass is formatted as an ordinary input: the whole history is JSON-dumped into the current user message (`[[ ## history ## ]] {"messages": [...]}`). `dspy/adapters/base.py:604-608` [api] (verified: `session_misc.py` §2) → here: `check_dspy_surface.py` should assert `annotation is dspy.History`
- **[session] How ChatAdapter renders a History (3.3.1)** — The history field is removed from the signature first (`base.py:416-424`). Each message then becomes:
  - a user turn with the signature's input fields that are *present* in the message; missing inputs are skipped, and if none are present the user turn is dropped entirely (`chat_adapter.py:159-163`, `base.py:658-660`);
  - an assistant turn with *all* output fields, where a missing one renders as `None` (`outputs.get(k, missing_field_message)` with `missing_field_message=None`), ending with `[[ ## completed ## ]]` (`chat_adapter.py:204-217`).

  Order: system, demos, history turns, then the current user message (`base.py:426-440`). `dspy/adapters/base.py:416-440,626-712`; `dspy/adapters/chat_adapter.py:150-217` [api] (verified: `render.py` a, b, c)
- **[session] Demos are formatted with the un-stripped signature** — `messages.extend(self.format_demos(signature, demos))` (`base.py:429`) uses the signature that still contains the history field. A demo missing any field is "incomplete" and gets the prefix „This is an example of the task, though some input or output fields are not supplied." (`base.py:560,574`). `dspy/adapters/base.py:542-590` [api] (verified: source read only; no demo with a History was produced, see OPT)
- **[session] Extra inputs are dropped with a log warning** — `dspy.Predict("question -> reply")(question=…, history=…)` logs „Input contains fields not in signature. These fields will be ignored: ['history']. Expected fields: ['question']." and the prior turns never reach the prompt. `dspy/predict/predict.py:195` [api] (verified: inline probe) → here: `trainset.py` (examples from sessions carry `history`)
- **[session] Adding a field to a signature** — `sig.append(name, dspy.InputField(desc="Conversation history", default=None), type_=History)` returns a new Signature class, which is assigned back to `predictor.signature`. The original module is untouched only because the module was deep-copied first. 3.3.1 also offers `with_instructions`, `append_instructions`, `prepend` and `delete` (`dspy/signatures/signature.py:278,307,362,389,416`). `dspy_session/session.py:549-554` [api] (verified: tests pass; `test_session.py:87-92`)
- **[session] `ChainOfThought` output is `reasoning`** — CoT prepends an output field named `reasoning` (`dspy/predict/chain_of_thought.py:48`). A session records it in `turn.outputs` and replays it in every later history message. The docs' advice to exclude `rationale` (`docs/api-usage-examples.md:182,221`) does nothing on 3.3.1; use `exclude_fields={"reasoning"}`. [api] (verified: `render.py` (d): outputs `{'reasoning': 'R1', 'answer': 'A1'}`, history keys `['question','reasoning','answer']`)
- **[session] Reading `forward` without the warning** — DSPy warns „Calling module.forward(...) on X directly is discouraged" when `forward` is read through normal attribute access (`dspy/primitives/module.py:346`). The session reads it with `object.__getattribute__(obj, name)` instead, and regression tests assert the warning never appears. `dspy_session/session.py:496-507`; `dspy_session/tests/test_session.py:854-891` [pattern] (verified: tests pass)
- **[session] Predictor paths change under wrapping** — `named_predictors()` names are:
  - `sessionify(dspy.Predict)`: `['module']`
  - `sessionify(program)`: `['module.a','module.b']`
  - `with_memory(program)`: `['module.a.module','module.b.module']`

  Saved-state keys (`dump_state`/`load_state`) therefore differ between the wrapped and unwrapped program. [api] (verified: `session_misc.py` §11) → here: any save/load of an optimized program
- **[session] `float(dspy.Prediction)`** — `float(Prediction(score=0.25, feedback=…))` returns 0.25; without `score` it raises `ValueError("Prediction object does not have a 'score' field to convert to float.")`. `dspy/primitives/prediction.py:53-56` [api] (verified: `session_misc.py` §4)
- **[optimizer] `Example.inputs()` needs `with_inputs`** — otherwise it raises `ValueError("Inputs have not been set for this example. Use `example.with_inputs()` to set them.")`. `dspy/primitives/example.py:264` [api] (verified: `optimizer_checks.py` §2) → here: `trainset.py`
- **[optimizer] ChatAdapter falls back to JSONAdapter with a second LM call** — `ChatAdapter(use_json_adapter_fallback=True)` is the default. On a parse failure it re-issues the request through `JSONAdapter` unless the error is an `LMError` (`chat_adapter.py:47,67,91`). An unparseable reply therefore costs 2 LM calls, and the model/format mismatch is hidden. `dspy/adapters/chat_adapter.py:47-92` [api] (verified: JSON text → 2 calls; ChatAdapter-formatted text → 1 call) → here: `lmrun.py` must count calls, not predictor invocations; `unparsed` can hide behind a successful fallback
- **[session] The adapter is global in 3.3.1** — `adapter = settings.adapter or ChatAdapter()` in Predict (`predict.py:254,268`), ReAct (`react.py:91`) and Refine (`refine.py:104`); there is no per-predictor `adapter` attribute. The proposal doc cites the same lines for 3.1.3 (`predict.py:191,205`) and asks for `Predict.adapter`, a module-scoped `lm`/`adapter` pushed through `settings.context`, and `set_adapter()`. Its priority chain: call kwarg → predictor → nearest ancestor module → global → `ChatAdapter()`. Per-call alternative today: `with dspy.context(adapter=...)`. `docs/dspy-proposal-per-module-lm-adapter.md:7-12,18-25,73-163,173-186` [api] (verified: grep of 3.3.1 source)
- **[session] Unknown `Predict` kwargs go to the provider** — `dspy.Predict("text, history: dspy.History -> corrected_text", append_history=True)` stores `{'append_history': True}` in `.config` and sends it with every LM call; the output has no `.history`. `append_history` (`docs/multiple-signatures.md:11-17`) is a proposal, not a DSPy feature. String signatures do resolve `dspy.History`. [api] (verified: DummyLM call kwargs `{'append_history': True}`)
- **[optimizer] `BaseLM.forward_contract` (new in 3.3)** — Two contracts:
  - `"legacy"` (default): `forward(prompt=None, messages=None, **kwargs)` returns an OpenAI-shaped object;
  - `"typed_lm"`: `forward(request: dspy.LMRequest) -> dspy.LMResponse`.

  A legacy response needs `.choices[i].message.content` and `.model` (read unconditionally, `base_lm.py:313`). `.usage` and `._hidden_params` are optional (`getattr` defaults, `base_lm.py:308-309`). Returning an `LMResponse` under the implicit legacy contract only triggers a DeprecationWarning; under an explicitly declared legacy contract it raises TypeError (`base_lm.py:237-265`). `dspy/clients/base_lm.py:57-165,286-320` [api] (verified: MockLLM runs) → here: `lm_fixture.py` (declare `forward_contract` explicitly)
- **[session] `dspy.utils.DummyLM`** — `DummyLM(answers: list[dict] | dict[str, dict], follow_examples=False, reasoning=False, adapter=None)`:
  - list mode: returns the dicts in order, then `{"answer": "No more responses"}`;
  - dict mode: keyed by a substring of the last message;
  - formats answers with the adapter's `format_field_with_value`, so they parse on the first try.

  `dspy/utils/dummies.py:16-160` [recipe] (verified: used by every probe here) → here: `lm_fixture.py`
- **[optimizer] Per-call instructions without mutation** — `Evaluator.forward` builds `dynamic_signature = self._base_signature.with_instructions(prompt)` and a new `dspy.ChainOfThought(dynamic_signature)` on every call; the base signature is unchanged. The price: `Evaluator.named_predictors()` is `[]`, so the evaluator is invisible to DSPy optimizers, `save()`/`load()` and demos. `dspy_optimizer/evaluator.py:22-43` [pattern] (verified: `optimizer_checks.py` §1)
- **[optimizer] Refiner signature** — `RefinerSignature` has 6 inputs: `prompt: str`, `example` (unannotated), `error_reasoning: str`, `prediction` (unannotated), `expected_output` (unannotated), `history: list[str]`. It has 5 outputs: `analysis`, `suggestion`, `target_block`, `operation: str` („The operation to perform: 'append' or 'replace'."), `content`. `ChainOfThought` adds `reasoning`. The docstring (the instructions) carries two complete worked examples in `**Prompt:** … **Content:**` form. `Refiner.forward` passes `history=str(history)` into the `list[str]` field. `dspy_optimizer/refiner/signature.py:6-138`; `dspy_optimizer/refiner/refiner.py:16-51` [api]
- **[optimizer] Unannotated fields default to `str`** — `input = dspy.InputField()` / `output = dspy.OutputField()` without annotations work in 3.3.1 signatures. `tests/dspy_optimizer/test_evaluator.py:9-13` [api] (verified: tests pass)
- **[optimizer] A `dspy.Module` subclass may skip `super().__init__()`** — `BatchedTrainingSetValidationStrategy.__init__` never calls it and still runs when called as a module. `dspy_optimizer/strategies/validation/batched.py:25-33` [api] (verified: tests pass; mechanism not traced)

## OPT

- **[session] `history_policy` was built for optimizer replay** — The three values:
  - `"override"` (default): explicit history is used as-is, no turn is recorded, and no finalization runs;
  - `"use_if_provided"`: use it and record the turn;
  - `"replace_session"`: install it as the seed, clear turns, then run with state.

  Explicit history must be a `dspy.History`, otherwise TypeError „Expected history to be dspy.History, got …". `dspy_session/session.py:658-690`; `dspy_session/tests/test_readme_usage.py:56-83` [api] (verified: tests pass) → here: any replay of recorded examples
- **[session] `override` protects only the root** — In a `with_memory` app, a replay with explicit history records nothing at the root, but child sessions record the replayed call in their own ledgers: root turns 1, worker turns 2 (`['Q1','replayed']`). Children never receive the explicit history, so they build their own. `dspy_session/session.py:674-690` [trap] (verified: inline probe)
- **[session] `BootstrapFewShot.compile(session)` produces 0 demos** — The README's recipe `optimized = dspy.BootstrapFewShot().compile(session, trainset=examples)` (`README.md:366`) prints „Bootstrapped 4 full traces…" (`README.md:371`). On 3.3.1 the same pattern printed „Bootstrapped 2 full traces after 2 examples" and left **0 demos** on the compiled predictor. Cause: the trace names the *original* predictor (next item); `predictor2name[id(predictor)]` raises KeyError, and BootstrapFewShot drops the step with `except KeyError: continue  # FIXME: !` (`dspy/teleprompt/bootstrap.py:230-231`). `README.md:363-371` [trap] (verified: `session_opt.py`)
- **[session] Copies run the original predictor** — `_wrap_predictor` closes over `orig_forward = object.__getattribute__(predictor, "forward")`, a bound method of the *original* predictor, and installs a new bound method whose body calls `orig_forward(**kwargs)`. `copy.deepcopy` rebinds the method to the copy but not the closure. So after `deepcopy`, `fork()`, `reset_copy()` or any optimizer copy:
  - calls use the original predictor's signature, demos and lm;
  - demos set on the copy are ignored;
  - demos set on the original leak into copies and forks;
  - `dspy.settings.trace` records the original object.

  `dspy_session/session.py:557-587,1052-1067` [trap] (verified: `session_copy.py`: closure bound to ORIGINAL; copy demo in prompt False; original demo in copy's prompt True, in fork's True)
- **[session] Optimizing a sessionified program: the path that works** — Optimize an *unwrapped* module whose signature already contains `history: dspy.History` on `session.to_examples()`. Then call `session.update_module(optimized)`: it deep-copies the module, re-patches the signature, and wraps with a closure bound to the new copy. `dspy_session/session.py:1006-1010` [recipe] (verified: `session_copy.py` §3, demo appears in the prompt) → here: `pairs.py`/any job that optimizes a stateful module
- **[session] A student without a history field drops the history** — README Example 9 runs `dspy.GEPA(metric=dummy_metric, max_metric_calls=10, reflection_lm=dspy.LM(model="gpt-5", temperature=1.0, max_tokens=32000)).compile(dspy.Predict(Support), trainset=trainset)` on `session.to_examples()`. Logged: „Running GEPA for approx 10 metric calls of the program. This amounts to 5.00 full evals on the train set." (trainset of 2 turns). `Support` has no history field, so every example's `history` is dropped (`predict.py:195` warning) and GEPA optimizes as if each turn were single-shot; `update_module` then adds history the optimizer never saw. `README.md:686-709` [number/trap] (verified: extra-input probe)
- **[session] A compiled or forked session carries the copied conversation** — The optimizer's deep copy includes `_default_state.turns`, so `optimized(question=…)` continues the old conversation. README Example 4's answer says „just like we did for x²". `README.md:376-382` [pattern] (verified: compiled session had 3 turns)
- **[session] GEPA metric signature in the README** — `def dummy_metric(example, pred, trace=None, pred_name=None, pred_trace=None): return len(pred.reply) > 10`: five arguments, and a bool is accepted as a score. `README.md:686-687` [api] → here: `pairs.py` (five-argument metric)
- **[optimizer] `PromptOptimizer` is not a DSPy teleprompter** — `PromptOptimizer(signature, initial_prompt, merger_strategy="block_based", validation_strategy="full", config=Config())` subclasses `dspy.Module` but has no `forward`. `optimize(dataset, scorer: str | Callable, callbacks=None)` returns the final prompt **string** and no program. `dspy_optimizer/optimizer.py:13-58,195` [api]
- **[optimizer] Real loop order** — For each example: one `Evaluator` call (CoT) and `scorer(example, prediction)`. If wrong, up to `Config.max_refine_iters=5` times: Refiner proposes `(target_block, operation, content)` → `PromptPatch` → Merger builds a *candidate* → Validator checks the candidate → on valid, adopt it and `break`; on invalid, append to the failure history. An adopted prompt applies immediately to all later examples. The README headline order „Evaluator -> Refiner -> Validator -> Merger" (`README.md:139`) is not the code's order; merging precedes validation. `dspy_optimizer/optimizer.py:86-190` [api] (verified: `optimizer_checks.py` §4)
- **[optimizer] Validation runs on the training set** — `self.validator(candidate_prompt=…, evaluator=…, scorer=…, dataset=dataset, example=example)` passes the same `dataset` being optimized. DESIGN promises „a `training_set` and a `validation_set`" and „a full, separate validation set" (`DESIGN.md:33,48`); there is no held-out set, so an accepted patch is fitted to the data it is judged on. `dspy_optimizer/optimizer.py:152-158` [trap]
- **[optimizer] Strategy parameters are fixed through the optimizer** — Strategies are created with no arguments (`merger_class()`, `validator_class()`), so `batch_size=10`, `sample_size=3` and `threshold=1.0` are fixed unless you overwrite `opt.validator`. `dspy_optimizer/optimizer.py:46-51` [trap]
- **[optimizer] Registries** — mergers `{block_based}`, validators `{batched, full, sample, single_example}`, scorers `{exact_match, numeric}`. Registration happens on import of `dspy_optimizer.strategies` (`strategies/__init__.py:3-12` imports `batched, full, sample`; `single_example` arrives through `validation/__init__.py:3`). `dspy_optimizer/strategies/registry.py:31-34` [api] (verified: `optimizer_checks.py` §3)
- **[optimizer] Cost per failing example** — Up to `max_refine_iters` × (1 Refiner CoT call + validator calls). `full` makes up to N evaluator calls per candidate (fail-fast), `batched` up to 10, `sample` 3, `single_example` 1. Every call can double through the JSON fallback. There is no call budget and no early stopping. `dspy_optimizer/optimizer.py:106-190` [number] (derived from code)
- **[optimizer] Evaluation counter is wrong** — `state["total_evaluations"] += 1` once per validation regardless of how many evaluations the validator ran; the code says „TODO: This is a simplification". Observed 8 real evaluator calls against `total_evaluations=5`. `dspy_optimizer/optimizer.py:159-161` [trap] (verified: `optimizer_checks.py` §4)
- **[optimizer] Config fields that do nothing** — `Config(max_refine_iters=5, temperature=0.0, parallel_workers=8)` is frozen; `temperature` and `parallel_workers` are never read (grep finds no use outside `models.py`). Evaluation is sequential, so README „Parallel evaluation, serial merging" (`README.md:30`) is false. `dspy_optimizer/models.py:7-19` [trap] (verified: grep)
- **[optimizer] The deleted predecessor** — In 19fb8d2 (2025-07-24, „remove old samples"), the 380-line `invoice_amount_optimizer.py` was deleted. It had:
  - `InvoicePromptOptimiser`: refine until correct (`max_refine_iters+1` attempts), then merge the refined prompt into the base with an LLM `ChainOfThought(PromptMerger)`;
  - a final accuracy pass on a `ThreadPoolExecutor(parallel_workers)` with `math.isclose(abs_tol=0.002)`;
  - a Dutch-number `parse_float`;
  - prompt changes made by mutating `self.extractor.predict.signature.instructions = prompt`, which is the shared-state pattern the current `with_instructions` Evaluator replaced;
  - `azure/gpt-4o-mini` with keys from `.env` loaded at import;
  - a `DummyModel` that „Always returns 0.0 to force the refiner to work" and is never called.

  `git show 19fb8d2^:dspy_optimizer/invoice_amount_optimizer.py:18-25,104-112,155-171,183-194,202-216,262-346` [pattern] (verified: read from git history)

## MET

- **[session] `score()` spends one metric call probing arity** — Before scoring, `score()` calls `metric(dspy.Example(), dspy.Prediction(), None)` once to learn the arity: TypeError means two arguments, any other exception means three. A metric runs N+1 times for N turns (observed 3 calls for 2 turns; the first saw `{}`). An LLM-judge metric spends a real call on empty input. `dspy_session/session.py:1092-1101` [trap] (verified: `session_misc.py` §4) → here: `lmrun.py` (no metric may be called for discovery)
- **[session] `gold=None` makes label metrics trivially 1.0** — Without gold, `score()` builds the example from the turn's own inputs, history and **outputs**, so any label-comparing metric compares the prediction with itself (observed `[1.0, 1.0]`). Only reference-free metrics mean anything here. The docstring says „If gold is None, each turn's own outputs are included in the example labels". `dspy_session/session.py:1085-1109` [trap] (verified: `session_misc.py` §4)
- **[session] Metric errors score 0.0** — `on_metric_error="zero"` (default) logs `logger.warning("Metric error on turn %s: %s")` and scores 0.0; `"raise"` re-raises. A metric returning `None` also becomes 0.0 (`turn.score = float(s) if s is not None else 0.0`). A TypeError raised *inside* the metric body is first mistaken for an arity problem and retried with the other arity. `dspy_session/session.py:1111-1135` [trap] (verified: `session_misc.py` §4)
- **[session] `Prediction(score, feedback)` metrics lose their feedback** — `score()` accepts GEPA-style metrics through `float(Prediction)` and keeps only the score (observed `[0.25, 0.25]`). `dspy_session/session.py:1134` [trap] (verified)
- **[session] `min_score` without scores drops everything** — `to_examples(min_score=…)` with no `metric` and no prior `score()` keeps nothing, because `turn.score is None` fails the filter. `dspy_session/session.py:1159-1162` [trap] (verified: 0 examples)
- **[session] Trajectory filtering** — `to_examples(metric=None, min_score=None, include_history=True, strict_trajectory=False, require_outputs=True)`:
  - `strict_trajectory=True` stops at the first turn that fails `min_score` or has empty outputs, dropping it and every later turn („later turns may rely on a flawed answer", `README.md:420-421`);
  - otherwise failing turns are skipped.

  README numbers from a real run: 4 turns → „Kept 3 of 4 turns" and „Strict kept: 0 turns" (turn 0 „Hello" had no code). `dspy_session/session.py:1139-1171`; `README.md:405-433` [number/api] (verified: `test_session.py:1095-1140` pass)
- **[session] Scores are stored on the turn** — `Turn.score` is a mutable field that `score()` overwrites; re-scoring with another metric replaces the old value, and there is no metric name. `dspy_session/session.py:61-69,1134` [api]
- **[optimizer] Scorer contract** — `scorer(example, prediction) -> bool`, called with 2 arguments (`optimizer.py:92`; `DESIGN.md:54` „returns `True` or `False`"). Both built-ins take the **first** non-input key of the example; other labels are ignored (`test_common_scorers.py:29-33` asserts this). `dspy_optimizer/strategies/scoring/common.py:25-31,64-70` [api]
- **[optimizer] `exact_match` is strict** — `str(expected) == str(predicted)`: case- and whitespace-sensitive. `80.0` vs `"80"` → False; `"pass"` vs `"pass "` → False. `dspy_optimizer/strategies/scoring/common.py:43` [api] (verified)
- **[optimizer] `numeric` scorer bug** — `s = s.replace(",", "")` removes every comma, so the next line `s.replace(",", ".")` („This is safe because all commas have been removed") never fires. Results: `"80,50"` → 8050.0 (False against 80.5); `"1.234,56"` → False; only US `"1,234.56"` parses. Tolerance is `math.isclose(rel_tol=1e-6)` with no `abs_tol`, so 0.0 vs 1e-7 → False, and `tolerance` cannot be passed through the optimizer. The deleted predecessor's `parse_float` handled `'€ 1.234,56' -> 1234.56` correctly (`19fb8d2^:…invoice_amount_optimizer.py:183-194`) and used `abs_tol=0.002`. `dspy_optimizer/strategies/scoring/common.py:76-95` [trap] (verified: `optimizer_checks.py` §2)
- **[optimizer] Scorers fail closed, except one case** — They return False on missing keys or parse errors (`common.py:29-33,39-40,89-90`). An Example built without `with_inputs` raises `ValueError` from `example.inputs()`, which is not caught (`except (AttributeError, IndexError)`). `dspy_optimizer/strategies/scoring/common.py:26-33` [trap] (verified)
- **[optimizer] Validation strategies (acceptance policies)** — All four are in `dspy_optimizer/strategies/validation/`:
  - `full`: every example, returns False at the first miss; `True` if all pass, **including an empty dataset** (the loop never runs). `full.py:12-60`
  - `batched`: `random.sample(dataset, min(batch_size=10, len))`, unseeded, fail-fast; `if not dataset: return True  # An empty dataset trivially passes.` `batched.py:13-76`
  - `sample`: `sample_size=3`, `threshold=1.0`; returns `{"is_valid": score >= threshold, "score": mean(bools)}`; empty → `{"is_valid": True, "score": 1.0}  # Vacuously true`. `sample.py:12-74`
  - `single_example`: only the example that triggered the refinement; raises `ValueError("SingleExampleValidationStrategy requires 'example' in kwargs.")` if it is missing; „provides no guarantee that the change does not negatively impact other examples". `single_example.py:11-52`

  [api/trap] (verified: all three empty cases in `optimizer_checks.py` §3)
- **[optimizer] Validator results are normalised** — The loop accepts `bool` or `{"is_valid", "score"}` and writes `state["validation_score"]`, which is the bool itself for bool validators. `dspy_optimizer/optimizer.py:163-170` [pattern]

## DATA

- **[session] One example per turn** — Each turn becomes `dspy.Example(**inputs, history=history_snapshot, **outputs).with_inputs(*inputs, "history")`; `include_history=False` omits history. All outputs become labels, including CoT `reasoning` and the ReAct `trajectory`. `dspy_session/session.py:1164-1169`; `dspy_session/tests/test_session.py:473-541` [recipe] (verified: tests pass; `session_opt.py` input keys `['history','question']`, history lengths `[0,1,2]`) → here: `trainset.py`
- **[session] Pooling sessions** — `Session.merge_examples(*sessions, **to_examples_kwargs)` concatenates; `to_trainset` is an alias of `to_examples`. `dspy_session/session.py:1173-1181` [api]
- **[session] What is recorded as input** — For a `Predict` root, only signature inputs except the history field. For a program, only the named parameters of `forward` (unless it has `**kwargs`, in which case everything except history). Runtime kwargs such as `config=` or `lm=` are therefore not recorded. `dspy_session/session.py:911-937` [api]
- **[session] Output extraction order** — Prediction-like `keys()`, then dict, then `model_dump()`, then `.dict()`, then the Predict's output-field attributes, and as a last resort `{"output": result}`. A `forward` returning a bare string is stored as `{"output": …}` (`README.md:215,222`). `dspy_session/session.py:939-973` [api/trap] (verified: `render.py` (c))
- **[session] Gold turns without an LM call** — `add_turn(inputs, outputs)` appends a deep-copied turn whose snapshot is the current history. `pop_turn()` returns the last turn or None; `undo(steps=1)` pops up to `steps` turns. `dspy_session/session.py:979-1004` [recipe] → here: a person's judgement added as a labelled example
- **[session] Record-time copying** — `_record_turn` deep-copies inputs and outputs (`copy.deepcopy`). The snapshot is not copied: under `use_if_provided` it *is* the caller's History object (identity check True). `dspy_session/session.py:826-836` [api] (verified: `session_misc.py` §6)
- **[optimizer] Dataset shape** — `list[dspy.Example]` with `with_inputs`; labels are the non-input keys, and the loop uses only the first (`list(expected_outputs.keys())[0]`). An example with no label raises IndexError. `dspy_optimizer/optimizer.py:113-126` [api/trap]
- **[optimizer] Predecessor's PDF data preparation** — `Attachments(file_path + "[tile:1x1]" + ("[pages:1,2,3,-2,-1]" if pages > 5 else ""))`, with the page count from `pdfplumber`, the label column `totaal_excl_btw`, and data from `data/invoices/grouped_df.parquet` (never committed). `git show 19fb8d2^:dspy_optimizer/invoice_amount_optimizer.py:32-51,349-364` [recipe]

## RLM

- **[session] The documented failure (DSPy 3.1.3)** — `sessionify(dspy.RLM("user -> assistant"))` then `chat(user='hello')`: the trajectory has 20 entries of `{'reasoning','code','output'}`. Every `output` is `'[Error] Unsupported value type: History'`, whatever the code did (`SUBMIT(...)`, bare strings, `print`, `llm_query`, `llm_query_batched`). Then „WARNING dspy.predict.rlm: RLM reached max iterations, using extract to get final output". The final `Prediction(final_reasoning='Extract forced final output', assistant='Hello! How can I help you today?')` looks like a normal answer. `docs/rlm.md:5-29` [trap/number] (verified: the transcript, plus the mechanism in the 3.1.3 source, next item)
- **[session] Why it happened in 3.1.3** — `RLM._validate_inputs` only checked for *missing* inputs (`3.1.3 dspy/predict/rlm.py:346-350`), so the session's extra `history` kwarg reached the REPL as a variable. `PythonInterpreter._serialize_value` had no `BaseModel` branch and raised `CodeInterpreterError(f"Unsupported value type: {type(value).__name__}")` on every code execution. `3.1.3 dspy/primitives/python_interpreter.py:418-452` [trap] (verified: 3.1.3 source installed with `--no-deps`)
- **[session] On 3.3.1 the same code fails at once** — `ValueError: Unexpected inputs not declared in the signature: ['history']`, before any LM or sandbox work. 3.3.1 validates both directions: „Missing required inputs" and „Unexpected inputs not declared in the signature". `dspy/predict/rlm.py:425-438` [trap] (verified: `session_misc.py` §1)
- **[session] 3.3.1 can serialise a History into the sandbox** — `_serialize_value` and `_to_json_compatible` gained `BaseModel` branches (`python_interpreter.py:674,736`), so `_serialize_value(History(...))` returns `{'messages': [...]}`. An RLM whose signature *declares* `history: dspy.History` would pass validation and receive history as a dict. `dspy/primitives/python_interpreter.py:670-760` [api] (verified: direct call; not run end to end because Deno is not installed)
- **[session] The session also patches RLM's internal predictors** — Both `generate_action` and `extract` (`rlm.py:181-182`) get a `history` input. Their signatures (`variables_info`, `repl_history`, `iteration` → `reasoning`, `code`, plus the user outputs for extract) share no field with chat messages, so injected chat history would render as `None`-valued assistant turns. [trap] (verified: `session_misc.py` §1 lists both patched) → here: `rlm_ingest.py`: never put a History-injecting wrapper around `dspy.RLM`
- **[session] `dspy.RLM` 3.3.1 surface** — `RLM(signature, max_iters=20, max_llm_calls=50, max_output_chars=10_000, verbose=False, tools=None, sub_lm=None, interpreter_factory=PythonInterpreter)`; `forward(self, interpreter=None, /, **input_args)`.
  - Inputs must match the signature exactly.
  - `SandboxSerializable` values are injected with `to_sandbox()`, `sandbox_setup()` and `sandbox_assignment()`.
  - Reserved names are `llm_query`, `llm_query_batched`, `SUBMIT` and `print`, plus the result names `trajectory` and `final_reasoning`.

  `dspy/predict/rlm.py:139-190,408-478,701-736` [api] (verified: source read) → here: `rlm_ingest.py`, `check_dspy_surface.py`
- **[session] How to detect an RLM fallback answer** — On max iterations RLM logs „RLM reached max iterations, using extract to get final output" and sets `final_reasoning="Extract forced final output"` (3.3.1 `rlm.py:550,560` sync and `745,755` async; identical in 3.1.3 `rlm.py:404,414`). The output field looks normal. Treat `final_reasoning == "Extract forced final output"`, or a trajectory whose `output`s all start with `[Error]`, as „never reached", not as an answer. [trap] (verified: source and `docs/rlm.md:23,27`) → here: `rlm_ingest.py` (P15)

## RAG

- **[session] Keep bulky retrieval out of history** — `sessionify(dspy.Predict(RAGAnswer), exclude_fields={"context"}, max_turns=10)`: history messages keep `question`/`answer` while `turn.inputs` still holds `context` for training data. `history_input_fields={"question"}` is the allow-list form. When a field is in both, `exclude_fields` wins; `exclude_fields` applies to outputs as well, `history_input_fields` only to inputs. `README.md:239-299`; `dspy_session/session.py:1024-1034`; `dspy_session/tests/test_session.py:177-188,206-253,999-1008` [recipe] (verified: tests pass)
- **[session] Excluding persistent context** — „Excluding it means the model will completely forget the document by turn 2"; exclude only data that is „different every turn and bulky". `docs/api-usage-examples.md:184` [recipe]

## AGENT

- **[session] Constructor** — `Session(module, *, history_field="history", max_turns=None, max_stored_turns=None, exclude_fields=None, input_field_override=None, history_input_fields=None, initial_history=None, history_policy="override", on_metric_error="zero", strict_history_annotation=False, copy_mode="deep", lock="none", on_turn=None, isolation="isolated", lifespan="persistent", consolidator=None, session_path="root")`.
  - Passing both `history_input_fields` and `input_field_override` raises ValueError.
  - `exclude_fields` always gains the history field.
  - `copy_mode` is `deep`, `shallow` or `none` (anything else raises ValueError).

  `dspy_session/session.py:209-284,483-490` [api]
- **[session] Factories** — `sessionify(module, **kwargs)` is just `Session(module, **kwargs)`. `with_memory(module, *, recursive=True, include=None, exclude=None, where=None, isolation="isolated", lifespan="persistent", consolidator=None, child_configs=None, **kwargs)` defaults `copy_mode="none"` and wraps nested predictors as child Sessions. `dspy_session/session.py:1287-1339` [api]
- **[session] How state reaches a module (three routes)** —
  1. The root predictor's signature gains `history: History`. If a History-typed input already exists, that name is used with the warning „Predictor already has history-like field …" (`session.py:527-554`).
  2. Every nested predictor's `forward`/`aforward` is replaced by a wrapper that fills the history kwarg from the contextvar `_CURRENT_SESSION_HISTORY` when absent (`557-587`).
  3. If the top-level `forward` accepts the history by name, by History annotation (resolved with `get_type_hints`), or through `**kwargs`, the history is passed directly (`589-634,764-768`).

  [api] (verified: `test_session.py:751-846` pass)
- **[session] `Turn` and what is fixed at call time** — `@dataclass class Turn: index, inputs, outputs, history_snapshot: History, score: float | None = None` is mutable (`Turn.__dataclass_params__.frozen` is False). The snapshot is the History built before the call, so later turns never change it (`test_session.py:279-291`). A turn is recorded only after a successful call (`test_session.py:1010-1024`). `dspy_session/session.py:61-69,689-696` [api] (verified)
- **[session] Saving loses the snapshots** — `Session.save_state()` (version 2) stores only `index`/`inputs`/`outputs`/`score` per turn. `Session.load_from` rebuilds every snapshot with the *loading* config (`design-notes.md:130` says so). A snapshot taken under `use_if_provided` (`[{'question':'injected',…}]`) comes back as `[]`. `dspy_session/session.py:1190-1215,1253-1263` [trap] (verified: `session_misc.py` §6)
- **[session] How history is built** — `initial_history` seed messages, then one message per turn: inputs not in `exclude_fields` (filtered by `history_input_fields` when set) plus outputs not in `exclude_fields`. Then `messages = messages[-self.max_turns:]`. `dspy_session/session.py:1016-1039` [api]
- **[session] `max_turns` counts messages, not turns** — Seed messages count and are evicted first: 2 seed + 1 turn with `max_turns=2` leaves `['s2','Q1']`. So „use `initial_history` to pin critical information" (`docs/api-usage-examples.md:135`) is false when combined with `max_turns`. `max_turns=0` means *unlimited* (`[-0:]` is the whole list). `max_stored_turns` trims stored turns permanently (`session.py:839-840`). `dspy_session/session.py:1036-1037` [trap] (verified: `session_misc.py` §6-7)
- **[session] `on_turn` hook** — `on_turn(session, turn)` fires after recording. Exceptions are swallowed with `logger.warning("on_turn callback error: %s", e)`. It does not fire for `override` pass-through. Forks share the callback; `with_memory` children get `on_turn=None`. At hook time `turn.score is None` always, because scores come only from `score()`. `dspy_session/session.py:842-846,470`; `README.md:880-883`; `dspy_session/tests/test_session.py:1178-1252` [api] (verified: `session_misc.py` §8) → here: `lmrun.py`-style per-call records (attach there, and record `dspy.settings.lm.history[-1]` yourself; the Turn has no raw output, tokens or cost)
- **[session] Memory-policy axes** —
  - Isolation: `"isolated"` means a child builds history from its own ledger; `"shared"` means a non-root child reads the outer/root history and records nothing (`session.py:680-690`).
  - Lifespan: `"persistent"`; `"episodic"`: at the end of each root call, if the child has turns, `consolidator(past_memory=l2, episode_transcript=_serialize_turns(turns))` runs, the result goes to `l2_memory`, and the turns are cleared (`882-902`); `"stateless"`: records nothing (`670,673,690`) and is cleared at finalize (`904-905`).
  - Finalization happens only at the root-call boundary and never for `override` replays (`699-701`).
  - Consolidator errors are only logged (`893-899`). Its output is read from `updated_memory`/`memory`/`l2_memory`/`output`, then the first key, then `str(pred)` (`1432-1457`).

  [api] (verified: `test_with_memory_policies.py` pass)
- **[session] `child_configs` and selection** — `child_configs` is keyed by dotted path: `{"enabled": False}` leaves that branch raw, and `isolation`/`lifespan`/`consolidator` override per child. `include`/`exclude` match a path exactly or as a `prefix + "."`; `where(path, obj)` is a predicate. Pre-sessionified children are adopted rather than double-wrapped. `dspy_session/session.py:390-477` [api] (verified: tests pass)
- **[session] Per-user state for serving** — `SessionState(turns, initial_history, l2_memory, node_states)`, `session.new_state(initial_history=None, l2_memory="")` and `with session.use_state(state):` (sync or async). A contextvar maps `id(session)` to the state, and child sessions route to `root_state.node_states[path]`, created lazily. Concurrent `asyncio.gather` tasks stay isolated. `dspy_session/session.py:72-191,290-328`; `dspy_session/tests/test_state_binding.py:41-83` [api] (verified: tests pass)
- **[session] Two persistence formats, and one that loses children** — `SessionState.to_dict()` is **version 1** and includes a per-turn `history_snapshot` and `node_states`; `from_dict` rejects other versions. `Session.save_state()` is **version 2** without snapshots; `load_from` accepts 1 and 2 and maps the v1 key `input_field_override` to `history_input_fields`. In unbound notebook mode, children keep their own `_default_state`, so `app.save_state()["node_states"] == {}` and child ledgers are lost. `dspy_session/session.py:99-157,1190-1271,857-863` [trap] (verified: inline probe: unbound `node_states: {}`, bound `['worker']`)
- **[session] Projection helpers** — Each returns `None` or `""` outside an active call:
  - `get_current_history()`: the current node's L1 history;
  - `get_outer_history()`: the root history;
  - `get_node_memory()`: the current node's `l2_memory`;
  - `get_child_l1_ledger(path)`: a YAML-like dump `- turn: i` / `inputs: {json}` / `outputs: {json}`;
  - `get_execution_trace()`: `name: turns=N l2_chars=M` lines plus `active_stack=root > …`.

  Child paths resolve by exact match, by a `root.` prefix, or by a unique suffix. `dspy_session/session.py:1342-1429`; `dspy_session/tests/test_state_binding.py:127-168` [api] (verified: tests pass)
- **[session] „Push, Don't Peek"** — „If Node A needs Node B's data, Node B must push it as an explicit output." Hidden side channels break optimizer causality: „When the optimizer tries to figure out why the writer hallucinated, the causal trace is broken. Optimization fails silently." There is no sibling-to-sibling or all-to-all projection; upward data goes through a consolidator. The two exceptions are supervisory (`get_child_l1_ledger`) and omniscient (`get_execution_trace`), for auditor or reflection nodes only. For „what websites did you look at?" the ranked answers are (1) push the data as an output field, (2) consolidate it into L2, (3) supervisory projection. The table headed „The four projection types" lists five helpers. `docs/api-usage-examples.md:975-1111` [pattern] → here: P13, and any multi-step DSPy pipeline (data flows only through fields)
- **[session] Approach 2's code in the docs does not work** — The orchestrator reads `notes = get_node_memory()`, but that returns the *root's* `l2_memory`. The researcher's consolidated memory lives in `state.node_states["researcher"].l2_memory`, which the orchestrator never sees (observed `['', '']` while the researcher held `'|n=1|n=1'`). `docs/api-usage-examples.md:1019-1063` [trap] (verified: `session_misc.py` §10)
- **[session] Wire-format analysis (design doc)** — Five strategies for what nested predictors see:
  1. per-predictor history;
  2. outer history, signature-filtered;
  3. outer history inline as text;
  4. `{"role":"history","user":…,"assistant":…}` field mapping;
  5. hybrid.

  Only Strategy 1 is „schema safe always"; 3-5 need TemplateAdapter. „Scenario B is the litmus test": a zero-overlap pipeline such as correct→translate breaks Strategy 2. The key insight: zero field overlap „is the **common case** for well-decomposed modules". `docs/v2-recursive-sessions.md:487-1406` [pattern] (verified: Strategies 1 and 2 on 3.3.1 in `render.py`)
- **[session] Plain `sessionify` on a composed program is Strategy 2** — Measured on 3.3.1 with `CorrectThenTranslate`: the corrector's prior assistant turns read `corrected: None`; the translator gets *no* user turns (no input field of its signature is in the root history) and only assistant turns `translated: …`. The string-returning `TravelAgent` from README Example 2 sends `travel_advice: None` as its previous answers. `with_memory` (children `isolated`) gives clean per-predictor histories (Strategy 1). `dspy_session/session.py:557-587`; `README.md:159-234`; `docs/decomposed-translator.md:77-100` [trap] (verified: `render.py` b, b2, c)
- **[session] ReAct under a session** — It runs (turn 2 answered „Your name is Max"), but turn outputs include the whole `trajectory` dict plus `reasoning` and are replayed every turn. The `react` step predictor sees prior turns as `next_thought`/`next_tool_name`/`next_tool_args` = `None`; only `extract` sees prior answers. `README.md:51-102` [trap] (verified: inline ReAct probe with DummyLM)
- **[session] `dspy.Parallel` workers get no history** — DSPy's `ParallelExecutor` copies only `thread_local_overrides` into worker threads (`dspy/utils/parallelizer.py:126-136,160`), so nested predictors called through `dspy.Parallel` see no injected history (observed `[0, None, None, 1, None, None]`). The same holds for `use_state` bindings inside worker threads. `dspy_session/session.py:35-58` [trap] (verified: `session_threads.py`)
- **[session] Locks are per Session object** — `lock="thread"` wraps `forward` in a `threading.Lock`; `lock="async"` creates an `asyncio.Lock` lazily in `aforward`. The lock belongs to the Session, not to a `SessionState`, so on a shared `with_memory` blueprint it serialises *all* users. `dspy_session/session.py:267-272,648-651,703-712` [trap] (verified: lock attribute probe)
- **[session] Async** — `acall` → `aforward`, which calls the inner module's `acall` or `aforward`; otherwise TypeError „… does not support async". `Session.acall` (`session.py:761-762`) overrides `dspy.Module.acall`, which in 3.3.1 adds `@with_callbacks`, the `caller_modules` context and `settings.track_usage` accounting (`dspy/primitives/module.py:112-129`). The Session layer therefore skips callbacks and usage tracking on async calls; the sync path goes through `Module.__call__`. `dspy_session/session.py:703-824` [api/trap] (verified: source read)
- **[session] `copy_mode="none"` edits the caller's module** — `with_memory` defaults to it. The caller's predictor gains a `history` input and a wrapped `forward` (`['question'] → ['question','history']`); `sessionify` (deep copy) leaves the caller untouched. `dspy_session/session.py:1323,513-587` [trap] (verified: `session_misc.py` §9)
- **[session] Design doc = draft; most of its API is not implemented** — Missing: `SessionContainer`, `CallRecord`/`record=`/`on_call`, `nested_sessions=`, `inner_scope=`, `to_examples(level="call", by="path")`, `Session.batch_run`, `reset/undo/fork(cascade=True)`, `Turn.print_trace_tree`, `session.replay`, `child_snapshots` time-travel. `sessionify(module, recursive=…)` raises `TypeError: Session.__init__() got an unexpected keyword argument 'recursive'`. What shipped instead is `with_memory` with isolation, lifespan and consolidator. The doc contradicts itself on the default nesting policy (`inherit` at lines 72 and 1918, `keep` at 121 and 229). The file is two byte-identical copies (1-1955 and 1956-3910). `docs/v2-recursive-sessions.md` [claim] (verified: TypeError probe; `diff` of the halves)
- **[session] Inner-state scopes (design doc)** — Scope A cross-turn, B per-outer-turn (fresh for ReAct and retry loops), C hybrid with turn-group tracking for `undo(cascade)`; „Scope C (hybrid) is the right default". What shipped maps roughly to `lifespan` persistent≈A and episodic≈B plus consolidation; C is not implemented. `docs/v2-recursive-sessions.md:1455-1689` [pattern]

## PROD

- **[session] MLflow add-on requirements** — `mlflow>=2.18`, checked when first called („mlflow >= 2.18 required (for mlflow.dspy flavor)"); `pandas` is needed for `log_examples`. Neither is declared in `pyproject.toml`, not even as an extra. `dspy_session/integrations/mlflow.py:42-63,219-222` [api] (verified: grep of `pyproject.toml`/`uv.lock`)
- **[session] `log_session`** — `log_session(session, *, experiment=None, run_name=None, log_model_flag=False, artifact_path="session", tags=None) -> run_id`. It logs:
  - params: `session.history_field`, `history_policy`, `max_turns`, `max_stored_turns`, `copy_mode`, `module_type` (a class name, not the LM);
  - metrics: `total_turns`; per turn `history_length` (step = `turn.index`) and `turn_score` only if scored; `score_mean`/`min`/`max` only if any turn is scored;
  - artifacts: `session_state.json`, `turns.json`, `examples.json`;
  - optionally `mlflow.dspy.log_model`, whose failure is only a warning.

  No tokens and no cost. `dspy_session/integrations/mlflow.py:71-187` [api] (verified: the committed run `71f90f4…` has exactly `total_turns=2` and `history_length` 0,1)
- **[session] `mlflow_turn_logger` never logs scores** — `mlflow_turn_logger(experiment=None, run_name=None)` returns a `TurnLogger`. The first turn starts a run named `session_<ModuleType>`; each turn logs `history_length` and `total_turns`; `.end(session)` logs `session_state.json` at the artifact root and ends the run. `turn_score` is guarded by `turn.score is not None`, which is never true inside `on_turn`. The committed `mlflow.db` run `2898734f…` (`session_Predict`) holds only `history_length` and `total_turns` at steps 0-2. Nothing ends the run if `.end` is forgotten. `dspy_session/integrations/mlflow.py:238-319` [trap] (verified: sqlite query)
- **[session] `load_model` falls back silently** — `load_model(uri, module=None, **kw)` uses the fallback module if `mlflow.dspy.load_model` fails (warning). If `session_state.json` cannot be downloaded it logs `logger.info("No session state found, creating fresh session.")` and returns an empty Session, so lost state is indistinguishable from a new session. `dspy_session/integrations/mlflow.py:355-392` [trap]
- **[session] `artifact_path` is deprecated in MLflow 3** — `mlflow.dspy.log_model(dspy_model, artifact_path=…)` is documented as „artifact_path: Deprecated. Use `name` instead." in mlflow 3.16.1, and `Model.log` warns. Both repos pass `artifact_path`. `dspy_session/integrations/mlflow.py:182-185,340-344`; `dspy_optimizer/callback/mlflow_callback.py:120-123` [api] (verified: `inspect.getsource` in mlflow 3.16.1)
- **[session] What the committed `mlflow.db` contains** — Experiment `my_chatbot` with 6 runs, 3 of them `FAILED` with no params or metrics; one `log_examples` dataset `chatbot_v1` (context `session_examples`); no traces, spans or logged models. `/home/user/dspy-session/mlflow.db` [number] (verified: read-only sqlite)
- **[session] JSON coercion never reports a fallback** — `_safe_serialize_value` tries primitives, then `model_dump()`, `toDict()`, dict/list recursion, and finally `str(v)`, silently and without a count. The MLflow copy `_safe_json_value` lacks the `toDict()` branch, so the two are not identical. `dspy_session/session.py:1491-1512`; `dspy_session/integrations/mlflow.py:400-416` [trap] (verified: `test_session.py:954-961` asserts the `str` fallback)
- **[optimizer] `MLflowCallback` reads keys the loop never writes** — `MLflowCallback(experiment_name, tracking_uri=None, run_name=None)` creates the experiment if missing (MlflowException → `ConnectionError`). Its hooks read `initial_prompt`, `merger_strategy`, `validation_strategy`, `scorer`, `score`, `new_prompt` and `optimizer`, none of which the loop writes. Driven by the real `optimize()`, it logs `log_params({})`, `is_valid` metrics (never `validation_score`), and the patch op/target params plus the patch text on success. It never logs the prompt text or the model. `dspy_optimizer/callback/mlflow_callback.py:35-125` [trap] (verified: `optimizer_checks.py` §5 with MagicMock)
- **[optimizer] mlflow is a hard dependency anyway** — `pyproject.toml:13` requires `mlflow>=3.1.4` (plus `attachments`, `pytesseract`, `tqdm`), so the lazy-import guard (`mlflow_callback.py:8-14`) only matters in trimmed installs. `pyproject.toml:10-15` [api]
- **[optimizer] Logging** — The core loop has 5 `print()` calls (a sixth is in `main()`); in the probe they printed 15 lines for 2 examples and hard-codes the invoice field `getattr(example, 'amount', '')` in a „domain-agnostic" loop. No `logging` module is used, while the repo's standard says „No `print` except in CLI demos" (`README.md:97`). `dspy_optimizer/optimizer.py:94-121` [trap] (verified: grep; stdout capture)
- **[optimizer] `HistoryCallback`** — An in-memory list of `{"event": name, **state}`, one per hook; zero dependencies. Entries hold live `Example`/`Prediction`/`PromptPatch` objects and need conversion before JSON. `dspy_optimizer/callback/history_callback.py:8-59` [pattern] → here: `lmrun.py` (per-step record)
- **[optimizer] No usage or cost accounting** — The only token or cost values are the MockLLM's zero `usage` and `_hidden_params`. `tests/conftest.py:47-52` [api] (verified: grep)

## TEST

- **[session] How the suite fakes the LM** — Every test replaces `predict.forward` (and `__call__`) with a canned-response function, so no LM or adapter formatting ever runs. As a result the suite cannot see None-filled history, copies calling the original predictor, lost history in Parallel workers, or the RLM failure. `dspy_session/tests/test_session.py:50-62`; `dspy_session/tests/test_readme_usage.py:16-28` [trap] (verified: all found defects coexist with 102 passing tests)
- **[session] Probe rendering with DummyLM instead** — Configure `DummyLM([...])`, run the session, and assert on `lm.history[i]["messages"]`: that shows exactly what reaches the provider. [recipe] (verified: `render.py`) → here: `lm_fixture.py`, `check_dspy_surface.py`
- **[session] Tests that cannot fail for the right reason** — `test_load_from_preserves_history_snapshots` (`test_session.py:664-682`) passes because rebuilding equals the original for a plain session. `test_fork_deep_copies_module` (`457-464`) asserts only `is not`. `dspy_session/tests/test_session.py` [trap]
- **[session] Async and README tests** — Async tests use `@pytest.mark.anyio` and need anyio's pytest plugin, which is installed with DSPy's dependencies (`test_state_binding.py:63`, `test_readme_usage.py:173`). README patterns are covered in `test_readme_usage.py`, but README Example 2 (string return) and Example 4 (BootstrapFewShot) are not. [api]
- **[optimizer] `MockLLM(dspy.BaseLM)`** — A legacy `forward` returns `SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=text, tool_calls=None), logprobs=None)], usage={0,0,0}, model=self.model)` plus `_hidden_params={"response_cost": 0.0}`. It runs unmodified on 3.3.1. The tests set `response_text` to a JSON object, which ChatAdapter cannot parse, so each predictor call makes **2** LM calls through the JSONAdapter fallback, and the history assertions inspect the fallback's messages. ChatAdapter-formatted text gives 1 call; the default „mocked response" raises `AdapterParseError`. `tests/conftest.py:9-53` [recipe] (verified: `optimizer_checks.py` §1) → here: `lm_fixture.py`
- **[optimizer] Global LM fixture** — `dspy.settings.configure(lm=llm)` is set per test and never reset, so it leaks into later tests. `tests/conftest.py:56-65` [trap]
- **[optimizer] Assert on the rendered prompt** — Read `mock_llm.history[-1]["messages"]` and assert that the dynamic prompt appears in the system message and every input in the user message. This catches fields that never render. `tests/dspy_optimizer/test_evaluator.py:41-47`; `tests/dspy_optimizer/refiner/test_refiner.py:53-65` [recipe] (verified: tests pass) → here: `lm_fixture.py`, P19
- **[optimizer] The integration test mocks both ends** — `test_optimizer_full_run` monkeypatches `Refiner.__call__` and `FullValidationStrategy.__call__`, so a real refiner output parsed into `PatchOperation` is never run against the merger and a real validator. `tests/dspy_optimizer/test_optimizer.py:33-50` [trap]
- **[optimizer] MLflow tests** — They hand-build state dicts with the keys the callback reads (`initial_prompt`, `score`, `new_prompt`, `optimizer`), not the keys the loop produces, so they pass while the integration is broken. Without mlflow installed, 5 of 6 fail with `AssertionError` at `assert MlflowException is not None` (`mlflow_callback.py:56`), because the mock patches `mlflow` but not `MlflowException`. `tests/callback/test_mlflow_callback.py:42-130` [trap] (verified: 38/43 and 43/43 runs)
- **[optimizer] Deterministic sampling in tests** — `monkeypatch.setattr("random.sample", lambda data, size: data)`. `tests/dspy_optimizer/strategies/validation/test_validation_strategies.py:74` [recipe]
- **[optimizer] Degradation tests for scorers** — Each scorer has a pass test and a garbage-input test (e.g. `"N/A"` → False). Nothing tests a decimal comma, which is why the numeric bug survived. `tests/dspy_optimizer/strategies/scoring/test_common_scorers.py:36-69` [pattern]

## PAT

- **[session] Linearisation first** — „Each turn stores a history snapshot at call time. `to_examples()` emits independent `dspy.Example`s … This aligns with DSPy optimizers that expect independent examples." `docs/design-notes.md:39-46` [pattern] → here: `trainset.py`
- **[session] Cut a trajectory at the first bad turn** — `strict_trajectory`: a bad earlier turn contaminates the history of every later turn, so drop from there on. `dspy_session/session.py:1154-1162` [pattern] → here: superseded upstream decisions
- **[session] Two-level memory with consolidation** — L1 is the per-node turn ledger; L2 is `l2_memory`, a string distilled by a consolidator `Signature("past_memory, episode_transcript -> updated_memory")` at episode end. `dspy_session/tests/test_with_memory_policies.py:29-42`; `docs/api-usage-examples.md:570-612` [pattern]
- **[session] Shared blueprint, per-user state** — One module instance serves all users; each user's state is bound through a contextvar for the duration of a `with` block. `dspy_session/session.py:167-191,302-328` [pattern]
- **[session] Versioned JSON state** — A `version` key, explicit rejection of unknown versions („Unsupported session state version: 999. Supported versions: 1, 2."), and one compatibility branch for a renamed key. `dspy_session/session.py:1221-1234` [pattern]
- **[optimizer] Self-critique with a failure history** — Each refinement attempt gets the list of previously rejected patches, so the model does not repeat them; the signature docstring shows a worked example where „a generic 'be more careful' rule already failed" and asks for a more specific one. `dspy_optimizer/optimizer.py:106,184-187`; `dspy_optimizer/refiner/signature.py:39-48` [pattern]
- **[optimizer] Worked examples in the instructions** — Two complete Analysis → Suggestion → Target Block → Operation → Content cases sit inside the Signature docstring, as instructions rather than `demos`. `dspy_optimizer/refiner/signature.py:14-107` [pattern]
- **[optimizer] Registry plus string-or-callable selection** — `Registry(name)` with a `register(name)` decorator (raises ValueError on a duplicate) and `get(name)` (KeyError „'x' not found in 'y' registry."). `optimize()` converts that KeyError into `ValueError("Scorer '…' not found in registry.")`. `dspy_optimizer/strategies/registry.py:6-34`; `dspy_optimizer/optimizer.py:69-76` [pattern]
- **[optimizer] Frozen config and patch objects, an enum of operations** — `@dataclass(frozen=True)` for `Config` and `PromptPatch`; `PatchOperation(Enum)` with APPEND and REPLACE; the tests assert `AttributeError` on mutation. `dspy_optimizer/models.py:7-44`; `tests/dspy_optimizer/test_models.py:42-50` [pattern]

## SKILL

- **[optimizer] Block-structured text artifact, structured patch, deterministic merge** — A prompt with `### Name` headers (`### Task / ### Output format / ### Examples / ### Heuristics`, `README.md:27-29`). The model proposes `PromptPatch(target_block, operation, content)`; `BlockBasedMerger` finds `^{re.escape(target_block)}.*$` (MULTILINE), treats the block as running to the next `^###\s` or end of string, then APPENDs (`rstrip` + `"\n" + content + "\n"`) or REPLACEs the body and keeps the header. The result is `.strip()`ped, and a missing block raises „Target block '…' not found in prompt." `dspy_optimizer/strategies/merger/block_based.py:18-59` [pattern] (verified: tests plus `optimizer_checks.py` §6) → here: job 4 (SKILL.md/description optimization): patch named sections instead of regenerating the text
- **[optimizer] Block matching is a case-sensitive prefix match** — `"### Ex"` patches `### Examples`; `### HEURISTICS` does not match `### Heuristics`. The Refiner docstring's examples use upper-case headers (`signature.py:19-24`), while the README convention is mixed case. [trap] (verified: `optimizer_checks.py` §6) → here: job 4 (headers must be chosen from the document by code, P26)
- **[optimizer] Acceptance policy for an edited artifact** — Validation strategies decide whether a patch is kept: all examples, a random batch, a thresholded sample, or only the triggering example. All of them accept a patch when there is nothing to check. `dspy_optimizer/strategies/validation/*.py` [pattern/trap] → here: job 4, `baseline.py` (compare against a floor; refuse empty sets)

## TRAP

- **[session] Copies and forks run the original predictor** — After `deepcopy`/`fork()`/optimizer copies, the wrapper's closure (`session.py:562-571`) calls the original predictor, so optimizing a Session is a silent no-op: 0 demos, and the original is still what runs. See OPT. [trap] (verified: `session_copy.py`, `session_opt.py`)
- **[session] Composed programs get `None`-filled history** — Plain `sessionify` injects root history signature-filtered into every nested predictor; unmatched outputs render as `None` and unmatched inputs vanish. README Examples 1-2 show a „remembering" chat that sent `travel_advice: None` as prior answers. See AGENT. [trap] (verified: `render.py`)
- **[session] RLM plus session** — On 3.1.3 all 20 iterations fail silently and an extract-fallback answer looks normal; on 3.3.1 it fails with an immediate `ValueError`. See RLM. [trap] (verified)
- **[session] Unsupported history annotations** — `Optional[History]` and History subclasses are accepted by the session (`_is_history_annotation`, `session.py:1460-1488`) but not by DSPy's adapters, so the history is silently rendered as inline JSON. [trap] (verified: `session_misc.py` §2)
- **[session] `strict_history_annotation` is described wrongly** — The docs say non-strict mode uses „name heuristics" and that `search_history: list[str]` could be confused with the history field (`docs/api-usage-examples.md:354-356`). The code never looks at names: non-strict additionally accepts `History` subclasses; strict accepts only `History` itself (`session.py:1476-1486`). `search_history` is never picked in either mode. [trap] (verified: `session_misc.py` §3)
- **[session] Snapshots are not persisted; `max_turns` quirks** — Save/load rebuilds snapshots; `max_turns` counts seed messages and `0` means unlimited; `on_turn` never sees a score; unbound `with_memory` saves no child ledgers; `copy_mode="none"` mutates the caller's module; `override` does not protect children; locks serialise all users; Parallel workers lose history. See AGENT/OPT. [trap] (verified)
- **[session] Metric edge cases** — The arity probe is an extra real call; `gold=None` self-labelling scores 1.0; errors and `None` become 0.0, the same as a genuinely wrong answer; feedback is dropped; `min_score` without a metric drops everything. See MET. [trap] (verified)
- **[session] Documentation defects** —
  - `README.md` is two concatenated copies: lines 1-1048 are newer (they include `with_memory`, `SessionState`, projection helpers) and 1049-1990 are an older copy without them.
  - `docs/v2-recursive-sessions.md` is two identical copies.
  - `docs/session-recursion.md:42-56` shows `NameError: name 'sessionify' is not defined`.
  - `docs/untitled.md` is empty.
  - `mrmd.md` repeats a template 4 times.
  - `docs/multiple-signatures.md` uses a non-existent `append_history=True`.
  - `docs/api-usage-examples.md:182` advises excluding `rationale`.
  - The Approach 2 code does not work.
  - `docs/sessionify-vs-with-memory.md:69` says sessionify has per-node policy controls „Available", but only `with_memory` wires `child_configs`.

  [trap] (verified: `diff`, probes)
- **[session] Committed run artefacts** — `session.json`, `therapy_session.json`, `mlflow.db` (626 KB) and `mlruns/` are in the repo, and the mlflow db records the author's absolute paths (`/home/maxime/Projects/dspy_session/...`). No API key appears anywhere (grep for `sk-`, `gsk_`, `API_KEY`, `api_key=` finds nothing). [claim → checked]
- **[optimizer] Validators pass on nothing** — `full`, `batched` and `sample` all accept a candidate on an empty dataset (`True` / `{"is_valid": True, "score": 1.0}`). [trap] (verified) → here: `baseline.py`/P23: an empty comparison set must fail or be reported, never pass
- **[optimizer] One bad field in the model's output crashes the whole run** — The refiner's `operation: str` goes through `PatchOperation(refiner_output.operation)`, which raises „'Append' is not a valid PatchOperation"; an unknown block name raises in the merger. Neither is caught in `optimize()`. `dspy_optimizer/optimizer.py:139-146`; `dspy_optimizer/refiner/signature.py:134-137` [trap] (verified) → here: type such outputs as `Literal[...]` built from the document by code (P26)
- **[optimizer] Refinement history is mislabelled** — The history string uses `f"Failed Attempt {i + 1}: …"` where `i` is the example index, so every failed attempt on example 2 is labelled „Failed Attempt 2". `dspy_optimizer/optimizer.py:184-187` [trap] (verified: `optimizer_checks.py` §4)
- **[optimizer] Asymmetric callback lifecycle** — On a successful merge `on_refinement_end` is never called, because `break` at line 180 precedes lines 189-190. Observed sequence: `refinement_start, validation_start, validation_end, merge_success, run_end`. DESIGN's `on_validation_success` hook does not exist, and callbacks cannot „control the flow of the optimization (e.g., early stopping)" (`DESIGN.md:26-27`): their return values are ignored. `dspy_optimizer/optimizer.py:175-193` [trap] (verified)
- **[optimizer] Loop counter, JSON fallback, scorer, MLflow** — `total_evaluations` undercounts; the JSON fallback doubles calls; the numeric scorer breaks on decimal commas; `MLflowCallback` logs almost nothing through the real loop; no held-out validation set; strategies cannot be configured. See OPT/MET/PROD. [trap] (verified)
- **[optimizer] Documentation outruns the code** —
  - `README.md:74-78,153` and `DESIGN.md:83-87` describe `examples/dutch_invoices/{optimize.py,dataset.py,data/}` as implemented („Complete, end-to-end example"). No `examples/` or `notebooks/` path exists in any of the 25 commits.
  - `README.md:126-127` shows `GenericPromptOptimiser(model, base_prompt, PhoneExtractor)` and `opt.optimise(dataset)`; neither exists (the real API is `PromptOptimizer(...).optimize(...)`).
  - `README.md:158` lists `SingleExampleValidationStrategy` as roadmap, although it exists.
  - `SampleValidationStrategy` is documented nowhere.
  - The `[project.scripts] dspy-optimizer = "dspy_optimizer:main"` entry point prints „Hello from dspy-optimizer!" (`dspy_optimizer/__init__.py:1-2`).
  - `dspy_optimizer/refiner.py` is an empty file shadowed by the `refiner/` package.
  - `scoring/base.py` is empty.

  [trap] (verified: `git log --all -- examples` empty; entry point run)
- **[optimizer] Comments that are wrong** — `single_example.py:49` says „The evaluator is a dspy.Predict module" (it is a ChainOfThought wrapper); `common.py:81-82` says the second replace is „safe because all commas have been removed" (so it is dead code). [trap]

---

## 3. Code worth keeping

**[session] Contextvar injection into nested predictors** — `dspy_session/session.py:557-587`. Runs on 3.3.1 (102 tests pass). Keep in mind that `orig_forward` is captured once, so a deep copy keeps calling the original; bind at call time (e.g. `type(_self).forward(_self, **kwargs)`, a suggestion not tested here) or re-wrap after copying.
```python
def _wrap_predictor(self, predictor: dspy.Predict, field_name: str) -> None:
    """Wrap predictor.forward/aforward to inject history from contextvar when absent."""
    if getattr(predictor, "_dspy_session_wrapped", False):
        return

    orig_forward = self._get_attr_quiet(predictor, "forward")
    if orig_forward is None:
        raise AttributeError(f"Predictor {type(predictor).__name__} has no forward method.")

    def wrapped_forward(_self, **kwargs):
        if field_name not in kwargs:
            h = _CURRENT_SESSION_HISTORY.get()
            if h is not None:
                kwargs[field_name] = h
        return orig_forward(**kwargs)

    predictor.forward = types.MethodType(wrapped_forward, predictor)
    # ... same for aforward ...
    predictor._dspy_session_wrapped = True
```

**[session] History policies at the call boundary** — `dspy_session/session.py:663-690`. Runs on 3.3.1 (`test_readme_usage.py:56-83`).
```python
skip_finalize = False

# explicit-history policy handling
if explicit_history is not None and self.history_policy == "replace_session":
    state.initial_history = explicit_history
    state.turns.clear()
    run_history = self._build_history()
    record_turn = self.lifespan != "stateless"
elif explicit_history is not None and self.history_policy == "use_if_provided":
    run_history = explicit_history
    record_turn = self.lifespan != "stateless"
elif explicit_history is not None and self.history_policy == "override":
    # optimizer/stateless replay mode
    run_history = explicit_history
    record_turn = False
    skip_finalize = True
else:
    # topology handling when no explicit history is provided
    if self.isolation == "shared" and not is_root_call:
        shared_history = _CURRENT_OUTER_HISTORY.get()
        if shared_history is None:
            root = _ACTIVE_SESSION_ROOT.get()
            shared_history = root._build_history() if root is not None else self._build_history()
        run_history = shared_history
        record_turn = False
    else:
        run_history = self._build_history()
        record_turn = self.lifespan != "stateless"
```

**[session] Turns to Examples, with trajectory cutting** — `dspy_session/session.py:1152-1171`. Runs on 3.3.1 (`session_opt.py`).
```python
examples: list[dspy.Example] = []
for turn in turns:
    if require_outputs and not turn.outputs:
        if strict_trajectory:
            break
        continue

    if min_score is not None and (turn.score is None or turn.score < min_score):
        if strict_trajectory:
            break
        continue

    input_dict = dict(turn.inputs)
    if include_history:
        input_dict[self.history_field] = turn.history_snapshot

    ex = dspy.Example(**input_dict, **turn.outputs).with_inputs(*list(input_dict.keys()))
    examples.append(ex)

return examples
```

**[session] Per-request state binding through a contextvar** — `dspy_session/session.py:167-191`. Runs on 3.3.1 (`test_state_binding.py:63-83`, concurrent asyncio).
```python
class _StateBinding:
    """Sync/async context manager for binding external state to a Session."""

    def __init__(self, session: "Session", state: SessionState):
        self._session = session
        self._state = state
        self._token: contextvars.Token | None = None

    def __enter__(self) -> SessionState:
        current = _ACTIVE_SESSION_STATES.get()
        mapping = dict(current) if current is not None else {}
        mapping[id(self._session)] = self._state
        self._token = _ACTIVE_SESSION_STATES.set(mapping)
        return self._state

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if self._token is not None:
            _ACTIVE_SESSION_STATES.reset(self._token)
            self._token = None

    async def __aenter__(self) -> SessionState:
        return self.__enter__()

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        self.__exit__(exc_type, exc_val, exc_tb)
```

**[session] Episodic consolidation at the root-call boundary** — `dspy_session/session.py:879-905`. Runs on 3.3.1 (`test_with_memory_policies.py:105-140`).
```python
if session.lifespan == "persistent":
    continue

if session.lifespan == "episodic":
    if session.consolidator is not None and state.turns:
        transcript = _serialize_turns(state.turns)
        try:
            pred = session.consolidator(
                past_memory=state.l2_memory,
                episode_transcript=transcript,
            )
            updated = _extract_updated_memory(pred)
            if updated is not None:
                state.l2_memory = str(updated)
        except Exception as e:
            logger.warning(
                "consolidator error on session '%s' (%s): %s",
                session._session_path,
                type(session.module).__name__,
                e,
            )

    state.turns.clear()
    continue

if session.lifespan == "stateless":
    state.turns.clear()
```

**Probe written for this extraction (not in the repo): how to see what history reaches the provider.** Taken from `scratchpad/sessopt/render.py`; runs on 3.3.1.
```python
import dspy
from dspy.utils import DummyLM
from dspy_session import sessionify

lm = DummyLM([{"corrected": "This plant is red."}, {"translated": "Cette plante est rouge."},
              {"corrected": "Can I have it?"}, {"translated": "Puis-je l'avoir ?"}])
dspy.configure(lm=lm)
s = sessionify(CorrectThenTranslate())          # corrector: text->corrected; translator: corrected,target_language->translated
s(text="This plant is red"); s(text="Can I have it?")
for m in lm.history[2]["messages"][1:]:          # corrector, turn 2
    print(m["role"], m["content"])               # -> assistant "[[ ## corrected ## ]]\nNone" for the prior turn
```

**[optimizer] Offline LM on the legacy contract** — `tests/conftest.py:9-53`. Runs unmodified on 3.3.1 (43/43 tests with mlflow). Set `forward_contract = "legacy"` explicitly, and use ChatAdapter-formatted `response_text` to avoid the hidden JSON fallback call.
```python
class MockLLM(dspy.BaseLM):
    def __init__(self, response_text: str = "mocked response"):
        super().__init__(model="mock-model")
        self.response_text = response_text

    def forward(self, prompt=None, messages=None, **kwargs):
        mock_choice = SimpleNamespace(
            message=SimpleNamespace(content=self.response_text, tool_calls=None),
            logprobs=None,
        )
        mock_response = SimpleNamespace(
            choices=[mock_choice],
            usage={"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0},
            model=self.model,
        )
        setattr(mock_response, "_hidden_params", {"response_cost": 0.0})
        return mock_response

# test usage (tests/dspy_optimizer/test_evaluator.py:41-47): assert on what was sent
#   last_messages = mock_llm.history[-1]["messages"]
#   system_prompt = next((m["content"] for m in last_messages if m["role"] == "system"), "")
#   assert test_prompt in system_prompt
```

**[optimizer] Per-call instructions without shared mutation** — `dspy_optimizer/evaluator.py:22-43`. Runs on 3.3.1 (`test_evaluator.py`).
```python
def forward(self, prompt: str, **kwargs) -> dspy.Prediction:
    # Use the official, immutable API to create a new signature with the
    # desired instructions. This is thread-safe and robust.
    dynamic_signature = self._base_signature.with_instructions(prompt)

    # Instantiate a predictor with the new, temporary signature.
    predictor = dspy.ChainOfThought(dynamic_signature)

    return predictor(**kwargs)
```

**[optimizer] Deterministic block patch** — `dspy_optimizer/strategies/merger/block_based.py:31-59`. Runs on 3.3.1 (`test_block_based.py`). Add `re.IGNORECASE` or exact-header matching, and select the target from the existing headers.
```python
block_start_regex = re.compile(f"^{re.escape(patch.target_block)}.*$", re.MULTILINE)
match = block_start_regex.search(base_prompt)

if not match:
    raise ValueError(f"Target block '{patch.target_block}' not found in prompt.")

start_pos = match.end()

# Find the end of the block (next block header or end of string)
next_block_regex = re.compile(r"^###\s", re.MULTILINE)
next_match = next_block_regex.search(base_prompt, start_pos)
end_pos = next_match.start() if next_match else len(base_prompt)

if patch.operation == PatchOperation.APPEND:
    new_prompt = (
        base_prompt[:end_pos].rstrip() + "\n" + patch.content + "\n" + base_prompt[end_pos:]
    )
elif patch.operation == PatchOperation.REPLACE:
    new_prompt = (
        base_prompt[:start_pos] + "\n" + patch.content + "\n" + base_prompt[end_pos:]
    )
else:
    # This should be unreachable if PatchOperation is used correctly
    raise ValueError(f"Unsupported operation: {patch.operation}")

return new_prompt.strip()
```

**[optimizer] Registry** — `dspy_optimizer/strategies/registry.py:6-28`. Pure Python; runs anywhere.
```python
class Registry:
    """A registry for storing and retrieving classes by name."""

    def __init__(self, name: str):
        self._name = name
        self._registry: dict[str, type] = {}

    def register(self, name: str) -> Callable:
        """A decorator to register a class."""

        def decorator(cls: type) -> type:
            if name in self._registry:
                raise ValueError(f"'{name}' is already registered in '{self._name}'.")
            self._registry[name] = cls
            return cls

        return decorator

    def get(self, name: str) -> type:
        """Get a class from the registry by name."""
        if name not in self._registry:
            raise KeyError(f"'{name}' not found in '{self._name}' registry.")
        return self._registry[name]
```

**[optimizer] Negative example: a guard that passes on nothing** — `dspy_optimizer/strategies/validation/sample.py:60-74`. Runs on 3.3.1 and returns `{"is_valid": True, "score": 1.0}` for `[]`.
```python
if len(dataset) < self.sample_size:
    sample_set = dataset
else:
    sample_set = random.sample(dataset, self.sample_size)

if not sample_set:
    return {"is_valid": True, "score": 1.0}  # Vacuously true

score = sum(
    scorer(example, evaluator(prompt=candidate_prompt, **example.inputs()))
    for example in sample_set
) / len(sample_set)

is_valid = score >= self.threshold
return {"is_valid": is_valid, "score": score}
```

**[optimizer] Negative and positive: parsing a Dutch number.** The shipped scorer, `dspy_optimizer/strategies/scoring/common.py:77-84`, is broken on decimal commas (verified). The deleted predecessor, `git show 19fb8d2^:dspy_optimizer/invoice_amount_optimizer.py:183-194`, is correct but was never run here (reading only).
```python
# shipped (broken): "80,50" -> 8050.0
def parse_numeric(value: Any) -> float:
    s = str(value).strip()
    s = s.replace(",", "")
    s = s.replace(",", ".")   # dead: no commas left
    return float(s)

# predecessor (handles '€ 1.234,56' -> 1234.56)
def parse_float(value: str) -> float:
    value = re.sub(r"[^\d,.-]", "", value)
    if value.count(",") == 1 and value.count(".") > 0:
        value = value.replace(".", "").replace(",", ".")
    elif value.count(",") == 1 and value.count(".") == 0:
        value = value.replace(",", ".")
    return float(value)
```

---

## 4. The old report, corrected

### `Plan/concept/dspy-repos_2026-09-23/dspy-session.md`

- **§1 says „a live LM run with a real API key baked into old output blocks"** — Wrong. No key is anywhere in the repo (grep for `sk-`, `gsk_`, `API_KEY`, `api_key=` finds nothing), and the report's own §4 concedes „There is no `.env`/key visible". The docs contain model strings and LM outputs only.
- **§1: dependency line numbers** — `dspy>=2.6` is at `pyproject.toml:28` (not :16), Alpha at `:17` (not :13), and `requires-python` at `:11` (not :9).
- **§2 item 1: „immutable afterward"** — Wrong. `Turn` is a plain `@dataclass`, which is mutable (`session.py:61`), and `score()` writes into it. The snapshot is not copied: under `use_if_provided` it is the caller's object. `Session.save`/`load_from` does not persist snapshots at all but rebuilds them with the loading config (`session.py:1203-1211,1253-1263`), so a `use_if_provided` snapshot is lost (verified).
- **§2 item 5** — The cited list-mutation test (`test_session.py:1256-1273`) exercises `add_turn`, not a recorded call; the call-path test is `1275-1293`.
- **§2 items 6-7: `override` as the optimizer path** — Incomplete in a way that matters. Under `BootstrapFewShot.compile(session)` the replays run the *original* predictor through the closure, trace steps are dropped by `bootstrap.py:230-231` (`except KeyError: continue  # FIXME: !`), and the compiled session has 0 demos (verified). `override` also does not protect child ledgers in `with_memory` apps (verified).
- **§2 item 8** — The annotation auto-detection accepts `Optional[History]` and subclasses, which DSPy's adapter does *not* treat as history (`adapters/base.py:604-608`); the result is inline JSON (verified). It is not simply more robust.
- **§2 item 10: `fork()` with an independent module copy** — Wrong in effect. The fork's module is a copy, but its calls go to the original predictor: demos set on the original appear in the fork's prompt, and demos set on the copy never do (verified).
- **§2 item 13** — The arity probe is a real metric call with an empty Example and Prediction (an extra LM call for judges), and a TypeError raised inside the metric is misread as an arity problem. Also missed: with `gold=None` the example's labels are the turn's own outputs, so label metrics score 1.0 trivially (verified).
- **§2 item 17: mlflow logs `turn_score`** — `mlflow_turn_logger` can never log `turn_score` (the score is None at hook time), and the committed `mlflow.db` shows only `history_length` and `total_turns` for run `2898734f…`. The db also holds 3 FAILED runs. The old scan read the artifacts but not the db.
- **§2 item 19: helpers „duplicated verbatim"** — Not verbatim: the MLflow copy lacks the `toDict()` branch.
- **§2 items 21-22: the README cannot silently drift because its patterns are tested** — Overstated. The tests fake `forward`, so rendering is never exercised. README Examples 1-2 „work" while sending `None` as prior answers for string-returning programs (verified). README Example 4's compile yields 0 demos (verified), and README.md is two concatenated copies (1-1048, 1049-1990).
- **§2 item 24 / §6 verdict on RLM** — The quoted failure is specific to DSPy **3.1.3**: no `BaseModel` branch in `_serialize_value`, and extra inputs tolerated. On **3.3.1**, `sessionify(dspy.RLM(...))` fails immediately with `ValueError: Unexpected inputs not declared in the signature: ['history']`, and `History` values *are* serialisable into the sandbox. The risk is „do not wrap RLM in a History injector". Plain `dspy.RLM` is unaffected. Also missed: the transcript is a textbook case of an extract-fallback answer that looks normal (`final_reasoning='Extract forced final output'`).
- **Not seen at all** —
  - the design-doc wire-format analysis (Strategies 1-5) and the fact that plain `sessionify` on composed programs *is* the failing Strategy 2;
  - „Push, Don't Peek" and the broken Approach 2 example;
  - `max_turns` counting seed messages, and `max_turns=0` meaning unlimited;
  - `copy_mode="none"` mutating the caller's module;
  - child ledgers lost when saving unbound `with_memory` apps;
  - contextvars not reaching `dspy.Parallel` workers;
  - locks serialising all users of a blueprint;
  - `Session.save` shadowing `dspy.Module.save`, and predictor names changing under wrapping;
  - ReAct under a session (the loop predictor sees `None` actions);
  - the draft v2 API (`SessionContainer`, `CallRecord`, `nested_sessions`) being unimplemented and `sessionify(recursive=…)` raising TypeError;
  - duplicated docs, `docs/multiple-signatures.md` using a non-existent `append_history`, and `rationale` vs `reasoning`.
- **Confirmed** — 102 passed and 1 skipped offline (now on DSPy 3.3.1 and Python 3.12). `on_turn` is swallowed with a warning. Versioned state rejects unknown versions. There is no token or cost logging anywhere.

### `Plan/concept/dspy-repos_2026-09-23/dspy-optimizer.md`

- **§1: „43 unit/integration tests, all against a hand-rolled MockLLM"** — Many use fakes, monkeypatching or MagicMock instead. Without mlflow installed, 5 tests *fail* (`AssertionError` at `mlflow_callback.py:56`); with mlflow 3.16.1 all 43 pass. The numpy RecursionError reported with mlflow was not reproduced (mlflow 3.16.1, numpy 2.5.3, Python 3.12).
- **§2 item 13: the numeric scorer normalises European formats** — Wrong. `common.py:80` removes every comma, which makes line 83 dead: `"80,50"` → 8050.0 and `"1.234,56"` → False. Only US format parses. The deleted predecessor's `parse_float` was correct (verified).
- **§2 item 12: scorers never raise** — Wrong for Examples without `with_inputs`, which raise `ValueError` (verified).
- **§4 item 1: vacuous validators** — `FullValidationStrategy` also returns True on an empty dataset, which the report missed; all three were verified.
- **§2 item 9: `full` against a separate validation set** — There is no separate set. The optimizer validates against the same `dataset` it optimizes (`optimizer.py:152-158`), contrary to `DESIGN.md:33,48`.
- **§2 item 15: failure history** — The history labels use the example index (`Failed Attempt {i + 1}`), not the attempt number (verified).
- **§2 item 17: callbacks with a full lifecycle** — `on_refinement_end` is skipped on success, `total_evaluations` undercounts (5 counted against 8 real calls), callbacks cannot stop the run, and `on_validation_success` (DESIGN) does not exist (verified).
- **§2 items 19-20: MLflow logs `validation_score` and a patch** — Wrong under the real loop. The callback reads keys the loop never writes, so it logs empty params, `is_valid` only, patch op/target and text, and no score, prompt or model. The unit tests pass only because they hand-build matching dicts (verified with MagicMock). `mlflow` is also a *hard* dependency (`pyproject.toml:13`), not optional.
- **§2 item 21: MockLLM verified on 3.3.1** — True. But the tests' JSON `response_text` goes through ChatAdapter's JSON fallback: 2 LM calls per predictor call, and the prompt assertions inspect the fallback call. The default text raises `AdapterParseError`. In 3.3.1 `_hidden_params` is optional while `.model` is required.
- **§2 item 3: `with_instructions` is the thing to adopt** — Also note that the per-call `ChainOfThought` leaves `Evaluator.named_predictors() == []`, so DSPy optimizers, save/load and demos cannot reach it.
- **Not seen** —
  - model-typed identifiers crash the run: `PatchOperation("Append")` and case- or prefix-mismatched block names, uncaught in `optimize()`;
  - `Config.temperature`/`parallel_workers` unused (no parallelism anywhere);
  - strategy parameters not configurable through `PromptOptimizer`;
  - the `amount` field hard-coded in the generic loop;
  - the entry point prints „Hello from dspy-optimizer!";
  - an empty `refiner.py` shadowed by the package;
  - README API names (`GenericPromptOptimiser`, `optimise`) that do not exist;
  - `SampleValidationStrategy` undocumented and `SingleExampleValidationStrategy` listed as roadmap;
  - the flagship's real history: `examples/` never existed in any of the 25 commits, but a 380-line `invoice_amount_optimizer.py` (LLM prompt merger, `ThreadPoolExecutor` evaluation, correct Dutch parser, Azure LM from `.env`) was deleted in `19fb8d2`.
- **Line numbers** — `uv.lock:745` is `name = "dspy"` and `:746` is `version = "2.6.27"` (the report cited 745 and 772).

---

## 5. Ten things the skill must say

1. A Session-wrapped predictor keeps calling the **original** object after `deepcopy`, `fork()` or any optimizer copy, so `BootstrapFewShot.compile(session)` yields 0 demos while printing „Bootstrapped N full traces". Optimize an unwrapped module (with a `history: dspy.History` field) and `update_module()` it (OPT: copies run the original predictor / the path that works).
2. Plain `sessionify` on a composed program feeds root history into every nested predictor: unmatched outputs render as `None`, and unmatched inputs vanish together with their user turn. Use per-predictor ledgers (`with_memory`) or pass data through fields (AGENT: Strategy 2 item; `render.py`).
3. DSPy treats an input as conversation history only when `annotation == dspy.History`; `Optional[History]` and subclasses are sent as inline JSON (API: exact-annotation item).
4. Never wrap `dspy.RLM` in a History injector. On 3.1.3 it wastes all 20 iterations on „Unsupported value type: History"; on 3.3.1 it raises „Unexpected inputs" at once. RLM 3.3.1 requires inputs to match its signature exactly (RLM section).
5. An RLM answer can be a fallback: check `final_reasoning == "Extract forced final output"` and the `[Error]` outputs in the trajectory before counting it as answered (RLM: fallback item, P15).
6. Metric plumbing hides failure. `session.score()` probes with an extra real call, self-labels (label metrics score 1.0), and turns errors and `None` into 0.0. The optimizer's `full`/`batched`/`sample` validators accept an empty set (MET; TRAP: validators pass on nothing).
7. An unparseable reply under ChatAdapter silently costs a second call through the JSONAdapter fallback. A mock LM should return ChatAdapter-formatted text, and call counts must be measured at the LM (API: fallback item; TEST: MockLLM item).
8. Any identifier the model types (`operation`, `target_block`) must be a `Literal` built from the artifact by code. Free strings crash or mis-patch the whole run (TRAP: one bad field crashes the run; SKILL: case-sensitive prefix match).
9. Tests that fake `forward`, or hand-build the callback state dict, stay green while rendering and integration are broken. Assert on `lm.history[-1]["messages"]` with a DummyLM or MockLLM (TEST: faked-forward and MLflow-test items).
10. „Push, Don't Peek": data moves between modules only through Input/Output fields, so optimizers can trace causality; memory side channels are for auditors only. The doc's own Approach 2 example shows how easily the wrong node's memory gets read (AGENT: „Push, Don't Peek" and Approach 2 items).
