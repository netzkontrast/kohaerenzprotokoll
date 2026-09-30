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
    "graphqlite": (ROOT / ".venv-graphqlite/bin/python", ROOT / ".venv-graphqlite/bin/python",
                   ".venv-graphqlite absent — scripts/install.sh graphqlite"),
    "dspy": (VENV, VENV, ".venv-dspy absent — scripts/install.sh dspy"),
    "typesafe": (ROOT / ".venv-typesafe" / "bin" / "python", ROOT / ".venv-typesafe" / "bin" / "python",
                 ".venv-typesafe absent — scripts/install.sh typesafe"),
    "he": (None, "he", "Hyper-Extract absent — scripts/install.sh hyperextract"),
}

# (name, interpreter, arguments). "dspy" means .venv-dspy.
SUITES = [
    ("knowledge init: plans and failures", "std", ["scripts/knowledge.py", "selftest"]),
    ("reading extraction: provenance and placement", "std", ["scripts/reading_extract.py", "selftest"]),
    ("reading extraction: real HE fixture", "he", ["scripts/reading_extract.py", "native-selftest"]),
    ("quotes, find, fold", "std", ["scripts/selftest.py"]),
    ("entities matcher", "std", ["scripts/entities.py", "selftest"]),
    ("overview: names, pairs, case", "std", ["scripts/overview.py", "selftest"]),
    ("candidate lists compared", "std", ["scripts/agree.py", "selftest"]),
    ("reconcile sweep", "std", ["scripts/reconcile.py", "--selftest"]),
    ("skills", "std", ["scripts/check_skills.py", "--selftest"]),
    ("skills, live", "std", ["scripts/check_skills.py"]),
    ("baseline ledger", "std", ["scripts/baseline.py", "selftest"]),
    ("pairs: rules and veto", "std", ["scripts/pairs.py", "selftest"]),
    ("chapter pages: checks fail", "std", ["scripts/chapters.py", "selftest"]),
    ("chapter pages, live", "std", ["scripts/chapters.py"]),
    ("chapter sources: query, section", "std", ["scripts/chapter_sources.py", "selftest"]),
    ("links: once per page", "std", ["scripts/link.py", "selftest"]),
    ("graph", "std", ["scripts/graph.py", "--selftest"]),
    ("graphqlite: real extension", "graphqlite", ["scripts/kg_selftest.py"]),
    ("graphrag", "std", ["scripts/graphrag.py", "selftest"]),
    ("ui app", "std", ["scripts/ui.py", "selftest"]),
    ("rlm_ingest tools, reach", "std", ["scripts/rlm_ingest.py", "--selftest"]),
    ("gold lists", "std", ["scripts/gold.py", "selftest"]),
    ("prose numbers", "std", ["scripts/state.py", "--prose"]),
    ("pipeline order: violations named", "std", ["scripts/account.py", "selftest"]),
    ("pipeline order, live", "std", ["scripts/account.py", "order", "--summary"]),
    ("quotes, live", "std", ["scripts/quotes.py"]),
    ("frontmatter, live", "std", ["scripts/wiki_index.py", "--check"]),
    ("judgements replay", "std", ["scripts/judgements.py", "--open"]),  # --open: no re-render
    ("jules: approval, tools, verify", "std", ["scripts/jules.py", "selftest"]),
    ("runlog: refusals, summary", "std", ["scripts/runlog.py", "selftest"]),
    ("readings lint: each class and its near-miss", "std", ["scripts/lint_readings.py", "selftest"]),
    ("digest: what a reader needs of a page", "std", ["scripts/digest.py", "selftest"]),
    ("readings: placed by code, refused, in order", "std", ["scripts/readings.py", "selftest"]),
    ("census: drafted by code, checked", "std", ["scripts/census.py", "selftest"]),
    ("record: derived from the pages, checked", "std", ["scripts/record.py", "selftest"]),
    ("reader lab: the clean reader's gate", "std",
     ["Plan/runs/reader-lab-2026-09-30/clean_reader.py", "selftest"]),
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
    ("ask store: bm25, ppr, sheets", "dspy", ["scripts/askdb.py", "selftest"]),
    ("ask: verify names each defect", "dspy", ["scripts/ask.py", "selftest"]),
    ("ask graph: lines, paragraphs, hyperedges", "std", ["scripts/askextract.py"]),
    ("aliases: similarity, threshold", "dspy", ["scripts/aliases.py", "selftest"]),
    ("claude cli model", "dspy", ["scripts/claude_lm.py"]),
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


def main(argv: list[str] | None = None) -> int:
    """`--only std` runs the suites this interpreter can run alone — what CI runs.

    The others are then skipped by request and counted as such, never as held:
    the exit status covers the suites that ran, and the last line says how many
    did not.
    """
    argv = sys.argv[1:] if argv is None else argv
    only = argv[argv.index("--only") + 1] if "--only" in argv else None
    global SUITES
    chosen = [s for s in SUITES if only is None or s[1] == only]
    skipped = len(SUITES) - len(chosen)
    everything, SUITES = SUITES, chosen
    counts: Counter = Counter()
    try:
        for status, name, said in run():
            print(f"  {status:<9}{name:<26} {said}", flush=True)
            counts[status] += 1
    finally:
        SUITES = everything
    held, failed, unrun = counts["held"], counts["FAILED"], counts["not run"]
    tail = f", {skipped} skipped by --only {only}" if only else ""
    print(f"\n{held} held, {failed} failed, {unrun} not run, of {len(chosen)} suites{tail}")
    return 1 if failed or unrun else 0


if __name__ == "__main__":
    raise SystemExit(main())
