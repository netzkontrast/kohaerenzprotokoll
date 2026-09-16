#!/usr/bin/env python3
"""Render the Codex/ views from the provenance graph (read-only).

`Codex/` is a derived view of `Graph/`. The facts live once, as CodexEntry,
StoryTimeEvent, WorldAxiom and World records seeded from `Canon/` by
`scripts/ingest_canon.py`; this script writes the Markdown a reader navigates.
The manuscript runs the other way: `Manuscript/` owns chapter prose, and
`scripts/chapter_drift.py` reports where it and the graph diverge.

    python3 scripts/render_codex_views.py            # write Codex/
    python3 scripts/render_codex_views.py --check    # exit 1 if views are stale
    python3 scripts/render_codex_views.py --stdout   # print, don't write

The shape is one convention, declared in `Graph/schema.yaml` and implemented in
`tools/kpcodex`:

    Codex/<VIEW>.md              navigation only — counts and links, no bodies
    Codex/<view>/README.md       the rendered index of that view
    Codex/<view>/<slug>.md       one retrievable unit

Writing puts every file the renderer produces on disk and deletes the ones it
no longer produces, so a renamed slug or a re-partitioned entry leaves nothing
behind. Never hand-edit a generated file: change the record in
`Graph/nodes/*.jsonl` and re-render.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from tools import kpcodex, kpgraph  # noqa: E402  (needs ROOT on the path)

GRAPH = ROOT / "Graph"
OUT = ROOT / "Codex"
EXIT_OK, EXIT_STALE, EXIT_CANNOT_RUN = 0, 1, 2
STALE_SHOWN = 8


def rendered_files(graph) -> dict[str, str]:
    """Every file Codex/ owns, keyed by its path relative to Codex/."""
    return kpcodex.all_views(graph)


def content_folder(name: str) -> str:
    """`Codex/entries/concept/riss.md` -> `Codex/entries` — the view it belongs to."""
    return "/".join(name.split("/")[:2])


def stale_files(files: dict[str, str]) -> set[str]:
    """Markdown under a rendered subfolder that the renderer no longer produces.

    Only the subfolders the renderer itself declares are swept, so hand-kept
    files at the `Codex/` root — `README.md` among them — are never touched.
    """
    folders = {content_folder(name) for name in files if name.count("/") > 1}
    on_disk = {path.relative_to(ROOT).as_posix()
               for folder in folders if (ROOT / folder).is_dir()
               for path in (ROOT / folder).rglob("*.md")}
    return on_disk - set(files)


def write(files: dict[str, str]) -> int:
    for name, content in sorted(files.items()):
        path = ROOT / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    for name in sorted(stale_files(files)):
        (ROOT / name).unlink()
        print(f"removed {name}")
    return len(files)


def check(files: dict[str, str]) -> list[str]:
    stale = [name for name, content in sorted(files.items())
             if not (ROOT / name).is_file()
             or (ROOT / name).read_text(encoding="utf-8") != content]
    return stale + [f"{name}: no longer rendered" for name in sorted(stale_files(files))]


def report(files: dict[str, str]) -> None:
    """What was written: the navigation-only routers, then each content folder."""
    routers = sorted(name for name in files if name.count("/") == 1)
    counts: dict[str, int] = {}
    for name in files:
        if name.count("/") > 1:
            folder = content_folder(name)
            counts[folder] = counts.get(folder, 0) + 1
    print(f"wrote {len(files)} file(s) under {OUT.name}/")
    print(f"  navigation: {', '.join(routers)}")
    for folder, count in sorted(counts.items()):
        print(f"  {folder}/: {count} file(s)")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--check", action="store_true", help="exit 1 if Codex/ is stale")
    parser.add_argument("--stdout", action="store_true", help="print instead of writing")
    args = parser.parse_args(argv)

    if not GRAPH.is_dir():
        print(f"no graph at {GRAPH}", file=sys.stderr)
        return EXIT_CANNOT_RUN
    files = rendered_files(kpgraph.load(ROOT))

    if args.stdout:
        for name, content in sorted(files.items()):
            print(f"\n===== {name} =====\n{content}")
        return EXIT_OK
    if args.check:
        stale = check(files)
        if stale:
            more = f" … (+{len(stale) - STALE_SHOWN} more)" if len(stale) > STALE_SHOWN else ""
            print("STALE: " + ", ".join(stale[:STALE_SHOWN]) + more
                  + " — run scripts/render_codex_views.py")
            return EXIT_STALE
        print(f"Codex/ views are up to date ({len(files)} files)")
        return EXIT_OK
    write(files)
    report(files)
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
