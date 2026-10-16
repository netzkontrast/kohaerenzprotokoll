---
id: AL-02
titel: Umverteilung
kapitel: 13
art: umverteilte-loeschung
redaktion: entwurf
lean: lean/AL02.lean
theoreme: [summe_le, mindestens_betroffen, urspruenglich_unzulaessig, umverteilung_zulaessig, jeder_zulaessige_plan_trifft_sechs, preis]
kanon: []
---

# AL-02 — Umverteilung

> Arbeitsentwurf einer Claude-Sitzung, 2026-10-07, auf den Auftrag des Autors, einen Lean-Piloten für AEGIS-Logs zu
> bauen. **Kein Kanon.** Die Kapitelstelle ist ein Vorschlag. Die Konsole, WE 0418 mit offener Rückfrage und der
> Nachbar in WE 0419 kommen aus Entwurf J (`kap-01/entwurf-j-rueckfrage.md`) und Kap 2 A
> (`kap-02/entwurf-a-die-rolle-haelt.md`), die Schwelle aus Entwurf D (`kap-01/entwurf-d-umgebungslog.md`:
> „RESTWERT · TONFOLGE (2) · UNTER SCHWELLE · BELASSEN“). Alle drei sind Arbeitsentwürfe, keiner ist Kanon.

## Lesefassung

```
WARTUNG SEKTOR 04 · FENSTER 16:40 · SOLL 1,2 × 10¹⁸ BIT
POSTEN WE 0418 · 1,2 × 10¹⁸ BIT · RÜCKFRAGE OFFEN

VORSCHAU · BEI OFFENER RÜCKFRAGE
WE 0418 · GESPERRT · 0 BIT
UMVERTEILUNG · SCHWELLE 2,0 × 10¹⁷ BIT JE WOHNEINHEIT
WE 0403 · 2,0 × 10¹⁷ BIT · OHNE KATALOGEINTRAG
WE 0407 · 2,0 × 10¹⁷ BIT · OHNE KATALOGEINTRAG
WE 0411 · 2,0 × 10¹⁷ BIT · OHNE KATALOGEINTRAG
WE 0419 · 2,0 × 10¹⁷ BIT · OHNE KATALOGEINTRAG
WE 0423 · 2,0 × 10¹⁷ BIT · OHNE KATALOGEINTRAG
WE 0431 · 2,0 × 10¹⁷ BIT · OHNE KATALOGEINTRAG
SUMME 1,2 × 10¹⁸ BIT · SOLL ERREICHT
JE WOHNEINHEIT NICHT ÜBER SCHWELLE · ZULÄSSIG
BETROFFEN 6 · BISHER 1

[BESTÄTIGEN]  [RÜCKFRAGE]
```

## Formale Behauptung

Für ein Wartungsfenster mit Soll, Schwelle und gesperrter Wohneinheit heißt ein Löschplan zulässig, wenn er M1–M4
erfüllt. Dann gilt:

1. Für **jeden** zulässigen Plan, mit beliebigem Soll, beliebiger Schwelle und beliebiger Sperre, ist
   Soll ≤ Schwelle × Zahl der betroffenen Wohneinheiten (`summe_le`, `mindestens_betroffen`).
2. Konkret, mit Soll 12, Schwelle 2 und Sperre WE 0418: Der ursprüngliche Plan, der die Zeile von WE 0418 löscht,
   ist unzulässig. Die Umverteilung auf sechs Wohneinheiten ist zulässig
   (`urspruenglich_unzulaessig`, `umverteilung_zulaessig`).
3. **Jeder** zulässige Plan dieses Fensters trifft mindestens sechs Wohneinheiten, nicht nur der vorgeschlagene
   (`jeder_zulaessige_plan_trifft_sechs`).
4. Die Umverteilung löscht so viel wie der ursprüngliche Plan und trifft sechs Wohneinheiten statt einer (`preis`).

## Definitionen und Voraussetzungen

- **Modell.** Ein Plan ist eine Liste von Posten, ein Posten eine Wohneinheit und ein Umfang in Einheiten zu
  10¹⁷ Bit. Soll 12 (1,2 × 10¹⁸ Bit), Schwelle 2, gesperrt ist WE 0418.
- **M1, Deckung:** Die Summe des Plans erreicht das Soll.
- **M2, Schwelle:** Kein Posten liegt über der Schwelle. **Die Schwelle zählt Bits je Wohneinheit und Fenster, nicht
  was die Bits sind.** Das ist die Voraussetzung, die den Preis unsichtbar macht.
- **M3, Sperre:** Die Zeile mit offener Rückfrage bleibt unberührt.
- **M4, Einmaligkeit:** Jede Wohneinheit steht höchstens einmal im Plan. Ohne M4 könnte ein Plan eine Wohneinheit
  mehrfach unter der Schwelle treffen, und Satz 3 zählte Posten statt Menschen.
- **S1, Zahlen:** Soll, Schwelle und die sechs Wohneinheiten sind für diesen Entwurf gesetzt.
- Keine `axiom`-Deklaration; alles Obige sind Definitionen in der Lean-Datei.

## Lean-Beweis

[lean/AL02.lean](lean/AL02.lean), Lean-Kern ohne Bibliothek, Version in [lean/lean-toolchain](lean/lean-toolchain).
Satz 1 ist ein Induktionsbeweis über beliebige Pläne, Satz 3 folgt aus ihm mit `omega` für **alle** zulässigen Pläne
des Fensters. Die Sätze 2 und 4 rechnen die zwei konkreten Pläne aus.

## Reichweite und Ausgeblendetes

- **Bewiesen ist:** AEGIS' Zulässigkeit erzwingt die Verteilung. Wer die Sperre achtet und die Schwelle einhält, muss
  mindestens sechs Wohneinheiten treffen. Die Zahl der Betroffenen ist kein Zufall der Planung, sondern folgt aus M2.
  Je kleiner die Schwelle, desto mehr Menschen zahlen.
- **Nicht bewiesen ist,** dass „nicht über der Schwelle“ harmlos heißt. Was die zwei Einheiten von WE 0419 sind, weiß
  das Modell nicht. Entwurf J lässt den Mann in 0419 ein Lied verlieren, das Log sagt nur „OHNE KATALOGEINTRAG“.
- **Ausgeblendet:** Wiederholung. Die Schwelle gilt je Fenster. Nichts im Modell verhindert, dass dieselben sechs
  Wohneinheiten im nächsten Fenster wieder zahlen. Ebenso fehlt, ob die Sperre selbst Kosten hat.

## Kapitel, Figurenhandlung und Storyform B

- **Kap 13, Die offene RÜCKFRAGE.** Das Treatment sagt: „Das Wenn-dann lähmt ihn: Wer zahlt, wenn er nicht
  bestätigt?“ und „für die Wartung von Sektor 04 zahlen andere“. `development.json` nennt als Wendung: „Die Rückfrage
  bleibt offen, obwohl er den Preis nun kennt.“ Die Vorschau ist der Vorschlag, wie er ihn kennt: Sie steht auf
  seiner Konsole, bevor er nicht bestätigt. Kap 13 ist ein Kapitel von A, kein AEGIS-Ich-Kapitel. Das Log hat
  deshalb keinen Riss und kein Ich, es ist Anzeige wie in Entwurf D und J.
- **Figurenhandlung:** Kael sieht den Preis als Zahl, sechs statt eins, und unter den sechs die Tür neben seiner.
  Seine Weigerung wird dadurch eine Wahl mit Wissen (A-MC Critical Flaw Speculation, A Story Costs Being).
- **Storyform B:** Kap 13 trägt B-IC Concern Subconscious und B-RS Concern Becoming. AEGIS handelt hier als System,
  nicht als Ich: Es achtet die Sperre lückenlos (Control) und verteilt die Kosten so, dass jede einzelne Zeile korrekt
  ist. Die Schuld liegt nicht in einer Zeile, sondern in der Summe.

## Offen

- Ob die Vorschau so explizit sein darf oder ob Kael die Zahl erst in Kap 14 erfährt.
- Ob WE 0419 hier wieder zahlen soll. Das hängt an Entwurf J, der nicht freigegeben ist.
