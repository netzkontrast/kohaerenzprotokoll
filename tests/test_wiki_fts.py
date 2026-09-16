"""Tests for scripts/wiki_fts.py against a temporary Wiki/Canon/Sources tree."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import wiki_fts  # noqa: E402

WIKI_PAGE = """---
title: Schleier
---
Preamble about the Multiplizitäts-Schleier.

# Schleier

## Definition
Der Schleier verbirgt die Multiplizität bis Kapitel dreizehn.

```
# not a heading inside a fence
```

## Open questions
Wann fällt der Schleier für Juna?
"""
CANON_PAGE = "# Kernwelt\n\nKW1 ist die Kölner Ebene.\n\n## Sensorik\n\nRegen, Beton, Juna.\n"
SOURCE_PAGE = "Ein Drive-Export über Argus und die Monstergruppe.\n"
CODEX_PAGE = "# Argus\n\n## Inhalt\nArgus beobachtet Kohärenz und Kritik.\n"


@pytest.fixture
def tree(tmp_path: Path) -> Path:
    (tmp_path / "Wiki/concepts").mkdir(parents=True)
    (tmp_path / "Canon").mkdir()
    (tmp_path / "Sources/drive").mkdir(parents=True)
    (tmp_path / "Codex/glossary/concept").mkdir(parents=True)
    (tmp_path / "Wiki/concepts/concept/schleier.md").write_text(WIKI_PAGE, encoding="utf-8")
    (tmp_path / "Canon/kernwelt.md").write_text(CANON_PAGE, encoding="utf-8")
    (tmp_path / "Sources/drive/argus.md").write_text(SOURCE_PAGE, encoding="utf-8")
    (tmp_path / "Codex/glossary/concept/argus.md").write_text(CODEX_PAGE, encoding="utf-8")
    return tmp_path


def run(tree: Path, *argv: str) -> int:
    return wiki_fts.main(["--root", str(tree), *argv])


def test_chunk_lines_heading_trail_and_line_spans():
    chunks = wiki_fts.chunk_lines(WIKI_PAGE.splitlines())
    headings = [c["heading"] for c in chunks]
    assert headings == ["", "Schleier", "Schleier > Definition", "Schleier > Open questions"]
    assert (chunks[0]["start_line"], chunks[0]["end_line"]) == (1, 4)
    assert (chunks[2]["start_line"], chunks[2]["end_line"]) == (8, 13)
    assert chunks[3]["start_line"] == 15 and chunks[3]["text"].startswith("## Open questions")


def test_chunk_lines_drops_empty_sections():
    chunks = wiki_fts.chunk_lines(["# A", "", "## B", "text", "## C", ""])
    assert [c["heading"] for c in chunks] == ["A", "A > B", "A > C"]
    assert chunks[1]["end_line"] == 4


def test_build_indexes_all_scopes(tree, capsys):
    assert run(tree, "build") == 0
    assert "indexed 4 files" in capsys.readouterr().out
    assert (tree / wiki_fts.DB_RELATIVE).is_file()


def test_search_prints_path_line_range_and_heading(tree, capsys):
    run(tree, "build")
    assert run(tree, "search", "Multiplizität Kapitel") == 0
    out = capsys.readouterr().out
    assert "Wiki/concepts/concept/schleier.md:L8-L13" in out and "Schleier > Definition" in out


def test_search_json_and_scope_filter(tree, capsys):
    run(tree, "build")
    capsys.readouterr()
    assert run(tree, "search", "Juna", "--scope", "canon", "--json") == 0
    hits = json.loads(capsys.readouterr().out)
    assert [h["path"] for h in hits] == ["Canon/kernwelt.md"]
    assert hits[0]["rank"] == 1 and hits[0]["start_line"] == 5 and "Juna" in hits[0]["snippet"]


def test_codex_scope_finds_small_entity_page(tree, capsys):
    run(tree, "build")
    capsys.readouterr()
    assert run(tree, "search", "Argus Kohärenz", "--scope", "codex", "--json") == 0
    hits = json.loads(capsys.readouterr().out)
    assert [hit["path"] for hit in hits] == ["Codex/glossary/concept/argus.md"]


def test_search_limit_and_or_fallback(tree):
    run(tree, "build")
    assert len(wiki_fts.search(tree, "Schleier", limit=1)) == 1
    hits = wiki_fts.search(tree, "Argus xyzunknownword")
    assert hits and hits[0]["path"] == "Sources/drive/argus.md"
    assert wiki_fts.search(tree, "xyzunknownword") == []


def test_search_without_index_exits_1(tree, capsys):
    assert run(tree, "search", "Juna") == 1
    assert "run: python3 scripts/wiki_fts.py build" in capsys.readouterr().out


def test_incremental_build_skips_unchanged_and_reindexes_changed(tree, capsys):
    run(tree, "build")
    capsys.readouterr()
    run(tree, "build")
    assert "indexed 0 files (0 chunks), 4 unchanged, 0 removed" in capsys.readouterr().out
    (tree / "Canon/kernwelt.md").write_text("# Kernwelt\n\nNeuer Text über Lex.\n", encoding="utf-8")
    run(tree, "build")
    assert "indexed 1 files" in capsys.readouterr().out
    assert wiki_fts.search(tree, "Lex")[0]["path"] == "Canon/kernwelt.md"
    assert wiki_fts.search(tree, "Beton") == []


def test_build_removes_vanished_files(tree, capsys):
    run(tree, "build")
    (tree / "Sources/drive/argus.md").unlink()
    capsys.readouterr()
    run(tree, "build")
    assert "1 removed" in capsys.readouterr().out
    assert wiki_fts.search(tree, "Argus") == []


def test_stats_counts_per_scope(tree, capsys):
    run(tree, "build")
    capsys.readouterr()
    assert run(tree, "stats") == 0
    out = capsys.readouterr().out
    assert "wiki: 1 files, 4 chunks" in out and "canon: 1 files, 2 chunks" in out
    assert "codex: 1 files, 2 chunks" in out
    assert "sources: 1 files, 1 chunks" in out and "built:" in out


def test_doctor_without_index_is_ok(tree, capsys):
    assert run(tree, "doctor") == 0
    assert "not built yet" in capsys.readouterr().out


def test_doctor_flags_stale_unindexed_and_vanished(tree, capsys):
    run(tree, "build")
    (tree / "Canon/kernwelt.md").write_text("# geändert\n", encoding="utf-8")
    (tree / "Canon/neu.md").write_text("# neu\n", encoding="utf-8")
    (tree / "Sources/drive/argus.md").unlink()
    capsys.readouterr()
    assert run(tree, "doctor") == 1
    out = capsys.readouterr().out
    assert "stale: Canon/kernwelt.md" in out and "unindexed: Canon/neu.md" in out
    assert "vanished: Sources/drive/argus.md" in out
    run(tree, "build")
    assert run(tree, "doctor") == 0


def test_match_expression_quotes_tokens():
    assert wiki_fts.match_expression('a "b" c-d', "AND") == '"a" AND "b" AND "c-d"'
    with pytest.raises(SystemExit):
        wiki_fts.match_expression("...", "OR")
