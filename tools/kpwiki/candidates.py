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
import re
from typing import Any, Iterable

import yaml

from . import wiki_pages, wiki_schema
from .schema import Citation, Compiled, ConceptDraft, Disagreement, Extraction

WRITER = "/research-ingest"
PENDING = "pending"
QUESTION_ANSWERS = (
    "The positions above are what the sources say, not candidate answers. Four corners "
    "come from `/tetraframe`, which this ingest never runs and never decides; the author "
    "does, and a supersession needs a D-xx."
)
LEDGER_USE = (
    "Read at the next reconcile: a subject's claims are checked against what is "
    "recorded here before a merge runs, so a known clash is recognised rather than "
    "rediscovered. Evidence, never a verdict — deciding which side is right is "
    "`/tetraframe` and a D-xx, and the author's call."
)
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


def disagreement_entry(draft: ConceptDraft, item: Disagreement, seen: str,
                       question_slug: str = "") -> list[str]:
    """One ledger entry: the topic, then every position with its source and citation.

    Positions are kept beside their sources rather than flattened into one line,
    because the ledger's whole job is to say who claimed what. A part the draft
    left empty is left out rather than hinted at.
    """
    lines = [f"### {item.topic}\n"]
    trail = f"- first seen {seen} · concept [[{draft.slug}]]"
    if question_slug:
        trail += f" · question [[{question_slug}]]"
    if item.resolution and item.resolution != PENDING:
        trail += f" · resolution: {item.resolution}"
    lines.append(trail)
    for index, source in enumerate(item.sources):
        position = item.positions[index] if index < len(item.positions) else ""
        cited = [c for c in item.citations if c.file.endswith(f"{source}.md")]
        lines.append(f"- [[{source}]] — {position} {markers(cited)}".rstrip())
    return lines + [""]


def concept_body(draft: ConceptDraft, ingested: str) -> str:
    definition = [f"{s.text.strip()} {markers(s.citations)}".strip() for s in draft.definition]
    agreements = [cited_line(a.text, a.citations) for a in draft.agreements]
    timeline = [f"- {t.date} — [[{t.source}]] — {t.what_changed}" for t in sorted(draft.timeline, key=lambda t: t.date)]
    names = _sections_of("concept")
    rendered = {
        "Definition": ["\n".join(definition)] if definition else [],
        "What Canon says": [CANON_UNCHECKED],
        "Where sources agree": agreements,
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


# --- the contradiction ledger --------------------------------------------------------
#
# The wiki states what the sources agree on. What they have ever disputed lives
# here, one file per subject, append-only, in two trees: keyed by concept and
# keyed by named entity, so a clash about Kael is reachable from the concept it
# surfaced in and from Kael. Permanence is the point — a document arriving next
# year is checked against clashes found long before it, which a list of
# currently-open questions could not do.


def entity_slug(name: str) -> str:
    """`AEGIS' Maschinenraum` -> `aegis-maschinenraum`."""
    lowered = (name.strip().lower().replace("ä", "ae").replace("ö", "oe")
               .replace("ü", "ue").replace("ß", "ss"))
    return re.sub(r"[^a-z0-9]+", "-", lowered).strip("-")


def ledger_subjects(draft: ConceptDraft) -> list[tuple[str, str, str]]:
    """`(subject_kind, slug, subject)` for every ledger a draft's clashes belong in."""
    subjects = [("concept", draft.slug, draft.slug)]
    for name in draft.entities:
        slug = entity_slug(name)
        if slug:
            subjects.append(("entity", slug, name))
    return subjects


def contradiction_record(draft: ConceptDraft, item: Disagreement, seen: str,
                         question_slug: str = "") -> dict[str, Any]:
    """One disagreement as a stored record — the unit the ledger never forgets."""
    return {
        "topic": item.topic, "concept": draft.slug,
        "sources": list(item.sources), "positions": list(item.positions),
        "citations": [c.model_dump() for c in item.citations],
        "resolution": item.resolution, "first_seen": seen, "question": question_slug,
    }


def record_entry(record: dict[str, Any]) -> list[str]:
    """A stored record rendered back into ledger prose."""
    lines = [f"### {record['topic']}\n"]
    trail = f"- first seen {record['first_seen']} · concept [[{record['concept']}]]"
    if record.get("question"):
        trail += f" · question [[{record['question']}]]"
    if record.get("resolution") and record["resolution"] != PENDING:
        trail += f" · resolution: {record['resolution']}"
    lines.append(trail)
    citations = [Citation(**c) for c in record.get("citations", [])]
    for index, source in enumerate(record["sources"]):
        position = record["positions"][index] if index < len(record["positions"]) else ""
        cited = [c for c in citations if c.file.endswith(f"{source}.md")]
        lines.append(f"- [[{source}]] — {position} {markers(cited)}".rstrip())
    return lines + [""]


def ledger_front(subject_kind: str, slug: str, subject: str,
                 records: list[dict[str, Any]], seen: str) -> dict[str, Any]:
    open_items = [r for r in records if r.get("resolution", PENDING) == PENDING]
    dates = sorted(r["first_seen"] for r in records) or [seen]
    return {
        "title": f"Contradictions — {subject}",
        "kind": "contradiction", "slug": slug,
        "subject_kind": subject_kind, "subject": subject,
        "status": "open" if open_items else "all-resolved",
        "first_seen": dates[0], "last_seen": seen,
        "open_count": len(open_items), "total_count": len(records),
        "concepts": sorted({r["concept"] for r in records}),
        "entities": [],
        "question_refs": sorted({r["question"] for r in records if r.get("question")}),
        "tags": [],
    }


def ledger_body(subject: str, records: list[dict[str, Any]], seen: str) -> str:
    open_lines, settled_lines = [], []
    for record in sorted(records, key=lambda r: (r["first_seen"], r["topic"])):
        entry = record_entry(record)
        pending = record.get("resolution", PENDING) == PENDING
        (open_lines if pending else settled_lines).extend(entry)
    rendered = {
        "Subject": [f"`{subject}` — every disagreement the ingest has ever recorded for it."],
        "Open contradictions": open_lines,
        "Resolved contradictions": settled_lines,
        "How this ledger is used": [LEDGER_USE],
    }
    names = _sections_of("contradiction")
    text = "\n".join(section(name, rendered.get(name, [])) for name in names)
    return text + f"\n<!-- recorded {seen} by {WRITER}; append-only, never a verdict -->\n"


def ledger_pages(store: dict[str, list[dict[str, Any]]], seen: str) -> dict[str, str]:
    """Render every ledger in the store as `{repo-relative path: text}`.

    The store is the record and this is its view, the same way `Graph/` is the
    record and `Codex/` its rendering. Regenerating a page can therefore never
    drop a contradiction: nothing is read back out of the Markdown.
    """
    pages = {}
    for key, records in store.items():
        subject_kind, _, slug = key.partition("/")
        if not records:
            continue
        subject = records[0].get("subject", slug)
        front = ledger_front(subject_kind, slug, subject, records, seen)
        pages[candidate_path("contradiction", slug, front)] = page_text(
            front, [ledger_body(subject, records, seen)])
    return pages


def question_for_disagreement(draft: ConceptDraft, item: Disagreement, slug: str,
                              seen: str) -> tuple[dict[str, Any], str]:
    """The worklist half of a contradiction: one question page, status open.

    The ledger remembers; this asks. `axis` is `incorrectness` because two
    sources disagreeing is exactly what that axis names. Owner is the author:
    an ingest records a clash and never settles one.
    """
    front = {
        "title": f"Widerspruch: {item.topic}",
        "kind": "question", "slug": slug, "axis": "incorrectness", "status": "open",
        "concepts": [draft.slug],
        "evidence": [{"citation": marker(c), "grade": "HIGH"} for c in item.citations] or
                    [{"citation": f"^[Sources/drive/{s}.md:1-1]", "grade": "LOW"}
                     for s in item.sources],
        "owner": "author", "tags": [],
        "context_summary": f"{item.topic}: {' vs '.join(item.positions)}"[:200],
        "context_scope": "global", "context_priority": "core",
        "chapter_start": 0, "chapter_end": 40, "spoiler_until": 40,
    }
    positions = [f"- [[{s}]] — {item.positions[i] if i < len(item.positions) else ''}".rstrip()
                 for i, s in enumerate(item.sources)]
    rendered = {
        "Question": [f"Die Quellen widersprechen sich zu **{item.topic}** "
                     f"(Konzept [[{draft.slug}]]). Welche Position gilt?"],
        "Evidence": positions,
        "What Canon says": [CANON_UNCHECKED],
        "Candidate answers": [QUESTION_ANSWERS],
        "Resolution": [],
    }
    names = _sections_of("question")
    body = "\n".join(section(name, rendered.get(name, [])) for name in names)
    return front, body + f"\n<!-- raised {seen} by {WRITER} from the contradiction ledger -->\n"
