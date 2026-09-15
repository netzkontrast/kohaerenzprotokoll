"""Pydantic models shared by the kpwiki signatures, metrics and wiki lint.

These mirror the page contract in Wiki/SCHEMA.md (Plan/wiki concept §3). The
enums are closed on purpose: a program that cannot fit a value must fail
loudly (Rule 0) rather than invent a new category.
"""
from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field

# Where a source sits relative to the novel. T0/T1/T4 are set deterministically
# by the inventory (duplicates, superseded drafts, out of scope); the LLM only
# decides between T2 (external theory) and T3 (work-related).
SourceTier = Literal["T0-duplicate", "T1-superseded", "T2-theory", "T3-work", "T4-out-of-scope"]

# The Drive index sections, collapsed to a stable enum.
SourceCategory = Literal[
    "kernkonzept", "plot-outline", "charaktere", "worldbuilding", "storyform",
    "audit", "theorie-mathematik", "theorie-logik", "theorie-physik",
    "theorie-psychologie", "theorie-philosophie", "theorie-genre", "aegis", "unzugeordnet",
]

ClaimKind = Literal["fact", "rule", "definition", "plot", "character", "world", "theory", "decision", "question"]

# How a research claim relates to Canon/ (never a judgement about Canon itself).
CanonRelation = Literal["consistent", "extends", "contradicts", "unrelated", "unknown"]

Confidence = Literal["high", "medium", "low"]


class Citation(BaseModel):
    """Line-scoped pointer into a source export (``^[file:start-end]``)."""

    file: str = Field(description="repo-relative path of the source export")
    start_line: int = Field(ge=1)
    end_line: int = Field(ge=1)

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
