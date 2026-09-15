"""Offline smoke test for the kpwiki DSPy base.

    python -m tools.kpwiki.smoke --dry-run

Constructs the LMs (no network), the SourceIngest program and the metric, and
scores a hand-built prediction against a fixture so a broken install or a
broken schema fails here, not in a paid run. ``--live`` runs SourceIngest on
the fixture with the configured task LM (needs ANTHROPIC_API_KEY).
"""
from __future__ import annotations

import argparse
import sys

import dspy

from . import lm
from .metrics import ingest_metric
from .programs import SourceIngest
from .schema import Citation, Claim

FIXTURE_FILE = "Sources/drive/fixture-kohaerenz-notiz.md"
FIXTURE_BODY = """# Notiz zum Kohärenz Protokoll
Das Kohärenz Protokoll ist ein Roman über ein System namens Kael.
Die Kernwelten KW1 bis KW4 folgen je einem eigenen Logik-Regime.
AEGIS wird in Akt I nicht beim Namen genannt.
"""
GOLD_FRAGMENTS = ["Logik-Regime", "nicht beim Namen"]


def fixture_example() -> dspy.Example:
    return dspy.Example(
        source_file=FIXTURE_FILE, title="Notiz zum Kohärenz Protokoll",
        category_hint="kernkonzept", body=FIXTURE_BODY, gold_fragments=GOLD_FRAGMENTS,
    ).with_inputs("source_file", "title", "category_hint", "body")


def handmade_prediction() -> dspy.Prediction:
    claims = [
        Claim(text="Die Kernwelten KW1 bis KW4 folgen je einem eigenen Logik-Regime.", kind="world",
              citation=Citation(file=FIXTURE_FILE, start_line=3, end_line=3), entities=["KW1", "KW4"]),
        Claim(text="AEGIS wird in Akt I nicht beim Namen genannt.", kind="rule",
              citation=Citation(file=FIXTURE_FILE, start_line=4, end_line=4), entities=["AEGIS"]),
    ]
    return dspy.Prediction(claims=claims, conflicts=[])


def dry_run() -> int:
    for role in ("task", "worker", "reflection"):
        print(f"  LM[{role}] = {lm.model_id(role)}")
    lm.configure("task")
    program = SourceIngest()
    predictors = [name for name, _ in program.named_predictors()]
    result = ingest_metric(fixture_example(), handmade_prediction())
    ok = result.score > 0.99
    print(f"  program predictors: {predictors}")
    print(f"  metric on fixture: score={result.score:.2f} feedback={result.feedback!r}")
    print("OK: kpwiki dry run passed" if ok else "FAIL: metric did not accept a valid prediction")
    return 0 if ok else 1


def live_run() -> int:
    lm.configure("task")
    example = fixture_example()
    pred = SourceIngest()(**example.inputs())
    print(pred.triage)
    for claim in pred.claims:
        print(f"  - {claim.kind}: {claim.text} {claim.citation.marker()}")
    print(ingest_metric(example, pred))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--live", action="store_true")
    args = parser.parse_args(argv)
    return live_run() if args.live else dry_run()


if __name__ == "__main__":
    sys.exit(main())
