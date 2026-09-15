"""Deterministic metric for the clarify gate (GEPA-ready).

Axes: meaning kept (no smuggled glossary terms, no dropped entities, no new
quantifiers), scope grounded in the source, hedges resolved or declared,
bindings to known slugs, questions well-formed with a consistent verdict,
language kept. Lexical on purpose: the gate cannot be optimized into
"sounding precise" — a rewrite that adds a Kernwelt or an *immer* the source
lacks scores below the vague original.
"""
from __future__ import annotations

import dspy

from .clarify import UNSPECIFIED, Clarification
from .metrics import looks_german

HEDGES = ("irgendwie", "meist", "meistens", "wohl", "vielleicht", "ungefähr", "manchmal",
          "eigentlich", "gewissermaßen", "somehow", "probably", "maybe", "roughly", "sometimes")
QUANTIFIERS = ("alle", "jede", "jeder", "jedes", "immer", "nie", "niemals", "kein", "keine", "nur",
               "all", "every", "always", "never", "only")
WEIGHTS = {"meaning": 0.30, "scope": 0.15, "hedges": 0.15, "bindings": 0.15, "questions": 0.15, "language": 0.10}
ENGLISH_FUNCTION_WORDS = (" the ", " and ", " is ", " not ")


def _present(text: str, markers: tuple[str, ...]) -> set[str]:
    padded = f" {text.lower()} "
    return {m for m in markers if f" {m} " in padded}


def _count(text: str, markers: tuple[str, ...]) -> int:
    padded = f" {text.lower()} "
    return sum(padded.count(f" {m} ") for m in markers)


def _meaning(c: Clarification, gold, context: str, glossary: list[str]) -> tuple[float, list[str]]:
    out = c.clarified_text.lower()
    new_terms = [g for g in glossary if g.lower() in out and g.lower() not in context.lower()]
    bound = {b.mention.lower() for b in c.bindings}
    dropped = [e for e in gold.entities if e.lower() not in out and e.lower() not in bound]
    new_quant = sorted(_present(c.clarified_text, QUANTIFIERS) - _present(context, QUANTIFIERS))
    score = 1.0 - min(1.0, 0.5 * (len(new_terms) + len(dropped) + len(new_quant)))
    parts = []
    if new_terms:
        parts.append(f"Introduced terms absent from the source: {new_terms}.")
    if dropped:
        parts.append(f"Dropped entities: {dropped}.")
    if new_quant:
        parts.append(f"Added quantifiers the source does not state: {new_quant}.")
    return score, parts


def _scope(c: Clarification, context: str) -> tuple[float, list[str]]:
    values = (c.scope.world, c.scope.act, c.scope.part)
    ungrounded = [v for v in values if v != UNSPECIFIED and v.lower() not in context.lower()]
    return (0.0 if ungrounded else 1.0,
            [f"Scope values not found in the source: {ungrounded}; use 'unspecified'."] if ungrounded else [])


def _hedges(c: Clarification, original: str) -> tuple[float, list[str]]:
    declared = {a.phrase.lower() for a in c.ambiguities}
    undeclared = [h for h in _present(c.clarified_text, HEDGES) if not any(h in d for d in declared)]
    increased = _count(c.clarified_text, HEDGES) > _count(original, HEDGES)
    parts = []
    if undeclared:
        parts.append(f"Hedges left unresolved and undeclared: {undeclared}; ground them in the source or list them as ambiguities.")
    if increased:
        parts.append("The rewrite is vaguer than the original.")
    return (0.0 if parts else 1.0), parts


def _bindings(c: Clarification, glossary: list[str]) -> tuple[float, list[str]]:
    bad = [b.slug for b in c.bindings if b.slug not in glossary]
    return (0.0 if bad else 1.0), ([f"Bindings to unknown glossary slugs: {bad}."] if bad else [])


def _questions(c: Clarification) -> tuple[float, list[str]]:
    malformed = [a.phrase for a in c.ambiguities if not a.question.strip().endswith("?")]
    consistent = (c.verdict != "clear") == bool(c.ambiguities)
    parts = []
    if malformed:
        parts.append(f"Ambiguities without a question: {malformed}.")
    if not consistent:
        parts.append("Verdict inconsistent with the ambiguity list ('clear' needs an empty list).")
    return (0.0 if parts else 1.0), parts


def _language(c: Clarification, original: str) -> tuple[float, list[str]]:
    padded = f" {c.clarified_text.lower()} "
    translated = looks_german(original) and any(w in padded for w in ENGLISH_FUNCTION_WORDS)
    return (0.0 if translated else 1.0), (["The claim was translated; keep the source language."] if translated else [])


def clarify_metric(gold: dspy.Example, pred: dspy.Prediction, trace=None,
                   pred_name=None, pred_trace=None) -> dspy.Prediction:
    """Score a Clarification against its claim, source excerpt, glossary and context."""
    c = getattr(pred, "clarification", None)
    if not isinstance(c, Clarification):
        return dspy.Prediction(score=0.0, feedback="No well-formed Clarification was produced.")
    context = " ".join([gold.claim_text, gold.source_excerpt, getattr(gold, "canon_context", "") or ""])
    glossary = [g.strip() for g in gold.glossary_terms.split(",") if g.strip()]
    axes = {
        "meaning": _meaning(c, gold, context, glossary),
        "scope": _scope(c, context),
        "hedges": _hedges(c, gold.claim_text),
        "bindings": _bindings(c, glossary),
        "questions": _questions(c),
        "language": _language(c, gold.claim_text),
    }
    score = sum(WEIGHTS[k] * v[0] for k, v in axes.items())
    feedback = " ".join(p for _, parts in axes.values() for p in parts)
    return dspy.Prediction(score=score, feedback=feedback or "Clarified without adding or losing meaning.")
