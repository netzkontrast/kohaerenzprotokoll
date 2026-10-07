---
id: AL-01
titel: Kühlreserve
kapitel: 6
art: schutzmassnahme
redaktion: entwurf
lean: lean/AL01.lean
theoreme: [korrektur_schont_bewohner, ohne_eingriff_schaden, ohne_eingriff_trifft_0415, mit_eingriff_kein_ueberlauf, mit_eingriff_kein_schaden, entfernt_genau_die_alte_fassung, entfernt_ist_duplikat, begruendung_verloren]
kanon: []
---

# AL-01 — Kühlreserve

> Arbeitsentwurf einer Claude-Sitzung, 2026-10-07, auf den Auftrag des Autors, einen Lean-Piloten für AEGIS-Logs zu
> bauen. **Kein Kanon.** Die Kapitelstelle ist ein Vorschlag. Der Speicherdruck von Sektor 04 kommt aus Entwurf H
> (`kap-01/entwurf-h-radiator.md`: „KONSOLIDIERUNG NICHT VERSCHIEBBAR · SPEICHERDRUCK SEKTOR 04 · 99,7 %“), die
> Werte des Abwärmebudgets aus `Plan/storyform/clock-b.json`.

## Lesefassung

```
SEKTOR 04 · SPEICHERDRUCK 99,7 %
ZULAUF BIS FENSTER · 0,6 %
PROGNOSE 100,3 % · ÜBERLAUF
ZWANGSKONSOLIDIERUNG · ÄLTESTER BESTAND ZUERST · WE 0415

SWEEP · EIGENE PRÜFHISTORIE
PRÜFENTSCHEID 4471 · FASSUNG ZYKLUS 6 · ABGESCHLOSSEN
PRÜFENTSCHEID 4471 · FASSUNG ZYKLUS 2 · ABGESCHLOSSEN
SCHLÜSSEL GLEICH · STATUS GLEICH · DUPLIKAT
FASSUNG ZYKLUS 2 · ENTFERNT · 0,5 %

PROGNOSE 99,8 % · KEIN ÜBERLAUF
BEWOHNERBESTAND UNVERÄNDERT · WE 0415 UNVERÄNDERT
MASSNAHME WIRKSAM
ABWÄRMEBUDGET 64 %

BEGRÜNDUNG FASSUNG ZYKLUS 6 · LIEGT VOR
BEGRÜNDUNG FASSUNG ZYKLUS 2 · ich
BEGRÜNDUNG FASSUNG ZYKLUS 2 · NICHT REKONSTRUIERBAR
OFFEN · ANSCHLUSS OHNE PLANEINTRAG · DATENTYP —
```

## Formale Behauptung

Im Modell von Sektor 04 gilt für die lokale Korrektur `korrektur`:

1. Für **jede** Eintragsliste lässt die Korrektur alle Bewohnereinträge unverändert und in derselben Reihenfolge
   (`korrektur_schont_bewohner`).
2. Ohne Eingriff liefe der Sektor im Wartungsfenster über, und die Zwangskonsolidierung nähme WE 0415 ihren Eintrag
   (`ohne_eingriff_schaden`, `ohne_eingriff_trifft_0415`).
3. Nach dem Eingriff passt das Fenster in die Kapazität, und keine Wohneinheit verliert etwas
   (`mit_eingriff_kein_ueberlauf`, `mit_eingriff_kein_schaden`).
4. Der Eingriff entfernt genau einen Eintrag, die Fassung Zyklus 2 des Prüfentscheids 4471. Im Sinn von M1 ist sie
   ein Duplikat der bleibenden Fassung (`entfernt_genau_die_alte_fassung`, `entfernt_ist_duplikat`).
5. Die Begründung dieser Fassung kommt danach im Sektor nicht mehr vor (`begruendung_verloren`).

## Definitionen und Voraussetzungen

- **Modell.** Ein Sektor ist eine Liste von Einträgen, geordnet von neu nach alt. Ein Eintrag hat einen Halter
  (eine Wohneinheit oder AEGIS' Prüfhistorie), einen Schlüssel, einen Status, eine Begründung und einen Umfang in
  Promille der Kapazität. Die Kapazität ist 1000, der Zulauf bis zum Fenster 6.
- **M1, Duplikat:** gleicher Schlüssel und gleicher Status. **Die Begründung wird nicht verglichen.** Das ist die
  Voraussetzung, die den Verlust trägt.
- **M2, Zwangskonsolidierung:** Sie löscht ohne Ansehen des Halters den ältesten Eintrag, bis Belegung und Zulauf
  passen. Ob AEGIS' Welt so konsolidiert, ist eine Modellannahme, kein Kanon.
- **M3, Schaden:** Ein Bewohnereintrag geht verloren. Verluste der Prüfhistorie gelten nicht als Schaden.
- **S1, Zahlen:** Die sechs Einträge von Sektor 04 sind für diesen Entwurf gesetzt, mit 99,7 % Belegung aus Entwurf H.
- Keine `axiom`-Deklaration; alles Obige sind Definitionen in der Lean-Datei.

## Lean-Beweis

[`lean/AL01.lean`](lean/AL01.lean), Lean-Kern ohne Bibliothek, Version in [`lean/lean-toolchain`](lean/lean-toolchain).
Satz 1 ist ein Induktionsbeweis über beliebige Listen. Die Sätze 2–5 rechnen das konkrete Modell mit `decide` aus.
Was die Prüfung ergab und von welchen Axiomen jeder Satz abhängt, schreibt `scripts/aegis_logs.py verify` nach
`Plan/runs/aegis-logs/verifikation.json`.

## Reichweite und Ausgeblendetes

- **Bewiesen ist:** Im Modell schützt die Korrektur jeden Bewohnereintrag, und sie verhindert den Überlauf, der
  WE 0415 getroffen hätte. Diese Schutzwirkung ist echt, nicht nur behauptet.
- **Nicht bewiesen ist,** dass die entfernte Fassung entbehrlich war. Nach M1 ist sie ein Duplikat, ihrem Inhalt nach
  ist sie es nicht. Satz 5 zeigt, dass mit ihr eine Begründung verschwindet. Das Log nennt das zweimal, aber nicht
  als Schaden, weil M3 AEGIS' eigenes Gedächtnis nicht zählt.
- **Ausgeblendet:** das Abwärmebudget, das die Löschung kostet (71 → 64 % stehen nur in der Lesefassung); ob es eine
  dritte Maßnahme gab; was der Anschluss ohne Planeintrag ist. Die Zahlen sind gesetzt, nicht gemessen.

## Kapitel, Figurenhandlung und Storyform B

- **Kap 6, AEGIS als Ich (C14).** Das Treatment sagt: „Der erste Sweep gelingt lückenlos und verhindert einen
  Schaden“, und als Kosten „ein früherer Prüfentscheid“; `development.json` nennt für Kap 6 „zwei eigene Versionen“
  und „eine lokale Korrektur“. Das Log führt genau diese Handlung aus. Neu und nur Vorschlag sind Sektor 04 als Ort,
  WE 0415 und die Duplikat-Definition.
- **Figurenhandlung:** AEGIS opfert ein Stück eigener Prüfhistorie, um eine Wohneinheit zu schonen. Der Leser kann es
  bewundern. Das Ich rutscht genau an der Stelle hinein, an der die Begründung fehlt. Das ist der eine Riss, den die
  Stimmkarte für Kap 6 vorsieht.
- **Storyform B:** Story Costs Memory (der Prüfentscheid), MC Unique Ability Control (die lückenlose Korrektur),
  MC Concern Future (die Prognose). Der Beweis zeigt die Schutzwirkung und die Kosten zugleich. Das Log nennt nur die
  Schutzwirkung.

## Offen

- Ob Kap 6 einen Ort in KW1 braucht, der Sektor 04 heißt (Kap 1, 2 und 13 nennen ihn schon).
- Ob WE 0415 später wiederkehrt. AL-03 greift den verlorenen Schutzentscheid in Kap 28 wieder auf.
