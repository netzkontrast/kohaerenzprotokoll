---
source: Sources/drive/romanidee-als-interaktiver-prototyp.md
drive_id: "1AhGr47Ue5p3TN17j6WtPvAGaUXi5Ml0svso6pLAnJX8"
title: "Romanidee als interaktiver Prototyp"
category: plot-outline
index_date: "2025-08-05"
extracted: "2026-10-06"
candidates: 95    # the terms capture.py counted
---

# Term census — Romanidee als interaktiver Prototyp

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py romanidee-als-interaktiver-prototyp`

```
  lines                303  (frontmatter ends at 9)
  body words           5995
  headings             22   bold-only lines 1
  table rows           13   code fences 0
  question marks       0
  backslash escapes    16
  typographic marks    145   ascii quotes 94
  invisible characters none
  math symbol lines    0
  glued ref numbers    13
  repeated labels      Interaktion x4, Szenario x4
  longest line         1075 chars
```

## Stance, read per passage

The document is a design proposal in four numbered parts, written in a consulting register that analyses and then recommends; it reports no events of its own. It names the text it draws on only as the reference „Outline“ ^[L302], and glued numbers `1` after its sentences point to that one reference, so the claims about the novel's world in part I are reports of that outline, not new statements.

**Part I, L18 to L90, an analysis of the novel's architecture.** The part opens by calling itself a „Dekonstruktion der Narrativen Architektur“ ^[L18] and says it produces the „Quellcodes“ of the narrative ^[L22]. It reads the conflict, the psyche of Kael, AEGIS, the two transcendent levels and the worlds, and ends each subsection with an interpretation of its own (for example that AEGIS' handling of Kael is a „Projektion seines eigenen, ungelösten inneren Paradoxons“ ^[L36], and that the Risse can be read as „Debugging- oder Korrekturversuche“ ^[L86] of AEGIS). Those readings are put as proposals: „Kaels Heilungsprozess kann als die Annahme einer parakonsistenten Logik“ ^[L48] modelled.

**Part II, L94 to L152, a specification.** It defines the Narrative Context Protocol as a server-side state tracker ^[L106], gives a matrix of variables in a table with its own caption ^[L118], and walks one example through five numbered steps (Input, State Change, Output Narrativ, Output Sensorisch, Output Systemisch, L146 to L150). The example is introduced as an illustration: „Ein konkretes Beispiel soll diesen Prozess verdeutlichen“ ^[L142].

**Part III, L156 to L257, a plan.** It announces itself as the „detaillierten, kapitelweisen Entwurf für den Prototyp“ ^[L160], names three gameplay loops ^[L188] and gives four chapter scenarios labelled `Szenario` and `Interaktion` under a heading that says „Auszug“ ^[L197], then a sensory design for KW1 and KW2 under the labels Visuell, Auditiv and Haptisch/Thermal. The scenario text is in the present tense and describes what the player does; it is a design, not a report.

**Part IV, L261 to L298, recommendations.** Labelled lines carry a priority, a technical challenge and an ethical challenge (`Priorität 1: Das NCP-Framework`, L273) and a guiding principle, „Leitprinzip“ ^[L295]. The ethical advice is a recommendation: „Es wird dringend empfohlen, Fachexperten“ ^[L276].

The document asks no questions (question marks: 0 in the profile) and carries no lock, sync or date of its own beyond the frontmatter.

## Candidates and counts

95 candidates, written while reading and frozen by the count (`Plan/runs/romanidee-als-interaktiver-prototyp/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `romanidee-als-interaktiver-prototyp.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `AEGIS` ^[romanidee-als-interaktiver-prototyp.md:#65] | 65 | 66 | 26, 30, 32, 34, 36, 44, 46, 48, 50, 54, 58, 60 … | `AEGIS-Agenten` ×1 |
| `Autonomous Entropic Gatekeeper for Integrity Systems` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 58 |  |
| `Kael` ^[romanidee-als-interaktiver-prototyp.md:#50] | 50 | 64 | 26, 30, 34, 36, 40, 44, 46, 48, 50, 58, 62, 70 … | `Kaels` ×14 |
| `System Kael` ^[romanidee-als-interaktiver-prototyp.md:#7] | 7 | 7 | 40, 44, 106, 108, 123, 124, 150 |  |
| `Nyx` ^[romanidee-als-interaktiver-prototyp.md:#8] | 8 | 8 | 88, 125, 144, 147, 223, 224, 233, 255 |  |
| `Lex` ^[romanidee-als-interaktiver-prototyp.md:#12] | 12 | 12 | 125, 144, 147, 148, 180, 206, 223, 224, 233 |  |
| `Kiko` ^[romanidee-als-interaktiver-prototyp.md:#9] | 9 | 12 | 88, 125, 132, 144, 146, 147, 180, 223, 224 | `Kikos` ×3 |
| `Rhys` ^[romanidee-als-interaktiver-prototyp.md:#4] | 4 | 4 | 132, 147, 148, 233 |  |
| `Alex` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 125 |  |
| `Selene` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 191 |  |
| `Juna/V` ^[romanidee-als-interaktiver-prototyp.md:#9] | 9 | 13 | 66, 70, 74, 76, 84, 88, 128, 132 | `Juna/V-Verbindung` ×2, `Juna/Vs` ×2 |
| `Juna/V-Verbindung` ^[romanidee-als-interaktiver-prototyp.md:#2] | 2 | 2 | 70, 74 |  |
| `Moonshine-Link` ^[romanidee-als-interaktiver-prototyp.md:#2] | 2 | 2 | 70, 74 |  |
| `Das Fundament` ^[romanidee-als-interaktiver-prototyp.md:#5] | 5 | 5 | 66, 70, 74, 76 |  |
| `Kernwelten` ^[romanidee-als-interaktiver-prototyp.md:#8] | 8 | 8 | 60, 74, 84, 86, 131, 179, 190, 284 |  |
| `KW1` ^[romanidee-als-interaktiver-prototyp.md:#10] | 10 | 10 | 84, 88, 131, 179, 193, 205, 237, 241, 274 |  |
| `KW2` ^[romanidee-als-interaktiver-prototyp.md:#7] | 7 | 7 | 84, 88, 124, 131, 193, 237, 251 |  |
| `KW3` ^[romanidee-als-interaktiver-prototyp.md:#2] | 2 | 2 | 84, 179 |  |
| `KW4` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 84 |  |
| `Logos-Prime` ^[romanidee-als-interaktiver-prototyp.md:#2] | 2 | 2 | 84, 241 |  |
| `Mnemosyne-Archipel` ^[romanidee-als-interaktiver-prototyp.md:#2] | 2 | 2 | 84, 251 |  |
| `Cerberus-Labyrinth` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 84 |  |
| `Kairos-Potentialis` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 84 |  |
| `Überwelt` ^[romanidee-als-interaktiver-prototyp.md:#4] | 4 | 4 | 74, 84, 228, 232 |  |
| `Externe Ebene` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 84 |  |
| `Konstrukt-Stadt` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 201 |  |
| `Risse` ^[romanidee-als-interaktiver-prototyp.md:#16] | 16 | 18 | 32, 84, 86, 90, 128, 131, 149, 168, 180, 190, 193, 245 … | `Rissen` ×1, `Risses` ×1 |
| `Riss` ^[romanidee-als-interaktiver-prototyp.md:#6] | 6 | 25 | 32, 84, 86, 88, 90, 128, 131, 149, 168, 180, 190, 193 … | `Risse` ×16, `Rissen` ×1, `Risses` ×1, `Riss-Interaktion` ×1 |
| `Datenriss` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 215 |  |
| `Guardians` ^[romanidee-als-interaktiver-prototyp.md:#2] | 2 | 2 | 128, 129 |  |
| `Guardian` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 3 | 128, 129, 150 | `Guardians` ×2 |
| `Archivar` ^[romanidee-als-interaktiver-prototyp.md:#2] | 2 | 2 | 210, 214 |  |
| `Wächter-Programm` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 232 |  |
| `Innerer Rat` ^[romanidee-als-interaktiver-prototyp.md:#2] | 2 | 2 | 191, 298 |  |
| `Inneren Rat` ^[romanidee-als-interaktiver-prototyp.md:#2] | 2 | 2 | 124, 144 |  |
| `Inneren Konferenzraum` ^[romanidee-als-interaktiver-prototyp.md:#2] | 2 | 2 | 191, 223 |  |
| `Paradoxon der Fehlausgerichteten Kohärenz` ^[romanidee-als-interaktiver-prototyp.md:#2] | 2 | 2 | 32, 58 |  |
| `Nichts Rauschen` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 2 | 34, 58 |  |
| `funktionale Multiplizität` ^[romanidee-als-interaktiver-prototyp.md:#3] | 3 | 3 | 30, 124, 285 |  |
| `funktionalen Multiplizität` ^[romanidee-als-interaktiver-prototyp.md:#2] | 2 | 2 | 46, 50 |  |
| `Zero Trust Environment Mandate` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 58 |  |
| `ZTEM` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 2 | 58, 60 | `ZTEM-Protokoll` ×1 |
| `Recursive Trust Signature Verification` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 58 |  |
| `RTSV` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 58 |  |
| `Systemic Isolation Shield` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 60 |  |
| `SIS-Protokoll` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 60 |  |
| `algorithmische Melancholie` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 128 |  |
| `Paradoxon X` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 128 |  |
| `analytischen Angriff` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 34 |  |
| `informationstheoretischer Schock` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 60 |  |
| `Ur-Trauma` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 60 |  |
| `ontologischer Exploit` ^[romanidee-als-interaktiver-prototyp.md:#2] | 2 | 2 | 48, 70 |  |
| `Spielphysik` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 74 |  |
| `Spiel-Engine` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 76 |  |
| `Anziehungsbecken` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 70 |  |
| `Anscheinend Normale Persönlichkeitsanteile` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 44 |  |
| `Emotionale Persönlichkeitsanteile` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 44 |  |
| `ANPs` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 44 |  |
| `EPs` ^[romanidee-als-interaktiver-prototyp.md:#2] | 2 | 2 | 44, 255 |  |
| `ANP-EP-Phobien` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 44 |  |
| `Anteile` ^[romanidee-als-interaktiver-prototyp.md:#15] | 15 | 19 | 34, 36, 44, 46, 124, 125, 132, 144, 178, 191, 223, 233 … | `Anteilen` ×4 |
| `Alters` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 44 |  |
| `Ko-Bewusstsein` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 2 | 124, 125 | `Ko-Bewusstseins` ×1 |
| `Psycho-Architekturen` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 84 |  |
| `Narrative Context Protocol` ^[romanidee-als-interaktiver-prototyp.md:#5] | 5 | 5 | 94, 98, 106, 118, 273 |  |
| `NCP` ^[romanidee-als-interaktiver-prototyp.md:#14] | 14 | 18 | 94, 98, 106, 108, 118, 134, 142, 146, 147, 160, 178, 179 … |  |
| `Key-Variable-Matrix` ^[romanidee-als-interaktiver-prototyp.md:#3] | 3 | 3 | 112, 118, 273 |  |
| `Kael.System.Cohesion` ^[romanidee-als-interaktiver-prototyp.md:#8] | 8 | 10 | 124, 126, 129, 134, 147, 150, 179, 192, 224, 233 | `Kael.System.Cohesion-Wert` ×2 |
| `Kael.Alter.Dominance` ^[romanidee-als-interaktiver-prototyp.md:#8] | 8 | 8 | 125, 147, 178, 206 |  |
| `Kael.Symptom.Amnesia` ^[romanidee-als-interaktiver-prototyp.md:#2] | 2 | 2 | 124, 126 |  |
| `AEGIS.System.Integrity` ^[romanidee-als-interaktiver-prototyp.md:#4] | 4 | 4 | 128, 131, 149, 284 |  |
| `AEGIS.Intervention.Level` ^[romanidee-als-interaktiver-prototyp.md:#4] | 4 | 4 | 129, 134, 150, 179 |  |
| `World.Stability` ^[romanidee-als-interaktiver-prototyp.md:#3] | 3 | 3 | 128, 131, 149 |  |
| `World.Stability.Risse` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 128 |  |
| `JunaV.Connection.Strength` ^[romanidee-als-interaktiver-prototyp.md:#2] | 2 | 2 | 129, 132 |  |
| `Single Source of Truth` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 106 |  |
| `Interne Verhandlung` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 191 |  |
| `Riss-Interaktion` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 193 |  |
| `Polyphone Prosa` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 178 |  |
| `Vulnerablen Narration` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 296 |  |
| `System-Shutdown` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 224 |  |
| `Meta-Wahrnehmung` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 284 |  |
| `logischer Kampf` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 285 |  |
| `Algorithmic Horror` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 129 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Tertiären Strukturellen Dissoziation der Persönlichkeit` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 44 |  |
| `TSDP` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 44 |  |
| `lebenden Gödel-Satz` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 50 |  |
| `Gödel-Sätzen` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 128 |  |
| `dialetheischen Geistes` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 48 |  |
| `seltsamer Attraktor` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 70 |  |
| `Quantenverschränkung` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 70 |  |
| `Environmental Storytelling` ^[romanidee-als-interaktiver-prototyp.md:#3] | 3 | 3 | 84, 179, 274 |  |
| `Gaslighting` ^[romanidee-als-interaktiver-prototyp.md:#3] | 3 | 5 | 36, 58, 62, 129, 150 | `Gaslighting-Versuchen` ×1, `Gaslighting-Versuch` ×1 |
| `Hamartia` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 1 | 58 |  |
| `autopoietische` ^[romanidee-als-interaktiver-prototyp.md:#1] | 1 | 2 | 30, 58 | `autopoietisches` ×1 |

## What the extraction ran into

Explanation of the facts below. There are no zeros: every candidate was written as the document writes it and each was asked with `read.py --find` before the count. Where a term stands alone less often than with compounds, the difference is inflection or a joined compound, not a second sense. `Riss` ^[romanidee-als-interaktiver-prototyp.md:#6] is mostly the plural: the `in` column of its row also holds `Risse`, `Rissen`, `Risses` and the compound `Riss-Interaktion`, and `Risse` is the main surface. `Kael` stands as the genitive `Kaels` and `Kiko` as `Kikos`; `AEGIS` appears in the compound `AEGIS-Agenten`; `Juna/V` stands as `Juna/Vs` and inside `Juna/V-Verbindung`, which is listed as its own row; `Guardian` stands inside `Guardians`, a surface the table writes in the variable rows (L128, L129) and once as `Guardian` in the example (L150); `Anteile` also stands as the dative `Anteilen`; `NCP` and `Kael.System.Cohesion` are joined to other words (`Kael.System.Cohesion-Wert`); `Gaslighting` has the compounds `Gaslighting-Versuchen` and `Gaslighting-Versuch`; `autopoietische` stands once as `autopoietisches`.

**The table is flattened with escapes.** The key-variable matrix (L120 to L132) is a pipe table with backslash escapes, and the variable name `Kael.Alter.Dominance.\\\[Name\\\]` ^[romanidee-als-interaktiver-prototyp.md:#1] is written with escaped brackets, so it is not listed whole; the stem `Kael.Alter.Dominance` is, and so is `World.Stability` for the row `World.Stability.KW\\\[1-4\\\]`. The export also leaves a sentence of part I split over two lines (L70 and L72, the words `nicht als` then `*Deus ex Machina*`), a list that restarts after `<!-- end list -->` marks in part III, and 13 glued reference numbers, which are the single digit `1` after sentences and point to one reference entry.

**Surfaces.** The document writes `funktionale Multiplizität` and `funktionalen Multiplizität` (and once capitalised in a heading, L40), the inner council as `Innerer Rat`, `Inneren Rat` and `Inneren Konferenzraum`, and the first two realms with and without number (`KW1: Logos-Prime`, a label written `KW1: Logos-Prime 1:` in the export of L241). The four Kernwelten are named only in one parenthesis (L84), and only `Logos-Prime` and `Mnemosyne-Archipel` return as headings of part III E; `KW3` and `KW4` are not explained beyond their names, though the worlds KW1 and KW2 are described at length. The names Nyx, Lex, Kiko, Rhys and Alex stand in the variable table or the examples with one-phrase roles, and the document says there are eleven Anteile without naming the other six. Selene is named once as a later role of the player.

**What the document says of its own standing.** It calls the NCP the „Single Source of Truth“ ^[L106], a claim about the NCP in the proposed prototype, not about the document or the novel; this is recorded and applied to nothing. It cites a document „Leser“ and a `Plotentwurf` by name (L168, L284) and a `Projektkonzept` (L106) without quoting them: these are references to other texts, not claims the reading can check.

**Zeros:** 0.

**Standing alone less often than with compounds:** 15 — `AEGIS` 65/66, `Kael` 50/64, `Kiko` 9/12, `Juna/V` 9/13, `Risse` 16/18, `Riss` 6/25, `Guardian` 1/3, `Nichts Rauschen` 1/2, `ZTEM` 1/2, `Anteile` 15/19, `Ko-Bewusstsein` 1/2, `NCP` 14/18, `Kael.System.Cohesion` 8/10, `Gaslighting` 3/5, `autopoietische` 1/2.
