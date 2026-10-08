# Lean lernen mit Kael — Kap 1 bis 3

Ein Tutorial für Lean 4, entlang der Dramatica-Outlines der ersten drei Kapitel (`Plan/storyform/development.json`
und `Manuscript/plot/treatment.md`). Angelegt am 2026-10-07 auf deinen Auftrag: „Bitte erstelle ein Tutorial für
Lean – folge dafür den Dramatica-Plot-Outlines für Kapitel 1–3. Webe es tief in die Story ein.“ **Übungsmaterial, kein
Kanon.** Es setzt keine neue Handlung, sondern folgt den Outlines. Die Zahlen kommen aus den Arbeitsentwürfen J (Kap 1)
und A (Kap 2).

Jede Lektion führt einen Schritt des Outlines in einen Lean-Begriff über: das Ziel in eine Aussage, den Widerstand in
einen Fall, den Lean nicht übergehen lässt, die Wahl in einen Zeugen, den Preis in einen Satz. Am Ende jeder Lektion
steht, was der Beweis nicht weiß. Das ist dieselbe Frage wie bei den [AEGIS-Logs](../README.md): Eine korrekte
Ableitung steht auf einer Definition, und die Definition hat jemand geschrieben.

| Lektion | Kap | Was Lean lehrt | Was die Geschichte trägt |
|---|---|---|---|
| [1 · Vorkühlung](lektion-1-vorkuehlung.md) | 1 | Typen, `Option`, `#eval`, Listen, `match`, `rfl`, `decide`, `¬` | die Zuweisung, die Zeile ohne Datentyp, die Hand, die 37 |
| [2 · Die Rolle hält](lektion-2-die-rolle-haelt.md) | 2 | `Prop`, `∧ ∨ ¬ → ∀ ∃`, Zeugen, Taktiken, Idempotenz | die Frist, der offene Posten, „Die Wartung.“, 251 |
| [3 · Der fehlende Schritt](lektion-3-der-fehlende-schritt.md) | 3 | Rekursion, Induktion, allgemeine Sätze, `sorry`, `#print axioms` | zweimal zählen, 0,73 m, der Abgleich, die Notiz |

## Wie man es benutzt

```bash
bash scripts/install.sh lean                     # einmal: Lean 4.24.0 nach .lean/, Version aus ../lean/lean-toolchain
L=.lean/lean-4.24.0-linux/bin/lean
$L Manuscript/aegis-logs/tutorial/K01.lean        # die Lektion: keine Meldung außer den #eval-Ausgaben
$L Manuscript/aegis-logs/tutorial/K01_Uebung.lean # die Übungen: eine Warnung je offenes `sorry`
```

Arbeite in der Übungsdatei. Ersetze ein `sorry` durch einen Beweis und lass Lean laufen; wenn die Warnung für diese
Übung verschwindet und kein Fehler kommt, ist sie gelöst. Die Lösungen stehen am Ende der Lektionsdatei.

## Wie es geprüft wird

- Jede Lektionsdatei kompiliert ohne `sorry`, und jeder Satz hängt höchstens von Leans Standardaxiomen ab
  (`python3 scripts/aegis_logs.py verify`, Ergebnis in `Plan/runs/aegis-logs/verifikation.json`).
- Jede Übungsdatei wird aus ihrer Lektion **erzeugt** (`python3 scripts/aegis_logs.py exercises`): dieselbe Datei, nur
  die Beweise der Lösungen durch `sorry` ersetzt. `aegis_logs.py check` scheitert, wenn eine Übungsdatei veraltet ist,
  und `verify` verlangt, dass sie mit genau einem `sorry` je Übung und ohne Fehler kompiliert.
- Die App zeigt die Lektionen unter Manuscript → Cast → AEGIS — Logs & Beweise und bei Kap 1, 2 und 3, mit demselben
  Prüfstatus wie die Logs.
