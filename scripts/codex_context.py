#!/usr/bin/env python3
"""Return the smallest spoiler-safe Codex hit list for a chapter task.

    python3 scripts/codex_context.py "Bunker Gegenregister" --chapter 3
    python3 scripts/codex_context.py "Bunker Gegenregister" --whole-novel

Chapter mode excludes every hit whose generated detail page has no numeric
``Writer-safe-from`` value. ``--whole-novel`` is an explicit opt-in to unknown
or later knowledge. This tool routes context; it does not verify factual claims.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import wiki_fts

ROOT = Path(__file__).resolve().parent.parent
SAFE_FROM = re.compile(r"^- \*\*Writer-safe-from:\*\* `(?P<value>[^`]+)`\s*$", re.MULTILINE)


def is_detail_page(relative_path: str) -> bool:
    path = Path(relative_path)
    return (len(path.parts) >= 3 and path.parts[0] == "Codex"
            and path.parts[1] in {"glossary", "timeline", "worlds"}
            and path.name != "README.md")


def writer_safe_from(root: Path, relative_path: str) -> int | None:
    path = root / relative_path
    if not path.is_file():
        return None
    match = SAFE_FROM.search(path.read_text(encoding="utf-8", errors="replace"))
    if not match or not match.group("value").isdigit():
        return None
    return int(match.group("value"))


def route(root: Path, query: str, chapter: int | None, whole_novel: bool,
          limit: int) -> tuple[list[dict], list[dict]]:
    candidates = wiki_fts.search(root, query, scope="codex", limit=max(limit * 5, 25))
    accepted, blocked, seen = [], [], set()
    for hit in candidates:
        if not is_detail_page(hit["path"]):
            continue
        if hit["path"] in seen:
            continue
        seen.add(hit["path"])
        safe_from = writer_safe_from(root, hit["path"])
        enriched = {**hit, "writer_safe_from": safe_from}
        if whole_novel or (safe_from is not None and chapter is not None and safe_from <= chapter):
            if len(accepted) < limit:
                accepted.append(enriched)
        else:
            blocked.append(enriched)
    return accepted, blocked


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--chapter", type=int, help="target chapter; unknown/later entries are withheld")
    mode.add_argument("--whole-novel", action="store_true", help="explicitly allow unknown and later knowledge")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--root", type=Path, default=ROOT)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = args.root.resolve()
    if not wiki_fts.db_path(root).is_file():
        print("no index yet — run: python3 scripts/wiki_fts.py build", file=sys.stderr)
        return 2
    accepted, blocked = route(root, args.query, args.chapter, args.whole_novel, args.limit)
    if args.json:
        print(json.dumps({"hits": accepted, "withheld": len(blocked)}, ensure_ascii=False, indent=2))
        return 0
    for hit in accepted:
        safety = hit["writer_safe_from"] if hit["writer_safe_from"] is not None else "whole-novel"
        print(f"{hit['path']}:L{hit['start_line']}-L{hit['end_line']}  writer-safe-from={safety}")
        print(f"  {hit['heading'] or '(preamble)'}")
    if blocked:
        print(f"withheld {len(blocked)} hit(s) without a safe chapter boundary")
    if not accepted:
        print("no spoiler-safe Codex hit; use Wiki/context-map.md or request whole-novel mode explicitly")
    return 0


if __name__ == "__main__":
    sys.exit(main())
