"""TetraFrame guards, verification suite and GEPA metric (deterministic).

Port of the heuristics in Hmbown/tetraframe-dspy ``guards.py`` and
``metrics.py``. Nine metrics with the original thresholds; an LM judge for
the rigor and transformation metrics is optional (``verify_run(run, judge=)``)
and only consulted when the heuristic is below 0.85 / 0.88. The GEPA metric
returns ``dspy.Prediction(score, feedback)``.
"""
from __future__ import annotations

import re
from itertools import combinations
from typing import Callable

import dspy

from .tetraframe import (BOTH_BASES, INCOMPATIBLE_PAIRS, NEITHER_FAILURES, Cartography, Corner, CornerView,
                         MetricScore, TetraFrameRun, TransformedFrame, Verification)

BLOCKED_VIEW_FIELDS = {"raw_seed", "candidate_predicates", "rejected", "rationale", "corners", "other_corner",
                       "cartography", "transformed", "verification", "traces"}
MUSH_WORDS = {"balanced", "nuanced", "important", "helpful", "complex", "thoughtful", "consider", "various",
              "multiple", "ausgewogen", "nuanciert", "differenziert"}
COMPROMISE_MARKERS = ("middle ground", "balance both", "balanced approach", "split the difference",
                      "on the one hand", "on the other hand", "mittelweg", "einerseits", "sowohl als auch")
OBSERVABLE_MARKERS = ("experiment", "benchmark", "metric", "trace", "counterexample", "failure rate", "dataset",
                      "measurement", "log", "kapitel", "szene", "canon", "quelle", "zitat", "beleg")
CROSS_REFERENCE_MARKERS = ("other corner", "another corner", "p says", "not-p says", "neither says", "both says",
                           "as above", "the previous branch", "die andere position")
THRESHOLDS = {"branch_independence": 0.90, "divergence_quality": 0.45, "rigor_of_both": 0.78,
              "rigor_of_neither": 0.78, "contradiction_honesty": 0.75, "transformation_quality": 0.82,
              "robustness": 0.70, "fake_novelty_risk": 0.70, "slop_risk": 0.70}
NEAR_DUPLICATE_SIMILARITY = 0.78
_TOKEN_RE = re.compile(r"[a-zA-ZäöüÄÖÜß_]+")

Judge = Callable[[str, object], tuple[float, str]]   # (kind, artefact) -> (score, rationale)


# --- guards ------------------------------------------------------------------

def assert_isolation(view: CornerView) -> None:
    """A corner sees the CornerView fields and nothing else (raises on a leaked field)."""
    fields = set(view.model_dump())
    leaked = fields & BLOCKED_VIEW_FIELDS
    extra = fields - set(CornerView.model_fields)
    if leaked or extra:
        raise ValueError(f"corner view leaked fields: {sorted(leaked | extra)}")


def _tokens(text: str) -> list[str]:
    return [t for t in _TOKEN_RE.findall((text or "").lower()) if len(t) > 2]


def residual_tokens(text: str, seed_text: str) -> list[str]:
    seed = set(_tokens(seed_text))
    return [t for t in _tokens(text) if t not in seed]


def similarity(a: str, b: str) -> float:
    ta, tb = set(_tokens(a)), set(_tokens(b))
    if not ta and not tb:
        return 1.0
    if not ta or not tb:
        return 0.0
    return round(len(ta & tb) / len(ta | tb), 3)


def near_duplicates(corners: dict[str, Corner], seed_text: str,
                    threshold: float = NEAR_DUPLICATE_SIMILARITY) -> list[tuple[str, str, float]]:
    """Corners whose claims coincide once the seed's own words are removed."""
    out = []
    for left, right in combinations(corners, 2):
        sim = similarity(" ".join(residual_tokens(corners[left].core_claim, seed_text)),
                         " ".join(residual_tokens(corners[right].core_claim, seed_text)))
        if sim >= threshold:
            out.append((left, right, sim))
    return out


def _mean(values) -> float:
    values = list(values)
    return sum(values) / len(values) if values else 0.0


# --- component heuristics ----------------------------------------------------

def evidence_specificity(items: list[str]) -> float:
    if not items:
        return 0.0
    hits = []
    for item in items:
        lowered = item.lower()
        specific = any(m in lowered for m in OBSERVABLE_MARKERS) or bool(re.search(r"\b\d+\b", lowered)) or ":" in lowered
        hits.append(1.0 if specific else 0.25)
    return round(_mean(hits), 3)


def falsifier_quality(corner: Corner) -> float:
    if not corner.minimal_falsifiers:
        return 0.0
    directness = _mean(1.0 if len(f.split()) >= 5 else 0.5 for f in corner.minimal_falsifiers)
    return round((directness + evidence_specificity(corner.minimal_falsifiers)) / 2.0, 3)


def both_rigor(corner: Corner) -> float:
    basis_ok = 1.0 if corner.basis_label in BOTH_BASES else 0.0
    compromise = 0.4 if any(m in corner.strongest_case.lower() for m in COMPROMISE_MARKERS) else 0.0
    co_hold = 1.0 if any(w in corner.basis_explanation.lower() for w in ("both", "co-hold", "simult", "split", "beide", "zugleich")) else 0.5
    scope = 1.0 if corner.scope_conditions else 0.5
    return round(max(0.0, _mean([basis_ok, co_hold, scope, falsifier_quality(corner)]) - compromise), 3)


def neither_rigor(corner: Corner) -> float:
    mode_ok = 1.0 if corner.basis_label in NEITHER_FAILURES else 0.0
    replacement = 1.0 if (corner.replacement_predicate.strip() or corner.replacement_frame.strip()) else 0.0
    diagnosis = 1.0 if len(corner.basis_explanation.split()) >= 8 else 0.5
    evasion = 0.3 if "it depends" in corner.strongest_case.lower() or "kommt darauf an" in corner.strongest_case.lower() else 0.0
    return round(max(0.0, _mean([mode_ok, replacement, diagnosis, falsifier_quality(corner)]) - evasion), 3)


def branch_independence(run: TetraFrameRun) -> float:
    cross = _mean(sum(m in (c.core_claim + " " + c.strongest_case).lower() for m in CROSS_REFERENCE_MARKERS) / 2.0
                  for c in run.corners.values())
    seed = run.distilled.normalized_seed
    pair = [max(0.0, similarity(" ".join(sorted(residual_tokens(run.corners[a].core_claim, seed))),
                                " ".join(sorted(residual_tokens(run.corners[b].core_claim, seed)))) - 0.35)
            for a, b in INCOMPATIBLE_PAIRS]
    return round(max(0.0, 1.0 - min(1.0, 0.2 * cross + 0.6 * _mean(pair))), 3)


def divergence_quality(run: TetraFrameRun) -> float:
    seed = run.distilled.normalized_seed
    claims = [1.0 - similarity(" ".join(sorted(residual_tokens(run.corners[a].patched_claim or run.corners[a].core_claim, seed))),
                               " ".join(sorted(residual_tokens(run.corners[b].patched_claim or run.corners[b].core_claim, seed))))
              for a, b in INCOMPATIBLE_PAIRS]
    signals = [1.0 - similarity(run.corners[a].unique_signal, run.corners[b].unique_signal) for a, b in INCOMPATIBLE_PAIRS]
    return round(0.7 * _mean(claims) + 0.3 * _mean(signals), 3)


def contradiction_honesty(cartography: Cartography) -> float:
    n_contra, n_compl, n_evid = len(cartography.contradiction_map), len(cartography.complementarity_map), len(cartography.discriminators)
    if n_contra == 0:
        return 0.35 if n_compl else 0.25
    return round(min(1.0, 0.4 + 0.1 * n_contra + 0.05 * n_evid), 3)


def non_averaging(frame: TransformedFrame, corners: dict[str, Corner]) -> float:
    text = (frame.transformed_frame + " " + frame.transformed_predicate).lower()
    compromise = any(m in text for m in COMPROMISE_MARKERS)
    required = [frame.survivors_from_p, frame.survivors_from_not_p, frame.hidden_structure_from_both,
                frame.dissolved_false_frame_from_neither, frame.operational_tests]
    overlap = similarity(frame.transformed_predicate, corners["P"].patched_claim + " " + corners["not-P"].patched_claim)
    # Deviation from the original: cap at 1.0 BEFORE the compromise penalty, so
    # compromise language always drops the score below the 0.82 threshold.
    score = min(1.0, _mean(1.0 if x else 0.0 for x in required) + 0.3 * (1.0 - min(1.0, overlap)))
    return round(max(0.0, score - (0.4 if compromise else 0.0)), 3)


def robustness(run: TetraFrameRun) -> float:
    f, c = run.transformed, run.cartography
    coverage = _mean([1.0 if f.boundary_conditions else 0.0, 1.0 if f.failure_modes else 0.0,
                      1.0 if c.reversible_implications else 0.0, 1.0 if c.irreversible_implications else 0.0])
    confidence = _mean(x.confidence_score for x in run.corners.values())
    return round(0.6 * coverage + 0.4 * min(1.0, confidence), 3)


def fake_novelty_resistance(run: TetraFrameRun) -> float:
    frame_tokens = set(_tokens(run.transformed.transformed_predicate))
    source = " ".join([run.selection.primary.text, run.distilled.normalized_seed,
                       *(c.patched_claim + " " + c.strongest_case + " " + c.replacement_predicate + " " + c.replacement_frame
                         for c in run.corners.values()),
                       *run.cartography.invariants, *run.cartography.frame_validity_map, run.cartography.arbiter_notes,
                       *run.cartography.transformation, *run.cartography.dissolution,
                       *run.transformed.survivors_from_p, *run.transformed.survivors_from_not_p,
                       *run.transformed.hidden_structure_from_both, *run.transformed.dissolved_false_frame_from_neither])
    source_tokens = set(_tokens(source))
    supported = lambda t: t in source_tokens or any(len(s) > 3 and s in t for s in source_tokens)  # noqa: E731
    unsupported = [t for t in frame_tokens if len(t) > 4 and not supported(t)]
    return round(max(0.0, 1.0 - min(0.6, 0.08 * len(unsupported))), 3)


def slop_resistance(run: TetraFrameRun) -> float:
    texts = [run.transformed.transformed_frame, run.transformed.non_averaging_explanation,
             *(c.patched_claim for c in run.corners.values())]
    tokens = [t for text in texts for t in _tokens(text)]
    mush = sum(t in MUSH_WORDS for t in tokens) / len(tokens) if tokens else 0.0
    evidence = _mean(evidence_specificity(c.evidence_needs) for c in run.corners.values())
    return round(0.5 * max(0.0, 1.0 - 3.0 * mush) + 0.5 * evidence, 3)


# --- suite ---------------------------------------------------------------------

def _scored(name: str, score: float, rationale: str) -> MetricScore:
    return MetricScore(score=round(score, 3), rationale=rationale, passed=score >= THRESHOLDS[name])


def verify_run(run: TetraFrameRun, judge: Judge | None = None) -> Verification:
    """Heuristics first; the optional judge only where the heuristic is not decisive."""
    both, neither = run.corners["both"], run.corners["neither"]
    rb, rn = both_rigor(both), neither_rigor(neither)
    rb_why, rn_why = "heuristic: basis, co-holding, scope, falsifiers", "heuristic: failure mode, replacement, diagnosis, falsifiers"
    if judge and rb < 0.85:
        rb, rb_why = judge("both", both)
    if judge and rn < 0.85:
        rn, rn_why = judge("neither", neither)
    tq, tq_why = non_averaging(run.transformed, run.corners), "heuristic: survivors/dissolution present, no compromise text, low overlap"
    if judge and tq < 0.88:
        tq, tq_why = judge("transform", run)
    metrics = {
        "branch_independence": _scored("branch_independence", branch_independence(run), "cross-references and residual overlap of incompatible corners"),
        "divergence_quality": _scored("divergence_quality", divergence_quality(run), "distinct claims and unique signals across incompatible corners"),
        "rigor_of_both": _scored("rigor_of_both", rb, rb_why),
        "rigor_of_neither": _scored("rigor_of_neither", rn, rn_why),
        "contradiction_honesty": _scored("contradiction_honesty", contradiction_honesty(run.cartography), "explicit contradictions and discriminators kept"),
        "transformation_quality": _scored("transformation_quality", tq, tq_why),
        "robustness": _scored("robustness", robustness(run), "boundary conditions, failure modes, reversibility, confidence"),
        "fake_novelty_risk": _scored("fake_novelty_risk", fake_novelty_resistance(run), "P* terms supported by corners and cartography"),
        "slop_risk": _scored("slop_risk", slop_resistance(run), "mush words and evidence specificity"),
    }
    advice = {
        "branch_independence": "Retry stage 2 with stronger anti-collapse hints and fresh rollout ids.",
        "rigor_of_both": "Retry the both corner with basis-specific hardening.",
        "rigor_of_neither": "Retry the neither corner with a stricter frame-failure diagnosis.",
        "transformation_quality": "Retry the transform with non-averaging pressure and cartography invariants.",
    }
    recommendations = [text for name, text in advice.items() if not metrics[name].passed]
    return Verification(metrics=metrics, aggregate=round(_mean(m.score for m in metrics.values()), 3),
                        retry_recommendations=recommendations)


# --- rewards and the GEPA metric ---------------------------------------------

def transform_reward(args: dict, pred: dspy.Prediction) -> float:
    """BestOfN reward for the transform stage: survivors present, no compromise language."""
    frame = getattr(pred, "frame", None)
    if frame is None:
        return 0.0
    text = (frame.transformed_predicate + " " + frame.transformed_frame).lower()
    penalty = 0.4 if any(m in text for m in COMPROMISE_MARKERS) else 0.0
    parts = [frame.survivors_from_p, frame.survivors_from_not_p, frame.hidden_structure_from_both, frame.dissolved_false_frame_from_neither]
    return round(max(0.0, _mean(1.0 if p else 0.0 for p in parts) - penalty), 3)


def _term_hits(text: str, terms: list[str]) -> float:
    return _mean(1.0 if t.lower() in text.lower() else 0.0 for t in terms) if terms else 1.0


def tetraframe_metric(gold: dspy.Example, pred: dspy.Prediction, trace=None,
                      pred_name=None, pred_trace=None) -> dspy.Prediction:
    """Verification aggregate plus optional gold expectations, with named deficits as feedback."""
    run = getattr(pred, "run", None)
    if not isinstance(run, TetraFrameRun):
        return dspy.Prediction(score=0.0, feedback="Prediction carries no TetraFrameRun.")
    verification = run.verification or verify_run(run)
    parts, feedback = [verification.aggregate], []
    for name, metric in verification.metrics.items():
        if not metric.passed:
            feedback.append(f"{name} {metric.score:.2f} < {THRESHOLDS[name]:.2f} ({metric.rationale}).")
    expect_pred = list(getattr(gold, "expected_primary_predicate_contains", []) or [])
    if expect_pred:
        s = _term_hits(run.selection.primary.text, expect_pred)
        parts.append(s)
        if s < 1.0:
            feedback.append(f"Primary predicate misses expected terms {expect_pred}.")
    allowed_basis = list(getattr(gold, "allowed_both_basis", []) or [])
    if allowed_basis:
        ok = run.corners["both"].basis_label in allowed_basis
        parts.append(1.0 if ok else 0.0)
        if not ok:
            feedback.append(f"'both' used basis {run.corners['both'].basis_label!r}; allowed {allowed_basis}.")
    expect_fail = list(getattr(gold, "expected_neither_failure_modes", []) or [])
    if expect_fail:
        ok = run.corners["neither"].basis_label in expect_fail
        parts.append(1.0 if ok else 0.0)
        if not ok:
            feedback.append(f"'neither' used failure mode {run.corners['neither'].basis_label!r}; expected one of {expect_fail}.")
    banned = list(getattr(gold, "banned_transformed_phrases", []) or [])
    if banned:
        text = (run.transformed.transformed_predicate + " " + run.transformed.transformed_frame).lower()
        hit = [b for b in banned if b.lower() in text]
        parts.append(0.0 if hit else 1.0)
        if hit:
            feedback.append(f"P* uses banned compromise phrases {hit}.")
    return dspy.Prediction(score=round(_mean(parts), 3),
                           feedback=" ".join(feedback) or "Structurally strong run: independent corners, rigorous both/neither, transformed P*.")
