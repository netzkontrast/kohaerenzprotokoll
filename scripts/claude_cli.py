"""One headless `claude -p` call, shut in an empty directory — standard library only.

The one encoding (P6) of how this repository calls Claude outside the session
(decision 011): `claude_lm.ClaudeCLI`, the DSPy model, and `he_claude.Claude`,
the model a HyperExtract contract run asks, both call `call()`. It lives apart from
them because DSPy is in a virtualenv and the contract run in none.

- **no tools** (`--tools ""`), no MCP servers, no skills, no settings files, no
  session written, and an empty working directory, so no `CLAUDE.md` is
  discovered and the model sees the prompt and nothing else;
- the system message replaces Claude Code's own (`--system-prompt`); the text
  goes in on stdin;
- **no thinking unless asked**: `thinking=0` sets `MAX_THINKING_TOKENS=0`;
- the CLI's JSON reply comes back whole — `result`, `usage`, `total_cost_usd`,
  `modelUsage` — with the wall-clock seconds added as `_seconds`.

A failure raises `CallError` with one `kind`: `missing` (no binary), `timeout`,
`unreadable` (no JSON), `rate` (rate limit or overload) or `error`. Each caller
maps the kind to its own framework's exception.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
import time
from pathlib import Path

# Removed from the child's environment: the first names more CLAUDE.md
# directories to load, the second ties the child to this session's id.
SCRUB = ("CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD", "CLAUDE_CODE_SESSION_ID")


class CallError(Exception):
    def __init__(self, kind: str, message: str):
        super().__init__(message)
        self.kind = kind


def command(model: str, system: str = "", effort: str | None = None, binary: str | None = None) -> list[str]:
    binary = binary or shutil.which("claude")
    if not binary:
        raise CallError("missing", "no `claude` executable on PATH")
    out = [binary, "-p", "--output-format", "json", "--model", model,
           "--tools", "", "--no-session-persistence", "--setting-sources", "",
           "--strict-mcp-config", "--disable-slash-commands"]
    if effort:
        out += ["--effort", effort]
    if system:
        out += ["--system-prompt", system]
    return out


def call(model: str, system: str, text: str, *, thinking: int | None = 0, effort: str | None = None,
         timeout: float = 300.0, binary: str | None = None, workdir: str | None = None) -> dict:
    """One call; the CLI's JSON reply, or `CallError`."""
    if workdir is None or not Path(workdir).is_dir():
        workdir = tempfile.mkdtemp(prefix="claude-cli-")
    env = {k: v for k, v in os.environ.items() if k not in SCRUB}
    if thinking is not None:
        env["MAX_THINKING_TOKENS"] = str(thinking)
    started = time.time()
    try:
        done = subprocess.run(command(model, system, effort, binary), input=text, capture_output=True,
                              text=True, timeout=timeout, cwd=workdir, env=env)
    except subprocess.TimeoutExpired as exc:
        raise CallError("timeout", f"claude -p gave no answer in {timeout:.0f}s") from exc
    except OSError as exc:
        raise CallError("missing", f"claude -p could not start: {exc}") from exc
    try:
        reply = json.loads(done.stdout)
    except json.JSONDecodeError as exc:
        raise CallError("unreadable", f"claude -p exit {done.returncode}, unreadable output: "
                                      f"{(done.stdout or done.stderr)[:300]!r}") from exc
    if done.returncode != 0 or reply.get("is_error"):
        detail = str(reply.get("result") or reply.get("subtype") or done.stderr)[:300]
        kind = "rate" if any(w in detail.lower() for w in ("rate limit", "overloaded", "429")) else "error"
        raise CallError(kind, f"claude -p exit {done.returncode}: {detail}")
    reply["_seconds"] = round(time.time() - started, 2)
    reply["_workdir"] = workdir
    return reply


def totals(calls: list[dict]) -> dict:
    """All observed usage, including paid responses that failed validation."""
    return {"calls": len(calls), "failed_calls": sum(not c.get("ok") for c in calls),
            "seconds": round(sum(c.get("seconds") or 0 for c in calls), 1),
            "input_tokens": sum(c.get("input") or 0 for c in calls),
            "output_tokens": sum(c.get("output") or 0 for c in calls),
            "cost_usd": round(sum(c.get("cost_usd") or 0 for c in calls), 4)}


def totals_selftest() -> int:
    failed = {"ok": False, "kind": "invalid", "seconds": 2, "input": 100, "output": 20, "cost_usd": 0.01}
    passed = {"ok": True, "seconds": 3, "input": 200, "output": 30, "cost_usd": 0.02}
    assert totals([failed, passed]) == {"calls": 2, "failed_calls": 1, "seconds": 5,
                                       "input_tokens": 300, "output_tokens": 50, "cost_usd": 0.03}
    assert totals([failed])["cost_usd"] == 0.01
    assert totals([{"ok": False, "kind": "timeout"}])["cost_usd"] == 0
    print("claude usage: retry, all-invalid, and missing usage held")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(totals_selftest() if sys.argv[1:] == ["totals-selftest"] else 2)
