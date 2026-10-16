# AEGIS — Logs & Beweise

Ein Pilot, angelegt am 2026-10-07 auf deinen Auftrag: **AEGIS legitimiert Handlungen durch formal überprüfbare
Ableitungen.** Die Spannung liegt darin, dass eine korrekte Ableitung auf einer begrenzten Definition oder einer
fragwürdigen Voraussetzung stehen kann. Drei Logs, jedes mit einem Lean-Beweis. **Nichts hier ist Kanon**, und keine
Kapitelstelle ist entschieden.

| id | Log | Kapitel (Vorschlag) | Art | Die Voraussetzung, die trägt |
|---|---|---|---|---|
| AL-01 | [Kühlreserve](al-01-kuehlreserve.md) | Kap 6 | eine überzeugende Schutzmaßnahme | Duplikat heißt gleicher Schlüssel und Status, ohne Begründung; AEGIS' eigenes Gedächtnis ist kein Schaden |
| AL-02 | [Umverteilung](al-02-umverteilung.md) | Kap 13 | eine umverteilte Löschung mit menschlichem Preis | die Schwelle zählt Bits je Wohneinheit und Fenster, nicht was die Bits sind |
| AL-03 | [Offenlassen](al-03-offenlassen.md) | Kap 28 | eine erkannte, von AEGIS verweigerte Alternative | Beleg ist nur, was eine messende Quelle sagt; Schaden zählt nur an Bewohnern |

Wer Lean dafür erst lernen will: [Lean lernen mit Kael](tutorial/README.md), ein Tutorial in drei Lektionen entlang
der Outlines von Kap 1–3, geprüft wie die Logs.

## Wie ein Log gebaut ist

Jedes Log hat sechs Teile, in dieser Reihenfolge: die **Lesefassung** (so stünde es im Roman), die **formale
Behauptung**, die **Definitionen und Voraussetzungen**, den **Lean-Beweis** (ein relativer Verweis auf die Datei in
[lean/](lean/)), die **Reichweite** mit dem, was ausgeblendet bleibt, und den **Bezug** zu Kapitel, Figurenhandlung
und Storyform B. Der Kopf nennt:

```yaml
id: AL-01            # stabil; bleibt, auch wenn das Log das Kapitel wechselt
kapitel: 6           # Vorschlag, ein Kapitel aus Manuscript/plot/treatment.md
redaktion: entwurf   # entwurf | vorgelegt | freigegeben — freigegeben nur mit deinem Wortlaut in kanon.md
lean: lean/AL01.lean
theoreme: [...]      # die Sätze, die als geprüft gelten sollen
kanon: []            # ids aus kanon.md; leer heißt: nichts entschieden
```

## Zwei Status, getrennt

- **Redaktion** sagt, wie weit du das Log angenommen hast. Sie steht im Kopf und ändert sich nur mit dir.
- **Verifikation** sagt, ob Lean die genannten Sätze geprüft hat. Sie wird gemessen, nicht eingetragen:
  `python3 scripts/aegis_logs.py verify` lässt Lean laufen, fragt für jeden Satz `#print axioms` ab und schreibt das
  Ergebnis mit den Prüfsummen nach `Plan/runs/aegis-logs/verifikation.json`. Geprüft gilt ein Log nur, solange die
  Lean-Datei, `lean/lean-toolchain`, die formale Behauptung und die Voraussetzungen dieselben Prüfsummen haben. Ändert
  sich eins davon, zeigt die App **„geändert seit Prüfung“**. Die Lesefassung, die Reichweite und der Bezug dürfen sich
  ändern, ohne dass die Prüfung verfällt.

Ein Beweis gilt als geprüft, wenn Lean ihn ohne Fehler und ohne `sorry` annimmt, wenn die Datei kein `sorry`,
`admit`, `axiom`, `native_decide`, `implemented_by`, `extern` oder `unsafe` enthält, und wenn jeder Satz höchstens von Leans drei
Standardaxiomen abhängt (`propext`, `Quot.sound`, `Classical.choice`). Die Lean-Version steht in
[lean/lean-toolchain](lean/lean-toolchain); `scripts/install.sh lean` installiert genau sie.
