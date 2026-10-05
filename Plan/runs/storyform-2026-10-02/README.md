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

Nicht berechnet: Signpost-Reihenfolge, Beziehung der Concerns untereinander, Plot-Story-Points jenseits ihrer Ebene. Die NCP-Dateien in `../plot-2026-09-30/ncp/` sind noch nicht neu gebaut.
