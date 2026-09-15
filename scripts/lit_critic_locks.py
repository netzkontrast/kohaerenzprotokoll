#!/usr/bin/env python3
"""Chapter-scoped canon locks — the decidable half of the prose gate.

lit-critic's own deterministic stage reads ``never use "X"`` rules out of
STYLE.md, but those rules are global. Ours are not: ``AEGIS`` is forbidden in
Act I and required from Kap 14, the Multiplizitäts-Schleier holds until it
falls, Kael is nameless until Kap 9. A global rule would fire across the whole
back half of the book, so the scoping lives here instead.

These checks are **lexical and decidable**: they prove a forbidden word is
absent. They cannot judge whether a required thing is present — no rule here
can tell you the ozone signature is missing or that R-2 was broken. That is
what the seven lenses are for. Keep it that way: a pattern that needs context
to judge belongs in the lenses, not in this file.

Every lock cites the canon source it encodes. Change the source first.

    python3 scripts/lit_critic_locks.py --chapter 1-13
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import lit_critic_project as proj  # noqa: E402

LENS = "canon-locks"


@dataclass(frozen=True)
class Lock:
    """One forbidden pattern, valid over an inclusive chapter range."""

    slug: str
    pattern: re.Pattern
    first_chapter: int
    last_chapter: int
    rule: str
    source: str
    impact: str
    options: tuple[str, ...]
    severity: str = "critical"

    def applies_to(self, chapter: int) -> bool:
        return self.first_chapter <= chapter <= self.last_chapter

    @property
    def range_label(self) -> str:
        if self.first_chapter == self.last_chapter:
            return f"Kap {self.first_chapter}"
        return f"Kap {self.first_chapter}–{self.last_chapter}"


# --------------------------------------------------------------------------
# The lock table
#
# Scopes confirmed with the author 2026-09-15:
#   - the Multiplizitäts-Schleier terms are banned through Kap 12; the veil
#     falls inside Kap 13, so Kap 13 is where they may first surface;
#   - the DKT ban runs the length of Akt I (Kap 1–13), per the drafting brief
#     §3 (2026-09-11), which supersedes the narrower "erste 50 Seiten" reading
#     in the Kap-0 annotation;
#   - a hit is critical and blocks the gate;
#   - the everyday words (Anteil, Fragment, System) are only flagged in
#     person-referring collocation, never bare.
# --------------------------------------------------------------------------

LOCKS: tuple[Lock, ...] = (
    Lock(
        slug="dkt-terminology",
        pattern=re.compile(r"\b(Coheron\w*|Erason\w*|Landauer\w*|Kohärenzfeld\w*)\b|(?<!\w)η(?!\w)"),
        first_chapter=1, last_chapter=13,
        rule="Keine DKT-Fachbegriffe in Akt I — nur Phänomenologie und diegetisches Vokabular.",
        source="Plan/drafting/drafting-brief.md §3; Canon/kap0-v1-annotiert.md R-6",
        impact="Benennt die Theorie, die Akt I nur als Erfahrung zeigen darf.",
        options=(
            "Den Vorgang sensorisch zeigen statt zu benennen.",
            "Diegetisches Vokabular verwenden: Konsolidierung, Ausgleich, Abweichung, "
            "Wartungsfenster, Bestand, Bestandspflege, Restwert, Ausnahme.",
        ),
    ),
    Lock(
        slug="veil-clinical",
        pattern=re.compile(r"\b(ANP|EP|TSDP|DID|Dissoziation|dissoziativ\w*|Alter-Ego)\b"),
        first_chapter=1, last_chapter=12,
        rule="R-3 — klinische Multiplizitäts-Terminologie fällt vor Kap 13 nicht.",
        source="Canon/kohaerenz-protokoll_welt-sensorik-drafting_2026-06-10.md §10.1 R-3",
        impact="Lüftet den Multiplizitäts-Schleier, bevor er in Kap 13 fällt.",
        options=("Den Wechsel über Syntaxbruch, Somatik und Lexikon zeigen, nie über den Begriff.",),
    ),
    Lock(
        slug="veil-collocation",
        # Only person-referring uses of the everyday words are a veil breach:
        # "ein Anteil von mir" is, "ein Anteil der Sequenzen" and "Systemhum"
        # are not.
        pattern=re.compile(
            r"\b(?:Anteil|Anteile|Anteilen|Fragment|Fragmente|Fragmenten|System|Systeme)\b"
            r"\s+(?:in|von)\s+(?:mir|ihm|ihr|uns)\b"
            r"|\b(?:Anteil|Fragment|System)\b\s+"
            r"(?:spricht|sprach|sagt|sagte|antwortet|antwortete|denkt|dachte|will|wollte|"
            r"übernimmt|übernahm|meldet|meldete)\b"
            r"|\bich\s+bin\s+(?:ein|eins?\s+der)\s+(?:Anteil|Fragment)\w*\b"
            r"|\b(?:einer|eins)\s+(?:meiner|der)\s+(?:Anteile|Fragmente)\b",
            re.IGNORECASE,
        ),
        first_chapter=1, last_chapter=12,
        rule="R-3 — Anteil/Fragment/System nicht in personenbezogener Verwendung vor Kap 13.",
        source="Canon/kohaerenz-protokoll_welt-sensorik-drafting_2026-06-10.md §10.1 R-3",
        impact="Macht die Vielheit benennbar, bevor der Schleier fällt.",
        options=("Die Präsenz als Körperempfinden, Lücke oder Stilbruch zeigen, nicht als Entität.",),
    ),
    Lock(
        slug="aegis-named",
        pattern=re.compile(r"\bAEGIS\b"),
        first_chapter=1, last_chapter=13,
        rule="Der Name AEGIS erscheint in Akt I nie im leserseitigen Text.",
        source="Plan/drafting/drafting-brief.md §3",
        impact="Gibt der Ordnungsinstanz einen Namen, den Akt I ihr verweigert.",
        options=(
            "VERSALIEN-Direktive, anonymes ORDNUNGSPROTOKOLL oder — nur in Kap 5 — "
            "subjektlose Funktions-Innensicht verwenden.",
        ),
    ),
    Lock(
        slug="kael-named-early",
        pattern=re.compile(r"\bKael\b"),
        first_chapter=1, last_chapter=8,
        rule="D-05 — Kaels Name erscheint erstmals in Kap 9.",
        source="Plan/drafting/decision-log_2026-09-11.md D-05; Plan/drafting/drafting-brief.md §3",
        impact="Nimmt der Namensnennung in Kap 9 ihre Wirkung.",
        options=("Den POV weiter namenlos führen; Bezeichnungen des Systems verwenden.",),
    ),
    Lock(
        slug="juna-named",
        # R-10's grammatical half (never a sentence subject) needs context and
        # stays with the lenses; only the name is decidable here. Scoped to
        # Akt I per the drafting brief, so Kap 38's direct appearance is clean.
        pattern=re.compile(r"\bJuna\b"),
        first_chapter=1, last_chapter=13,
        rule="R-10 — Juna ist in Akt I nie Name, nie Stimme, nie Körper; nur Wirkung.",
        source="Plan/drafting/drafting-brief.md §3; welt-sensorik §10.1 R-10",
        impact="Macht aus einer Wirkung eine Figur.",
        options=("Die Spur zeigen — hautwarm, quellenlos —, nie die Quelle benennen.",),
    ),
    Lock(
        slug="forbidden-sentence",
        pattern=re.compile(r"ich erinnere mich nicht", re.IGNORECASE),
        first_chapter=1, last_chapter=13,
        rule='Kaels Stimme sagt nie „ich erinnere mich nicht“.',
        source="Plan/drafting/drafting-brief.md §2",
        impact="Benennt die Amnesie, die Akt I nur als Lücke zeigen darf.",
        options=("Die Lücke als Absatz-Schnitt oder unerklärten Rest zeigen.",),
    ),
)


def scan_scene(scene: dict, scene_text: str) -> list[dict]:
    """Return lock findings for one projected scene, in the gate's finding shape.

    Line numbers are 1-based within the scene file (including the @@META
    header), matching what lit-critic's own findings use, so the gate maps
    them back to chapter lines the same way.
    """
    chapter = scene["chapter_number"]
    active = [lock for lock in LOCKS if lock.applies_to(chapter)]
    if not active:
        return []

    lines = scene_text.splitlines()
    findings: list[dict] = []
    for lock in active:
        hits: list[tuple[int, str]] = []
        for offset, line in enumerate(lines[proj.BODY_START_SCENE_LINE - 1:],
                                      start=proj.BODY_START_SCENE_LINE):
            for match in lock.pattern.finditer(line):
                hits.append((offset, match.group(0)))
        if not hits:
            continue
        terms = sorted({term for _, term in hits})
        findings.append({
            "number": 0,                       # renumbered by the caller
            "severity": lock.severity,
            "lens": LENS,
            "location": f"L{hits[0][0]:03d}",
            "line_start": hits[0][0],
            "line_end": hits[-1][0],
            "scene_file": scene["scene_file"],
            "evidence": (
                f"{lock.rule} Gefunden in {lock.range_label}: "
                + ", ".join(f"«{term}»" for term in terms)
                + f" ({len(hits)}×)."
            ),
            "impact": f"{lock.impact} Quelle: {lock.source}.",
            "options": list(lock.options),
            "flagged_by": [LENS, lock.slug],
            "state": "active",
        })
    return findings


def scan_scenes(scenes: list[dict], project_dir: Path) -> list[dict]:
    """Scan every projected scene and return numbered findings."""
    findings: list[dict] = []
    for scene in scenes:
        text = (project_dir / "text" / scene["scene_file"]).read_text(encoding="utf-8")
        findings.extend(scan_scene(scene, text))
    for number, finding in enumerate(findings, start=1):
        finding["number"] = number
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--chapter", action="append", metavar="N", required=True,
                        help="chapter number, list or range (repeatable): 4 · 4,6 · 1-13")
    parser.add_argument("--project", type=Path, default=proj.DEFAULT_OUT)
    args = parser.parse_args(argv)

    import lit_critic_gate as gate  # late import: only the CLI needs it
    chapters = gate.parse_chapters(args.chapter)
    manifest = proj.load_manifest(args.project)
    scenes = proj.scenes_for_chapters(manifest, chapters)
    findings = scan_scenes(scenes, args.project)

    active = {lock.slug for lock in LOCKS if any(lock.applies_to(c) for c in chapters)}
    print(f"{len(active)} lock(s) active over chapter(s) "
          f"{', '.join(map(str, chapters))}, {len(scenes)} scenes scanned")
    for finding in findings:
        print(f"  [{finding['severity']}] {finding['scene_file']} L{finding['line_start']}: "
              f"{finding['evidence']}")
    print(f"\n{len(findings)} lock violation(s)")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
