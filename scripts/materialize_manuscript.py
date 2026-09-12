#!/usr/bin/env python3
"""Materialize Manuscript/ chapter files from the graph (Spec 121 layout).

The bare CLI runs the engine without `_novel_production`, so create_chapter
writes graph nodes only. Disk files are a derived artifact: render them with
the engine's own FileNovelStateDriver from graph ground truth (read-only DB
access; no graph writes, no provenance bypass).

WARNING -- the graph is NOT the source of truth for chapter prose. As of
2026-09-12 it holds chapter 0's body plus 400-1000 character outline stubs
for chapters 1-40, while the drafted prose of every chapter lives only in
the Manuscript/ files. Rendering from the graph therefore cannot reproduce
the manuscript. A pre-flight guard below refuses to run when any disk file
carries more prose than its graph body; pass --force to override it, which
you should only do when the graph has been brought up to date first.
"""
from __future__ import annotations

import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VENV = "/root/.local/share/pipx/venvs/agency/lib/python3.11/site-packages"
sys.path.insert(0, VENV)

from agency.capabilities.novel.config import NovelConfig          # noqa: E402
from agency.capabilities.novel.drivers_production import (        # noqa: E402
    FileNovelStateDriver)

AUTHOR = "The Agency System"
GENRE = "Hard SciFi / Cosmic Horror / Psychological Thriller"
TITLE = "Kohärenz Protokoll"


def chapters_from_graph() -> list[dict]:
    c = sqlite3.connect(f"file:{ROOT}/.agency/session.db?mode=ro", uri=True)
    q = """
    SELECT l.node_id FROM node_labels l WHERE l.label='Chapter'
    """
    out = []
    for (nid,) in c.execute(q):
        props = {}
        for table, cast in [("node_props_text", str), ("node_props_int", int)]:
            for k, v in c.execute(
                    f"SELECT pk.key, t.value FROM {table} t "
                    f"JOIN property_keys pk ON pk.id=t.key_id "
                    f"WHERE t.node_id=?", (nid,)):
                props[k] = cast(v)
        out.append(props)
    c.close()
    return sorted(out, key=lambda p: p.get("number", 0))


def _disk_prose_words(path: Path) -> int:
    """Words in the reader-facing prose body of a chapter file."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return 0
    marker = text.find("\n# Kapitel ")
    if marker == -1:
        return 0
    return len(text[marker:].split())


def check_disk_not_ahead(chapters: list[dict]) -> list[tuple[str, int, int]]:
    """Return chapters whose disk prose exceeds what the graph could render.

    The graph body is compared against the prose actually on disk. Anything
    where disk is materially ahead would be lost or misrepresented by a
    render, so the caller refuses to proceed.
    """
    chapter_dirs = list(ROOT.glob("Manuscript/**/chapters"))
    if not chapter_dirs:
        return []
    files = sorted(chapter_dirs[0].glob("*.md"))
    ahead = []
    for ch in chapters:
        number = ch.get("number", 0)
        prefix = f"{number:02d}-"
        match = next((f for f in files if f.name.startswith(prefix)), None)
        if match is None:
            continue
        disk = _disk_prose_words(match)
        graph = len(str(ch.get("body", "")).split())
        if disk > graph + 100:
            ahead.append((match.name, graph, disk))
    return ahead


def main() -> int:
    force = "--force" in sys.argv
    ahead = check_disk_not_ahead(chapters_from_graph())
    if ahead and not force:
        print("REFUSING TO RENDER: the manuscript on disk is ahead of the graph.\n")
        print(f"{'file':46} {'graph':>8} {'disk':>8}")
        for name, graph, disk in ahead:
            print(f"{name[:46]:46} {graph:>8} {disk:>8}")
        print(f"\n{len(ahead)} chapter(s) carry prose the graph cannot reproduce.")
        print("Rendering would replace them with outline stubs, or leave the")
        print("tree silently inconsistent with the graph. Bring the graph up to")
        print("date first, or pass --force if you genuinely intend to discard.")
        return 1
    if ahead:
        print(f"--force: proceeding despite {len(ahead)} chapter(s) ahead on disk.\n")
    cfg = NovelConfig.load([str(ROOT / ".agency" / "novel-config.yaml")])
    drv = FileNovelStateDriver(cfg)
    chapters = chapters_from_graph()
    created = skipped = 0
    for ch in chapters:
        r = drv.create_chapter(AUTHOR, GENRE, TITLE,
                               ch.get("number", 0), ch.get("title", ""),
                               body=ch.get("body", ""))
        if r.get("created", True):
            created += 1
        else:
            skipped += 1
        status = ch.get("status", "")
        if status:
            drv.update_chapter_field(AUTHOR, GENRE, TITLE,
                                     ch.get("number", 0), r["slug"],
                                     "status", status)
    print(f"chapters: {created} written, {skipped} already on disk "
          f"({len(chapters)} in graph)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
