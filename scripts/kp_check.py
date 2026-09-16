#!/usr/bin/env python3
"""Run every free, deterministic gate in one command.

    python3 scripts/kp_check.py              # the standing gates
    python3 scripts/kp_check.py --chapters   # also lint every chapter file
    python3 scripts/kp_check.py --json       # machine-readable
    python3 scripts/kp_check.py --quiet      # the table only, no gate output

None of these gates calls an LLM, needs an API key or touches the network, so
there is never a reason to skip them before saying a piece of work is done.
Each one is also runnable on its own; this script exists so nobody has to
remember the list.

Exit 0 when every gate passes, 1 when one fails, 2 when a gate could not run
at all (a missing file, a broken tree). A gate that reports a Canon-Lock
finding is not a failure: `storyform_check.py` runs without --strict here,
because Storyform B's heterodox rows are deliberate.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXIT_OK, EXIT_FAILED, EXIT_CANNOT_RUN = 0, 1, 2

# (name, argv, what a non-zero status means)
GATES: list[tuple[str, list[str], str]] = [
    ("wiki health", ["scripts/wiki_lint.py", "--health"], "the wiki has lint errors"),
    ("wiki views", ["scripts/render_wiki_views.py", "--check"], "re-run render_wiki_views.py"),
    ("codex views", ["scripts/render_codex_views.py", "--check"], "re-run render_codex_views.py"),
    ("source manifest", ["scripts/source_inventory.py", "--check"], "re-run source_inventory.py"),
    ("claim provenance", ["scripts/audit_graph_claims.py"], "a claim points into Wiki/ (D-W2)"),
    ("storyform", ["scripts/storyform_check.py"], "a storyform row could not be read"),
    ("world axioms", ["scripts/world_check.py"], "the worlds or axioms are unreadable"),
    ("chapter drift", ["scripts/chapter_drift.py"], "the graph or the manuscript is unreadable"),
]

CHAPTER_GLOB = "Manuscript/**/chapters/*.md"


def run_gate(argv: list[str], quiet: bool) -> tuple[int, str]:
    result = subprocess.run([sys.executable, *argv], cwd=ROOT, capture_output=True, text=True)
    output = (result.stdout or "") + (result.stderr or "")
    if not quiet and output.strip():
        print(f"\n$ python3 {' '.join(argv)}")
        print(output.rstrip())
    return result.returncode, output


def chapter_gate(quiet: bool) -> tuple[str, int, str]:
    """Lint every chapter file; a VIOLATION in any of them fails the gate."""
    files = sorted(ROOT.glob(CHAPTER_GLOB))
    if not files:
        return "chapter lints", EXIT_CANNOT_RUN, "no chapter files found"
    failed = []
    for path in files:
        result = subprocess.run([sys.executable, "scripts/lint_chapter.py", str(path)],
                                cwd=ROOT, capture_output=True, text=True)
        if result.returncode == 1:
            failed.append(path.name)
            if not quiet:
                print(f"\n$ lint_chapter.py {path.name}")
                print((result.stdout or "").rstrip())
    summary = f"{len(files) - len(failed)}/{len(files)} chapters clean"
    return "chapter lints", EXIT_FAILED if failed else EXIT_OK, summary


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--chapters", action="store_true", help="also lint every chapter file")
    parser.add_argument("--json", action="store_true", help="print the summary as JSON")
    parser.add_argument("--quiet", action="store_true", help="print the table only")
    args = parser.parse_args(argv)
    quiet = args.quiet or args.json

    results = []
    for name, gate_argv, meaning in GATES:
        code, _ = run_gate(gate_argv, quiet)
        results.append({"gate": name, "status": code, "note": "" if code == 0 else meaning})
    if args.chapters:
        name, code, note = chapter_gate(quiet)
        results.append({"gate": name, "status": code, "note": note})

    if args.json:
        print(json.dumps({"gates": results}, ensure_ascii=False, indent=2))
    else:
        print("\n" + "-" * 52)
        for row in results:
            mark = "ok  " if row["status"] == EXIT_OK else ("FAIL" if row["status"] == EXIT_FAILED else "ERR ")
            print(f"  {mark}  {row['gate']:<18} {row['note']}")
        clean = all(r["status"] == EXIT_OK for r in results)
        print("-" * 52)
        print("every gate passes" if clean else "some gates need attention")

    if any(r["status"] == EXIT_CANNOT_RUN for r in results):
        return EXIT_CANNOT_RUN
    return EXIT_FAILED if any(r["status"] != EXIT_OK for r in results) else EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
