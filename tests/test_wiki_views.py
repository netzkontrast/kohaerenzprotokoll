"""Tests for the rendered wiki views (index, concept table, coverage) and their CLI."""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.kpwiki import wiki_pages, wiki_views  # noqa: E402

SOURCE = """---
title: "Konzeptentwicklung"
kind: source
slug: konzeptentwicklung
tier: T3-work
category: kernkonzept
status: reviewed
---
## Summary
Ein Dokument.
"""
CONCEPT = """---
title: "Kohärenz"
kind: concept
slug: kohaerenz
kind_detail: rule
status: contested
confidence: high
sources: [konzeptentwicklung, audit-1]
canon_status: unverified
---
## Definition
Kohärenz ist „ein Maß“ ^[Sources/drive/konzeptentwicklung.md:1-2] und hängt mit [[dkt|DKT]] zusammen. Zweiter Satz.

## Open questions
- [[frage-1]]
- [[frage-2]]
"""


def _load_cli():
    spec = importlib.util.spec_from_file_location("render_wiki_views", ROOT / "scripts" / "render_wiki_views.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def make_wiki(tmp_path: Path) -> Path:
    wiki = tmp_path / "Wiki"
    for name in ("sources", "concepts", "questions", "syntheses", "candidates", "graph"):
        (wiki / name).mkdir(parents=True)
    (wiki / "sources" / "konzeptentwicklung.md").write_text(SOURCE, encoding="utf-8")
    (wiki / "concepts" / "kohaerenz.md").write_text(CONCEPT, encoding="utf-8")
    (wiki / "candidates" / "q1.md").write_text("---\nkind: question\nslug: q1\nstatus: draft\n---\nbody\n", encoding="utf-8")
    (wiki / "graph" / "edges.jsonl").write_text(
        '{"from": "kohaerenz", "to": "dkt", "type": "supports"}\n', encoding="utf-8")
    manifest = tmp_path / "Sources" / "manifest.jsonl"
    manifest.parent.mkdir()
    manifest.write_text('{"slug": "a", "tier": "T3-work", "export_path": "Sources/drive/a.md"}\n'
                        '{"slug": "b", "tier": "T2-theory", "export_path": ""}\n', encoding="utf-8")
    return wiki


def test_index_lists_promoted_pages_and_counts_candidates(tmp_path):
    wiki = make_wiki(tmp_path)
    text = wiki_views.render_index(wiki_pages.iter_pages(wiki))
    assert "## Sources (1)" in text and "## Concepts (1)" in text and "## Candidates (1)" in text
    assert "- [Konzeptentwicklung](sources/konzeptentwicklung.md) · T3-work · kernkonzept · reviewed" in text
    assert "- [Kohärenz](concepts/kohaerenz.md) · rule · high · unverified · contested" in text
    assert "q1" not in text and "## Questions (0)\n\n_none yet_" in text


def test_concept_table_strips_citations_and_links(tmp_path):
    wiki = make_wiki(tmp_path)
    text = wiki_views.render_concept_table(wiki_pages.iter_pages(wiki))
    row = [line for line in text.splitlines() if line.startswith("| [Kohärenz]")][0]
    assert row == ("| [Kohärenz](concepts/kohaerenz.md) | rule | Kohärenz ist „ein Maß“ und hängt mit DKT zusammen. "
                   "| 2 | high | unverified | contested | 2 |")


def test_concept_table_empty_wiki():
    assert "_no concept pages yet_" in wiki_views.render_concept_table([])


def test_coverage_numbers(tmp_path):
    wiki = make_wiki(tmp_path)
    pages = wiki_pages.iter_pages(wiki)
    edges = wiki_pages.read_edges(wiki / "graph" / "edges.jsonl")
    data = wiki_views.coverage(pages, edges, tmp_path / "Sources" / "manifest.jsonl")
    assert data["pages"]["concept"] == {"contested": 1} and data["candidates"] == {"question": 1}
    assert data["sources"]["manifest"] == {"total": 2, "exported": 1,
                                           "by_tier": {"T2-theory": 1, "T3-work": 1}}
    assert data["contested"] == ["kohaerenz"] and data["edges"] == {"total": 1, "by_type": {"supports": 1}}
    assert data["concepts"]["by_canon_status"] == {"unverified": 1}


def test_cli_writes_views_then_check_is_clean_and_detects_drift(tmp_path):
    wiki = make_wiki(tmp_path)
    cli = _load_cli()
    assert cli.main(["--wiki-root", str(wiki), "--repo-root", str(tmp_path)]) == 0
    assert cli.main(["--wiki-root", str(wiki), "--repo-root", str(tmp_path), "--check"]) == 0
    assert json.loads((wiki / "graph" / "coverage.json").read_text())["edges"]["total"] == 1
    (wiki / "index.md").write_text("edited\n", encoding="utf-8")
    assert wiki_views.check(wiki, tmp_path) == ["index.md: stale"]
    assert cli.main(["--wiki-root", str(wiki), "--repo-root", str(tmp_path), "--check"]) == 1


def test_cli_check_reports_missing_views_and_missing_wiki(tmp_path):
    wiki = make_wiki(tmp_path)
    assert sorted(wiki_views.check(wiki, tmp_path)) == [
        "concept-table.md: missing", "graph/coverage.json: missing", "index.md: missing"]
    assert _load_cli().main(["--wiki-root", str(tmp_path / "nowhere")]) == 2


def test_rendering_is_deterministic(tmp_path):
    wiki = make_wiki(tmp_path)
    assert wiki_views.views(wiki, tmp_path) == wiki_views.views(wiki, tmp_path)


def test_real_wiki_views_are_in_sync():
    assert wiki_views.check(ROOT / "Wiki", ROOT) == []
