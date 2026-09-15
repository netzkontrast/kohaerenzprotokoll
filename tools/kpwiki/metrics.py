"""Metrics for kpwiki programs — deterministic where possible, rich feedback always.

The metric is the safety rail that survives optimization: GEPA can rewrite a
Signature's instructions, but it cannot change what these functions reward.
Every metric returns ``dspy.Prediction(score=..., feedback=...)`` (never a
dict — dspy.Evaluate's aggregator sums scores, see dspy-evaluation-harness).

Axes for ``ingest_metric``:
    citation_validity  every claim cites an existing line range of the source
    quote_grounding    a claim's text (or a long fragment of it) occurs in the cited lines
    schema_validity    the prediction parsed into the closed Pydantic enums
    language_kept      German source text was not translated into English claims
    coverage           expected gold claims are recovered (when gold is given)
"""
from __future__ import annotations

import dspy
from pydantic import ValidationError

from .schema import Claim

WEIGHTS = {
    "citation_validity": 0.35,
    "quote_grounding": 0.25,
    "schema_validity": 0.15,
    "language_kept": 0.10,
    "coverage": 0.15,
}
MIN_GROUNDING_FRAGMENT = 20
GERMAN_MARKERS = (" der ", " die ", " das ", " und ", " nicht ", " ist ", "ä", "ö", "ü", "ß")
ENGLISH_MARKERS = (" the ", " and ", " is ", " not ", " of ")


def citation_ok(claim: Claim, source_lines: list[str], source_file: str) -> bool:
    """A citation is valid when it names this file and a range inside it."""
    c = claim.citation
    return (c.file == source_file and c.start_line <= c.end_line
            and 1 <= c.start_line and c.end_line <= len(source_lines))


def grounded(claim: Claim, source_lines: list[str]) -> bool:
    """The claim text, or any 20-char fragment of it, appears in the cited lines."""
    c = claim.citation
    span = " ".join(source_lines[c.start_line - 1:c.end_line]).lower()
    text = claim.text.lower().strip()
    if not text or not span:
        return False
    if text in span:
        return True
    fragments = (text[i:i + MIN_GROUNDING_FRAGMENT] for i in range(0, max(1, len(text) - MIN_GROUNDING_FRAGMENT + 1)))
    return any(fragment in span for fragment in fragments)


def _marker_counts(text: str) -> tuple[int, int]:
    padded = f" {text.lower()} "
    return (sum(padded.count(m) for m in GERMAN_MARKERS),
            sum(padded.count(m) for m in ENGLISH_MARKERS))


def looks_german(text: str) -> bool:
    """True only with at least one German marker and no English majority."""
    german, english = _marker_counts(text)
    return german > 0 and german >= english


def language_unknown(text: str) -> bool:
    """No marker of either language (names, numbers, formulas): never penalised."""
    return _marker_counts(text) == (0, 0)


def language_kept(claims: list[Claim], source_is_german: bool) -> float:
    """Share of claims still German (or language-neutral) when the source is German."""
    if not source_is_german or not claims:
        return 1.0
    return sum(looks_german(c.text) or language_unknown(c.text) for c in claims) / len(claims)


def coverage(claims: list[Claim], gold_fragments: list[str]) -> float:
    """Share of gold fragments that some predicted claim contains (1.0 without gold)."""
    if not gold_fragments:
        return 1.0
    texts = [c.text.lower() for c in claims]
    hits = sum(any(frag.lower() in t for t in texts) for frag in gold_fragments)
    return hits / len(gold_fragments)


def coerce_claims(raw: list) -> tuple[list[Claim], int]:
    """Keep well-formed claims; count the malformed ones instead of raising."""
    claims, malformed = [], 0
    for item in raw:
        if isinstance(item, Claim):
            claims.append(item)
            continue
        try:
            claims.append(Claim.model_validate(item))
        except (ValidationError, TypeError, ValueError):
            malformed += 1
    return claims, malformed


def _axis_scores(gold: dspy.Example, claims: list[Claim], malformed: int) -> dict[str, float]:
    source_lines = gold.body.splitlines()
    n = len(claims)
    total = n + malformed
    valid = [c for c in claims if citation_ok(c, source_lines, gold.source_file)]
    return {
        "citation_validity": len(valid) / n if n else 0.0,
        "quote_grounding": sum(grounded(c, source_lines) for c in valid) / n if n else 0.0,
        "schema_validity": n / total if total else 0.0,
        "language_kept": language_kept(claims, looks_german(gold.body)),
        "coverage": coverage(claims, list(getattr(gold, "gold_fragments", []) or [])),
    }


def _feedback(scores: dict[str, float], n_claims: int) -> str:
    parts = []
    if n_claims == 0:
        parts.append("No claims were extracted; the source has citable statements.")
    if scores["schema_validity"] < 1.0:
        parts.append("Some claims did not fit the Claim schema (kind enum, citation fields); emit only well-formed claims.")
    if scores["citation_validity"] < 1.0:
        parts.append("Some citations point outside the numbered body or to another file; cite only 'NNN|' lines of this source.")
    if scores["quote_grounding"] < 1.0:
        parts.append("Some claims are not found in their cited lines; quote or closely paraphrase the cited text.")
    if scores["language_kept"] < 1.0:
        parts.append("German source text was translated; keep claims in the source language.")
    if scores["coverage"] < 1.0:
        parts.append("Expected statements were missed; extract every atomic claim, do not summarise.")
    return " ".join(parts) or "All claims are cited, grounded, schema-valid and in the source language."


def ingest_metric(gold: dspy.Example, pred: dspy.Prediction, trace=None,
                  pred_name=None, pred_trace=None) -> dspy.Prediction:
    """Rich-feedback metric for SourceIngest (GEPA-ready)."""
    claims, malformed = coerce_claims(list(getattr(pred, "claims", []) or []))
    scores = _axis_scores(gold, claims, malformed)
    score = sum(WEIGHTS[k] * v for k, v in scores.items())
    return dspy.Prediction(score=score, feedback=_feedback(scores, len(claims) + malformed))
