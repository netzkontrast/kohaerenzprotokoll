# Storyform-Prüfung — 2026-10-02/05

**Entscheidungen des Autors stehen in [Entscheidung 022](../../decisions/022-dramatica-is-the-recipe.md); dieses Verzeichnis hält das Werkzeug und die Spezifikationen.**

- `dramatica.py` — die Dramatica Table of Story Elements (Screenplay Systems, 1995/1999) als Daten, von Hand abgeschrieben, mit Selbsttest (`selftest`: 64 Elemente je Klasse, jedes Paar auf einer Diagonale, und der Checker muss die Quell-Storyform A ablehnen) und Prüfer (`check <spec>`, Regeln R1–R7 im Docstring). Gegen das Wörterbuch von 1995 gegengeprüft: 258 Paare, 0 Abweichungen (eine Meldung war ein Seitenumbruch-Artefakt).
- `specs/a-source.json`, `specs/b-source.json` — die Werte des Statusberichts vom 2026-05-07, unverändert: beide scheitern an R5 (Problem-Element nicht unter dem Concern).
- `specs/a1-avoid.json`, `specs/a2-memory.json` — die zwei Reparaturen, die dem Autor gezeigt wurden.
- `specs/a-author.json`, `specs/b-author.json` — der Stand nach den Antworten des Autors; beide `ok`.

```bash
python3 dramatica.py selftest
python3 dramatica.py check specs/a-author.json
python3 dramatica.py where Inertia
```

- `build_ncp.py` → `ncp/storyform-a.ncp.json`, `ncp/storyform-b.ncp.json`: NCP 1.3.0 nach dem `ncp-author`-Skill (Stufen 0, 2, 3, 5, 6), Status `draft` — vier Perspektiven, neun Dynamiken, die gewählten Storypoints, die vier OS-Signposts. Das Skript baut nicht, wenn `dramatica.check` einen Fehler findet; nicht Entschiedenes bleibt leer. Schema-Validator des Skills: PASS; Checkliste §8: keine Befunde. Acht Element-Namen schreibt NCP anders (Consider, Reconsider, Self Interest, Selflessness für Morality, …); die Abbildung steht im Skript.

Nicht berechnet: Signpost-Reihenfolge, Beziehung der Concerns untereinander, Plot-Story-Points jenseits ihrer Ebene. Die vorläufigen Dateien in `../plot-2026-09-30/ncp/` bleiben als Quellenposition stehen; diese hier lösen sie für die Arbeit ab.
