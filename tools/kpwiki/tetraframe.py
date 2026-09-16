"""TetraFrame — four-corner decision assessment as a DSPy program.

Port of Hmbown/tetraframe-dspy (MIT, docs/tetraframe-LICENSE.txt). For
decisions that a pro/con list would flatten: the predicate is reasoned over
from four isolated corners — P, not-P, both (a typed co-holding, never a
compromise), neither (a frame failure with a replacement predicate) — their
relations are mapped, and a framing P* is synthesized that preserves the
tension. ``verify_run`` in ``tetraframe_metric.py`` scores the run; the
program never decides — the author does (command /tetraframe).

Differences from the original: typed Pydantic outputs instead of JSON
strings, corner isolation enforced by the ``CornerView`` model, the
verification suite is deterministic by default (an LM judge is optional),
and the GEPA metric returns ``dspy.Prediction``.
"""
from __future__ import annotations

import hashlib
from typing import Literal

import dspy
from pydantic import BaseModel, Field

CornerMode = Literal["P", "not-P", "both", "neither"]
MODES: tuple[CornerMode, ...] = ("P", "not-P", "both", "neither")
BOTH_BASES = ("temporal_split", "scale_split", "role_split", "ontology_split",
              "context_split", "layered_causality", "admissible_paradox")
NEITHER_FAILURES = ("category_error", "false_binary", "overloaded_predicate", "missing_latent_variable",
                    "bad_ontology", "ill_posed_objective", "frame_collapse_under_scrutiny")
RelationType = Literal["opposition", "contradiction", "complementarity", "paradox",
                       "dissolution", "transformation", "support", "block"]
INCOMPATIBLE_PAIRS: tuple[tuple[CornerMode, CornerMode], ...] = (("P", "not-P"), ("P", "neither"), ("not-P", "neither"))
CORNER_TEMPERATURES = {"P": 0.7, "not-P": 0.85, "both": 0.9, "neither": 0.9}
CORNER_CONTRACTS = {
    "P": "Strongest clean affirmation of the predicate. No compromise, no mention of other corners.",
    "not-P": "Strongest clean rejection, inversion or dismantling of the predicate. No mere surface negation.",
    "both": "Valid only when P and not-P co-hold under a typed split or an admissible paradox.",
    "neither": "Valid only when the predicate is misframed and replaced by a better predicate or frame.",
}
ANTI_COLLAPSE_HINTS = {
    "P": "State the strongest clean affirmation of the predicate itself. Do not hedge into synthesis.",
    "not-P": "Find a deeper failure, inversion or dismantling. Do not restate the seed with weaker confidence.",
    "both": "Choose one explicit co-holding basis (e.g. role_split, temporal_split) and show why P and not-P both hold under it.",
    "neither": "Diagnose a concrete frame failure (e.g. overloaded_predicate, false_binary) and replace the predicate.",
}


# --- artefacts -------------------------------------------------------------

class DistilledSeed(BaseModel):
    normalized_seed: str
    stakes: list[str] = Field(default_factory=list)
    constraints: list[str] = Field(default_factory=list)
    unknowns: list[str] = Field(default_factory=list)
    hidden_assumptions: list[str] = Field(default_factory=list)
    candidate_predicates: list[str] = Field(default_factory=list)
    frame_risk_score: float = Field(ge=0.0, le=1.0, description="high when the seed bundles objectives or confuses categories")
    evaluation_criteria: list[str] = Field(default_factory=list)


class Predicate(BaseModel):
    text: str
    subject: str = ""
    relation: str = ""
    object: str = ""
    scope: str = ""
    operational_tests: list[str] = Field(default_factory=list)


class RejectedPredicate(BaseModel):
    text: str
    reason: str
    rewrite_suggestion: str = ""


class PredicateSelection(BaseModel):
    primary: Predicate
    sub_predicates: list[Predicate] = Field(default_factory=list)
    rejected: list[RejectedPredicate] = Field(default_factory=list)
    rationale: str = ""


class CornerView(BaseModel):
    """The only thing a corner generator ever sees — no other corner, no seed text, no cartography."""

    normalized_seed: str
    stakes: list[str]
    constraints: list[str]
    unknowns: list[str]
    hidden_assumptions: list[str]
    primary_predicate: str
    sub_predicates: list[str]
    evaluation_criteria: list[str]
    corner_contract: str
    anti_collapse_hint: str


class Corner(BaseModel):
    mode: CornerMode
    core_claim: str
    assumptions: list[str] = Field(default_factory=list)
    strongest_case: str
    scope_conditions: list[str] = Field(default_factory=list)
    falsifiers: list[str] = Field(default_factory=list)
    evidence_needs: list[str] = Field(default_factory=list)
    unique_signal: str = ""
    basis_label: str = Field(description="'affirmation' | 'rejection' | a both-basis | a neither failure mode")
    basis_explanation: str = ""
    replacement_predicate: str = ""
    replacement_frame: str = ""
    internal_attack: list[str] = Field(default_factory=list)
    patched_claim: str = ""
    minimal_falsifiers: list[str] = Field(default_factory=list)
    confidence_boundaries: list[str] = Field(default_factory=list)
    unresolved_weaknesses: list[str] = Field(default_factory=list)
    confidence_score: float = Field(ge=0.0, le=1.0, default=0.5)
    still_valid: bool = True
    invalidity_reason: str = ""


class PairRelation(BaseModel):
    source: CornerMode
    target: CornerMode
    relation: RelationType
    rationale: str
    evidence_discriminator: str = ""
    reversible: bool = False


class Discriminator(BaseModel):
    discriminator: str
    corner_favors: str = ""
    evidence_needed: str = ""


class Reconstruction(BaseModel):
    mode: CornerMode
    fair_restatement: str
    unsupported_premises: list[str] = Field(default_factory=list)


class StructuralMiss(BaseModel):
    mode: CornerMode
    detects: str


class Cartography(BaseModel):
    pairwise: list[PairRelation] = Field(default_factory=list)
    contradiction_map: list[str] = Field(default_factory=list)
    complementarity_map: list[str] = Field(default_factory=list)
    paradox_map: list[str] = Field(default_factory=list)
    category_error_map: list[str] = Field(default_factory=list)
    frame_validity_map: list[str] = Field(default_factory=list)
    discriminators: list[Discriminator] = Field(default_factory=list)
    invariants: list[str] = Field(default_factory=list)
    reversible_implications: list[str] = Field(default_factory=list)
    irreversible_implications: list[str] = Field(default_factory=list)
    structural_miss: list[StructuralMiss] = Field(default_factory=list)
    reconstructions: list[Reconstruction] = Field(default_factory=list)
    dissolution: list[str] = Field(default_factory=list)
    transformation: list[str] = Field(default_factory=list)
    arbiter_notes: str = ""


class TransformedFrame(BaseModel):
    transformed_predicate: str
    transformed_frame: str
    survivors_from_p: list[str] = Field(default_factory=list)
    survivors_from_not_p: list[str] = Field(default_factory=list)
    hidden_structure_from_both: list[str] = Field(default_factory=list)
    dissolved_false_frame_from_neither: list[str] = Field(default_factory=list)
    non_averaging_explanation: str = ""
    operational_tests: list[str] = Field(default_factory=list)
    boundary_conditions: list[str] = Field(default_factory=list)
    failure_modes: list[str] = Field(default_factory=list)
    confidence: float = Field(ge=0.0, le=1.0, default=0.5)


class MetricScore(BaseModel):
    score: float
    rationale: str
    passed: bool


class Verification(BaseModel):
    metrics: dict[str, MetricScore]
    aggregate: float
    retry_recommendations: list[str] = Field(default_factory=list)


class TetraFrameRun(BaseModel):
    seed: str
    distilled: DistilledSeed
    selection: PredicateSelection
    corners: dict[str, Corner]
    cartography: Cartography
    transformed: TransformedFrame
    verification: Verification | None = None
    retries: list[str] = Field(default_factory=list)


# --- signatures --------------------------------------------------------------

class DistillSeed(dspy.Signature):
    """Distill a raw decision seed into an operational brief: stakes, constraints, unknowns,
    hidden assumptions, candidate predicates, evaluation criteria. Prefer operational
    predicates over slogans. Give a high frame risk when the seed bundles several objectives
    or confuses categories. Quote canon passages in their language; write the brief in English."""

    seed: str = dspy.InputField()
    context: str = dspy.InputField(desc="canon passages, claims with citations, prior decisions; may be empty")
    distilled: DistilledSeed = dspy.OutputField()


class SelectPredicate(dspy.Signature):
    """Split the candidate predicates into atomic operational ones, reject malformed ones with a
    reason and a rewrite, and choose the primary predicate: operational, falsifiable, specific
    enough to support meaningful P, not-P, both and neither corners."""

    distilled: DistilledSeed = dspy.InputField()
    selection: PredicateSelection = dspy.OutputField()


class GenerateCorner(dspy.Signature):
    """Generate and harden one corner from the view alone. Build the position, attack it from
    within, patch the weaknesses, tighten the language, name minimal falsifiers and confidence
    boundaries, and say whether it still stands. Never mention or anticipate other corners."""

    view: CornerView = dspy.InputField()
    corner: Corner = dspy.OutputField()


class CornerP(GenerateCorner):
    """Strongest clean affirmation of the predicate, hardened from within. No hedging into
    compromise, no reference to other positions. basis_label must be exactly 'affirmation'."""


class CornerNotP(GenerateCorner):
    """Strongest clean rejection, inversion or dismantling of the predicate's substance, causal
    logic or usefulness — not a surface negation — hardened from within.
    basis_label must be exactly 'rejection'."""


class CornerBoth(GenerateCorner):
    """Strongest valid 'both' corner: NOT a compromise. Valid only if P and not-P co-hold under
    exactly one basis from temporal_split, scale_split, role_split, ontology_split,
    context_split, layered_causality, admissible_paradox — put it in basis_label and show why
    both hold under it. Hardened from within."""


class CornerNeither(GenerateCorner):
    """Strongest valid 'neither' corner: NOT evasion. Valid only if the predicate is misframed;
    basis_label must be one of category_error, false_binary, overloaded_predicate,
    missing_latent_variable, bad_ontology, ill_posed_objective, frame_collapse_under_scrutiny,
    and replacement_predicate or replacement_frame must propose something better. Hardened from within."""


class RelateCorners(dspy.Signature):
    """Classify the relation between two corners without inventing premises, and say what
    evidence would discriminate between them."""

    source: Corner = dspy.InputField()
    target: Corner = dspy.InputField()
    relation: RelationType = dspy.OutputField()
    rationale: str = dspy.OutputField()
    evidence_discriminator: str = dspy.OutputField()
    reversible: bool = dspy.OutputField()


class MapCorners(dspy.Signature):
    """Map the four corners: contradictions, complementarities, paradoxes, category errors,
    frame validity, evidence discriminators, invariants, reversible and irreversible
    implications, what each corner uniquely detects; reconstruct each corner sympathetically,
    separate dissolution from transformation, write arbiter notes. Add no unsupported premises."""

    corners: list[Corner] = dspy.InputField()
    pairwise: list[PairRelation] = dspy.InputField()
    cartography: Cartography = dspy.OutputField()


class TransformFrame(dspy.Signature):
    """Produce the transformed framing P*. Not an average or compromise: keep what survives from
    P and from not-P, reveal the hidden structure 'both' exposed, dissolve the false framing
    'neither' exposed, and give operational tests, boundary conditions and failure modes."""

    primary_predicate: str = dspy.InputField()
    corners: list[Corner] = dspy.InputField()
    cartography: Cartography = dspy.InputField()
    evaluation_criteria: list[str] = dspy.InputField()
    frame: TransformedFrame = dspy.OutputField()


class CornerRigorJudge(dspy.Signature):
    """Judge whether a 'both' or 'neither' corner is rigorous (0..1): penalise compromise
    masquerading as both and evasion masquerading as neither."""

    corner: Corner = dspy.InputField()
    score: float = dspy.OutputField()
    rationale: str = dspy.OutputField()


class TransformationJudge(dspy.Signature):
    """Judge whether the transformed frame is truly transformed rather than averaged (0..1)."""

    frame: TransformedFrame = dspy.InputField()
    corners: list[Corner] = dspy.InputField()
    score: float = dspy.OutputField()
    rationale: str = dspy.OutputField()


# --- program -----------------------------------------------------------------

def make_view(distilled: DistilledSeed, selection: PredicateSelection, mode: CornerMode, hint: str = "") -> CornerView:
    return CornerView(
        normalized_seed=distilled.normalized_seed, stakes=distilled.stakes, constraints=distilled.constraints,
        unknowns=distilled.unknowns, hidden_assumptions=distilled.hidden_assumptions,
        primary_predicate=selection.primary.text, sub_predicates=[p.text for p in selection.sub_predicates],
        evaluation_criteria=distilled.evaluation_criteria, corner_contract=CORNER_CONTRACTS[mode],
        anti_collapse_hint=hint or ANTI_COLLAPSE_HINTS[mode],
    )


def seed_digest(seed: str) -> int:
    return int(hashlib.sha256(seed.encode("utf-8")).hexdigest()[:8], 16)


class TetraFrame(dspy.Module):
    """Distill → select predicate → four isolated corners → map → transform → verify."""

    def __init__(self, max_corner_attempts: int = 2, n_best: int = 3, transform_threshold: float = 0.84):
        super().__init__()
        from .tetraframe_metric import transform_reward

        self.distill = dspy.ChainOfThought(DistillSeed)
        self.select = dspy.ChainOfThought(SelectPredicate)
        self.corner_p = dspy.ChainOfThought(CornerP)
        self.corner_not_p = dspy.ChainOfThought(CornerNotP)
        self.corner_both = dspy.ChainOfThought(CornerBoth)
        self.corner_neither = dspy.ChainOfThought(CornerNeither)
        self.relate = dspy.ChainOfThought(RelateCorners)
        self.map = dspy.ChainOfThought(MapCorners)
        self.transform = dspy.BestOfN(module=dspy.ChainOfThought(TransformFrame), N=n_best,
                                      reward_fn=transform_reward, threshold=transform_threshold)
        self.max_corner_attempts = max_corner_attempts

    def _generator(self, mode: CornerMode):
        return {"P": self.corner_p, "not-P": self.corner_not_p, "both": self.corner_both,
                "neither": self.corner_neither}[mode]

    def _one_corner(self, mode: CornerMode, view: CornerView, rollout: int) -> Corner:
        from .tetraframe_metric import assert_isolation

        assert_isolation(view)
        base = self.corner_p.get_lm() or dspy.settings.lm
        with dspy.context(lm=base.copy(rollout_id=rollout, temperature=CORNER_TEMPERATURES[mode])):
            corner = self._generator(mode)(view=view).corner
        corner.mode = mode
        return corner

    def _corners(self, distilled: DistilledSeed, selection: PredicateSelection, retries: list[str]) -> dict[str, Corner]:
        from .tetraframe_metric import near_duplicates

        base_rollout = seed_digest(distilled.normalized_seed)
        corners = {m: self._one_corner(m, make_view(distilled, selection, m), base_rollout) for m in MODES}
        for attempt in range(1, self.max_corner_attempts):
            dupes = near_duplicates(corners, distilled.normalized_seed)
            if not dupes:
                break
            for left, right, sim in dupes:
                retries.append(f"attempt {attempt}: {left} ~ {right} (similarity {sim:.2f}); regenerated with stronger hints")
                for mode in (left, right):
                    hint = ANTI_COLLAPSE_HINTS[mode] + " Your previous draft duplicated another corner; diverge in substance."
                    corners[mode] = self._one_corner(mode, make_view(distilled, selection, mode, hint), base_rollout + attempt)
        return corners

    def forward(self, seed: str, context: str = "", on_stage=None) -> dspy.Prediction:
        """``on_stage(name, payload)`` is called after every completed stage so a caller can
        checkpoint; a stage that fails (timeout, parse error) then loses only itself."""
        from .tetraframe_metric import verify_run

        stage = on_stage or (lambda name, payload: None)
        retries: list[str] = []
        distilled = self.distill(seed=seed, context=context).distilled
        stage("distilled", distilled)
        selection = self.select(distilled=distilled).selection
        stage("selection", selection)
        corners = self._corners(distilled, selection, retries)
        stage("corners", corners)
        pairwise = []
        for a, b in (("P", "not-P"), ("P", "both"), ("P", "neither"), ("not-P", "both"), ("not-P", "neither"), ("both", "neither")):
            r = self.relate(source=corners[a], target=corners[b])
            pairwise.append(PairRelation(source=a, target=b, relation=r.relation, rationale=r.rationale,
                                         evidence_discriminator=r.evidence_discriminator, reversible=bool(r.reversible)))
        stage("pairwise", pairwise)
        cartography = self.map(corners=list(corners.values()), pairwise=pairwise).cartography
        cartography.pairwise = pairwise
        stage("cartography", cartography)
        frame = self.transform(primary_predicate=selection.primary.text, corners=list(corners.values()),
                               cartography=cartography, evaluation_criteria=distilled.evaluation_criteria).frame
        stage("transformed", frame)
        run = TetraFrameRun(seed=seed, distilled=distilled, selection=selection, corners=corners,
                            cartography=cartography, transformed=frame, retries=retries)
        run.verification = verify_run(run)
        return dspy.Prediction(run=run)
