"""Tests for the conservative Codex chapter-context gate."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import codex_context  # noqa: E402


def test_writer_safe_from_is_explicit_not_inferred(tmp_path: Path):
    known = tmp_path / "Codex/glossary/concept/known.md"
    unknown = tmp_path / "Codex/glossary/concept/unknown.md"
    known.parent.mkdir(parents=True)
    known.write_text("# Known\n\n- **Writer-safe-from:** `3`\n", encoding="utf-8")
    unknown.write_text("# Unknown\n\nNo metadata.\n", encoding="utf-8")
    assert codex_context.writer_safe_from(tmp_path, known.relative_to(tmp_path).as_posix()) == 3
    assert codex_context.writer_safe_from(tmp_path, unknown.relative_to(tmp_path).as_posix()) is None


def test_chapter_mode_withholds_unknown_and_later_hits(tmp_path: Path, monkeypatch):
    base = tmp_path / "Codex/glossary/concept"
    base.mkdir(parents=True)
    for slug, safe in (("safe", "3"), ("late", "20"), ("unknown", "unknown")):
        (base / f"{slug}.md").write_text(
            f"# {slug}\n\n- **Writer-safe-from:** `{safe}`\n", encoding="utf-8")
    hits = [{"path": f"Codex/glossary/concept/{slug}.md", "rank": rank}
            for rank, slug in enumerate(("safe", "late", "unknown"), 1)]
    monkeypatch.setattr(codex_context.wiki_fts, "search", lambda *args, **kwargs: hits)
    accepted, blocked = codex_context.route(tmp_path, "test", chapter=3, whole_novel=False, limit=5)
    assert [hit["path"] for hit in accepted] == ["Codex/glossary/concept/safe.md"]
    assert len(blocked) == 2
    accepted, _ = codex_context.route(tmp_path, "test", chapter=None, whole_novel=True, limit=5)
    assert len(accepted) == 3


def test_route_returns_at_most_one_hit_per_file(tmp_path: Path, monkeypatch):
    page = tmp_path / "Codex/glossary/concept/safe.md"
    page.parent.mkdir(parents=True)
    page.write_text("# Safe\n\n- **Writer-safe-from:** `1`\n", encoding="utf-8")
    hits = [{"path": "Codex/glossary/concept/safe.md", "rank": rank} for rank in (1, 2)]
    monkeypatch.setattr(codex_context.wiki_fts, "search", lambda *args, **kwargs: hits)
    accepted, blocked = codex_context.route(tmp_path, "test", chapter=3, whole_novel=False, limit=5)
    assert len(accepted) == 1 and blocked == []


def test_route_excludes_navigation_indexes(tmp_path: Path, monkeypatch):
    index = tmp_path / "Codex/glossary/concept/README.md"
    index.parent.mkdir(parents=True)
    index.write_text("# Index\n", encoding="utf-8")
    hits = [{"path": "Codex/glossary/concept/README.md", "rank": 1}]
    monkeypatch.setattr(codex_context.wiki_fts, "search", lambda *args, **kwargs: hits)
    assert codex_context.route(tmp_path, "test", chapter=None, whole_novel=True, limit=5) == ([], [])
