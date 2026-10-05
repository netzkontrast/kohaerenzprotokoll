# NCP 1.3.0 → 3.0.0-rc.1 — was der Fork des Autors ändert, mit einem Probelauf (2026-10-05)

**Gelesen:** `netzkontrast/narrative-context-protocol` auf `afa8d86` (2026-10-05, „Merge branch 'narrative-first:main'“),
als schreibgeschützter Klon. Verglichen mit dem Schema, das der `ncp-author`-Skill gepinnt hat (`0b9ab12`, 1.3.0),
gegen das unsere zwei Dateien validiert sind.

## Was NCP 3 ist

Eine **Schichtung**: Ein neutraler Kern (`core/ncp-core-schema.json`, `ncp_version: 3.0.0-rc.1`) mit `document`, `story`,
`profiles`, `extensions`, `payloads` trägt das Dramatica-Material als **Profil** (`profiles/dramatica/profile-schema.json`,
`dramatica:` 1.0.0-rc.1). Laut der Migrationsanleitung `governance/migration-2-to-3.md` wird das alte `story`-Objekt
**unverändert** nach `payloads["dramatica:"].storyform` kopiert. Der Validator prüft Kern und Profil getrennt und sagt bei
jedem Lauf, dass er nur die Struktur prüft, nicht ob eine Storyform gültig ist. Das entscheidet das lizenzierte
„Dramatica Semantic Model“, und diese Grenze sagt `profiles/dramatica/semantic-boundary.md` ausdrücklich.

## Das Delta, das für uns zählt

1. **Moments auf Story-Ebene, über mehrere Narratives** (`story.moments[]`, Definition `story_moment`). Jeder Verweis
   nennt `narrative_id`, und Moments dürfen Storybeats und Storypoints aus *beiden* Storyforms zugleich referenzieren. Im
   gepinnten 1.3.0 gibt es Moments nur innerhalb einer Narrative. **Das ist genau die Form unseres Weavings**: eine
   Datei mit A und B, und je Kapitel ein Moment, der die Stränge beider trägt. Eine Bridge wird dann zu einem Moment
   mit Verweisen in beide Narratives, statt zu zwei getrennten Moments in zwei Dateien.
2. **Moments auf Narrative-Ebene gibt es nicht mehr.** `narratives[].storytelling` kennt nur noch `overviews`. Ein
   Dokument im heutigen Format besteht die Fork-Validierung erst, wenn die Moments auf die Story-Ebene wandern.
3. **Zwei Appreciations heißen anders.** Aus „Main Character Evolution“ wird „MC Steadfast Expression“, aus „Influence
   Character Evolution“ wird „OC Steadfast Expression“. Wir benutzen keine von beiden.
4. **Story-Settings:** Neu ist ein optionales `story.settings[]` als Ortsglossar, auf das Moments mit `setting_id` zeigen.
   Das passt zu den Kernwelten, sobald sie entschieden sind (Q5).

## Probelauf (Scratchpad, nichts im Repo)

Aus den heutigen Dateien gebaut: **eine** Story mit beiden Narratives (A, B) und 41 Story-Moments aus `weave.json`, deren
Beat-Verweise je `narrative_id` tragen. Validiert mit `tests/validate-file.js` des Forks:

| Datei | Prüfung | Ergebnis |
|---|---|---|
| kombiniert, `schema_version: 1.3.0` (das eingefrorene Legacy-Schema des Forks) | Legacy | PASS |
| dieselbe Story im NCP-3-Umschlag (`payloads["dramatica:"]`) | Core | PASS |
| dieselbe | Dramatica-Profil | PASS |

Der erste Versuch scheiterte nur an Punkt 2 (Moments in `narratives[].storytelling`). Nach dem Verschieben bestanden alle
drei Prüfungen.

## Was eine Migration hier kosten würde

- `storyform.py` schreibt **eine** Datei statt zwei, und die Moments ziehen auf die Story-Ebene. Das sind etwa dreißig
  Zeilen. Der Validator des Skills (gepinnt auf 1.3.0) kennt `story.moments` nicht, daher müsste die Prüfung auf den
  Validator des Forks wechseln (ajv, `ajv/dist/2020`).
- `dsm_version` ist Pflicht. Ehrlich ausgefüllt hieße es: „Tafel von 1999, lokale Prüfung (nicht das lizenzierte DSM)“.
  Eine Zertifizierung ist das nicht und gibt es ohne die Plattform auch nicht. Du hast entschieden, ohne die Plattform zu
  arbeiten (2026-10-05).
- **Risiko:** Ein rc kann sich bis 3.0.0 noch ändern (`RELEASE_STATUS.md`, „What may change“). Der Skill `ncp-author` und
  der `novel-architect` auf claude.ai kennen nur 1.3.0.

## Offen — deine Entscheidung

Bleibt das Repo bei 1.3.0 mit zwei Dateien, oder wechselt es auf das Format deines Forks: eine Datei, Story-Moments, als
Legacy 1.3.0 oder gleich im 3.0.0-rc.1-Umschlag?
