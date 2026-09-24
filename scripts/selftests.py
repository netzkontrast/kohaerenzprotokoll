"""Run every self-test in the repository, and report each one on its own line.

P11: never collapse several checks into one pass/fail bit. Each suite here
proves one checker can fail; this runs them all and says which held, which
failed, and which **could not run** — a suite whose interpreter is missing has
not passed (P15), it has not been reached, and the line says how to reach it.

Standard-library suites run under this interpreter. DSPy suites need
`.venv-dspy`; when it is absent they are reported `not run`, with the command
that creates it, and the exit status says so.

    python3 scripts/selftests.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENV = ROOT / ".venv-dspy" / "bin" / "python"

# (name, interpreter, arguments). "dspy" means .venv-dspy.
SUITES = [
    ("quotes, find, fold", "std", ["scripts/selftest.py"]),
    ("entities matcher", "std", ["scripts/entities.py", "selftest"]),
    ("skills", "std", ["scripts/check_skills.py", "--selftest"]),
    ("skills, live", "std", ["scripts/check_skills.py"]),
    ("baseline ledger", "std", ["scripts/baseline.py", "selftest"]),
    ("graph", "std", ["scripts/graph.py", "--selftest"]),
    ("graphrag", "std", ["scripts/graphrag.py", "selftest"]),
    ("ui app", "std", ["scripts/ui.py", "selftest"]),
    ("rlm_ingest tools, reach", "std", ["scripts/rlm_ingest.py", "--selftest"]),
    ("prose numbers", "std", ["scripts/state.py", "--prose"]),
    ("dspy surface", "dspy", ["scripts/check_dspy_surface.py"]),
    ("lm fixture", "dspy", ["scripts/lm_fixture.py"]),
    ("lmrun", "dspy", ["scripts/lmrun.py"]),
    ("pairs dry-run", "dspy", ["scripts/pairs.py", "run", "--optimizer", "labeled", "--dry-run"]),
    ("graphrag answer dry-run", "dspy",
     ["scripts/graphrag.py", "ask", "Nexus Überraum", "--answer", "--dry-run"]),
]


def main() -> int:
    held = failed = unrun = 0
    for name, kind, args in SUITES:
        if kind == "dspy" and not VENV.exists():
            print(f"  not run  {name:<26} .venv-dspy absent — uv venv --python 3.11 .venv-dspy && "
                  "uv pip install --python .venv-dspy/bin/python 'dspy[numpy]==3.3.1'")
            unrun += 1
            continue
        python = str(VENV) if kind == "dspy" else sys.executable
        proc = subprocess.run([python, *args], cwd=ROOT, capture_output=True, text=True, timeout=900)
        last = (proc.stdout.strip().splitlines() or proc.stderr.strip().splitlines() or ["(no output)"])[-1]
        if proc.returncode == 0:
            held += 1
            print(f"  held     {name:<26} {last[:90]}")
        else:
            failed += 1
            print(f"  FAILED   {name:<26} {last[:90]}")
    print(f"\n{held} held, {failed} failed, {unrun} not run, of {len(SUITES)} suites")
    return 1 if failed or unrun else 0


if __name__ == "__main__":
    raise SystemExit(main())
