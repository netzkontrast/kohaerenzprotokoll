"""Tests for the chapter → lit-critic scene projection.

The projection is the one place where a silent bug is expensive: a wrong line
offset sends the author to the wrong paragraph of the wrong chapter, and the
finding looks like nonsense rather than like a bug. These tests pin the split
and the line mapping against the real manuscript.

    python3 -m pytest tests/test_lit_critic_projection.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import lit_critic_project as proj  # noqa: E402


@pytest.fixture(scope="module")
def built():
    scenes, bodies, skipped = proj.build_scenes()
    return scenes, bodies, skipped


def test_every_chapter_file_is_projected(built):
    scenes, _, skipped = built
    projected = {scene.chapter_number for scene in scenes}
    expected = {proj.chapter_number(path) for path in proj.chapter_files()}
    assert projected == expected, f"unprojected chapters: {sorted(expected - projected)} ({skipped})"


def test_scene_bodies_are_verbatim_chapter_slices(built):
    """Every projected line must exist, unchanged, at the mapped chapter line."""
    scenes, bodies, _ = built
    cache: dict[str, list[str]] = {}
    for scene in scenes:
        chapter_lines = cache.setdefault(
            scene.chapter_file, (ROOT / scene.chapter_file).read_text(encoding="utf-8").splitlines()
        )
        body_lines = bodies[scene.scene_file].splitlines()
        assert len(body_lines) == scene.body_lines
        start = scene.body_start_chapter_line - 1
        assert chapter_lines[start:start + len(body_lines)] == body_lines, scene.scene_file


def test_scene_line_maps_back_to_the_chapter_line(built):
    """A finding at scene line N points at the chapter line the author edits."""
    scenes, bodies, _ = built
    cache: dict[str, list[str]] = {}
    for scene in scenes:
        chapter_lines = cache.setdefault(
            scene.chapter_file, (ROOT / scene.chapter_file).read_text(encoding="utf-8").splitlines()
        )
        rendered = scene.render(bodies[scene.scene_file]).splitlines()
        for scene_line in range(scene.body_start_scene_line, len(rendered) + 1):
            chapter_line = proj.chapter_line_for(scene, scene_line)
            assert chapter_lines[chapter_line - 1] == rendered[scene_line - 1], (
                f"{scene.scene_file} line {scene_line} → {scene.chapter_file}:{chapter_line}"
            )


def test_header_lines_map_to_the_scene_start(built):
    """Findings on the @@META block itself land on the scene's first line."""
    scenes, _, _ = built
    scene = scenes[0]
    for header_line in range(1, proj.BODY_START_SCENE_LINE):
        assert proj.chapter_line_for(scene, header_line) == scene.body_start_chapter_line
    assert proj.chapter_line_for(scene, None) is None


def test_prev_next_chain_is_a_closed_doubly_linked_list(built):
    scenes, _, _ = built
    assert scenes[0].prev == "None"
    assert scenes[-1].next == "TBD"
    for earlier, later in zip(scenes, scenes[1:]):
        assert earlier.next == later.scene_file
        assert later.prev == earlier.scene_file
    assert len({scene.scene_file for scene in scenes}) == len(scenes), "duplicate scene filenames"


def test_scene_order_follows_reading_order(built):
    scenes, _, _ = built
    keys = [(scene.chapter_number, scene.scene_index) for scene in scenes]
    assert keys == sorted(keys)


def test_planning_header_is_never_projected(built):
    """Front matter, `# Chapter N`, Summary and Outline stay out of the prose."""
    scenes, bodies, _ = built
    for scene in scenes:
        body = bodies[scene.scene_file]
        assert "## Summary" not in body
        assert "## Outline" not in body
        assert not body.startswith("---")
        assert "type: novel.chapter" not in body


def test_split_scenes_trims_padding_and_drops_empty_segments():
    lines = ["# Kapitel 9 — X", "", "erste zeile", "", "---", "", "", "---", "zweite", ""]
    scenes = proj.split_scenes(lines, body_start=1)
    assert [body for _, body in scenes] == [["erste zeile"], ["zweite"]]
    # 1-based: "erste zeile" sits on line 3 of the file.
    assert scenes[0][0] == 3
    assert scenes[1][0] == 9


def test_find_body_start_skips_the_planning_header():
    lines = ["---", 'title: "x"', "---", "# Chapter 7", "## Summary", "s", "# Kapitel 7 — T", "p"]
    assert proj.find_body_start(lines) == 7
    assert proj.find_body_start(["# Chapter 7", "## Summary"]) is None


def test_slugify_transliterates_umlauts_and_bounds_length():
    assert proj.slugify("Genesis — Bewegung 1: Das Rauschen", "x") == "genesis-bewegung-1-das-rauschen"
    assert proj.slugify("Die Wächterin über Größe", "x") == "die-waechterin-ueber-groesse"
    assert proj.slugify("!!!", "fallback") == "fallback"
    assert len(proj.slugify("w" * 200, "x")) <= 60
