"""Tests for the lit-critic gate's non-LLM pipeline.

Everything except the lens run itself is covered here: reading findings back out
of the snapshot database, mapping them onto chapter lines, applying the blocking
policy and rendering the report. A synthetic snapshot stands in for the model, so
these tests need no API key and cost nothing.

    python3 .lit-critic-src/.venv/bin/pytest tests/test_lit_critic_gate.py

The gate imports lit-critic from the pinned checkout, so the whole module is
skipped when scripts/setup_lit_critic.sh has not been run.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import lit_critic_gate as gate  # noqa: E402

pytestmark = pytest.mark.skipif(
    not (ROOT / ".lit-critic-src/lit-critic-server.py").exists(),
    reason="lit-critic is not installed — run scripts/setup_lit_critic.sh",
)


@pytest.fixture(scope="module")
def lit_critic():
    return gate.load_lit_critic()


def finding(**overrides) -> dict:
    base = {
        "severity": "minor", "lens": "prose", "state": "active",
        "line_start": 7, "line_end": 7, "scene_file": "04.02_x.txt",
        "evidence": "e", "impact": "i", "options": [], "flagged_by": ["prose"],
        "number": 1, "location": "L007",
    }
    base.update(overrides)
    return base


# --------------------------------------------------------------------------
# Chapter selection
# --------------------------------------------------------------------------

def test_parse_chapters_accepts_numbers_lists_and_ranges():
    assert gate.parse_chapters(["4"]) == [4]
    assert gate.parse_chapters(["4,6"]) == [4, 6]
    assert gate.parse_chapters(["1-5"]) == [1, 2, 3, 4, 5]
    assert gate.parse_chapters(["7", "1-3", "7"]) == [1, 2, 3, 7]


def test_parse_chapters_rejects_nonsense():
    with pytest.raises(SystemExit):
        gate.parse_chapters(["vier"])
    with pytest.raises(SystemExit):
        gate.parse_chapters(["1-x"])


# --------------------------------------------------------------------------
# Blocking policy: critical blocks, horizon never does
# --------------------------------------------------------------------------

@pytest.mark.parametrize("severity,lens,blocks", [
    ("critical", "continuity", True),
    ("critical", "logic", True),
    ("critical", "horizon", False),      # horizon offers roads not taken, not defects
    ("major", "continuity", False),
    ("minor", "prose", False),
])
def test_blocking_policy(severity, lens, blocks):
    assert gate.is_blocking(finding(severity=severity, lens=lens)) is blocks


@pytest.mark.parametrize("state", ["silenced", "resolved"])
def test_inactive_findings_never_block(state):
    assert gate.is_blocking(finding(severity="critical", lens="logic", state=state)) is False


# --------------------------------------------------------------------------
# Location mapping and report rendering
# --------------------------------------------------------------------------

def test_attach_locations_points_at_the_chapter_line():
    scene = {
        "scene_file": "04.02_x.txt", "chapter_file": "Manuscript/…/04-pforten.md",
        "chapter_number": 4, "heading": "Kapitel 4, Szene 2",
        "body_start_chapter_line": 100, "body_start_scene_line": 6, "body_lines": 20,
    }
    findings = [finding(line_start=6, line_end=8), finding(scene_file="unknown.txt")]
    gate.attach_locations(findings, {"04.02_x.txt": scene})

    assert findings[0]["chapter_file"].endswith("04-pforten.md")
    assert findings[0]["chapter_number"] == 4
    assert findings[0]["chapter_line"] == 100        # first body line
    assert findings[0]["chapter_line_end"] == 102
    assert findings[1]["chapter_line"] is None       # unmapped scene, reported as such


def test_report_marks_blocking_findings_and_states_the_verdict():
    scene = {
        "scene_file": "04.02_x.txt", "chapter_file": "chapters/04-pforten.md",
        "chapter_number": 4, "heading": "Szene 2",
        "body_start_chapter_line": 100, "body_start_scene_line": 6, "body_lines": 20,
    }
    findings = [
        finding(severity="critical", lens="continuity", evidence="Ozon und Wärme in einer Szene"),
        finding(severity="minor", lens="horizon", evidence="kein Dialog"),
    ]
    gate.attach_locations(findings, {"04.02_x.txt": scene})
    report = gate.render_report(4, findings, "deep", {"checker_model": "sonnet", "frontier_model": "opus"})

    assert "BLOCKED" in report
    assert "1 blockierend" in report
    assert "⛔ [critical/continuity] chapters/04-pforten.md:101" in report
    assert "Ozon und Wärme in einer Szene" in report
    assert "· [minor/horizon]" in report          # reported, never blocking


def test_report_says_pass_when_nothing_blocks():
    report = gate.render_report(9, [], "quick", {"checker_model": "haiku"})
    assert "**PASS**" in report
    assert "Keine Findings." in report


# --------------------------------------------------------------------------
# The chapter-lint adapter: lint_chapter is the single rule encoding, and the
# gate consumes it rather than restating it.
# --------------------------------------------------------------------------

def test_chapter_lint_findings_arrive_pre_located():
    """lint_chapter reports chapter files and lines, so these skip scene mapping."""
    found = gate.chapter_lint_findings([1, 2])
    assert all(f["chapter_file"] for f in found)
    assert all(f["chapter_line"] for f in found)
    assert all(f["lens"] == gate.LINT_LENS for f in found)
    assert {f["chapter_number"] for f in found} <= {1, 2}


def test_attach_locations_leaves_pre_located_findings_alone():
    pre_located = {
        "scene_file": "", "line_start": None, "line_end": None,
        "chapter_file": "chapters/07-x.md", "chapter_number": 7, "chapter_line": 91,
    }
    gate.attach_locations([pre_located], {})
    assert pre_located["chapter_line"] == 91, "a chapter lint must not be re-mapped"
    assert pre_located["chapter_file"] == "chapters/07-x.md"


def test_lint_levels_map_onto_the_blocking_policy(monkeypatch):
    """VIOLATION blocks the gate; WARN is advisory."""
    import lint_chapter

    fake = [
        lint_chapter.Finding("chapters/04-x.md", 10, "VIOLATION", "ACT1-AEGIS", "m", "e"),
        lint_chapter.Finding("chapters/04-x.md", 12, "WARN", "R5-HEAT", "m", "e"),
    ]
    monkeypatch.setattr(lint_chapter, "lint_file", lambda path: fake)
    found = gate.chapter_lint_findings([4])
    by_code = {f["flagged_by"][1]: f for f in found}
    assert by_code["ACT1-AEGIS"]["severity"] == "critical"
    assert gate.is_blocking(by_code["ACT1-AEGIS"]) is True
    assert by_code["R5-HEAT"]["severity"] == "major"
    assert gate.is_blocking(by_code["R5-HEAT"]) is False
    assert [f["number"] for f in found] == [1, 2]


def test_act_one_is_lint_clean_through_the_gate():
    """Regression: Akt I carries no blocking chapter lint today."""
    found = gate.chapter_lint_findings(list(range(1, 14)))
    blocking = [f for f in found if gate.is_blocking(f)]
    assert blocking == [], "\n".join(f"{f['location']}: {f['evidence']}" for f in blocking)


# --------------------------------------------------------------------------
# End-to-end read-back through a real lit-critic database
# --------------------------------------------------------------------------

def test_collect_findings_reads_the_persisted_snapshot(lit_critic, tmp_path):
    """Write a snapshot exactly the way the engine does, then read it back."""
    _, get_connection, SnapshotStore, _, _, _ = lit_critic
    from core.domain import CoreFinding
    from orchestrator.services.snapshot_analysis_service import create_snapshot_from_core_findings

    project = tmp_path / "project"
    (project / "text").mkdir(parents=True)
    scene = project / "text" / "04.02_x.txt"
    scene.write_text("@@META\nPrev: None\nNext: TBD\n@@END\n\nProsa.\n", encoding="utf-8")

    conn = get_connection(project)
    try:
        create_snapshot_from_core_findings(
            conn,
            scene_paths=[str(scene)],
            findings_by_scene={str(scene): [
                CoreFinding(number=1, severity="critical", lens="continuity", location="L006",
                            line_start=6, line_end=6, evidence="ev", impact="im",
                            options=["o1"], flagged_by=["continuity", "logic"]),
                CoreFinding(number=2, severity="minor", lens="horizon", location="L006",
                            line_start=6, evidence="road not taken"),
            ]},
            depth_mode="deep", checker_model="sonnet", project_path=project,
        )
    finally:
        conn.close()

    findings, analysed, run_models = gate.collect_findings(
        SnapshotStore, get_connection, project, [scene]
    )
    assert len(findings) == 2
    assert analysed == 1
    # The report must state the run that produced the findings, not the config
    # that happens to be active now.
    assert run_models == {"mode": "deep", "checker_model": "sonnet", "frontier_model": ""}

    critical = next(f for f in findings if f["severity"] == "critical")
    assert critical["lens"] == "continuity"
    assert critical["scene_file"] == "04.02_x.txt"
    assert critical["line_start"] == 6
    assert critical["options"] == ["o1"]
    assert critical["flagged_by"] == ["continuity", "logic"]
    assert gate.is_blocking(critical) is True

    horizon = next(f for f in findings if f["lens"] == "horizon")
    assert gate.is_blocking(horizon) is False


def test_collect_findings_deduplicates_across_the_scene_set(lit_critic, tmp_path):
    """One snapshot covers every scene of a run; reading each must not duplicate it."""
    _, get_connection, SnapshotStore, _, _, _ = lit_critic
    from core.domain import CoreFinding
    from orchestrator.services.snapshot_analysis_service import create_snapshot_from_core_findings

    project = tmp_path / "project"
    (project / "text").mkdir(parents=True)
    scenes = []
    for index in (1, 2):
        scene = project / "text" / f"04.0{index}_x.txt"
        scene.write_text("@@META\nPrev: None\nNext: TBD\n@@END\n\nProsa.\n", encoding="utf-8")
        scenes.append(scene)

    conn = get_connection(project)
    try:
        create_snapshot_from_core_findings(
            conn,
            scene_paths=[str(s) for s in scenes],
            findings_by_scene={
                str(scenes[0]): [CoreFinding(number=1, severity="major", lens="prose",
                                             location="L006", line_start=6, evidence="a")],
                str(scenes[1]): [CoreFinding(number=2, severity="minor", lens="clarity",
                                             location="L007", line_start=7, evidence="b")],
            },
            depth_mode="deep", checker_model="sonnet", project_path=project,
        )
    finally:
        conn.close()

    findings, _, _ = gate.collect_findings(SnapshotStore, get_connection, project, scenes)
    assert len(findings) == 2
    assert {f["scene_file"] for f in findings} == {"04.01_x.txt", "04.02_x.txt"}


def test_collect_findings_is_empty_for_an_unanalysed_project(lit_critic, tmp_path):
    _, get_connection, SnapshotStore, _, _, _ = lit_critic
    project = tmp_path / "empty"
    project.mkdir()
    assert gate.collect_findings(SnapshotStore, get_connection, project, [project / "a.txt"]) == ([], 0, {})
