"""Pydantic models shared by the kpwiki signatures, metrics and wiki lint.

The page-level enums are built from ``Wiki/schema/entities.yaml`` at import
time (Wiki/SCHEMA.md, Plan/wiki concept §3.2), so the YAML stays the single
source of truth and nothing here can drift from it. ``ClaimKind`` is a
claim-level enum of the extraction step and has no page field. The enums are
closed on purpose: a program that cannot fit a value must fail loudly
(Rule 0) rather than invent a new category.

Two families of models live here:

* the ingest models (``Citation``, ``Claim``, ``Triage``, ``CanonConflict``,
  ``OpenQuestion``) used by ``SourceIngest``;
* the batch-compile models (``Extraction`` … ``Compiled``) used by
  ``BatchCompile`` (programs.py) and ``compile_metric`` (compile_metric.py).
  They mirror the concept page contract (``kinds.concept`` in entities.yaml):
  a definition made of cited sentences, agreements, two-sourced
  disagreements with a resolution, a dated timeline. Validators stay minimal
  (line order, slug shape); every other page rule is scored by the metric so
  an optimizer receives feedback instead of a crash.
"""
from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field, field_validator, model_validator

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

# Concept page enums (kinds.concept in entities.yaml).
KindDetail = Literal[tuple(wiki_schema.enum_values("kind_detail"))]
ConceptTableStatus = Literal[tuple(wiki_schema.enum_values("concept_table_status"))]

# How a disagreement between sources stands; ``pending`` forces status ``contradicted``.
Resolution = Literal["pending", "supersedes", "both-valid"]

# The three ingest outcomes (synthadoc rules 1 / 1b / 2 / 3); ``create`` is decided in code.
IngestAction = Literal["flag", "update", "create"]

QUOTE_MAX_CHARS = 200


class Citation(BaseModel):
    """Line-scoped pointer into a source export (``^[file:start-end]``)."""

    file: str = Field(description="repo-relative path of the source export")
    start_line: int = Field(ge=1)
    end_line: int = Field(ge=1)
    quote: str = Field(default="", description="verbatim fragment (≤ 200 chars) copied from the cited lines")

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


# --- batch compile (two-phase: extract every source, then merge concepts) ------------


class Extraction(BaseModel):
    """Phase-1 result for one source: its triage and every cited claim."""

    source: str = Field(description="manifest slug of the source")
    title: str
    triage: Triage
    claims: list[Claim] = Field(default_factory=list)


class DefinitionSentence(BaseModel):
    """One English sentence of a concept definition with the lines that back it."""

    text: str = Field(description="one English sentence")
    citations: list[Citation] = Field(default_factory=list, description="at least one, quote verbatim")


class CitedStatement(BaseModel):
    """A statement the sources agree on, with its citations."""

    text: str
    citations: list[Citation] = Field(default_factory=list)


class Disagreement(BaseModel):
    """Two or more sources taking different positions on one topic."""

    topic: str
    sources: list[str] = Field(default_factory=list, description="at least two distinct source slugs")
    positions: list[str] = Field(default_factory=list, description="one position per source, same order")
    citations: list[Citation] = Field(default_factory=list)
    resolution: Resolution = "pending"


class TimelineEntry(BaseModel):
    """How the understanding moved with one source, dated by its index_date."""

    date: str = Field(description="YYYY-MM-DD index_date of the source")
    source: str = Field(description="source slug")
    what_changed: str


def _check_slug(value: str) -> str:
    rules = wiki_schema.conventions()["slug"]
    if not wiki_schema.slug_pattern().match(value) or len(value) > rules["max_length"]:
        raise ValueError(f"slug {value!r} must match {rules['pattern']} and be at most {rules['max_length']} chars")
    return value


class ConceptDraft(BaseModel):
    """A concept page in draft form: one merged idea across the batch's sources."""

    slug: str
    title: str
    kind_detail: KindDetail
    definition: list[DefinitionSentence] = Field(default_factory=list)
    agreements: list[CitedStatement] = Field(default_factory=list)
    disagreements: list[Disagreement] = Field(default_factory=list)
    timeline: list[TimelineEntry] = Field(default_factory=list)
    sources: list[str] = Field(default_factory=list, description="distinct source slugs the draft cites")
    entities: list[str] = Field(default_factory=list)
    codex_ref: str = ""
    confidence: Confidence
    status: ConceptTableStatus

    @field_validator("slug")
    @classmethod
    def _slug_shape(cls, value: str) -> str:
        return _check_slug(value)


class ConceptPlan(BaseModel):
    """Clustering output: which claims (global 1-based digest ids) form one concept."""

    slug: str
    title: str
    kind_detail: KindDetail
    claim_ids: list[int] = Field(default_factory=list)
    existing_slug: str = Field(default="", description="slug of an existing concept page this merges into")


class PageState(BaseModel):
    """What the wiki currently holds under a slug."""

    slug: str
    kind: str
    status: str
    body: str


class IngestDecision(BaseModel):
    """flag / update / create for one concept against its existing page."""

    slug: str
    action: IngestAction
    rationale: str
    conflicts: list[str] = Field(default_factory=list, description="every conflict with the page, verbatim")


class Diff(BaseModel):
    """What the batch changes for one page (quicky-wiki knowledge diff)."""

    reinforced: list[str] = Field(default_factory=list)
    challenged: list[str] = Field(default_factory=list)
    new: list[str] = Field(default_factory=list)
    gaps: list[str] = Field(default_factory=list)


class Compiled(BaseModel):
    """Everything BatchCompile returns; writing pages is the caller's reviewed step."""

    extractions: list[Extraction] = Field(default_factory=list)
    concepts: list[ConceptDraft] = Field(default_factory=list)
    decisions: list[IngestDecision] = Field(default_factory=list)
    diffs: dict[str, Diff] = Field(default_factory=dict)
    skipped: list[str] = Field(default_factory=list, description="slugs of truncated or empty sources")
    unassigned_claims: list[str] = Field(default_factory=list, description="'slug:index' of claims no concept used")
    plans: list[ConceptPlan] = Field(default_factory=list, description="the clustering step's output, for the metric")
