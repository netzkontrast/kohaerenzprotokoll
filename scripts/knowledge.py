"""Initialize tool capabilities and the shared corpus/wiki graph store.

    python3 scripts/knowledge.py init --profile reader
    python3 scripts/knowledge.py init --profile research --check
    python3 scripts/knowledge.py init --profile full
    python3 scripts/knowledge.py selftest

Only the coordinating session initializes. Subagents use --check, then report
missing capabilities. Initialization performs one shared graph build; it performs no model extraction or source authoring.
Full includes the existing qmd-models installer (large downloads/embeddings).
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def phases(profile: str, check: bool) -> list[tuple[str, list[str]]]:
    install = ["bash", "scripts/install.sh"]
    if check:
        install.append("--check")
    if profile == "reader":
        install += ["derived", "graphqlite", "qmd"]
    elif profile == "research":
        install += ["--session"]
    elif profile == "full":
        # No components means the installer owns the full component registry.
        pass
    else:
        raise ValueError("unknown profile")
    result = [("tools", install), ("sources", [sys.executable, "scripts/sources.py", "check"])]
    if not check:
        result.append(("derive", [sys.executable, "scripts/derive.py"]))
        result.append(("wiki-graph-index", [".venv-graphqlite/bin/python", "scripts/kg.py", "index"]))
    result.append(("wiki-graph-freshness", [".venv-graphqlite/bin/python", "scripts/kg.py", "check"]))
    if profile != "reader":
        result.append(("ask-freshness", [".venv-dspy/bin/python", "scripts/askdb.py", "check"]))
    if not check:
        result.append(("qmd-update", [".tools-node/node_modules/.bin/qmd", "update"]))
    result += [("qmd-status", [".tools-node/node_modules/.bin/qmd", "status"]),
               ("qmd-coverage", [sys.executable, "scripts/qmd_coverage.py"]),
               ("templates", [sys.executable, "scripts/hx.py", "check"] if check else
                [sys.executable, "scripts/templates.py", "check"])]
    if profile == "full":
        result.append(("qmd-semantic", ["bash", "scripts/setup_qmd.sh", "--check"] if check
                       else ["bash", "scripts/install.sh", "qmd-models"]))
    return result


def execute(profile: str, check: bool, runner=subprocess.run) -> dict:
    rows = []
    for name, command in phases(profile, check):
        try:
            done = runner(command, cwd=ROOT, capture_output=True, text=True)
            text = done.stdout + done.stderr
            # Existing shell --check commands deliberately exit zero on missing
            # components; inspect their explicit diagnostic states as well.
            reported_missing = name in {"tools", "qmd-semantic"} and re.search(
                r"\b(?:MISSING|FAILED)\b|INDEX DISAGREES|A DIRECTORY IS UNCOVERED|\d+ pending", text)
            semantic_unknown = name == "qmd-semantic" and check and not re.search(r"embeddings\s+complete", text)
            rows.append({"capability": name, "command": command,
                         "status": "ok" if done.returncode == 0 and not reported_missing and not semantic_unknown else "failed",
                         "exit_code": done.returncode,
                         "detail": (done.stdout + done.stderr)[-2000:]})
        except OSError as exc:
            rows.append({"capability": name, "command": command,
                         "status": "unavailable", "detail": str(exc)})
    return {"profile": profile, "check_only": check, "capabilities": rows,
            "ready": all(r["status"] == "ok" for r in rows)}


def selftest() -> int:
    from types import SimpleNamespace
    for profile in ("reader", "research", "full"):
        check = phases(profile, True)
        assert all(not any(arg in {"build", "index", "update", "scripts/derive.py"}
                           for arg in cmd) for _, cmd in check)
        assert "--check" in check[0][1]
    assert sum("index" in cmd or "build" in cmd for _, cmd in phases("research", False)) == 1
    commands = []
    def offline(command, **kwargs):
        commands.append(command)
        if "scripts/kg.py" in command:
            raise FileNotFoundError("fixture: missing interpreter")
        return SimpleNamespace(returncode=1 if "scripts/sources.py" in command else 0,
                               stdout="fixture", stderr="")
    report = execute("research", True, offline)
    assert not report["ready"]
    assert {r["status"] for r in report["capabilities"]} == {"ok", "failed", "unavailable"}
    assert len(commands) == len(phases("research", True))
    assert any("scripts/askdb.py" in c for c in commands)
    assert "qmd-models" not in str(phases("reader", False))
    assert "qmd-models" in str(phases("full", False))
    assert "scripts/templates.py" not in str(phases("reader", True))
    missing = execute("reader", True, lambda *a, **k: SimpleNamespace(
        returncode=0, stdout="MISSING", stderr=""))
    assert not missing["ready"]
    print("knowledge: read-only plans, capability failures, continuation, shared store and opt-in semantic setup hold")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    s = p.add_subparsers(dest="command", required=True)
    s.add_parser("selftest")
    init = s.add_parser("init")
    init.add_argument("--profile", choices=("reader", "research", "full"), default="reader")
    init.add_argument("--check", action="store_true")
    args = p.parse_args()
    if args.command == "selftest":
        return selftest()
    if args.check:
        report = execute(args.profile, True)
    else:
        import fcntl
        lock_dir = ROOT / "Plan/derived"
        lock_dir.mkdir(parents=True, exist_ok=True)
        with (lock_dir / ".knowledge-init.lock").open("a") as lock:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                print("Initialization already running; let the coordinating session finish.", file=sys.stderr)
                return 2
            report = execute(args.profile, False)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ready"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
