"""Tests for the chapter-scoped canon locks.

Five of the seven locks never fire anywhere in the current manuscript, so
scanning the real chapters proves nothing about their patterns — a broken regex
and a clean manuscript look identical. Every lock therefore gets a synthetic
positive here, plus its scope boundary and, where the pattern is a collocation,
the everyday uses that must stay clean.

The Act-I regression at the end pins the manuscript's current state: if a later
draft breaks a lock, that test fails before the gate ever costs an API call.

    python3 -m pytest tests/test_lit_critic_locks.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import lit_critic_locks as locks  # noqa: E402
import lit_critic_project as proj  # noqa: E402

HEADER = "@@META\nPrev: None\nNext: TBD\n@@END\n\n"


def scene(chapter: int, index: int = 1) -> dict:
    return {
        "scene_file": f"{chapter:02d}.{index:02d}_x.txt",
        "chapter_file": f"chapters/{chapter:02d}-x.md",
        "chapter_number": chapter,
        "scene_index": index,
        "heading": "x",
        "body_start_chapter_line": 50,
        "body_start_scene_line": proj.BODY_START_SCENE_LINE,
        "body_lines": 4,
        "words": 10,
    }


def hits(chapter: int, prose: str) -> list[dict]:
    return locks.scan_scene(scene(chapter), HEADER + prose)


def slugs(chapter: int, prose: str) -> set[str]:
    return {f["flagged_by"][1] for f in hits(chapter, prose)}


# --------------------------------------------------------------------------
# Every lock fires on the thing it forbids
# --------------------------------------------------------------------------

@pytest.mark.parametrize("slug,chapter,prose", [
    ("dkt-terminology", 4, "Die Coheronen fallen aus dem Feld."),
    ("dkt-terminology", 4, "Ein Erason löscht den Rest."),
    ("dkt-terminology", 4, "Die Landauer-Grenze ist erreicht."),
    ("dkt-terminology", 4, "Das Kohärenzfeld bricht zusammen."),
    ("dkt-terminology", 4, "Der Wert η sinkt."),
    ("veil-clinical", 4, "Die Dissoziation setzt ein."),
    ("veil-clinical", 4, "Ein dissoziativer Zustand."),
    ("veil-clinical", 4, "Der ANP übernimmt."),
    ("veil-clinical", 4, "Die Diagnose lautet DID."),
    ("veil-clinical", 4, "Ein Alter-Ego meldet sich."),
    ("veil-collocation", 4, "Ein Anteil von mir bleibt stehen."),
    ("veil-collocation", 4, "Das Fragment in mir zählt weiter."),
    ("veil-collocation", 4, "Der Anteil spricht, bevor ich es kann."),
    ("veil-collocation", 4, "Ich bin ein Fragment eines größeren Ganzen."),
    ("veil-collocation", 4, "Einer meiner Anteile hält die Zahl."),
    ("aegis-named", 4, "AEGIS meldet die Abweichung."),
    ("kael-named-early", 4, "Kael steht auf."),
    ("juna-named", 4, "Juna ist die Wärme."),
    ("forbidden-sentence", 4, "Ich erinnere mich nicht."),
])
def test_lock_fires_on_its_own_violation(slug, chapter, prose):
    assert slug in slugs(chapter, prose), f"{slug} did not fire on: {prose!r}"


# --------------------------------------------------------------------------
# Scope boundaries — the chapter where each lock stops applying
# --------------------------------------------------------------------------

@pytest.mark.parametrize("slug,prose,last_banned,first_allowed", [
    ("kael-named-early", "Kael steht auf.", 8, 9),
    ("aegis-named", "AEGIS meldet die Abweichung.", 13, 14),
    ("veil-clinical", "Die Dissoziation setzt ein.", 12, 13),
    ("veil-collocation", "Ein Anteil von mir bleibt stehen.", 12, 13),
    ("dkt-terminology", "Die Coheronen fallen aus.", 13, 14),
    ("juna-named", "Juna ist die Wärme.", 13, 14),
    ("forbidden-sentence", "Ich erinnere mich nicht.", 13, 14),
])
def test_scope_boundary(slug, prose, last_banned, first_allowed):
    assert slug in slugs(last_banned, prose), f"{slug} must still apply in Kap {last_banned}"
    assert slug not in slugs(first_allowed, prose), f"{slug} must not apply in Kap {first_allowed}"


def test_kapitel_0_is_outside_every_lock():
    """Kap 0 is Genesis, not Akt I — the veil and the name locks do not reach it."""
    prose = "AEGIS. Kael. Juna. Ein Anteil von mir. Die Dissoziation."
    assert slugs(0, prose) == set()


# --------------------------------------------------------------------------
# The collocation rule must leave ordinary German alone
# --------------------------------------------------------------------------

@pytest.mark.parametrize("prose", [
    "Ein Anteil der Sequenzen bleibt offen.",
    "Das Systemhum liegt unter allem.",
    "Ich trage meinen Anteil an der Bestandspflege.",
    "Auf dem Boden liegen Fragmente von Glas.",
    "Das System der Aufzeichnungen bewahrt ihn.",
    "Der größte Anteil der Abweichungen ist korrigiert.",
])
def test_everyday_german_is_not_a_veil_breach(prose):
    assert "veil-collocation" not in slugs(4, prose), f"false positive on: {prose!r}"


# --------------------------------------------------------------------------
# Finding shape — the gate maps these like any other finding
# --------------------------------------------------------------------------

def test_finding_shape_matches_the_gate_contract():
    found = hits(4, "AEGIS meldet.\nNoch einmal AEGIS.")
    assert len(found) == 1, "one finding per lock per scene, not per hit"
    finding = found[0]
    assert finding["severity"] == "critical"
    assert finding["lens"] == locks.LENS
    assert finding["state"] == "active"
    assert finding["scene_file"] == "04.01_x.txt"
    assert finding["line_start"] == proj.BODY_START_SCENE_LINE
    assert finding["line_end"] == proj.BODY_START_SCENE_LINE + 1
    assert "«AEGIS»" in finding["evidence"] and "2×" in finding["evidence"]
    assert "drafting-brief" in finding["impact"]      # every lock cites its source
    assert finding["options"]


def test_scan_scenes_numbers_findings_sequentially(tmp_path):
    project = tmp_path / "project"
    (project / "text").mkdir(parents=True)
    scenes = []
    for index in (1, 2):
        s = scene(4, index)
        (project / "text" / s["scene_file"]).write_text(
            HEADER + "AEGIS meldet. Kael nickt.\n", encoding="utf-8"
        )
        scenes.append(s)
    found = locks.scan_scenes(scenes, project)
    assert [f["number"] for f in found] == [1, 2, 3, 4]


# --------------------------------------------------------------------------
# Regression: the manuscript as it stands today
# --------------------------------------------------------------------------

def test_act_one_is_lock_clean():
    """Akt I (Kap 1–13) currently honours every lock. Keep it that way."""
    manifest_path = ROOT / ".lit-critic/projection-manifest.json"
    if not manifest_path.exists():
        pytest.skip("no projection — run scripts/lit_critic_project.py")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    act1 = proj.scenes_for_chapters(manifest, list(range(1, 14)))
    assert act1, "Act I projected to nothing — the projection is broken"
    found = locks.scan_scenes(act1, ROOT / ".lit-critic/project")
    assert found == [], "\n".join(
        f"{f['scene_file']} L{f['line_start']}: {f['evidence']}" for f in found
    )
