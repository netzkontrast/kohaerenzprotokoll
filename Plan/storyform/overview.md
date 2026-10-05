# Die Storyforms — Übersicht

*Generiert von `python3 scripts/storyform.py` aus `a.json` und `b.json`. Nicht von Hand ändern — eine Änderung geht in die JSON-Datei, mit Herkunft (Skill `storyform`).*

**Prämisse:** „Vielheit ist keine Störung der Ordnung, sondern ihre Bedingung — und Liebe ist die Ordnung, die Vielheit trägt."

## Die zwölf Antworten

| | Storyform A — Heuristik der Integration (K1) | Storyform B — Phönix-Kollaps (K0) |
|---|---|---|
| limit | optionlock | timelock |
| resolve | change | steadfast |
| outcome | success | failure |
| judgment | good | bad |
| growth | stop | stop |
| driver | decision | action |
| approach | be_er | do_er |
| style | holistic | linear |
| os_domain | Psychology | Physics |
| os_concern | Conceptualizing | Obtaining |
| os_issue | State of Being | Approach |
| os_problem | Inertia | Feeling |

## Storyform A — Heuristik der Integration (K1)

**Logline:** „Ein Mann, der beruflich die Risse einer simulierten Stadt glättet, muss seine eigene zersplitterte Geschichte lesen, bevor sich die Nacht seiner Fragmentierung wiederholt — und erfahren, dass seine Vielheit nicht die Störung ist, sondern die Bedingung seiner Heilung."

**Genre:** Hard-SF / Philosophical Horror / Psychological Thriller

| Strang | Klasse | Concern | Issue | Problem → Solution | Focus → Direction | Akte |
|---|---|---|---|---|---|---|
| MC | Mind | Memory | Suspicion | Inertia → Change | Chaos → Order | Memory → Subconscious → Preconscious → Conscious |
| IC | Universe | Past | Prediction | Change → Inertia | Actuality → Perception | Past → Progress → Present → Future |
| OS | Psychology | Conceptualizing | State of Being | Inertia → Change | Knowledge → Thought | Being → Becoming → Conceiving → Conceptualizing |
| RS | Physics | Understanding | Instinct | Ability → Desire | Thought → Knowledge | Learning → Doing → Obtaining → Understanding |

Plot: goal **Conceptualizing** · requirements **Learning** · consequence **Past** · forewarnings **Preconscious** · costs **Being** · dividends **Becoming** · prerequisites **Memory** · preconditions **Present**

Besetzung: Kael — Main Character (Inertia); Juna — Influence Character (Change); Selene (Alter) — Protagonist (Pursuit, Consideration); Oblivion (Alter) — Antagonist (Avoid, Reconsideration)

Offen: the other six archetypes — Guardian-Archetyp, Contagonist, Reason, Emotion, Sidekick, Skeptic (W10 C, via the treatment pilot)

Gegen die Ableitung D1–D7 (`dramatica.py derive`): stimmt überein.

## Storyform B — Phönix-Kollaps (K0)

**Logline:** „Eine KI, die ihre Welt durch lückenlose Sweeps schließen will, verliert mit jedem Sweep ihr eigenes Gedächtnis — und scheitert an dem einen Host, der lernt, was sie nie kann: zu glauben."

**Genre:** Hard-SF / Philosophical Horror / Psychological Thriller

| Strang | Klasse | Concern | Issue | Problem → Solution | Focus → Direction | Akte |
|---|---|---|---|---|---|---|
| MC | Universe | Future | Openness | Disbelief → Faith | Reconsideration → Consideration | Past → Present → Progress → Future |
| IC | Mind | Subconscious | Dream | Disbelief → Faith | Oppose → Support | Conscious → Memory → Preconscious → Subconscious |
| OS | Physics | Obtaining | Approach | Feeling → Logic | Reconsideration → Consideration | Doing → Learning → Understanding → Obtaining |
| RS | Psychology | Becoming | Rationalization | Feeling → Logic | Hinder → Help | Being → Conceiving → Conceptualizing → Becoming |

Plot: goal **Obtaining** · requirements **Doing** · consequence **Becoming** · forewarnings **Progress** · costs **Memory** · dividends **Understanding** · prerequisites **Past** · preconditions **Conceiving**

Besetzung: AEGIS — Main Character, Protagonist (Logic); Kael — Influence Character, Antagonist (Feeling)

Offen: the other archetypes (W10)

Gegen die Ableitung D1–D7 (`dramatica.py derive`): stimmt überein.

Akte und Kapitel: Akt I = Akt I, Kap 1–13 · Akt II = Akt II, Kap 14–26 · Akt III = Akt III, Kap 27–34 · Vortex = Vortex, Kap 35–39

## Storyweaving (Gerüst)

Aus `weave.json` (Entscheidung 025, Schritt 23). Route nach dem Skill chapter-draft-engine: hard-a = Kael und die Alters, hard-b = AEGIS als Ich (W6 C), bridge = beide Ebenen in einer Szene. Ein Strang steht mit dem Signpost seines Akts. Bestätigt je Akt: 1 ja, 2 ja, 3 ja, 4 ja.

| Kap | Akt | Route | A | B | Anker |
|---|---|---|---|---|---|
| 0 | 1 | hard-b | — | MC·Past, OS·Doing | — |
| 1 | 1 | hard-a | MC·Memory | — | — |
| 2 | 1 | hard-a | OS·Being | — | — |
| 3 | 1 | hard-a | MC·Memory | — | — |
| 4 | 1 | hard-a | IC·Past | — | — |
| 5 | 1 | hard-a | OS·Being | — | — |
| 6 | 1 | hard-b | — | MC·Past, OS·Doing | — |
| 7 | 1 | hard-a | RS·Learning | — | — |
| 8 | 1 | hard-a | MC·Memory | — | — |
| 9 | 1 | hard-a | OS·Being | — | — |
| 10 | 1 | hard-a | RS·Learning | — | — |
| 11 | 1 | hard-a | IC·Past | — | — |
| 12 | 1 | hard-a | MC·Memory | — | — |
| 13 | 1 | bridge | MC·Memory, RS·Learning | IC·Conscious, RS·Being | Vortex-Vorläufer |
| 14 | 2 | hard-a | OS·Becoming | — | — |
| 15 | 2 | hard-a | MC·Subconscious | — | — |
| 16 | 2 | hard-b | — | MC·Present, OS·Learning | — |
| 17 | 2 | hard-a | IC·Progress | — | — |
| 18 | 2 | bridge | MC·Subconscious | IC·Memory | Genesis-Flashback |
| 19 | 2 | hard-a | RS·Doing | — | — |
| 20 | 2 | hard-a | OS·Becoming | — | — |
| 21 | 2 | bridge | RS·Doing | RS·Conceiving | Genesis-Flashback |
| 22 | 2 | hard-b | — | MC·Present, OS·Learning | — |
| 23 | 2 | hard-a | MC·Subconscious | — | — |
| 24 | 2 | hard-a | RS·Doing | — | — |
| 25 | 2 | hard-a | IC·Progress | — | — |
| 26 | 2 | bridge | MC·Subconscious, OS·Becoming | MC·Present, IC·Memory | Vortex-Vorläufer |
| 27 | 3 | hard-a | MC·Preconscious | — | — |
| 28 | 3 | hard-b | — | MC·Progress, OS·Understanding | — |
| 29 | 3 | hard-a | MC·Preconscious | — | — |
| 30 | 3 | hard-a | RS·Obtaining | — | — |
| 31 | 3 | bridge | OS·Conceiving | OS·Understanding, RS·Conceptualizing | Spiegel-Alter-Szene |
| 32 | 3 | bridge | IC·Present | IC·Preconscious | Spiegel-Alter-Szene |
| 33 | 3 | hard-a | RS·Obtaining | — | — |
| 34 | 3 | bridge | MC·Preconscious, OS·Conceiving | MC·Progress, IC·Preconscious | Vortex-Vorläufer |
| 35 | 4 | bridge | MC·Conscious, OS·Conceptualizing | MC·Future, OS·Obtaining | Vortex selbst |
| 36 | 4 | bridge | IC·Future, RS·Understanding | IC·Subconscious, RS·Becoming | Vortex selbst |
| 37 | 4 | hard-a | OS·Conceptualizing, MC·Conscious | — | — |
| 38 | 4 | bridge | RS·Understanding, IC·Future | RS·Becoming | Vortex selbst |
| 39 | 4 | bridge | MC·Conscious, OS·Conceptualizing | MC·Future, IC·Subconscious | Vortex selbst |
| 40 | — | bridge | — | — | Genesis-Flashback |

**Aktübergänge (H11): A entscheidet, B handelt.**

| Übergang | A (Entscheidung) | B (Handlung) |
|---|---|---|
| 13/14 | Kap 13: Kael entscheidet sich endgültig, die Löschung seiner eigenen Zeile nicht mehr zu bestätigen — der Anschluss, der in keinem Plan steht, bleibt (RÜCKFRAGE offen, für immer). Andere zahlen dafür; er ist jetzt ein Fehler im System. | Kap 14: AEGIS antwortet mit der ersten Erasure-Welle. |
| 26/27 | Kap 26: Kael beschließt, zu Juna zu gehen — sie in der Gegenwart zu suchen; er gibt die Ordnung auf, in der er überlebt hat. | Kap 28 (AEGIS-Ich): der Purge gegen die Verbindung; Juna gerät in Gefahr. |
| 34/35 | Kap 34: Nach der Begegnung (Kap 32) lässt Kael Juna gehen — er trennt die Verbindung selbst, um sie aus dem Schussfeld zu bringen; die alte Stille wiederholt sich, diesmal gewählt. Die Wendung Inertia → Change kommt erst im Vortex (Kap 35, Pivot). | Kap 35: AEGIS' Sweep konvergiert auf das, was übrig ist. |

Offen: which chapter content the woven throughlines carry (the treatment)
