"""Command-line front for TetraFrame (used by /tetraframe).

    python -m tools.kpwiki.tetraframe_cli --seed "<decision seed>" \
        [--context-file Canon/x.md ...] [--out Plan/decisions/tetraframe/<slug>.json] [--dry-run]

``--dry-run`` prints the assembled seed and context without an LM call. The
live run executes the six stages with the task LM, writes the run artefact
as JSON to ``--out`` (if given) and prints the verification table. Nothing
else is written; the author decides (command /tetraframe, Step 4).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import lm
from .tetraframe import TetraFrame

ROOT = Path(__file__).resolve().parents[2]


def load_context(paths: list[str]) -> str:
    parts = []
    for p in paths:
        text = (ROOT / p).read_text(encoding="utf-8")
        parts.append(f"### {p}\n{text}")
    return "\n\n".join(parts)


def render_verification(run) -> str:
    rows = [f"{name:24s} {m.score:5.2f}  {'pass' if m.passed else 'FAIL'}  {m.rationale}"
            for name, m in run.verification.metrics.items()]
    rows.append(f"{'aggregate':24s} {run.verification.aggregate:5.2f}")
    rows += [f"retry: {r}" for r in run.verification.retry_recommendations]
    rows += [f"corner retry: {r}" for r in run.retries]
    return "\n".join(rows)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", required=True, help="the decision seed: a genuine tension, not a lookup")
    parser.add_argument("--context-file", action="append", default=[], help="repo-relative file to attach as context")
    parser.add_argument("--out", default="", help="write the run artefact (JSON) here")
    parser.add_argument("--dry-run", action="store_true", help="assemble inputs only, no LM call")
    args = parser.parse_args(argv)

    context = load_context(args.context_file)
    if args.dry_run:
        print(json.dumps({"seed": args.seed, "context_chars": len(context), "context_files": args.context_file},
                         ensure_ascii=False, indent=2))
        return 0
    lm.configure("task")
    run = TetraFrame()(seed=args.seed, context=context).run
    if args.out:
        out = ROOT / args.out
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(run.model_dump_json(indent=2), encoding="utf-8")
        print(f"wrote {args.out}")
    print(f"predicate: {run.selection.primary.text}")
    for mode, corner in run.corners.items():
        print(f"[{mode}] {corner.patched_claim or corner.core_claim}")
    print(f"P*: {run.transformed.transformed_predicate}")
    print(render_verification(run))
    return 0


if __name__ == "__main__":
    sys.exit(main())
