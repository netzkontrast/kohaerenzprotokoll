# Adapters and types — DSPy 3.3.1

## 1. Header

**Slice**: `dspy/adapters/` (all, incl. `types/`) and `dspy/streaming/` (all); their tests;
their docs and six tutorials.

**Files read**:
- Code, full: 24 files, 5,759 lines — every file in `dspy/adapters/` (`__init__.py`,
  `base.py` 778, `chat_adapter.py` 299, `json_adapter.py` 311, `xml_adapter.py` 240,
  `two_step_adapter.py` 244, `baml_adapter.py` 270, `utils.py` 336,
  `_legacy_type_markers.py` 145, `types/__init__.py`, `types/{audio,base_type,citation,
  code,document,file,history,image,reasoning,tool}.py`) and every file in
  `dspy/streaming/` (`__init__.py`, `messages.py` 184, `streamify.py` 288,
  `streaming_listener.py` 415).
- Tests, mixed depth: 16 files, 10,316 lines total. Read in full: `conftest.py`,
  `test_adapter_utils.py`, `test_audio.py`, `test_base_type.py`, `test_code.py`,
  `test_document.py`, `test_reasoning.py` (≈390 lines). For the six largest files
  (`test_chat_adapter.py` 2,948, `test_json_adapter.py` 1,718, `test_xml_adapter.py`
  1,020, `test_streaming.py` 2,063, `test_tool.py` 768, `test_baml_adapter.py` 643) I
  listed every `def test_...` name (100% of test coverage surveyed) and read the full
  body of ~35 representative tests per the behaviour they pin down (~1,000 lines) —
  this was a deliberate economy after a mid-task interruption; the remaining lines of
  those six files were not read line by line.
- Docs: all 19 API-reference stub pages in scope (`adapters/`, `experimental/`,
  the six `primitives/` pages, the four `utils/` pages) are `mkdocstrings` `:::`
  stubs with no prose of their own — confirmed empty of independent content.
  `diving-deeper/adapters.md` (186) and `learn/programming/adapters.md` (335) read in
  full — both substantive and directly source-verified. `tutorials/streaming/index.md`
  (493) read in full. `tutorials/mcp/index.md` and `tutorials/email_extraction/index.md`
  grep-targeted for adapter/type-relevant sections only. **Not read**:
  `tutorials/audio/index.ipynb`, `tutorials/image_generation_prompting/index.ipynb`,
  `tutorials/entity_extraction/index.ipynb` — skipped under the economy directive;
  their ground is otherwise covered by `types/audio.py`, `types/image.py`, the
  `email_extraction` tutorial's Pydantic/Enum/Optional signatures, and the JSON/Chat
  adapter test suites. This is a real gap, not a claim of completeness.
- Also read, outside the nominal slice because the brief's own questions require it:
  `dspy/utils/exceptions.py:246-283` (`AdapterParseError`'s fields — explicitly asked
  for), `dspy/utils/annotation.py` (`@experimental`, decorates `Citations`/`Document`),
  `dspy/predict/chain_of_thought.py` (55 lines — resolves an apparent contradiction
  about `dspy.Reasoning`), `dspy/experimental/__init__.py`, and light greps of
  `dspy/clients/base_lm.py` / `dspy/clients/lm.py` for `supports_function_calling` /
  `supports_reasoning` defaults. Also read (this repository, not the DSPy source, at
  the coordinator's request): `scripts/claude_lm.py:1-100`.

**Verified by running** (`.venv-dspy/bin/python`, keys scrubbed): `inspect.signature`
on every adapter/`StreamListener`/`streamify`/`ChainOfThought` constructor; the exact
`ChatAdapter`/`JSONAdapter` system-message text for a German `Literal` signature
matching `pairs.py`'s shape; the streaming-adapter-name-vs-`isinstance` mismatch for
`BAMLAdapter`; `issubclass(dspy.Reasoning, str)` and `ChainOfThought`'s default
`reasoning` field type; `dspy.OpenAI` absence; `Document`'s mutability and silent
extra-kwarg acceptance; `AdapterParseError`'s fields end to end; `Tool.__call__`'s
exact `ValueError` on a sync call into an async function; the Literal-out-of-set
→ `AdapterParseError` path and the ChatAdapter→JSONAdapter two-call fallback cost,
both via `lm_fixture.FixtureLM`; `BAMLAdapter`'s recursive-model guard; and — the
slice's sharpest find — that a `Literal`/enum/pydantic value that fails
`parse_value` inside **otherwise-valid JSON** escapes `JSONAdapter.parse()` as a
**bare, unwrapped exception**, not `AdapterParseError`, both directly and end to end
through `dspy.Predict`.

**What this part of DSPy is** (≤5 lines): the adapter layer turns a `Signature` plus
inputs/demos/history into chat messages, sends the call, and parses the reply back
into typed fields — four adapters (`Chat`, `JSON`, `XML`, `TwoStep`) plus one built on
`JSON` (`BAML`), each with a different prompt shape and its own parse strategy, but
all funnelling type coercion through one function, `parse_value`. `dspy.Type`
subclasses (`Image`, `Audio`, `File`, `Code`, `Reasoning`, `Citations`, `Document`,
`Tool`, `ToolCalls`, `History`) own their own rendering and, for `Reasoning` and
`Citations`, their own native-LM-feature wiring. `dspy.streaming` reads the same
adapters' own field-marker conventions token-by-token to let one output field stream
before the whole `Predict` call returns.

## 2. Knowledge items

## API

- **`Adapter.__init__` takes two parameters the skill's surface line omits** —
  `native_response_types=None` (defaults to `[Citations, Reasoning]`) and
  `parallel_tool_calls=None`. `ChatAdapter`/`XMLAdapter` inherit both, on top of their
  own `use_json_adapter_fallback=True`; `JSONAdapter`/`BAMLAdapter` also take
  `parallel_tool_calls` but not `native_response_types`. `dspy/adapters/base.py:30,51-74`,
  `dspy/adapters/chat_adapter.py:42-49`, `dspy/adapters/json_adapter.py:41-46`.
  [api] (verified: `inspect.signature` on the installed package) · skill:
  **wrong** — `api.md`'s surface block gives
  `dspy.ChatAdapter(callbacks=None, use_native_function_calling=False, use_json_adapter_fallback=True)`
  and the JSON/XML lines likewise, all missing `native_response_types` and
  `parallel_tool_calls`.
- **`Reasoning` is a native response type by default, not only `Citations`.**
  `_DEFAULT_NATIVE_RESPONSE_TYPES = [Citations, Reasoning]`; the skill's own prose
  ("For example, `dspy.Citations` can be populated directly…") only names Citations.
  `dspy/adapters/base.py:30`. [api] (verified: read) · skill: new.
- **The adapter pipeline runs `_call_preprocess → format → _render_request → _call_lm →
  _call_postprocess`**, not `format → LM → parse` as a flat sequence. Preprocess
  strips or wires `tools`/`tool_choice`/`parallel_tool_calls` in `lm_kwargs` and, for
  every output field whose annotation is a native-response `Type`, calls
  `field.annotation.adapt_to_native_lm_feature(signature, name, lm, lm_kwargs)`, which
  may delete that field from the signature the LM ever sees. Postprocess reassembles
  tool calls and native-typed fields after `self.parse()` runs.
  `dspy/adapters/base.py:83-135,137-207,315-348`. [api] (verified: read + traced
  against `_call_postprocess` tests) · skill: new — `api.md`'s adapter section names
  none of this internal shape, and the file's own `TODO(adapters-plan)` comments say
  it is an active, acknowledged mid-refactor (an `_AdapterPlan` is "the next stacked
  PR"), worth a caveat if the skill cites specific line numbers here.
- **`_call_preprocess` raises if a `ToolCalls` output field is declared without a
  `list[dspy.Tool]`/`dspy.Tool` input field**: `ValueError(f"You provided an output
  field {tool_call_output_field_name} to receive the tool calls information, but did
  not provide any tools as the input. …")`. It only wires native tool calling (deletes
  both fields from the formatted signature, sets `lm_kwargs["tools"]`) when
  `lm.supports_function_calling` is also true; otherwise the `ToolCalls` field stays
  in the prompt as an ordinary field. `dspy/adapters/base.py:96-121`. [api] (verified:
  read) · skill: new.
- **An empty or null LM response, with no tool calls, is `AdapterParseError`, not a
  `None`-filled Prediction**: `_call_postprocess` raises
  `AdapterParseError(..., message="The LM returned an empty or null response.")`
  exactly when `text` is falsy and there is no `(tool_calls, tool_call_output_field_name)`
  pair to fall back to. `dspy/adapters/base.py:164-177`. Confirmed end to end by
  `tests/adapters/test_chat_adapter.py:2683-2716` (`content=None` from a content
  filter, and `content=""`, both raise). [api|trap] (verified: read code + tests) ·
  skill: new.
- **When tool calls ARE present, missing/`None` text does not raise.**
  `_call_postprocess`'s other branch tries `self.parse(...)` only if
  `text and processed_signature.output_fields`, else uses `{}`, and swallows an
  `AdapterParseError` from that attempt — so a tool-call-only response with no
  free-text content parses fine. `dspy/adapters/base.py:166-170`, confirmed by
  `tests/adapters/test_chat_adapter.py:2716-2733`
  (`test_tool_call_with_null_or_missing_content_does_not_raise`). [api] (verified:
  read + test) · skill: new.
- **After `self.parse()` succeeds, every declared output field still gets a second,
  looser default pass**: `apply_output_field_defaults` then
  `value.setdefault(field_name, None)` for every field in `original_signature`. For
  `ChatAdapter`/`XMLAdapter`/`JSONAdapter`'s own `.parse()`, this is a no-op (their
  own key-mismatch check already forced every key to be present or raised). It is
  **not** a no-op on the tool-call branch: when the LM's `text` fails to parse there,
  `value = {}` and this second pass fills **every** other declared output field with
  `None`, even a required, non-Optional one with no declared default —
  silently, no error. `dspy/adapters/base.py:164-186`. [api|trap] (verified: read) ·
  skill: new.
- **`ChatAdapter` is the default, `[[ ## field ## ]]` markers ending in
  `[[ ## completed ## ]]`** — confirmed unchanged (`api.md`'s existing claim). skill: same.
- **`ChatAdapter.__call__`/`.acall()` fall back to `JSONAdapter` on *any* non-`LMError`
  exception raised anywhere in `Adapter.__call__`'s pipeline (format, request build, or
  parse), not only a parse failure** — the whole `super().__call__(...)` call is
  inside one `try`, and the `except Exception as e:` only re-raises (no fallback) when
  `isinstance(e, LMError)` or `isinstance(self, JSONAdapter)` or
  `not self.use_json_adapter_fallback`. `dspy/adapters/chat_adapter.py:77-115`.
  [api|trap] (verified: read; test-confirmed by
  `tests/adapters/test_chat_adapter.py:2339-2434`) · skill: **wrong** — `api.md` says
  "It falls back to JSONAdapter when its own parse fails", which is the common case
  but understates the actual guard (any local, non-provider exception).
- **The JSONAdapter built for the fallback inherits the *original* adapter's
  `use_native_function_calling`/`parallel_tool_calls`, not `JSONAdapter`'s own
  default (`True`)**: `_make_json_adapter_fallback` passes
  `use_native_function_calling=self.use_native_function_calling`.
  `dspy/adapters/chat_adapter.py:69-75`. Confirmed by
  `tests/adapters/test_chat_adapter.py:2361-2384`
  (`test_chat_adapter_async_fallback_preserves_native_function_calling_flag`). [api]
  (verified: read + test) · skill: new.
- **`use_json_adapter_fallback=False` fully disables the fallback and lets the
  original `AdapterParseError` propagate**; the JSONAdapter path is never even
  constructed. Confirmed by `tests/adapters/test_chat_adapter.py:2384-2399`
  (`test_chat_adapter_respects_use_json_adapter_fallback_flag` — asserts
  `JSONAdapter.__call__` is never called). [api] (verified: test) · skill: same
  (already stated as the toggle; the test is new evidence).
- **`AdapterParseError`'s constructor fields**: `adapter_name: str`, `signature:
  Signature`, `lm_response: str`, `message: str | None = None`,
  `parsed_result: str | None = None` (the annotation says `str`; every real caller
  passes a **dict** — `', '.join(parsed_result.keys())` only works on dict-like
  values, so the type hint is misleading). It inherits `DSPyError`'s
  `code`/`model`/`provider`/`provider_code`/`status`/`request_id`/`retry_after`, but
  its own `__init__` exposes none of them as parameters — `code` always resolves to
  the class default `"adapter_parse_error"`, and **`model` is always `None`** (an
  `AdapterParseError` never records which LM produced the unparseable answer). Its
  composed message **always embeds the full raw `lm_response` verbatim**, plus
  `"Expected to find output fields in the LM response: […]"`, plus, when
  `parsed_result` is given, `"Actual output fields parsed from the LM response: […]"`.
  `dspy/utils/exceptions.py:246-283`. [api|trap] (verified: constructed one directly
  and inspected `.adapter_name`/`.parsed_result`/`.code`/`.model` and `str(e)`) ·
  skill: new — relevant to this repo's logging: any code that prints or logs
  `str(exc)` on an `AdapterParseError` writes the whole model response (and, via the
  system/user message it was answering, effectively the prompt content) into that log
  line unredacted.
- **`JSONAdapter.parse()`'s per-field `parse_value` call is *not* wrapped in a
  try/except, unlike `ChatAdapter.parse()`'s.** When the LM's reply is syntactically
  valid JSON (or JSON-repairable to a dict) but one field's value fails `parse_value`
  — an off-list `Literal`, a bad enum, a pydantic-model field that doesn't validate —
  the exception that comes out of `JSONAdapter.parse()` is a **bare `ValueError` (or
  whatever `parse_value`/pydantic raises)**, not `dspy.AdapterParseError`.
  `dspy/adapters/json_adapter.py:189-191` (no try/except) vs.
  `dspy/adapters/chat_adapter.py:236-245` (wrapped). **Verified end to end**: a
  `Literal` field fed `'{"decision": "not-a-real-choice"}'` through
  `dspy.JSONAdapter().parse(sig, text)` directly raises `ValueError: 'not-a-real-choice'
  is not one of (...)`; run through `dspy.Predict(sig)` with `dspy.context(adapter=
  dspy.JSONAdapter())` and an offline `FixtureLM` answering the same bad JSON twice
  (structured-output attempt, then `JSONAdapter.__call__`'s own retry in loose
  `json_object` mode — see next item), the **second** attempt's `ValueError` is not
  caught by anything in `JSONAdapter.__call__`/`ChatAdapter.__call__`'s fallback logic
  and reaches the caller as a bare `ValueError`. [api|trap] (verified: ran both the
  direct and end-to-end probe on `.venv-dspy`) · skill: **new, and this repository's
  most load-bearing finding in this slice** — `lmrun.call` is described (`api.md`,
  `SKILL.md` item 7) as catching `AdapterParseError` and recording `unparsed`; a
  Literal value that fails inside otherwise-valid JSON from a `JSONAdapter` call (or
  from **`ChatAdapter`'s own JSON fallback**, which is on by default) would not be
  caught that way and would surface as an uncaught `ValueError` instead. This
  repository's scripts use `ChatAdapter` with `Literal` fields — exactly the
  configuration where the fallback can reach this path.
- **`JSONAdapter.__call__` tries up to three shapes of the request before giving up**:
  (1) if `"response_format" not in lm.supported_params`, it just calls
  `ChatAdapter`'s own text-marker pipeline with no JSON at all; (2) else if the
  signature has an open-ended `dict[...]` output field, or `ToolCalls` is present
  without native function calling, or `not lm.supports_response_schema`, it sets
  `lm_kwargs["response_format"] = {"type": "json_object"}` (loose JSON mode); (3)
  otherwise it builds a strict, `extra="forbid"` Pydantic model via
  `_get_structured_outputs_response_format` and sets `response_format` to that model
  **class** (not a dict). If step 3's call raises anything other than `LMError`
  (including a local `AdapterParseError` from its own `.parse()`), it logs
  `"Failed to use structured output format, falling back to JSON mode."` and retries
  **once more** in loose `json_object` mode. `dspy/adapters/json_adapter.py:55-93`.
  [api] (verified: read; the "does not fall back on a real LM/network error" half
  confirmed by `tests/adapters/test_json_adapter.py:1323-1341`, which asserts
  `mock_completion.call_count == 1` when `litellm.completion` itself raises) · skill:
  new — `api.md` says only "JSONAdapter uses native structured output where the
  provider has it", with no mention of the three-tier fallthrough or the extra retry
  call this can cost.
- **`_get_structured_outputs_response_format` strips DSPy's own field descriptions
  from the schema it sends as `response_format`**, and forces every schema level
  (recursively, including `$defs`/`definitions` and array items) to list every
  property in `"required"` and set `"additionalProperties": false`, to satisfy OpenAI
  Structured Outputs' constraint that there is no true optionality in strict mode
  (`extra="forbid"`, `pydantic.create_model("DSPyProgramOutputs", ...)`).
  `dspy/adapters/json_adapter.py:233-311`. [api] (verified: read) · skill: new.
- **`ChatAdapter.format_field_structure`'s exact per-field template**: for output
  field `X` with a non-`str`, non-`Reasoning` type, the structure block literally
  contains `{X}` followed by an 8-space-indented `# note: the value you produce
  must …` line, whose text is: `bool`→"must be True or False"; `int`/`float`→"must be
  a single {type} value"; `Enum`→"must be one of: {v1; v2; …}" (using `.value`); a
  `Literal[...]`→**"must exactly match (no extra characters) one of:
  {"a"; "b"; …}"** (quoted per-value, choosing single vs. double quotes to avoid an
  escaping clash — `_quoted_string_for_literal_type_annotation`); a `Code` type with a
  non-empty `.description()`→no note at all (its own description carries the schema);
  anything else→"must adhere to the JSON schema: {schema, with `"type"` moved to the
  front of each object for readability}". `dspy/adapters/utils.py:131-156,317-336`.
  Verified end to end: built `SameTerm` (this repo's `pairs.py` shape — German
  docstring, `Literal["one-term","two-terms"]` output) and printed
  `ChatAdapter().format_system_message(SameTerm)` — the `decision` field renders as
  `{decision}\n        # note: the value you produce must exactly match (no extra
  characters) one of: one-term; two-terms`. [api|number] (verified: ran on
  `.venv-dspy`) · skill: new — this is the exact text behind `api.md`'s
  `literal-out-of-set-unparsed` claim, not previously spelled out.
- **`get_annotation_name` special-cases `Reasoning` to render as the string `"str"`**
  in every field-type label a model reads — "Keep backward compatibility with the old
  behaviour in `dspy.ChainOfThought`, where reasoning field type is treated as a
  string." `dspy/adapters/utils.py:239-250`. [api] (verified: read) · skill: new.
- **`format_task_description`'s exact shape**: `textwrap.dedent(signature.instructions)`,
  then each line joined with `"\n" + " "*8`, prefixed by `""`, wrapped as
  `f"In adhering to this structure, your objective is: {objective}"`. For a
  multi-line German docstring (as this repo's `SameTerm` uses), every line after the
  first is indented 8 spaces in the actual system message sent to the model.
  `dspy/adapters/chat_adapter.py:145-148`. [api|number] (verified: read + reproduced
  in the probe above) · skill: new.
- **`format_user_message_content`'s output-format reminder is appended only to the
  *current* (`main_request=True`) user turn — never to a demo's or a history turn's
  user message.** `dspy/adapters/chat_adapter.py:150-171` (`main_request` defaults
  `False`; only the top-level call in `Adapter.format` passes `True`). [api]
  (verified: read) · skill: new.
- **`ChatAdapter.user_message_output_requirements`'s exact text**: "Respond with the
  corresponding output fields, starting with the field `` `[[ ## f1 ## ]]` ``
  `<type_info>`, then `` `[[ ## f2 ## ]]` `` `<type_info>`, …, and then ending with the
  marker for `` `[[ ## completed ## ]]` ``." where `<type_info>` is
  `' (must be a JSON object like {"tool_calls": [{"name": "...", "args": {...}}]})'`
  for a `ToolCalls` field, `" (must be formatted as a valid Python <name>)"` for any
  other non-`str` type, or nothing for `str`. `dspy/adapters/chat_adapter.py:173-202`.
  [api] (verified: read; matches the worked example in
  `docs/docs/learn/programming/adapters.md:74`) · skill: new.
- **`ChatAdapter.format_demos` silently drops a demo that has neither an input field
  nor an output field in common with the signature** — it is neither "complete" nor
  "incomplete" by the function's own test (`has_input and has_output`), so it never
  reaches `messages` at all, with no warning. A demo missing *some* fields (but at
  least one input and one output) is kept, prefixed "This is an example of the task,
  though some input or output fields are not supplied." and its missing fields
  rendered as the literal text `"Not supplied for this particular example. "`.
  `dspy/adapters/base.py:542-602`. [api|trap] (verified: read) · skill: new.
- **`ChatAdapter.parse()`'s exact mechanics**: splits `completion` into `(header,
  lines)` sections on `field_header_pattern = re.compile(r"\[\[ ## (\w+) ## \]\])")`
  matched against each **stripped** line (so trailing text on the marker's own line
  becomes the section's first content line); only the **first** occurrence of a
  recognised header populates that field (`if (k not in fields) and (k in
  signature.output_fields)`); any header **not** in `signature.output_fields` — and
  any preamble text before the first header — is silently discarded, never raising.
  Each field value is parsed by the shared `parse_value`; a parse failure there
  raises `AdapterParseError(message=f"Failed to parse field {k} with value {v} …")`.
  After `apply_output_field_defaults`, if the resulting key set doesn't exactly equal
  `signature.output_fields.keys()`, raises a **second, differently-shaped**
  `AdapterParseError` — this one carries `parsed_result=fields` and no custom
  `message=`. `dspy/adapters/chat_adapter.py:219-255`. [api] (verified: read; the
  literal-out-of-set path confirmed live via `FixtureLM`) · skill: same/expanded (the
  skill already has the "unparseable → AdapterParseError" fact; this adds the two
  distinct shapes and the silent-header-discard behaviour).
- **`parse_value`'s full strategy, in order**: `str` → `str(value)` (never fails);
  `enum.EnumMeta` → `find_enum_member` (checks member **values** first, then
  **names**, raising `ValueError(f"{identifier} is not a valid name or value for the
  enum {enum.__name__}")` for neither); `Literal` → checks `value in allowed` first
  (case-sensitive `in`), and only on a `str` miss tries stripping whitespace, a
  wrapping `Literal[...]`/`str[...]` prefix, and one layer of matching quote
  characters before re-checking membership — so `"Literal[one-term]"` or
  `'"one-term"'` both still parse, but anything else raises
  `ValueError(f"{value!r} is not one of {allowed!r}")`; a non-`str` value goes
  straight to `TypeAdapter(annotation).validate_python(value)`; `Optional[str]`/`str |
  None` (specifically, a Union containing both `NoneType` and `str`) also validates
  the raw string directly, no JSON step; otherwise: `json_repair.loads(value)`
  (returns `""` on failure) → on failure, `ast.literal_eval(value)` → on failure, the
  raw string itself → `TypeAdapter(annotation).validate_python(candidate)`; if *that*
  raises `pydantic.ValidationError` **and** the annotation is a `dspy.Type` subclass,
  one more retry validates the **original, un-repaired** string (so a custom type's
  own validator gets a chance). `dspy/adapters/utils.py:187-236`. [api] (verified:
  read; every branch confirmed by `tests/adapters/test_adapter_utils.py` — parametrized
  cases for quoted/`Literal[...]`-wrapped literals, `Optional`/`Union` fallback to
  `str`, dict via `json_repair` then `ast.literal_eval`, and a malformed-string
  failure case) · skill: expanded — `api.md` only says "Literal … enforced at parse
  time" and "Pydantic types work through the default adapter"; this is the actual
  algorithm, including the quote/`Literal[...]` tolerance and the dspy.Type retry.
- **A number in a model's answer can carry Python-style underscore digit
  separators and still parse.** After `json-repair >= 0.54.1` (installed here:
  0.63.5), `json_repair.loads('{"score": 123_456.789}')` treats `123_456.789` as the
  float `123456.789` — confirmed by
  `tests/adapters/test_chat_adapter.py:2620-2646`
  (`test_chat_adapter_parses_float_with_underscores`), whose own docstring names the
  version. [api|number] (verified: read test; confirmed `json_repair==0.63.5` in
  `.venv-dspy`) · skill: new.
- **`XMLAdapter` is a subclass of `ChatAdapter`, not a peer** — it declares no
  `__init__` of its own, so it takes the same five parameters (including
  `use_json_adapter_fallback=True`) and falls back to `JSONAdapter` the same way on
  any non-`LMError` exception. `dspy/adapters/xml_adapter.py:23`. [api] (verified:
  `inspect.signature`; `"__init__" in dspy.XMLAdapter.__dict__` is `False`) · skill:
  **wrong** — `api.md`'s surface line
  `dspy.XMLAdapter(callbacks=None, use_native_function_calling=False,
  use_json_adapter_fallback=True)` implies a standalone constructor and, like the
  ChatAdapter line, omits `native_response_types`/`parallel_tool_calls`.
- **`XMLAdapter` has a whole nested-XML rendering/parsing subsystem the skill doesn't
  mention at all.** An output field whose type is `list`, `dict`, a `TypedDict`, or a
  Pydantic `BaseModel` that is **not** itself defined in the `dspy.` package
  (`_uses_nested_xml`) gets rendered as genuine nested tags —
  `_value_to_xml`/`_xml_schema`/`_schema_to_xml` walk the field's `TypeAdapter(...)
  .json_schema()`, resolving `$ref`s with a `seen` set to cut infinite recursion
  (replacing a repeat with `<tag>...</tag>`), and a dict key that is not a valid
  Python identifier is written as `<entry key="...">` instead of `<key>`. Plain
  scalars (`str`/`int`/`Literal`/enum, and any Pydantic model that **is** a `dspy.`
  type, e.g. `dspy.Image`) fall through to the same
  `format_field_value`/`translate_field_type` text ChatAdapter uses, wrapped in
  `<field>…</field>`. There is **no `[[ ## completed ## ]]` marker for XMLAdapter** —
  `format_field_structure` never emits one. `dspy/adapters/xml_adapter.py:24-93,
  137-240`. [api] (verified: read) · skill: new.
- **`XMLAdapter.parse()` wraps the whole completion in a synthetic
  `<dspy_root>…</dspy_root>` and runs `xml.etree.ElementTree.fromstring` on it** — a
  bare, unescaped `&` or `<`/`>` **anywhere in the raw text**, including inside a
  model's own chain-of-thought prose *outside* any field tag, breaks the parse for
  the **entire** response with `AdapterParseError(message=f"Failed to parse XML:
  {e}")`. An output field simply absent from the top-level elements is silently
  skipped (`continue`), not an immediate error — it only surfaces later if
  `apply_output_field_defaults` can't fill it. `dspy/adapters/xml_adapter.py:95-129`.
  [api|trap] (verified: read) · skill: new.
- **`TwoStepAdapter`'s stage-1 prompt has no field markers, no output-format
  instruction, and its own separate system-message builder** (`format()` is
  overridden entirely — `format_system_message`/`format_field_description`/
  `format_field_structure` are never called for it). Its demos and current input are
  plain `"{name}: {value}"` lines, one per field, joined by blank lines — no
  `[[ ## ## ]]`, no JSON. `dspy/adapters/two_step_adapter.py:49-76,192-220`. Exact
  system message for a plain `question -> answer` signature, verbatim from the test
  suite: `"You are a helpful assistant that can solve tasks based on user input.\nAs
  input, you will be provided with:\n1. \`question\` (str):\nYour outputs must
  contain:\n1. \`answer\` (str):\nYou should lay out your outputs in detail so that
  your answer can be understood by another agent\nSpecific instructions: Given the
  fields \`question\`, produce the fields \`answer\`."` —
  `tests/adapters/test_two_step_adapter.py:9-30`. [api] (verified: read + test) ·
  skill: expanded — `api.md` has the "demo-less second stage" fact but nothing about
  stage 1's own prompt shape.
- **`TwoStepAdapter.acall` is a hand-rolled reimplementation that bypasses
  `_call_preprocess`/`_render_request`/`_call_lm` entirely** (it calls `self.format(...)`
  and `lm.acall(...)` directly). Consequently: (a) `use_native_function_calling` and
  `native_response_types` configured on the adapter have **no effect on the async
  path** — there is no equivalent of `_call_preprocess`'s tool-list wiring, so a
  `list[dspy.Tool]` input field is never turned into `lm_kwargs["tools"]` for
  `acall`; (b) tool-call reconstruction is done manually, keying off whatever
  `output.get("tool_calls")` the LM returned regardless of
  `self.use_native_function_calling`. The **sync** `__call__` (inherited, unoverridden
  from `Adapter`) does go through the normal pipeline. `dspy/adapters/two_step_adapter.py:
  43-47,114-176`. [api|trap] (verified: read) · skill: new.
- **`TwoStepAdapter`'s extraction stage always constructs a *fresh* `ChatAdapter()`**,
  never `self` or any adapter the caller configured — so even a `TwoStepAdapter`
  built with custom `native_response_types` won't propagate them to the extractor.
  Its own module docstring: "The main issue below is that the second step's signature
  is entirely created on the fly and is invoked with a chat adapter explicitly
  constructed with no demonstrations. This means that it cannot 'learn' or get
  optimized." `dspy/adapters/two_step_adapter.py:14-19,93-102,141-150`. [api] (verified:
  read) · skill: same (already cited by `api.md`).
- **`TwoStepAdapter`'s extraction step can itself cost two LM calls** (the fresh
  `ChatAdapter()` has `use_json_adapter_fallback=True` by default), so a TwoStepAdapter
  call is 1 (main) + up to 2 (extractor, with its own JSON fallback) = up to 3 real LM
  calls, not 2. `dspy/adapters/two_step_adapter.py:93-112`. [api|number] (verified:
  read, arithmetic on the traced call graph) · skill: new.
- **`BAMLAdapter` subclasses `JSONAdapter`, not `ChatAdapter` or `Adapter`.** It
  inherits `JSONAdapter`'s `__init__` (so `use_native_function_calling=True` by
  default, same as plain `JSONAdapter`), its structured-output/loose-JSON `__call__`
  logic unchanged, and its `.parse()` unchanged (still `json_repair`-based). It
  overrides **only** `format_field_structure` and `format_user_message_content`.
  `dspy/adapters/baml_adapter.py:163`. [api] (verified: `inspect.signature`; confirmed
  no own `__init__` in `BAMLAdapter.__dict__`) · skill: expanded — `api.md` only has
  the import-path fact ("not a top-level name").
- **`BAMLAdapter`'s field-structure text is a hybrid**: `[[ ## name ## ]]` markers
  (like ChatAdapter) around a compact, BAML-style type description — a Pydantic model
  renders as an indented `{ field: type, }` block with the model's docstring and each
  field's `description` (or, absent that, its `alias`) as `#`-prefixed comments;
  `Optional[T]` → `"T or null"`; `Literal[...]` → `"\"a\" or \"b\""`; `list[Model]` →
  a bracketed multi-line block, `list[scalar]` → `"T[]"`; `dict[K,V]` →
  `"dict[K, V]"`. Comment symbol is `#` on purpose — "Changing the comment symbol to
  Python's `#` rather than other languages' `//` seems to help" (an unverifiable
  empirical claim in the code, not a measured fact). Input fields in the structure
  section get **no** type note at all, just the bare `{name}` placeholder, regardless
  of type — unlike `ChatAdapter`/`JSONAdapter`, which append a note for any non-`str`
  input too. `dspy/adapters/baml_adapter.py:17-18,21-160,212-239`. [api|claim for the
  comment-symbol line] (verified: read; exact system-message text confirmed by
  `tests/adapters/test_baml_adapter.py:55-84`) · skill: new.
- **`BAMLAdapter` raises at *format* time (before any LM call) on a self-referential
  Pydantic model**: `ValueError("BAMLAdapter cannot handle recursive pydantic models,
  please use a different adapter.")`, tracked via a `seen_models` set walked while
  building the schema. `dspy/adapters/baml_adapter.py:103-107`. [api] (verified: ran
  `BAMLAdapter().format_field_structure(sig)` on a self-referential `Node` model —
  raised exactly this message with no LM configured) · skill: new.
- **`BAMLAdapter`'s own module docstring example calls `dspy.OpenAI(model=...)`**,
  which does not exist on 3.3.1 (confirmed `hasattr(dspy, "OpenAI")` is `False`,
  matching `api.md`'s "Names that moved" table) — the adapter's own usage example is
  stale as written. `dspy/adapters/baml_adapter.py:198`. [trap] (verified: ran) ·
  skill: new (a concrete instance of the already-known `dspy.OpenAI` removal, inside
  code this slice reads).
- **`History` is a plain, frozen `pydantic.BaseModel`, not a `dspy.Type`** —
  `messages: list[dict[str, Any]]`, `frozen=True, str_strip_whitespace=True,
  validate_assignment=True, extra="forbid"`. It never goes through the
  `Type.serialize_model`/marker mechanism; the adapter detects and expands it by a
  dedicated code path (`_get_history_field_name`/`format_conversation_history`), not
  the generic custom-type pipeline. `dspy/adapters/types/history.py:6-68`. [api]
  (verified: read) · skill: same (the `extra="forbid"` detail is new — an unknown
  kwarg to `dspy.History(...)` is a hard pydantic error, not silently dropped).
- **`format_conversation_history` also reconstructs tool-call turns.** When
  `self.use_native_function_calling` is true and a history message carries a
  `ToolCalls`-shaped value, it rebuilds the OpenAI-style
  `assistant` (with `tool_calls=[...]`) / `tool` (one per result, keyed by
  `tool_call_id`) turn pair — replaying earlier tool calls and their results as
  genuine provider tool messages, not text. If the recorded `tool_call_results`' ids
  don't line up 1:1 with the turn's `tool_calls` ids, the results are dropped for
  that turn (`tool_call_results = None`) rather than sent mismatched.
  `dspy/adapters/base.py:626-712`. [api] (verified: read) · skill: new — `patterns.md`'s
  and `api.md`'s History sections only describe the plain field-replay case, not
  native-tool-call history replay (also exercised by
  `tests/adapters/test_chat_adapter.py:1233-1455`, not read in full here).
- **A keyword the signature doesn't declare is dropped with a `logging` call, not a
  `warnings.warn`** — confirmed unchanged; `-W error` still would not catch it. skill:
  same (already in `api.md`).
- **`Tool(func, ...)` auto-infers `name`/`desc`/`args`/`arg_types`/`arg_desc` from the
  function's signature and docstring** when not given explicitly, building each arg's
  JSON schema via `TypeAdapter(hint).json_schema()` (or `.model_json_schema()` for a
  Pydantic-typed arg), with `$ref`s resolved inline
  (`_resolve_json_schema_reference`), a schema `"default"` key added when the
  parameter has one, and `has_kwargs` recording whether the function accepts
  `**kwargs` (which relaxes `_validate_and_parse_args` to allow any extra keyword).
  `dspy/adapters/types/tool.py:25-151`. [api] (verified: read) · skill: new (the
  skill's `Tool` coverage is limited to the surface line and the async-swallow trap).
- **A plain `Tool` used as an input value (not via native function calling) renders
  as plain text, not JSON, and is never wrapped in the custom-type markers** —
  `Tool.format()` returns `str(self)`:
  `f"{name}, whose description is <desc>{desc}</desc>. It takes arguments {args}."`
  (or `f"{name}."` with no description); because this is a plain `str`, not a list,
  `Type.serialize_model` never applies the `<<CUSTOM-TYPE-START-IDENTIFIER>>` marker
  to it. `dspy/adapters/types/tool.py:153-154,267-273`,
  `dspy/adapters/types/base_type.py:70-77`. [api] (verified: read) · skill: new.
- **`format_as_litellm_function_call`'s `"required"` list is every arg whose schema
  entry lacks a `"default"` key** — `[k for k in self.args if "default" not in
  self.args[k]]`. `dspy/adapters/types/tool.py:156-168`. [api] (verified: read) ·
  skill: new.
- **`Tool.__call__` (sync) raises a specific `ValueError` when the wrapped function is
  async and `settings.allow_tool_async_sync_conversion` is not set**: "You are
  calling `` `__call__` `` on an async tool, please use `` `acall` `` instead or
  enable async-to-sync conversion with `` `dspy.configure
  (allow_tool_async_sync_conversion=True)` `` or `` `with dspy.context
  (allow_tool_async_sync_conversion=True):` ``." With the setting on, it runs the
  coroutine via `asyncio.run` or, inside a running loop, on a fresh one-worker
  thread. `dspy/adapters/types/tool.py:170-194`. [api] (verified: ran directly — the
  `ValueError` fires with the setting off and the call succeeds with it on; also
  `tests/adapters/test_tool.py:400-408`) · skill: expanded — `api.md`'s
  `react-async-tool-swallowed` trap describes the *observable* effect through
  `ReAct` (the tool's failure "becomes the step's observation text"); this is the
  concrete exception `Tool.__call__` itself raises, which some caller (not read in
  this slice) must be catching to produce that observation text.
- **`ToolCall`'s and `ToolCalls`' generated JSON schemas hide bookkeeping fields from
  the model**: a custom `__get_pydantic_json_schema__` strips `id` out of
  `ToolCall`'s `properties`/`required`, and `tool_call_results` out of `ToolCalls`' —
  a model asked to produce a `ToolCalls` value is never asked to invent an id or echo
  back results. `dspy/adapters/types/tool.py:282-292,345-355`. [api] (verified: read) ·
  skill: new.
- **`ToolCalls.validate_input` (a pydantic `model_validator(mode="before")`) accepts a
  bare list of call-shaped dicts, a dict with a `"tool_calls"` key, or a single
  call-shaped dict** (auto-wrapped into a one-item list), and normalises both
  DSPy-shaped (`{"name","args"}`) and provider-shaped (`{"function":{"name",
  "arguments"}}`) dicts, including a stringified `arguments` repaired via
  `json_repair`. Anything else raises `ValueError(f"Received invalid value for
  \`dspy.ToolCalls\`: {data}")`. `dspy/adapters/types/tool.py:403-431,490-514`. [api]
  (verified: read) · skill: new.
- **`ToolCalls.description()`'s exact text** (shown as the field's custom-type
  description whenever native function calling is off but a `ToolCalls` output field
  is still declared): `"Tool calls must be a JSON object with \`tool_calls\`, a list
  of calls. Each call must include \`name\` and \`args\`. Example:
  {"tool_calls": [{"name": "search", "args": {"query": "cats"}}]}"`.
  `dspy/adapters/types/tool.py:380-386`. [api] (verified: read) · skill: new.
- **`Citations.adapt_to_native_lm_feature` only activates for `lm.model.startswith
  ("anthropic/")`** — on any other provider, a `Citations` output field is left in
  the signature as an ordinary field: rendered with its `.description()` text
  ("Citations with quoted text and source references. Include the exact text being
  cited and information about its source.") and expected to come back as parseable
  JSON matching the `Citation` schema, with no native help at all.
  `dspy/adapters/types/citation.py:170-179`. [api] (verified: read;
  `tests/adapters/test_citation.py:128-164` shows the Anthropic branch: the field is
  deleted from the formatted signature and `Citations.parse_lm_response` reads a
  top-level `output["citations"]` key the raw response carries) · skill: new — the
  skill's only Citations mention (`api.md`, one line) doesn't say this is
  provider-gated.
- **`Reasoning.adapt_to_native_lm_feature`'s exact resolution order and one
  hard-coded provider carve-out**: `reasoning_effort` comes from
  `lm_kwargs["reasoning_effort"]`, else `lm.kwargs["reasoning_effort"]`, else
  defaults to `"low"` **just because a `Reasoning` field is present** (native
  reasoning turns on by default, unasked). If that resolves to `None`, or
  `not lm.supports_reasoning`, the field stays a plain prompted field. There is a
  named exception: `if "gpt-5" in lm.model and lm.model_type == "chat": return
  signature` unchanged — "a caveat of Litellm as 1.79.0 that when using the chat
  completion API on GPT-5 family models, the reasoning content is not available in
  the response" (cites `github.com/BerriAI/litellm/issues/14748`). Otherwise it sets
  `lm_kwargs["reasoning_effort"]` and deletes the field from the formatted signature.
  `dspy/adapters/types/reasoning.py:45-77`. [api|number] (verified: read; end-to-end
  reasoning parse confirmed by `tests/adapters/test_json_adapter.py:1573-1602`, which
  mocks `message.reasoning_content` and asserts `result[0]["reasoning"] ==
  dspy.Reasoning(content=...)`) · skill: new — this is exactly the "native reasoning
  of reasoning models" the brief asks about, and none of it is in the skill today.
- **`dspy.Reasoning` is *not* a `str` subclass, and `dspy.ChainOfThought`'s own
  `reasoning` field is a plain `str` by default, not `dspy.Reasoning`.**
  `issubclass(dspy.Reasoning, str)` is `False`. `ChainOfThought.__init__`'s
  `rationale_field_type: type = str` (default). Its file carries the comment
  `"NOTE: This restores the legacy rationale_field behavior after PR #8822."` —
  i.e. DSPy at some point made `dspy.Reasoning` the *default* rationale type and then
  reverted it. `dspy.Reasoning.__getattr__` still carries a helpful error for anyone
  who *does* opt in (via `rationale_field_type=dspy.Reasoning` or a custom
  `rationale_field=`) and then hits a non-string-method attribute: `` `Reasoning`
  object has no attribute '<name>'. If you are using `dspy.ChainOfThought`, note that
  the 'reasoning' field in ChainOfThought is now a `dspy.Reasoning` object (not a
  plain string). You can convert it to a string with str(reasoning) or access the
  content with reasoning.content. `` `dspy/predict/chain_of_thought.py:9,36-50`,
  `dspy/adapters/types/reasoning.py:149-170`. [api|trap] (verified: ran both checks;
  confirmed by `tests/adapters/test_reasoning.py:90-104`, whose own
  `test_reasoning_with_chain_of_thought` asserts `isinstance(result.reasoning, str)`)
  · skill: new — reconciles what looked, from the error message alone, like a
  contradiction; it is a genuine versioned reversal, and any code (or future skill
  text) that assumes `ChainOfThought`'s `reasoning` is `dspy.Reasoning` by default
  would be wrong today.
- **`Reasoning` is `str`-like by design**: `__getattr__` forwards any name that
  `hasattr(str, name)` to `self.content` (so `.strip()`, `.lower()`, `.split()`, …
  all work), and it separately overrides `__eq__` (compares equal to a plain `str`),
  `__len__`, `__getitem__`, `__contains__`, `__iter__`, `__add__`/`__radd__`
  (mixed `Reasoning`+`str` concatenation returns `str`; `Reasoning`+`Reasoning`
  returns `Reasoning`). `dspy/adapters/types/reasoning.py:107-170`. [api] (verified:
  read; every operator confirmed by `tests/adapters/test_reasoning.py:6-88`) · skill:
  new.
- **`Image`'s constructor is now positional-source-only and never touches
  network/filesystem on its own.** `Image(source=None, /, *, download=_UNSET,
  verify=_UNSET, **data)`. Passing `download=`/`verify=` **without** a positional
  `source` (e.g. from a dict routed through pydantic validation) raises `TypeError`
  outright — the code's own comment: "pydantic routes dict data into `__init__`, so
  an untrusted value such as `{"url": "http://169.254.169.254/...", "download":
  true}` would otherwise trigger a server-side fetch during output parsing.
  Requiring a positional source keeps the shim reachable only from direct developer
  construction." Passing them positionally still works but warns
  `DeprecationWarning` (removed in 3.4). Ordinary construction from a string just
  classifies it as a data URI or an `http`/`https`/`gs` URL reference (`is_url`) and
  keeps it as-is — no download. A non-data, non-URL string raises `ValueError(
  f"Unrecognized image string: {image}. Local files must be loaded with
  Image.from_path().")`. `dspy/adapters/types/image.py:24-105,166-222`. [api|trap]
  (verified: read; matches `docs/docs/diving-deeper/adapters.md:156-173`'s migration
  table exactly, and this repository has no code touching `dspy.Image`) · skill:
  expanded — `api.md` already cites the `from_path()` error message; this adds the
  SSRF-motivated constructor redesign, which is new and load-bearing security
  context.
- **A whole dedicated test file exists for exactly this property**:
  `tests/adapters/test_resource_loading.py` parametrizes attacker-shaped locator
  inputs (`/etc/passwd`, `https://evil.example/...`) across `Image`/`Audio`/`File`
  and asserts **neither construction nor `TypeAdapter(...).validate_python(...)`**
  (the path adapters use to coerce untrusted LM output) ever calls `open()` or
  `requests.get` — patched to `pytest.fail` if they do.
  `tests/adapters/test_resource_loading.py:9-56`. [test|trap] (verified: read) ·
  skill: new.
- **`Image.is_url` accepts `http`/`https`/`gs` schemes, but `Image.from_url`/
  `_is_http_url` (the actual-download path) accepts only `http`/`https`** — a
  `gs://...` reference is a valid, retained `Image` value but can never be
  downloaded through `.from_url()` (raises `ValueError(f"Image.from_url requires an
  HTTP(S) URL, received: {url}")`). `dspy/adapters/types/image.py:115-127,166-181`.
  [api|trap] (verified: read) · skill: new.
- **`Image.format()` is `@lru_cache(maxsize=32)`**, a cache shared across **all**
  `Image` instances in the process (not per-instance) since `Image` is frozen and
  therefore hashable by its fields; a failing `.format()` call (wrapped as
  `ValueError(f"Failed to format image for DSPy: {e}")`) is never cached, since
  `functools.lru_cache` doesn't cache exceptions. `dspy/adapters/types/image.py:
  107-113`. [api|trap] (verified: read) · skill: new.
- **`Image.from_url`/`Audio.from_url` default `timeout=30.0` even when the caller
  doesn't pass one; `timeout=None` disables it and can hang indefinitely** — both
  confirmed by `tests/adapters/test_resource_loading.py:147-170`
  (`test_from_url_applies_a_timeout_by_default`, parametrized over both types).
  Matches `api.md`'s surface line. [api] (verified: test) · skill: same.
- **`Audio` validates the downloaded/read MIME type actually starts with `"audio/"`
  and raises otherwise; `Image` performs no such family check** at all — it trusts
  whatever `Content-Type` (or extension-guessed type) it gets.
  `dspy/adapters/types/audio.py:82-135`, `dspy/adapters/types/image.py:239-262`.
  [api|trap] (verified: read) · skill: new.
- **`File` has no `from_url` at all** — only `from_path`, `from_bytes`,
  `from_file_id`, unlike `Image`/`Audio` which both have `from_url`.
  `dspy/adapters/types/file.py:114-160`. [api] (verified: read) · skill: new.
- **`dspy.experimental.Document` sets no `model_config` at all**, unlike
  `Image`/`Audio`/`File`/`History` (all `frozen=True`, mostly `extra="forbid"`) — a
  `Document` instance is **mutable** (pydantic's default) and **silently drops an
  unknown constructor keyword** instead of raising (pydantic's default `extra=
  "ignore"`). `dspy/adapters/types/document.py` (whole file — no `model_config`
  anywhere). [api|trap] (verified: constructed one with a bogus kwarg — no error,
  attribute absent — and mutated `.data` post-construction — succeeded) · skill: new.
- **`Document.format()`'s `citations.enabled` is hard-coded `True`, with no field to
  turn it off** — every `Document` used as an input always requests citation-enabled
  document blocks from the provider. `dspy/adapters/types/document.py:61-83`,
  confirmed by `tests/adapters/test_document.py:39-57`. `media_type` is a
  `Literal["text/plain", "application/pdf"]` — nothing else validates. [api] (verified:
  read + test) · skill: new.
- **`@experimental(version="3.0.4")` (decorating `Citations` and `Document`) only
  edits the docstring** — it prepends "Experimental: This class may change or be
  removed in a future release without warning (introduced in v3.0.4)." and does
  **not** emit any runtime warning, unlike the `DeprecationWarning`s on
  `Image.from_file`/`Image.from_PIL`/`Audio.from_file`/the deprecated
  `download=`/`verify=` constructor path. `dspy/utils/annotation.py:19-71`. [api]
  (verified: read) · skill: new.
- **`Code["python"]`/`Code["java"]` subscript syntax is a module-level monkey-patch**,
  not a class-body `__class_getitem__`: `Code.__class_getitem__ =
  classmethod(_code_class_getitem)`, and each subscript call builds a **fresh**
  `pydantic.create_model(...)` subclass with `language` set as a `ClassVar` — two
  calls with the same language string produce two distinct classes.
  `dspy/adapters/types/code.py:66-68,124-131`. [api] (verified: read) · skill: new.
- **`dspy.Code(...)`'s validator auto-strips markdown code fences from any string it
  is constructed from** (whether a plain construction or parsing a model's answer),
  extracting only the fenced block's content (or the raw text, if no fence is
  found) — `_filter_code` handles ` ```lang\n…\n``` `, bare ` ```…``` `, and text with
  prose before/after the fence. `dspy/adapters/types/code.py:86-121`, confirmed by
  `tests/adapters/test_code.py:48-63`. `Code.description()` exact text: "Code
  represented in a string, specified in the `code` field. If this is an output
  field, the code field should follow the markdown code block format, e.g.
  \n```{language}\n{code}\n```\nProgramming language: {language}" — and because
  `translate_field_type` special-cases `Code` types with a non-empty description to
  show no separate "note:" text, the whole field-structure block for a `Code` output
  field is just this description string. `dspy/adapters/types/code.py:78-84`,
  `dspy/adapters/utils.py:149-151`. [api] (verified: read + test) · skill: new.
- **The custom-type marker pipeline only rewrites `role == "user"` messages, and only
  where the content is a plain string containing the marker.** An `assistant`-role
  message (a demo's or history's output value, if it happens to be an `Image`/
  `Audio`/`File`/`Document`) is never split into multipart content — it stays literal
  marker text. `dspy/adapters/_legacy_type_markers.py:15-37`. [api|trap] (verified:
  read) · skill: new.
- **`dspy.adapters.types.base_type.split_message_content_for_custom_types` is dead
  code** — fully implemented, fully docstringed, does the same conceptual job as
  `_legacy_type_markers.py`'s pair of `_expand_legacy_custom_type_markers_in_*`
  functions, but is called from nowhere in `dspy/` or `tests/`, and is not
  mentioned in any doc in this slice. `dspy/adapters/types/base_type.py:135-209`
  (grep confirms zero other references). [trap] (verified: grepped the whole
  package and the docs tree) · skill: new.
- **The `Type` base class's native-feature hooks — `is_streamable()`,
  `parse_stream_chunk()`, `parse_lm_response()`, `adapt_to_native_lm_feature()` — are
  only overridden by `Citations` and `Reasoning`.** Every other custom type (`Image`,
  `Audio`, `File`, `Code`, `Tool`, `ToolCalls`, `History`) uses the base defaults
  (`is_streamable()` False, the rest no-ops/`None`) — none of them stream, and none
  has a native-LM path. `dspy/adapters/types/base_type.py:104-132` cross-checked
  against every other type file. [api] (verified: grepped for overrides across the
  whole `dspy/` tree) · skill: new.

## AGENT

- **`Tool.from_mcp_tool(session, tool, result_mode="text"|"structured")`**
  delegates to `dspy.utils.mcp.convert_mcp_tool` (outside this slice); `"text"`
  preserves the old text/non-text conversion, `"structured"` prefers MCP structured
  content when present. `dspy/adapters/types/tool.py:206-229`. [api] (verified:
  read) · skill: expanded (skill only has the bare surface line).
- **`convert_input_schema_to_tool_args` (used when building a `Tool` from a raw JSON
  input schema, e.g. an MCP tool) maps schema `"type"` to Python types through a
  tiny, lossy table**: `{"string": str, "integer": int, "number": float, "boolean":
  bool, "array": list, "object": dict}`, defaulting to `Any` for anything else
  (including `"null"`), and appends `" (Required)"` to `arg_desc` for a required
  property. `dspy/adapters/types/tool.py:18,543-572`. [agent|api] (verified: read) ·
  skill: new.
- **`use_native_function_calling` is only referenced inside `dspy/adapters/`** — it
  has nothing to do with `dspy.ReAct`'s own tool loop, which is a separate mechanism.
  It only matters for a signature that itself declares a `list[dspy.Tool]` input
  field and a `dspy.ToolCalls` output field. (grepped across `dspy/`; the only hits
  are `dspy/adapters/base.py:110` and the adapter constructors.) [agent|api]
  (verified: grep) · skill: new — worth stating explicitly since it's easy to assume
  it governs `ReAct`'s tool calling too.

## PROD

- **`AdapterParseError`'s composed message always embeds the model's full raw reply
  verbatim** (see the API item above) — logging or printing such an exception
  un-redacted writes the whole answer (and often the shape of the question it
  answers) into whatever log sink catches it. `dspy/utils/exceptions.py:246-283`.
  [prod|trap] (verified: read + constructed) · skill: new.
- **`format_finetune_data` is implemented only on `ChatAdapter`** (OpenAI message
  format: `self.format(...)` plus one appended assistant message).
  `JSONAdapter.format_finetune_data` is `raise NotImplementedError` — literally
  `# TODO: implement format_finetune_data method in JSONAdapter`.
  `XMLAdapter`/`TwoStepAdapter`/`BAMLAdapter` inherit whichever of those two they get
  (`XMLAdapter`→`ChatAdapter`'s implementation runs but produces XML-tagged content
  under an OpenAI-message wrapper — untested for correctness in this slice;
  `TwoStepAdapter`/`BAMLAdapter`→effectively `JSONAdapter`'s `NotImplementedError`
  for BAML, and `TwoStepAdapter` has no override at all so it inherits
  `Adapter.format_finetune_data`'s base `NotImplementedError`).
  `dspy/adapters/chat_adapter.py:277-299`, `dspy/adapters/json_adapter.py:226-230`.
  [prod] (verified: read; matches `docs/docs/diving-deeper/adapters.md:51-53`) ·
  skill: new.
- **Nothing in DSPy's own adapter code requires demos or history to arrive at the LM
  as separate turns.** `Adapter.format_demos`/`format_conversation_history` build
  alternating `{"role": "user"/"assistant", ...}` dicts purely as *this* adapter's
  own prompt convention; `Adapter.parse()` (and every concrete adapter's own
  `.parse()`) operates **only on the final completion string**, never on the
  message/turn structure that produced it — the `[[ ## field ## ]]`/JSON/XML markers
  are self-contained text patterns. This repository's `scripts/claude_lm.py` proves
  the point in practice: its `flatten()` collapses every earlier user/assistant pair
  into one stdin string of "=== Example N: the message ===" / "the reply that was
  given ===" blocks (because the `claude -p` CLI takes no assistant turn), preserving
  each message's text **verbatim** — and `ChatAdapter.parse()` on whatever the model
  answers afterward works exactly as it would against a real multi-turn call, because
  parsing never looked at turn boundaries in the first place.
  `dspy/adapters/base.py:367-442,542-602,626-712,714-726` (verified: read) vs.
  `scripts/claude_lm.py:66-92` (verified: read, this repository). [prod|pattern]
  (verified: read both sides) · skill: new — the one genuine risk `flatten()`
  introduces is unrelated to turn separation: its `_text()` helper extracts only
  `{"type": "text", ...}` parts from a content-parts list — `"only text reaches the
  CLI"` is its own comment — so **any multimodal field** (`dspy.Image`/`dspy.Audio`/
  `dspy.File`, once expanded by `_expand_legacy_custom_type_markers_in_chat_message`
  into a content-parts list) is **silently dropped** when the LM is `ClaudeCLI`, with
  no error. `scripts/claude_lm.py:95-99`.
- **The adapter is process-global via `settings.adapter`, defaulting to `ChatAdapter()`
  when unset** — confirmed unchanged from the skill's existing claim; `Predict`,
  `ReAct`, `Refine` each read `settings.adapter or ChatAdapter()`.
  `docs/docs/learn/programming/adapters.md:17-43` (doc-confirmed, matches the skill's
  own citation of `predict.py:254,268`, not re-read here). skill: same.
- **`BootstrapFinetune` accepts an `adapter` dict keyed by LM**, so a finetuning loop
  spanning several LMs can use a different adapter per LM — outside this slice's
  files, mentioned only as a cross-link in
  `docs/docs/diving-deeper/adapters.md:175-179`. [prod|claim] (doc only, not
  independently verified in this slice's source) · skill: new, low-confidence — flag
  for the OPT/optimizers reader to confirm against `dspy/teleprompt/bootstrap_finetune.py`.

## TEST

- **`tests/adapters/conftest.py`'s `CapturingLM` pattern**: a `dspy.BaseLM` whose
  `__call__` records `(messages, kwargs)` then raises a dedicated `BaseException`
  subclass (`StopAdapterCallCapture`) to short-circuit the call before any response
  needs to exist — `format_messages_and_lm_kwargs(adapter, signature, demos, inputs,
  lm_kwargs=None, lm=None)` wraps this into one assertion-ready call. Used across
  every `test_*_format_exact_messages_*` test in this test directory.
  `tests/adapters/conftest.py` (whole file, 56 lines). [test|pattern] (verified:
  read) · skill: new — a much lighter way to assert "exactly what ChatAdapter sends"
  than building a full mock LM response.
- **`tests/adapters/test_resource_loading.py` is a dedicated security-property test
  file** for `Image`/`Audio`/`File` (see the PROD item above) — worth pointing to
  directly whenever this repository considers adding an `Image`/`Audio`/`File` field
  to a signature. [test] (verified: read) · skill: new.
- **DSPy's own error-wrapping is exercised directly**: a raw `RuntimeError`/
  `ValueError` raised by a mocked `litellm.completion`/`litellm.acompletion` inside a
  `JSONAdapter` call surfaces to the caller as `dspy.LMUnexpectedError`, with the
  original message text preserved in `str(error)` — `tests/adapters/
  test_json_adapter.py:1421-1442` (sync) and `1444-1467` (async). Because
  `LMUnexpectedError` is an `LMError`, `JSONAdapter.__call__`'s own
  `except LMError: raise` guard means a genuine provider/network failure during the
  **structured-output** call attempt does **not** trigger the loose-`json_object`
  retry — confirmed by `call_count == 1` in
  `test_json_adapter_does_not_fallback_to_json_mode_on_structured_output_lm_error`
  (`tests/adapters/test_json_adapter.py:1323-1341`). [test] (verified: read) · skill:
  new — sharpens `api.md`'s error-hierarchy section with adapter-specific evidence.
- **`test_stream_listener_missing_completion_marker_chat_adapter` is the evidence for
  why `StreamListener.finalize()` must always run**: a fabricated stream that has a
  field's start marker but never emits `[[ ## completed ## ]]` (14 content chunks,
  more than the "hold back ≤10" buffer) — without `finalize()`, the last several
  buffered tokens would never be yielded; `dspy.streamify`'s handling of the final
  `Prediction` calls `.finalize()` on every listener first, and the test asserts the
  streamed text equals the full answer with nothing lost.
  `tests/streaming/test_streaming.py:711-767`. [test] (verified: read) · skill: new.

## PAT

- **`CapturingLM`/`format_messages_and_lm_kwargs`** (above) — directly reusable
  pattern for any future test in this repository that wants to assert exactly what
  an adapter would send, without a fake response. [pattern] · skill: new.
- **BAML's compact, commented, per-field schema notation** is a genuine, measured
  alternative to raw JSON Schema for a nested Pydantic output — worth knowing exists
  even though nothing here uses nested Pydantic outputs yet
  (`docs/docs/diving-deeper/adapters.md:73-74`: "Worth trying when JSONAdapter's raw
  JSON schema is too verbose for complex nested types."). [pattern|claim] · skill:
  new.
- **The DSPy source's own `# TODO(adapters-plan): …` comments in `base.py` describe a
  planned `_AdapterPlan` refactor and call the current preprocess/postprocess split
  "the pre-normalized planning hook"** — the source treats its own internal
  boundary as explicitly provisional, in almost the same shape as this repository's
  `provisional`/`may not`/`retire when` construct convention. Not a fact to teach the
  skill as DSPy API, but a data point that upstream churn here (line numbers,
  internal call shape) is more likely than in the stabler adapter-output-format
  parts of this same file. `dspy/adapters/base.py:83-149,209-226`. [pattern|claim] ·
  skill: new, low priority.

## TRAP

- **`StreamListener` cannot stream a field through `BAMLAdapter` (or any adapter
  whose class name isn't exactly `"ChatAdapter"`/`"JSONAdapter"`/`"XMLAdapter"`),
  even though `BAMLAdapter` *is* a `JSONAdapter` by `isinstance`.** `receive()`'s
  entry guard keys `self.adapter_identifiers` (exactly those three class-name
  strings) by `settings.adapter.__class__.__name__`; `BAMLAdapter.__name__` is
  `"BAMLAdapter"`, not in that dict, so the **very first chunk** raises
  `ValueError(f"Unsupported adapter for streaming: BAMLAdapter, please use one of the
  following adapters: ChatAdapter, XMLAdapter, JSONAdapter")` — before ever reaching
  `flush()`, which (inconsistently) checks by `isinstance` and *would* have
  recognised it as JSON-shaped. `TwoStepAdapter` hits the same guard for the same
  reason. `dspy/streaming/streaming_listener.py:23,59-81,118-124,312-337`. [trap]
  (verified: constructed a `StreamListener`, listed its `adapter_identifiers` keys,
  and confirmed `BAMLAdapter.__name__ not in` them while
  `isinstance(BAMLAdapter(), dspy.JSONAdapter)` is `True`) · skill: new.
- **A single stream chunk carrying the whole field (a cache hit, or — the code's own
  example — some Gemini responses) is detected and marked `cache_hit=True,
  stream_start=True, stream_end=True` but the field's text is never yielded as a
  `StreamResponse` at all**, for every adapter except `JSONAdapter`
  (`… and not isinstance(settings.adapter, JSONAdapter)`); the caller only gets the
  value from the final `Prediction`. Matches the tutorial's own documented claim
  ("the stream will skip individual tokens and only yield the final Prediction") but
  the code's exact scoping (JSONAdapter excluded from this specific fast path) isn't
  stated anywhere in docs. `dspy/streaming/streaming_listener.py:118,164-176`. [trap]
  (verified: read; cross-checked against `docs/docs/tutorials/streaming/index.md`'s
  "Streaming with Cache" section) · skill: new.
- **The "how many tokens to hold back before flushing" limit is a hard-coded 10**:
  `elif self.field_end_queue.qsize() > 10: token = self.field_end_queue.get()` — "10
  is a heuristic number that is sufficient to capture the end_identifier for all
  LMs," per the code's own comment; not configurable.
  `dspy/streaming/streaming_listener.py:224-228`. [trap|number] (verified: read) ·
  skill: new.
- **JSONAdapter's streaming end-detection depends on the third-party `jiter` package
  directly** (`jiter.from_json(bytes, partial_mode="trailing-strings")`), confirmed
  installed (`jiter==0.17.0` in `.venv-dspy`) but not documented anywhere in this
  repository's DSPy notes. `dspy/streaming/streaming_listener.py:9,241-292`. [trap]
  (verified: `importlib.metadata.version("jiter")`) · skill: new.
- **`dspy.streaming.streamify`'s module unconditionally imports `orjson` and
  `anyio`** at the top level (`dspy/streaming/streamify.py:9-11`) — both confirmed
  installed (`orjson==3.12.0`, `anyio==4.15.1`); if either were ever missing,
  `import dspy` itself would not fail (nothing forces `dspy.streaming` to load
  eagerly, per `dspy/adapters`/`dspy/streaming` being separate subpackages — not
  independently re-verified here), but any code doing `import dspy.streaming` or
  `from dspy.streaming import streamify` would. [trap] (verified: version check only;
  did not verify dspy's own `__init__.py` import graph) · skill: new, low
  confidence on the "doesn't break `import dspy`" half.
- **`streamify`'s per-invocation callback list is captured once, when `streamify(...)`
  is called to build the wrapper — not per call of the returned function.**
  `callbacks = list(settings.callbacks)` runs at wrap time;
  a later `dspy.configure(callbacks=[...])` change is invisible to an
  already-built streamer. `dspy/streaming/streamify.py:168-171`. [trap] (verified:
  read) · skill: new.
- **Without `stream_listeners`, `dspy.streamify` yields raw, provider-shaped litellm
  `ModelResponseStream` chunks straight through** — "for backwards compatibility" —
  not the clean `dspy.streaming.StreamResponse` objects you get once you add
  listeners. The check that routes chunks to listeners duck-types the class
  (`cls.__name__ == "ModelResponseStream" and cls.__module__.startswith("litellm")`),
  not an isinstance/import check. `dspy/streaming/streamify.py:22-24,183-196`. [trap]
  (verified: read) · skill: new.
- **`include_final_prediction_in_output_stream=False` still yields the final
  `Prediction` whenever there were no listeners, any listener hit a cache, or *no*
  listener ever started** (`not any(listener.stream_start for l in stream_listeners)`)
  — exactly reproducing the docstring's own claim, now pinned to the precise boolean
  condition. `dspy/streaming/streamify.py:204-213`. [api] (verified: read) · skill:
  new (precision on an already-documented behaviour).
- **`StatusMessageProvider`'s four non-tool hooks (`module_start`/`module_end`/
  `lm_start`/`lm_end`) all default to `pass` (return `None`)** — only
  `tool_start_status_message`/`tool_end_status_message` have real default text
  ("Calling tool {name}...", "Tool calling finished! Querying the LLM with tool
  calling results..."). Out of the box, status streaming only narrates tool calls,
  never module or LM boundaries, unless a subclass overrides those hooks.
  `dspy/streaming/messages.py:53-95`. [trap] (verified: read) · skill: new.
- **`StatusStreamingCallback` never announces the `ReAct` "finish" pseudo-tool**:
  `on_tool_start` returns early if `instance.name == "finish"`; `on_tool_end` returns
  early if `outputs == "Completed."` (an exact sentinel string match).
  `dspy/streaming/messages.py:98-184`. [trap] (verified: read) · skill: new.
- **`sync_send_to_stream` spins up a brand-new event loop on a one-worker thread pool
  whenever it's called from inside an already-running event loop** (so a
  synchronous callback like `on_tool_start` can still push a message onto the async
  stream); outside a running loop it uses `anyio.from_thread.run` directly.
  `dspy/streaming/messages.py:27-50`. [prod] (verified: read) · skill: new.
- **`apply_sync_streaming` (the `async_streaming=False` path) runs the async
  generator on a daemon background thread and explicitly threads the current
  `contextvars.copy_context()` through** — "To propagate prediction request ID
  context to the child thread" — without which the `predict_id`-keyed listener
  routing in `async_streamer` could silently misroute chunks across the thread
  boundary. `dspy/streaming/streamify.py:231-261`. [trap] (verified: read) · skill:
  new.
- **`find_predictor_for_stream_listeners` raises on an ambiguous or absent field
  name**, both messages exact and quotable: `"Signature field {name} is not unique
  in the program, cannot automatically determine which predictor to use for
  streaming. Please specify the predictor to listen to."` and `"Signature field
  {name} is not a field of any predictor in the program, cannot automatically
  determine which predictor to use for streaming. Please verify your field name or
  specify the predictor to listen to."` `dspy/streaming/streaming_listener.py:
  373-415`. [trap] (verified: read; the multi-predictor disambiguation pattern
  matches `docs/docs/tutorials/streaming/index.md`'s "Handling Duplicate Field
  Names" section) · skill: new.
- **A `StreamListener` is single-use by default**: once `self.stream_end` is `True`,
  `receive()` returns `None` for the rest of any *subsequent* stream unless
  `allow_reuse=True` was passed at construction — the tutorial's own stated reason is
  performance ("every token is broadcast to all configured stream listeners, and
  having too many active listeners can introduce significant overhead"), and the
  worked example is exactly the case this repository would hit if it ever streamed a
  `dspy.ReAct` loop's repeating field (`next_thought`).
  `dspy/streaming/streaming_listener.py:29-56,129-139`,
  `docs/docs/tutorials/streaming/index.md` ("Streaming the Same Field Multiple
  Times"). [trap] (verified: read) · skill: new.

## 3. Code worth keeping

**Exactly what `ChatAdapter` sends for a `Literal` field — ran on the installed
package, this repository's own signature shape** (`dspy/adapters/utils.py:131-156`,
verified: ran, output reproduced verbatim):

```python
class SameTerm(dspy.Signature):
    """Sind die beiden Oberflaechenformen derselbe Begriff?"""
    first: str = dspy.InputField()
    second: str = dspy.InputField(desc="die andere Oberflaechenform")
    decision: Literal["one-term", "two-terms"] = dspy.OutputField()
    rule: str = dspy.OutputField(desc="die Regel, in einem Satz")

print(dspy.ChatAdapter().format_system_message(SameTerm))
# ...
# [[ ## decision ## ]]
# {decision}        # note: the value you produce must exactly match (no extra
#                      characters) one of: one-term; two-terms
# ...
```

**`_get_structured_outputs_response_format` — how JSONAdapter builds an OpenAI
Structured Outputs schema** (ran, not modified) `dspy/adapters/json_adapter.py:233-311`:

```python
def enforce_required(schema_part: dict):
    if schema_part.get("type") == "object":
        props = schema_part.get("properties")
        if props is not None:
            schema_part["required"] = list(props.keys())
            schema_part["additionalProperties"] = False
            for sub_schema in props.values():
                if isinstance(sub_schema, dict):
                    enforce_required(sub_schema)
        else:
            schema_part["properties"] = {}
            schema_part["required"] = []
            schema_part["additionalProperties"] = False
    if schema_part.get("type") == "array" and isinstance(schema_part.get("items"), dict):
        enforce_required(schema_part["items"])
    for key in ("$defs", "definitions"):
        if key in schema_part:
            for def_schema in schema_part[key].values():
                enforce_required(def_schema)
```

**`CapturingLM` — asserting exact adapter output with no real response needed** (ran,
part of the test suite) `tests/adapters/conftest.py` (whole file):

```python
class StopAdapterCallCapture(BaseException):
    """Stop adapter execution after capturing the LM call."""

class CapturingLM(dspy.BaseLM):
    def __call__(self, messages=None, **kwargs):
        self.calls.append({"messages": messages, "kwargs": kwargs})
        raise StopAdapterCallCapture

def format_messages_and_lm_kwargs(adapter, signature, demos, inputs, lm_kwargs=None, lm=None):
    capturing_lm = CapturingLM(lm)
    try:
        adapter(capturing_lm, dict(lm_kwargs or {}), signature, demos, inputs)
    except StopAdapterCallCapture:
        pass
    call = capturing_lm.calls[0]
    return call["messages"], call["kwargs"]
```

**The SSRF-safety guard in `Image.__init__`** (ran indirectly via
`test_resource_loading.py`) `dspy/adapters/types/image.py:63-75`:

```python
download_requested = download is not _UNSET
verify_requested = verify is not _UNSET
if (download_requested or verify_requested) and source is None:
    # `download`/`verify` are a compatibility shim for the positional constructor
    # `Image(url, download=True)`. They must never be honored through the validation
    # path: pydantic routes dict data into `__init__`, so an untrusted value such as
    # `{"url": "http://169.254.169.254/...", "download": true}` would otherwise trigger
    # a server-side fetch during output parsing. Requiring a positional source keeps the
    # shim reachable only from direct developer construction.
    raise TypeError(
        "`download` and `verify` are only valid with a positional image source; "
        "use Image.from_url(url, verify=...) to download a remote image."
    )
```

## 4. Probes worth adding

```python
# id: json-adapter-literal-failure-is-bare-exception
# "A Literal/enum/pydantic value that fails parse_value inside otherwise-valid JSON
#  escapes JSONAdapter.parse() as a bare exception, not dspy.AdapterParseError."
import sys
sys.path.insert(0, "/home/user/kohaerenzprotokoll/scripts")
from lm_fixture import FixtureLM, offline
import dspy
from typing import Literal

def p_json_adapter_literal_failure_is_bare_exception():
    class Sig(dspy.Signature):
        q: str = dspy.InputField()
        decision: Literal["one-term", "two-terms"] = dspy.OutputField()
    try:
        dspy.JSONAdapter().parse(Sig, '{"decision": "not-a-real-choice"}')
        return "expected an exception, got none"
    except dspy.utils.exceptions.AdapterParseError:
        return "parse_value's failure was wrapped as AdapterParseError (behaviour changed)"
    except ValueError:
        return None  # holds: a bare ValueError, not AdapterParseError

# Ran on .venv-dspy/bin/python with keys scrubbed: returns None (holds).
```

```python
# id: baml-adapter-unsupported-by-stream-listener
# "StreamListener cannot stream through BAMLAdapter: its class name isn't one of the
#  three names StreamListener recognises, even though it IS a JSONAdapter."
import dspy
from dspy.adapters.baml_adapter import BAMLAdapter

def p_baml_adapter_unsupported_by_stream_listener():
    listener = dspy.streaming.StreamListener(signature_field_name="answer")
    if BAMLAdapter.__name__ in listener.adapter_identifiers:
        return f"BAMLAdapter unexpectedly recognised: {listener.adapter_identifiers.keys()}"
    if not isinstance(BAMLAdapter(), dspy.JSONAdapter):
        return "BAMLAdapter is no longer a JSONAdapter subclass (behaviour changed)"
    return None  # holds

# Ran on .venv-dspy/bin/python: returns None (holds).
```

```python
# id: chain-of-thought-reasoning-is-plain-str-by-default
# "dspy.ChainOfThought's own `reasoning` output field is a plain str by default,
#  not dspy.Reasoning."
import inspect
import dspy

def p_chain_of_thought_reasoning_is_plain_str_by_default():
    default = inspect.signature(dspy.ChainOfThought.__init__).parameters["rationale_field_type"].default
    if default is not str:
        return f"ChainOfThought's default rationale_field_type is {default!r}, not str"
    cot = dspy.ChainOfThought("question -> answer")
    ann = cot.predict.signature.output_fields["reasoning"].annotation
    if ann is not str:
        return f"reasoning field annotation is {ann!r}, not str"
    return None  # holds

# Ran on .venv-dspy/bin/python: returns None (holds).
```

## 5. Surface worth asserting

```
dspy.adapters.base.Adapter(callbacks=None, use_native_function_calling=False, native_response_types=None, parallel_tool_calls=None)
dspy.ChatAdapter(callbacks=None, use_native_function_calling=False, native_response_types=None, use_json_adapter_fallback=True, parallel_tool_calls=None)
dspy.JSONAdapter(callbacks=None, use_native_function_calling=True, parallel_tool_calls=None)
dspy.XMLAdapter — no own __init__; identical signature to dspy.ChatAdapter
dspy.TwoStepAdapter(extraction_model: dspy.BaseLM, **kwargs)
dspy.adapters.baml_adapter.BAMLAdapter — no own __init__; identical signature to dspy.JSONAdapter
dspy.streaming.StreamListener(signature_field_name: str, predict=None, predict_name=None, allow_reuse=False)
dspy.streamify(program, status_message_provider=None, stream_listeners=None, include_final_prediction_in_output_stream=True, is_async_program=False, async_streaming=True)
dspy.streaming.apply_sync_streaming(async_generator)  # not in the skill's surface block at all
dspy.streaming.streaming_response(streamer)           # not in the skill's surface block at all
dspy.ChainOfThought(signature, rationale_field=None, rationale_field_type: type = str, **config)
dspy.Tool(func, name=None, desc=None, args=None, arg_types=None, arg_desc=None)  # __init__ only takes these; auto-inference fills the rest
dspy.Tool.from_mcp_tool(session, tool, *, result_mode: Literal["text", "structured"] = "text")
dspy.Image(source=None, /, *, download=<unset>, verify=<unset>, **data)  # positional source only; download/verify are a deprecated compatibility shim
dspy.Audio(*args, **data)  # at most one positional arg
dspy.File(*args, **data)   # at most one positional arg; no File.from_url
dspy.Code["python"](code=...)  # subscript builds a fresh model_class each call
```
(all confirmed by `inspect.signature` on the installed 3.3.1 package, this session.)

## 6. Ten things the skill must say

1. **`JSONAdapter.parse()`'s per-field `parse_value` call is unwrapped — a bad
   Literal/enum/pydantic value inside otherwise-valid JSON escapes as a bare
   exception, not `AdapterParseError`** — and `ChatAdapter`'s default JSON fallback
   means this can happen even when the primary adapter is `ChatAdapter`. This is the
   one finding that can silently break `lmrun.call`'s `unparsed` bookkeeping in this
   repository's own default configuration (`ChatAdapter` + `Literal` fields).
   `dspy/adapters/json_adapter.py:189-191`.
2. **`ChatAdapter` falls back to `JSONAdapter` on *any* non-`LMError` exception in its
   pipeline, not only a parse failure**, and the fallback instance inherits the
   original's `use_native_function_calling`, not `JSONAdapter`'s own default.
   `dspy/adapters/chat_adapter.py:77-115`.
3. **The exact `format_field_structure` text for a `Literal` output field** —
   `{field}` then an 8-space-indented `# note: the value you produce must exactly
   match (no extra characters) one of: "a"; "b"` — is what makes an off-list answer
   unparseable rather than merely wrong; reproduced live against `pairs.py`'s own
   signature shape. `dspy/adapters/utils.py:131-156`.
4. **`dspy.ChainOfThought`'s `reasoning` field is a plain `str` by default, not
   `dspy.Reasoning`** — that type only applies to a field a signature declares
   explicitly, and DSPy itself reverted making it the ChainOfThought default ("PR
   #8822"). `dspy/predict/chain_of_thought.py:9,40`.
5. **`Reasoning.adapt_to_native_lm_feature` turns on native reasoning (`reasoning_effort
   ="low"`) just because a `Reasoning` field is declared, unless the LM is GPT-5-family
   on the chat API (a named litellm caveat) or doesn't support reasoning at all.**
   `dspy/adapters/types/reasoning.py:45-77`.
6. **`Image`/`Audio`/`File` construction and pydantic validation never touch the
   network or filesystem — a whole test file exists to prove attacker-controlled
   locator strings can't trigger host I/O** — directly relevant if this repository
   ever lets a model's output populate one of these types. `dspy/adapters/types/
   image.py:63-105`, `tests/adapters/test_resource_loading.py`.
7. **`StreamListener` cannot stream through `BAMLAdapter`/`TwoStepAdapter`** — the
   streaming guard checks the adapter's exact class name, not `isinstance`, so a
   `BAMLAdapter` (which *is* a `JSONAdapter`) is rejected on the first chunk.
   `dspy/streaming/streaming_listener.py:23,118-124`.
8. **`JSONAdapter.format_finetune_data` raises `NotImplementedError` — only
   `ChatAdapter` implements it** — relevant if `BootstrapFinetune` is ever used with
   a non-default adapter. `dspy/adapters/json_adapter.py:226-230`.
9. **`XMLAdapter.parse()` wraps the whole completion in `<dspy_root>…</dspy_root>`
   and parses with `ElementTree` — a bare `&`/`<`/`>` anywhere in the raw text, even
   in prose outside any field, breaks the entire parse.**
   `dspy/adapters/xml_adapter.py:95-104`.
10. **Nothing in the adapter code requires demos/history to arrive as separate LM
    turns — only the final completion text is ever parsed** — so
    `scripts/claude_lm.py`'s `flatten()` (collapsing them into one stdin message for
    `claude -p`) is mechanically safe; its real risk is that it drops any non-text
    content part (`dspy.Image`/`Audio`/`File`) silently, since `_text()` only keeps
    `"text"` blocks. `dspy/adapters/base.py:367-442`, `scripts/claude_lm.py:66-99`.
