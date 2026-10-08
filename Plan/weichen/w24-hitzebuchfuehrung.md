---
id: W24
status: offen     # offen | beantwortet | vertagt | ersetzt — nur der Autor setzt beantwortet
hängt_ab_von: [W5, Schritt 43, Schritt 48, SP L9]
frage_art: schlüssel        # schlüssel | schalter | standard | vertagt
auslöser: "Durchsicht P3, S4, M4; Tabelle der Hitzegrößen: fünf Größen ohne Umrechnung"
empfehlung: "A"
---

# W24 — Die Hitzebuchführung: eine Währung, und warum die Uhr in Kap 35 abläuft

**Entscheidungsblatt, vorbereitet 2026-10-06.** Aus der kritischen Durchsicht (`Plan/runs/storyform-2026-10-06/kritische-durchsicht.md`, P3, S4, M4,
W-D) und der Tabelle der Hitzegrößen (`Plan/runs/storyform-2026-10-06/hitzegroessen.md`). Vorschlag, keine Festlegung. Kein Storyform-Wert ändert
sich; es geht um die Mechanik hinter B's Uhr.

## Was entschieden ist

- **B's Uhr ist das Abwärmebudget** (Schritt 43, Kanon Q8), ein Timelock, am Vortex aufgebraucht.
- **Die Zahlen** sind 71, 64, 47, 31, 9 und 0 % in Kap 0, 6, 16, 22, 28 und 35. Die Form ist deine, die Werte sind ein
  Vorschlag (Schritt 48).
- **Beat 4,** die Landauer-Hitze, liegt in Kap 35 (Schritt 48).

## Was die Tabelle zeigt

- **Fünf Größen, keine Umrechnung zwischen ihnen:**
  - die Abwärme einer Zeile in Joule, aus Bit nach Landauer;
  - das Abwärmebudget eines Sektorfensters in Joule (Entwurf J);
  - die Vorkühlung in °C;
  - AEGIS' Reserve in Prozent;
  - Kaels Landauer-Hitze ohne Einheit (Kap 31).
- **Dasselbe Wort, zwei Größen:** „Abwärmebudget“ steht in Entwurf J für die Sektorgröße und überall sonst für AEGIS'
  Prozent-Uhr. Ein Hard-SF-Leser hält beides für dasselbe und rechnet.
- **Die Rechnung der Entwürfe stimmt genau:** kT ln 2 bei 20,1–21,0 °C mal 2,2 × 10²⁹ Bit ergibt 6,17–6,19 × 10⁸ J,
  und J schreibt 6,18 × 10⁸ J. Die Stadt löscht also exakt an der Landauer-Grenze, mit Wirkungsgrad 1. Der Text sagt das
  nirgends.
- **Kap 35 läuft rückwärts:** Kap 31 lässt Kaels inneres Löschen AEGIS' Budget senken. Wenn Oblivion in Kap 35 aufhört,
  müsste das AEGIS entlasten, und trotzdem steht das Budget „im selben Moment“ auf 0 %.
- **Die Uhr verhält sich wie ein Optionlock:** Sie fällt nur mit Sweeps, nie mit dem Kalender (S4). Die Welle in Kap 14,
  der größte Sweep in Akt II, hat keinen Wert.
- **Nach 0 % läuft B noch vier Kapitel weiter** (Kap 36–39).

## Die Optionen

- **A — Eine Währung, mit Kalender, Rückkehr und Überhitzung.**
  1. **Ein Name, zwei Ebenen.** „Abwärmebudget“ ist AEGIS' Reserve, die Wärme, die die Stadt insgesamt noch loswerden
     kann. Jedes Sektorfenster zieht seinen Anteil in Joule daraus. Die Zahl in J ist dann ein Abzug von der Uhr, nicht
     eine zweite Größe. Wie viel Joule 100 % sind, legt eine Zeile in `clock-b.json` fest.
  2. **Kalender.** Die Reserve fällt mit jedem geplanten Fenster, also mit der Zeit, und zusätzlich mit jedem Sweep. Damit
     ist die Uhr ein echter Timelock (S4). Die Wartungsfenster werden dichter, wie die Forewarnings sagen.
  3. **Rückkehr.** Was nicht bestätigt wird, kommt zurück, wie die 251 in Entwurf A von Kap 2: „Ein Ausgleich, der
     zurückkommt, ist kein Ausgleich.“ Jedes erneute Löschen kostet erneut.
  4. **Kap 31.** Kaels inneres Löschen läuft auf demselben Substrat und kostet dieselbe Reserve. Darum sinkt sie.
  5. **Kap 35.** Kael bestätigt Oblivions Löschung nicht mehr. Was Oblivion gelöscht hat, kehrt zurück, und AEGIS'
     Sweep löscht gegen etwas, das immer wiederkommt. Der Sweep verbrennt den Rest. **Die beiden Wenden hängen durch ein
     Weil zusammen.**
  6. **Kap 36–39.** Bei 0 % endet AEGIS nicht, es beginnt zu überhitzen. Was es nicht mehr abführen kann, kommt in Kap 38
     als Rauschen herein. B läuft bis Kap 39, weil Sterben Zeit braucht.
- **B — Zwei Größen.** Kaels Landauer-Hitze gehört ihm, und AEGIS' Reserve fällt nur durch Sweeps. Dann kostet Kap 31
  AEGIS nichts, und das gleichzeitige Ende in Kap 35 bleibt Zufall.
- **C — Wie jetzt.** P3 bleibt, und die Hard-SF-Leser rechnen gegen das Buch.

## Empfehlung

**A.** Die Mechanik steht schon in den Entwürfen (die 251, die Vorkühlung als Kalender). Sie wird nur zur Regel. Zwei
Folgen:
- **W5:** Die Empfehlung dort bleibt. Löschwärme hat eine Zahl, Junas Wärme keine.
- **Sperre L9:** Kap 31 zeigt Löschwärme. Beat 4 bleibt der Moment, in dem die Reserve leer ist.

**Der Wirkungsgrad 1** ist eine Weltregel, die du festhalten könntest: Die Stadt rechnet an der physikalischen Grenze.
Das ist ein stiller Hinweis, dass ihr Substrat keine gewöhnliche Maschine ist.

## Was es ändert

- **Werte:** `clock-b.json`, dazu eine Zeile „100 % = … J“ und vielleicht ein Wert im Kalender.
- **Kapitel:** Kap 14, 31, 33, 35, 36 und 38 in Treatment und `development.json`.
- **Entwürfe:** keine Änderung. Das Wort in J:L98 passt dann.

**Frage an dich:** Eine Währung, die mit dem Kalender und jedem Sweep fällt, mit Rückkehr des Unbestätigten (A)?
