#!/usr/bin/env python3
"""Materialize Manuscript/ chapter files from the graph (Spec 121 layout).

The bare CLI runs the engine without `_novel_production`, so create_chapter
writes graph nodes only. Disk files are a derived artifact: render them with
the engine's own FileNovelStateDriver from graph ground truth (read-only DB
access; no graph writes, no provenance bypass).
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


def main() -> int:
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
