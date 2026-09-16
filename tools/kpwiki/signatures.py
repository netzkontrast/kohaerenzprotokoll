"""Typed I/O contracts for the research-wiki loop.

Docstrings are the instructions DSPy renders; GEPA may rewrite them. Keep them
about the *what* (contract, hard rules) — never few-shot examples, never
prompt prose. Hard rules that must survive any optimization are also enforced
by ``metrics.py`` / ``compile_metric.py`` and the deterministic wiki lint, not
only by these texts.

Ingest (``SourceIngest``): ``TriageSource``, ``ExtractClaims``,
``CheckCanonConflict``, ``RaiseQuestions``.
Batch compile (``BatchCompile``): ``PlanConcepts`` (cluster the batch's claims
into concepts), ``MergeConcept`` (write one concept draft from its claims),
``DecideIngest`` (flag / update against an existing page), ``KnowledgeDiff``.
"""
from __future__ import annotations

import dspy

from .schema import (CanonConflict, Claim, ConceptDraft, ConceptPlan, Diff, IngestDecision, OpenQuestion,
                     PageState, Triage)


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
    without a verifiable citation must be dropped. Every citation carries a quote: a
    verbatim fragment copied from the cited numbered lines with the 'NNN| ' prefixes
    removed, never paraphrased and never translated.
    Write each claim in the language of the document it comes from: a German source
    gives German claims, an English source English ones; never translate a source.
    Quotation marks promise the source: any term the claim itself puts in quotation
    marks must stand verbatim in the lines that claim cites, so do not quote a term
    you have translated or reworded. Do not merge two statements into one claim.
    Prefer claims that name entities from the glossary."""

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


class PlanConcepts(dspy.Signature):
    """Cluster the cited claims of a whole source batch into concepts: one concept per
    merged idea, entity, rule, theory or motif across ALL sources. The same thing under
    different names (Kael / System Kael / Kael-System) is one concept, never two. When a
    concept page already exists, reuse its slug through existing_slug instead of creating
    a twin. A claim may belong to several concepts; leave a claim unassigned only when it
    is about nothing the batch names twice. Slugs are lowercase words joined by single
    hyphens, at most 60 characters, without umlauts (ae/oe/ue/ss)."""

    claims_digest: str = dspy.InputField(desc="numbered lines 'N. [source-slug] claim text — entities: …'")
    known_entities: list[str] = dspy.InputField(desc="codex slugs")
    existing_pages: list[str] = dspy.InputField(desc="'slug — title' of concept pages that already exist")
    plan: list[ConceptPlan] = dspy.OutputField()


class MergeConcept(dspy.Signature):
    """Write one concept draft from the claims planned for it. Definition sentences are
    engineering English, each backed by at least one citation whose quote is verbatim from
    the source; quotes are never translated. Where they disagree lists at least two
    distinct sources per disagreement, resolution pending unless one source explicitly
    supersedes the other. Quotation marks promise the source here too: a term a
    definition or agreement sentence puts in quotation marks must stand verbatim in
    the lines that sentence cites. codex_ref is a slug from known_entities and empty
    when none of them is the concept. Status is contradicted iff a disagreement is pending,
    single-source when only one source backs the concept, high-confidence when three or
    more sources agree, tentative otherwise. The timeline runs oldest to newest by
    index_date. Never emit the marker [K]; never invent story facts the claims lack."""

    title: str = dspy.InputField()
    kind_detail: str = dspy.InputField()
    claims: list[Claim] = dspy.InputField(desc="each claim's citation.file names its source")
    claim_sources: str = dspy.InputField(desc="'file → slug (index_date)' lines for the cited files")
    known_entities: list[str] = dspy.InputField(desc="codex slugs")
    draft: ConceptDraft = dspy.OutputField()


class DecideIngest(dspy.Signature):
    """RULE 1: a concept whose sources dispute the page → flag. RULE 1b: a reviewed page
    is authoritative; conflicting content is flagged, never applied. RULE 2: additions
    without dispute → update. List every conflict verbatim. Create is not a choice here:
    a missing page is created by the caller."""

    page: PageState = dspy.InputField()
    concept: ConceptDraft = dspy.InputField()
    decision: IngestDecision = dspy.OutputField()


class KnowledgeDiff(dspy.Signature):
    """What the batch changes for this page: reinforced (what the page already says and
    the sources confirm), challenged (only what conflicts with the page), new (only what
    the page lacks), gaps (what the sources leave open)."""

    page: PageState = dspy.InputField()
    concept: ConceptDraft = dspy.InputField()
    diff: Diff = dspy.OutputField()
