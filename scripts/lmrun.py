"""Every model call here goes through this, and leaves its evidence on disk.

`continuous-improvement_2026-09-17.md` names the first blocker to any model
loop: **a judgement records its rule and not its evidence.** And the catalogue
has kept a `--trace` idea since the reset: raw model output kept aside, because
you cannot reduce a cost you cannot see. This is both.

One call, one record, appended to `Plan/runs/<subject>/lm/<step>.jsonl`:

| field | why |
|---|---|
| `inputs`, `outputs` | what the program was given and what it returned, frozen at call time — never reconstructed later (dspy-session's `Turn`) |
| `raw` | the model's own text, from `lm.history`, before any parsing |
| `finish_reason`, `usage`, `cost`, `model` | a reasoning model that spent its budget returns `content: None, finish_reason: length` and no error (P19) |
| `status` | `answered`, `refused`, `unparsed` or `unreachable` — **never a score** (P15). A 404 is not a wrong answer |
| `problems` | empty fields; German expected and not found; German *unmeasurable* (too short to tell) said as such (P23) |
| `approval` | which decision allowed this text to leave the container |

Three refusals are built in, because each is a rule this project already has
and no scanned repository enforced:

- **cache on** — a cached call replays the first completion, and an
  unreliable model scores 100% (P18). `make_lm()` builds with `cache=False`;
  `call()` refuses an LM whose cache is on.
- **no approval** — corpus text goes to a third party only when the author has
  said yes to *that* run (`NOW.md`). A real LM needs `approval=` naming the
  decision. The offline fixture needs none.
- **a `History`-carrying wrapper around `dspy.RLM`** is not offered at all:
  `dspy-session`'s own `docs/rlm.md` records RLM failing on every iteration
  with „Unsupported value type: History" — on DSPy 3.1.3. On 3.3.1 the same
  wrapper fails at once, „Unexpected inputs not declared in the signature"
  (re-read 2026-09-24, `Plan/concept/dspy-extract_2026-09-24/`).

Ported: `dspy.track_usage()` around each call (dspy-agents
`compile_rag.py:85-87`), `{"event": …, **state}` appended per call
(dspy-optimizer `HistoryCallback._log_event`), the language markers
(dspy-wiki-compile `language_kept`, with the length guard it lacked).

    from lmrun import make_lm, call
    lm = make_lm("openrouter/…")                       # cache off
    with dspy.context(lm=lm):
        pred, rec = call(program, step="pairs", subject="surface-pairs",
                         approval="NOW.md 2026-09-23 …", german=["rule"], first=…, second=…)

    .venv-dspy/bin/python scripts/lmrun.py   # the offline self-test
"""

from __future__ import annotations

import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "Plan" / "runs"
sys.path.insert(0, str(ROOT / "scripts"))

import dspy  # noqa: E402

STATUSES = ("answered", "refused", "unparsed", "unreachable")
MARKERS = {"de": (" der ", " die ", " das ", " und ", " nicht ", " ist ", " ein ", " eine "),
           "en": (" the ", " and ", " not ", " is ", " of ", " with ", " a ", " an ")}
MIN_WORDS_FOR_LANGUAGE = 8


def make_lm(model: str, **kwargs) -> dspy.LM:
    """A real LM, built the only way this repository builds one: cache off."""
    kwargs.pop("cache", None)
    return dspy.LM(model, cache=False, **kwargs)


def language(text: str, expected: str = "de") -> str:
    """`ok`, `wrong`, or `unmeasured` — a short answer is not evidence of either."""
    words = re.findall(r"\w+", text)
    if len(words) < MIN_WORDS_FOR_LANGUAGE:
        return "unmeasured"
    padded = f" {text.lower()} "
    own = sum(padded.count(m) for m in MARKERS[expected])
    other = sum(padded.count(m) for lang, ms in MARKERS.items() if lang != expected for m in ms)
    if own == other == 0:
        return "unmeasured"
    return "ok" if own >= other else "wrong"


def _is_fixture(lm) -> bool:
    return type(lm).__name__ == "FixtureLM"


# DSPy 3.3 wraps every provider and network failure in its own typed errors, so
# the litellm names below are no longer what reaches the caller. Measured
# 2026-09-24: a closed local port raised `dspy.LMTransportError` and `call()`
# re-raised it instead of recording `unreachable` — the selftest only ever
# raised the fixture's own `NetworkRefused`. Everything under `LMProviderError`
# (auth, billing, rate limit, server, timeout, invalid request, context window)
# or `LMTransportError` means no answer came back. `LMConfigurationError` and
# `LMUnsupportedFeatureError` are this repository's own mistakes and still raise.
# The name set below stays for what DSPy does not wrap: the fixture's own
# `NetworkRefused`, and anything raised outside `dspy.LM.forward`.
_NO_ANSWER = tuple(getattr(dspy, n) for n in ("LMProviderError", "LMTransportError") if hasattr(dspy, n))


def _unreachable(error: BaseException) -> bool:
    chain = [e for e in (error, error.__cause__, error.__context__) if e]
    if any(isinstance(e, _NO_ANSWER) for e in chain):
        return True
    names = {type(e).__name__ for e in chain}
    return bool(names & {"NetworkRefused", "APIConnectionError", "NotFoundError",
                         "AuthenticationError", "RateLimitError", "ServiceUnavailableError",
                         "Timeout", "ConnectionError", "PermissionDeniedError"})


def call(program, *, step: str, subject: str = "lm", approval: str | None = None,
         german: list[str] | tuple[str, ...] = (), out_dir: Path | None = None, **inputs):
    """Run `program(**inputs)` once and record it. Returns (prediction or None, record)."""
    lm = dspy.settings.lm
    if lm is None:
        raise RuntimeError("no LM configured — use dspy.context(lm=make_lm(...)) or lm_fixture.offline()")
    if not _is_fixture(lm):
        if getattr(lm, "cache", True):
            raise RuntimeError(f"{lm.model}: cache is on. Build it with lmrun.make_lm() — "
                               "a cached call replays its first answer (P18)")
        if not approval:
            raise RuntimeError(f"{lm.model}: no approval= given. Name the author's decision that "
                               "lets this text leave the container (NOW.md)")

    before = len(lm.history)
    started = time.time()
    prediction, status, error = None, "answered", None
    with dspy.track_usage() as usage:
        try:
            prediction = program(**inputs)
        except Exception as exc:  # classified, never swallowed into a score
            error = f"{type(exc).__name__}: {exc}"[:500]
            if _unreachable(exc):
                status = "unreachable"
            elif "Adapter" in type(exc).__name__ or "parse" in str(exc).lower():
                status = "unparsed"
            else:
                raise
    entries = lm.history[before:]

    raw, finish = [], []
    for entry in entries:
        for choice in getattr(entry.get("response"), "choices", []) or []:
            message = getattr(choice, "message", None)
            raw.append(getattr(message, "content", None))
            finish.append(getattr(choice, "finish_reason", None))

    outputs = dict(prediction.items()) if prediction is not None else {}
    problems = []
    # P19 before parsing: no content, or a budget spent on reasoning, is a refusal
    # whatever the adapter made of it afterwards.
    if status != "unreachable" and (not raw or all(not r for r in raw)
                                    or any(f == "length" for f in finish)):
        status = "refused"
        problems.append(f"empty content or budget exhausted (finish_reason {finish})")
    if status == "answered":
        for name, value in outputs.items():
            if value in (None, "", []):
                problems.append(f"output {name!r} is empty")
        for name in german:
            verdict = language(str(outputs.get(name, "")), "de")
            if verdict != "ok":
                problems.append(f"output {name!r}: German {verdict}")

    record = {
        "event": "lm_call", "step": step, "subject": subject,
        "at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "model": getattr(lm, "model", "?"), "fixture": _is_fixture(lm),
        "approval": approval, "status": status, "error": error,
        "inputs": {k: str(v) for k, v in inputs.items()},
        "outputs": {k: str(v) for k, v in outputs.items()},
        "raw": raw, "finish_reason": finish,
        "usage": usage.get_total_tokens() if usage else {},
        "cost": sum(e.get("cost") or 0 for e in entries),
        "seconds": round(time.time() - started, 2),
        "problems": problems,
    }
    target = (out_dir or RUNS / subject / "lm") / f"{step}.jsonl"
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, ensure_ascii=False, default=str) + "\n")
    return prediction, record


def selftest() -> list[str]:
    """Each of the four statuses, and each refusal, produced offline and asserted."""
    import tempfile
    from lm_fixture import FixtureLM, NetworkRefused, chat, offline

    failures = []
    prog = dspy.Predict("frage -> antwort")
    german = "Das ist eine Antwort, die nicht nur kurz ist und die deutsche Sprache trägt."
    cases = [
        ("answered", FixtureLM([chat(antwort=german)]), []),
        ("unparsed", FixtureLM(["kein format", "immer noch kein format", "nein"]), []),
        ("refused", FixtureLM(lambda messages: ""), ["empty content"]),
        ("answered", FixtureLM([chat(antwort="")]), ["'antwort' is empty"]),
        ("answered", FixtureLM([chat(antwort="This is an answer that is long enough to be measured as English.")]),
         ["German wrong"]),
    ]

    def unreachable(messages):
        raise NetworkRefused("offline")
    cases.append(("unreachable", FixtureLM(unreachable), []))

    def provider_down(messages):  # what DSPy 3.3 raises for a refused connection
        raise dspy.LMTransportError("connection refused", model="fixture")
    cases.append(("unreachable", FixtureLM(provider_down), []))

    with tempfile.TemporaryDirectory() as tmp:
        for expected, lm, needles in cases:
            with offline(lm):
                try:
                    _, rec = call(prog, step="selftest", german=["antwort"], out_dir=Path(tmp), frage="?")
                except Exception as exc:  # a case that raises has failed; it must not end the suite
                    failures.append(f"expected {expected}, call raised {type(exc).__name__}: {exc}"[:200])
                    continue
            if rec["status"] != expected:
                failures.append(f"expected {expected}, got {rec['status']} ({rec['error'] or rec['problems']})")
            for needle in needles:
                if not any(needle in p for p in rec["problems"]):
                    failures.append(f"{expected}: no problem naming {needle!r} in {rec['problems']}")
        written = (Path(tmp) / "selftest.jsonl").read_text().count("\n")
        if written != len(cases):
            failures.append(f"{len(cases)} calls, {written} records written")

    cached = dspy.LM("openrouter/x/y")  # cache on by default, never called
    with dspy.context(lm=cached):
        try:
            call(prog, step="x", approval="test", frage="?")
            failures.append("a cached LM was accepted")
        except RuntimeError as exc:
            if "cache" not in str(exc):
                failures.append(f"cached LM refused for the wrong reason: {exc}")
    with dspy.context(lm=make_lm("openrouter/x/y")):
        try:
            call(prog, step="x", frage="?")
            failures.append("a real LM ran without approval")
        except RuntimeError as exc:
            if "approval" not in str(exc):
                failures.append(f"unapproved LM refused for the wrong reason: {exc}")
    if language("ja") != "unmeasured":
        failures.append("a one-word answer was judged for language instead of unmeasured")
    return failures


if __name__ == "__main__":
    problems = selftest()
    for p in problems:
        print(f"  FAIL  {p}")
    total = 10
    print(f"lmrun: {total - len(problems)} of {total} cases hold "
          "(4 statuses, DSPy's own transport error, empty field, English caught, cache refused, "
          "approval refused, short text unmeasured)")
    raise SystemExit(1 if problems else 0)
