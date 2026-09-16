"""Render a ``BatchCompile`` result into candidate pages, edges and log lines.

Deterministic and LM-free: everything here is a projection of the ``Compiled``
object onto the page contract (``Wiki/SCHEMA.md``). Section names and field
lists come from ``Wiki/schema/entities.yaml`` through ``wiki_schema``, so a
contract change moves the pages with it instead of leaving this module behind.

What is written where (``Wiki/schema/writers.yaml`` → ``/research-ingest``):

* ``Wiki/candidates/<kind>/<partition>/<slug>.md`` — one page per extracted source (kind
  ``source``) and one per merged concept (kind ``concept``), both with
  ``status: draft``; a candidate declares its kind in the frontmatter.
* ``Wiki/graph/edges.jsonl`` — one ``supports`` edge per (source, concept)
  pair the concept actually cites, with that citation as its evidence.
* ``Wiki/log.md`` — one ``ingest`` line per written page and one ``claim``
  line per epistemic event of the knowledge diff.

The manifest, not the model, decides ``drive_id``, ``tier``, ``category`` and
``sha256``: those are deterministic (``scripts/source_inventory.py``,
``scripts/source_dedup.py``). A triage that disagrees is reported by
:func:`triage_disagreements` rather than silently overriding the manifest.

Nothing here promotes anything: ``/wiki-promote`` moves a reviewed candidate
into ``Wiki/sources/`` or ``Wiki/concepts/``.
"""
from __future__ import annotations

import datetime as dt
from typing import Any, Iterable

import yaml

from . import wiki_pages, wiki_schema
from .schema import Citation, Compiled, ConceptDraft, Extraction

WRITER = "/research-ingest"
INGEST_OP = "ingest"
CLAIM_OP = "claim"
EDGE_TYPE = "supports"
CANON_UNCHECKED = ("This pass did not retrieve Canon, so `canon_status` stays `unverified` (D-W12); "
                   "`/interrogate-canon` and the author decide the relation.")
NO_ENTRIES = "_none_"
CODEX_PREFIX = "codex:"
CLAIM_EVENTS = {"reinforced": "reinforced", "challenged": "challenged", "new": "created"}


def today() -> str:
    return dt.date.today().isoformat()


# --- small render helpers ---------------------------------------------------------


def marker(citation: Citation) -> str:
    """``^[file:start-end]`` exactly as ``entities.yaml → citation.pattern`` expects."""
    return f"^[{citation.file}:{citation.start_line}-{citation.end_line}]"


def markers(citations: Iterable[Citation]) -> str:
    return " ".join(marker(c) for c in citations)


def quoted(text: str) -> str:
    """German quotation marks; the lint checks the fragment against the cited lines."""
    return f"„{' '.join(text.split())}“"


def cited_line(text: str, citations: list[Citation], quote: str = "") -> str:
    parts = [quoted(quote)] if quote.strip() else []
    parts.append(text.strip())
    tail = markers(citations)
    return f"- {' — '.join(parts)}{' ' + tail if tail else ''}"


def section(title: str, lines: list[str]) -> str:
    body = "\n".join(lines) if lines else NO_ENTRIES
    return f"## {title}\n\n{body}\n"


def page_text(front: dict[str, Any], sections: list[str]) -> str:
    dumped = yaml.safe_dump(front, sort_keys=False, allow_unicode=True)
    return f"---\n{dumped}---\n\n" + "\n".join(sections)


def candidate_path(kind: str, slug: str, front: dict[str, Any]) -> str:
    partition = wiki_schema.partition_for(kind, front)
    return f"{wiki_pages.CANDIDATES_DIR}/{kind}s/{partition}/{slug}.md"


def _sections_of(kind: str) -> list[str]:
    return list(wiki_schema.kind(kind).get("sections", []))


def _initial_status() -> str:
    return wiki_schema.lifecycle()["initial"]


# --- source candidate --------------------------------------------------------------


def source_front(extraction: Extraction, record: dict[str, Any], ingested: str) -> dict[str, Any]:
    """Frontmatter of a source candidate; the manifest owns every deterministic field."""
    return {
        "title": record.get("title") or extraction.title,
        "kind": "source",
        "slug": extraction.source,
        "drive_id": record.get("drive_id", ""),
        "tier": record.get("tier", ""),
        "category": record.get("category", ""),
        "language": extraction.triage.language,
        "status": _initial_status(),
        "sha256": record.get("sha256", ""),
        "ingested": ingested,
        "truncated": bool(record.get("truncated", False)),
        "aliases": [],
        "tags": [],
    }


def source_body(extraction: Extraction, concept_slugs: list[str], ingested: str) -> str:
    """Summary, cited key claims, the concepts this source feeds, canon relation, log."""
    claims = [cited_line(c.text, [c.citation], c.citation.quote) for c in extraction.claims]
    entities = [f"- [[{slug}]]" for slug in concept_slugs]
    relation = [f"unknown — {CANON_UNCHECKED}"]
    log = [f"- {ingested} ingest by {WRITER}"]
    names = _sections_of("source")
    rendered = {"Summary": [extraction.triage.summary.strip()], "Key claims": claims,
                "Entities": entities, "Canon relation": relation, "Open questions": [], "Log": log}
    return "\n".join(section(name, rendered.get(name, [])) for name in names)


# --- concept candidate -------------------------------------------------------------


def codex_ref(value: str, known: frozenset[str]) -> str:
    """``codex:<slug>`` when the glossary has that entry, else nothing.

    A model that answers with the bare slug means the right thing, so the
    prefix is added; a slug the glossary does not carry is a guess, and
    ``codex:`` targets are terminal and never auto-created (``xref.yaml``).
    """
    slug = value.strip().removeprefix(CODEX_PREFIX)
    return f"{CODEX_PREFIX}{slug}" if slug and slug in known else ""


def concept_front(draft: ConceptDraft, ingested: str, codex_slugs: frozenset[str] = frozenset()) -> dict[str, Any]:
    summary = " ".join((draft.definition[0].text if draft.definition else draft.title).split())
    summary = " ".join(summary.split()[:40])
    front = {
        "title": draft.title,
        "kind": "concept",
        "slug": draft.slug,
        "kind_detail": draft.kind_detail,
        "status": _initial_status(),
        "confidence": draft.confidence,
        "sources": list(draft.sources),
        "canon_status": wiki_schema.kind("concept")["fields"]["canon_status"]["initial"],
        "table_status": draft.status,
        "disagreements": [d.topic for d in draft.disagreements],
        "aliases": [],
        "tags": [],
        "ingested": ingested,
        # Conservative routing defaults: a reviewer narrows these before promotion.
        "context_summary": summary,
        "context_scope": "global",
        "context_priority": "supporting",
        "chapter_start": 0,
        "chapter_end": 40,
        "spoiler_until": 40,
    }
    reference = codex_ref(draft.codex_ref, codex_slugs)
    if reference:
        front["codex_ref"] = reference
    return front


def _disagreement_lines(draft: ConceptDraft) -> list[str]:
    """One line per disagreement; a part the draft left empty is left out, not hinted at."""
    lines = []
    for item in draft.disagreements:
        parts = [item.topic, " vs ".join(f"[[{slug}]]" for slug in item.sources),
                 " · ".join(p for p in item.positions if p.strip()),
                 f"resolution: {item.resolution}"]
        line = " — ".join(part for part in parts if part.strip())
        lines.append(f"- {line} {markers(item.citations)}".rstrip())
    return lines


def concept_body(draft: ConceptDraft, ingested: str) -> str:
    definition = [f"{s.text.strip()} {markers(s.citations)}".strip() for s in draft.definition]
    agreements = [cited_line(a.text, a.citations) for a in draft.agreements]
    timeline = [f"- {t.date} — [[{t.source}]] — {t.what_changed}" for t in sorted(draft.timeline, key=lambda t: t.date)]
    names = _sections_of("concept")
    rendered = {
        "Definition": ["\n".join(definition)] if definition else [],
        "What Canon says": [CANON_UNCHECKED],
        "Where sources agree": agreements,
        "Where they disagree": _disagreement_lines(draft),
        "Timeline of the idea": timeline,
        "Open questions": [],
    }
    text = "\n".join(section(name, rendered.get(name, [])) for name in names)
    return text + f"\n<!-- drafted {ingested} by {WRITER}; promotion is a human step -->\n"


# --- the whole batch ----------------------------------------------------------------


def concepts_by_source(run: Compiled) -> dict[str, list[str]]:
    """Source slug → the concept slugs that list it, so the reverse link is written too."""
    mapping: dict[str, list[str]] = {}
    for draft in run.concepts:
        for slug in draft.sources:
            mapping.setdefault(slug, []).append(draft.slug)
    return mapping


def render_pages(run: Compiled, manifest: dict[str, dict[str, Any]], ingested: str | None = None,
                 codex_slugs: frozenset[str] = frozenset()) -> dict[str, str]:
    """Every candidate page of one batch as ``{repo-relative path: text}``."""
    stamp = ingested or today()
    feeds = concepts_by_source(run)
    pages = {}
    for extraction in run.extractions:
        record = manifest.get(extraction.source, {})
        front = source_front(extraction, record, stamp)
        body = source_body(extraction, sorted(feeds.get(extraction.source, [])), stamp)
        pages[candidate_path("source", extraction.source, front)] = page_text(front, [body])
    for draft in run.concepts:
        front = concept_front(draft, stamp, codex_slugs)
        pages[candidate_path("concept", draft.slug, front)] = page_text(front, [concept_body(draft, stamp)])
    return pages


def triage_disagreements(run: Compiled, manifest: dict[str, dict[str, Any]]) -> list[str]:
    """Where the model's triage differs from the deterministic manifest (manifest wins)."""
    notes = []
    for extraction in run.extractions:
        record = manifest.get(extraction.source, {})
        for field, value in (("tier", extraction.triage.tier), ("category", extraction.triage.category)):
            known = record.get(field)
            if known and known != value:
                notes.append(f"{extraction.source}: triage says {field}={value}, manifest says {known}")
    return notes


def edge_records(run: Compiled, at: str | None = None) -> list[dict[str, Any]]:
    """One ``supports`` edge per (source, concept) pair the concept cites, with its evidence."""
    stamp = at or today()
    by_file = {c.citation.file: e.source for e in run.extractions for c in e.claims}
    records = []
    for draft in run.concepts:
        seen: dict[str, Citation] = {}
        for citation in [c for s in draft.definition for c in s.citations] + \
                        [c for a in draft.agreements for c in a.citations] + \
                        [c for d in draft.disagreements for c in d.citations]:
            source = by_file.get(citation.file)
            if source and source not in seen:
                seen[source] = citation
        for source, citation in seen.items():
            records.append({"from": source, "to": draft.slug, "type": EDGE_TYPE,
                            "confidence": draft.confidence, "evidence": marker(citation),
                            "written_by": WRITER, "at": stamp})
    return records


def _log_line(date: str, op: str, title: str, **fields: str) -> str:
    """``## [date] op | title | k=v …`` — the grammar of ``conventions.yaml → log``."""
    tail = "".join(f" | {key}={value}" for key, value in fields.items() if value)
    return f"## [{date}] {op} | {' '.join(title.split())}{tail}"


def log_entries(run: Compiled, pages: dict[str, str], at: str | None = None) -> list[str]:
    """One ingest line per written page, one claim line per epistemic event of the diff."""
    stamp = at or today()
    titles = {draft.slug: draft.title for draft in run.concepts}
    titles.update({e.source: e.title for e in run.extractions})
    lines = []
    for path, text in sorted(pages.items()):
        slug = path.rsplit("/", 1)[-1][: -len(".md")]
        body = wiki_pages.split_frontmatter(text)[1]
        lines.append(_log_line(stamp, INGEST_OP, titles.get(slug, slug),
                               skill=WRITER, sha256=wiki_pages.body_sha256(body)))
    for slug, diff in sorted(run.diffs.items()):
        for field, event in CLAIM_EVENTS.items():
            for item in getattr(diff, field):
                lines.append(_log_line(stamp, CLAIM_OP, f"{slug} {event}: {item}", skill=WRITER))
    return lines


def knowledge_diff_report(run: Compiled, manifest: dict[str, dict[str, Any]]) -> list[str]:
    """What this batch would change, printed before anything is written."""
    lines = [f"sources extracted: {len(run.extractions)}"
             + (f" · skipped: {', '.join(run.skipped)}" if run.skipped else ""),
             f"claims: {sum(len(e.claims) for e in run.extractions)}"
             + (f" · unassigned: {len(run.unassigned_claims)}" if run.unassigned_claims else ""),
             f"concepts: {len(run.concepts)}"]
    for decision in sorted(run.decisions, key=lambda d: (d.action, d.slug)):
        conflicts = f" · conflicts: {'; '.join(decision.conflicts)}" if decision.conflicts else ""
        lines.append(f"  {decision.action:<6} {decision.slug} — {decision.rationale}{conflicts}")
    for slug, diff in sorted(run.diffs.items()):
        lines.append(f"  diff {slug}: " + " · ".join(
            f"{name} {len(getattr(diff, name))}" for name in ("reinforced", "challenged", "new", "gaps")))
    contradicted = [k.slug for k in run.concepts if k.status == "contradicted"]
    if contradicted:
        lines.append(f"contradicted (a disagreement is pending): {', '.join(contradicted)}")
    lines.extend(f"triage vs manifest — {note}" for note in triage_disagreements(run, manifest))
    return lines
