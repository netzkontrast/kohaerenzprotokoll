# Testing DSPy code here

`api.md` has the DSPy surface and the evidence conventions; this file does not
repeat either. `operations.md` is this file's other half: what happens once a
call is trusted enough to leave the container. This file is everything before
that point — offline fixtures, dry runs, the two scripts that check the skill
itself, and the shapes of test that pass without proving anything, collected
from nine repositories that mostly ship at least one.

## In this repository

### `lm_fixture.py` is the one fixture every model step uses

| piece | what it is | what it guards against |
|---|---|---|
| `chat(**fields)` | builds one completion in `ChatAdapter`'s own wire format, `[[ ## field ## ]]` per output, ending `[[ ## completed ## ]]` | a fixture whose text does not look like a real answer and so exercises a different parse path than production |
| `fill(**values)` | reads the *output fields* an optimizer's own internal prompt asks for straight out of `ChatAdapter`'s system message (`"Your output fields are:\n1. \`name\` (type)"`), then answers each by name, or `"[]"` for a list type, or a marked placeholder | a dry run dying on the first field it did not anticipate — `InferRules` proposing rules and `GEPA` reflecting both ask for fields the task signature never declared |
| `FixtureLM(respond, model="fixture/offline")` | a `dspy.BaseLM` subclass, `cache=False`; `respond` is either `(messages) -> str` or a list consumed in order; every request lands in `self.requests` | a fixture that quietly repeats its last answer once its script runs out — this one raises `AssertionError: FixtureLM script exhausted after N answers` instead |
| `offline(lm)` | a context manager: `dspy.context(lm=lm)`, strips every `*_API_KEY` from `os.environ`, and replaces `litellm.completion`/`acompletion` with a function that raises `NetworkRefused` | a step that builds its *own* `dspy.LM` behind the fixture's back — it fails loudly rather than calling out (see *The accidental live call*) |

`chat()` and `fill()` are not decoration: they are why a dry run can reach an
optimizer's *own* prompts, not only the task's. `fill()` is what lets
`check_dspy_skill.py`'s `p_inferrules_halves_trainset` and
`p_rlm_runs_offline` probes run a real `InferRules.compile()` or `dspy.RLM`
loop against a fixture that was never told those calls were coming.

`FixtureLM` does not set `forward_contract` explicitly, so it runs under the
implicit default, `"legacy"` — `forward(prompt=None, messages=None, **kwargs)`
returning an OpenAI-shaped response. `session-optimizer.md` (`[optimizer]`
item, `BaseLM.forward_contract`) names the alternative, `"typed_lm"`
(`forward(request: dspy.LMRequest) -> dspy.LMResponse`, called inside
`dspy.context(experimental=True)`), and recommends declaring the contract
explicitly rather than relying on the default. Nothing here does; `FixtureLM`
has never needed to, because every caller of it uses the legacy `messages=`
form.

`scripts/lm_fixture.py` is its own self-test, three cases: the fixture
answers and records the exact request it was sent; a real `dspy.LM`
constructed *inside* `offline()` is refused, and every hidden key is restored
afterward; an exhausted scripted list raises rather than repeating.
`.venv-dspy/bin/python scripts/lm_fixture.py` runs it — "`lm_fixture: 3 of 3
cases hold (answer+record, refuse network, exhausted script)`".

### The suites `scripts/selftests.py` runs

Sixteen named suites, nine standard-library and seven needing `.venv-dspy`
(`scripts/selftests.py`):

| kind | suite | command |
|---|---|---|
| std | quotes, find, fold | `scripts/selftest.py` |
| std | entities matcher | `scripts/entities.py selftest` |
| std | skills | `scripts/check_skills.py --selftest` |
| std | skills, live | `scripts/check_skills.py` |
| std | baseline ledger | `scripts/baseline.py selftest` |
| std | graph | `scripts/graph.py --selftest` |
| std | graphrag | `scripts/graphrag.py selftest` |
| std | rlm_ingest tools, reach | `scripts/rlm_ingest.py --selftest` |
| std | prose numbers | `scripts/state.py --prose` |
| dspy | dspy surface | `check_dspy_surface.py` |
| dspy | dspy skill, selftest | `check_dspy_skill.py --selftest` |
| dspy | dspy skill, live | `check_dspy_skill.py` |
| dspy | lm fixture | `lm_fixture.py` |
| dspy | lmrun | `lmrun.py` |
| dspy | pairs dry-run | `pairs.py run --optimizer labeled --dry-run` |
| dspy | graphrag answer dry-run | `graphrag.py ask "Nexus Überraum" --answer --dry-run` |

`python3 scripts/selftests.py` runs every std suite with `sys.executable` and
every dspy suite with `.venv-dspy/bin/python`, 900s timeout each, and prints
one line per suite — `held`, `FAILED`, or, when `.venv-dspy` does not exist,
`not run` with the exact `uv venv`/`uv pip install` command that creates it
(`scripts/selftests.py`). It never runs a suite partially: a `.venv-dspy`
suite is skipped whole when the interpreter is absent, not attempted and
marked failed.

**Two scripts that call a real model have no suite here at all.** `bilingual.py`
and `jev_entities.py` both call Jev; neither has a `selftest()` of its own and
neither is in `SUITES` (`grep selftest scripts/bilingual.py
scripts/jev_entities.py` finds nothing). Both have `--replay`, which reruns a
past run's cached responses with no key and no network — a different
guarantee: it proves a recorded answer replays, not that the script's own
logic can be shown to fail (P5). This is a named gap, not a defect: see *Not
taken*.

### What `not run` means

**A suite that did not run has not passed (P15).** It is a third state, the
same shape as `lmrun.call`'s `unreachable` status and `baseline.compare`'s
`unscored` verdict: none of the three ever collapses into a pass. The exit
status enforces it — `scripts/selftests.py` returns `1` whenever
`failed or unrun` is non-zero, so a fresh container with no `.venv-dspy` fails
`python3 scripts/selftests.py` exactly as if seven suites had failed, not as
if they had been skipped politely. Reading `not run` as green is the mistake
P23 is written against: a guard's blind spot has to be counted, never folded
into "checked".

### Adding a dry run to a new model step

The shape is always the same: run the real program against `offline()`, never
a stand-in of the program. `lmrun.py`'s own self-test is the clearest instance
of the pattern — a list of `(expected_status, FixtureLM(...), needles)` cases,
each run through the real `call()`:

```python
from lm_fixture import FixtureLM, chat, offline
from lmrun import call

cases = [
    ("answered", FixtureLM([chat(antwort="Das ist eine deutsche Antwort.")]), []),
    ("unparsed", FixtureLM(["kein format", "immer noch kein format", "nein"]), []),
]
for expected, lm, needles in cases:
    with offline(lm):
        _, record = call(program, step="selftest", german=["antwort"], frage="?")
    assert record["status"] == expected, record
```

Four things make this reusable for a new step (generalised from
`scripts/lmrun.py` and `scripts/lm_fixture.py`, not from any
of the nine repositories):

1. **The offline fixture answers the real program**, not a rewritten copy of
   its logic — that is what `das-rlm-rag.md`'s *dry-runs that test a
   plain-Python model of the package* names as the failure to avoid (below).
2. **Assert on the record, not only on the parsed output** — `status`,
   `problems`, and, for a script with its own header line (`rlm_ingest.py`,
   `entities.py place`), the header fields that say whether the run is a
   reading or a reconstruction.
3. **Add a case that must fail**, carrying the exact defect the step must
   name — an empty answer, a merged canary, an unparseable reply — never only
   the happy path (P23; *Tests that cannot fail*, below).
4. **Register the command** as a `(name, "dspy", [args])` tuple in
   `scripts/selftests.py`'s `SUITES`, so `python3 scripts/selftests.py` covers
   it without a separate thing to remember to run.

## Offline language models

Four fixtures answer a `dspy.Predict` call with no key and no network. Only
one is built for this repository; the other three come from three of the nine
repositories, verified by their readers against DSPy 3.3.1.

| fixture | source | is a `dspy.BaseLM`? | records | what it misses |
|---|---|---|---|---|
| `FixtureLM` | `scripts/lm_fixture.py`, ported from the next two | yes (`cache=False`) | every request, in `self.requests`, and raises when a scripted list runs out | nothing declared for `forward_contract` (implicit `"legacy"`) |
| `dspy.utils.DummyLM` | DSPy itself | yes | `lm.history`, like any real LM | answers pre-formatted through the adapter's own `format_field_with_value`, so a malformed reply is never exercised unless deliberately constructed |
| `MockLLM` | `dspy-optimizer:tests/conftest.py:9-53` | yes | nothing beyond the base class's `lm.history` | **a JSON `response_text` doubles the call count** — see below |
| `RecorderLM` | `dspy-agents:tests/test_dspy_config.py:13-20` | **no** — a plain class, not a `BaseLM` subclass | constructor `args`/`kwargs` only | never runs a real completion at all — see below |

**`dspy.utils.DummyLM(answers, follow_examples=False, reasoning=False,
adapter=None)`** answers from a list of dicts (served in order, then
`{"answer": "No more responses"}`), or a dict keyed by a substring of the last
message, and honours `n` so `config={"n": 5}` yields five completions
(`session-optimizer.md`, `[session]` item; `dspy:utils/dummies.py:16-160`).
Because it formats every answer through the configured adapter before
returning it, an answer built this way parses on the first try by
construction — useful for exercising a program's logic, useless for
exercising the JSON-fallback or `unparsed` path, which needs deliberately
unparseable text (as `FixtureLM`'s scripted lists supply). Nothing in this
repository imports `DummyLM` directly; `lm_fixture.py`'s docstring names it as
one of two things `FixtureLM` was ported from — the other is `MockLLM`'s
response shape.

**`MockLLM(dspy.BaseLM)`** (`dspy-optimizer:tests/conftest.py:9-53`) is a
legacy-contract fixture: `forward` returns
`SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=text,
tool_calls=None), logprobs=None)], usage={0,0,0}, model=self.model)` plus
`_hidden_params={"response_cost": 0.0}` — the same shape `FixtureLM.forward`
builds. **It runs unmodified on 3.3.1, and its own suite's `response_text` is
set to a JSON object**, which `ChatAdapter` cannot parse: every predictor call
under it costs **two** LM calls through the `JSONAdapter` fallback, and the
suite's history assertions inspect the *fallback's* messages, not the first
attempt's (`session-optimizer.md`, `[optimizer]`/TEST items;
`dspy-optimizer:tests/dspy_optimizer/test_evaluator.py:41-47`). ChatAdapter-
formatted text costs one call; the fixture's own default "mocked response"
string raises `AdapterParseError` outright. `check_dspy_skill.py`'s own probe
for this exact mechanism is `p_chat_adapter_json_fallback`, asserted in
`api.md` as `[checked: chat-adapter-json-fallback]` — do not re-derive it
here; the point for a fixture author is that **a call count is a call count
at the LM, not at the predictor**, and a fixture that answers JSON when the
adapter expects `[[ ## field ## ]]` sections is silently paying for two.

**`RecorderLM`** (`dspy-agents:tests/test_dspy_config.py:13-20`) is not a
`dspy.BaseLM` at all:

```python
class RecorderLM:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.model = kwargs.get("model", args[0] if args else None)
        self.model_type = kwargs.get("model_type", "chat")
```

It is monkeypatched in for `dspy.LM` itself (`monkeypatch.setattr(cfg.dspy,
"LM", fake_lm)`), so no LM is ever built and no completion is ever run — every
assertion is against the *constructor kwargs* the project's own config module
passed: the responses-vs-chat path, `temperature == 1.0`, `max_tokens >=
16000` (`dspy-agents:tests/test_dspy_config.py:23-56`, three tests, verified
passing on 3.3.1 in 0.28s). **What it structurally cannot see is what DSPy
does with those kwargs afterward**: 3.3.1 renames `max_tokens` and collapses
it with `max_output_tokens` into one Responses-API field, so the config's
`OPENAI_MAX_OUTPUT_TOKENS=2048` cap is silently dropped in favour of
`max_tokens=20000` — a fact a `RecorderLM`-only test cannot catch by
construction, because it never lets DSPy touch the kwargs at all
(`dspy-agents:tests/test_dspy_config.py:13-20`; the recipe for pairing it with
a real, offline `dspy.LM(...)` construction is `[agents]` under TEST in the
same note). A recorder fixture answers "what did we pass"; it does not answer
"what did DSPy do with it" — a `RecorderLM`-shaped check needs a second,
paired assertion against a real (but keyless) `dspy.LM(...)` construction
before it earns the word "verified".

## The accidental live call

**A dry run that *can* reach the network is not a dry run.** This is not
hypothetical: scanning `dspy-auto-gepa` at commit `80a5402` on 2026-09-23, its
test `test_partial_explicit_fields_infer_rest` was unmocked — it calls
`auto.datasets()` with no `metric=` and no patch of
`generate_metric_file`, which reaches a real `dspy.RLM` configured for
`openrouter/openai/gpt-oss-120b`. Running the suite under an offline guard
recorded the attempt: `litellm.completion(model='openrouter/openai/gpt-oss-
120b')`, reached through `runner.py:228` → `metric_builder.py:296` →
`dspy:predict/rlm.py:728`, and raising `LMUnexpectedError` only because the
guard was there to refuse it (`dspy-auto-gepa:tests/test_auto_gepa.py:538-560`).
Its sibling tests *do* patch `dspy_auto_gepa.runner.generate_metric_file`
(`dspy-auto-gepa:tests/test_auto_gepa.py:479,501`); this one alone falls
through. `poe test-e2e` cannot even be used to separate it out — the pyproject
script references a `--run-e2e` flag no `conftest.py` defines
(`dspy-auto-gepa:pyproject.toml:71`), so the live test runs under a plain
`pytest`, unflagged (`dspy-auto-gepa:tests/test_auto_gepa.py:538-560`).

**This is the reason `lm_fixture.offline()` does three things, not one**
(`scripts/lm_fixture.py`): it is not enough to configure the
fixture as the active LM, because a step (or, as here, a test) can build its
own `dspy.LM` and call it directly, bypassing `dspy.settings.lm` entirely.
`offline()` therefore also:

1. **strips every `*_API_KEY`** from `os.environ` for the duration of the
   block, so a freshly constructed `dspy.LM` has no key to authenticate with
   even if one is built; and
2. **replaces `litellm.completion`/`acompletion`** with a function that raises
   `NetworkRefused` unconditionally, so the failure happens at the transport
   call itself rather than depending on the key removal alone (a key could be
   read from a `.env` file, an already-loaded module global, or a second
   process).

Both keys are restored and `litellm.completion`/`acompletion` are restored to
their originals in the `finally` block, asserted by
`lm_fixture.selftest()`'s second case. The fixture words sent in the
`dspy-auto-gepa` incident were never corpus text — but the mechanism this
repository built afterward refuses the call on principle, not on the content.

**`drg-kg` configures DSPy's global LM as a side effect of extraction, with no
`lm=` argument needed to trigger it.** Verified by the `dspy-agent-skills`
reader, probing the installed `drg-kg` package directly rather than restating
what `dspy-agent-skills`' own skill text claims: with nothing configured,
calling `extract_typed` runs `_configure_llm_auto()`, whose
`LMConfig._configure_unsafe()` does two things unconditionally — it calls
`load_dotenv(".env", override=False)` from the **current working directory**,
and it picks a model (`DRG_MODEL`, default `openai/gpt-4o-mini`), only warning
about a missing key, and **always** calls `dspy.configure(lm=...)`. After one
`extract_typed` call, `dspy.settings.lm` moved from `None` to
`openai/gpt-4o-mini`, and a live completion to that model was attempted (the
probe refused it) — reproduced against `drg-kg` 0.1.2. **Setting
`DRG_REQUIRE_LM=1` does not prevent this**: the strict guard only raises when
no LM exists *after* auto-configuration has already run, and auto-
configuration always creates one, so the same keyless call is attempted and
fails at request time rather than being refused up front. The environment
variables involved — `DRG_MODEL`, `DRG_BASE_URL`, `DRG_TEMPERATURE`,
`DRG_MAX_TOKENS`, and the four provider key names — are documented at
`dspy-agent-skills:skills/dspy-drg-kg/reference.md:117-125`. **This repository
installs `drg-kg` for exactly one module, its evaluation scorer** (`CLAUDE.md`,
*Installing anything*); nothing here calls `extract_typed` or any other part
of its extraction layer, and this fact is the reason not to start.

## Surface checks and behaviour probes

Two scripts, answering two different questions, both run only in
`.venv-dspy`:

**`scripts/check_dspy_surface.py`** asserts the DSPy surface **the scripts in
this repository call** — `dspy.LM`, `dspy.RLM.__init__`, the five optimizers on
the ladder, `dspy.Evaluate`, `dspy.BaseLM.__init__` — against
`inspect.signature` of the installed package, plus behavioural gotchas
asserted by construction: the pinned version, `dspy.LM`'s `cache` default
still `True` (this repository overrides it — the check exists so a *changed*
default is noticed rather than silently inherited), `dspy.SIMBA`'s `bsize`
default still `32`, `dspy.track_usage` still present, `dspy.GEPA()` without
`reflection_lm` still raising, `gepa.optimize_anything` still importable and
still taking `evaluator=`, and `numpy` importable. **17 checks in total**
(`scripts/check_dspy_surface.py`): 9 named callables plus 8
behavioural assertions (version, three defaults, the `GEPA` gotcha, `gepa`
importability, `numpy`, and `example_param_ok()`'s own self-check on a good
and a bad evaluator signature). It asserts *only* what is called — "a surface
check that asserts things nobody uses is a second, drifting description of
DSPy" (`scripts/check_dspy_surface.py`).

**`scripts/check_dspy_skill.py`** asserts what **this skill's Markdown files
teach**, in three unrelated parts, run over every `.md` file under
`.agents/skills/dspy/`:

1. **Surface** — every fenced ` ```surface ` block's call-shaped lines
   (`dspy.RLM(signature, max_iters=20, …)`) are parsed and checked: each named
   parameter must exist on the installed callable, and each default given must
   match the installed default. A line that will not parse as a call is
   reported as unreadable, never silently skipped.
2. **Behaviour** — every sentence ending `[checked: <id>]` names a probe in
   `PROBES`, run offline against `lm_fixture`. The check is two-way: a mark
   with no matching probe fails, and a probe cited by no mark also fails
   (`scripts/check_dspy_skill.py`) — so the marks and the probes
   **cannot drift apart silently** (P23). A probe that needs Deno and finds it
   absent returns `NotRun(...)`, counted separately from held and from failed.
3. **Paths** — every backticked path this skill names under `scripts/`,
   `Plan/`, `Wiki/`, `Sources/`, `.agents/` or `.claude/` must exist, and a
   cited line number must be inside the file
   (`scripts/check_dspy_skill.py`).

Its own `--selftest` is **9 cases**, each a skill built to break one rule and
checked for the exact reason it must fail: a wrong parameter name, a wrong
default, an unreadable surface line, a correct line wrongly flagged (surface,
4 cases); an unknown `[checked: …]` mark, a probe cited by no mark, a probe
reported `not run` rather than held (behaviour, 3 cases); a missing file, a
line past the end of a file (paths, 2 cases) —
`.venv-dspy/bin/python scripts/check_dspy_skill.py --selftest` prints "`9 of
9 cases hold`" (`scripts/check_dspy_skill.py`).

**The lesson both scripts encode is `dspy-agent-skills`' own.** Its
`dspy.RLM` rename (`max_iterations` → `max_iters`, `interpreter` →
`interpreter_factory`, in 3.3.0) was caught only because a surface check
existed at all — and that check had asserted **seven of eight** symbols and
missed the one that broke, which is exactly the shape `check_dspy_surface.py`
was built to close here: assert only what is called, but assert *all* of it
(`scripts/check_dspy_skill.py`; the CHANGELOG entry itself is
`dspy-agent-skills`'s own document, not reproduced here — the point survives
without it). A renamed keyword does not fail at import; it fails mid-run, or
worse, is swallowed by `**kwargs`.

## Tests that cannot fail

**A test that cannot fail is the same defect as the retired pipeline's
`coverage()` term, which returned `1.0` whenever it was passed no gold
fragments and was never passed any** — two live runs scored `0.987` and
`0.967` on a number that could not fall for missing anything
(`scripts/selftest.py`). The nine repositories were read for exactly this
shape, and it recurs in four ways.

**Faked forward.** Every test in `dspy-session`'s suite replaces
`predict.forward` (and `__call__`) directly with a canned-response function,
so no LM and no adapter ever formats a prompt. As a direct consequence, the
suite of 102 passing tests cannot see any of the four real defects the reader
found by probing with `DummyLM` instead: `None`-filled history in a composed
program, a copy or fork still calling the *original* predictor's closure, lost
history inside `dspy.Parallel` workers, or `dspy.RLM`'s outright failure under
the session wrapper (`dspy-session:tests/test_session.py:50-62`;
`dspy-session:tests/test_readme_usage.py:16-28`). `braid-dspy`'s suite is the
same shape taken to its limit: **no test in it configures an LM or uses
`DummyLM` at all** — the LM path is exercised only as the "No LM is loaded"
error string, and three of its own example scripts print plausible-looking
output (100% accuracy, a completed optimization) while making zero real calls
(`braid-dspy:tests/`, grep; `braid-dspy` examples run offline). `dspydantic`'s
`test_forward_produces_descriptions_not_meta_instructions` replaces every
predictor with a `MagicMock` returning clean text — it tests the mock, not the
fix it is named for (`dspydantic:tests/unit/test_module.py:86-130`).

**Hand-built callback state.** `dspy-optimizer`'s MLflow tests hand-construct
the state dict with the *keys the callback reads* (`initial_prompt`, `score`,
`new_prompt`, `optimizer`) rather than the keys the real optimize loop
actually produces, so they pass while the wiring between the loop and the
callback is broken — `MLflowCallback` never once logs the prompt text or the
model name when driven by a real run
(`dspy-optimizer:tests/callback/test_mlflow_callback.py:42-130`;
`dspy-optimizer:dspy_optimizer/callback/mlflow_callback.py:35-125`). The same
repository's own integration test mocks both ends of the thing it claims to
integrate: `Refiner.__call__` and `FullValidationStrategy.__call__` are both
monkeypatched, so a real refiner's output is never run against a real merger
or validator (`dspy-optimizer:tests/dspy_optimizer/test_optimizer.py:33-50`).

**String-presence tests.** `dspy-agent-skills`' own regression suite —
633 tests, otherwise the strongest of the nine — has two that check only that
the literal string `"--dry-run"` appears somewhere in an example's source:
`test_example_has_dry_run` and `test_every_skill_has_example`
(`dspy-agent-skills:tests/test_examples_parse.py:38-44`;
`dspy-agent-skills:tests/test_skill_correctness.py:268-280`). **Nothing in
`pytest` actually runs a dry run**; "633 passed" says nothing about whether
the 33 examples themselves execute — that was checked separately, by hand, and
the CHANGELOG's "all 33 dry-runs pass on 3.3.1" is the record of that manual
run, not of the suite (`dspy-agent-skills:docs/CHANGELOG.md:93-97`, cited via
the `das-patterns` note). The same repository's coverage-gate story appears
the other way round in `braid-dspy`: `pytest` genuinely runs 185 tests offline,
but among them `assert len(labeled_edges) >= 0`, `assert score >= 0.0`, and
`assert "error" in result or …` (where every returned dict happens to carry an
`"error"` key) cannot fail for any input at all
(`braid-dspy:tests/test_parser.py:102`; `braid-dspy:tests/test_optimizer.py:273,289,319,334`;
`braid-dspy:tests/test_integration.py:160`). Worse: several of `braid-dspy`'s
tests wrap a real assertion in `try: … assert …; except Exception: pass`,
which silently swallows the test's *own* `AssertionError` — replaying the body
of `tests/test_module.py:138-145` without the `try` turns a passing test into
a failing one (`braid-dspy:tests/test_module.py:138-145`).

**Dry runs of a plain-Python model of the package.** Four of `dspy-agent-
skills`' six RLM/graph/retrieval example dry-runs — the ones for `dspy-rlm-
hooks`, `dspy-drg-kg`, `dspy-refrag` and TARA — never import the package they
teach at all. Each re-implements the skill's own model of the package's
behaviour in plain Python (`composition_is_correct`, `diagnose_empty_graph`,
`select_mmr`, `decide`, …) and reports honestly when the real package is
absent ("package not installed: skipped live API assertions"), but the model
being asserted can simply be wrong about the package it stands in for — and
was: the drg-kg empty-graph fallback the skill describes does not reproduce
(see *The accidental live call*, above), the ported MMR has an inverted λ, and
TARA's routing threshold is off by one retry
(`dspy-agent-skills:skills/dspy-rlm-hooks/example_rlm_hooks.py:151-159`;
`dspy-agent-skills:skills/dspy-drg-kg/example_drg_kg.py:157-166`). Even when
the real package *is* installed, the same repository's asserts stay at
signature level — checking defaults and keyword-only-ness — while the
behavioural claims beside them are wrong or unverified; a signature check is
not a behaviour check, and the CHANGELOG's "their asserted API surfaces
verified live" overstates what a signature check can show
(`dspy-agent-skills:docs/CHANGELOG.md:163`). This is the same distinction
`check_dspy_surface.py` and `check_dspy_skill.py` keep apart on purpose in
this repository: a `surface` block is signature-level, and only a
`[checked: …]` probe runs real behaviour.

Also worth naming once, because each is a slightly different failure inside
the same family: `dspy-auto-gepa`'s test asserting a maximum call size of 2
that never reads the config field it claims to bound
(`dspy-auto-gepa:tests/test_generator.py:589-634`); its 14 tests that keep
three functions (`_subsample_balanced`, `RejectionSampler`, `DiversityChecker`)
looking alive although the real pipeline never calls any of them
(`dspy-auto-gepa:tests/test_generator.py:1188-1382`,
`dspy-auto-gepa:tests/test_quality.py:18-175`); `dspy-agent-skills`'s own
`validate_dag` cycle test with no `else: raise`, which would pass a
`validate_dag` that had quietly stopped raising on a cycle
(`dspy-agent-skills:skills/dspy-rlm-workflow/example_rlm_workflow.py:164-168`);
and `dspydantic`'s `assert 0.0 <= score <= 1.0` on a score its own metric
clamps into that range before returning it
(`dspydantic:tests/unit/test_evaluators.py:373`). `dspydantic` also has a
test-environment leak worth flagging on its own: its `lm` fixture builds
`dspy.LM(..., api_key=os.getenv("OPENAI_API_KEY", "test-key"))`, so a real key
left in the environment silently turns a unit test into a live call
(`dspydantic:tests/conftest.py:16-17`) — the exact failure mode
`lm_fixture.offline()` exists to make structurally impossible here (it strips
the key rather than trusting nobody set one).

## Regression tests with provenance

**`dspy-agent-skills`' ten regression rules each exist because a mistake
shipped once and was caught in external review**
(`dspy-agent-skills:tests/test_skill_correctness.py:1-40`): `.overall_score`
should be `.score`; a metric returning a dict is caught in code, prose and
multi-line dict literals; a stale RLM `max_output_chars` of `100_000`;
`BetterTogether`'s renamed constructor keywords; every skill ships a `--dry-
run` example; `docs/usage.md` lists every example; the install doc names
3.3.1, the key env var, and the surface script; no "all artifacts are 3.1.3"
regressions; the RAG example's numbers agree across five documents; stale RLM
constructor names. **One of the ten was proven able to fail, on purpose**:
re-introducing the `max_iterations` rename made Rule 10 fail, and reverting it
made Rule 10 pass again
(`dspy-agent-skills:docs/CHANGELOG.md:99-100`, cited via the note) — the same
proof-of-life this repository's own `scripts/selftest.py` gives each of its 17
cases, and the same reason `check_dspy_skill.py --selftest` breaks its own
rules on purpose before trusting them.

**This repository's regression tests carry the same shape, and each is
provenanced the same way — a mistake, then a case that names it:**

| script | the mistake | the case that now names it |
|---|---|---|
| `scripts/lmrun.py` | `call()` re-raised DSPy 3.3's own `LMTransportError` instead of recording `unreachable`, because its first nine offline cases never raised that exact type | a tenth case, added 2026-09-24, that raises `dspy.LMTransportError` directly and asserts `status == "unreachable"` (`scripts/lmrun.py`) |
| `scripts/rlm_ingest.py` | a run forced to stop by `max_iters` could be read as a completed census | `judge(1.0, [], [], 1.0, forced=True)` must **not** start with "a reading" (`scripts/rlm_ingest.py`) |
| `scripts/wiki_index.py` / `scripts/reconcile.py` | `fold()`'s own docstring claimed behaviour it did not have, repeated in two other files | `scripts/judgements.py` replays all 68 recorded near-match decisions against the current code and reports `agrees`/`DISAGREES`/`judgement` |

**And note what a green replay of recorded judgements does *not* prove**:
`fold()` was correct the whole time `reconcile.py`'s own intra-list check
excluded exact fold-equality, which made it report three worlds as six new
terms. `judgements.py` stayed green throughout, because no recorded judgement
covered the *caller* — a green replay says the recorded decisions still hold,
not that the code around them is right (`CLAUDE.md`, *A mechanised rule stays
checkable*). Run `judgements.py` after touching `fold()` or any matching
rule; it is a floor, not a ceiling.

## Not taken

| thing | why not | source |
|---|---|---|
| a mock `CodeInterpreter` that lets `dspy.RLM` run with **no Deno at all** | this repository's own offline RLM probe still needs Deno present — `p_rlm_runs_offline` (`[checked: rlm-runs-offline]`) returns `NotRun(...)` and is not counted as held when `import deno` fails, exactly like `check_dspy_skill.py`'s other Deno-gated probes; the idea exists as a recipe in the notes, not as code here | catalogued from `das-rlm-rag.md`, "A mock `CodeInterpreter` makes RLM testable without Deno" |
| installing `dspy-rlm-hooks` for its testing conveniences | it monkeypatches private DSPy internals and carries its own duplicate copy of DSPy's iteration loop, silently shadowed the day DSPy's own loop changes; its own security note says to pin the pair | `Plan/concept/dspy-toolchain_2026-09-23.md`, *Deliberately not taken* |
| any of the nine repositories as a test dependency | every reader reached the same conclusion independently: the value is a pattern of tens of lines, and the package would bring a pin, a Python floor or a runtime this project does not need | `Plan/concept/dspy-toolchain_2026-09-23.md` |
| a selftest for `bilingual.py` or `jev_entities.py` | not built; both scripts call Jev, not DSPy, and both have `--replay` (a different guarantee — see *In this repository*, above) rather than a fixture-driven failing case | this-repo.md, TEST |
| `TARA`'s progressive-leniency retry ladder as a pattern for a gate here | it lowers the acceptance bar on every retry until something passes; the right terminal state for a canon-facing gate — refuse rather than settle for less — is still an open question, not a decision to route around with a looser bar (P15) | `Plan/concept/dspy-toolchain_2026-09-23.md`, *Deliberately not taken* |

The evaluator registry — `dspydantic`'s `EvaluatorFactory`/
`PredefinedScoreEvaluator` pattern, one interface behind `fold_exact`,
`jev_choice` and `judgement_replay` — is catalogued rather than built; it
waits for a second evaluator actually in use, and belongs beside
`baseline.py` rather than in this file when it arrives
(`Plan/concept/dspy-toolchain_2026-09-23.md`, *Layer 3*).
