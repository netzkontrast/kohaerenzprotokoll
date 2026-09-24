"""Assert the DSPy surface this repository calls, and fail loudly when it moves.

`dspy.RLM` is upstream-experimental and was renamed once already
(`max_iterations` → `max_iters`, `interpreter` → `interpreter_factory`, in
3.3.0). Nothing re-checked it. A renamed keyword does not fail at import — it
fails in the middle of a paid run, or worse, is swallowed by `**kwargs`.

So this lists exactly what the scripts here pass to DSPy and asserts each
against the installed package with `inspect.signature`. It asserts **only what
is called** (the design's rule: a surface check that asserts things nobody uses
is a second, drifting description of DSPy).

Pattern from `netzkontrast/dspy-agent-skills` `scripts/check_dspy_surface.py`;
the list is this repository's own.

    .venv-dspy/bin/python scripts/check_dspy_surface.py
"""

from __future__ import annotations

import inspect
import sys

PIN = "3.3.1"

try:
    import dspy
except ImportError:
    sys.exit("no DSPy in this interpreter. Create it:\n"
             "  uv venv --python 3.11 .venv-dspy\n"
             f"  uv pip install --python .venv-dspy/bin/python 'dspy[numpy]=={PIN}'\n"
             "then run this with .venv-dspy/bin/python")

# (what, callable, parameters used here, who uses them)
USED = [
    ("dspy.LM", dspy.LM, {"model", "cache", "max_tokens", "temperature", "num_retries"},
     "lmrun.py, rlm_ingest.py"),
    ("dspy.RLM", dspy.RLM.__init__, {"signature", "max_iters", "max_llm_calls", "tools", "sub_lm"},
     "rlm_ingest.py"),
    ("dspy.LabeledFewShot", dspy.LabeledFewShot, {"k"}, "pairs.py ladder"),
    ("dspy.BootstrapFewShot", dspy.BootstrapFewShot,
     {"metric", "max_bootstrapped_demos", "max_labeled_demos"}, "pairs.py ladder"),
    ("dspy.InferRules", dspy.InferRules, {"num_candidates", "num_rules"}, "pairs.py ladder"),
    ("dspy.SIMBA", dspy.SIMBA, {"metric", "bsize", "num_candidates", "max_steps"}, "pairs.py ladder"),
    ("dspy.GEPA", dspy.GEPA, {"metric", "auto", "reflection_lm", "seed", "track_stats", "log_dir"},
     "pairs.py ladder"),
    ("dspy.Evaluate", dspy.Evaluate, {"devset", "metric", "num_threads", "failure_score"}, "pairs.py"),
    ("dspy.BaseLM", dspy.BaseLM.__init__, {"model", "cache"}, "lm_fixture.py"),
]


def params(obj) -> set[str]:
    return set(inspect.signature(obj).parameters)


def example_param_ok(evaluator) -> bool:
    """`gepa.optimize_anything` introspects its evaluator: the second parameter
    must be named `example`, or the data is dropped silently and the crash comes
    layers later (dspy-book-coding-agents/SKILL.md:59). Call this before handing
    any evaluator over."""
    names = list(inspect.signature(evaluator).parameters)
    return len(names) >= 2 and names[1] == "example"


def gepa_needs_reflection_lm() -> str | None:
    """`dspy.GEPA` asserts at construction that it has a reflection LM or an
    instruction proposer. None while that holds, else what moved. One
    encoding: `check_dspy_skill.py` cites it as `gepa-asserts-reflection-lm`."""
    try:
        dspy.GEPA(metric=lambda *a, **k: 0.0, auto="light")
    except AssertionError:
        return None
    return "dspy.GEPA constructed without reflection_lm — the gotcha it guards moved"


def run() -> list[str]:
    failures = []
    if dspy.__version__ != PIN:
        failures.append(f"DSPy {dspy.__version__} installed, {PIN} pinned — CLAUDE.md, .venv-dspy")
    for name, obj, used, who in USED:
        missing = sorted(used - params(obj))
        if missing:
            failures.append(f"{name} no longer takes {', '.join(missing)} (used by {who})")

    # Defaults this repository depends on being overridden, asserted so a changed
    # default is noticed rather than silently inherited.
    if inspect.signature(dspy.LM).parameters["cache"].default is not True:
        failures.append("dspy.LM cache default changed — lmrun.py sets cache=False explicitly; re-read why")
    bsize = inspect.signature(dspy.SIMBA).parameters["bsize"].default
    if bsize != 32:
        failures.append(f"dspy.SIMBA bsize default is {bsize}, the ladder note assumes 32 (> n=26)")
    if not hasattr(dspy, "track_usage"):
        failures.append("dspy.track_usage is gone — lmrun.py records cost through it")

    # Construction-time gotchas: asserted by behaviour, not by reading.
    if moved := gepa_needs_reflection_lm():
        failures.append(moved)

    try:
        import gepa.optimize_anything as oa
        if "evaluator" not in params(oa.optimize_anything):
            failures.append("gepa.optimize_anything no longer takes evaluator= (job 4)")
    except ImportError:
        failures.append("gepa is not importable; DSPy 3.3.1 installs it (job 4 needs optimize_anything)")

    try:
        import numpy  # noqa: F401
    except ImportError:
        failures.append("numpy missing — dspy.SIMBA raises without it; install dspy[numpy]==3.3.1")

    def good(candidate, example): ...  # noqa: E704
    def bad(candidate, task): ...  # noqa: E704
    if not example_param_ok(good) or example_param_ok(bad):
        failures.append("example_param_ok() cannot tell a good evaluator from a bad one")
    return failures


def main() -> int:
    failures = run()
    for f in failures:
        print(f"  FAIL  {f}")
    checked = len(USED) + 8  # version, three defaults, GEPA, gepa, numpy, example_param_ok
    print(f"DSPy {dspy.__version__}: {checked - len(failures)} of {checked} surface checks hold")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
