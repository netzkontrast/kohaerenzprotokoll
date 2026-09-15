"""Command-line front for the clarify gate (used by /clarify).

    python -m tools.kpwiki.clarify_cli --claim "<text>" --source Sources/drive/x.md:12-14 \
        [--entities AEGIS,Kael] [--glossary aegis,kael] [--canon-context-file Canon/x.md] [--dry-run]

Reads the cited lines from the source export, runs ``ClarifyGate`` with the
task LM, prints the ``Clarification`` as JSON plus the metric score and
feedback. ``--dry-run`` assembles and prints the inputs without an LM call.
Nothing is written anywhere; acting on the verdict is the /clarify command's
Step 3.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import dspy

from . import lm
from .clarify import ClarifyGate, may_propose_promotion
from .clarify_metric import clarify_metric

ROOT = Path(__file__).resolve().parents[2]


def read_excerpt(spec: str) -> str:
    """``path:start-end`` → the cited lines (1-based, inclusive)."""
    path, _, span = spec.rpartition(":")
    start, _, end = span.partition("-")
    lines = (ROOT / path).read_text(encoding="utf-8").splitlines()
    first, last = int(start), int(end or start)
    if not 1 <= first <= last <= len(lines):
        raise SystemExit(f"citation {spec} is outside the file ({len(lines)} lines)")
    return "\n".join(lines[first - 1:last])


def build_example(args: argparse.Namespace) -> dspy.Example:
    context = Path(args.canon_context_file).read_text(encoding="utf-8") if args.canon_context_file else ""
    return dspy.Example(
        claim_text=args.claim, source_excerpt=read_excerpt(args.source),
        entities=[e.strip() for e in args.entities.split(",") if e.strip()],
        glossary_terms=args.glossary, canon_context=context,
    ).with_inputs("claim_text", "source_excerpt", "entities", "glossary_terms", "canon_context")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--claim", required=True)
    parser.add_argument("--source", required=True, help="repo-relative path:start-end")
    parser.add_argument("--entities", default="")
    parser.add_argument("--glossary", default="", help="comma-separated codex slugs")
    parser.add_argument("--canon-context-file", default="")
    parser.add_argument("--dry-run", action="store_true", help="assemble inputs only, no LM call")
    args = parser.parse_args(argv)

    example = build_example(args)
    if args.dry_run:
        print(json.dumps(example.inputs().toDict(), ensure_ascii=False, indent=2))
        return 0
    lm.configure("task")
    pred = ClarifyGate()(**example.inputs())
    verdict = clarify_metric(example, pred)
    print(pred.clarification.model_dump_json(indent=2))
    print(f"score={verdict.score:.2f} promotable={may_propose_promotion(pred.clarification)}")
    print(verdict.feedback)
    return 0


if __name__ == "__main__":
    sys.exit(main())
