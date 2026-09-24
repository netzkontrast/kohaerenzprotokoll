"""An offline language model, so every model step can run with no key and no network.

P5 says a workflow ships a fixture that runs offline and free. For a DSPy step
that means a `dspy.BaseLM` that answers from a script, records what it was
asked, and **cannot reach the network even by accident**.

The accident is not hypothetical. Scanning `dspy-auto-gepa` on 2026-09-23, its
test `test_partial_explicit_fields_infer_rest` was unmocked, fell through to
the default LM, and made a live OpenRouter call from this container. A dry-run
that *can* reach the network is not a dry-run. So `offline()` does three
things, not one:

1. configures DSPy with the fixture,
2. removes every `*_API_KEY` from this process's environment, and
3. replaces `litellm.completion` with a function that raises — so a step that
   builds its own `dspy.LM` behind the fixture's back fails loudly instead of
   calling out.

Ported from `netzkontrast/dspy-optimizer` `tests/conftest.py` (`MockLLM`, the
response shape) and `netzkontrast/dspy-agents` `tests/test_dspy_config.py`
(`RecorderLM`, the recording). Verified against DSPy 3.3.1.

    from lm_fixture import FixtureLM, chat, offline
    lm = FixtureLM(lambda messages: chat(decision="one-term", rule="…"))
    with offline(lm):
        program(first="Riss", second="Risse")
    lm.requests   # every request, in order

Runs only in `.venv-dspy`; `python3 scripts/lm_fixture.py` with that
interpreter is its own test.
"""

from __future__ import annotations

import contextlib
import os
import re
import sys
from types import SimpleNamespace
from typing import Callable, Iterator

try:
    import dspy
except ImportError:  # pragma: no cover - says how to fix it rather than a traceback
    sys.exit("lm_fixture needs DSPy: uv venv --python 3.11 .venv-dspy && "
             "uv pip install --python .venv-dspy/bin/python dspy==3.3.1")


class NetworkRefused(RuntimeError):
    """A step tried to call a real model while `offline()` was in force."""


def chat(**fields: str) -> str:
    """A completion in ChatAdapter's own format: one `[[ ## field ## ]]` per output."""
    body = "\n\n".join(f"[[ ## {k} ## ]]\n{v}" for k, v in fields.items())
    return f"{body}\n\n[[ ## completed ## ]]"


_OUTPUTS = re.compile(r"Your output fields are:\n(.*?)\nAll interactions", re.S)
_FIELD = re.compile(r"^\d+\. `(\w+)` \(([^)]*)\)", re.M)


def fill(**values: str) -> Callable[[list], str]:
    """A responder that answers *whatever* output fields the prompt asks for.

    An optimizer's own prompts (InferRules proposing rules, GEPA reflecting) ask
    for fields the task never declared. `fill` reads them from ChatAdapter's
    system message and answers each: the value given here by name, else an
    empty list for a list type, else a marked placeholder. So a dry-run reaches
    every optimizer's internal calls instead of dying on the first unknown one.
    """
    def respond(messages: list) -> str:
        system = next((m["content"] for m in messages if m.get("role") == "system"), "")
        block = _OUTPUTS.search(system)
        fields = _FIELD.findall(block.group(1)) if block else []
        out = {}
        for name, kind in fields:
            out[name] = values.get(name, "[]" if kind.startswith("list") else f"(fixture: {name})")
        return chat(**out) if out else chat(**values)
    return respond


class FixtureLM(dspy.BaseLM):
    """Answers from `respond(messages) -> str`, or from a list consumed in order.

    Every request is kept in `self.requests`. A script that runs out raises
    rather than repeating its last answer, because a repeated answer is how a
    fixture quietly stops testing what it claims to.
    """

    def __init__(self, respond: Callable[[list], str] | list[str], model: str = "fixture/offline"):
        super().__init__(model=model, cache=False)
        self._respond = respond
        self._script = list(respond) if isinstance(respond, list) else None
        self.requests: list[dict] = []

    def forward(self, prompt=None, messages=None, **kwargs):
        messages = messages or [{"role": "user", "content": prompt or ""}]
        self.requests.append({"messages": messages, "kwargs": kwargs})
        if self._script is not None:
            if not self._script:
                raise AssertionError(f"FixtureLM script exhausted after {len(self.requests) - 1} answers")
            text = self._script.pop(0)
        else:
            text = self._respond(messages)
        choice = SimpleNamespace(
            message=SimpleNamespace(content=text, tool_calls=None),
            logprobs=None, finish_reason="stop")
        response = SimpleNamespace(
            choices=[choice], model=self.model,
            usage={"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0})
        response._hidden_params = {"response_cost": 0.0}
        return response


def _refuse(*args, **kwargs):
    raise NetworkRefused("a real model call was attempted inside offline() — "
                         "a step built its own dspy.LM instead of using the configured one")


@contextlib.contextmanager
def offline(lm: dspy.BaseLM) -> Iterator[dspy.BaseLM]:
    """Configure `lm`, hide every API key, and make any real completion raise."""
    import litellm
    hidden = {k: os.environ.pop(k) for k in list(os.environ) if k.endswith("_API_KEY")}
    saved = (litellm.completion, litellm.acompletion)
    litellm.completion = litellm.acompletion = _refuse
    try:
        with dspy.context(lm=lm):
            yield lm
    finally:
        litellm.completion, litellm.acompletion = saved
        os.environ.update(hidden)


def selftest() -> list[str]:
    """The fixture answers, records, and refuses — each asserted, not assumed."""
    failures = []
    keys_before = sorted(k for k in os.environ if k.endswith("_API_KEY"))
    lm = FixtureLM(lambda messages: chat(answer="ja"))
    with offline(lm):
        out = dspy.Predict("question -> answer")(question="Ist das offline?")
    if out.answer != "ja":
        failures.append(f"fixture answer not parsed: {out.answer!r}")
    if len(lm.requests) != 1 or "Ist das offline?" not in str(lm.requests[0]["messages"]):
        failures.append("fixture did not record the request it was sent")

    with offline(FixtureLM([])):
        try:
            with dspy.context(lm=dspy.LM("openrouter/any/model", cache=False)):
                dspy.Predict("question -> answer")(question="x")
            failures.append("a real dspy.LM ran inside offline() — the network guard is open")
        except Exception as error:  # the refusal may arrive wrapped by the adapter
            if "offline()" not in f"{error!r}{error.__cause__!r}{error.__context__!r}":
                failures.append(f"real LM failed, but not by the guard: {error!r}")
    if sorted(k for k in os.environ if k.endswith("_API_KEY")) != keys_before:
        failures.append("the environment's keys were not restored after offline()")

    script = FixtureLM([chat(answer="eins")])
    with offline(script):
        dspy.Predict("question -> answer")(question="a")
        try:
            dspy.Predict("question -> answer")(question="b")
            failures.append("an exhausted script answered anyway")
        except Exception:
            pass
    return failures


if __name__ == "__main__":
    problems = selftest()
    for p in problems:
        print(f"  FAIL  {p}")
    print(f"lm_fixture: {3 - len(problems)} of 3 cases hold (answer+record, refuse network, exhausted script)")
    raise SystemExit(1 if problems else 0)
