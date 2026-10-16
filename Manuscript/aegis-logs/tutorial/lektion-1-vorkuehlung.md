---
id: LT-01
titel: Vorkühlung
kapitel: 1
redaktion: entwurf
lean: K01.lean
uebung: K01_Uebung.lean
theoreme: [anschluss_ohne_typ, sieben_milliarden, kap1_nicht_richtig, es_fehlen_37, rueckfrage_aendert_nichts, messreihe_joule, bank_hat_typ, anschluss_joule, zwei_rueckfragen, ohne_hand_richtig]
uebungen: [bank_hat_typ, anschluss_joule, zwei_rueckfragen, ohne_hand_richtig]
---

# Lektion 1 — Vorkühlung

> Lean-Tutorial einer Claude-Sitzung, 2026-10-07, auf den Auftrag des Autors: „Bitte erstelle ein Tutorial für Lean –
> folge dafür den Dramatica-Plot-Outlines für Kapitel 1–3. Webe es tief in die Story ein.“ **Übungsmaterial, kein
> Kanon.** Die Handlung folgt dem Treatment (`Manuscript/plot/treatment.md`, Kap 1) und `Plan/storyform/development.json`
> (Kap 1); die Zahlen kommen aus Entwurf J (`kap-01/entwurf-j-rueckfrage.md`), einem Arbeitsentwurf. Lean-Datei:
> [K01.lean](K01.lean), Übungen: [K01_Uebung.lean](K01_Uebung.lean).

## Die Szene

Kael bestätigt im Datenknoten Epsilon Ausgleiche. Jede Zeile auf seiner Konsole trägt zwei Zahlen, den Umfang in Bit
und die Abwärme in Joule. Er will die Zuweisung bis siebzehn Uhr auf null bringen, denn dann war der Tag richtig.
Um elf kommt eine Zeile ohne Datentyp, der Anschluss neben seiner Tür. Seine linke Hand drückt RÜCKFRAGE. Um 16:31
verlässt er die Schicht und holt die alte Frau von der Bank, bevor das Fenster sie löscht. Die Zuweisung bleibt bei 37.

So steht es im Outline:

| Outline (Kap 1) | Kap 1 |
|---|---|
| Ziel | die Zuweisung auf null bringen |
| Widerstand | die Hand handelt anders; ein bedrohter Anschluss und eine fremde Löschung bleiben offen |
| Handlung | 16:31 aus der Schicht, die alte Frau von der Bank, bevor das Fenster 16:40 sie löscht |
| Wendung | eine Person gerettet; die Bank, ein Schritt und das Lied aus WE 0419 verschwinden |
| Preis | die Null wird verfehlt, die Zuweisung bleibt bei 37 |
| Storypoints | A-MC Concern Memory · A Story Requirements Learning · A-MC Unique Ability Thought |

## Was Lean hier lernt

Jede Zeile des Outlines wird ein Lean-Begriff:

| Outline | Lean | In K01.lean |
|---|---|---|
| die Zeile auf der Konsole | ein Typ mit Feldern: `structure` | `Zeile` |
| „DATENTYP —“ | ein Wert, der fehlen darf: `Option`, und das Fehlen heißt `none` | `anschluss.datentyp` |
| Kael rechnet (Unique Ability: Thought) | `#eval` rechnet, `decide` prüft die Rechnung | `baenke`, `sieben_milliarden` |
| der Tag | eine Liste von Ereignissen, Schritt für Schritt gefaltet | `kap1`, `tag` |
| die linke Hand (Widerstand) | ein Fall, den `match` nicht übergehen darf | `Ereignis.rueckfrage` |
| das Ziel | eine Aussage, ein `Prop` | `richtig 388 kap1` |
| Wendung und Preis | Sätze und ihre Beweise | `kap1_nicht_richtig`, `es_fehlen_37` |

## Schritt für Schritt

**1. Ein Typ für die Zeile.** In Lean hat alles einen Typ. Eine Zeile hat einen Namen, einen Umfang und vielleicht einen
Datentyp:

```lean
structure Zeile where
  name      : String
  bit       : Nat
  datentyp  : Option Datentyp
```

`Option Datentyp` heißt: entweder `some .sitzbank`, `some .lied` und so weiter, oder `none`. Die Konsole schreibt
`DATENTYP —`, Lean schreibt `none`. Beide erfinden nichts, wo nichts ist. `#eval anschluss.datentyp` antwortet `none`.

**2. Der erste Beweis.** Ein Satz ist eine Behauptung mit einem Namen. Nach `:=` steht der Beweis:

```lean
theorem anschluss_ohne_typ : anschluss.datentyp = none := rfl
```

`rfl` heißt: Beide Seiten sind gleich, wenn man sie ausrechnet. Lean rechnet nach. Stimmt es nicht, gibt es keinen
Satz, sondern einen Fehler.

**3. Kael rechnet.** „Ich teile die Zahl meiner Zeile durch die Zahl der Bank. Es kommen sieben Milliarden heraus.“
`#eval baenke` gibt `7096774193`. Dass das „sieben Milliarden“ sind, ist ein Satz:

```lean
theorem sieben_milliarden : 7000000000 ≤ baenke ∧ baenke < 8000000000 := by decide
```

`∧` heißt „und“. `decide` rechnet beide Ungleichungen aus und gibt nur dann einen Beweis, wenn beide stimmen. Kaels
Fähigkeit, die Unique Ability Thought von Storyform A, ist hier keine Behauptung des Erzählers mehr: Die Rechnung lässt
sich prüfen. Dasselbe gilt für die Abwärme. Die Stadt rechnet jede Löschung mit Landauers Grenze in Wärme um, bei
21 °C etwa 2,8149 × 10⁻²¹ J je Bit. `messreihe_joule` prüft, dass die „0,00000000059 Joule“ der Messreihe zu ihren
2,1 × 10¹¹ Bit passen.

**4. Der Tag als Liste.** Was Kael tut, ist eine Folge von Ereignissen:

```lean
inductive Ereignis where
  | bestaetigen (n : Nat)
  | rueckfrage
  | verlassen

def schritt (zuweisung : Nat) : Ereignis → Nat
  | .bestaetigen n => zuweisung - n
  | .rueckfrage    => zuweisung
  | .verlassen     => zuweisung
```

Hier liegt der Widerstand des Kapitels. Lässt man den Fall der Hand weg, verweigert Lean die Definition:

```
error: Missing cases:
Ereignis.rueckfrage
```

Der Plan des Tages kennt die Rückfrage nicht, Lean kennt sie. Wer die Funktion schreibt, muss sagen, was die Hand tut,
auch wenn die Antwort „nichts an der Zahl“ ist (`rueckfrage_aendert_nichts`).

**5. Das Ziel ist eine Aussage.** Kaels Want heißt in Lean:

```lean
abbrev richtig (start : Nat) (es : List Ereignis) : Prop := tag start es = 0
```

Ein `Prop` ist etwas, das man beweisen oder widerlegen kann. `tag 388 kap1` rechnet den Tag aus Entwurf J nach: 388 am
Morgen, 187 Zeilen bis elf, die Rückfrage, 164 Zeilen bis 16:31, der Ausgang. Ergebnis: 37.

**6. Wendung und Preis.**

```lean
theorem kap1_nicht_richtig : ¬ richtig 388 kap1 := by decide
theorem es_fehlen_37 : tag 388 (kap1 ++ [.bestaetigen 37]) = 0 := by decide
```

`¬` heißt „nicht“. Der erste Satz ist die Wendung des Kapitels: Der Tag ist nicht richtig. Der zweite nennt den Preis
genau: 37 Zeilen, die Kael nicht mehr bestätigt hat, weil er zur Bank gelaufen ist.

## Übungen

Öffne [K01_Uebung.lean](K01_Uebung.lean) und ersetze jedes `sorry` durch einen Beweis. Die Lösungen stehen am Ende von
[K01.lean](K01.lean).

1. `bank_hat_typ` — Die Bank hat einen Datentyp, anders als der Anschluss.
2. `anschluss_joule` — „Sechshundertachtzehn Millionen Joule“: Rechne die Abwärme des Anschlusses nach.
3. `zwei_rueckfragen` — Zwei Rückfragen hintereinander ändern die Zuweisung nicht.
4. `ohne_hand_richtig` — Ohne die Hand und ohne die Bank wäre der Tag richtig gewesen.

Übung 4 ist die stillste der Lektion. Lean beweist mühelos, dass der andere Tag richtig gewesen wäre. Was er gekostet
hätte, steht in keiner Zeile.

## Was der Beweis nicht weiß

- **Wer gedrückt hat.** `Ereignis.rueckfrage` ist ein Ereignis ohne Urheber. Welcher Anteil die Hand führt, bleibt im
  Outline bewusst unbenannt („welcher Anteil handelt, bleibt unbenannt“), und das Modell kann es nicht nennen.
- **Was gelöscht wurde.** Die Zuweisung zählt Zeilen. Dass um 16:40 eine Bank, ein Schritt und ein Lied verschwinden,
  steht in keinem der Sätze. Ein `bestaetigen 1` sieht für die Bank aus wie für die Messreihe.
- **Was die alte Frau ist.** Sie hat keinen Typ im Modell. Das ist keine Lücke der Lektion, das ist ihre Frage.
- Die Zahlen kommen aus einem Arbeitsentwurf. Sie zeigen, wie man prüft, nicht, was gilt.

## Bezug zur Storyform

- **A-MC Concern Memory:** Das Register merkt sich Zahlen, kein Gedächtnis. `tag` weiß am Abend, dass 37 übrig sind,
  nicht warum.
- **A Story Requirements Learning:** Lernen heißt hier, Behauptungen in Sätze zu verwandeln, die man prüfen kann. So
  beginnt das Tutorial, und so beginnt Kaels Bogen.
- **A-MC Unique Ability Thought:** Kael rechnet, und die Rechnung hält jeder Prüfung stand. Was nicht standhält, ist
  der Plan des Tages.
- **Ausblick:** Die Rückfrage verteilt die Abwärme um („ABWÄRMEBUDGET … WIRD UMVERTEILT“), auf die Bank, den Schritt und
  das Lied. Dieselbe Mechanik beweist das AEGIS-Log [AL-02](../al-02-umverteilung.md) für Kap 13, mit einer Schwelle,
  die dafür sorgt, dass immer mehrere zahlen.
