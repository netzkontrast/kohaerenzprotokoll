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
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Iterator

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
    ("candidate lists compared", "std", ["scripts/agree.py", "selftest"]),
    ("skills", "std", ["scripts/check_skills.py", "--selftest"]),
    ("skills, live", "std", ["scripts/check_skills.py"]),
    ("baseline ledger", "std", ["scripts/baseline.py", "selftest"]),
    ("pairs: rules and veto", "std", ["scripts/pairs.py", "selftest"]),
    ("graph", "std", ["scripts/graph.py", "--selftest"]),
    ("graphrag", "std", ["scripts/graphrag.py", "selftest"]),
    ("ui app", "std", ["scripts/ui.py", "selftest"]),
    ("rlm_ingest tools, reach", "std", ["scripts/rlm_ingest.py", "--selftest"]),
    ("gold lists", "std", ["scripts/gold.py", "selftest"]),
    ("prose numbers", "std", ["scripts/state.py", "--prose"]),
    ("qmd coverage patterns", "std", ["scripts/qmd_coverage.py", "--selftest"]),
    ("qmd coverage, live", "std", ["scripts/qmd_coverage.py"]),
    ("route: price, consent, record", "typesafe", ["scripts/route.py", "selftest"]),
    ("templates: checks fail", "he", ["scripts/templates.py", "selftest"]),
    ("templates, live", "he", ["scripts/templates.py", "check"]),
    ("dspy surface", "dspy", ["scripts/check_dspy_surface.py"]),
    ("dspy skill, selftest", "dspy", ["scripts/check_dspy_skill.py", "--selftest"]),
    ("dspy skill, live", "dspy", ["scripts/check_dspy_skill.py"]),
    ("lm fixture", "dspy", ["scripts/lm_fixture.py"]),
    ("lmrun", "dspy", ["scripts/lmrun.py"]),
    ("pairs dry-run", "dspy", ["scripts/pairs.py", "run", "--optimizer", "labeled", "--dry-run"]),
    ("pairs dry-run, plural first", "dspy",
     ["scripts/pairs.py", "run", "--optimizer", "labeled", "--rule", "plural", "--dry-run"]),
    ("graphrag answer dry-run", "dspy",
     ["scripts/graphrag.py", "ask", "Nexus Überraum", "--answer", "--dry-run"]),
]


def run_suite(suite: tuple[str, str, list[str]]) -> tuple[str, str, str]:
    """(held | FAILED | not run, the suite's name, what it said last) for one suite."""
    name, kind, args = suite
    interpreter, needs, remedy = KINDS.get(kind, (None, None, ""))
    present = needs is None or (shutil.which(needs) if isinstance(needs, str) else needs.exists())
    if not present:
        return "not run", name, remedy
    python = str(interpreter) if interpreter else sys.executable
    proc = subprocess.run([python, *args], cwd=ROOT, capture_output=True, text=True, timeout=900)
    last = (proc.stdout.strip().splitlines() or proc.stderr.strip().splitlines() or ["(no output)"])[-1]
    return ("held" if proc.returncode == 0 else "FAILED"), name, last[:90]


def run(workers: int = 4) -> Iterator[tuple[str, str, str]]:
    """Every suite's row, in the order of SUITES, each as soon as it and those before it are done.

    The suites are independent and each runs in its own process, so up to
    `workers` run at once. Measured here: 65 seconds one after another before,
    16 four at a time, the suites' own speedups included. `ui.py` takes these
    rows as they are rather than parsing the lines `main` prints, which dropped
    any suite whose name outgrew the column.
    """
    with ThreadPoolExecutor(workers) as pool:
        yield from pool.map(run_suite, SUITES)


def main() -> int:
    counts: Counter = Counter()
    for status, name, said in run():
        print(f"  {status:<9}{name:<26} {said}", flush=True)
        counts[status] += 1
    held, failed, unrun = counts["held"], counts["FAILED"], counts["not run"]
    print(f"\n{held} held, {failed} failed, {unrun} not run, of {len(SUITES)} suites")
    return 1 if failed or unrun else 0


if __name__ == "__main__":
    raise SystemExit(main())
