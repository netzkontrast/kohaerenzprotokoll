"""Offline tests for the TetraFrame port (skip when dspy is not installed)."""
from __future__ import annotations

import pytest

dspy = pytest.importorskip("dspy")

from tools.kpwiki import tetraframe as tf  # noqa: E402
from tools.kpwiki import tetraframe_metric as tm  # noqa: E402

SEED = "Canon says AEGIS is never named in Act I, but three later documents assume the name is known from chapter 3."


def corner(mode, claim, **kw) -> tf.Corner:
    base = dict(mode=mode, core_claim=claim, strongest_case=claim, patched_claim=claim,
                unique_signal=f"signal of {mode}", basis_label={"P": "affirmation", "not-P": "rejection"}.get(mode, ""),
                scope_conditions=["Act I chapters 1-13"], minimal_falsifiers=["A chapter 3 scene naming AEGIS in the manuscript"],
                confidence_boundaries=["holds until the drafting brief changes"], evidence_needs=["canon: storyform §3 quote"],
                confidence_score=0.8)
    base.update(kw)
    return tf.Corner(**base)


def fixture_run() -> tf.TetraFrameRun:
    corners = {
        "P": corner("P", "The Act I naming lock must stand; the later documents are superseded drafts."),
        "not-P": corner("not-P", "The lock is a drafting artefact; naming in chapter 3 raises stakes earlier."),
        "both": corner("both", "The lock holds for Kael's perspective while AEGIS logs may carry the name.",
                       basis_label="role_split", basis_explanation="Both hold under a role split: reader vs POV knowledge co-hold simultaneously."),
        "neither": corner("neither", "The predicate bundles two questions: when the reader learns the name and when Kael does.",
                          basis_label="overloaded_predicate", replacement_predicate="Separate reader-knowledge from POV-knowledge of the name.",
                          basis_explanation="The naming question is overloaded because it conflates reader knowledge with the character's knowledge fence."),
    }
    cartography = tf.Cartography(contradiction_map=["P vs not-P on whether the lock is canon"],
                                 complementarity_map=["both and neither agree the predicate mixes two fences"],
                                 discriminators=[tf.Discriminator(discriminator="does any Act I scene need the name for causality?")],
                                 reversible_implications=["renaming later"], irreversible_implications=["reader knows the name"],
                                 invariants=["Kael's knowledge fence stays intact"])
    frame = tf.TransformedFrame(
        transformed_predicate="Separate the reader's and Kael's knowledge of the name; keep the POV fence, allow the log fence to open earlier.",
        transformed_frame="Two fences instead of one lock; AEGIS logs may name, Kael's perspective may not.",
        survivors_from_p=["Kael's fence"], survivors_from_not_p=["earlier stakes via logs"],
        hidden_structure_from_both=["role split reader/POV"], dissolved_false_frame_from_neither=["one naming lock"],
        operational_tests=["lint: no AEGIS name in Kael-POV prose of chapters 1-13"],
        boundary_conditions=["only Act I"], failure_modes=["reader confusion if logs name too early"], confidence=0.7)
    return tf.TetraFrameRun(seed=SEED, distilled=tf.DistilledSeed(normalized_seed=SEED, frame_risk_score=0.6,
                                                                 evaluation_criteria=["knowledge fences intact"]),
                            selection=tf.PredicateSelection(primary=tf.Predicate(text="The Act I naming lock for AEGIS is canon")),
                            corners=corners, cartography=cartography, transformed=frame)


def test_program_predictors_are_named():
    names = [n for n, _ in tf.TetraFrame().named_predictors()]
    assert {"distill.predict", "corner_p.predict", "corner_both.predict", "corner_neither.predict", "map.predict"} <= set(names)


def test_corner_view_isolation():
    view = tf.make_view(fixture_run().distilled, fixture_run().selection, "both")
    tm.assert_isolation(view)
    assert "corners" not in view.model_dump() and view.corner_contract == tf.CORNER_CONTRACTS["both"]


def test_near_duplicate_detection():
    run = fixture_run()
    run.corners["not-P"] = corner("not-P", run.corners["P"].core_claim)
    dupes = tm.near_duplicates(run.corners, run.distilled.normalized_seed)
    assert dupes and dupes[0][:2] == ("P", "not-P")


def test_both_and_neither_rigor_reject_compromise_and_evasion():
    run = fixture_run()
    assert tm.both_rigor(run.corners["both"]) >= 0.85 and tm.neither_rigor(run.corners["neither"]) >= 0.85
    mushy = corner("both", "A balanced approach that finds a middle ground.", basis_label="compromise", basis_explanation="")
    assert tm.both_rigor(mushy) < 0.4
    evasive = corner("neither", "It depends on the reader.", basis_label="", basis_explanation="short")
    assert tm.neither_rigor(evasive) < 0.4


def test_verify_run_passes_fixture_and_flags_averaging():
    run = fixture_run()
    verdict = tm.verify_run(run)
    assert verdict.metrics["branch_independence"].passed and verdict.metrics["transformation_quality"].passed
    assert verdict.aggregate > 0.75 and not verdict.retry_recommendations
    run.transformed.transformed_frame = "On the one hand the lock, on the other hand the logs: a balanced approach."
    assert not tm.verify_run(run).metrics["transformation_quality"].passed


def test_metric_returns_prediction_with_named_deficits():
    run = fixture_run()
    gold = dspy.Example(seed=SEED, allowed_both_basis=["role_split"], expected_neither_failure_modes=["false_binary"],
                        banned_transformed_phrases=["balanced approach"]).with_inputs("seed")
    result = tm.tetraframe_metric(gold, dspy.Prediction(run=run))
    assert isinstance(result, dspy.Prediction) and 0.5 < result.score < 1.0
    assert "overloaded_predicate" in result.feedback and "false_binary" in result.feedback
    assert tm.tetraframe_metric(gold, dspy.Prediction(run="nope")).score == 0.0


def test_transform_reward_penalises_compromise():
    good = dspy.Prediction(frame=fixture_run().transformed)
    assert tm.transform_reward({}, good) == 1.0
    bad_frame = fixture_run().transformed.model_copy(update={"transformed_frame": "split the difference"})
    assert tm.transform_reward({}, dspy.Prediction(frame=bad_frame)) == 0.6
