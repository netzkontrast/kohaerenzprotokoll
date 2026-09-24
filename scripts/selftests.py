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

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENV = ROOT / ".venv-dspy" / "bin" / "python"
# kind -> (interpreter, or None for this one; what must exist; how to reach it)
KINDS = {
    "dspy": (VENV, VENV, ".venv-dspy absent — scripts/install.sh dspy"),
    "typesafe": (ROOT / ".venv-typesafe" / "bin" / "python", ROOT / ".venv-typesafe" / "bin" / "python",
                 ".venv-typesafe absent — scripts/install.sh typesafe"),
    "he": (None, "he", "Hyper-Extract absent — scripts/install.sh hyperextract"),
}

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
    ("route: price, consent, record", "typesafe", ["scripts/route.py", "selftest"]),
    ("templates: checks fail", "he", ["scripts/templates.py", "selftest"]),
    ("templates, live", "he", ["scripts/templates.py", "check"]),
    ("dspy surface", "dspy", ["scripts/check_dspy_surface.py"]),
    ("dspy skill, selftest", "dspy", ["scripts/check_dspy_skill.py", "--selftest"]),
    ("dspy skill, live", "dspy", ["scripts/check_dspy_skill.py"]),
    ("lm fixture", "dspy", ["scripts/lm_fixture.py"]),
    ("lmrun", "dspy", ["scripts/lmrun.py"]),
    ("pairs dry-run", "dspy", ["scripts/pairs.py", "run", "--optimizer", "labeled", "--dry-run"]),
    ("graphrag answer dry-run", "dspy",
     ["scripts/graphrag.py", "ask", "Nexus Überraum", "--answer", "--dry-run"]),
]


def main() -> int:
    held = failed = unrun = 0
    for name, kind, args in SUITES:
        interpreter, needs, remedy = KINDS.get(kind, (None, None, ""))
        present = needs is None or (shutil.which(needs) if isinstance(needs, str) else needs.exists())
        if not present:
            print(f"  not run  {name:<26} {remedy}")
            unrun += 1
            continue
        python = str(interpreter) if interpreter else sys.executable
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
