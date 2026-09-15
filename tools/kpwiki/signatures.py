"""Typed I/O contracts for the research-wiki loop.

Docstrings are the instructions DSPy renders; GEPA may rewrite them. Keep them
about the *what* (contract, hard rules) — never few-shot examples, never
prompt prose. Hard rules that must survive any optimization are also enforced
by ``metrics.py`` and the deterministic wiki lint, not only by these texts.
"""
from __future__ import annotations

import dspy

from .schema import CanonConflict, Claim, OpenQuestion, Triage


class TriageSource(dspy.Signature):
    """Classify one Google-Drive research document for the Kohärenz Protokoll wiki.
    Decide only tier T2-theory vs T3-work (T0/T1/T4 are assigned by the inventory),
    the category, the language, and a short engineering-English summary.
    Never invent story facts; the summary describes the document, not the novel."""

    title: str = dspy.InputField()
    category_hint: str = dspy.InputField(desc="section of the Drive index the document was listed under")
    body: str = dspy.InputField(desc="markdown export of the document, possibly truncated")
    triage: Triage = dspy.OutputField()


class ExtractClaims(dspy.Signature):
    """Extract the atomic claims a research document makes about the novel or its theory.
    Every claim carries a line-scoped citation into the given numbered body; a claim
    without a verifiable citation must be dropped. Quote German in German. Do not merge
    two statements into one claim. Prefer claims that name entities from the glossary."""

    source_file: str = dspy.InputField(desc="repo-relative path used in citations")
    numbered_body: str = dspy.InputField(desc="body with 'NNN| ' line prefixes")
    glossary_terms: str = dspy.InputField(desc="comma-separated codex slugs/names known to the project")
    claims: list[Claim] = dspy.OutputField()


class CheckCanonConflict(dspy.Signature):
    """Compare research claims against retrieved Canon passages. Report only real
    disagreements about the same entity, rule or event; different Kernwelten having
    different logic regimes is not a conflict, and Storyform A/B differing is by design.
    Canon is normative — describe the disagreement, never propose to change Canon here."""

    claims: list[Claim] = dspy.InputField()
    canon_passages: str = dspy.InputField(desc="retrieved Canon excerpts with file paths")
    conflicts: list[CanonConflict] = dspy.OutputField()


class RaiseQuestions(dspy.Signature):
    """From a concept's merged research claims and its Canon status, formulate the
    questions we should ask about our own understanding, along three axes:
    incompleteness (research assumes what Canon does not say), incorrectness
    (research and Canon disagree), redundancy (overlapping or duplicated concepts).
    Questions are for the author to decide, not for the model to answer."""

    concept: str = dspy.InputField()
    merged_claims: str = dspy.InputField()
    canon_status: str = dspy.InputField(desc="what Canon/ currently says, with file references, or 'absent'")
    questions: list[OpenQuestion] = dspy.OutputField()
