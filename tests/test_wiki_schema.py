"""Tests for the wiki schema contract (``Wiki/schema/*.yaml``) and the shared page model.

The YAML is the single source of truth; these tests pin what every script relies
on: kinds, transitions, enums, the citation grammar, the templates' sections and
the mirror between the YAML enums and ``tools/kpwiki/schema.py``.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.kpwiki import wiki_pages, wiki_schema  # noqa: E402

PAGE = """---
title: "Kohärenz"
kind: concept
slug: kohaerenz
status: draft
sources: [konzeptentwicklung]
---
## Definition
Kohärenz ist „ein Maß der Übereinstimmung“ ^[Sources/drive/konzeptentwicklung.md:12-14] und hängt mit [[dkt|DKT]] und [[juna#anteile]] zusammen. `[[not-a-link]]`

## Open questions
- [[frage-1]]
"""


def test_every_schema_file_loads_as_mapping():
    for name in wiki_schema.FILES:
        assert isinstance(wiki_schema.load(name), dict)
    with pytest.raises(ValueError):
        wiki_schema.load("nope")


def test_kinds_and_required_fields():
    assert wiki_schema.kinds() == ["source", "concept", "question", "synthesis"]
    for name in wiki_schema.kinds():
        required = wiki_schema.required_fields(name)
        assert {"title", "kind", "slug"} <= set(required), name
    with pytest.raises(KeyError):
        wiki_schema.kind("chapter")


def test_lifecycle_transitions():
    assert wiki_schema.legal_transition("draft", "reviewed")
    assert wiki_schema.legal_transition("reviewed", "reviewed")
    assert wiki_schema.legal_transition("reviewed", "contested")
    assert not wiki_schema.legal_transition("draft", "contested")
    assert not wiki_schema.legal_transition("archived", "draft")
    assert wiki_schema.protected_statuses() == ["reviewed"]


def test_field_enum_resolution():
    assert wiki_schema.field_enum("source", "kind") == ["source"]
    assert wiki_schema.field_enum("concept", "status") == wiki_schema.lifecycle()["states"]
    assert wiki_schema.field_enum("question", "status") == wiki_schema.enum_values("question_status")
    assert wiki_schema.field_enum("question", "owner") == ["author", "session", "graph"]
    assert wiki_schema.field_enum("source", "title") is None
    with pytest.raises(KeyError):
        wiki_schema.enum_values("colour")


def test_kind_for_path_by_directory():
    assert wiki_schema.kind_for_path("Wiki/sources/x.md") == "source"
    assert wiki_schema.kind_for_path(Path("Wiki/questions/q.md")) == "question"
    assert wiki_schema.kind_for_path("Wiki/candidates/x.md") is None
    assert wiki_schema.kind_for_path("Plan/x.md") is None


def test_slug_pattern_and_length():
    pattern = wiki_schema.slug_pattern()
    assert pattern.match("kohaerenz-protokoll-1")
    assert not pattern.match("Kohärenz")
    assert not pattern.match("-leading")
    assert wiki_schema.conventions()["slug"]["max_length"] == 60


def test_citation_pattern_groups():
    pattern = wiki_schema.citation_pattern()
    match = pattern.search("x ^[Sources/drive/abc-1.md:12-14] y")
    assert match and match.group("file") == "Sources/drive/abc-1.md"
    assert (match.group("start"), match.group("end")) == ("12", "14")
    single = pattern.search("^[Canon/kap0-v1-annotiert.md:3]")
    assert single and single.group("end") is None
    assert pattern.search("^[Wiki/concepts/x.md:1]") is None


def test_edge_types_and_writers():
    assert set(wiki_schema.edge_types()) == {"supports", "extends", "contradicts",
                                             "supersedes", "same_as", "mentions"}
    assert "writes" in wiki_schema.writer_for("/wiki-promote")
    assert wiki_schema.writer_for("/nope") is None


@pytest.mark.parametrize("name", ["source", "concept", "question", "synthesis"])
def test_template_carries_exact_sections_in_order(name):
    spec = wiki_schema.kind(name)
    text = (ROOT / spec["template"]).read_text(encoding="utf-8")
    tokens = wiki_pages.template_tokens(text)
    front, body = wiki_pages.split_frontmatter(wiki_pages.fill_template(text, {t: t for t in tokens}))
    assert list(wiki_pages.sections(body)) == spec["sections"]
    assert front.get("kind") == name
    for field in spec["required"]:
        assert field in front, f"{name} template lacks {field}"


def test_fill_template_requires_every_token():
    assert wiki_pages.template_tokens("{{a}} {{b}} {{a}}") == ["a", "b"]
    assert wiki_pages.fill_template("x={{a}}", {"a": 1}) == "x=1"
    with pytest.raises(KeyError, match="b"):
        wiki_pages.fill_template("{{a}} {{b}}", {"a": 1})


def test_yaml_enums_mirror_schema_py():
    pytest.importorskip("pydantic")
    assert wiki_schema.mirror_report() == []


def test_split_frontmatter_variants():
    front, body = wiki_pages.split_frontmatter(PAGE)
    assert front["slug"] == "kohaerenz" and body.startswith("## Definition")
    assert wiki_pages.split_frontmatter("no front") == ({}, "no front")
    with pytest.raises(ValueError):
        wiki_pages.split_frontmatter('---\n"x: [\n---\nbody')
    with pytest.raises(ValueError):
        wiki_pages.split_frontmatter("---\n- a\n---\nbody")


def test_sections_links_citations_quotes():
    _, body = wiki_pages.split_frontmatter(PAGE)
    assert list(wiki_pages.sections(body)) == ["Definition", "Open questions"]
    assert wiki_pages.wikilinks(body) == ["dkt", "juna", "frage-1"]
    cite = wiki_pages.citations(body)[0]
    assert (cite.file, cite.start, cite.end) == ("Sources/drive/konzeptentwicklung.md", 12, 14)
    assert wiki_pages.quoted_fragments(body) == ["ein Maß der Übereinstimmung"]


def test_iter_pages_flags_candidates_and_records_errors(tmp_path):
    (tmp_path / "concepts").mkdir()
    (tmp_path / "candidates").mkdir()
    (tmp_path / "concepts" / "kohaerenz.md").write_text(PAGE, encoding="utf-8")
    (tmp_path / "candidates" / "q1.md").write_text("---\nkind: question\n---\nbody\n", encoding="utf-8")
    (tmp_path / "candidates" / "bad.md").write_text('---\n"x: [\n---\nbody\n', encoding="utf-8")
    pages = {p.rel: p for p in wiki_pages.iter_pages(tmp_path)}
    assert pages["concepts/kohaerenz.md"].kind == "concept"
    assert pages["candidates/q1.md"].kind == "question" and pages["candidates/q1.md"].is_candidate
    assert pages["candidates/bad.md"].error and pages["candidates/bad.md"].front == {}
    assert [p.rel for p in wiki_pages.iter_pages(tmp_path, include_candidates=False)] == ["concepts/kohaerenz.md"]


def test_log_line_grammar():
    entry = wiki_pages.parse_log_line(
        "## [2026-09-16] ingest | Konzeptentwicklung | skill=/research-ingest | sha256=abc", 3)
    assert entry and (entry.date, entry.op, entry.title) == ("2026-09-16", "ingest", "Konzeptentwicklung")
    assert entry.fields == {"skill": "/research-ingest", "sha256": "abc"} and entry.lineno == 3
    assert wiki_pages.parse_log_line("# Wiki log") is None


def test_real_log_parses():
    entries = wiki_pages.read_log(ROOT / "Wiki" / "log.md")
    assert entries and all(e.fields.get("skill") for e in entries)


def test_body_sha256_normalises_line_endings():
    assert wiki_pages.body_sha256("a\r\nb  \n\n") == wiki_pages.body_sha256("a\nb")
    assert wiki_pages.body_sha256("a") != wiki_pages.body_sha256("b")


def test_read_edges_reports_bad_line(tmp_path):
    path = tmp_path / "edges.jsonl"
    path.write_text('{"from": "a", "to": "b"}\n\nnot json\n', encoding="utf-8")
    with pytest.raises(ValueError, match="edges.jsonl:3"):
        wiki_pages.read_edges(path)
    assert wiki_pages.read_edges(tmp_path / "missing.jsonl") == []
