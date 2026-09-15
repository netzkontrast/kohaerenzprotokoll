"""Tests for the R-3 veil rules in scripts/lint_chapter.py.

lint_chapter is the single encoding of the repo's decidable prose rules — the
post-tool-use hook runs it, and the lit-critic gate consumes it. The R-3 rules
were split and rescoped 2026-09-15 after the author confirmed: the veil terms
are banned through Kap 12 (the veil falls inside Kap 13), a clinical term is a
VIOLATION rather than a warning, and the everyday German words only block in
person-referring collocation.

These rules fire nowhere in the current manuscript, so scanning real chapters
proves nothing about them — a broken regex and a clean manuscript look
identical. Hence synthetic fixtures.

    python3 -m pytest tests/test_lint_chapter_rules.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import lint_chapter  # noqa: E402

FRONTMATTER = """---
type: novel.chapter
status: "drafted"
chapter_number: "{number}"
---

# Chapter {number}

## Outline
x

---

# Kapitel {number} — Test

{prose}
"""


def lint(tmp_path: Path, number: int, prose: str) -> list:
    path = tmp_path / f"{number:02d}-test.md"
    path.write_text(FRONTMATTER.format(number=number, prose=prose), encoding="utf-8")
    return lint_chapter.lint_file(path)


def codes(tmp_path: Path, number: int, prose: str) -> set[str]:
    return {f.code for f in lint(tmp_path, number, prose)}


def level_of(tmp_path: Path, number: int, prose: str, code: str) -> str | None:
    for finding in lint(tmp_path, number, prose):
        if finding.code == code:
            return finding.level
    return None


# --------------------------------------------------------------------------
# Clinical vocabulary — VIOLATION, Kap 1–12
# --------------------------------------------------------------------------

@pytest.mark.parametrize("prose", [
    "Die Dissoziation setzt ein.",
    "Ein dissoziativer Zustand hält an.",
    "Der ANP übernimmt.",
    "Die Diagnose lautet DID.",
    "Ein Alter-Ego meldet sich.",
    "Die Multiplizität ist messbar.",
])
def test_clinical_terms_are_violations_in_the_veil(tmp_path, prose):
    assert level_of(tmp_path, 4, prose, "ACT1-R3") == "VIOLATION"


def test_clinical_terms_stop_at_kapitel_13(tmp_path):
    prose = "Die Dissoziation setzt ein."
    assert "ACT1-R3" in codes(tmp_path, 12, prose), "must still apply in Kap 12"
    assert "ACT1-R3" not in codes(tmp_path, 13, prose), "the veil falls inside Kap 13"


# --------------------------------------------------------------------------
# Person-referring collocation — VIOLATION; everyday German — WARN only
# --------------------------------------------------------------------------

@pytest.mark.parametrize("prose", [
    "Ein Anteil von mir bleibt stehen.",
    "Das Fragment in mir zählt weiter.",
    "Der Anteil spricht, bevor ich es kann.",
    "Ich bin ein Fragment eines größeren Ganzen.",
    "Einer meiner Anteile hält die Zahl.",
    "Das System in mir meldet sich.",
])
def test_person_referring_use_is_a_violation(tmp_path, prose):
    assert level_of(tmp_path, 4, prose, "ACT1-R3-PERSON") == "VIOLATION"


@pytest.mark.parametrize("prose", [
    "Ein Anteil der Sequenzen bleibt offen.",
    "Das Systemhum liegt unter allem.",
    "Auf dem Boden liegen Fragmente von Glas.",
    "Der größte Anteil der Abweichungen ist korrigiert.",
])
def test_everyday_german_never_blocks(tmp_path, prose):
    """The bare words may WARN, but they must never be a VIOLATION."""
    found = lint(tmp_path, 4, prose)
    assert not [f for f in found if f.level == "VIOLATION"], \
        f"false blocking finding on: {prose!r}"


def test_bare_words_still_warn_as_a_safety_net(tmp_path):
    assert level_of(tmp_path, 4, "Ein Anteil der Sequenzen bleibt offen.",
                    "ACT1-R3-BARE") == "WARN"
    assert "ACT1-R3-BARE" not in codes(tmp_path, 13, "Ein Anteil der Sequenzen bleibt offen.")


# --------------------------------------------------------------------------
# The locks that were already there keep their scopes
# --------------------------------------------------------------------------

@pytest.mark.parametrize("code,prose,last_banned,first_allowed", [
    ("ACT1-AEGIS", "AEGIS meldet die Abweichung.", 13, 14),
    ("ACT1-DKT", "Die Coheronen fallen aus.", 13, 14),
    ("ACT1-JUNA", "Juna ist die Wärme.", 13, 14),
    ("NAME-KAEL", "Kael steht auf.", 8, 9),
])
def test_existing_scope_boundaries_are_unchanged(tmp_path, code, prose,
                                                 last_banned, first_allowed):
    assert code in codes(tmp_path, last_banned, prose)
    assert code not in codes(tmp_path, first_allowed, prose)


# --------------------------------------------------------------------------
# Regression: the manuscript as it stands today
# --------------------------------------------------------------------------

def test_every_chapter_is_lint_clean():
    """All 41 chapters pass. A future draft that breaks a rule fails here first."""
    findings = []
    for path in lint_chapter.target_files([]):
        findings.extend(lint_chapter.lint_file(path))
    violations = [f for f in findings if f.level == "VIOLATION"]
    assert violations == [], "\n".join(f.render() for f in violations)
