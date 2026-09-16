"""kpwiki programs — composed DSPy modules.

``SourceIngest`` is the first program of the ingest loop
(Plan/wiki concept §4, Phase B): triage → claims → canon-conflict check.
Retrieval of Canon passages is injected as a callable so the program stays
testable offline and independent of the search backend (BM25 first, graph
``match_codex_entries`` later).

``BatchCompile`` is the two-phase wiki compiler (Phase C, skill
``dspy-wiki-compile``): every source of a batch is triaged and extracted
before any concept is written; the batch's claims are then clustered into
concepts by one ``plan`` call and each concept is merged from its own claims
by one ``merge`` call; finally every concept is decided against the page the
wiki already holds (``create`` in code when there is none, ``flag`` /
``update`` by the LM otherwise) and a knowledge diff is produced. The program
returns drafts only — writing pages is the caller's reviewed step.

Bounded prompts: the clustering step sees a one-line digest per claim, not
the claims themselves; when a batch yields more than ``MAX_DIGEST_CLAIMS``
claims the digest is planned in consecutive slices of that size and the
slice plans are concatenated, plans with an equal slug being merged (union
of claim ids). Each ``merge`` call sees only the claims of its concept.
"""
from __future__ import annotations

import re
from typing import Callable, NamedTuple

import dspy
from pydantic import BaseModel, Field

from .schema import Claim, Compiled, ConceptDraft, ConceptPlan, Extraction, IngestDecision, PageState
from .signatures import (CheckCanonConflict, DecideIngest, ExtractClaims, KnowledgeDiff, MergeConcept,
                         PlanConcepts, TriageSource)

CanonRetriever = Callable[[list[Claim]], str]
BODY_PREVIEW_CHARS = 12000
MAX_DIGEST_CLAIMS = 1200
CREATE_RATIONALE = "no page yet"
FRONTMATTER_TITLE = re.compile(r"^title:\s*[\"']?(.*?)[\"']?\s*$", re.MULTILINE)


def number_lines(body: str) -> str:
    """Prefix every line with its 1-based number so citations are verifiable."""
    return "\n".join(f"{i:04d}| {line}" for i, line in enumerate(body.splitlines(), start=1))


def no_canon_retrieval(_claims: list[Claim]) -> str:
    """Retriever used in dry runs: nothing retrieved, so nothing can conflict."""
    return ""


class SourceIngest(dspy.Module):
    """Turn one source export into triage, cited claims and canon conflicts."""

    def __init__(self, retrieve_canon: CanonRetriever = no_canon_retrieval):
        super().__init__()
        self.triage = dspy.ChainOfThought(TriageSource)
        self.extract = dspy.Predict(ExtractClaims)
        self.conflicts = dspy.ChainOfThought(CheckCanonConflict)
        self.retrieve_canon = retrieve_canon

    def forward(self, source_file: str, title: str, category_hint: str,
                body: str, glossary_terms: str = "") -> dspy.Prediction:
        triage = self.triage(title=title, category_hint=category_hint,
                             body=body[:BODY_PREVIEW_CHARS]).triage
        claims = self.extract(source_file=source_file, numbered_body=number_lines(body),
                              glossary_terms=glossary_terms).claims
        passages = self.retrieve_canon(claims)
        conflicts = self.conflicts(claims=claims, canon_passages=passages).conflicts if passages else []
        return dspy.Prediction(triage=triage, claims=claims, conflicts=conflicts)


# --- BatchCompile -------------------------------------------------------------------


class SourceInput(BaseModel):
    """One manifest row plus its export body, as BatchCompile consumes it."""

    slug: str
    title: str
    category_hint: str = ""
    index_date: str = Field(default="", description="YYYY-MM-DD from the Drive index")
    source_file: str = Field(description="repo-relative export path, 'Sources/drive/<slug>.md'")
    body: str = ""
    truncated: bool = False


class ClaimRef(NamedTuple):
    """A claim with its global digest id and its position inside its extraction."""

    global_id: int
    source: str
    index: int
    claim: Claim


def index_claims(extractions: list[Extraction]) -> list[ClaimRef]:
    """Global 1-based ids over all extractions, in source order."""
    refs, next_id = [], 1
    for extraction in extractions:
        for index, claim in enumerate(extraction.claims):
            refs.append(ClaimRef(next_id, extraction.source, index, claim))
            next_id += 1
    return refs


def digest_line(ref: ClaimRef) -> str:
    """The one-line form of a claim the planner sees."""
    entities = ", ".join(ref.claim.entities) or "-"
    return f"{ref.global_id}. [{ref.source}] {ref.claim.text} — entities: {entities}"


def page_label(page: PageState) -> str:
    """'slug — title' for the planner; the title comes from the page frontmatter when present."""
    match = FRONTMATTER_TITLE.search(page.body)
    return f"{page.slug} — {match.group(1) if match and match.group(1) else page.slug}"


def merge_plans(plans: list[ConceptPlan]) -> list[ConceptPlan]:
    """Plans with an equal slug become one plan with the union of their claim ids."""
    merged: dict[str, ConceptPlan] = {}
    for plan in plans:
        seen = merged.get(plan.slug)
        if seen is None:
            merged[plan.slug] = plan.model_copy(update={"claim_ids": list(dict.fromkeys(plan.claim_ids))})
            continue
        ids = list(dict.fromkeys([*seen.claim_ids, *plan.claim_ids]))
        seen.claim_ids = ids
        if not seen.existing_slug:
            seen.existing_slug = plan.existing_slug
    return list(merged.values())


def _cited_files(draft: ConceptDraft) -> list[str]:
    citations = [c for s in draft.definition for c in s.citations]
    citations += [c for a in draft.agreements for c in a.citations]
    citations += [c for d in draft.disagreements for c in d.citations]
    return list(dict.fromkeys(c.file for c in citations))


class BatchCompile(dspy.Module):
    """Extract every source, cluster the batch's claims into concepts, merge, decide, diff."""

    def __init__(self, retrieve_canon: CanonRetriever = no_canon_retrieval):
        super().__init__()
        self.triage = dspy.ChainOfThought(TriageSource)
        self.extract = dspy.Predict(ExtractClaims)
        self.plan = dspy.ChainOfThought(PlanConcepts)
        self.merge = dspy.ChainOfThought(MergeConcept)
        self.decide = dspy.ChainOfThought(DecideIngest)
        self.diff = dspy.ChainOfThought(KnowledgeDiff)
        self.retrieve_canon = retrieve_canon

    def forward(self, sources: list[SourceInput], pages: dict[str, PageState],
                known_entities: list[str]) -> dspy.Prediction:
        extractions, skipped = self._extract_all(sources, known_entities)          # phase 1
        refs = index_claims(extractions)
        plans = self._plan_all(refs, pages, known_entities)                       # phase 2
        concepts, used = self._merge_all(plans, refs, sources, pages, known_entities)
        decisions, diffs = self._decide_all(concepts, pages)                      # phase 3
        unassigned = [f"{r.source}:{r.index}" for r in refs if r.global_id not in used]
        compiled = Compiled(extractions=extractions, concepts=concepts, decisions=decisions, diffs=diffs,
                            skipped=skipped, unassigned_claims=unassigned, plans=plans)
        return dspy.Prediction(compiled=compiled)

    def _extract_all(self, sources: list[SourceInput], known_entities: list[str]) -> tuple[list[Extraction], list[str]]:
        glossary = ", ".join(known_entities)
        extractions, skipped = [], []
        for src in sources:
            if src.truncated or not src.body.strip():
                skipped.append(src.slug)
                continue
            triage = self.triage(title=src.title, category_hint=src.category_hint,
                                 body=src.body[:BODY_PREVIEW_CHARS]).triage
            claims = self.extract(source_file=src.source_file, numbered_body=number_lines(src.body),
                                  glossary_terms=glossary).claims
            extractions.append(Extraction(source=src.slug, title=src.title, triage=triage, claims=list(claims or [])))
        return extractions, skipped

    def _plan_all(self, refs: list[ClaimRef], pages: dict[str, PageState], known_entities: list[str]) -> list[ConceptPlan]:
        existing = [page_label(p) for p in pages.values() if p.kind == "concept"]
        plans: list[ConceptPlan] = []
        for start in range(0, len(refs), MAX_DIGEST_CLAIMS):
            digest = "\n".join(digest_line(r) for r in refs[start:start + MAX_DIGEST_CLAIMS])
            plans.extend(self.plan(claims_digest=digest, known_entities=known_entities, existing_pages=existing).plan)
        return merge_plans(plans)

    def _merge_all(self, plans: list[ConceptPlan], refs: list[ClaimRef], sources: list[SourceInput],
                   pages: dict[str, PageState], known_entities: list[str]) -> tuple[list[ConceptDraft], set[int]]:
        by_id = {r.global_id: r for r in refs}
        file_to_source = {s.source_file: s for s in sources}
        concepts, used = [], set()
        for plan in plans:
            chosen = [by_id[i] for i in plan.claim_ids if i in by_id]   # unknown ids are dropped, scored by the metric
            if not chosen:
                continue
            used.update(r.global_id for r in chosen)
            concepts.append(self._merge_one(plan, chosen, file_to_source, pages, known_entities))
        return concepts, used

    def _merge_one(self, plan: ConceptPlan, chosen: list[ClaimRef], file_to_source: dict[str, SourceInput],
                   pages: dict[str, PageState], known_entities: list[str]) -> ConceptDraft:
        files = list(dict.fromkeys(r.claim.citation.file for r in chosen))
        lines = [f"{f} → {file_to_source[f].slug} ({file_to_source[f].index_date})" if f in file_to_source else f"{f} → ?"
                 for f in files]
        draft = self.merge(title=plan.title, kind_detail=plan.kind_detail, claims=[r.claim for r in chosen],
                           claim_sources="\n".join(lines), known_entities=known_entities).draft
        slug = plan.existing_slug if plan.existing_slug in pages else plan.slug
        sources = list(draft.sources) or self._cited_slugs(draft, file_to_source) or list(dict.fromkeys(r.source for r in chosen))
        return draft.model_copy(update={"slug": slug, "sources": sources})

    @staticmethod
    def _cited_slugs(draft: ConceptDraft, file_to_source: dict[str, SourceInput]) -> list[str]:
        return list(dict.fromkeys(file_to_source[f].slug for f in _cited_files(draft) if f in file_to_source))

    def _decide_all(self, concepts: list[ConceptDraft], pages: dict[str, PageState]):
        decisions, diffs = [], {}
        for concept in concepts:
            page = pages.get(concept.slug)
            if page is None:                                                      # create is a lookup, not a judgement
                decisions.append(IngestDecision(slug=concept.slug, action="create", rationale=CREATE_RATIONALE))
                continue
            decision = self.decide(page=page, concept=concept).decision
            decisions.append(decision.model_copy(update={"slug": concept.slug}))
            diffs[concept.slug] = self.diff(page=page, concept=concept).diff
        return decisions, diffs
