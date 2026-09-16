"""Offline smoke test for the kpwiki DSPy base.

    python -m tools.kpwiki.smoke --dry-run

Constructs the LMs (no network), the SourceIngest and BatchCompile programs
and their metrics, and scores hand-built predictions against fixtures so a
broken install or a broken schema fails here, not in a paid run. The
BatchCompile half also scores the deliberately broken fixture and checks that
every rule it violates is named in the feedback. ``--live`` runs SourceIngest
on the fixture with the configured task LM (needs ANTHROPIC_API_KEY).
"""
from __future__ import annotations

import argparse
import sys

import dspy

from . import compile_fixture
from . import lm
from .compile_metric import compile_metric
from .metrics import ingest_metric
from .programs import BatchCompile, SourceIngest
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


def dry_run_ingest() -> bool:
    """SourceIngest constructs and its metric accepts a valid prediction."""
    program = SourceIngest()
    result = ingest_metric(fixture_example(), handmade_prediction())
    print(f"  SourceIngest predictors: {[name for name, _ in program.named_predictors()]}")
    print(f"  ingest_metric on fixture: score={result.score:.2f} feedback={result.feedback!r}")
    return result.score > 0.99


def dry_run_compile() -> bool:
    """BatchCompile constructs, its metric accepts the batch and names every broken rule."""
    program = BatchCompile()
    gold = compile_fixture.gold_example()
    good = compile_metric(gold, dspy.Prediction(compiled=compile_fixture.handmade_compiled()))
    broken = compile_metric(gold, dspy.Prediction(compiled=compile_fixture.broken_compiled()))
    missing = [needle for needle in compile_fixture.BROKEN_NEEDLES if needle not in broken.feedback]
    print(f"  BatchCompile predictors: {[name for name, _ in program.named_predictors()]}")
    print(f"  compile_metric on fixture: score={good.score:.2f} · broken batch: {broken.score:.2f}")
    print(f"  broken-batch feedback: {broken.feedback[:160]}…")
    if missing:
        print(f"  FAIL: the broken batch did not name {missing}")
    return good.score >= 0.95 and broken.score < good.score and not missing


def dry_run() -> int:
    for role in ("task", "worker", "reflection"):
        print(f"  LM[{role}] = {lm.model_id(role)}")
    lm.configure("task")
    ok = dry_run_ingest() and dry_run_compile()
    print("OK: kpwiki dry run passed" if ok else "FAIL: a metric did not accept a valid prediction")
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
