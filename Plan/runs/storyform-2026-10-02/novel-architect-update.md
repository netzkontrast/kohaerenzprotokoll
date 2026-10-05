# Textbausteine: den `novel-architect`-Skill auf das Repository umstellen

**Entscheidung des Autors, 2026-10-05:** Das Repository `netzkontrast/kohaerenzprotokoll` ist die eine Quelle der
Plot-Struktur; der Skill führt keinen eigenen Kanon mehr, sondern zeigt hierher. Den Skill ändern und neu packen
kann nur der Autor (claude.ai, Skills). Die Bausteine unten ersetzen die genannten Stellen in `SKILL.md`; die
Kanon-Dateien des Skills werden zu Historie.

---

## 1. In `SKILL.md`, Abschnitt „Mission", Punkt 3 — ersetzen durch

> 3. **Strukturellen Kanon im Repository lesen, nicht hier halten.** Die Plot-Struktur — Storyform A und B mit
>    allen Werten, Herkunft je Wert, Besetzung, offenen Punkten — lebt im Repository `netzkontrast/kohaerenzprotokoll`
>    unter `Plan/storyform/` (`overview.md` zuerst, Quelle `a.json`/`b.json`, generiert `ncp/`). Warum jeder Wert so
>    ist: `Plan/decisions/025-dramatica-is-the-recipe.md`. Wie man ihn ändert: der Repo-Skill `storyform` (eine
>    Frage an den Autor nach der anderen; `python3 scripts/storyform.py` prüft und schreibt). Die Dateien unter
>    `references/canon/` und `canon-meta.md` sind der Stand vom 2026-05-03 — Historie, kein Kanon.

## 2. Abschnitt „Bootstrap-Protocol" — vor „Nach dem Workspace-Setup" einfügen

> **Repository zuerst.** Ist das Repository `netzkontrast/kohaerenzprotokoll` in der Sitzung verfügbar, liest der
> Bootstrap dort: `NOW.md`, `Plan/storyform/overview.md`, den Skill `.agents/skills/storyform/SKILL.md`. Die
> Reference-Files dieses Skills werden dann nur als Historie gelesen. Ist das Repository nicht verfügbar, sagt die
> Sitzung das und arbeitet nicht auf dem Stand vom 2026-05-03 weiter, als wäre er aktuell.

## 3. Abschnitt „Constraints" — die Zeilen „Canon-Hierarchy" und „NCP-Mutation NUR via ncp-author" ersetzen durch

> - **Canon-Hierarchy**: Entscheidungen des Autors, wie sie im Repository stehen (`Plan/decisions/`,
>   `Plan/storyform/`) > dieses Skill-Archiv > Memory > Training. Kein Datum und kein Anspruch, Kanon zu sein,
>   entscheidet etwas (Repo-Entscheidung 006).
> - **NCP wird generiert, nicht editiert**: `Plan/storyform/ncp/*.ncp.json` schreibt `scripts/storyform.py` aus
>   `a.json`/`b.json`, im Format des `ncp-author`-Skills. Eine Änderung geht in die JSON-Quelle, mit Herkunft.

## 4. Abschnitt „Constraints" — die Zeile „Story-First … Theorie ist Diagnose, kein Rezept" ersetzen durch

> - **Theorie als Rezept, Treatment als Kontrolle** (Weiche W1, Autor 2026-10-02): Das Treatment wird aus den
>   Storyforms geschrieben und danach gegen sie diagnostiziert. Widerspricht das Treatment der Storyform, ist das
>   eine Frage an den Autor, kein stilles Glätten in die eine oder andere Richtung.

## 5. `references/canon/README.md` — oben einfügen

> **Historie, Stand 2026-05-03.** Die geltende Fassung liegt im Repository unter `Plan/storyform/`. Was sich seither
> geändert hat und warum: `Plan/runs/storyform-2026-10-02/novel-architect-abgleich.md`.

---

**Was sich seit dem Skill-Stand geändert hat**, in einem Satz je Punkt: Approach getauscht (A Be-er, B Do-er —
Lock-in 2026-05-07, sonst sind beide Storyforms ungültig); A Growth Stop; beide MC-Ketten neu (Tafel und
Ableitung); IC von B ist Kael; fünf Guardians; Alter-Zahl offen; W1 = Rezept; Prämisse „Vielheit ist keine
Störung der Ordnung, sondern ihre Bedingung — und Liebe ist die Ordnung, die Vielheit trägt."; Besetzung A:
Selene Protagonist, Oblivion Antagonist.
