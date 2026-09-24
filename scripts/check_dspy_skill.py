"""Assert what the `dspy` skill teaches, against the DSPy installed here.

`.agents/skills/dspy/` teaches DSPy 3.3.1 from nine repositories. A skill is
prose, and prose about an API drifts the day the package moves: the pack it
learned most from caught its own `dspy.RLM` rename only because a surface check
existed, and that check had asserted seven of eight symbols and missed the one
that broke (`dspy-agent-skills` `docs/CHANGELOG.md`). So every claim the skill
makes about DSPy is written where a program can read it, and this reads it:

1. **Surface.** Every fenced `surface` block in the skill holds call-shaped
   lines, `dspy.RLM(signature, max_iters=20, …)`. Each parameter named must be
   a parameter of the installed callable, and each default given must be its
   default. A line that does not parse is reported as unreadable, never skipped.
2. **Behaviour.** A sentence in the skill that ends in `[checked: <id>]` is
   run here as a probe, offline, against `lm_fixture`. A mark with no probe and
   a probe no mark cites both fail, so the two cannot drift apart silently (P23).
3. **Paths.** Every path in this repository the skill names in backticks exists,
   and a cited line is inside the file (P2, P7).

`check_dspy_surface.py` asserts what the scripts *call*; this asserts what the
skill *teaches*. Two lists, because they answer two questions.

    .venv-dspy/bin/python scripts/check_dspy_skill.py
    .venv-dspy/bin/python scripts/check_dspy_skill.py --selftest
"""

from __future__ import annotations

import ast
import importlib
import inspect
import os
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents" / "skills" / "dspy"
sys.path.insert(0, str(ROOT / "scripts"))

try:
    import dspy
except ImportError:
    sys.exit("no DSPy in this interpreter. Create it:\n"
             "  uv venv --python 3.11 .venv-dspy\n"
             "  uv pip install --python .venv-dspy/bin/python 'dspy[deno,numpy]==3.3.1'\n"
             "then run this with .venv-dspy/bin/python")

from check_dspy_surface import gepa_needs_reflection_lm  # noqa: E402  — one encoding of that gotcha
from lm_fixture import FixtureLM, chat, fill, offline  # noqa: E402

BLOCK = re.compile(r"```surface\n(.*?)```", re.S)
MARK = re.compile(r"\[checked: ([a-z0-9-]+)\]")
PATH = re.compile(r"`((?:scripts|Plan|Wiki|Sources|\.agents|\.claude)/[^`\s:]*)(?::(\d+)(?:-(\d+))?)?`")


class NotRun(str):
    """A probe that could not run here. Reported as such, never as held (P15)."""


# --- 1 · surface -------------------------------------------------------------------

def resolve(dotted: str):
    """`dspy.GEPA.compile` → the object, importing the longest module prefix."""
    parts = dotted.split(".")
    for cut in range(len(parts), 0, -1):
        try:
            obj = importlib.import_module(".".join(parts[:cut]))
        except ImportError:
            continue
        for name in parts[cut:]:
            obj = getattr(obj, name)
        return obj
    raise ImportError(dotted)


def surface_line(line: str) -> tuple[int, list[str]]:
    """(parameters asserted, every way one call-shaped line disagrees with the package)."""
    try:
        call = ast.parse(line, mode="eval").body
        if not isinstance(call, ast.Call):
            raise SyntaxError("not a call")
        dotted = ast.unparse(call.func)
        wanted = {a.id: inspect.Parameter.empty for a in call.args if isinstance(a, ast.Name)}
        if len(wanted) != len(call.args):
            raise SyntaxError("a positional entry is not a bare parameter name")
        for kw in call.keywords:
            wanted[kw.arg] = ast.literal_eval(kw.value)
    except (SyntaxError, ValueError) as error:
        return 0, [f"unreadable surface line ({error}): {line}"]
    try:
        target = resolve(dotted)
        # A dspy.Module's metaclass answers inspect.signature(cls) with (*args, **kwargs);
        # the parameters a caller passes are __init__'s.
        params = inspect.signature(target.__init__ if inspect.isclass(target) else target).parameters
    except (ImportError, AttributeError) as error:
        return 0, [f"{dotted}: not importable here ({error})"]
    problems = []
    for name, default in wanted.items():
        if name not in params:
            problems.append(f"{dotted}: no parameter {name!r}")
        elif default is not inspect.Parameter.empty and params[name].default != default:
            problems.append(f"{dotted}: {name} defaults to {params[name].default!r}, the skill says {default!r}")
    return len(wanted), problems


def surface(texts: dict[str, str]) -> tuple[int, int, list[str]]:
    """(callables, parameters, problems) over every surface block."""
    callables = parameters = 0
    problems = []
    for text in texts.values():
        for block in BLOCK.findall(text):
            for raw in block.splitlines():
                line = raw.strip()
                if not line or line.startswith("#"):
                    continue
                callables += 1
                count, found = surface_line(line)
                parameters += count
                problems += found
    return callables, parameters, problems


# --- 2 · behaviour -------------------------------------------------------------------

def _devset(n=4):
    return [dspy.Example(q=str(i), a="ja").with_inputs("q") for i in range(n)]


def _evaluate(metric, program=None):
    with offline(FixtureLM(lambda messages: chat(a="ja"))):
        return dspy.Evaluate(devset=_devset(), metric=metric, num_threads=1)(program or dspy.Predict("q -> a"))


def p_evaluate_score_percent():
    score = _evaluate(lambda e, p, trace=None: float(p.a == e.a)).score
    return None if score == 100.0 else f"all-correct Evaluate score is {score!r}, not 100.0"


def p_evaluate_failure_is_zero():
    class Crash(dspy.Module):
        def forward(self, q):
            raise RuntimeError("the program failed")
    result = _evaluate(lambda e, p, trace=None: 1.0, Crash())
    scores = [r[2] for r in result.results]
    return None if result.score == 0.0 and scores == [0.0] * 4 else \
        f"a crashing program scored {result.score!r} with per-example {scores!r}"


def p_metric_dict_crashes():
    try:
        _evaluate(lambda e, p, trace=None: {"score": 1.0, "feedback": "x"})
    except TypeError:
        return None
    return "a metric returning a dict did not crash dspy.Evaluate"


def p_metric_prediction_aggregates():
    metric = lambda e, p, trace=None, pred_name=None, pred_trace=None: \
        dspy.Prediction(score=float(p.a == e.a), feedback="ok")  # noqa: E731
    score = _evaluate(metric).score
    return None if score == 100.0 else f"a Prediction(score, feedback) metric aggregated to {score!r}"


def p_gepa_light_budget():
    gepa = dspy.GEPA(metric=lambda *a, **k: 0.0, auto="light", reflection_lm=dspy.LM("openai/probe", cache=False))
    got = {n: gepa.auto_budget(1, 6, n) for n in (26, 45, 57)}
    return None if got == {26: 484, 45: 560, 57: 608} else f"auto='light' budgets for one predictor are {got}"


def p_labeledfewshot_fixed_seed():
    train = [dspy.Example(q=str(i), a="x").with_inputs("q") for i in range(20)]
    runs = [[d.q for d in dspy.LabeledFewShot(k=5).compile(dspy.Predict("q -> a"), trainset=train).demos]
            for _ in range(2)]
    order = [d.q for d in train[:5]]
    return None if runs[0] == runs[1] and runs[0] != order else \
        f"LabeledFewShot demos {runs} are not a fixed random sample"


def p_bootstrap_keeps_wrong_demos_on_prediction():
    train = [dspy.Example(q=str(i), a="richtig").with_inputs("q") for i in range(4)]
    kept = {}
    for name, metric in (("prediction", lambda e, p, t=None: dspy.Prediction(score=float(p.a == e.a))),
                         ("float", lambda e, p, t=None: float(p.a == e.a))):
        with offline(FixtureLM(fill(a="falsch"))):
            compiled = dspy.BootstrapFewShot(metric=metric, max_bootstrapped_demos=4, max_labeled_demos=0) \
                .compile(dspy.Predict("q -> a"), trainset=train)
        kept[name] = len(compiled.demos)
    if bool(dspy.Prediction(score=0.0)) is not True:
        return "bool(dspy.Prediction(score=0.0)) is no longer True"
    return None if kept == {"prediction": 4, "float": 0} else f"wrong answers kept as demos: {kept}"


def p_simba_trainset_below_bsize():
    try:
        dspy.SIMBA(metric=lambda e, p: 1.0, bsize=32).compile(dspy.Predict("q -> a"), trainset=_devset(20))
    except AssertionError as error:
        return None if "Trainset too small" in str(error) else f"SIMBA refused for another reason: {error}"
    return "SIMBA compiled on 20 examples with bsize=32"


def p_inferrules_halves_trainset():
    seen: dict[str, list[str]] = {}

    class Spy(dspy.InferRules):
        def induce_natural_language_rules(self, predictor, trainset):
            seen.setdefault("rules", [e.q for e in trainset])
            return "Regel"

        def evaluate_program(self, program, dataset):
            seen.setdefault("select", [e.q for e in dataset])
            return 0.0

    train = [dspy.Example(q=str(i), a="x").with_inputs("q") for i in range(6)]
    with offline(FixtureLM(fill(a="x"))):
        Spy(num_candidates=1, num_rules=1, metric=lambda e, p, t=None: 1.0).compile(
            dspy.Predict("q -> a"), trainset=train)
    want = {"rules": ["0", "1", "2"], "select": ["3", "4", "5"]}
    return None if seen == want else f"InferRules split the trainset as {seen}, expected {want}"


def p_chat_adapter_json_fallback():
    lm = FixtureLM(lambda messages: '{"a": "x"}')
    with offline(lm):
        answer = dspy.Predict("q -> a")(q="?").a
    if answer != "x":
        return f"a JSON answer parsed to {answer!r}"
    return None if len(lm.requests) == 2 else f"the fallback cost {len(lm.requests)} calls, not 2"


def p_unparseable_is_adapter_error():
    with offline(FixtureLM(lambda messages: "kein format")):
        try:
            dspy.Predict("q -> a")(q="?")
        except dspy.AdapterParseError as error:
            return None if not isinstance(error, dspy.LMError) else "AdapterParseError is now an LMError"
        except Exception as error:
            return f"an unparseable answer raised {type(error).__name__}"
    return "an unparseable answer was accepted"


def p_literal_out_of_set_unparsed():
    from typing import Literal

    class Decide(dspy.Signature):
        """Decide."""
        q: str = dspy.InputField()
        decision: Literal["one-term", "two-terms"] = dspy.OutputField()

    with offline(FixtureLM(lambda messages: chat(decision="maybe"))):
        try:
            dspy.Predict(Decide)(q="?")
        except dspy.AdapterParseError:
            return None
    return "a value outside the Literal was accepted as an answer"


def p_refused_connection_is_transport_error():
    lm = dspy.LM("openai/probe", api_base="http://127.0.0.1:9/v1", api_key="none", cache=False, num_retries=0)
    hidden = {k: os.environ.pop(k) for k in list(os.environ) if k.endswith("_API_KEY")}
    try:
        with dspy.context(lm=lm):
            dspy.Predict("q -> a")(q="?")
        return "a closed local port answered"
    except dspy.LMTransportError:
        return None
    except Exception as error:
        return f"a closed local port raised {type(error).__name__}, not dspy.LMTransportError"
    finally:
        os.environ.update(hidden)


def p_numpy_typing_after_dspy():
    import subprocess
    env = {k: v for k, v in os.environ.items() if not k.endswith("_API_KEY")}

    def runs(code: str) -> subprocess.CompletedProcess:
        return subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, env=env, timeout=120)

    after, before = runs("import dspy; import numpy.typing"), runs("import numpy.typing; import dspy")
    if before.returncode != 0:
        return f"importing numpy.typing before dspy failed too: {before.stderr.strip()[-160:]}"
    if after.returncode == 0:
        return "importing numpy.typing after dspy works now; the skill's warning is stale"
    return None if "circular import" in after.stderr else f"it failed differently: {after.stderr.strip()[-160:]}"


def p_track_usage_misses_threads():

    class Counted(FixtureLM):
        def forward(self, prompt=None, messages=None, **kwargs):
            response = super().forward(prompt=prompt, messages=messages, **kwargs)
            response.usage = {"prompt_tokens": 10, "completion_tokens": 2, "total_tokens": 12}
            return response

    seen = {}
    for threads in (1, 4):
        with offline(Counted(lambda messages: chat(a="ja"))):
            with dspy.track_usage() as usage:
                dspy.Evaluate(devset=_devset(6), metric=lambda e, p, t=None: 1.0,
                              num_threads=threads)(dspy.Predict("q -> a"))
        seen[threads] = sum(v.get("total_tokens", 0) for v in usage.get_total_tokens().values())
    return None if seen == {1: 72, 4: 0} else f"tokens tracked by thread count: {seen}, expected {{1: 72, 4: 0}}"


def p_load_refuses_pickle():
    with tempfile.TemporaryDirectory() as tmp:
        dspy.Predict("q -> a").save(f"{tmp}/program", save_program=True)
        try:
            dspy.load(f"{tmp}/program")
        except ValueError:
            return None
    return "dspy.load accepted a pickled program without allow_pickle=True"


def p_saved_state_has_no_key():
    program = dspy.Predict("q -> a")
    program.set_lm(dspy.LM("openrouter/probe", api_key="PROBE-KEY", cache=False))
    return None if "PROBE-KEY" not in repr(program.dump_state()) else "dump_state() wrote the api_key"


def p_example_reaches_evaluator_by_name():
    import gepa.optimize_anything as oa
    got = {}

    def good(candidate, example):
        got["example"] = example
        return 1.0

    def renamed(candidate, task):
        return 1.0

    oa.EvaluatorWrapper(good, single_instance_mode=False)({"text": "c"}, example={"x": 1})
    if got.get("example") != {"x": 1}:
        return "an evaluator whose parameter is named `example` did not receive the example"
    try:
        oa.EvaluatorWrapper(renamed, single_instance_mode=False)({"text": "c"}, example={"x": 1})
    except TypeError:
        return None
    return "an evaluator without an `example` parameter was called without error"


def _need_deno() -> NotRun | None:
    """dspy.RLM runs in a Deno sandbox, and the `dspy[deno]` extra installs the runtime."""
    try:
        import deno  # noqa: F401
    except ImportError:
        return NotRun("no Deno — uv pip install --python .venv-dspy/bin/python 'dspy[deno,numpy]==3.3.1'")
    return None


def p_rlm_runs_offline():
    if (skip := _need_deno()) is not None:
        return skip
    step = chat(reasoning="Ich lese.", code="SUBMIT(candidates='- Kern-Welt  ^[L1]')")
    with offline(FixtureLM(lambda messages: step)):
        out = dspy.RLM("document: str, task: str -> candidates: str", max_iters=2, max_llm_calls=3)(
            document="L1| Die Kern-Welt ist eine Welt.", task="list the terms")
    return None if out.candidates == "- Kern-Welt  ^[L1]" else f"RLM returned {out.candidates!r}"


def p_rlm_forced_final_output():
    from rlm_ingest import FORCED  # the constant rlm_ingest.judge() reads
    if (skip := _need_deno()) is not None:
        return skip
    never_submits = fill(reasoning="Ich lese weiter.", code="print(len(document))",
                         candidates="- Kern-Welt  ^[L1]")
    with offline(FixtureLM(never_submits)):
        out = dspy.RLM("document: str, task: str -> candidates: str", max_iters=1, max_llm_calls=3)(
            document="L1| Die Kern-Welt ist eine Welt.", task="list the terms")
    if out.final_reasoning != FORCED:
        return f"an RLM out of iterations reported final_reasoning {out.final_reasoning!r}"
    return None if out.candidates == "- Kern-Welt  ^[L1]" else "the forced answer did not look like an answer"


class _EveryAttemptFails(dspy.Module):
    def __init__(self):
        super().__init__()
        self.predict = dspy.Predict("q -> a")

    def forward(self, q):
        raise RuntimeError("attempt failed")


def p_refine_none_when_all_fail():
    got = {}
    for cls in (dspy.BestOfN, dspy.Refine):
        for n in (2, 3):
            with offline(FixtureLM(fill(a="x", discussion="d", advice="{}"))):
                try:
                    got[(cls.__name__, n)] = cls(module=_EveryAttemptFails(), N=n,
                                                  reward_fn=lambda args, pred: 1.0, threshold=1.0)(q="?")
                except RuntimeError:
                    got[(cls.__name__, n)] = "raised"
    want = {("BestOfN", 2): None, ("BestOfN", 3): "raised", ("Refine", 2): None, ("Refine", 3): "raised"}
    return None if got == want else f"every attempt failing gave {got}, expected {want}"


PROBES = {
    "evaluate-score-percent": p_evaluate_score_percent,
    "evaluate-failure-is-zero": p_evaluate_failure_is_zero,
    "metric-dict-crashes": p_metric_dict_crashes,
    "metric-prediction-aggregates": p_metric_prediction_aggregates,
    "gepa-asserts-reflection-lm": gepa_needs_reflection_lm,
    "gepa-light-budget": p_gepa_light_budget,
    "labeledfewshot-fixed-seed": p_labeledfewshot_fixed_seed,
    "simba-trainset-below-bsize": p_simba_trainset_below_bsize,
    "bootstrap-keeps-wrong-demos-on-prediction": p_bootstrap_keeps_wrong_demos_on_prediction,
    "inferrules-halves-trainset": p_inferrules_halves_trainset,
    "chat-adapter-json-fallback": p_chat_adapter_json_fallback,
    "unparseable-is-adapter-error": p_unparseable_is_adapter_error,
    "literal-out-of-set-unparsed": p_literal_out_of_set_unparsed,
    "refused-connection-is-transport-error": p_refused_connection_is_transport_error,
    "load-refuses-pickle": p_load_refuses_pickle,
    "numpy-typing-after-dspy": p_numpy_typing_after_dspy,
    "track-usage-misses-threads": p_track_usage_misses_threads,
    "saved-state-has-no-key": p_saved_state_has_no_key,
    "example-reaches-evaluator-by-name": p_example_reaches_evaluator_by_name,
    "rlm-runs-offline": p_rlm_runs_offline,
    "rlm-forced-final-output": p_rlm_forced_final_output,
    "refine-none-when-all-fail": p_refine_none_when_all_fail,
}


def behaviour(texts: dict[str, str], probes: dict = PROBES) -> tuple[int, int, list[str]]:
    """(held, not run, problems). Marks and probes must match both ways."""
    cited = {m for text in texts.values() for m in MARK.findall(text)}
    problems = [f"the skill cites [checked: {m}] and no probe exists" for m in sorted(cited - set(probes))]
    problems += [f"probe {p!r} is cited nowhere in the skill" for p in sorted(set(probes) - cited)]
    held = unrun = 0
    for name in sorted(cited & set(probes)):
        try:
            outcome = probes[name]()
        except Exception as error:  # a probe that crashes has failed, loudly
            outcome = f"probe crashed: {type(error).__name__}: {error}"[:300]
        if outcome is None:
            held += 1
        elif isinstance(outcome, NotRun):
            unrun += 1
            problems.append(f"{name}: not run — {outcome}")
        else:
            problems.append(f"{name}: {outcome}")
    return held, unrun, problems


# --- 3 · paths -----------------------------------------------------------------------

def paths(texts: dict[str, str], root: Path = ROOT) -> tuple[int, list[str]]:
    seen, problems, lengths = set(), [], {}
    for source, text in texts.items():
        for match in PATH.finditer(text):
            path, line = match.group(1), match.group(2)
            if any(c in path for c in "<>*{}"):
                continue
            seen.add((path, line))
            target = root / path
            if not target.exists():
                problems.append(f"{source}: `{path}` does not exist")
            elif line and target.is_file():
                if target not in lengths:
                    lengths[target] = len(target.read_text(encoding="utf-8").splitlines())
                if int(line) > lengths[target]:
                    problems.append(f"{source}: `{path}:{line}` is past the end of the file")
    return len(seen), problems


# --- the run --------------------------------------------------------------------------

def texts_of(folder: Path) -> dict[str, str]:
    return {str(p.relative_to(folder)): p.read_text(encoding="utf-8")
            for p in sorted(folder.rglob("*.md"))}


def run(folder: Path = SKILL) -> tuple[list[str], list[str]]:
    texts = texts_of(folder)
    callables, parameters, s_problems = surface(texts)
    held, unrun, b_problems = behaviour(texts)
    named, p_problems = paths(texts)
    lines = [
        f"surface    {callables} callables, {parameters} parameters, {len(s_problems)} disagreements",
        f"behaviour  {held} held, {unrun} not run, {len(b_problems) - unrun} failed or unmatched",
        f"paths      {named} named, {len(p_problems)} missing",
    ]
    return lines, s_problems + b_problems + p_problems


def selftest() -> tuple[int, list[str]]:
    """(cases run, failures). Each check fails on a skill built to break it, for the reason it names."""
    ran, failures = 0, []

    def expect(ok: bool, failure: str) -> None:
        nonlocal ran
        ran += 1
        if not ok:
            failures.append(failure)

    bad = {
        "a.md": "```surface\n"
                "dspy.RLM(signature, max_iters=20)\n"
                "dspy.RLM(max_iterations)\n"
                "dspy.LM(model, cache=False)\n"
                "dspy.LM(model cache)\n"
                "```\n"
                "A claim. [checked: no-such-probe]\n"
                "See `scripts/no_such_script.py` and `scripts/lmrun.py:99999`.\n",
    }
    _, _, problems = surface(bad)
    for needle in ("no parameter 'max_iterations'", "cache defaults to True", "unreadable surface line"):
        expect(any(needle in p for p in problems), f"surface: expected a problem naming {needle!r}, got {problems}")
    expect(not any("max_iters" in p for p in problems), "surface: a correct line was reported")
    _, _, problems = behaviour(bad, probes={"held": lambda: None, "unrun": lambda: NotRun("x")})
    for needle in ("no-such-probe", "'held' is cited nowhere"):
        expect(any(needle in p for p in problems), f"behaviour: expected a problem naming {needle!r}, got {problems}")
    held, unrun, problems = behaviour({"a.md": "[checked: unrun] [checked: held]"},
                                      probes={"held": lambda: None, "unrun": lambda: NotRun("no runtime")})
    expect((held, unrun) == (1, 1) and any("not run" in p for p in problems),
           f"behaviour: a probe that could not run was not reported as not run ({held}, {unrun})")
    _, problems = paths(bad)
    for needle in ("no_such_script.py` does not exist", "past the end"):
        expect(any(needle in p for p in problems), f"paths: expected a problem naming {needle!r}, got {problems}")
    return ran, failures


def report(problems: list[str]) -> int:
    for p in problems:
        print(f"  FAIL  {p}")
    return 1 if problems else 0


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        ran, problems = selftest()
        status = report(problems)
        print(f"check_dspy_skill: {ran - len(problems)} of {ran} cases hold "
              "(surface: wrong name, wrong default, unreadable, correct line; behaviour: unknown mark, "
              "uncited probe, not run; paths: missing file, line past the end)")
        return status
    if not SKILL.exists():
        print(f"no skill at {SKILL.relative_to(ROOT)}")
        return 1
    lines, problems = run()
    status = report(problems)
    for line in lines:
        print(line)
    print(f"DSPy {dspy.__version__}: the dspy skill {'holds' if not problems else 'does NOT hold'}")
    return status


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
