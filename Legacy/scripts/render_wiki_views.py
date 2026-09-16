#!/usr/bin/env python3
"""Render the tools-only views of the research wiki from page frontmatter.

    python3 scripts/render_wiki_views.py            # write global views and local README indexes
    python3 scripts/render_wiki_views.py --check    # exit 1 when any view is stale or missing

These files are derived (``Wiki/schema/conventions.yaml`` → ``tools_only``)
and never edited by hand; ``scripts/wiki_lint.py`` rule ``index-sync`` fails
until this script has been re-run. Rendering is deterministic (no timestamps),
so ``--check`` is stable. Standard library plus PyYAML only.
"""
from __future__ import annotations

import argparse
import os
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from tools.kpwiki import wiki_views  # noqa: E402


def write_atomic(target: Path, text: str) -> None:
    """Write via a sibling temp file + rename so readers never see a partial view."""
    target.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(dir=target.parent, prefix=f".{target.name}.", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        os.replace(tmp_name, target)
    except BaseException:
        Path(tmp_name).unlink(missing_ok=True)
        raise


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--wiki-root", type=Path, default=None, help="default <repo-root>/Wiki")
    parser.add_argument("--repo-root", type=Path, default=ROOT, help="where Sources/manifest.jsonl lives")
    parser.add_argument("--check", action="store_true", help="exit 1 when a view is stale, write nothing")
    args = parser.parse_args(argv)
    repo_root = args.repo_root.resolve()
    wiki_root = (args.wiki_root or repo_root / "Wiki").resolve()
    if not wiki_root.is_dir():
        print(f"no wiki at {wiki_root}", file=sys.stderr)
        return 2
    if args.check:
        stale = wiki_views.check(wiki_root, repo_root)
        for item in stale:
            print(f"Wiki/{item}")
        print("views up to date" if not stale else "views STALE — run scripts/render_wiki_views.py")
        return 1 if stale else 0
    for rel, text in wiki_views.views(wiki_root, repo_root).items():
        write_atomic(wiki_root / rel, text)
        print(f"wrote Wiki/{rel}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
