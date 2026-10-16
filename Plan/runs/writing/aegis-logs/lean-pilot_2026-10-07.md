# lean-pilot — AEGIS-Logs mit Lean-Beweis, eine Bewertung (2026-10-07)

**Auftrag:** einen kleinen Pilot für Lean als Beweisformat der literarischen AEGIS-Logs bauen, in die
Manuskript-UI einbinden und bewerten: Was gewinnt der Roman? Wo wird das Format schwer lesbar? Welche
Voraussetzungen tragen die problematischen Entscheidungen?

**Status:** Befund einer Claude-Sitzung, kein Kanon. Die drei Logs (`Manuscript/aegis-logs/`) sind
Arbeitsentwürfe. Keine Storyform-Zeile wurde geändert. Das Treatment ist unverändert; die Kapitelstellen
stehen nur in den Logs und sind dort als Vorschläge markiert.

## Was gebaut ist

| Log | Kap | Art | Bewiesen | Die tragende Voraussetzung |
|---|---|---|---|---|
| AL-01 Kühlreserve | 6 | Schutzmaßnahme | Die Korrektur schont jeden Bewohnereintrag (für jede Liste) und verhindert den Überlauf, der WE 0415 getroffen hätte. | Duplikat ohne Begründung; AEGIS' Gedächtnis zählt nicht als Schaden |
| AL-02 Umverteilung | 13 | umverteilte Löschung | Jeder zulässige Plan des Fensters trifft mindestens sechs Wohneinheiten (für alle zulässigen Pläne). | Die Schwelle zählt Bits je Wohneinheit und Fenster |
| AL-03 Offenlassen | 28 | verweigerte Alternative | Für jede Vertrauensregel: Offenlassen ist genau dann zulässig, wenn Mnemosyne oder dem Kanal geglaubt wird. | Nur messende Quellen belegen; Schaden zählt nur an Bewohnern |

Geprüft mit Lean 4.24.0, Kern ohne Bibliothek, kein `sorry`, keine eigene `axiom`. Die Sätze hängen höchstens
von `propext` und `Quot.sound` ab (`Plan/runs/aegis-logs/verifikation.json`). Jedes Log hat mindestens einen
Satz, der für alle Eingaben gilt, und mindestens einen, der einen konkreten modellierten Eingriff ausrechnet.

## Was der Roman gewinnt

- **AEGIS wird unschuldig im Bösen, und das ist nachprüfbar.** Die Stimmkarte will „unschuldig im Bösen“
  (Widerspruch A3). Mit Beweisen ist das keine Behauptung des Erzählers mehr: Jede Ableitung stimmt, und der
  Schaden steckt in einer Definition. AL-02 zeigt das am deutlichsten. Die sechs Betroffenen sind kein
  Planungsfehler, sondern folgen aus der Schwelle. Wer AEGIS widerlegen will, muss die Schwelle angreifen, nicht
  die Rechnung.
- **Storyform B bekommt eine Mechanik.** MC Problem Disbelief ist in AL-03 eine Zeile Code: `messend`. MC
  Solution Faith wäre eine andere Vertrauensregel, und Satz 1 sagt genau, welche. Dass AEGIS steadfast bleibt,
  heißt: Es ändert diese Regel nie. B endet in Failure, weil die Regel stimmt und trotzdem zu wenig sieht.
- **Die Risse der Stimme bekommen einen Ort.** In AL-01 rutscht das Ich genau dort hinein, wo der Beweis den
  Verlust zeigt und das Log ihn verschweigt. In AL-03 ist „WIDERSPRUCH IM BEFUND · 0“ eine korrekte Zahl, die nicht
  stimmt (Satz 5). Das ist die Stimmkarte (S3, „Zahlen, die nicht stimmen“), ohne dass AEGIS sich verrechnet.
- **Kontinuität, die eine Maschine hält.** AL-03 kann den Schutzentscheid aus AL-01 nicht mehr finden. Beide
  Logs teilen Sektor 04, und eine Zahl wie 99,7 % kommt aus einem Beweis, nicht aus dem Gedächtnis der Sitzung.
- **Kael bekommt eine Wahl mit Wissen.** In Kap 13 sieht er die Vorschau, sechs statt eins. Damit erfüllt das
  Log, was `development.json` für die Wendung verlangt: Die Rückfrage bleibt offen, obwohl er den Preis kennt.

## Wo das Format schwer lesbar wird

- **Die Lean-Ebene gehört nicht auf die Romanseite.** Kein Leser liest `theorem jeder_zulaessige_plan_trifft_sechs`.
  Was auf die Seite gehört, ist die Lesefassung. Die Werkstatt ist Material für dich, und für einen Anhang höchstens
  in Auszügen. Die App zeigt deshalb die Lesefassung zuerst und die Werkstatt nur auf Klick.
- **Die Lesefassung trägt nur, wenn sie den Beweis nicht nacherzählt.** Sobald das Log „BETROFFEN 6 · BISHER 1“
  schreibt, liegt die Pointe offen. Mehr Beweis im Log würde sie erklären und damit töten. Die Spannung entsteht im
  Abstand zwischen Log und Beweis, nicht im Beweis.
- **Die Form wiederholt sich schnell.** Drei Logs desselben Baus (Lage, Maßnahme, Ergebnis, Riss) tragen; zehn
  würden sich lesen wie ein Formular. Das Format gehört in wenige Wendepunkte, nicht in jedes AEGIS-Kapitel.
- **Zahlen verlangen Pflege.** Jede Zahl in der Lesefassung muss zum Modell passen (99,7 % = 997 von 1000,
  1,2 × 10¹⁸ = 6 × 2,0 × 10¹⁷). Der Prüfer vergleicht Lesefassung und Modell nicht; das ist bisher Handarbeit.
- **Die Modelle sind gesetzt, nicht gemessen.** Ein Beweis über ein selbstgebautes Modell beweist nichts über die
  Welt des Romans, solange die Welt nicht entschieden ist. Ein Leser, der das merkt, könnte das ganze Format für
  eine Täuschung halten. Die Abschnitte „Reichweite“ sind dagegen die Versicherung.

## Welche Voraussetzungen die problematischen Entscheidungen tragen

- **AL-01, M1 und M3:** Duplikat heißt gleicher Schlüssel und Status, die Begründung zählt nicht; AEGIS'
  eigenes Gedächtnis ist kein Schaden. Beides zusammen macht eine echte Schutzmaßnahme zum ersten Gedächtnisverlust
  (B Story Costs Memory).
- **AL-02, M2:** Die Schwelle zählt Bits je Wohneinheit und je Fenster. Sie misst nicht, was die Bits sind, und
  nicht, ob dieselben Menschen im nächsten Fenster wieder zahlen. Das Modell enthält keine Wiederholung; das ist
  die größte ausgeblendete Stelle des Piloten.
- **AL-03, M1 und M4:** Nur messende Quellen belegen, und Schaden zählt nur an Bewohnern. M1 verwirft die
  Alternative; M4 macht den Purge schadensfrei, obwohl er Juna trifft. Widersprechende Zeugnisse sind als Daten
  verschiedener Quellen modelliert. Lean muss deshalb nie P und ¬P zugleich annehmen, und AEGIS' Widerspruchsfreiheit
  wird zu einem berechneten Befund (Satz 5), nicht zu einer Logikfrage.

## Was offen ist (deine Entscheidungen)

1. Ob die Logs Beweise tragen sollen, also ob AEGIS' Legitimation durch Ableitung eine Regel des Buchs wird.
2. Ob die Kapitelstellen 6, 13 und 28 passen. Kap 13 ist ein Kapitel von A; das Log steht dort als Anzeige auf
   Kaels Konsole, nicht als AEGIS-Ich.
3. Ob die Werkstatt irgendwo im Buch erscheint (Anhang, Kapitelende) oder nur im Arbeitsplatz bleibt.
4. Ob AEGIS die Alternative in Kap 28 rechnen darf (C14: was das Ich wissen darf).
