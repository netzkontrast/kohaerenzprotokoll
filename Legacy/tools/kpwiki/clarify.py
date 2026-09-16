"""Clarify gate — precision before a research claim changes authority.

Transposes the ``clarify`` code skill (Hmbown/clarify, Apache 2.0: reveal
intent, make the implicit explicit, add nothing, never change behaviour) to
statements. ``ClarifyGate`` returns the same claim with explicit scope (only
where the source states it), glossary bindings, labelled assumptions and every
remaining ambiguity as a question for the author — it never picks a reading.
``clarify_metric`` in ``clarify_metric.py`` is the "never change meaning" rule
as a deterministic metric. Concept: Plan/wiki/knowledge-system-concept §4 E.
"""
from __future__ import annotations

from typing import Literal

import dspy
from pydantic import BaseModel, Field

UNSPECIFIED = "unspecified"

# Scope axes of this novel. Values are free strings so the metric can check
# them against the source; the enum lives in the glossary, not here.
World = str      # KW1 … KW4, Überwelt, Externe Ebene, Kosmos-Meta, or "unspecified"
Act = str        # "Akt I" … "Akt III", or "unspecified"
Part = str       # an Anteil of System Kael, or "unspecified"

Verdict = Literal["clear", "needs-author", "not-promotable"]


class Ambiguity(BaseModel):
    phrase: str = Field(description="the ambiguous span, verbatim from the claim")
    readings: list[str] = Field(min_length=2, description="the distinct readings")
    question: str = Field(description="what the author must decide; ends with '?'")


class Binding(BaseModel):
    mention: str
    slug: str = Field(description="a codex slug from the glossary")


class Scope(BaseModel):
    world: World = UNSPECIFIED
    act: Act = UNSPECIFIED
    part: Part = UNSPECIFIED


class Clarification(BaseModel):
    clarified_text: str = Field(description="the claim, same language, same meaning, explicit")
    scope: Scope = Field(default_factory=Scope)
    assumptions: list[str] = Field(default_factory=list)
    ambiguities: list[Ambiguity] = Field(default_factory=list)
    bindings: list[Binding] = Field(default_factory=list)
    verdict: Verdict


class ClarifyClaim(dspy.Signature):
    """Rewrite the research claim so that a reader with the codex glossary understands
    exactly what it asserts about Kohärenz Protokoll, and nothing more: make the scope
    (Kernwelt, Akt, Anteil) explicit only where the cited source states it, bind names
    to glossary slugs, state implicit assumptions as assumptions, and turn every
    remaining ambiguity into a question for the author instead of choosing a reading.
    Canon context is for binding and conflict awareness, never for rewriting the claim.
    Never add, drop or generalise content; German stays German."""

    claim_text: str = dspy.InputField()
    source_excerpt: str = dspy.InputField(desc="the cited lines of the source export")
    entities: list[str] = dspy.InputField()
    glossary_terms: str = dspy.InputField(desc="comma-separated codex slugs")
    canon_context: str = dspy.InputField(desc="Canon passages about the same entities, or empty")
    clarification: Clarification = dspy.OutputField()


class ClarifyGate(dspy.Module):
    """One predictor; the caller decides what to do with the verdict."""

    def __init__(self):
        super().__init__()
        self.clarify = dspy.ChainOfThought(ClarifyClaim)

    def forward(self, claim_text: str, source_excerpt: str, entities: list[str],
                glossary_terms: str, canon_context: str = "") -> dspy.Prediction:
        out = self.clarify(claim_text=claim_text, source_excerpt=source_excerpt, entities=entities,
                           glossary_terms=glossary_terms, canon_context=canon_context)
        return dspy.Prediction(clarification=out.clarification)


def may_propose_promotion(clarification: Clarification) -> bool:
    """The only verdict that may enter /promote-to-canon."""
    return clarification.verdict == "clear" and not clarification.ambiguities
