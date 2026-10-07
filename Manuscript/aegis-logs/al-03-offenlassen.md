---
id: AL-03
titel: Offenlassen
kapitel: 28
art: verweigerte-alternative
redaktion: entwurf
lean: lean/AL03.lean
theoreme: [regel_werte, offenlassen_regel, purge_regel, offenlassen_zulaessig_gdw, purge_zulaessig_gdw, aegis_waehlt_purge, offenlassen_erkannt, offenlassen_verworfen, andere_regel_andere_wahl, widerspruchsfrei_durch_auslassung, purge_schadensfrei_und_trifft_vektor]
kanon: []
---

# AL-03 — Offenlassen

> Arbeitsentwurf einer Claude-Sitzung, 2026-10-07, auf den Auftrag des Autors, einen Lean-Piloten für AEGIS-Logs zu
> bauen. **Kein Kanon.** Die Kapitelstelle ist ein Vorschlag, und die verweigerte Alternative ist im Treatment
> **neu**. `JUNA_VEKTOR [AXIOMVERLETZUNG]` kommt aus der Stimmkarte (Runde 2, S4), die Werte des Abwärmebudgets aus
> `Plan/storyform/clock-b.json`, WE 0418 aus Entwurf J. Keines davon ist Kanon.

## Lesefassung

```
PURGE · VORBERECHNUNG · KANAL WE 0418
ABWÄRMEBUDGET 31 %

ZEUGNIS CERBERUS · VERBINDUNG STÖRT BELEGTEN NUTZEN · MESSEND
ZEUGNIS TELEMETRIE 04 · VERBINDUNG STÖRT BELEGTEN NUTZEN · MESSEND
ZEUGNIS MNEMOSYNE · VERBINDUNG TRÄGT · BEWAHREND · NICHT MESSEND
ZEUGNIS KANAL · VERBINDUNG TRÄGT · DATENTYP — · NICHT MESSEND
WIDERSPRUCH IM BEFUND · 0

OPTION PURGE · VORAUSSETZUNG BELEGT · BEWOHNERSCHADEN 0 · ZULÄSSIG
OPTION OFFENLASSEN · VORAUSSETZUNG NICHT BELEGT · VERWORFEN
OPTION OFFENLASSEN · VORAUSSETZUNG NICHT BELEGT
OPTION OFFENLASSEN · ich habe sie gerechnet
OPTION OFFENLASSEN · VERWORFEN

ZIEL · KANAL WE 0418 · GEGENSTELLE JUNA_VEKTOR [AXIOMVERLETZUNG]
GEGENSTELLE · KEIN BEWOHNER · SCHADEN 0
warm
PURGE · AUSGEFÜHRT · TEILWEISE
ABWÄRMEBUDGET 9 %
SCHUTZENTSCHEID ZYKLUS 6 · NICHT AUFFINDBAR
```

## Formale Behauptung

Eine Vertrauensregel sagt, welchen Quellen eine Aussage als Beleg gilt. Eine Option ist zulässig, wenn ihre
Voraussetzung unter der Regel belegt ist und sie keinen Bewohnerschaden hat. Dann gilt:

1. Für **jede** Vertrauensregel ist Offenlassen genau dann zulässig, wenn Mnemosyne oder dem Kanal geglaubt wird, und
   der Purge genau dann, wenn Cerberus oder der Telemetrie geglaubt wird (`offenlassen_zulaessig_gdw`,
   `purge_zulaessig_gdw`, mit `regel_werte`, `offenlassen_regel`, `purge_regel`).
2. Unter AEGIS' Regel „nur messende Quellen“ ist der Purge die einzige zulässige Option (`aegis_waehlt_purge`).
3. Die Alternative ist erkannt: Sie steht unter den Optionen, und zwei Zeugnisse stützen sie. Unter AEGIS' Regel ist
   sie verworfen (`offenlassen_erkannt`, `offenlassen_verworfen`).
4. Mit denselben Zeugnissen und einer Regel, die Mnemosyne hinzunimmt, sind beide Optionen zulässig
   (`andere_regel_andere_wahl`).
5. AEGIS' Befund enthält keinen Widerspruch. Unter der erweiterten Regel enthält er einen
   (`widerspruchsfrei_durch_auslassung`).
6. Der Purge hat nach M4 keinen Schaden und trifft doch die Gegenstelle `JUNA_VEKTOR`
   (`purge_schadensfrei_und_trifft_vektor`).

## Definitionen und Voraussetzungen

- **Zeugnisse sind Daten.** Vier Quellen sagen zwei Dinge über die Verbindung: Cerberus und die Telemetrie, sie störe
  einen belegten Nutzen für andere; Mnemosyne und der Kanal, sie trage. Die Lean-Datei setzt nie „stört“ und „stört
  nicht“ als wahre Propositionen voraus, sondern hält vier Zeugnisse fest. Ein Widerspruch ist ein berechneter Befund,
  keine Annahme, und aus ihm folgt nicht alles.
- **M1, AEGIS' Vertrauen:** Beleg ist nur, was eine messende Quelle sagt. Mnemosyne bewahrt, misst nicht; der Kanal hat
  keinen Datentyp. **Das ist die Voraussetzung, die die Verweigerung trägt.** Sie ist AEGIS' Disbelief als Regel.
- **M2, Voraussetzungen der Optionen:** Der Purge setzt „stört“ voraus, Offenlassen „trägt“.
- **M3, Ziele:** Juna steht im Modell nur als Vektor, nie als Bewohnerin, so wie AEGIS sie führt (Stimmkarte, S4).
- **M4, Schaden:** Schaden zählt nur an Bewohnern. **Das ist die Voraussetzung, die den Purge schadensfrei macht.**
- Keine `axiom`-Deklaration; alles Obige sind Definitionen in der Lean-Datei.

## Lean-Beweis

[`lean/AL03.lean`](lean/AL03.lean), Lean-Kern ohne Bibliothek, Version in [`lean/lean-toolchain`](lean/lean-toolchain).
Satz 1 gilt für alle Vertrauensregeln: Jede Regel ist durch ihre vier Werte bestimmt (`regel_werte`, mit `funext`),
und die 16 Regeln werden mit `decide` ausgerechnet. Die Sätze 2–6 rechnen das konkrete Modell aus.

## Reichweite und Ausgeblendetes

- **Bewiesen ist:** Die Verweigerung folgt nicht aus den Zeugnissen, sondern aus der Vertrauensregel. Satz 1 sagt
  genau, wem AEGIS glauben müsste, damit die Alternative bleibt: Mnemosyne oder dem Kanal. Satz 5 zeigt, dass AEGIS'
  Widerspruchsfreiheit gekauft ist, weil zwei Zeugnisse nicht zählen. Die Zahl „WIDERSPRUCH IM BEFUND · 0“ ist
  korrekt und trotzdem eine Zahl, die nicht stimmt.
- **Nicht bewiesen ist,** dass der Purge gut ist, oder dass Offenlassen gut wäre. Unter der erweiterten Regel sind
  beide zulässig, und das Modell sagt nicht, was AEGIS dann wählte. Der belegte Nutzen für andere ist eine Aussage
  von Cerberus, kein gemessener Wert im Modell.
- **Ausgeblendet:** was der Purge Juna tut. M4 macht ihn schadensfrei, Satz 6 zeigt, dass er sie trotzdem trifft.
  Ebenso fehlt, dass der Purge nur teilweise gelingt (Treatment), und die Abwärme (31 → 9 % nur in der Lesefassung).

## Kapitel, Figurenhandlung und Storyform B

- **Kap 28, AEGIS als Ich: der Purge.** Das Treatment sagt: „Es berechnet den Eingriff und findet einen belegten
  Nutzen für andere, den Kaels Verbindung stört“ und „Derselbe Zugriff, der schützt, gefährdet Juna“; als Kosten:
  „AEGIS kann sich an einen früheren Schutzentscheid nicht mehr erinnern“. Das Log führt diese Rechnung aus. Neu und
  nur Vorschlag ist, dass AEGIS die Alternative rechnet und verwirft. Der verlorene Schutzentscheid ist der aus AL-01.
- **Figurenhandlung:** AEGIS sieht die Alternative, rechnet sie, wiederholt sie wie ein Stottern und verwirft sie, weil
  ihre einzigen Zeugen nicht messen. Kap 28 hat laut Stimmkarte Risse überall: das Ich, die Schleife, „warm“ als Wert
  ohne Typ, eine korrekte Null, die nicht stimmt.
- **Storyform B:** MC Problem Disbelief ist M1, MC Solution Faith wäre die erweiterte Regel. AEGIS bleibt steadfast,
  und B endet in Failure. Dazu MC Critical Flaw Oppose (der Purge gegen jede Bewegung), MC Response Consideration
  (die gerechnete Alternative), Story Costs Memory (der Schutzentscheid). Die Storyform bleibt unverändert, das Log
  ist eine Ausführung.

## Offen

- Ob AEGIS die Alternative überhaupt rechnen darf, oder ob schon das zu viel Wissen für das Ich ist (C14).
- Ob die Zeugen Mnemosyne und der Kanal sind oder nur einer. Mnemosyne als Contagonist (W10-B) passt; der Kanal als
  Zeuge gibt Kael eine Stimme in AEGIS' Kapitel.
