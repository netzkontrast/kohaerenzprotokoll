"""Claude as a DSPy model, through the Claude Code CLI — first party, no key, no tools.

Every other real model a DSPy script here could call sends corpus words to a
third party, which is why each waits on the author's yes (`NOW.md`). This
repository already treats one model differently: **Claude**. Document 14's second
readers ran „with Claude as the model so no text left", and the entity-list
readers are Haiku subagents. Decision 011 applies that precedent to DSPy: a
program may use Claude through the `claude` CLI that runs this session.

`ClaudeCLI` is a `dspy.BaseLM` on the legacy forward contract (the one
`lm_fixture.FixtureLM` uses). Each call is one headless `claude -p`:

- **no tools** (`--tools ""`), no MCP servers, no skills, no settings files,
  no session written, and an empty working directory, so no `CLAUDE.md` is
  discovered and the model sees the prompt DSPy built and nothing else;
- DSPy's system message becomes `--system-prompt`, which replaces Claude Code's
  own; the conversation goes in on stdin. Few-shot demos arrive as user and
  assistant turns, and the CLI takes no assistant turn, so they are written
  out as numbered examples, each message with the reply given to it;
- usage and `total_cost_usd` come from the CLI's JSON and reach `lm.history`,
  so `lmrun` records them and a run can add up what it cost;
- a failure is one of DSPy 3.3's own types — a timeout `LMTimeoutError`, a
  failed or error-marked call `LMServerError` or `LMRateLimitError`, an
  unreadable reply `LMTransportError` — which `lmrun.call` records as
  `unreachable` (P15); a missing binary is `LMNotConfiguredError`, this
  repository's own mistake, and raises.

**No thinking unless asked.** `thinking=0` (the default) sets `MAX_THINKING_TOKENS=0`
for the child. Measured 2026-09-25 on Haiku 4.5 with the ladder's prompt: with
`--effort low` alone, 18 calls spent 590–3,282 output tokens on a one-sentence
answer, 8–35 s and $0.005–0.018 each; with the budget at 0, 153 calls spent
42–131 tokens, 2.4–3.9 s and $0.0024 on average. A reflection model is built with
`thinking=None`, the CLI's own default.

**No temperature, no cache.** The CLI takes no sampling parameters, so repeats
measure the model at its own default; there is no response cache to turn off
(P18). `cache=False` is set anyway, because `lmrun.call` refuses an LM without it.

    from claude_lm import ClaudeCLI
    lm = ClaudeCLI("haiku")                       # or via lmrun.make_lm("claude-cli/haiku")
    with dspy.context(lm=lm):
        pred, rec = lmrun.call(program, step=…, approval="decision 011", …)

    .venv-dspy/bin/python scripts/claude_lm.py        # the offline self-test, a fake `claude`
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from types import SimpleNamespace

import dspy

# Removed from the child's environment: the first names more CLAUDE.md
# directories to load, the second ties the child to this session's id.
_SCRUB = ("CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD", "CLAUDE_CODE_SESSION_ID")
_FINISH = {"end_turn": "stop", "stop_sequence": "stop", "max_tokens": "length"}


def flatten(messages: list[dict]) -> tuple[str, str]:
    """(system prompt, stdin text) for one CLI call.

    The last user message is the task. Every user turn before it, with the
    assistant turn that follows it, is an example — written out rather than
    replayed, because the CLI accepts no assistant turn."""
    system = "\n\n".join(str(m.get("content") or "") for m in messages if m.get("role") == "system")
    turns = [m for m in messages if m.get("role") != "system"]
    if not turns:
        return system, ""
    final = turns[-1]
    earlier = turns[:-1]
    if not earlier:
        return system, _text(final)
    parts, number = [], 0
    for i, m in enumerate(earlier):
        if m.get("role") == "user":
            number += 1
            reply = earlier[i + 1] if i + 1 < len(earlier) and earlier[i + 1].get("role") == "assistant" else None
            parts.append(f"=== Example {number}: the message ===\n{_text(m)}")
            if reply is not None:
                parts.append(f"=== Example {number}: the reply that was given ===\n{_text(reply)}")
        elif m.get("role") == "assistant" and (i == 0 or earlier[i - 1].get("role") != "user"):
            parts.append(f"=== A reply that was given ===\n{_text(m)}")
    intro = ("The examples below show messages of this task and the replies given to them. "
             "Answer the final message the same way, in the same format.")
    return system, "\n\n".join([intro, *parts, f"=== The message to answer ===\n{_text(final)}"])


def _text(message: dict) -> str:
    """A message's text. An image, audio or file part is refused rather than dropped: the
    CLI takes text on stdin, and a prompt with a part silently missing is a different
    prompt (`Plan/concept/dspy-source_2026-09-24/adapters-and-types.md`)."""
    content = message.get("content")
    if isinstance(content, list):
        other = sorted({str(p.get("type")) for p in content if isinstance(p, dict) and p.get("type") != "text"})
        if other:
            raise dspy.LMUnsupportedFeatureError(f"claude -p takes text only; this message carries {other}",
                                                 features=other, model="claude-cli")
        return "\n".join(str(p.get("text", "")) for p in content if isinstance(p, dict))
    return str(content or "")


class ClaudeCLI(dspy.BaseLM):
    """Claude through `claude -p`. `model` is a CLI alias (`haiku`, `sonnet`, `opus`) or a model id."""

    forward_contract = "legacy"

    def __init__(self, model: str = "haiku", *, thinking: int | None = 0, effort: str | None = None,
                 timeout: float = 300.0, binary: str | None = None, **kwargs):
        kwargs.pop("cache", None)
        super().__init__(model=f"claude-cli/{model}", cache=False, **kwargs)
        self.cli_model = model
        self.thinking = thinking
        self.effort = effort
        self.timeout = timeout
        self.binary = binary
        self._workdir = None

    def dump_state(self) -> dict:
        state = super().dump_state()
        state.update(model=self.cli_model, thinking=self.thinking, effort=self.effort, timeout=self.timeout)
        return state

    def _command(self, system: str) -> list[str]:
        binary = self.binary or shutil.which("claude")
        if not binary:
            raise dspy.LMNotConfiguredError("no `claude` executable on PATH", model=self.model)
        command = [binary, "-p", "--output-format", "json", "--model", self.cli_model,
                   "--tools", "", "--no-session-persistence", "--setting-sources", "",
                   "--strict-mcp-config", "--disable-slash-commands"]
        if self.effort:
            command += ["--effort", self.effort]
        if system:
            command += ["--system-prompt", system]
        return command

    def _one(self, system: str, text: str) -> dict:
        if self._workdir is None or not Path(self._workdir).is_dir():
            self._workdir = tempfile.mkdtemp(prefix="claude-lm-")
        env = {k: v for k, v in os.environ.items() if k not in _SCRUB}
        if self.thinking is not None:
            env["MAX_THINKING_TOKENS"] = str(self.thinking)
        started = time.time()
        try:
            done = subprocess.run(self._command(system), input=text, capture_output=True, text=True,
                                  timeout=self.timeout, cwd=self._workdir, env=env)
        except subprocess.TimeoutExpired as exc:
            raise dspy.LMTimeoutError(f"claude -p gave no answer in {self.timeout:.0f}s",
                                      model=self.model, provider="claude-cli") from exc
        except OSError as exc:
            raise dspy.LMNotConfiguredError(f"claude -p could not start: {exc}", model=self.model) from exc
        try:
            reply = json.loads(done.stdout)
        except json.JSONDecodeError as exc:
            raise dspy.LMTransportError(
                f"claude -p exit {done.returncode}, unreadable output: {(done.stdout or done.stderr)[:300]!r}",
                model=self.model, provider="claude-cli") from exc
        if done.returncode != 0 or reply.get("is_error"):
            detail = str(reply.get("result") or reply.get("subtype") or done.stderr)[:300]
            kind = (dspy.LMRateLimitError if any(w in detail.lower() for w in ("rate limit", "overloaded", "429"))
                    else dspy.LMServerError)
            raise kind(f"claude -p exit {done.returncode}: {detail}", model=self.model, provider="claude-cli")
        reply["_seconds"] = round(time.time() - started, 2)
        return reply

    def forward(self, prompt=None, messages=None, **kwargs):
        messages = messages or [{"role": "user", "content": prompt or ""}]
        system, text = flatten(messages)
        n = int(kwargs.get("n") or self.kwargs.get("n") or 1)
        replies = [self._one(system, text) for _ in range(max(1, n))]
        choices, usage, cost, served = [], {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}, 0.0, None
        for reply in replies:
            choices.append(SimpleNamespace(
                message=SimpleNamespace(content=reply.get("result") or "", tool_calls=None),
                logprobs=None, finish_reason=_FINISH.get(reply.get("stop_reason"), reply.get("stop_reason"))))
            u = reply.get("usage") or {}
            prompt_tokens = sum(int(u.get(k) or 0) for k in
                                ("input_tokens", "cache_read_input_tokens", "cache_creation_input_tokens"))
            usage["prompt_tokens"] += prompt_tokens
            usage["completion_tokens"] += int(u.get("output_tokens") or 0)
            cost += float(reply.get("total_cost_usd") or 0.0)
            served = served or next(iter(reply.get("modelUsage") or {}), None)
        usage["total_tokens"] = usage["prompt_tokens"] + usage["completion_tokens"]
        response = SimpleNamespace(choices=choices, model=served or self.model, usage=usage)
        response._hidden_params = {"response_cost": cost}
        return response


# --- the offline self-test: a fake `claude` that records what it was given ------------------

_FAKE = r'''#!/usr/bin/env python3
import json, os, sys
argv = sys.argv[1:]
stdin = sys.stdin.read()
log = os.environ["FAKE_CLAUDE_LOG"]
with open(log, "a") as fh:
    fh.write(json.dumps({"argv": argv, "stdin": stdin, "cwd": os.getcwd(),
                         "env_scrubbed": "CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD" not in os.environ,
                         "thinking": os.environ.get("MAX_THINKING_TOKENS"),
                         "cwd_files": os.listdir(".")}) + "\n")
mode = os.environ.get("FAKE_CLAUDE_MODE", "ok")
if mode == "crash":
    sys.stderr.write("boom\n"); sys.exit(1)
if mode == "garbage":
    print("not json"); sys.exit(0)
if mode == "error":
    print(json.dumps({"is_error": True, "result": "API Error: 529 overloaded", "subtype": "error"})); sys.exit(1)
answer = "[[ ## antwort ## ]]\nja\n\n[[ ## completed ## ]]"
print(json.dumps({"result": answer, "is_error": False, "stop_reason": "end_turn", "total_cost_usd": 0.002,
                  "usage": {"input_tokens": 100, "cache_read_input_tokens": 20, "output_tokens": 7},
                  "modelUsage": {"claude-haiku-4-5": {}}}))
'''


def selftest() -> tuple[list[str], int]:
    """Each claim of the docstring, run against a fake `claude` — no network, no key."""
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from lmrun import call

    failures, cases = [], 0
    with tempfile.TemporaryDirectory() as tmp:
        fake = Path(tmp) / "claude"
        fake.write_text(_FAKE)
        fake.chmod(0o755)
        log = Path(tmp) / "calls.jsonl"
        saved = {k: os.environ.get(k) for k in ("FAKE_CLAUDE_LOG", "FAKE_CLAUDE_MODE",
                                                 "CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD")}
        os.environ["FAKE_CLAUDE_LOG"] = str(log)
        os.environ["CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD"] = "/somewhere"
        try:
            lm = ClaudeCLI("haiku", binary=str(fake))
            program = dspy.Predict("frage -> antwort")
            demo = dspy.Example(frage="Beispiel?", antwort="Beispielantwort").with_inputs("frage")
            program.demos = [demo]

            os.environ["FAKE_CLAUDE_MODE"] = "ok"
            with dspy.context(lm=lm):
                pred, rec = call(program, step="selftest", approval="selftest", out_dir=Path(tmp), frage="Wirklich?")
            seen = json.loads(log.read_text().splitlines()[-1])
            argv = seen["argv"]
            checks = {
                "the answer is parsed": pred is not None and pred.antwort == "ja",
                "the call is recorded answered": rec["status"] == "answered",
                "cost reaches the record": abs(rec["cost"] - 0.002) < 1e-9,
                "tools are off": argv[argv.index("--tools") + 1] == "",
                "no session is written": "--no-session-persistence" in argv,
                "no settings, MCP or skills": all(f in argv for f in ("--setting-sources", "--strict-mcp-config",
                                                                        "--disable-slash-commands")),
                "DSPy's system message replaces Claude Code's": "Your input fields are" in argv[argv.index("--system-prompt") + 1],
                "the demo is written out with its reply, before the task":
                    "Example 1: the reply that was given ===\n[[ ## antwort ## ]]\nBeispielantwort" in seen["stdin"]
                    and "Wirklich?" in seen["stdin"].split("=== The message to answer ===")[-1]
                    and "Wirklich?" not in seen["stdin"].split("=== The message to answer ===")[0],
                "the child does not see the extra CLAUDE.md directories": seen["env_scrubbed"],
                "the working directory is empty": seen["cwd_files"] == [],
                "thinking is off by default": seen["thinking"] == "0",
            }
            for name, held in checks.items():
                cases += 1
                if not held:
                    failures.append(name)

            for mode, expected in (("crash", "unreachable"), ("garbage", "unreachable"), ("error", "unreachable")):
                cases += 1
                os.environ["FAKE_CLAUDE_MODE"] = mode
                with dspy.context(lm=lm):
                    _, rec = call(program, step="selftest", approval="selftest", out_dir=Path(tmp), frage="x")
                if rec["status"] != expected:
                    failures.append(f"{mode}: expected {expected}, got {rec['status']} ({rec['error']})")

            cases += 1
            os.environ["FAKE_CLAUDE_MODE"] = "ok"
            with dspy.context(lm=lm):
                try:
                    call(program, step="selftest", out_dir=Path(tmp), frage="x")
                    failures.append("a Claude call ran without approval")
                except RuntimeError as exc:
                    if "approval" not in str(exc):
                        failures.append(f"refused for the wrong reason: {exc}")

            cases += 1
            before = len(log.read_text().splitlines())
            lm.forward(messages=[{"role": "user", "content": "x"}], n=2)
            if len(log.read_text().splitlines()) - before != 2:
                failures.append("n=2 did not make two calls")

            cases += 1
            try:
                lm.forward(messages=[{"role": "user", "content": [
                    {"type": "text", "text": "Was zeigt das Bild?"},
                    {"type": "image_url", "image_url": {"url": "data:image/png;base64,AAAA"}}]}])
                failures.append("an image part was dropped instead of refused")
            except dspy.LMUnsupportedFeatureError:
                pass

            cases += 1
            missing = ClaudeCLI("haiku", binary=str(Path(tmp) / "absent"))
            try:
                missing.forward(messages=[{"role": "user", "content": "x"}])
                failures.append("a missing binary did not raise")
            except dspy.LMNotConfiguredError:
                pass
        finally:
            for k, v in saved.items():
                if v is None:
                    os.environ.pop(k, None)
                else:
                    os.environ[k] = v
    return failures, cases


if __name__ == "__main__":
    problems, total = selftest()
    for p in problems:
        print(f"  FAIL  {p}")
    print(f"claude_lm: {total - len(problems)} of {total} cases hold (parse, record, cost, no tools, no session, "
          "no settings, system prompt, demos written out, env scrubbed, empty cwd, thinking off, 3 failures unreachable, "
          "approval refused, n=2, an image refused, missing binary raises)")
    raise SystemExit(1 if problems else 0)
