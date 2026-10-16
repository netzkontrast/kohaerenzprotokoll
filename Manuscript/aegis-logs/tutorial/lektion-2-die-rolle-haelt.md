---
id: LT-02
titel: Die Rolle hält
kapitel: 2
redaktion: entwurf
lean: K02.lean
uebung: K02_Uebung.lean
theoreme: [frist_in_stunden, frist_am_abend, rueckfrage_hat_ursache, zeuge_belastet_tamm, wartung_schliesst_nicht, zwoelf_minuten_ohne_zeugen, nichts_schliesst, korrigiere_idempotent, fehler_der_wartet, neun_zehntel, hand_erklaert_rueckfrage, ausgang_hat_ursache, und_tauschen, ehrlich_schliesst_auch_nicht]
uebungen: [hand_erklaert_rueckfrage, ausgang_hat_ursache, und_tauschen, ehrlich_schliesst_auch_nicht]
---

# Lektion 2 — Die Rolle hält

> Lean-Tutorial einer Claude-Sitzung, 2026-10-07, auf den Auftrag des Autors. **Übungsmaterial, kein Kanon.** Die
> Handlung folgt dem Treatment (Kap 2) und `development.json` (Kap 2), die Zahlen und Sätze kommen aus Kap 2, Entwurf A
> (`kap-02/entwurf-a-die-rolle-haelt.md`), einem Arbeitsentwurf. Lean-Datei: [K02.lean](K02.lean), Übungen:
> [K02_Uebung.lean](K02_Uebung.lean). Setzt Lektion 1 voraus ([lektion-1-vorkuehlung.md](lektion-1-vorkuehlung.md)).

## Die Szene

Um 06:10 kommt die Zeile zurück. Die Rückfrage geht in eine Prüfung, die Frist ist das nächste Wartungsfenster von
Sektor 04. An der Stelle, wo die Bank war, zeigt das Inventar einen Posten ohne Datentyp, der mit ihr gegangen ist. An
der Konsole kehrt der Wert 251 zurück, derselbe Wert mit derselben falschen Ziffer. Die Kollegin rechts hat einen
offenen Posten notiert: „Er schließt, wenn ich eine Ursache habe, die ich prüfen kann.“ Kael sagt: „Die Wartung.“

| Outline (Kap 2) | Kap 2 |
|---|---|
| Ziel | die Rolle trotz des offenen Postens halten |
| Widerstand | die Kollegin verlangt den Nachweis vor dem nächsten Fenster |
| Handlung | das Register gegen einen Gegenstand vor Ort prüfen; der Wert 251 kehrt zurück |
| Wahl (Schritt 47) | die Wartung als Ursache, statt den offenen Posten auf sich zu nehmen |
| Wendung | der Wert stimmt auf der Konsole, außerhalb bleibt eine Abweichung |
| Preis | die Erklärung wird überprüfbar und belastet einen anderen |
| Storypoints | A-OS Concern Conceptualizing · A Catalyst Threat |

## Was Lean hier lernt

| Outline | Lean | In K02.lean |
|---|---|---|
| die Frist (Catalyst: Threat) | eine Gleichung, die Lean nachrechnet | `frist_in_stunden` |
| „eine Ursache, die ich prüfen kann“ | ein Beweis | `schliesst` |
| was als Ursache zählt (Concern: Conceptualizing) | eine Definition entscheidet, was bewiesen werden muss | `erklaert`, `schliesst` |
| Kaels Wahl | `∃` braucht einen Zeugen, und der Zeuge hat Folgen | `rueckfrage_hat_ursache`, `zeuge_belastet_tamm` |
| die zwölf Minuten | eine Aussage ohne Zeugen | `zwoelf_minuten_ohne_zeugen` |
| 251 kehrt zurück | Idempotenz, und was eine Nacht mit ihr macht | `korrigiere_idempotent`, `fehler_der_wartet` |
| Register gegen Inventar | widersprechende Belege als Daten verschiedener Quellen | `neun_zehntel` |

## Schritt für Schritt

**1. Die Frist.** „Elf Tage. Ich rechne es aus, weil ich es nicht lassen kann: zweihundertvierundsechzig Stunden.“

```lean
theorem frist_in_stunden : 11 * 24 = 264 := rfl
```

Am Abend steht auf der Wand `FRIST: 10 TAGE 12 STUNDEN`. `frist_am_abend` prüft, dass das zwölf Stunden weniger sind.
Der Catalyst von Kap 2 ist eine Drohung mit einer Zahl, und eine Zahl lässt sich prüfen.

**2. Aussagen.** In Lektion 1 waren die Aussagen Gleichungen. Jetzt kommen Verknüpfungen dazu: `∧` (und), `∨` (oder),
`¬` (nicht), `→` (wenn … dann), `∀` (für alle) und `∃` (es gibt). Die Kollegin denkt in genau diesen Wörtern:

```lean
def schliesst (us : List Ursache) : Prop :=
  ∀ a : Abweichung, ∃ u, u ∈ us ∧ erklaert u a = true
```

Der Posten schließt, wenn es **für jede** Abweichung **eine** angebotene Ursache gibt, die sie erklärt. Das ist das
Concern des Kapitels, Conceptualizing: Wer `schliesst` definiert, entscheidet, was Kael beweisen muss. Die Kollegin hat
die Definition geschrieben, nicht er.

**3. `∃` braucht einen Zeugen.** Einen Satz mit „es gibt“ beweist man, indem man ein Beispiel zeigt und beweist, dass
es passt:

```lean
theorem rueckfrage_hat_ursache : ∃ u, erklaert u .rueckfrage = true :=
  ⟨.wartungsplan, rfl⟩
```

Das ist Kaels Wahl in Lean. Er hat zwei Zeugen für die Rückfrage, `.wartungsplan` und `.linkeHand`, und nennt den
ersten. Lean nimmt beide an, denn beide erklären die Abweichung. Aber ein Zeuge ist ein Wert, und Werte haben Folgen:
`belastet .wartungsplan` ist „H. Tamm, Freigabe Wartungsplan Sektor 04“. `zeuge_belastet_tamm` beweist, dass es nicht
Kael ist. „Es ist kein ganz falscher Satz. Es ist ein Satz, der die richtige Form hat.“ In Lean heißt das: Er hat den
richtigen Typ.

**4. Ein Beweis durch Widerspruch.** „Die Wartung erklärt eine Zeile. Sie erklärt nicht, wo Sie gestern Morgen
waren.“

```lean
theorem wartung_schliesst_nicht : ¬ schliesst [.wartungsplan] := by
  intro h                                   -- angenommen, der Posten schlösse
  obtain ⟨u, hu, he⟩ := h .ankunft           -- dann gäbe es eine Ursache für die Ankunft
  simp at hu                                -- die einzige angebotene ist der Wartungsplan
  subst hu
  simp [erklaert] at he                     -- und der erklärt die Ankunft nicht
```

Hier beginnen Taktiken. Nach `by` schreibt man Schritte, und Lean zeigt nach jedem, was noch zu zeigen ist. `¬ P`
beweist man, indem man `P` annimmt (`intro h`) und daraus etwas Unmögliches folgert. Die Kollegin macht es genauso: Sie
nimmt Kaels Ursache an und fragt nach der Ankunft.

**5. Eine Aussage ohne Zeugen.** Für die zwölf Minuten gibt es im Modell keine Ursache:

```lean
theorem zwoelf_minuten_ohne_zeugen : ∀ u, erklaert u .ankunft = false := by
  intro u
  cases u <;> rfl
```

`cases u` geht alle drei möglichen Ursachen durch, `rfl` prüft jede. Daraus folgt `nichts_schliesst`: Keine Liste von
Ursachen schließt den Posten, auch die ehrlichste nicht. „Ich kann ihr kein Nichts geben. Es hat keine Form.“ In Lean
kann man ein `∃` nicht ohne Zeugen beweisen, und für die zwölf Minuten hat Kael keinen.

**6. 251.** „Ein Ausgleich, der zurückkommt, ist kein Ausgleich. Er ist ein Fehler, der wartet.“

```lean
theorem korrigiere_idempotent (s : Stelle) : korrigiere (korrigiere s) = korrigiere s := rfl
theorem fehler_der_wartet : nacht (korrigiere ⟨3⟩) ≠ korrigiere ⟨3⟩ := by decide
```

Eine Korrektur ist idempotent: Zweimal angewandt ist einmal angewandt. Der zweite Satz zeigt, warum das nicht reicht.
Die Nacht setzt die Drei zurück, und die Korrektur hält nicht über das Fenster. Auf der Konsole stimmt alles, und der
Fehler wartet trotzdem.

**7. Zwei Belege, kein Widerspruch in der Logik.** Die Liste von Kap 1 sagt 3,1 × 10¹⁹ Bit für die Bank, das Inventar
sagt 2,8 × 10¹⁹ Bit für das Anhaftende. Lean bekommt das nicht als „die Bank war 3,1“ und „die Bank war nicht 3,1“,
sondern als zwei Belege mit ihrer Quelle. `neun_zehntel` rechnet nach, was Kael daraus schließt: Mehr als neun Zehntel
des Registerwerts waren nicht die Bank.

## Übungen

Öffne [K02_Uebung.lean](K02_Uebung.lean) und ersetze jedes `sorry`. Die Lösungen stehen am Ende von [K02.lean](K02.lean).

1. `hand_erklaert_rueckfrage` — Die wahre Ursache gibt es auch, aber ihr Zeuge belastet Kael selbst.
2. `ausgang_hat_ursache` — Für den Ausgang um 16:31 gibt es eine Ursache. Welche?
3. `und_tauschen` — Reine Logik: Aus „p und q“ folgt „q und p“.
4. `ehrlich_schliesst_auch_nicht` — Auch die ehrliche Auskunft schließt den Posten nicht.

Übung 1 ist die Wahl, die Kael nicht trifft. Lean beweist sie in einer Zeile. Im Roman kostet sie ihn die Rolle.

## Was der Beweis nicht weiß

- **Ob die Wartung gelogen ist.** Im Modell erklärt `.wartungsplan` die Rückfrage, weil `erklaert` es so festlegt.
  Wer die Tabelle schreibt, entscheidet, was als Erklärung zählt. Das ist dieselbe Frage wie in den AEGIS-Logs: eine
  korrekte Ableitung auf einer gesetzten Definition.
- **Was mit H. Tamm geschieht.** `belastet` nennt einen Namen. Die Prüfung, die auf Tamms Fläche erscheint, kommt im
  Modell nicht vor.
- **Was die zwölf Minuten waren.** Das Modell sagt nur, dass es keinen Zeugen gibt, nicht, dass nichts war.

## Bezug zur Storyform

- **A-OS Concern Conceptualizing:** Die Kollegin konzipiert, was eine Ursache ist, und Kael passt seinen Satz in ihre
  Form. In Lean ist Conceptualizing das Schreiben von Definitionen, und Definitionen entscheiden, was später beweisbar ist.
- **A Catalyst Threat:** Die Frist ist eine Zahl mit einem Ende. `frist_in_stunden` und `frist_am_abend` machen die
  Drohung prüfbar. Abwenden können sie sie nicht.
- **Schritt 47, die Wahl:** Kael wählt einen Zeugen, der einen anderen belastet. Der Beweis ist gültig. Die Schuld steht
  nicht in seinem Typ.
