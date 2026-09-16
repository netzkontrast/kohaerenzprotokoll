"""Deterministic metric for BatchCompile (GEPA-ready), plus its lint-side helpers.

Every axis is decidable without an LM, so the compiler cannot be optimized
into confident prose: a citation either resolves to its lines or it does not,
an update on a reviewed page with conflicts is illegal, a disagreement needs
two distinct sources, a ``new`` diff item must be absent from the page.

Axes and weights (``WEIGHTS``):
    citations       every Citation (claims, definition sentences, agreements,
                    disagreements) names a batch file, a range inside it and a
                    verbatim quote found in those lines; and every term a
                    claim or a cited sentence puts in quotation marks is in
                    the lines it cites — quotation marks promise the source
    decisions       ``decision_legal`` per concept (create iff no page; no
                    update on a protected page with conflicts)
    merge           per concept: sources inside the batch and distinct, at
                    least one citation, every definition sentence cited,
                    disagreements two-sourced and with a position per source,
                    status ⇔ pending disagreement,
                    slug shape, plan ids resolve; coverage of ``gold_concepts``
                    is folded in when the gold example names them
    diffs           ``diff_consistent`` per existing page
    links_language  claims keep the source language in either direction (a
                    German source is not summarised into English claims and an
                    English source is not turned into German ones), definition
                    sentences are English, no draft emits the marker [K]

``gold`` is a ``dspy.Example`` with ``sources: dict[file, body]``,
``pages: dict[slug, PageState]``, ``known_entities: list[str]`` and an
optional ``gold_concepts: list[str]`` (expected concept slugs). The helpers
``citation_resolves``, ``decision_legal``, ``diff_consistent`` and
``concept_problems`` are what the wiki lint reuses on written pages.
"""
from __future__ import annotations

import re

import dspy
from pydantic import ValidationError

from . import wiki_pages, wiki_schema
from .metrics import language_of, looks_german
from .schema import Citation, Compiled, ConceptDraft, ConceptPlan, Diff, Extraction, IngestDecision, PageState

WEIGHTS = {"citations": 0.30, "decisions": 0.25, "merge": 0.20, "diffs": 0.15, "links_language": 0.10}
CLEAN_FEEDBACK = "cited, legally decided, merged across sources, consistent diff"
FORBIDDEN_MARKER = "[K]"
QUOTE_PREVIEW_CHARS = 30
SENTENCE_PREVIEW_CHARS = 40
MIN_TOKEN_CHARS = 3
SOURCE_DIR = "Sources/drive"


def normalise(text: str) -> str:
    """Collapse all whitespace so a quote copied across a line break still matches."""
    return " ".join(text.split())


def _mean(values) -> float:
    values = list(values)
    return sum(values) / len(values) if values else 1.0


# --- helpers shared with the lint ------------------------------------------------------


def cited_span(citation: Citation, sources: dict[str, str]) -> str:
    """The cited lines as one whitespace-normalised string ('' when the range is unusable)."""
    lines = sources.get(citation.file, "").splitlines()
    if not lines or not 1 <= citation.start_line <= citation.end_line <= len(lines):
        return ""
    return normalise(" ".join(lines[citation.start_line - 1:citation.end_line]))


def unverifiable_quotes(text: str, citations: list[Citation], sources: dict[str, str]) -> list[str]:
    """Terms the text puts in quotation marks that the cited lines do not carry.

    The wiki lint applies the same rule to the written page (rule
    ``citation-resolves``); checking it here too means the program is told
    about it while it can still learn, not only after the page exists.
    """
    span = " ".join(cited_span(c, sources) for c in citations)
    if not span:
        return []
    return [fragment for fragment in wiki_pages.quoted_fragments(text)
            if normalise(fragment) not in span]


def citation_resolves(citation: Citation, sources: dict[str, str]) -> bool:
    """The file is in the batch, the range is inside it and the quote is in those lines."""
    quote = normalise(citation.quote)
    return bool(quote) and quote in cited_span(citation, sources)


def decision_legal(decision: IngestDecision, page: PageState | None) -> bool:
    """Create iff no page; a protected page with conflicts is flagged, never updated."""
    if page is None:
        return decision.action == "create"
    if decision.action == "create":
        return False
    protected = page.status in wiki_schema.protected_statuses()
    return not (decision.action == "update" and protected and decision.conflicts)


def _tokens(text: str) -> set[str]:
    return {w for w in re.findall(r"\w+", text.lower()) if len(w) >= MIN_TOKEN_CHARS}


def _overlap(a: str, b: str) -> bool:
    return bool(_tokens(a) & _tokens(b))


def diff_consistent(diff: Diff, decision: IngestDecision, prior_body: str) -> list[str]:
    """Challenged items must map to a conflict; new items must be absent from the page."""
    problems = [f"challenged item without a conflict: {item!r}" for item in diff.challenged
                if not any(_overlap(item, conflict) for conflict in decision.conflicts)]
    problems += [f"'new' item already on the page: {item!r}" for item in diff.new
                 if normalise(item).lower() in normalise(prior_body).lower()]
    return problems


def draft_citations(draft: ConceptDraft) -> list[Citation]:
    citations = [c for s in draft.definition for c in s.citations]
    citations += [c for a in draft.agreements for c in a.citations]
    citations += [c for d in draft.disagreements for c in d.citations]
    return citations


def draft_text(draft: ConceptDraft) -> str:
    parts = [draft.title, *(s.text for s in draft.definition), *(a.text for a in draft.agreements)]
    parts += [d.topic for d in draft.disagreements] + [p for d in draft.disagreements for p in d.positions]
    parts += [t.what_changed for t in draft.timeline]
    return "\n".join(parts)


def _concept_checks(draft: ConceptDraft, batch: set[str], plan: ConceptPlan | None,
                    n_claims: int) -> list[tuple[bool, list[str]]]:
    slug = draft.slug
    sources_ok = bool(draft.sources) and set(draft.sources) <= batch and len(draft.sources) == len(set(draft.sources))
    cited = bool(draft_citations(draft))
    uncited = [s.text for s in draft.definition if not s.citations]
    two_sourced = all(len(set(d.sources)) >= 2 for d in draft.disagreements)
    thin = [d.topic for d in draft.disagreements if len(d.positions) < len(set(d.sources))]
    pending = any(d.resolution == "pending" for d in draft.disagreements)
    status_ok = (draft.status == "contradicted") == pending
    slug_ok = bool(wiki_schema.slug_pattern().match(slug)) and len(slug) <= wiki_schema.conventions()["slug"]["max_length"]
    unknown_ids = [i for i in plan.claim_ids if not 1 <= i <= n_claims] if plan is not None else []
    return [
        (sources_ok and cited, [f"{slug}: sources outside the batch or no citation"]),
        (not uncited, [f"{slug}: definition sentence without citation: '{t[:SENTENCE_PREVIEW_CHARS]}'" for t in uncited]),
        (two_sourced, [f"{slug}: a disagreement needs two distinct sources"]),
        (not thin, [f"{slug}: a disagreement needs one position per source: {t[:SENTENCE_PREVIEW_CHARS]!r}"
                    for t in thin]),
        (status_ok, [f"{slug}: status {draft.status} does not match its pending disagreements"]),
        (slug_ok, [f"{slug}: slug does not match {wiki_schema.conventions()['slug']['pattern']}"]),
        (not unknown_ids, [f"{slug}: plan references unknown claim ids {unknown_ids}"]),
    ]


def concept_problems(draft: ConceptDraft, batch: set[str], plan: ConceptPlan | None = None,
                     n_claims: int = 0) -> list[str]:
    """The named deficits of one concept draft (empty when it satisfies the page rules)."""
    return [d for ok, deficits in _concept_checks(draft, batch, plan, n_claims) if not ok for d in deficits]


# --- axes -----------------------------------------------------------------------------


def _all_citations(run: Compiled) -> list[Citation]:
    return [c.citation for e in run.extractions for c in e.claims] + [c for k in run.concepts for c in draft_citations(k)]


def _quoting_texts(run: Compiled) -> list[tuple[str, str, list[Citation]]]:
    """``(where, text, citations)`` for every text that is rendered on a citing line."""
    texts = [(e.source, c.text, [c.citation]) for e in run.extractions for c in e.claims]
    for draft in run.concepts:
        texts += [(draft.slug, s.text, s.citations) for s in draft.definition]
        texts += [(draft.slug, a.text, a.citations) for a in draft.agreements]
    return texts


def _citation_axis(run: Compiled, sources: dict[str, str], deficits: list[str]) -> float:
    citations = _all_citations(run)
    bad = 0
    for c in citations:
        if not c.quote.strip():
            deficits.append(f"citation without quote: {c.file}:{c.start_line}-{c.end_line}")
        elif not citation_resolves(c, sources):
            deficits.append(f"citation does not resolve: {c.file}:{c.start_line}-{c.end_line} "
                            f"{c.quote[:QUOTE_PREVIEW_CHARS]!r}")
        else:
            continue
        bad += 1
    texts = _quoting_texts(run)
    for where, text, cites in texts:
        loose = unverifiable_quotes(text, cites, sources)
        if loose:
            bad += 1
            deficits.append(f"{where}: quoted term not in the cited lines: "
                            f"{loose[0][:QUOTE_PREVIEW_CHARS]!r}")
    total = len(citations) + len(texts)
    return 1.0 - bad / total if total else 0.0


def _decision_axis(run: Compiled, pages: dict[str, PageState], deficits: list[str]) -> float:
    scores = []
    decided = {d.slug for d in run.decisions}
    for d in run.decisions:
        page = pages.get(d.slug)
        ok = decision_legal(d, page)
        scores.append(1.0 if ok else 0.0)
        if not ok:
            deficits.append(f"illegal decision: {d.action} on {d.slug} "
                            f"(status {page.status if page else 'absent'}, conflicts {d.conflicts})")
    for k in run.concepts:
        if k.slug not in decided:
            scores.append(0.0)
            deficits.append(f"no decision for {k.slug}")
    return _mean(scores)


def _plan_for(concept: ConceptDraft, run: Compiled, pages: dict[str, PageState]) -> ConceptPlan | None:
    for plan in run.plans:
        target = plan.existing_slug if plan.existing_slug in pages else plan.slug
        if target == concept.slug:
            return plan
    return None


def _merge_axis(run: Compiled, gold: dspy.Example, pages: dict[str, PageState], deficits: list[str]) -> float:
    batch = {e.source for e in run.extractions}
    n_claims = sum(len(e.claims) for e in run.extractions)
    scores = []
    for k in run.concepts:
        checks = _concept_checks(k, batch, _plan_for(k, run, pages), n_claims)
        scores.append(_mean(1.0 if ok else 0.0 for ok, _ in checks))
        deficits.extend(d for ok, ds in checks if not ok for d in ds)
    quality = _mean(scores)
    if not run.concepts and n_claims:
        quality = 0.0
        deficits.append(f"no concepts merged although {n_claims} claims were extracted")
    expected = list(getattr(gold, "gold_concepts", None) or [])
    if not expected:
        return quality
    present = {k.slug for k in run.concepts}
    missing = [slug for slug in expected if slug not in present]
    if missing:
        deficits.append(f"expected concepts missing: {missing}")
    return (quality + 1.0 - len(missing) / len(expected)) / 2


def _diff_axis(run: Compiled, pages: dict[str, PageState], deficits: list[str]) -> float:
    decisions = {d.slug: d for d in run.decisions}
    scores = []
    for slug, diff in run.diffs.items():
        if slug not in decisions or slug not in pages:
            continue
        problems = diff_consistent(diff, decisions[slug], pages[slug].body)
        scores.append(0.0 if problems else 1.0)
        deficits.extend(f"{slug}: {p}" for p in problems)
    return _mean(scores)


def _source_body(extraction: Extraction, sources: dict[str, str]) -> str | None:
    body = sources.get(f"{SOURCE_DIR}/{extraction.source}.md")
    if body is not None:
        return body
    return next((sources[c.citation.file] for c in extraction.claims if c.citation.file in sources), None)


def claims_keep_language(claims, body: str) -> tuple[float, str]:
    """Share of claims still in the source's language; ``unknown`` texts never count against it."""
    source_language = language_of(body)
    if source_language == "unknown" or not claims:
        return 1.0, source_language
    kept = sum(language_of(c.text) in (source_language, "unknown") for c in claims)
    return kept / len(claims), source_language


def _links_language_axis(run: Compiled, sources: dict[str, str], deficits: list[str]) -> float:
    scores = []
    for e in run.extractions:
        body = _source_body(e, sources)
        if body is None or not e.claims:
            continue
        kept, source_language = claims_keep_language(e.claims, body)
        scores.append(kept)
        if kept < 1.0:
            deficits.append(f"{e.source}: claims left the source language ({source_language})")
    for k in run.concepts:
        english = all(not looks_german(s.text) for s in k.definition)
        marker_free = FORBIDDEN_MARKER not in draft_text(k)
        scores.append(_mean([1.0 if english else 0.0, 1.0 if marker_free else 0.0]))
        if not english:
            deficits.append(f"{k.slug}: definition sentence is not English")
        if not marker_free:
            deficits.append(f"{k.slug}: emits {FORBIDDEN_MARKER}")
    return _mean(scores)


# --- metric ---------------------------------------------------------------------------


def coerce_compiled(raw) -> Compiled | None:
    """The program's ``compiled`` output, or None when it is missing or malformed."""
    if isinstance(raw, Compiled):
        return raw
    try:
        return Compiled.model_validate(raw)
    except (ValidationError, TypeError, ValueError):
        return None


def _pages(gold: dspy.Example) -> dict[str, PageState]:
    raw = getattr(gold, "pages", None) or {}
    return {slug: page if isinstance(page, PageState) else PageState.model_validate(page) for slug, page in raw.items()}


def compile_metric(gold: dspy.Example, pred: dspy.Prediction, trace=None,
                   pred_name=None, pred_trace=None) -> dspy.Prediction:
    """Rich-feedback metric for BatchCompile: every axis deterministic, every deficit named."""
    run = coerce_compiled(getattr(pred, "compiled", None))
    if run is None:
        return dspy.Prediction(score=0.0, feedback="prediction carries no Compiled result")
    pages, sources = _pages(gold), dict(getattr(gold, "sources", None) or {})
    deficits: list[str] = []
    axes = {
        "citations": _citation_axis(run, sources, deficits),
        "decisions": _decision_axis(run, pages, deficits),
        "merge": _merge_axis(run, gold, pages, deficits),
        "diffs": _diff_axis(run, pages, deficits),
        "links_language": _links_language_axis(run, sources, deficits),
    }
    score = round(sum(WEIGHTS[axis] * value for axis, value in axes.items()), 3)
    return dspy.Prediction(score=score, feedback="; ".join(deficits) or CLEAN_FEEDBACK)
