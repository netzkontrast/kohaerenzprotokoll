#!/usr/bin/env python3
"""Project the German chapter files into a lit-critic scene project.

lit-critic expects a project directory holding hand-written CANON.md and
STYLE.md plus one plain-text file per scene, each carrying a ``@@META`` header
that links it to its neighbours. Our manuscript instead keeps one Markdown file
per chapter, with YAML front matter and a planning header in front of the German
prose. This script is the adapter between the two.

    python3 scripts/lit_critic_project.py [--out DIR] [--check]

The projection is always built for the WHOLE manuscript, even when the gate only
analyses one chapter: lit-critic reads the Prev/Next chain for continuity
context, so a partial chain would make it report false continuity gaps.

The generated tree is disposable (``.lit-critic/`` is gitignored) and is
regenerated from the chapter files on every gate run. Nothing here ever writes
back into the manuscript.

Every scene records where its body came from, so a finding reported at scene
line N can be pointed back at the chapter file and line the author actually
edits — see ``chapter_line_for``.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from dataclasses import dataclass, asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS = ROOT / (
    "Manuscript/works/the-agency-system/works/"
    "hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/chapters"
)
INPUTS = ROOT / "tools/lit-critic"
DEFAULT_OUT = ROOT / ".lit-critic/project"
MANIFEST_NAME = "projection-manifest.json"

CHAPTER_GLOB = "[0-9][0-9]-*.md"
PLANNING_H1 = re.compile(r"^#\s+Chapter\s+\d+\s*$")
H1 = re.compile(r"^#\s+\S")
SCENE_BREAK = re.compile(r"^-{3,}\s*$")
HEADING = re.compile(r"^#{1,6}\s+(.*?)\s*$")

# @@META, Prev:, Next:, @@END, blank line — then the body starts.
HEADER_LINES = 5
BODY_START_SCENE_LINE = HEADER_LINES + 1

UMLAUTS = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss",
                         "Ä": "Ae", "Ö": "Oe", "Ü": "Ue"})


@dataclass
class Scene:
    """One projected scene: a contiguous slice of one chapter's prose body."""

    scene_file: str
    chapter_file: str
    chapter_number: int
    scene_index: int
    heading: str
    body_start_chapter_line: int   # 1-based line in the chapter .md
    body_start_scene_line: int     # 1-based line in the projected .txt
    body_lines: int
    words: int
    prev: str = "None"
    next: str = "TBD"

    def render(self, body: str) -> str:
        return (
            "@@META\n"
            f"Prev: {self.prev}\n"
            f"Next: {self.next}\n"
            "@@END\n"
            "\n"
            f"{body}\n"
        )


def slugify(text: str, fallback: str) -> str:
    text = text.translate(UMLAUTS)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-").lower()
    text = re.sub(r"-{2,}", "-", text)
    return text[:60].strip("-") or fallback


def chapter_files(chapters_dir: Path = CHAPTERS) -> list[Path]:
    """Chapter files in reading order. README and other strays are ignored."""
    return sorted(chapters_dir.glob(CHAPTER_GLOB), key=lambda p: chapter_number(p))


def chapter_number(path: Path) -> int:
    return int(path.name[:2])


def find_body_start(lines: list[str]) -> int | None:
    """Index of the first prose-body line, or None when the chapter is outline-only.

    The body is everything after the first top-level heading that is not the
    ``# Chapter N`` planning header — ``# Kapitel 3 — …`` in most chapters,
    ``# Kohärenz Protokoll — Kapitel 0 …`` in the prologue.
    """
    for i, line in enumerate(lines):
        if H1.match(line) and not PLANNING_H1.match(line):
            return i + 1
    return None


def split_scenes(lines: list[str], body_start: int) -> list[tuple[int, list[str]]]:
    """Split a prose body at its ``---`` scene breaks.

    Returns ``(chapter_line_of_first_body_line, body_lines)`` per scene, with
    blank padding trimmed and empty segments dropped. Line numbers are 1-based
    so they can be quoted straight back at the author.
    """
    scenes: list[tuple[int, list[str]]] = []
    current: list[str] = []
    start = body_start

    def flush(segment: list[str], segment_start: int) -> None:
        offset = 0
        while offset < len(segment) and not segment[offset].strip():
            offset += 1
        trimmed = segment[offset:]
        while trimmed and not trimmed[-1].strip():
            trimmed.pop()
        if trimmed:
            scenes.append((segment_start + offset + 1, trimmed))

    for index in range(body_start, len(lines)):
        if SCENE_BREAK.match(lines[index]):
            flush(current, start)
            current = []
            start = index + 1
            continue
        current.append(lines[index])
    flush(current, start)
    return scenes


def scene_heading(body: list[str], chapter_no: int, scene_index: int) -> str:
    for line in body:
        match = HEADING.match(line)
        if match:
            return match.group(1)
    return f"Kapitel {chapter_no}, Szene {scene_index}"


def count_words(body: list[str]) -> int:
    prose = "\n".join(line for line in body if not line.startswith("#"))
    return len(prose.split())


def build_scenes(chapters_dir: Path = CHAPTERS) -> tuple[list[Scene], dict[str, str], list[str]]:
    """Build every scene of the manuscript plus its rendered body text."""
    scenes: list[Scene] = []
    bodies: dict[str, str] = {}
    skipped: list[str] = []

    for chapter_path in chapter_files(chapters_dir):
        lines = chapter_path.read_text(encoding="utf-8").splitlines()
        body_start = find_body_start(lines)
        if body_start is None:
            skipped.append(f"{chapter_path.name}: no prose body (outline only)")
            continue

        number = chapter_number(chapter_path)
        segments = split_scenes(lines, body_start)
        if not segments:
            skipped.append(f"{chapter_path.name}: prose body is empty")
            continue

        for scene_index, (chapter_line, body) in enumerate(segments, start=1):
            heading = scene_heading(body, number, scene_index)
            slug = slugify(heading, f"szene-{scene_index:02d}")
            scene_file = f"{number:02d}.{scene_index:02d}_{slug}.txt"
            scenes.append(
                Scene(
                    scene_file=scene_file,
                    chapter_file=str(chapter_path.relative_to(ROOT)),
                    chapter_number=number,
                    scene_index=scene_index,
                    heading=heading,
                    body_start_chapter_line=chapter_line,
                    body_start_scene_line=BODY_START_SCENE_LINE,
                    body_lines=len(body),
                    words=count_words(body),
                )
            )
            bodies[scene_file] = "\n".join(body)

    for position, scene in enumerate(scenes):
        scene.prev = scenes[position - 1].scene_file if position else "None"
        scene.next = scenes[position + 1].scene_file if position + 1 < len(scenes) else "TBD"

    return scenes, bodies, skipped


def chapter_line_for(scene: dict | Scene, scene_line: int | None) -> int | None:
    """Translate a scene-file line number back to its chapter-file line."""
    if scene_line is None:
        return None
    data = scene if isinstance(scene, dict) else asdict(scene)
    offset = scene_line - data["body_start_scene_line"]
    if offset < 0:
        return data["body_start_chapter_line"]      # inside the @@META header
    offset = min(offset, max(data["body_lines"] - 1, 0))
    return data["body_start_chapter_line"] + offset


def write_if_changed(path: Path, content: str) -> bool:
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def build_project(out_dir: Path = DEFAULT_OUT, chapters_dir: Path = CHAPTERS,
                  inputs_dir: Path = INPUTS) -> dict:
    """Materialise the lit-critic project. Returns the manifest."""
    scenes, bodies, skipped = build_scenes(chapters_dir)
    text_dir = out_dir / "text"
    text_dir.mkdir(parents=True, exist_ok=True)

    missing_inputs = [
        name for name in ("CANON.md", "STYLE.md") if not (inputs_dir / name).exists()
    ]
    if missing_inputs:
        raise SystemExit(
            f"missing lit-critic input file(s) in {inputs_dir}: {', '.join(missing_inputs)}"
        )
    for name in ("CANON.md", "STYLE.md"):
        write_if_changed(out_dir / name, (inputs_dir / name).read_text(encoding="utf-8"))

    written = 0
    for scene in scenes:
        if write_if_changed(text_dir / scene.scene_file, scene.render(bodies[scene.scene_file])):
            written += 1

    expected = {scene.scene_file for scene in scenes}
    removed = []
    for stale in text_dir.glob("*.txt"):
        if stale.name not in expected:
            stale.unlink()
            removed.append(stale.name)

    manifest = {
        "chapters_dir": str(chapters_dir.relative_to(ROOT)),
        "project_dir": str(out_dir.relative_to(ROOT)),
        "scene_count": len(scenes),
        "chapter_count": len({scene.chapter_number for scene in scenes}),
        "word_count": sum(scene.words for scene in scenes),
        "skipped": skipped,
        "scenes": [asdict(scene) for scene in scenes],
    }
    (out_dir.parent / MANIFEST_NAME).write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    manifest["_written"] = written
    manifest["_removed"] = removed
    return manifest


def load_manifest(out_dir: Path = DEFAULT_OUT) -> dict:
    path = out_dir.parent / MANIFEST_NAME
    if not path.exists():
        raise SystemExit(
            f"no projection manifest at {path} — run scripts/lit_critic_project.py first"
        )
    return json.loads(path.read_text(encoding="utf-8"))


def scenes_for_chapters(manifest: dict, chapters: list[int]) -> list[dict]:
    wanted = set(chapters)
    return [scene for scene in manifest["scenes"] if scene["chapter_number"] in wanted]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT,
                        help=f"project directory to build (default: {DEFAULT_OUT})")
    parser.add_argument("--check", action="store_true",
                        help="report what the projection would contain without writing scene files")
    args = parser.parse_args(argv)

    if args.check:
        scenes, _, skipped = build_scenes()
        by_chapter: dict[int, int] = {}
        for scene in scenes:
            by_chapter[scene.chapter_number] = by_chapter.get(scene.chapter_number, 0) + 1
        print(f"{len(scenes)} scenes across {len(by_chapter)} chapters, "
              f"{sum(s.words for s in scenes):,} words")
        for chapter, count in sorted(by_chapter.items()):
            print(f"  Kap {chapter:>2}: {count} scenes")
        for note in skipped:
            print(f"  skipped {note}")
        return 0

    manifest = build_project(args.out)
    print(f"projected {manifest['scene_count']} scenes from "
          f"{manifest['chapter_count']} chapters into {args.out}")
    print(f"  {manifest['_written']} scene/input files written, "
          f"{len(manifest['_removed'])} stale removed")
    for note in manifest["skipped"]:
        print(f"  skipped {note}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
