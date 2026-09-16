"""Rendered views of the research wiki.

``Wiki/index.md``, ``Wiki/concept-table.md`` and ``Wiki/graph/coverage.json``
are derived from page frontmatter and never edited by hand
(``conventions.yaml`` → ``ownership.tools_only``). ``scripts/render_wiki_views.py``
writes them; ``scripts/wiki_lint.py`` (rule ``index-sync``) compares the files
on disk with what these functions return. Everything here is deterministic —
no timestamps — so ``--check`` gives the same answer on any day.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

from . import wiki_pages
from .wiki_pages import Page

RENDER_NOTE = ("<!-- rendered by scripts/render_wiki_views.py from page frontmatter; "
               "edit the pages, not this file -->")
KINDS = (("source", "Sources"), ("concept", "Concepts"),
         ("question", "Questions"), ("synthesis", "Syntheses"))
VIEW_FILES = ("index.md", "concept-table.md", "graph/coverage.json")
DEFINITION_MAX_CHARS = 160
EMPTY = "—"
CITATION_RE = re.compile(r"\s*\^\[[^\]]*\]")
LINK_RE = re.compile(r"\[\[([^\[\]|#]+?)(?:#[^\[\]|]*)?(?:\|([^\[\]]*))?\]\]")
SENTENCE_END_RE = re.compile(r"(?<=[.!?])\s")


def _field(page: Page, key: str) -> str:
    value = page.front.get(key)
    if value is None or value == "" or value == []:
        return EMPTY
    if isinstance(value, list):
        return ", ".join(str(v) for v in value)
    return str(value)


def _promoted(pages: list[Page]) -> list[Page]:
    return sorted((p for p in pages if not p.is_candidate), key=lambda p: (p.kind or "", p.slug))


def _index_row(page: Page) -> str:
    link = f"[{page.title}]({page.rel})"
    columns = {
        "source": ("tier", "category", "status"),
        "concept": ("kind_detail", "confidence", "canon_status", "status"),
        "question": ("axis", "status", "owner"),
        "synthesis": ("filed", "status"),
    }.get(page.kind or "", ("status",))
    return f"- {link} · " + " · ".join(_field(page, key) for key in columns)


def render_index(pages: list[Page]) -> str:
    """The catalogue by kind; candidates are counted, never listed."""
    promoted = _promoted(pages)
    candidates = [p for p in pages if p.is_candidate]
    lines = ["# Wiki index", "", RENDER_NOTE, "",
             "- [Overview](overview.md) · what we currently understand the novel to be",
             "- [Concept table](concept-table.md) · concept · definition · sources · status · open questions",
             "- [Log](log.md) · append-only record of every operation",
             "- [Schema](SCHEMA.md) · the operating contract"]
    for kind, heading in KINDS:
        rows = [p for p in promoted if p.kind == kind]
        lines += ["", f"## {heading} ({len(rows)})", ""]
        lines += [_index_row(p) for p in rows] or ["_none yet_"]
    lines += ["", f"## Candidates ({len(candidates)})", "",
              "_written by a program, awaiting `/wiki-promote`; not part of the wiki until promoted_"]
    return "\n".join(lines) + "\n"


def _definition(page: Page) -> str:
    text = wiki_pages.sections(page.body).get("Definition", "")
    text = CITATION_RE.sub("", text)
    text = LINK_RE.sub(lambda m: (m.group(2) or m.group(1)).strip(), text)
    text = " ".join(text.split())
    if not text:
        return EMPTY
    first = SENTENCE_END_RE.split(text, maxsplit=1)[0]
    if len(first) > DEFINITION_MAX_CHARS:
        first = first[:DEFINITION_MAX_CHARS - 1].rstrip() + "…"
    return first.replace("|", "\\|")


def _open_question_count(page: Page) -> int:
    return len(wiki_pages.wikilinks(wiki_pages.sections(page.body).get("Open questions", "")))


def render_concept_table(pages: list[Page]) -> str:
    """The compressed map: one row per promoted concept page."""
    concepts = [p for p in _promoted(pages) if p.kind == "concept"]
    lines = ["# Concept table", "", RENDER_NOTE, "",
             "| concept | kind | definition | sources | confidence | canon | status | open questions |",
             "|---|---|---|---|---|---|---|---|"]
    for page in concepts:
        sources = page.front.get("sources") or []
        lines.append("| " + " | ".join([
            f"[{page.title}]({page.rel})", _field(page, "kind_detail"), _definition(page),
            str(len(sources)), _field(page, "confidence"), _field(page, "canon_status"),
            _field(page, "status"), str(_open_question_count(page)),
        ]) + " |")
    if not concepts:
        lines.append("| _no concept pages yet_ | | | | | | | |")
    return "\n".join(lines) + "\n"


def _manifest_summary(manifest_path: Path | None) -> dict[str, Any]:
    if manifest_path is None or not manifest_path.exists():
        return {"total": 0, "exported": 0, "by_tier": {}}
    tiers: Counter[str] = Counter()
    exported = total = 0
    for line in manifest_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        total += 1
        tiers[str(record.get("tier", ""))] += 1
        exported += bool(record.get("export_path"))
    return {"total": total, "exported": exported, "by_tier": dict(sorted(tiers.items()))}


def _count_by(pages: list[Page], key: str) -> dict[str, int]:
    return dict(sorted(Counter(_field(p, key) for p in pages).items()))


def coverage(pages: list[Page], edges: list[dict[str, Any]],
             manifest_path: Path | None = None) -> dict[str, Any]:
    """The numbers of concept §4 F: what is ingested, understood, questioned, contested."""
    promoted = _promoted(pages)
    by_kind = {kind: [p for p in promoted if p.kind == kind] for kind, _ in KINDS}
    return {
        "pages": {kind: _count_by(rows, "status") for kind, rows in by_kind.items()},
        "candidates": _count_by([p for p in pages if p.is_candidate], "kind"),
        "sources": {"ingested": len(by_kind["source"]), "manifest": _manifest_summary(manifest_path),
                    "by_tier": _count_by(by_kind["source"], "tier")},
        "concepts": {"by_canon_status": _count_by(by_kind["concept"], "canon_status"),
                     "by_confidence": _count_by(by_kind["concept"], "confidence")},
        "questions": {"by_axis": _count_by(by_kind["question"], "axis"),
                      "by_status": _count_by(by_kind["question"], "status")},
        "contested": sorted(p.slug for p in promoted if p.status == "contested"),
        "edges": {"total": len(edges), "by_type": dict(sorted(Counter(str(e.get("type")) for e in edges).items()))},
    }


def render_coverage(data: dict[str, Any]) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True) + "\n"


def views(wiki_root: Path, repo_root: Path) -> dict[str, str]:
    """Rendered text of every view file, keyed by path relative to the wiki root."""
    pages = wiki_pages.iter_pages(wiki_root, include_candidates=True)
    edges = wiki_pages.read_edges(wiki_root / "graph" / "edges.jsonl")
    manifest = repo_root / "Sources" / "manifest.jsonl"
    return {
        "index.md": render_index(pages),
        "concept-table.md": render_concept_table(pages),
        "graph/coverage.json": render_coverage(coverage(pages, edges, manifest)),
    }


def check(wiki_root: Path, repo_root: Path) -> list[str]:
    """Names of view files that are missing or differ from their rendering."""
    stale = []
    for rel, text in views(wiki_root, repo_root).items():
        target = wiki_root / rel
        if not target.exists():
            stale.append(f"{rel}: missing")
        elif target.read_text(encoding="utf-8") != text:
            stale.append(f"{rel}: stale")
    return stale
