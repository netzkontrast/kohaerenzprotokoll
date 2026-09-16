"""Pydantic models shared by the kpwiki signatures, metrics and wiki lint.

The page-level enums are built from ``Wiki/schema/entities.yaml`` at import
time (Wiki/SCHEMA.md, Plan/wiki concept §3.2), so the YAML stays the single
source of truth and nothing here can drift from it. ``ClaimKind`` is a
claim-level enum of the extraction step and has no page field. The enums are
closed on purpose: a program that cannot fit a value must fail loudly
(Rule 0) rather than invent a new category.
"""
from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field, model_validator

from . import wiki_schema

# Where a source sits relative to the novel. T0/T1/T4 are set deterministically
# by the inventory (duplicates, superseded drafts, out of scope); the LLM only
# decides between T2 (external theory) and T3 (work-related).
SourceTier = Literal[tuple(wiki_schema.enum_values("tier"))]

# The Drive index sections, collapsed to a stable enum.
SourceCategory = Literal[tuple(wiki_schema.enum_values("category"))]

ClaimKind = Literal["fact", "rule", "definition", "plot", "character", "world", "theory", "decision", "question"]

# How a research claim relates to Canon/ (never a judgement about Canon itself).
CanonRelation = Literal[tuple(wiki_schema.enum_values("canon_relation"))]

Confidence = Literal[tuple(wiki_schema.enum_values("confidence"))]


class Citation(BaseModel):
    """Line-scoped pointer into a source export (``^[file:start-end]``)."""

    file: str = Field(description="repo-relative path of the source export")
    start_line: int = Field(ge=1)
    end_line: int = Field(ge=1)

    @model_validator(mode="after")
    def _ordered(self) -> "Citation":
        if self.end_line < self.start_line:
            raise ValueError(f"inverted line range {self.start_line}-{self.end_line}")
        return self

    def marker(self) -> str:
        return f"^[{self.file}:{self.start_line}-{self.end_line}]"


class Claim(BaseModel):
    """One atomic statement lifted from a source, in the source's language."""

    text: str = Field(description="the claim, quoted or closely paraphrased in the source language")
    kind: ClaimKind
    citation: Citation
    entities: list[str] = Field(default_factory=list, description="names/terms the claim is about")
    canon_relation: CanonRelation = "unknown"
    confidence: Confidence = "medium"


class Triage(BaseModel):
    """Result of looking at a source once: what it is and whether it matters."""

    tier: SourceTier
    category: SourceCategory
    language: Literal["de", "en", "mixed"]
    summary: str = Field(description="2-4 sentences, engineering English, no new lore")
    supersedes_hint: str = Field(default="", description="title of an older version this replaces, if evident")


class CanonConflict(BaseModel):
    """A research claim that disagrees with a Canon passage."""

    claim_text: str
    canon_file: str
    canon_excerpt: str = Field(description="verbatim Canon passage (German stays German)")
    explanation: str = Field(description="why they conflict, English, one or two sentences")
    severity: Literal["critical", "major", "minor"]


class OpenQuestion(BaseModel):
    """A question the research raises about our understanding of the novel."""

    question: str
    axis: Literal["incompleteness", "incorrectness", "redundancy"]
    evidence: list[str] = Field(default_factory=list, description="citation markers")
    suggested_owner: Literal["author", "session", "graph"] = "author"
