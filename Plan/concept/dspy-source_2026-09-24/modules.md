# Modules — DSPy 3.3.1

## 1. Header

**Slice**: `dspy/predict/` (all: `__init__.py`, `parameter.py`, `predict.py`,
`chain_of_thought.py`, `react.py`, `react_v2.py`, `rlm.py`, `flex/` [`flex.py`,
`ctx.py`, `bridge.py`, `_sandbox_shim.py`, `primitives_doc.py`, `__init__.py`],
`code_act.py`, `program_of_thought.py`, `refine.py`, `best_of_n.py`,
`parallel.py`, `retry.py`, `avatar/` [`avatar.py`, `models.py`, `signatures.py`,
`__init__.py`], `knn.py`, `aggregation.py`, `multi_chain_comparison.py`) and
`dspy/primitives/{python_interpreter,code_interpreter,repl_types,
sandbox_serializable}.py` — **29 code files, ~5,508 source lines**, read in
full. Tests read in full or by targeted section (test names + key bodies,
given a mid-task token-budget interruption): `tests/predict/*.py` (14 files,
~253K bytes; `test_predict.py`, `test_rlm.py`, `test_react.py` read for
sections/names, `test_refine.py`/`test_best_of_n.py`/`test_parallel.py`/
`test_program_of_thought.py`/`test_code_act.py`/`test_chain_of_thought.py`/
`test_aggregation.py`/`test_knn.py`/`test_multi_chain_comparison.py` skimmed
by name), `tests/flex/*.py` (7 files; `test_flex_gepa.py` read closely,
others by name), `tests/mock_interpreter.py`, `tests/primitives/test_{python_
interpreter,code_interpreter,sandbox_serializable}.py` (names read, bodies
spot-checked), `tests/callback/test_interpreter_callback.py` (not opened —
noted as a gap). Docs: all 14 `docs/docs/api/modules/*.md` except `Module.md`
(excluded by the brief), `docs/docs/api/tools/PythonInterpreter.md`,
`docs/docs/diving-deeper/{built-in-module-variants,react,rlm,flex,tools}.md`
(all 5, full), `docs/docs/learn/programming/{tools,mcp}.md` (grepped for
module-relevant sections rather than read start-to-end). Tutorials: fully —
`dataframe_rlm/` (both `.py` files, notebook cells), `output_refinement/
best-of-n-and-refine.md`; by targeted grep of code cells — `agents`,
`tool_use`, `program_of_thought`, `custom_module`, `conversation_history`,
`customer_service_agent`, `yahoo_finance_react`, `mem0_react_agent`,
`ai_text_game`, `games`, `math`, `sample_code_generation`.

**Verification run**: `.venv-dspy/bin/python` (offline, all `*_API_KEY`
unset) — `inspect.signature` on every class named below; three live
`FixtureLM`/`lm_fixture` probes (the silent temperature bump, `ReAct`'s
`AdapterParseError` not being a `ValueError`, `BestOfN`'s `threshold=None`
crash at N=2 vs N=3); one `Refine`/`OSError`-on-unretrievable-source
construction probe; one `Refine(threshold=None)` probe; `hasattr(dspy, …)`
checks for `Avatar`/`TypedPredictor`/`LocalSandbox`; `grep -n` for every
cited line number.

**What this slice is**: the module layer — everything that turns a signature
into a callable strategy for producing its outputs, from the one-call
`Predict` up through agent loops (`ReAct`/`ReActV2`), code-executing modules
(`ProgramOfThought`, `CodeAct`, `RLM`), the optimizable-source module
(`Flex`), and the sampling/comparison/parallel wrappers around any of them
(`Refine`, `BestOfN`, `MultiChainComparison`, `Parallel`, `majority`). The
`primitives/` files in scope are the sandbox underneath four of these
(`RLM`, `ProgramOfThought`, `CodeAct`, `Flex`): a Deno/Pyodide WASM
interpreter, its abstract protocol, the REPL history/variable types, and
`SandboxSerializable`, an extension point for non-string inputs.

## 2. Knowledge items

### API

- **`Predict.__call__` refuses positional args** — `if args: raise
  ValueError("Positional arguments are not allowed when calling
  \`dspy.Predict\`, must use keyword arguments that match your signature
  input fields: '<fields>'. For example: \`predict(<f0>=input_value, …)\`.")`
  on both `__call__` and `acall`. `dspy:predict/predict.py:130-140` [api]
  (verified: read) · skill: new.
- **Silent temperature bump to 0.7** — `Predict._forward_preprocess`: if
  `(config.get("temperature") or lm.kwargs.get("temperature"))` is `None`
  or `<= 0.15`, **and** `n > 1` (from `config["n"]`, `lm.kwargs["n"]` or
  `lm.kwargs["num_generations"]`, default 1), `config["temperature"]` is set
  to `0.7` — with no warning, no log line.
  `dspy:predict/predict.py:168-173` [trap] (verified: ran — `dspy.Predict("q
  -> answer")(q="hi", config={"n": 3})` against a `FixtureLM` sent
  `{"temperature": 0.7, "n": 3}` although neither the LM nor the call set a
  temperature) · skill: new.
- **Extra input fields, type mismatches, and missing required inputs are
  all `logger.warning`, never an error, on plain `Predict`** — an unknown
  kwarg is dropped with "Input contains fields not in signature. These
  fields will be ignored: …"; a value whose runtime type doesn't match the
  declared annotation (checked by a hand-rolled `_check_type` supporting
  Union/Literal/list/dict/tuple/set, gated by `settings.warn_on_type_mismatch`,
  default `True`) logs "Type mismatch for field '%s': …"; a required field
  the caller never supplied logs "Not all input fields were provided to
  module. Present: …. Missing: …" — the call still runs. `dspy:predict/
  predict.py:191-231` [trap] (verified: read; the three DSPy tests
  `test_extra_fields_warning`, `test_missing_optional_input_field_no_warning`,
  `test_missing_required_input_field_still_warns` in
  `tests/predict/test_predict.py:1093-1139` exercise exactly this) · skill:
  new. **Contrast**: `dspy.RLM._validate_inputs` is strict — `ValueError`
  on an unexpected or a missing input (rlm.md already documents this for
  RLM); plain `Predict`'s permissiveness is the opposite end of the same
  design axis and isn't in the skill at all.
- **`dspy.ChainOfThought` takes a fourth parameter the skill's surface line
  omits**: `rationale_field_type: type = str` — ignored when
  `rationale_field` is given. `dspy:predict/chain_of_thought.py:36-42`,
  confirmed by `inspect.signature` [api] (verified: ran) · skill: wrong:
  `api.md` line 45 says `dspy.ChainOfThought(signature, rationale_field=None)`.
- **The `reasoning` field is `prepend`ed, placed before every declared
  output** — `signature.prepend(name="reasoning", field=rationale_field,
  type_=rationale_field_type)`, default `desc="${reasoning}"`.
  `dspy:predict/chain_of_thought.py:44-49` [api] (verified: read) · skill:
  same (`api.md`'s module table already says this).
- **`dspy.majority`'s default field is the LAST output field**, not the
  first: `field = list(signature.output_fields.keys())[-1]` when no
  `field=` is given and a signature is available. A completion whose
  normalized value is `None` (post `default_normalize`) is excluded from
  the vote unless *every* completion normalizes to `None`. Ties go to the
  earliest completion in iteration order (`max(value_counts, key=…)` over
  a dict built in completion order). Returns
  `Prediction.from_completions([completion], signature=signature)` — one
  winning completion, never a synthesized merge.
  `dspy:predict/aggregation.py:9-54` [api] (verified: read) · skill: same
  (already summarized in `api.md`'s Modules table, mechanism now precise).
- **`dspy.KNN` is not a `Module`** — a plain class, `__call__` not
  `forward`, not traceable/compileable. Ranks by **raw dot product**, not
  cosine similarity — no normalization of either the trainset or the query
  embedding (`np.dot(self.trainset_vectors, input_example_vector.T)`), so a
  non-unit-norm embedder biases results toward larger-magnitude vectors.
  Embeds only the `_input_keys` of each training `Example`, joined
  `"key: value"`. `dspy:predict/knn.py:8-53` [api|trap] (verified: read) ·
  skill: new.
- **`dspy.MultiChainComparison` is not called with plain input fields** —
  `forward(completions, **kwargs)` expects `completions` to be an iterable
  of exactly `M` dict-likes (typically `dspy.Predict(sig, n=M)(...).completions`),
  each with a `"rationale"` (falls back to `"reasoning"`) and the ORIGINAL
  signature's last output field, captured as `self.last_key` *before* `M`
  `reasoning_attempt_i` input fields are appended and a `rationale` output
  field is prepended. Both the rationale and the answer are silently
  truncated to their **first line** (`.split("\n")[0]`) when building the
  `«I'm trying to … I'm not sure but my prediction is …»` attempt string.
  `len(attempts) != M` raises `AssertionError` naming both numbers.
  `dspy:predict/multi_chain_comparison.py:7-53` [api|trap] (verified: read)
  · skill: new.
- **`dspy.predict.retry`'s entire file body is commented out** — no `Retry`
  class, nothing importable; `dspy.predict.__init__` does not import it.
  Confirms and extends the skill's existing "`dspy.Assert`, `dspy.Suggest` —
  gone; `dspy.Refine` replaced them": the backtracking machinery that
  supported them (`dspy.settings.backtrack_to`) is not merely unreferenced,
  it is fully disabled in-file. `dspy:predict/retry.py:1-75` [trap]
  (verified: read) · skill: new.
- **`dspy.Parallel` is not a `Module` subclass** — `class Parallel:` with
  no base at all (confirmed: `Parallel.__bases__ == (object,)`); no
  `predictors()`, no callbacks, invisible to every optimizer and to
  `dump_state`. `__call__` is exactly `forward`. Dispatches each
  `(module, example)` pair by the example's TYPE: `Example` (unpacked via
  `.inputs()` iff `access_examples=True`, default `True`; else passed
  **positionally**, `module(example)`), `dict` (`module(**example)`),
  `list` (passed positionally, only when
  `module.__class__.__name__ == "Parallel"` — a string comparison, not
  `isinstance`), `tuple` (unpacked positionally, `module(*example)`); any
  other type raises `ValueError("Invalid example type: …")`.
  `return_failed_examples=True` changes the return shape from `results` to
  a 3-tuple `(results, failed_examples, exceptions)`.
  `dspy:predict/parallel.py:9-127` [api|trap] (verified: read) · skill:
  same for the `(module, dict)`/`(module, Example)` pairing already in
  `api.md`; new for the positional-tuple/positional-Example/nested-list
  branches and the `Predict.__call__`-refuses-positional interaction (a
  `Predict`/`ChainOfThought` module paired with `access_examples=False` or
  a tuple example fails every pair with `ValueError`, caught per-pair by
  `ParallelExecutor`, not re-raised to the caller).
- **`dspy.Avatar` (the module, `dspy.predict.avatar.avatar.Avatar`) is
  dead code on 3.3.1, and it is not exported anywhere at the top level.**
  `hasattr(dspy, "Avatar")` is `False` — reachable only via `from
  dspy.predict.avatar.avatar import Avatar`. Its `__init__` calls
  `dspy.TypedPredictor(self.actor_signature)`
  (`dspy:predict/avatar/avatar.py:52`), and `dspy.TypedPredictor` does not
  exist on 3.3.1 — construction raises `AttributeError: module 'dspy' has
  no attribute 'TypedPredictor'` unconditionally, before any input is
  processed. `dspy:predict/avatar/avatar.py:22-55` [trap] (verified: ran —
  `Avatar(signature="question -> answer", tools=[Tool(tool=noop, name="echo",
  desc="…")])` raises that `AttributeError`) · skill: new — extends
  `api.md`'s existing `AvatarOptimizer`-unconstructible trap ("Its surface
  line above still holds, because the signature is intact; a signature that
  exists is not a class that works") one level further: the *module itself*
  that `AvatarOptimizer` is meant to optimize is equally unconstructible,
  and isn't even public.
- **Deprecation, in force on 3.3.1, not 3.5**: `dspy.ProgramOfThought` and
  `dspy.CodeAct` both carry `.. deprecated:: 3.4` docstrings and fire a real
  `warnings.warn(…, DeprecationWarning, stacklevel=2)` on **every
  construction**: "ProgramOfThought is deprecated and will be removed in
  3.5. RLM is the preferred replacement." / "CodeAct is deprecated and
  will be removed in DSPy 3.5. RLM is the preferred replacement."
  `dspy:predict/program_of_thought.py:26-29,58-62`,
  `dspy:predict/code_act.py:17-20,53-57`; confirmed a second way by
  `docs/docs/api/modules/{ProgramOfThought,CodeAct}.md`'s own top-of-page
  `!!! warning "Deprecated"` callouts [api|trap] (verified: read, both
  code and docs) · skill: new — `api.md`'s module table lists both with no
  deprecation note at all ("`ProgramOfThought`, `CodeAct` | the model
  writes code, a sandbox runs it (Deno) | nothing").
- **`dspy.ReActV2` will become `dspy.ReAct` in DSPy 3.5.** "DSPy is
  transitioning between two implementations. `dspy.ReAct` is the current
  implementation. `dspy.ReActV2` is its experimental, structured-history
  replacement and will become the implementation behind the canonical
  `dspy.ReAct` name in DSPy 3.5. The `dspy.ReActV2` name will remain as a
  deprecated compatibility alias throughout the 3.5 release line and will
  be removed in DSPy 3.6." `docs/docs/diving-deeper/react.md:7,184-190`,
  echoed in `docs/docs/api/modules/ReActV2.md:3` [claim] (verified: read;
  this is a documentation-only claim about a future release, not something
  3.3.1's code can itself prove) · skill: new, top priority — this makes
  every ReAct-vs-ReActV2 behavioral difference below a forward-looking
  breaking-change list, not merely a stable-vs-experimental comparison.
- **`dspy.ReAct`'s own docstring states the wrong default.** "max_iters
  (Optional[int]): The maximum number of iterations to run. Defaults to
  10." — the real default, both in the signature and confirmed by
  `inspect.signature`, is `20`. `dspy:predict/react.py:17,28` [trap]
  (verified: read + `inspect.signature`) · skill: new.
- **`ReAct.forward`'s `except ValueError` cannot catch the failure it is
  written for.** The loop wraps each `self._call_with_potential_trajectory_
  truncation(self.react, …)` call in `except ContextWindowExceededError: …
  break` / `except ValueError: … "Agent failed to select a valid tool" …
  break` (`dspy:predict/react.py:98-106`). An out-of-`Literal` or otherwise
  unparseable `next_tool_name`/`next_tool_args` answer raises
  `dspy.AdapterParseError`, which extends `DSPyError(Exception)` directly
  — **not** `ValueError` (`dspy:utils/exceptions.py:9,246`). The except
  clause does not catch it; it propagates uncaught out of `forward()`.
  [trap] (verified: ran offline against a `FixtureLM` scripting an
  out-of-set `next_tool_name`; two LM calls — `ChatAdapter` then its
  `JSONAdapter` fallback — then `AdapterParseError: Adapter JSONAdapter
  failed to parse the LM response…` propagated out of `agent(question=…)`,
  not the "Ending the trajectory" log path) · skill: new, high value —
  **corroborated inside DSPy's own source**: `ReActV2`'s equivalent except
  clause explicitly lists both: `except (AdapterParseError, ValueError) as
  err:` (`dspy:predict/react_v2.py:14,102`) — ReActV2's own author closed
  exactly this gap.
- **`ReAct`'s built-in `"finish"` tool silently overwrites a same-named
  user tool.** `tools = {tool.name: tool for tool in tools}` then
  `tools["finish"] = Tool(func=lambda: "Completed.", …)` — plain dict
  assignment, no collision check, no warning.
  `dspy:predict/react.py:44,62-67` [trap] (verified: read) · skill: new.
  **Contrast**: `ReActV2` raises at construction instead —
  `if "submit" in self.tools: raise ValueError("\`submit\` is reserved by
  ReActV2 as the final-output tool.")` (`dspy:predict/react_v2.py:31-32`).
- **`CodeInterpreterError(DSPyError, RuntimeError)` — dual inheritance,
  unlike the LM/adapter error hierarchy.** `except RuntimeError:` DOES
  catch `CodeInterpreterError`/`CodeExecutionError`; it does NOT catch
  `AdapterParseError`/any `LMError` (those extend only `DSPyError(Exception)`,
  no builtin base). `dspy:primitives/code_interpreter.py:18-29`,
  `dspy:utils/exceptions.py:9,50,246` [api|trap] (verified: read) · skill:
  new — a genuine, exploitable inconsistency for anyone writing one
  exception handler for both DSPy's LM-calling and its sandboxed modules.
- **`CodeInterpreterError` vs `CodeExecutionError` is a stated two-tier
  design, not an accident**: a bare `CodeInterpreterError` means "a failure
  that submitted code cannot repair… host-side setup or a process/protocol
  failure… Implementations should make process/protocol failures terminal
  for that interpreter session"; `CodeExecutionError(CodeInterpreterError)`
  is "Recoverable error raised by code running in a healthy interpreter."
  `dspy:primitives/code_interpreter.py:18-29` [api] (verified: read) ·
  skill: new — this is the design rule behind `rlm.py`'s/`program_of_
  thought.py`'s `except (CodeExecutionError, SyntaxError)` catches, which
  the skill already cites without the stated rationale.
- **`_validate_interpreter_factory`/`_create_interpreter`/`_validate_
  interpreter` are shared, one implementation, by all four sandboxed
  modules** (`RLM`, `ProgramOfThought`, `CodeAct`, `Flex`, all call them at
  construction and again on every `forward()`): passing an already-built
  interpreter INSTANCE where a factory is expected raises `TypeError(
  "interpreter_factory received an object that already implements
  CodeInterpreter, so its ownership is ambiguous. Pass an existing
  interpreter as the first positional argument when calling the module.
  If this object also creates interpreters, pass a dedicated zero-argument
  creation callable instead.")`; a non-callable factory raises `TypeError(
  "interpreter_factory must be a zero-argument callable…")`; a factory
  whose return value isn't a `CodeInterpreter` raises `TypeError(
  "interpreter_factory must return a CodeInterpreter, not {type}.")`.
  `dspy:primitives/code_interpreter.py:150-179` [api] (verified: read) ·
  skill: new — the concrete mechanism behind the skill's already-known
  "positional-only interpreter" and "DSPy shuts down every interpreter it
  creates" claims, one shared function instead of four separate behaviors.
- **`dspy.Flex`'s real constructor is keyword-only after `signature`**:
  `dspy.Flex(self, signature, *, tools=None, interpreter_factory=
  PythonInterpreter, max_predictor_calls=100)`, confirmed by `inspect.
  signature` and by the official docs' own "API walkthrough". `dspy:
  predict/flex/flex.py:45-52` [api] (verified: ran) · skill: new —
  `api.md`'s surface line `dspy.Flex(signature, interpreter_factory,
  tools=None, max_predictor_calls=100)` shows neither the `*,` nor the real
  order (`tools` before `interpreter_factory`).
- **`RLM`'s and `ProgramOfThought`'s/`CodeAct`'s own surface lines in
  `api.md` place `interpreter_factory` earlier than `inspect.signature`
  shows it.** Real order, `inspect.signature`-confirmed: `dspy.RLM(signature,
  max_iters=20, max_llm_calls=50, max_output_chars=10000, verbose=False,
  tools=None, sub_lm=None, interpreter_factory=PythonInterpreter)` —
  `interpreter_factory` is LAST, not second; `dspy.ProgramOfThought(
  signature, max_iters=3, interpreter_factory=PythonInterpreter)` —
  `interpreter_factory` is third, not second; `dspy.CodeAct(signature,
  tools, max_iters=5, interpreter_factory=PythonInterpreter)` —
  `interpreter_factory` is fourth, not third. `api.md`'s lines write
  `interpreter_factory` right after `signature`/`tools` in all three cases.
  [api|trap] (verified: ran `inspect.signature` on all three) · skill:
  wrong (order) — calling any of the three **positionally** with a second
  argument intending it as `interpreter_factory` (as the skill's own
  surface-line order would suggest) actually binds to `max_iters` (RLM,
  ProgramOfThought) or nothing useful — a real, not merely cosmetic, risk
  for anyone reading the surface block as call-order truth.
- **`PythonInterpreter`'s surface line in `api.md` omits two real
  parameters**: `output_fields: list[dict] | None = None` and `callbacks:
  list[BaseCallback] | None = None`. `dspy:primitives/python_interpreter.
  py:243-254`, confirmed by `inspect.signature` [api] (verified: ran) ·
  skill: wrong (incomplete).

### RLM

*(dspy.RLM completely — every constructor parameter and default, the REPL
loop, `max_iters`/`max_llm_calls`/`sub_lm`, tools, the forced final output,
what the trajectory holds, Deno and the sandbox, the interpreter's security
limits, how RLM is optimized. Most of this is already precisely documented
in `.agents/skills/dspy/references/rlm.md`; only what is missing or
sharpenable is written out below — cite `rlm.md` for everything marked
"same".)*

- **`dspy.RLM` exposes its two predictors through the normal
  `named_predictors()` walk — `RLM` does NOT override it — unlike
  `dspy.Flex`, which does.** `self.generate_action = dspy.Predict(action_
  sig)`, `self.extract = dspy.Predict(extract_sig)`
  (`dspy:predict/rlm.py:181-182`); no `named_predictors` override anywhere
  in `rlm.py` (grep-confirmed). This is the precise, DSPy-level answer to
  "how RLM is optimized": through its two ordinary `Predict` components,
  using the same machinery as any other module — **any** standard
  optimizer that walks `named_predictors()` (not only GEPA) can bootstrap
  demos or tune instructions on `generate_action`/`extract`. Confirmed
  independently, twice, in the official docs: "The action and extract
  steps are ordinary `dspy.Predict` instances; `dspy.RLM` exposes them
  through `named_predictors` and compiles like any module… Running GEPA
  or MIPROv2 against a metric improves the loop's behavior, not just the
  task instructions." (`docs/docs/diving-deeper/rlm.md`, design decision
  #10, and `built-in-module-variants.md` #10). [api] (verified: read code
  + two docs) · skill: new — `rlm.md`'s "Not taken, or waiting" table only
  says "an RLM has exactly two predictors, `generate_action` and `extract`"
  without stating that this makes RLM optimizable through ordinary
  optimizer machinery, unlike Flex.
- **`generate_action`'s signature is structurally decoupled from the
  task's own declared fields — architecturally different from every other
  module in this slice.** `action_sig = dspy.Signature({}, task_instructions
  + ACTION_INSTRUCTIONS_TEMPLATE.format(…) + tool_docs)` starts from an
  EMPTY fields dict; the task's real input/output field NAMES appear only
  as interpolated prose in the instructions text
  (`inputs_str`/`output_fields`, from `self.signature.input_fields`/
  `output_fields`). The only typed fields `action_sig` ever declares are
  RLM-internal: `variables_info: str`, `repl_history: REPLHistory` (a real
  pydantic type, not `str`), `iteration: str`, output `reasoning: str`,
  output `code: str`. `dspy:predict/rlm.py:336-369` [api] (verified: read)
  · skill: new. Every other module here (`Predict`, `ChainOfThought`,
  `ReAct`, `CodeAct`, `ProgramOfThought`, `MultiChainComparison`, `Avatar`)
  embeds the task's own declared fields directly as typed signature
  fields; RLM's outer reasoning step never does — the task's real shape
  reaches the model as prose and reaches the sandbox as an enforced, typed
  `SUBMIT(...)` function. RLM enforces the output contract at the *code*
  layer, never the LM-parsing layer.
- **`execution_instructions` (the `PythonInterpreter` class attribute)
  reaches the model's system prompt through a confirmed, one-line
  mechanism**: `execution_instructions = getattr(self._interpreter_factory,
  "execution_instructions", "")`, read as a CLASS-level attribute (works
  without instantiating), guarded by `if not isinstance(execution_
  instructions, str): raise TypeError("interpreter_factory.execution_
  instructions must be a string")`, folded into `action_sig`'s
  instructions as `f"\nExecution environment:\n{execution_instructions}\n"`.
  `dspy:predict/rlm.py:354-357` [api] (verified: read; independently
  confirmed by `docs/docs/api/tools/PythonInterpreter.md:26-33`: "`RLM`
  includes these instructions in its action prompt, which adapters render
  in the model's system prompt… Custom interpreter factories may expose
  their own `execution_instructions` string. This metadata is optional; a
  factory without it remains valid and uses RLM's generic action prompt.")
  · skill: new. `PythonInterpreter.execution_instructions`'s literal text:
  "Python runs in Pyodide/WebAssembly. State persists across executions,
  but subprocesses and native extensions are unavailable. Python standard
  libraries such as re, json, collections, and math are available. Host
  filesystem, environment, and network access require explicit permission."
  `dspy:primitives/python_interpreter.py:346-350`.
- **`dspy.RLM.aforward()` exists — full async support, not mentioned in
  the skill at all.** `async def aforward(self, interpreter=None, /,
  **input_args) -> Prediction`, backed by `_aextract_fallback`/
  `_aexecute_iteration` (`await self.generate_action.acall(...)`),
  mirroring the sync path exactly including the positional-only
  `interpreter` parameter. `dspy:predict/rlm.py:738,759,790` [api]
  (verified: read; `docs/docs/diving-deeper/rlm.md:60-61` confirms:
  "`acall()` is the async twin and uses `acall` on the predictors") ·
  skill: new.
- **`SandboxSerializable` — a major RLM extension point entirely absent
  from `rlm.md`.** Lets a rich, non-string object (a pandas DataFrame, a
  parsed corpus, any binary blob) be used directly as a `dspy.RLM`/
  `dspy.Signature` input, with a custom sandbox-side load, instead of RLM
  only ever seeing plain strings/JSON. `SandboxSerializable(ABC)` requires
  four methods: `sandbox_setup() -> str` (one-time imports, ALSO appended
  into the variable's description so the model learns which names, e.g.
  `pd`, are already bound), `to_sandbox() -> bytes` (the payload),
  `sandbox_assignment(var_name, data_expr) -> str` (code reconstructing
  the value), `rlm_preview(max_chars=500) -> str` (shown instead of the
  default JSON/str preview). Inherits `__get_pydantic_core_schema__` (a
  pass-through, `str()`-serializing schema) so a subclass can be a typed
  Signature field: "RLM owns real serialization via `to_sandbox()` and
  `sandbox_assignment()`." `dspy:primitives/sandbox_serializable.py:41-101`
  [api] (verified: read) · skill: new, high value.
  - **`dspy.RLM` uses this directly**: `_build_variables` calls
    `build_repl_variable(value, name, field_info=field_info)` instead of
    `REPLVariable.from_value` for any `isinstance(value, SandboxSerializable)`
    input (`dspy:predict/rlm.py:408-418`, imports at `rlm.py:42`).
    `_prepare_serializable_vars` runs **once**, right after `repl.start()`,
    **before** the main REPL loop begins: gets `payload = value.to_
    sandbox()`; if the bytes decode as valid UTF-8 they're injected as a
    plain string, else base64-encoded with a prepended `base64.b64decode`
    line; then runs `sandbox_setup()` + `sandbox_assignment(name, raw_var_
    name)` via `repl.execute(code, variables=payload_vars)` — the same
    channel `python_interpreter.py`'s `_inject_variables` uses (subject to
    the same 100 MB threshold below). `dspy:predict/rlm.py:440-478` [rlm]
    (verified: read) · skill: new.
  - **Asymmetry not stated anywhere in the skill**: a plain (non-
    `SandboxSerializable`) input is RE-INJECTED fresh every iteration
    (`rlm.md`'s already-correct "a name the model reassigns… reverts on
    the next iteration"), but a `SandboxSerializable` input's setup+
    assignment code runs exactly ONCE and the resulting sandbox object
    (e.g. a real `pd.DataFrame`) then persists and can be mutated across
    every subsequent iteration like any other sandbox state the model
    creates — it is never silently reset. [rlm] (verified: read
    `_prepare_serializable_vars` vs. `_execute_code`'s per-iteration
    `repl.execute(code, variables=dict(input_args))`) · skill: new.
  - **A complete, official, working example**:
    `docs/docs/tutorials/dataframe_rlm/cohort_analysis/dataframe.py` — a
    `DataFrame(SandboxSerializable)` wrapper for pandas, `sandbox_setup()`
    returns `"import pandas as pd\nimport pyarrow\nimport base64\nimport
    io"`, `to_sandbox()` returns `base64.b64encode(self.data.to_
    parquet(index=False))`, `sandbox_assignment` returns `f"{var_name} =
    pd.read_parquet(io.BytesIO(base64.b64decode({data_expr})))"`,
    `rlm_preview` reports shape + per-column dtype/null-count (first 10
    columns) + a 3-row sample, capped at 500 chars. The demo notebook uses
    THREE separate `DataFrame` input fields in one signature and states in
    its own prose: "The full data is injected once into the sandbox at the
    start of the session" — directly confirming the once-not-per-iteration
    finding above. [pattern] (verified: read) · skill: new.
- **`RLM.tools` is a documented, public property** — returns the
  user-provided tools as a name→`Tool` dict, EXCLUDING the built-in
  `llm_query`/`llm_query_batched`. `dspy:predict/rlm.py:328` (grep-
  confirmed method) [api] (verified: read via grep + `docs/docs/diving-
  deeper/rlm.md:106-107`) · skill: new, small.
- **`llm_query_batched` runs on an 8-worker thread pool, and the shared
  call counter is lock-protected** — `_make_llm_tools(self, max_workers:
  int = 8)` (grep-confirmed signature); `max_llm_calls`'s counter is
  thread-safe by construction, needed because `llm_query_batched` uses a
  `ThreadPoolExecutor`. [rlm] (verified: `docs/docs/diving-deeper/rlm.md:70-71`
  + `tests/predict/test_rlm.py:393-424`, `test_tools_call_counter_is_
  thread_safe`: 10 concurrent `llm_query` calls against `max_llm_calls=10`
  via 5 workers all succeed, an 11th raises `RuntimeError` matching "LLM
  call limit exceeded") · skill: new — `rlm.md` never states the worker
  count or that the counter is a lock.
- **The exact "forgot to print" string**: a code block that computes
  without printing anything returns the literal
  `"(no output - did you forget to print?)"`. `dspy:predict/rlm.py:420-423`
  (`_format_output`) [api] (verified: read; matches `docs/docs/diving-
  deeper/rlm.md:76-77` verbatim) · skill: new, quotable.
- **`"interpreter"` can legally be a real signature input field name.**
  `_validate_inputs`'s special case (`if "interpreter" in input_args and
  "interpreter" not in self.signature.input_fields: raise TypeError(…)`)
  only fires when the caller passes `interpreter=` as a keyword AND the
  signature doesn't declare that field; `RLM("interpreter -> answer",
  …)` works normally and the value becomes an ordinary REPL variable.
  `dspy:predict/rlm.py:427-430` [rlm] (verified: `tests/predict/
  test_rlm.py:472-482`, `test_interpreter_remains_available_as_signature_
  input`, scripts `SUBMIT(interpreter)` against it) · skill: new, a real
  exception to the "positional-only interpreter" rule `rlm.md` states
  unconditionally.
- **Caller-owned interpreter reuse across a sync call *then* an async
  call, verified**: `rlm(interpreter, query="sync")` then `await
  rlm.acall(interpreter, query="async")` on the same interpreter both
  succeed with different scripted answers, `factory.instances == []`
  (the factory is never touched), and the interpreter stays open after
  both (only the caller's own `finally: interpreter.shutdown()` closes
  it). `tests/predict/test_rlm.py:505-526` [rlm] (verified: read test) ·
  skill: same in spirit (`rlm.md` already states caller-owned reuse is
  sequential-only) — new detail that sync and async calls can interleave
  over one reused interpreter.
- **Every interpreter, real or mock, is dead after `shutdown()` in DSPy's
  own test doubles too** — `tests/predict/test_rlm.py:486-503`,
  `test_factory_creates_and_shuts_down_one_interpreter_per_call`: after
  each of a sync and an async call, `interpreter.execute(…)` raises
  `CodeInterpreterError` matching `"shutdown"` — DSPy's own `MockInterpreter`
  deliberately replicates the real sandbox's terminal-session behavior.
  [test] (verified: read) · skill: same (confirms `rlm.md`'s "DSPy shuts
  down every interpreter it creates").

### AGENT

- **ReAct vs. ReActV2 — the full comparison, source of truth
  `docs/docs/diving-deeper/react.md`.** `rlm.md`/`patterns.md` do not
  cover ReActV2 at all beyond one line in `api.md`'s module table
  ("nothing; `ReActV2` is marked experimental"). Condensed, confirmed
  against source where checked:

  | axis | `dspy.ReAct` (3.3.1) | `dspy.ReActV2` (becomes `dspy.ReAct` in 3.5) |
  |---|---|---|
  | stored history | flat `trajectory` dict, 4 keys/turn | structured `dspy.History` events |
  | model-facing history | whole trajectory reformatted into ONE input field, every turn | prior turns replayed as separate messages |
  | tool selection | `next_tool_name: Literal[…]` + `next_tool_args: dict` | `dspy.ToolCalls`, natively typed |
  | calls per model turn | exactly one | one or more |
  | completion | `finish` tool, then a SEPARATE `dspy.ChainOfThought` extraction call | `submit` tool carries final typed outputs directly, no extractor |
  | original task inputs sent | every iteration, unmutated | first turn only, then `{}` |
  | returned diagnostics | `prediction.trajectory` only | `prediction.history` AND `prediction.termination_reason` |
  | forced ending on exhaustion | none — loop just stops, no marker at all | one more call forcing `tool_choice="submit"` (native mode); `termination_reason="forced_submit"` on success, `"failed"`/other on failure |
  | async | full (`aforward`) | none |
  | prompt caching | trajectory resent as one changing field — poor reuse | stable message prefix — provider caching reuses it |

  `docs/docs/diving-deeper/react.md:28-37,86-159` [api|agent] (verified:
  read doc; `pending_inputs = {}` after first turn confirmed at
  `dspy:predict/react_v2.py:121`; no `aforward` in `react_v2.py`,
  grep-confirmed) · skill: new, highest priority.
- **ReActV2's `_forced_submit` can return a `Prediction` with NO output
  fields at all** — if the forced call also fails `(AdapterParseError,
  ValueError, ContextWindowExceededError)`, or returns no `submit` call:
  `return Prediction(history=history, termination_reason=break_reason or
  "failed")` — no signature output fields, not even `None`. A caller
  reading `pred.answer` gets `AttributeError`, not a clean sentinel.
  `dspy:predict/react_v2.py:174-202` [trap] (verified: read; officially
  confirmed — "the prediction still returns its history and a termination
  reason describing why the normal loop stopped, but it may not contain
  the declared output fields," `docs/docs/diving-deeper/react.md:157`) ·
  skill: new — a sneakier failure shape than `Refine`/`BestOfN`'s
  documented `None` return (`[checked: refine-none-when-all-fail]`),
  because the return value here is a real, truthy `Prediction`.
- **Forced-submit reliability depends on native vs. non-native mode, not
  visible from `react_v2.py` alone.** "With native function calling
  enabled, [`_forced_submit`] sets `tool_choice` to `submit`, so the
  provider enforces that choice. In non-native mode, the adapter removes
  `tool_choice` and requests `submit` through the formatted prompt
  instead, so structured submission is not guaranteed."
  `docs/docs/diving-deeper/react.md:157` [claim] (adapter-side code, out
  of this slice) · skill: new — tempers a source-only reading of
  `_forced_submit` (`dspy:predict/react_v2.py:174-187`, which always
  builds the same `tool_choice` config regardless of mode) as reliably
  forcing structured output.
- **`ChatAdapter`/`JSONAdapter`'s different `use_native_function_calling`
  defaults exist because of ReActV2** — with native calling on, a
  completed turn replays as `user(inputs) → assistant(next_thought +
  native tool_calls) → tool(one result message per call, by
  tool_call_id)`; off, the adapter renders the assistant fields in its
  normal text/JSON/XML format and tool results as a following user
  message. `JSONAdapter` enables native calling BY DEFAULT; `ChatAdapter`
  needs it set explicitly (`dspy.ChatAdapter(use_native_function_calling=
  True, parallel_tool_calls=True)`). `docs/docs/diving-deeper/react.md:119-143`
  [claim, ties to `api.md`'s already-known surface defaults] · skill: new
  — connects two previously-separate facts (the adapter defaults, and
  ReActV2's existence) with an explicit reason.
- **`parallel_tool_calls` asks the provider for multiple calls in one
  turn, but ReActV2 executes them sequentially in Python regardless.**
  `_execute_tool_calls`'s plain `for tool_call in tool_calls.tool_calls:`
  loop, no threading/asyncio. `dspy:predict/react_v2.py:128-149` [agent]
  (verified: read; confirmed in prose: "ReActV2 currently executes the
  returned calls one after another in Python,"
  `docs/docs/diving-deeper/react.md:147`) · skill: new.
- **`ReAct`'s truncation retries three times, and its own failure is
  swallowed by the *outer* handler, invisibly.**
  `_call_with_potential_trajectory_truncation` retries up to 3 times on
  `ContextWindowExceededError`, calling `self.truncate_trajectory` each
  time; on a 4th failure it raises a NEW `ContextWindowExceededError`
  ("…even after 3 attempts to truncate the trajectory."). That exception
  propagates one frame up into `forward()`'s own `except
  ContextWindowExceededError: … break`, so **even total, unrecoverable
  context-window failure is silently absorbed** into "stop the loop, call
  `extract` anyway" — the caller never sees it raised, and the returned
  `Prediction` carries no marker that this happened.
  `dspy:predict/react.py:99-106,151-165` [trap] (verified: read) · skill:
  new. `truncate_trajectory` pops the OLDEST 4 keys per call (comment:
  "Every tool call has 4 keys: thought, tool_name, tool_args,
  observation"); raises immediately if `len(keys) <= 4` ("cannot be
  truncated because it only has one tool call"); documented as
  user-overridable.
- **CodeAct's `inspect.getsource(tool.func)` sandbox-injection trap,
  confirmed by DSPy's own official docs with worked examples.**
  `CodeAct.forward` executes each tool's own top-level source text inside
  the sandbox (`interpreter.execute(inspect.getsource(tool.func))`,
  `dspy:predict/code_act.py:128-129`) — NOT the function's enclosing
  module. `docs/docs/api/modules/CodeAct.md`'s "Limitations" section gives
  exactly this failure with runnable examples: "External libraries cannot
  be used" (`def exp(i): return np.exp(i)` fails — the function's own
  source has no `import numpy as np` line, that import lived at module
  scope) and "All dependent functions need to be passed to CodeAct" (a
  tool calling another function/class not itself passed as a tool fails
  the same way; fix: pass every dependency as its own tool). [trap]
  (verified: read code + doc, doubly sourced) · skill: new.
- **CodeAct gives NO marker at all for a forced/timed-out ending — not
  even RLM's `final_reasoning`.** The `for idx in range(max_iters):` loop
  ends either via `code_data.finished == True` (break) or by exhausting
  `max_iters`; either way `extract = self._call_with_potential_trajectory_
  truncation(self.extractor, trajectory, **kwargs)` runs unconditionally,
  and the returned `dspy.Prediction(trajectory=trajectory, **extract)`
  never carries `code_data.finished` or any other exhaustion flag.
  `dspy:predict/code_act.py:112-154` [trap] (verified: read) · skill: new
  — a caller must inspect `trajectory`'s last `finished_{i}`-shaped entry
  themselves; unlike `ReActV2`'s explicit `termination_reason`.
- **`ProgramOfThought`'s failure on exhaustion is a hard `RuntimeError`**
  — the opposite of RLM's graceful forced extraction and CodeAct's silent
  stop: `if hop == self.max_iters: raise RuntimeError(f"Max hops reached.
  Failed to run ProgramOfThought: {error}")`.
  `dspy:predict/program_of_thought.py:217-222` [trap] (verified: read) ·
  skill: new — three sandboxed modules, three different "budget exhausted"
  behaviors (RLM: forced `extract` call, normal-shaped `Prediction`;
  CodeAct: silent stop, no marker; ProgramOfThought: hard raise), worth
  stating as one comparison.
- **The "caller-owned interpreter, positional-only" idiom, and its exact
  error text, is shared verbatim across `RLM`, `ProgramOfThought`, and
  `CodeAct`** — `forward(self, interpreter: CodeInterpreter | None = None,
  /, **kwargs)`; `TypeError("To use a caller-owned interpreter, pass it as
  the first positional argument when calling the module.")`.
  `dspy:predict/rlm.py:701`, `program_of_thought.py:196-209`,
  `code_act.py:112-125` [pattern] (verified: read all three) · skill: new
  as an explicit shared-pattern statement (`rlm.md` states it for RLM
  only).
- **`ProgramOfThought._parse_code`'s closing code fence is optional.**
  Regex `r"```python[ \n](.*?)[ \n]```?"` — the trailing backtick group
  has a `?`, so an unterminated ```` ```python ```` block still matches.
  Empty code after parsing: `"Error: Empty code after parsing."`; a
  single-line block with more than one `=`: `"Error: Code format is not
  correct."`; a bare trailing assignment (`^(\w+)\s*=`) gets its variable
  name appended as a new line so its value is implicitly printed.
  `dspy:predict/program_of_thought.py:165-177` [trap] (verified: read) ·
  skill: new.

### OPT

*(dspy.Flex — what it is, how GEPA optimizes it; grouped under OPT because
every fact below is either GEPA's own treatment of Flex or the mechanism
that treatment depends on. Entirely new to the skill:
`api.md`'s module table has one line — "new in 3.3.0, experimental: a
module whose *source* GEPA may rewrite; runs optimizer-written code in the
Deno sandbox | nothing". Everything below is new unless marked otherwise.)*

- **What it is.** `dspy.Flex(signature, *, tools=None, interpreter_
  factory=PythonInterpreter, max_predictor_calls=100)`, `@experimental
  (version="3.3.0")`, `class Flex(Module, Parameter)`. Its "program" is a
  Python source string held as `self._module_src` and exposed read-only as
  `.module_src` — one `dspy.Module` subclass with exactly `__init__`
  (constructs predictors) and `forward` (calls them, returns a
  `dspy.Prediction`). It starts from a baseline template (`_baseline_src`):
  a single `dspy.Predict(sig)` with no tools, or `dspy.RLM(sig,
  tools=[…])` with tools. `dspy:predict/flex/flex.py:18-151` [api]
  (verified: read + `inspect.signature`) · skill: new.
- **`named_predictors()` always returns `[]`** — "A Flex's update unit is
  only its `module_src`." Consequence: every optimizer that discovers
  tunable predictors by walking `named_predictors()` (`LabeledFewShot`,
  `BootstrapFewShot`, `BootstrapFewShotWithRandomSearch`, `KNNFewShot`,
  `InferRules`, `COPRO`, `MIPROv2`, `SIMBA` — everything except `GEPA`,
  which type-checks for `Flex`) sees ZERO predictors inside a `Flex`
  submodule and silently does nothing to it: no demos, no tuned
  instructions, no error. `dspy:predict/flex/flex.py:114-116` [trap]
  (verified: read; `Flex` is a `Parameter` too — "a parent program's
  `named_parameters()` yields it as one leaf and never recurses into it,"
  `docs/docs/diving-deeper/flex.md` design decision #5) · skill: new.
  **Contrast with `RLM`**, above, which does *not* override
  `named_predictors()`.
- **The sandbox bridge — only three things cross the boundary, all as
  JSON over the interpreter's own tool-call protocol** (the same channel
  `dspy.RLM` uses for `find_line`/`count`): `__dspy_construct__` (the
  sandbox asks the host to build a real predictor, returns a string
  handle), `__dspy_call__` (run a predictor by handle, real LM call,
  return fields as JSON), and user tools passed to `dspy.Flex(tools=…)`
  (registered by name). `dspy:predict/flex/bridge.py:1-26` [rag|api]
  (verified: read) · skill: new.
- **`BRIDGEABLE_KINDS = ("Predict", "ChainOfThought", "RLM", "CodeAct",
  "ProgramOfThought", "ReAct", "ReActV2")`** — the exact, closed set of
  predictor types generated code may construct via `dspy.<Kind>(...)`.
  Anything else raises `CodeInterpreterError(f"dspy.{kind} is not
  supported inside a sandboxed dspy.Flex yet (bridgeable: …)")`.
  `dspy:predict/flex/bridge.py:56,192-200` [api] (verified: read; code-
  level test confirms the failure mode via `dspy.Nope`, see TEST) ·
  skill: new.
- **Three-way documentation/implementation gap on which kinds are
  actually advertised**: mechanically bridgeable — 7 (above). Advertised
  to the OPTIMIZER (`dspy/predict/flex/primitives_doc.py`, the literal
  prompt text GEPA's code proposer reads): `Predict`, `ChainOfThought`,
  `ReAct`, `RLM` — **4** (never `ReActV2`, `CodeAct`, or
  `ProgramOfThought`). Advertised to a HUMAN reader
  (`docs/docs/diving-deeper/flex.md`'s "Available" list): adds `ReActV2` —
  **5**, still omits the two now-deprecated ones. `dspy:predict/flex/
  primitives_doc.py:41-96`, `docs/docs/diving-deeper/flex.md:90-97` [trap]
  (verified: read both) · skill: new.
- **`max_predictor_calls` (default 100) counts bridged PREDICTOR calls,
  checked and incremented before the call runs — the identical idiom to
  RLM's `max_llm_calls`** — `_Invocation.call`: `if budget is not None and
  self._calls > budget: raise CodeInterpreterError(f"Sandboxed dspy.Flex
  forward exceeded its predictor-call budget ({budget}). Raise
  max_predictor_calls if this is expected.")`. It does NOT bound raw
  Python loop iterations with no predictor call inside them — bounding
  those is a PROMPT-ONLY instruction to the optimizer ("Every `while` loop
  must be bounded… Pick a small N"), not a code-enforced limit anywhere in
  this slice. `dspy:predict/flex/bridge.py:202-210`,
  `dspy:predict/flex/primitives_doc.py:114-115` [trap] (verified: read) ·
  skill: new. One bridged call to a nested `dspy.RLM` counts as ONE
  against this budget even though that RLM call can independently spend
  its own `max_iters` + `max_llm_calls` — the two budgets are separate and
  multiply in the worst case.
- **LM errors are wrapped crossing into the sandbox and unwrapped crossing
  back out, asymmetrically.** A bridged call raising `LMError` is tagged
  and re-raised as `CodeInterpreterError(f"{tag} {type(e).__name__}: {e}")`
  — so code INSIDE the sandbox (e.g. a try/except around a predictor call)
  can only ever see `CodeInterpreterError`, never the real `LMError`
  subclass. If that error propagates all the way out uncaught,
  `BridgeRuntime.forward`'s own except-block detects the tag and
  **re-raises the original `LMError`** to the real caller — so a caller
  outside `Flex` (e.g. `lmrun.call`'s exception-type matching) sees the
  same error hierarchy it always would. `dspy:predict/flex/bridge.py:215-220,
  273-278` [trap] (verified: read) · skill: new.
- **The returned `Prediction`'s shape is always enforced host-side against
  the FLEX's OWN declared signature, regardless of what the sandboxed
  code computed.** `prediction_to_fields` requires `json.dumps(fields)` to
  succeed or raises `CodeInterpreterError("A bridged predictor returned a
  field that cannot cross the sandbox boundary (must be JSON-serializable):
  …")`. `BridgeRuntime._to_prediction`: a missing-but-optional output is
  filled from its default; missing-but-None-allowed is filled `None`;
  anything else missing raises `CodeInterpreterError("… missing required
  output field(s) …")`; every present value is parsed against its real
  annotation, raising `CodeInterpreterError("… is not a valid {annotation}:
  …")` on a mismatch. `dspy:predict/flex/bridge.py:113-131,291-325` [api]
  (verified: read) · skill: new — GEPA can rewrite the logic, never the
  output contract.
- **Custom-type objects cross the boundary only as their serialized
  string, never as live objects inside the sandbox.**
  `_collect_custom_type_originals` records every `dspy.adapters.types.
  base_type.Type` instance in the ORIGINAL top-level `forward(**kwargs)`
  inputs, keyed by `value.serialize_model()`; every later bridged tool or
  predictor call restores the real host object wherever its serialized
  string reappears in that call's kwargs. `dspy:predict/flex/bridge.py:157-
  177,214` [api] (verified: read) · skill: new.
- **A nested code-executing sub-predictor (`RLM`/`CodeAct`/`ProgramOfThought`
  constructed inside `module_src`) automatically inherits `Flex`'s own
  `interpreter_factory` unless the generated code overrides it** —
  `_build_predictor`: `if "interpreter_factory" not in extra and
  _accepts_interpreter_factory(cls): extra["interpreter_factory"] = self.
  _sub_interpreter_factory()` — "The sandbox code can't set this itself,
  since a live interpreter can't cross the boundary." It gets its own
  SEPARATE session from that factory, not a shared live one: "a forward
  owns an outer session and nested code-executing modules may request
  separate sessions." `dspy:predict/flex/bridge.py:352-365` [api]
  (verified: read; confirmed in `docs/docs/diving-deeper/flex.md` design
  decision #7) · skill: new.
- **The sandbox's fake `dspy` module exposes exactly 4 names + 7
  predictor constructors, registered as `sys.modules["dspy"]` inside the
  guest interpreter only** — `Module`, `Prediction` (bare attribute bag),
  `Signature` (a FUNCTION, not a class: `dspy.Signature(str, instructions)`
  returns a marker dict — no `InputField`/`OutputField`/class-based
  signatures exist inside the sandbox at all), `Tool` (identity function,
  silently discards `name=`/`desc=`), plus `Predict`/`ChainOfThought`/
  `RLM`/`CodeAct`/`ProgramOfThought`/`ReAct`/`ReActV2` constructors.
  `dspy:predict/flex/_sandbox_shim.py:100-127` [api] (verified: read;
  confirmed by the official "Not available" list: "adapters…, `dspy.
  settings`, `dspy.context`, `dspy.configure`, `dspy.LM`, `dspy.Example`,
  `dspy.Evaluate`, the optimizers, retrievers, and `dspy.Flex` itself — no
  nesting. Class-based signatures and typed field declarations.",
  `docs/docs/diving-deeper/flex.md:99-105`) · skill: new.
- **Predictor construction is deferred until `__setattr__` fires, and the
  ATTRIBUTE NAME becomes the host-side handle** — `dspy.Predict(sig)`
  inside the shim just returns a `_DspyPending`; `_DspyModule.__setattr__`
  is the only place that calls `__dspy_construct__`, keyed by the literal
  attribute name being assigned to. `dspy:predict/flex/_sandbox_shim.py:60-
  83` [api] (verified: read) · skill: new — this is *why*
  `primitives_doc.py` states as a hard rule "Define every predictor in
  `__init__` as `self.<name> = dspy.Predict(...)`" — not style, mechanism.
  A `tools=[local_helper]` passed to a shim-nested `ReAct`/`RLM` is encoded
  purely BY NAME (`_dspy_enc`: any callable with `__name__` becomes
  `{"__dspy_tool__": name}`); if that name isn't one of the ORIGINAL
  `dspy.Flex(tools=…)` tools, the host raises `CodeInterpreterError(
  "Sandboxed code referenced tool {name!r}, which was not passed to
  dspy.Flex(tools=...). Tools authored inside the generated module cannot
  be handed to a bridged sub-predictor.")` — a locally-defined sandbox
  helper LOOKS syntactically valid to pass this way and always fails at
  runtime.
- **Custom output types need `custom_types` explicitly because DSPy's
  normal signature-string type lookup inspects the CALLER's stack frame,
  and Flex's caller is bridge machinery, not the user's module** — "dspy's
  usual caller-frame type lookup runs inside dspy, where your module is
  out of scope." `docs/docs/diving-deeper/flex.md` design decision #8
  [claim] (the caller-frame lookup itself is outside this slice) · skill:
  new — the rationale behind `FlexContext.custom_types()`/`render_
  annotation` (`dspy:predict/flex/ctx.py:76-164`), threaded through
  `make_signature(..., custom_types=…)` in `_resolve_signature`
  (`bridge.py:95-102`). An annotation that can't round-trip the signature-
  string grammar at all (e.g. `Callable`) is emitted **untyped** in the
  rendered baseline rather than failing construction
  (`ctx.py:65-72,145-148`, `except ValueError: parts.append(fname)`).
- **`program_trace` — a GEPA metric parameter, opt-in by declaration, on
  top of the standard 5-arg metric shape, code-verified.** A metric
  declaring `program_trace=None` as a sixth parameter receives the real
  execution trace during GEPA's selection-eval pass while the ordinary
  `trace` argument stays `None` ("eval-mode semantics of the `trace`
  argument are preserved"); a metric that doesn't declare it gets vanilla
  behavior ("never fed the trace through the bootstrapping channel").
  `tests/flex/test_flex_gepa.py:153-197`,
  `test_selection_eval_passes_program_trace_to_declaring_metric` /
  `test_selection_eval_keeps_vanilla_semantics_for_legacy_metric` [opt]
  (verified: read test code, not just docs) · skill: new. Worked example
  from `docs/docs/api/modules/Flex.md:68-83`: `score = max(0.0, (1.0 if
  correct else 0.0) - LLM_CALL_PENALTY * len(program_trace))` — "Keep the
  penalty small relative to correctness, so a decomposition has to *hold*
  accuracy to win."
- **A broken candidate has TWO failure-isolation levels, code-verified,
  and a genuine safety exception the docs' own summary glosses over.**
  - Bind-time failure (source doesn't parse / no class / raises while
    constructing a predictor, e.g. `self.p = dspy.Nope('q -> a')`): the
    WHOLE batch scores at `failure_score`, every output slot `None` ("the
    batch never ran"). `tests/flex/test_flex_gepa.py:299-334`,
    parametrized over exactly these three cases.
  - Run-time failure (parses, crashes on one input): scored PER EXAMPLE,
    in its own slot as a `FailedPrediction` carrying the error text; other
    examples' scores/outputs are untouched — "the gepa engine pairs scores
    with example ids positionally, so a short list would credit example
    N+1's score to example N." `tests/flex/test_flex_gepa.py:242-264`.
  - **The crashing input and the exact error text reach the code
    proposer's own reflective dataset** — `recs[1]["Inputs"] == {"q":
    "boom"}`, `"RuntimeError: runtime crash on this input" in
    str(recs[1]["Generated Outputs"])`: "For a code candidate the crash
    IS the feedback… If it were dropped, GEPA would score the slot as a
    failure yet reflection would never learn which input broke or how."
    `tests/flex/test_flex_gepa.py:268-296`.
  - **Only source-level failures are absorbed — a genuine infrastructure
    error (rate limit, provider outage) during the bind/build step is NOT
    swallowed, it propagates and stops the run.** Simulated via
    monkeypatching `dspy.teleprompt.gepa.gepa_utils.rebind_flex_code` to
    raise a plain `RateLimitError`: `with pytest.raises(RateLimitError):
    adapter.evaluate(...)`. Docstring: "Only source-level failures are
    absorbed. An LM provider or rate-limit error is not the candidate's
    fault — swallowing it would silently score a whole run at the failure
    score and hand back an 'optimized' program chosen from garbage."
    `tests/flex/test_flex_gepa.py:336-358` [opt] (verified: read test) ·
    skill: new — this REFINES the docs' own "a broken candidate can't
    crash the optimization run" (`docs/docs/api/modules/Flex.md:36`),
    which doesn't itself draw the source-vs-infrastructure line; missing
    this distinction would make someone think GEPA silently absorbs
    *every* error during a Flex candidate's evaluation, which it does not.
- **GEPA's code proposer is separate from its instruction proposer, and a
  custom `instruction_proposer=` never touches Flex components.** "Code
  components are seeded with their current `module_src` and evolved by a
  dedicated code proposer; instruction components… by GEPA's usual
  instruction proposer. A custom `instruction_proposer` replaces the
  instruction proposer only; code components stay on the code proposer."
  `docs/docs/diving-deeper/flex.md` design decision #3 [claim] (GEPA's own
  proposer code is outside this slice) · skill: new — directly relevant to
  `dspy.GEPA(instruction_proposer=…)`, already a documented parameter in
  `api.md`'s surface line.
- **Mixing a `Flex` with ordinary predictors in one program**: GEPA
  optimizes the Flex's code and the other predictors' instructions, but
  NEVER the instructions of predictors that live *inside* the Flex — "they
  are constructed by the current `module_src` and will be replaced
  wholesale by the next code candidate." `docs/docs/diving-deeper/flex.md`
  design decision #5 [claim] · skill: new.
- **Saving/loading: `interpreter_factory` is never part of saved state,
  and silently falls back to the default.** `dump_state`/`load_state` are
  exactly `{"module_src": …, "lm": …}`; `Flex.__getstate__` pops `_bridge`
  before pickling, `__setstate__` rebuilds it and rebinds `module_src`.
  "Reconstructing with `dspy.Flex(signature)` restores the default
  sandbox… re-supply [interpreter_factory] in the constructor before
  `load` only if you used a custom one." `dspy:predict/flex/flex.py:72-
  108,157-159` [api|trap] (verified: read; confirmed twice more in docs —
  `Flex.md:114-125`, `diving-deeper/flex.md` design decision #9) · skill:
  new — loading a Flex optimized with a custom `interpreter_factory`
  WITHOUT re-supplying it silently gets the default `PythonInterpreter`,
  no warning.
- **Deepcopying a `Flex` re-parses `module_src` (`ast.parse`) every time**
  — `__setstate__` calls `self._rebuild_bridge()` then, if `module_src` is
  set, `self._bridge.bind(self._module_src)` immediately, which re-runs
  `parse_module_class_name` (`ast.parse`). `Refine`/`BestOfN` deepcopy
  the wrapped module on EVERY attempt (`mod = self.module.deepcopy()`) —
  wrapping a `Flex` in `Refine(module=flex_instance, N=5, …)` reparses
  `module_src` 5 times per call, purely from the deepcopy machinery,
  before any interpreter is created. `dspy:predict/flex/flex.py:72-81`,
  `dspy:predict/refine.py:108`, `best_of_n.py:58` [pattern] (verified:
  read all three) · skill: new.

### PROD

- **The Deno/Pyodide sandbox's default-deny security posture, in exact
  flags**: `PythonInterpreter`'s docstring — "Code runs in an isolated
  Pyodide environment with no access to the host filesystem, network, or
  environment by default." `--allow-read` is ALWAYS present (the runner
  script + Deno's own cache dir, plus any `enable_read_paths`/
  `enable_write_paths`); `--allow-env` only with `enable_env_vars`;
  `--allow-net` only with `enable_network_access`; `--allow-write` only
  with `enable_write_paths`. `dspy:primitives/python_interpreter.py:220-
  222,297-328` [prod] (verified: read) · skill: new — `rlm.md` states
  "restricted by default" without the flags.
  - **Mounted read/write paths collide on basename, not full path** — two
    host files with the same basename cannot both be mounted:
    `CodeInterpreterError("Mounted files must have unique basenames inside
    the sandbox.")`. `python_interpreter.py:274-283` [prod] (verified:
    read) · skill: new.
  - **Write access to the interpreter's own runtime files is explicitly
    forbidden** — a write path overlapping the runner script or Deno's
    cache dir raises `CodeInterpreterError("Write paths cannot overlap
    PythonInterpreter runtime files.")`. `python_interpreter.py:306-310`
    [prod] (verified: read) · skill: new.
  - **DSPy disables ambient Deno project discovery for its runner**:
    `--no-config --no-lock --node-modules-dir=false`. "A `package.json` in
    the current directory or an ancestor therefore cannot redirect the
    sandbox's pinned Pyodide dependency. No `DENO_NO_PACKAGE_JSON`
    environment variable is required." `python_interpreter.py:298-304`,
    `docs/docs/api/tools/PythonInterpreter.md:22-24` [prod] (verified:
    read code + doc) · skill: new.
- **A session that ends terminally cannot be reused, ever, and actively
  kills the Deno subprocess.** `_raise_terminal_error` sets `_session_
  ended = True`, terminates the live process, then raises. `_check_
  session_active` guards every `execute()`/`start()`:
  `CodeInterpreterError("PythonInterpreter session has ended; create a new
  interpreter for a fresh session.")`. `start()`'s own docstring: "A
  stopped or shut-down session cannot be restarted because its Python
  state cannot be reconstructed." `python_interpreter.py:352-371,854-869`
  [prod] (verified: read) · skill: new — sharpens `rlm.md`'s existing
  caller-owned-interpreter-reuse note: any protocol/process failure on
  *any* call permanently kills it for every later call too.
- **Thread ownership is claimed on first use, not at construction.**
  `_check_thread_ownership` records `self._owner_thread` on the first
  `execute()` from any thread, then raises `RuntimeError("PythonInterpreter
  is not thread-safe and cannot be shared across threads. Create a
  separate interpreter instance for each thread.")` on a different
  thread's first attempt. `python_interpreter.py:384-393` [prod]
  (verified: read) · skill: same (already cited by `rlm.md`), precision
  added: ownership is claimed by whichever thread calls `execute()` first,
  not the constructing thread.
- **Large-variable threshold and its exact reason**: `LARGE_VAR_THRESHOLD
  = 100 * 1024 * 1024` (100 MB). "Pyodide's FFI crashes at exactly 128MB
  (134,217,728 bytes). Use filesystem injection for strings above 100MB
  to stay safely below this limit." A variable over the threshold is not
  inlined as Python source; it is sent via a separate `inject_var` JSON-
  RPC call to a virtual file (`/tmp/dspy_vars/{name}.json`), read back by
  a preamble `{k} = json.loads(open('/tmp/dspy_vars/{k}.json').read())`.
  `python_interpreter.py:36-38,692-715` [prod] (verified: read) · skill:
  new — a concrete capacity limit not stated anywhere in `rlm.md`.
  `SandboxSerializable` payloads go through the same channel and the same
  threshold.
- **`_inject_variables`' name rule is broader than "just `json`."**
  `if not key.isidentifier() or keyword.iskeyword(key) or key == "json":
  raise CodeInterpreterError(f"Invalid variable name: '{key}'")` — ANY
  non-identifier or Python keyword (`class`, `def`, `for`, `import`,
  `lambda`, …) is also rejected as an input name, not only the literal
  string `"json"`. `python_interpreter.py:694-696` [trap] (verified:
  read) · skill: wrong: `rlm.md`'s "an input named `json`" trap names only
  that one case.
- **`MIN_DENO_VERSION = (2, 0, 0)`, `MAX_DENO_VERSION = (3, 0, 0)`
  (exclusive), `DENO_PROBE_TIMEOUT_SECONDS = 10`** — the version window
  `rlm.md` already cites, now directly sourced, plus the previously-
  undocumented 10-second timeout on the `deno info --json` subprocess call
  used to find Deno's cache dir. `python_interpreter.py:39-41` [prod]
  (verified: read) · skill: same (version window), new (probe timeout).
  The `deno` PyPI extra pins `>=2.4.5,<3.0.0`, "adds approximately 40–50
  MiB," ships binaries for "macOS x86-64/arm64, glibc Linux x86-64/arm64,
  and Windows x86-64." `docs/docs/api/tools/PythonInterpreter.md:12-15`.
- **JSON-RPC error taxonomy is closed and numbered.** Protocol errors
  `ParseError`(-32700)/`InvalidRequest`(-32600)/`MethodNotFound`(-32601)
  are always terminal out-of-band. Application errors: `SyntaxError`
  (-32000), `NameError`(-32001), `TypeError`(-32002), `ValueError`(-32003),
  `AttributeError`(-32004), `IndexError`(-32005), `KeyError`(-32006),
  `RuntimeError`(-32007), `CodeInterpreterError`(-32008), `Unknown`
  (-32099). In `execute()`: a `SyntaxError` app-error code raises a REAL
  `SyntaxError`; any other recognized code raises `CodeExecutionError`;
  a code outside this set is TERMINAL rather than raised as a normal
  exception. `python_interpreter.py:47-66,842-846` [prod] (verified:
  read) · skill: new.
- **`execute()` refuses to recurse from inside a tool call**: `if self.
  _handling_tool_call: raise CodeInterpreterError("PythonInterpreter
  cannot execute recursively from one of its tools.")`. Tolerates up to
  100 non-JSON-RPC stdout lines (Pyodide package-loading noise) before
  giving up: `CodeInterpreterError("Too many skipped lines (…) …")`.
  `_health_check()` runs on every process start, requiring `print(1+1)`
  to output exactly `"2"` or the session is killed.
  `python_interpreter.py:663-668,773-774,793-851` [prod] (verified:
  read) · skill: new.
- **`shutdown()` blocks, and behaves differently by prior state**:
  graceful (JSON-RPC `shutdown` notification, close stdin, then `wait()`)
  only while the session was still active; an already-terminally-ended
  session's process is just `terminate()`d directly. Always blocks on
  `deno_process.wait()`. `python_interpreter.py:883-896` [prod] (verified:
  read) · skill: new.

### TEST

- **DSPy's own `dspy.utils.DummyLM`-based reward-function bug in its
  shipped test suite: `tests/predict/test_best_of_n.py`'s only reward
  function never actually validates anything.** `test_refine_forward_
  success_first_attempt` (the file's own first test — note the name, see
  next item) uses `reward_fn = lambda kwargs, pred: 1.0 if
  len(pred.answer) == 1 else 0.0` with the comment "The answer should
  always be one word" — this checks the STRING's character count, not
  `len(pred.answer.split())`. Every scripted answer ("Brussels", "City of
  Brussels") is longer than 1 character, so the reward is 0.0 on every
  attempt, `threshold=1.0` is never met, and `BestOfN` returns the first
  (tied) attempt — which happens to equal the expected "Brussels," so the
  test passes without the reward function ever correctly testing anything.
  `tests/predict/test_best_of_n.py:20-44` [test] (verified: read) · skill:
  new — the exact "a check that cannot fail" shape `patterns.md`'s "What
  the patterns share that is worth keeping" section names as recurring
  across the nine repositories, found here instead in DSPy's own shipped
  test suite.
- **`tests/predict/test_best_of_n.py`'s three test functions are literally
  named after `Refine`** — `test_refine_forward_success_first_attempt`,
  `test_refine_module_default_fail_count`, `test_refine_module_custom_
  fail_count`, all importing and exercising `BestOfN` — a copy-paste
  artifact from `test_refine.py` left uncorrected; the test bodies are
  otherwise correct. `tests/predict/test_best_of_n.py:20,48,62` [test]
  (verified: read) · skill: new, small.
- **`dspy.Flex`'s bind-vs-runtime failure distinction, and the code-
  proposer's crash-visibility, are asserted by dedicated tests**, not only
  claimed in prose — see FLEX above (`tests/flex/test_flex_gepa.py`, four
  tests cited). [test] (verified: read) · skill: new.
- **RLM's caller-owned-interpreter reuse across sync+async calls, and the
  post-shutdown-raises contract, are both directly tested** —
  `tests/predict/test_rlm.py:472-528`, three tests cited under RLM above.
  [test] (verified: read) · skill: new.
- **A dunder-attribute restriction inside Flex-authored code is a PROMPT
  rule only, with no code-level enforcement found anywhere in this
  slice** — `primitives_doc.py`: "Do NOT access dunder attributes
  (anything matching `__*__`). Use the public API." No corresponding
  check exists in `ctx.py`/`bridge.py`/`_sandbox_shim.py`; whatever stops
  it (if anything) is either the Pyodide sandbox itself or nothing.
  [trap] (verified: read all four flex/ files, found no such guard) ·
  skill: new — a rule stated to the model, unchecked by code, exactly the
  P23 shape ("a guard that covers less than it claims is worse than no
  guard") this repository's own principles name.
- **A while-loop bound inside Flex-authored code is likewise a prompt
  instruction only, not a code-level budget** — `max_predictor_calls`
  bounds bridged PREDICTOR calls, not raw Python loop iterations; a
  `while True: pass` with no predictor call inside would not be stopped by
  anything visible in this slice's code — whatever eventually kills it (a
  Deno/process-level timeout, if any) is not in `dspy/predict/flex/*` or
  `dspy/primitives/python_interpreter.py`. [trap] (verified: read; no
  wall-clock `execute()` timeout found in `python_interpreter.py`) ·
  skill: new.
- **A tutorial shipped with 3.3.1 references a class that does not
  exist.** `docs/docs/tutorials/program_of_thought/index.ipynb`'s second
  code cell: `sandbox = dspy.LocalSandbox()`. `hasattr(dspy,
  "LocalSandbox")` is `False` in both the source tag's `dspy/` and the
  installed package — grepped, zero hits either way; confirmed at
  runtime: `AttributeError: module 'dspy' has no attribute
  'LocalSandbox'`. [trap] (verified: ran; grepped both trees) · skill:
  new, high value — a genuinely broken cell in shipped, official
  documentation, and the same tutorial never mentions that
  `ProgramOfThought` itself (the module it teaches) is deprecated as of
  this same version (no "deprecat" string anywhere in the notebook,
  grep-confirmed).

### PAT

- **The "caller-owned interpreter, positional-only" idiom is one pattern
  shared by four modules**, not four independent designs: same parameter
  shape (`interpreter: CodeInterpreter | None = None, /`), same error
  text, same shared validation functions
  (`_validate_interpreter_factory`/`_create_interpreter`/`_validate_
  interpreter`, `code_interpreter.py:150-179`). `RLM`, `ProgramOfThought`,
  `CodeAct`, `Flex` [pattern] (verified: read all four) · skill: new.
- **Three sandboxed modules, three different "budget exhausted"
  behaviors** — `RLM`: forced `extract` call, normal-shaped `Prediction`,
  `final_reasoning="Extract forced final output"` (already in `rlm.md`);
  `CodeAct`: silent stop, no marker at all in the returned `Prediction`;
  `ProgramOfThought`: hard `RuntimeError`. `ReActV2` (not sandboxed but
  the same shape of question): forced `submit` call with an explicit
  `termination_reason` field; plain `ReAct`: silent stop, no marker.
  [pattern] (verified: read all five forward()s) · skill: new — a direct
  answer to the brief's "the forced final output" ask, generalized across
  every module in this slice rather than RLM alone.
- **A tool passed as a plain function is re-executed as SOURCE TEXT inside
  a sandbox by `CodeAct`, but only INVOKED BY REFERENCE (never
  re-executed) by `ReAct`/`ReActV2`/`RLM`.** `CodeAct` needs
  `inspect.getsource(tool.func)` to succeed and needs every free
  name/import the function relies on to be independently supplied — a
  materially different, more restrictive tool contract than every other
  agent module in this slice. `dspy:predict/code_act.py:128-129` vs.
  `react.py:112-115`, `react_v2.py:139-149`, `rlm.py`'s host-side tool
  invocation (rlm.md) [pattern] (verified: read) · skill: new.
- **Manual per-tool timeouts are a documented workaround, not a DSPy
  feature.** `docs/docs/tutorials/tool_use/index.ipynb` wraps tools with
  `func_timeout.func_set_timeout(10)` before handing them to a hand-rolled
  agent loop — none of `ReAct`/`ReActV2`/`RLM`/`CodeAct` impose a
  per-tool-call wall-clock limit anywhere in this slice (only `max_iters`/
  `max_llm_calls`/`max_predictor_calls` bound counts, never time). [pattern]
  (verified: read notebook cell) · skill: new.
- **A hand-rolled loop is sometimes preferred to `ReAct` even in DSPy's
  own tutorials** — `docs/docs/tutorials/games/index.ipynb`'s `Agent`
  class builds its own `max_iters`-bounded loop around a bare
  `dspy.Predict("task, trajectory, possible_actions: list[str] -> action")`
  instead of `dspy.ReAct`, when the action space needs custom
  presentation. [pattern] (verified: read notebook cell) · skill: new,
  small.

## 3. Code worth keeping

**A real `SandboxSerializable` for pandas** — `dspy:` no, this is the
tutorial, not the package: `docs/docs/tutorials/dataframe_rlm/cohort_
analysis/dataframe.py:65-99` (ran: no, read only; requires pandas/pyarrow
not installed in `.venv-dspy`):
```python
def sandbox_setup(self) -> str:
    return "import pandas as pd\nimport pyarrow\nimport base64\nimport io"

def to_sandbox(self) -> bytes:
    """Serialize DataFrame as base64-encoded Parquet."""
    return base64.b64encode(self.data.to_parquet(index=False))

def sandbox_assignment(self, var_name: str, data_expr: str) -> str:
    return f"{var_name} = pd.read_parquet(io.BytesIO(base64.b64decode({data_expr})))"

def rlm_preview(self, max_chars: int = 500) -> str:
    df = self.data
    lines = [f"DataFrame: {df.shape[0]:,} rows x {df.shape[1]} columns", "", "Columns:"]
    for col in list(df.columns)[:10]:
        dtype = str(df[col].dtype)
        null_count = int(df[col].isna().sum())
        null_info = f" ({null_count:,} nulls)" if null_count > 0 else ""
        lines.append(f"  {col}: {dtype}{null_info}")
    if len(df) > 0:
        lines.extend(["", "Sample (first 3 rows):", df.head(3).to_string()])
    preview = "\n".join(lines)
    return preview[:max_chars] + "..." if len(preview) > max_chars else preview
```

**`Refine`'s per-attempt advice injection, the actual mechanism** —
`dspy:predict/refine.py:117-130` (ran: no, read only):
```python
if not advice:
    outputs = mod(**kwargs)
else:
    class WrapperAdapter(adapter.__class__):
        def __call__(self, lm, lm_kwargs, signature, demos, inputs):
            inputs["hint_"] = advice.get(signature2name.get(signature), "N/A")
            signature = signature.append(
                "hint_", InputField(desc="A hint to the module from an earlier run")
            )
            return adapter(lm, lm_kwargs, signature, demos, inputs)

    with dspy.context(adapter=WrapperAdapter()):
        outputs = mod(**kwargs)
```

**`BestOfN`'s `threshold=None` crash, minimal repro** — my own probe
against `dspy:predict/best_of_n.py:72`, ran on `.venv-dspy/bin/python`
offline via `lm_fixture`:
```python
import dspy
from lm_fixture import FixtureLM, offline, fill
lm = FixtureLM(fill(answer="answerX"))
qa = dspy.Predict("question -> answer")
bon = dspy.BestOfN(module=qa, N=2, reward_fn=lambda a, p: 0.5, threshold=None)
with offline(lm):
    dspy.configure(lm=lm)
    bon(question="what?")
# prints two misleading "Attempt failed: '>=' not supported between
# instances of 'float' and 'NoneType'" lines, then returns a NORMAL
# Prediction(answer="answerX") anyway.
```

**`FlexContext.render_annotation`, the signature-string type renderer that
decides what a Flex signature field can even be** —
`dspy:predict/flex/ctx.py:125-165` (ran: no, read only; ≤40 lines):
```python
def render_annotation(annotation: Any, custom_types: dict[str, type] | None = None) -> str:
    return ast.unparse(_render_type_node(annotation, custom_types or {}))

def _render_type_node(annotation: Any, custom_types: dict[str, type]) -> ast.expr:
    if annotation is type(None):
        return ast.Constant(value=None)
    origin = get_origin(annotation)
    if origin is None:
        name = getattr(annotation, "__name__", None)
        if annotation in _BUILTIN_TYPES:
            return ast.Name(id=annotation.__name__)
        if annotation is Any or (name and typing.__dict__.get(name) is annotation):
            return ast.Name(id=name or "Any")
        if isinstance(annotation, type) and name and custom_types.get(name) is annotation:
            return ast.Name(id=name)
        raise ValueError(
            f"Annotation {annotation!r} has no name the signature-string grammar can resolve; "
            "pass it via custom_types to make it renderable."
        )
    args = get_args(annotation)
    if origin in (typing.Union, types.UnionType):
        node = _render_type_node(args[0], custom_types)
        for arg in args[1:]:
            node = ast.BinOp(left=node, op=ast.BitOr(), right=_render_type_node(arg, custom_types))
        return node
    # … Literal and generic-subscript branches omitted for length
```

## 4. Probes worth adding

- **`predict-silent-temperature-bump`** — "A `Predict` call requesting more
  than one completion at the LM's unset or near-zero temperature is
  silently sent at `temperature=0.7`."
  ```python
  def p_predict_silent_temperature_bump():
      import sys
      sys.path.insert(0, "/home/user/kohaerenzprotokoll/scripts")
      import dspy
      from lm_fixture import FixtureLM, chat, offline
      lm = FixtureLM(lambda messages: chat(answer="x"))
      with offline(lm):
          dspy.configure(lm=lm)
          dspy.Predict("q -> answer")(q="hi", config={"n": 3})
          sent = lm.requests[-1]["kwargs"] if hasattr(lm, "requests") else lm.history[-1]["kwargs"]
          if sent.get("temperature") != 0.7:
              return f"expected silent temperature=0.7 for n=3 with no explicit temperature, got {sent.get('temperature')!r}"
      return None
  ```
  Ran on `.venv-dspy/bin/python`, offline, and saw hold: `lm.history[-1]
  ["kwargs"] == {"temperature": 0.7, "n": 3}`.
- **`bestofn-none-threshold-crashes`** — "`dspy.BestOfN(threshold=None)`
  raises a misleading `TypeError` from inside its own threshold check on
  every attempt, unlike `dspy.Refine`, which explicitly guards `threshold
  is not None`."
  ```python
  def p_bestofn_none_threshold_crashes():
      import sys
      sys.path.insert(0, "/home/user/kohaerenzprotokoll/scripts")
      import dspy
      from lm_fixture import FixtureLM, offline, fill
      lm = FixtureLM(fill(answer="x"))
      qa = dspy.Predict("question -> answer")
      bon = dspy.BestOfN(module=qa, N=3, reward_fn=lambda a, p: 0.5, threshold=None)
      with offline(lm):
          dspy.configure(lm=lm)
          try:
              bon(question="hi")
              return "expected TypeError at N=3 (fail_count exhausted), call returned instead"
          except TypeError as e:
              if "'>=' not supported" not in str(e):
                  return f"raised TypeError but not the threshold-comparison one: {e}"
      return None
  ```
  Ran on `.venv-dspy/bin/python`, offline, and saw hold (N=3 raised the
  expected `TypeError`; N=2 was separately observed to return a normal
  `Prediction` despite two misleading "Attempt failed" lines).
- **`react-adapterparseerror-uncaught`** — "`dspy.ReAct`'s own `except
  ValueError` for an invalid tool choice does not catch
  `dspy.AdapterParseError`, so an out-of-set `next_tool_name` answer
  propagates uncaught out of `forward()`."
  ```python
  def p_react_adapterparseerror_uncaught():
      import sys
      sys.path.insert(0, "/home/user/kohaerenzprotokoll/scripts")
      import dspy
      from lm_fixture import FixtureLM, chat, offline
      def get_weather(city: str) -> str:
          return f"sunny in {city}"
      def responder(messages):
          return chat(next_thought="x", next_tool_name="bogus_tool", next_tool_args="{}")
      lm = FixtureLM(responder)
      agent = dspy.ReAct("question -> answer", tools=[get_weather], max_iters=3)
      with offline(lm):
          dspy.configure(lm=lm)
          try:
              agent(question="weather in Oslo?")
              return "expected AdapterParseError to propagate, forward() returned instead"
          except dspy.AdapterParseError:
              return None
          except Exception as e:
              return f"raised {type(e).__name__}, not AdapterParseError: {e}"
  ```
  Ran on `.venv-dspy/bin/python`, offline, and saw hold: `AdapterParseError`
  propagated out of `agent(...)` uncaught.
- **`refine-requires-retrievable-module-source`** — "`dspy.Refine`
  requires `inspect.getsource` on the wrapped module's *class*, not only
  the reward function; `dspy.BestOfN` requires neither."
  ```python
  def p_refine_requires_retrievable_module_source():
      # Run as a FILE (python script.py), not `python -c`: inspect.getsource
      # needs a real source file backing the module class.
      import sys
      sys.path.insert(0, "/home/user/kohaerenzprotokoll/scripts")
      import dspy
      qa = dspy.Predict("question -> answer")
      try:
          dspy.Refine(module=qa, N=2, reward_fn=lambda a, p: 0.0, threshold=1.0)
          dspy.BestOfN(module=qa, N=2, reward_fn=lambda a, p: 0.0, threshold=1.0)
      except OSError:
          return None if "Refine" in locals() else "unexpected OSError"
      return None
  ```
  Not run as written above (needs a real file, not `-c`); ran the
  equivalent as a `.py` script and saw hold — `Refine(module=dspy.Predict(
  …), …)` raised `OSError: could not get source code` at
  `dspy:predict/refine.py:94` while an equivalent `BestOfN(...)` call did
  not raise at all.

## 5. Surface worth asserting

All confirmed via `inspect.signature` on `.venv-dspy`'s installed package,
2026-09-25 (offline, no key):

```
dspy.Predict(signature, callbacks=None, **config)
dspy.ChainOfThought(signature, rationale_field=None, rationale_field_type=str, **config)
dspy.ReAct(signature, tools, max_iters=20)
dspy.ReActV2(signature, tools, max_iters=20)
dspy.ProgramOfThought(signature, max_iters=3, interpreter_factory=PythonInterpreter)
dspy.CodeAct(signature, tools, max_iters=5, interpreter_factory=PythonInterpreter)
dspy.RLM(signature, max_iters=20, max_llm_calls=50, max_output_chars=10000, verbose=False, tools=None, sub_lm=None, interpreter_factory=PythonInterpreter)
dspy.Flex(signature, *, tools=None, interpreter_factory=PythonInterpreter, max_predictor_calls=100)
dspy.Refine(module, N, reward_fn, threshold, fail_count=None)
dspy.BestOfN(module, N, reward_fn, threshold, fail_count=None)
dspy.MultiChainComparison(signature, M=3, temperature=0.7, **config)
dspy.Parallel(num_threads=None, max_errors=None, access_examples=True, return_failed_examples=False, provide_traceback=None, disable_progress_bar=False, timeout=120, straggler_limit=3)
dspy.PythonInterpreter(deno_command=None, enable_read_paths=None, enable_write_paths=None, enable_env_vars=None, enable_network_access=None, sync_files=True, tools=None, output_fields=None, callbacks=None)
dspy.KNN(k, trainset, vectorizer)
dspy.majority(prediction_or_completions, normalize=default_normalize, field=None)
```
Not constructible on 3.3.1, signature intact but body fails (verified: ran):
```
dspy.predict.avatar.avatar.Avatar(signature, tools, max_iters=3, verbose=False)   # -> AttributeError: dspy.TypedPredictor
```
Class relationships, verified via `__mro__`/`__bases__`:
```
dspy.predict.code_act.CodeAct.__mro__ == (CodeAct, ReAct, ProgramOfThought, Module, BaseModule, object)
dspy.predict.flex.flex.Flex.__bases__ == (Module, Parameter)
dspy.predict.avatar.avatar.Avatar.__bases__ == (Module,)          # NOT Parameter
dspy.predict.parallel.Parallel.__bases__ == (object,)             # NOT Module
dspy.predict.knn.KNN.__bases__ == (object,)                       # NOT Module
```

## 6. Ten things the skill must say

1. **`dspy.ReActV2` will become `dspy.ReAct` in DSPy 3.5**, with the current
   implementation demoted and `ReActV2` itself removed in 3.6 — every
   ReAct/ReActV2 difference in this file is a forward-looking breaking
   change, not a stable-vs-experimental curiosity (§AGENT, first item).
2. **`dspy.ReAct`'s own `except ValueError` cannot catch an out-of-set tool
   choice** (`AdapterParseError` isn't a `ValueError`) and propagates
   uncaught — verified live, and independently fixed in `ReActV2`'s own
   except clause (§AGENT).
3. **`dspy.ProgramOfThought` and `dspy.CodeAct` are already deprecated in
   3.3.1**, fire a real `DeprecationWarning` on every construction, name
   RLM as the replacement, and are gone in 3.5 — the skill's module table
   says "nothing" with no deprecation note at all (§API).
4. **`dspy.Flex` (new in 3.3.0): its "program" is a Python source string
   (`module_src`), sandboxed via the same bridge protocol RLM uses,
   `named_predictors()` always `[]` so only GEPA (by isinstance) can touch
   it, and its BRIDGEABLE_KINDS/prompt/docs each advertise a different
   subset of what it can construct** — entirely new to the skill (§FLEX).
5. **`dspy.SandboxSerializable` lets non-string inputs (DataFrames, binary
   blobs) enter an RLM sandbox once, by name, and then persist and mutate
   across iterations — unlike every plain string/dict/list input, which is
   silently reverted every iteration** — a real exception to `rlm.md`'s
   blanket "inputs revert every iteration" claim, absent from it entirely
   (§RLM).
6. **`Predict._forward_preprocess` silently bumps `temperature` to `0.7`
   whenever `n>1` and the configured temperature is unset or ≤0.15** —
   verified live, no warning anywhere (§API).
7. **`BestOfN(threshold=None)` crashes with a misleading `TypeError` on
   every attempt** (no `is not None` guard, unlike `Refine`), returning a
   normal-looking `Prediction` at small N and raising at larger N — verified
   live, a materially more dangerous failure than `Refine`'s clean support
   for the same call (§API / §Probes).
8. **Three sandboxed modules have three different "ran out of budget"
   behaviors**: RLM forces a clean `extract` call, `CodeAct` stops silently
   with no marker anywhere in the `Prediction`, `ProgramOfThought` raises
   `RuntimeError` — and `ReActV2` forces `submit` with an explicit
   `termination_reason` while plain `ReAct` also gives no marker at all
   (§AGENT/§PAT).
9. **The Deno/Pyodide sandbox has a hard, sourced 100 MB variable-injection
   threshold** (Pyodide's FFI crashes at exactly 128 MB), a closed
   9-name error taxonomy, a terminal-session model where any protocol
   failure permanently kills reuse, and `--allow-read/-env/-net/-write`
   flags that are each strictly conditional on the matching constructor
   argument — none of this is in the skill (§PROD).
10. **The `program_of_thought` tutorial shipped with 3.3.1 calls
    `dspy.LocalSandbox()`, a class that does not exist anywhere in the
    package**, and never mentions that `ProgramOfThought` itself is
    deprecated in the same version — verified by grep and at runtime
    (§TEST).
