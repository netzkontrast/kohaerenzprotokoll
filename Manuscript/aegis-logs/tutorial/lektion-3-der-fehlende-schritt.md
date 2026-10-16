---
id: LT-03
titel: Der fehlende Schritt
kapitel: 3
redaktion: entwurf
lean: K03.lean
uebung: K03_Uebung.lean
theoreme: [fuss_gleich_kopf, ein_stueck_ein_schritt, zweihundertneun, nach_abgleich_kein_beleg, vorher_ein_beleg, nur_er_weiss, fuss_append, konsole_unveraendert, zwei_stuecke]
uebungen: [fuss_append, konsole_unveraendert, zwei_stuecke]
---

# Lektion 3 — Der fehlende Schritt

> Lean-Tutorial einer Claude-Sitzung, 2026-10-07, auf den Auftrag des Autors. **Übungsmaterial, kein Kanon.** Die
> Handlung folgt dem Treatment (Kap 3) und `development.json` (Kap 3). Für Kap 3 gibt es noch keinen Entwurf; die
> Zahlen kommen aus Entwurf J (210 Schritte, dann 209, „KORRIDOR DELTA-7 · ABSCHNITT 2 · 0,73 M“) und aus Kap 2 A
> (312 Schritte bis zur Konsole). Lean-Datei: [K03.lean](K03.lean), Übungen: [K03_Uebung.lean](K03_Uebung.lean). Setzt
> Lektion 2 voraus ([lektion-2-die-rolle-haelt.md](lektion-2-die-rolle-haelt.md)).

## Die Szene

Kael misst sein eigenes Register und die Schritte von der Bank bis zur Tür. Er findet ein Messzeichen, das er selbst
angelegt hat, ohne sich daran zu erinnern. Die Zeit stockt, und er findet sich am Boden eines Korridors. Ein Schritt
fehlt, 0,73 m. Er meldet den fehlenden Schritt nicht und trägt die Messung nicht ins Register ein. Danach kann er
seinem Arbeitsgedächtnis nicht mehr ganz trauen, und niemand außer ihm weiß von der Lücke.

| Outline (Kap 3) | Kap 3 |
|---|---|
| Ziel | die Lücke im eigenen Register finden |
| Widerstand | jeder erfolgreiche Abgleich entfernt einen Beleg des fehlenden Schritts |
| Handlung | den Korridor selbst vermessen; ein eigenes Messzeichen ohne Erinnerung |
| Wahl (Schritt 47) | den fehlenden Schritt nicht melden, die Messung nicht eintragen |
| Wendung | ein Befund, aber keine eindeutige Urheberschaft |
| Preis | dem Arbeitsgedächtnis nicht mehr ganz trauen; niemand sonst weiß es |
| Leser | Beleg und Schlussfolgerung bleiben unterscheidbar |
| Storypoints | A-MC Concern Memory · A Story Requirements Learning |

## Was Lean hier lernt

| Outline | Lean | In K03.lean |
|---|---|---|
| zweimal zählen, im Fuß und im Kopf | Rekursion, und ein Beweis durch Induktion | `fuss`, `fuss_gleich_kopf` |
| 0,73 m, ein Schritt | ein allgemeiner Satz, dann sein Einzelfall | `ein_stueck_ein_schritt`, `zweihundertneun` |
| der Abgleich entfernt den Beleg (Widerstand) | ein Satz über **alle** Register | `nach_abgleich_kein_beleg` |
| die Messung, die er nicht einträgt | ein Wert außerhalb des Registers | `kaels_messung`, `nur_er_weiss` |
| Beleg und Schlussfolgerung | Voraussetzung und Satz | die Form jedes `theorem` |
| was man nicht beweisen kann | `sorry`, und `#print axioms` verrät es | der Abschnitt „Die Lücke“ |

## Schritt für Schritt

**1. Zweimal zählen.** „Ich zähle jeden Schritt zweimal, einmal im Fuß und einmal im Kopf.“ (Kap 2, Entwurf A.) Der Fuß
zählt rekursiv, Schritt für Schritt. Der Kopf nimmt die Länge:

```lean
def fuss : List Schritt → Nat
  | []      => 0
  | _ :: xs => fuss xs + 1

def kopf (xs : List Schritt) : Nat := xs.length
```

Dass beide immer übereinstimmen, in jedem Korridor, beweist man durch Induktion: für den leeren Weg, und von einem Weg
auf denselben Weg mit einem Schritt mehr.

```lean
theorem fuss_gleich_kopf (xs : List Schritt) : fuss xs = kopf xs := by
  induction xs with
  | nil => rfl
  | cons x xs ih => simp [fuss, kopf, ih]
```

`ih` ist die Induktionsannahme: Für den kürzeren Weg stimmt es schon. Das ist der Satz, auf den sich Kap 3 stützt. Wenn
Kaels Zählen verlässlich ist, dann liegt die Abweichung nicht an ihm, sondern am Korridor.

**2. Ein Stück, ein Schritt.** Erst allgemein, für jede Schrittlänge `s > 0`:

```lean
theorem ein_stueck_ein_schritt (n s : Nat) (hs : 0 < s) :
    schritte (n * s - s) s = n - 1
```

Dann der Fall aus Kap 1: Kaels Schritt ist 73 cm, und die Stadt hat 0,73 m aus Abschnitt 2 ausgeglichen.

```lean
theorem zweihundertneun : schritte (210 * 73 - 73) 73 = 209 :=
  ein_stueck_ein_schritt 210 73 (by decide)
```

Ein allgemeiner Satz wird wie eine Funktion benutzt: Man gibt ihm die Zahlen und einen Beweis für die Voraussetzung
`0 < 73`. Hier wird der Unterschied zwischen **Beleg** und **Schlussfolgerung** sichtbar, den das Outline für den
Leser verlangt. `hs : 0 < s` ist eine Voraussetzung, `= n - 1` ist die Schlussfolgerung, und Lean hält beide getrennt.

**3. Der Abgleich löscht den Beleg.** Das ist der Widerstand des Kapitels, und er gilt für jedes Register:

```lean
theorem nach_abgleich_kein_beleg (register messung : List Nat) :
    abweichungen (abgleich register messung) messung = 0
```

Vorher gab es eine Abweichung (`vorher_ein_beleg`: das Register sagt 210, Kael misst 209). Nach dem Abgleich gibt es
keine mehr, und das nicht zufällig, sondern bewiesen, für alle Register. Die Stadt korrigiert nicht falsch. Sie
korrigiert richtig, und gerade deshalb bleibt nichts zurück.

**4. Was bleibt.** Kaels Messung ist ein Wert außerhalb des Registers:

```lean
def kaels_messung : Notiz := ⟨209, false⟩
theorem nur_er_weiss : kaels_messung.eingetragen = false ∧ kaels_messung.schritte ≠ 210 := by decide
```

Das ist seine Wahl im Modell. Der Satz sagt, dass es die Notiz gibt und dass sie nicht eingetragen ist. Er sagt nicht,
wer das Messzeichen gesetzt hat. Lean kennt keine Urheber, und das Outline verlangt genau das: einen Befund ohne
eindeutige Urheberschaft.

**5. Die Lücke.** Was passiert, wenn man einen Schritt nicht beweisen kann? In Lean schreibt man dann `sorry`:

```lean
theorem schritt_gezaehlt : 210 * 73 - 73 = 209 * 73 := by
  sorry
#print axioms schritt_gezaehlt
```

Lean nimmt das an, aber nicht stillschweigend:

```
warning: declaration uses 'sorry'
'schritt_gezaehlt' depends on axioms: [sorryAx]
```

Das ist der Kern der Lektion. Das Register der Stadt vergisst seine Lücken, denn der Abgleich entfernt sie. Lean vergisst
keine. Jeder Satz, der auf einer Lücke steht, trägt `sorryAx` in seinen Abhängigkeiten, auch jeder Satz, der ihn später
benutzt. Kael tut in Kap 3 das Gegenteil. Er weiß von der Lücke und trägt sie nicht ein. Seine Messung ist ein Beweis,
den nur er kennt, und er traut seinem eigenen Gedächtnis nicht mehr ganz. Darum prüft `scripts/aegis_logs.py verify`
jeden Satz dieses Tutorials mit `#print axioms`, und ein `sorry` ist nur in den Übungsdateien erlaubt.

## Übungen

Öffne [K03_Uebung.lean](K03_Uebung.lean) und ersetze jedes `sorry`. Die Lösungen stehen am Ende von [K03.lean](K03.lean).

1. `fuss_append` — Zwei Wege hintereinander: Der Fuß zählt so viel wie beide Wege zusammen. Deine erste eigene Induktion.
2. `konsole_unveraendert` — Bis zur Konsole sind es 312 Schritte, „und heute sind es dreihundertzwölf“.
3. `zwei_stuecke` — Fehlen zwei Schrittlängen, fehlen zwei Schritte.

Lässt du ein `sorry` stehen, kompiliert die Datei trotzdem, mit einer Warnung je Lücke. Das ist Absicht: So sieht ein
Register aus, das seine Lücken zeigt.

## Was der Beweis nicht weiß

- **Warum die Zeit stockt.** Das Outline nennt Kiko als Spur. Kein Satz hier modelliert die Minuten, die fehlen, und
  das Tutorial versucht es nicht. Amnesie und Kiko bleiben, wie `development.json` sagt, unerklärt.
- **Ob die 73 cm stimmen.** Die Schrittlänge ist aus Entwurf J geschlossen (ein Abschnitt von 0,73 m, ein Schritt
  weniger), nicht entschieden.
- **Wer das Messzeichen gesetzt hat.** Im Modell gibt es nur eine Notiz, keinen Anteil, der sie geschrieben hat.

## Bezug zur Storyform

- **A-MC Concern Memory:** Zwei Gedächtnisse stehen gegeneinander, das Register und Kaels Notiz. Lean zeigt, warum das
  Register nach dem Abgleich nichts mehr weiß: Der Abgleich ist korrekt.
- **A Story Requirements Learning:** Induktion ist die Form des Lernens in Lean, vom leeren Weg zum Weg mit einem Schritt
  mehr. Kael lernt in Kap 3 dasselbe: dass seine Zählung stimmt und die Welt nicht.
- **Ausblick auf Kap 4:** Eine Wärme, die nicht in die Stadt passt, ist kurz da (Treatment, Hook-out). Für sie hat
  dieses Tutorial keinen Typ, so wie die Konsole für den Anschluss keinen hatte.
