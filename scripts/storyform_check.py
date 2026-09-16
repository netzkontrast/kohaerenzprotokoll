#!/usr/bin/env python3
"""Run the decidable Dramatica checks over the novel's NCP storyforms.

    python3 scripts/storyform_check.py                  # both ncp.json and ncp-b.json
    python3 scripts/storyform_check.py --ncp ncp-b.json # one of them
    python3 scripts/storyform_check.py --json           # machine-readable
    python3 scripts/storyform_check.py --strict         # exit 1 on any violation

`ncp.json` is Storyform A (Kael/K₁) and `ncp-b.json` is Storyform B
(AEGIS/K₀); both live in the manuscript work tree. The checks are in
`tools/kpstoryform`, which reads the vendored NCP v1.3.0 vocabularies and the
Dramatica ontology — no engine, no API key, no network.

Storyform B carries two documented heterodox rows (linear-progressive
signposts). They are Canon-Lock: a run that reports them is working correctly
and they are never "fixed". The default exit status is therefore 0 even when
rows fail; pass --strict when a caller wants failure to be fatal.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from tools import kpstoryform  # noqa: E402  (needs ROOT on the path)

WORK_TREE = ("Manuscript/works/the-agency-system/works/"
             "hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll")
STORYFORMS = {"ncp.json": "A — Kael/K₁", "ncp-b.json": "B — AEGIS/K₀"}
EXIT_OK, EXIT_VIOLATION, EXIT_CANNOT_RUN = 0, 1, 2


def ncp_path(name: str) -> Path:
    return ROOT / WORK_TREE / name


def report_one(name: str, ncp: dict) -> tuple[str, dict]:
    results = kpstoryform.run_all(ncp)
    summary = kpstoryform.summarise(results)
    lines = [f"{name}  ({STORYFORMS.get(name, 'storyform')})",
             f"  {summary['passed']}/{summary['rows']} rows pass"]
    for result in results:
        if result.passed and not result.warnings:
            continue
        mark = "warn " if result.passed else "FAIL "
        lines.append(f"  {mark}row {result.row:>2} {result.name}")
        lines += [f"        {text}" for text in result.violations + result.warnings]
    return "\n".join(lines), summary


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--ncp", action="append", default=[],
                        help="storyform file name; repeatable (default: both)")
    parser.add_argument("--json", action="store_true", help="print the report as JSON")
    parser.add_argument("--strict", action="store_true", help="exit 1 when a row fails")
    args = parser.parse_args(argv)

    wanted = args.ncp or list(STORYFORMS)
    reports, summaries = [], {}
    for name in wanted:
        path = ncp_path(name)
        if not path.is_file():
            print(f"no storyform at {path}", file=sys.stderr)
            return EXIT_CANNOT_RUN
        try:
            ncp = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            print(f"{name}: {exc}", file=sys.stderr)
            return EXIT_CANNOT_RUN
        text, summary = report_one(name, ncp)
        reports.append(text)
        summaries[name] = summary

    if args.json:
        print(json.dumps(summaries, ensure_ascii=False, indent=2))
    else:
        print("\n\n".join(reports))
        print("\nStoryform B's heterodox signpost rows are Canon-Lock; a report is not a defect.")
    failed = any(s["failed"] for s in summaries.values())
    return EXIT_VIOLATION if args.strict and failed else EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
