#!/usr/bin/env python3
"""Measure candidate LMs on this repository's own typed program.

    scripts/lm_bench.py --models openrouter/deepseek/deepseek-chat,openrouter/qwen/qwen-2.5-72b-instruct
    scripts/lm_bench.py --models-file Plan/quality/lm-candidates.txt --repeats 3
    scripts/lm_bench.py --models … --json > Plan/quality/lm-bench_2026-09-16.json

Run it with the DSPy virtualenv: ``.venv-dspy/bin/python scripts/lm_bench.py …``

WHAT IT MEASURES, AND WHY THIS TASK

Every kpwiki program is a typed DSPy Signature with closed enums, and the way a
weak model fails is not a wrong answer — it is prose where a schema belongs. So
the benchmark runs ``SourceIngest`` on the fixture that ``tools/kpwiki/smoke.py``
already defines and scores the result with ``ingest_metric``, the same metric a
real run is judged by. There is no benchmark-specific task and no second copy of
the scoring rules: a model that scores here scores on the real workload.

Four numbers per model:

    structure   schema-valid share of the attempts that actually reached the
                model. A parse failure or a refusal counts against it and is the
                number that disqualifies a model regardless of the rest. A model
                the provider never served is reported separately as NEVER REACHED
                rather than as 0%: "would not answer" and "answered badly" are
                different findings, and only the second is about the model.
    score       mean ``ingest_metric`` score over the attempts that survived, so
                it is quality *given* valid structure — read it together with
                ``structure``, never alone.
    latency     median wall-clock seconds per attempt.
    cost        total USD as LiteLLM prices it, or 0.0 for a free model. A model
                LiteLLM has no price table for reports cost as ``None``, not 0.

Models run concurrently, one thread each, through ``dspy.context`` — which
``tools/kpwiki/lm.py`` documents as the thread-safe override. Repeats of one
model run in sequence inside its thread, so a rate-limited model slows only
itself. ``--repeats`` above 1 is what makes ``structure`` meaningful: a single
attempt cannot distinguish a model that always emits a schema from one that does
so half the time.

Caching is off. DSPy's disk cache would return the first attempt's completion for
every repeat and turn a reliability measurement into one sample copied N times.

The output ranks models; it does not choose one. Which model earns which role is
the author's call, and a cheap model that is merely adequate on ``worker`` is a
different decision from one that is adequate on ``task``.
"""
from __future__ import annotations

import argparse
import json
import os
import statistics
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import dspy  # noqa: E402  (after sys.path so the repo's tools/ package is importable)

from tools.kpwiki import lm  # noqa: E402
from tools.kpwiki.metrics import ingest_metric  # noqa: E402
from tools.kpwiki.programs import SourceIngest  # noqa: E402
from tools.kpwiki.smoke import fixture_example  # noqa: E402

TASK_MAX_TOKENS = lm.TASK_MAX_TOKENS


# A model that was never reached has not been measured. Conflating "the provider
# would not serve it" with "it cannot hold the schema" is the one way this tool
# can actively mislead, so transport failures are classified and reported apart.
UNAVAILABLE_MARKERS = (
    "LMUnsupportedModelError", "LMAuthError", "NotFoundError", "AuthenticationError",
    "RateLimitError", "Timeout", "APIConnectionError", "ServiceUnavailable",
    "only available on", "Provider returned error", "No endpoints found",
)


def classify(exc: Exception) -> str:
    """`unavailable` when the model was never reached, else `schema`."""
    text = f"{type(exc).__name__}: {exc}"
    return "unavailable" if any(m in text for m in UNAVAILABLE_MARKERS) else "schema"


@dataclass
class Attempt:
    """One run of the program against one model."""

    ok: bool
    kind: str = "ok"  # ok | schema | unavailable
    score: float = 0.0
    seconds: float = 0.0
    prompt_tokens: int = 0
    completion_tokens: int = 0
    cost: float | None = None
    error: str = ""


@dataclass
class ModelResult:
    """Every attempt for one model, plus the aggregates the table prints."""

    model: str
    attempts: list[Attempt] = field(default_factory=list)

    @property
    def valid(self) -> list[Attempt]:
        return [a for a in self.attempts if a.ok]

    @property
    def reached(self) -> list[Attempt]:
        """Attempts that actually got a response out of the model."""
        return [a for a in self.attempts if a.kind != "unavailable"]

    @property
    def structure_rate(self) -> float | None:
        """Schema-valid share of the attempts that reached the model, or None if none did."""
        return len(self.valid) / len(self.reached) if self.reached else None

    @property
    def mean_score(self) -> float:
        return statistics.fmean([a.score for a in self.valid]) if self.valid else 0.0

    @property
    def median_seconds(self) -> float:
        return statistics.median([a.seconds for a in self.attempts]) if self.attempts else 0.0

    @property
    def total_cost(self) -> float | None:
        priced = [a.cost for a in self.valid if a.cost is not None]
        return sum(priced) if priced else None

    @property
    def first_error(self) -> str:
        return next((a.error for a in self.attempts if not a.ok), "")


def _usage_totals(prediction) -> tuple[int, int]:
    """Sum prompt and completion tokens across every LM call the prediction made."""
    prompt = completion = 0
    for entry in (prediction.get_lm_usage() or {}).values():
        prompt += entry.get("prompt_tokens", 0) or 0
        completion += entry.get("completion_tokens", 0) or 0
    return prompt, completion


def _price(model: str, prompt_tokens: int, completion_tokens: int) -> float | None:
    """USD for this many tokens, or None when LiteLLM has no price table for the model."""
    try:
        from litellm import cost_per_token

        prompt_cost, completion_cost = cost_per_token(
            model=model, prompt_tokens=prompt_tokens, completion_tokens=completion_tokens)
        return prompt_cost + completion_cost
    except Exception:
        return None


def run_attempt(model: str, example: dspy.Example) -> Attempt:
    """Run SourceIngest once on `model` and score it. Never raises."""
    candidate = dspy.LM(model, temperature=0.0, max_tokens=TASK_MAX_TOKENS, cache=False)
    started = time.monotonic()
    try:
        with dspy.context(lm=candidate, track_usage=True):
            prediction = SourceIngest()(**example.inputs())
        elapsed = time.monotonic() - started
        result = ingest_metric(example, prediction)
        prompt_tokens, completion_tokens = _usage_totals(prediction)
        return Attempt(
            ok=True, score=float(result.score), seconds=elapsed,
            prompt_tokens=prompt_tokens, completion_tokens=completion_tokens,
            cost=_price(model, prompt_tokens, completion_tokens))
    except Exception as exc:  # a model that cannot hold the schema is a result, not a crash
        return Attempt(ok=False, kind=classify(exc), seconds=time.monotonic() - started,
                       error=f"{type(exc).__name__}: {exc}"[:200])


def bench_model(model: str, repeats: int, example: dspy.Example) -> ModelResult:
    """Run one model `repeats` times in sequence, so its rate limit slows only itself."""
    result = ModelResult(model=model)
    for _ in range(repeats):
        result.attempts.append(run_attempt(model, example))
    return result


def bench(models: list[str], repeats: int, workers: int) -> list[ModelResult]:
    """Run every model concurrently and return results in the order requested."""
    example = fixture_example()
    with ThreadPoolExecutor(max_workers=min(workers, len(models))) as pool:
        return list(pool.map(lambda m: bench_model(m, repeats, example), models))


def _cost_cell(result: ModelResult) -> str:
    if result.total_cost is None:
        return "     n/a"
    return "    free" if result.total_cost == 0 else f"${result.total_cost:7.4f}"


def print_table(results: list[ModelResult], repeats: int) -> None:
    measured = [r for r in results if r.structure_rate is not None]
    unreachable = [r for r in results if r.structure_rate is None]
    ranked = sorted(measured, key=lambda r: (r.structure_rate, r.mean_score), reverse=True)

    print(f"\n{'model':52s} {'structure':>9s} {'score':>6s} {'median s':>9s} {'cost':>9s}")
    print("-" * 90)
    for result in ranked:
        print(f"{result.model:52s} {result.structure_rate:8.0%} {result.mean_score:6.2f} "
              f"{result.median_seconds:9.1f} {_cost_cell(result)}")
    print("-" * 90)
    print(f"{repeats} attempt(s) per model · structure = schema-valid share of the attempts "
          f"that reached the model · score = mean ingest_metric over those")
    for result in ranked:
        if result.first_error:
            print(f"  ! {result.model}: {result.first_error}")

    if unreachable:
        print("\nNEVER REACHED — not measured, and not a verdict on the model:")
        for result in unreachable:
            print(f"  · {result.model}\n      {result.first_error}")

    print("\nThis ranks; it does not choose. Assign roles with KP_LM_TASK / "
          "KP_LM_WORKER / KP_LM_REFLECTION.")


def as_json(results: list[ModelResult], repeats: int) -> str:
    return json.dumps({
        "repeats": repeats,
        "task": "SourceIngest on tools/kpwiki/smoke.py fixture, scored by ingest_metric",
        "models": [{
            "model": r.model,
            "structure_rate": r.structure_rate,
            "mean_score": r.mean_score,
            "median_seconds": r.median_seconds,
            "total_cost_usd": r.total_cost,
            "attempts": [vars(a) for a in r.attempts],
        } for r in results],
    }, indent=2)


def resolve_models(args: argparse.Namespace) -> list[str]:
    if args.models_file:
        lines = Path(args.models_file).read_text(encoding="utf-8").splitlines()
        names = [line.strip() for line in lines if line.strip() and not line.startswith("#")]
    else:
        names = [name.strip() for name in args.models.split(",") if name.strip()]
    if not names:
        raise SystemExit("no models given; pass --models or --models-file")
    return names


def check_keys(models: list[str]) -> None:
    """Fail before spending time when a named provider has no key in the environment."""
    missing = sorted({
        key for model in models
        if (key := lm.PROVIDER_KEY_ENV.get(model.split("/", 1)[0])) and not os.environ.get(key)
    })
    if missing:
        raise SystemExit(f"missing API key(s): {', '.join(missing)} — export them and re-run")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--models", help="comma-separated LiteLLM provider/model strings")
    source.add_argument("--models-file", help="file with one model per line; # comments allowed")
    parser.add_argument("--repeats", type=int, default=3,
                        help="attempts per model; >1 is what makes `structure` meaningful")
    parser.add_argument("--workers", type=int, default=4, help="models benchmarked concurrently")
    parser.add_argument("--json", action="store_true", help="emit JSON instead of the table")
    args = parser.parse_args(argv)

    models = resolve_models(args)
    check_keys(models)
    results = bench(models, args.repeats, args.workers)
    print(as_json(results, args.repeats)) if args.json else print_table(results, args.repeats)
    return 0


if __name__ == "__main__":
    sys.exit(main())
