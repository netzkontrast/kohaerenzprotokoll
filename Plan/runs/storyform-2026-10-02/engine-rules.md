# Was die Dramatica-Engine aus 12 Antworten ableitet — Befund vom 2026-10-05

**Anlass:** der Hinweis des Autors, die Signposts müssten bestimmbar sein. Sie sind es — aber nicht mit der Tafel allein.

## Was offiziell gesagt ist

- **Chris Huntley (Mitentwickler), Dramatica-Forum:** die Signpost-Reihenfolge entsteht aus „flips and rotations" der Quads; Ausgangspunkt sind die Problem/Solution-Elemente, das Verhältnis von MC- zu OS-Domain und mehrere Dynamiken; zwei Durchgänge, „bottom up" und „top down". Die genaue Regel ist „for commercial purposes" geheim. <https://discuss.dramatica.com/t/how-does-dramatica-determine-signpost-order/672>
- **Melanie Anne Phillips (Mitentwicklerin), storymind.com:** zwei „wind ups" der Tafel wie eine Uhrfeder, eine um das OS-Problem-Element, eine um das MC-Problem-Element; welche zuerst kommt, bestimmen Storyform-Wahlen; Rotationen um eine Position, Flips von Paaren, Kinder-Quads werden mitgenommen oder nicht. <https://www.storymind.com/content/90.htm>
- **Die Engine kennt 32 768 Storyforms**, festgelegt durch **12 Antworten**: Limit, Resolve, Outcome, Judgment, Growth, Driver, Approach, Problem-Solving Style, OS Domain, OS Concern, OS Issue, OS Problem. **Alles andere — MC/IC/RS-Domains, -Concerns, -Issues, -Problems, Plot-Punkte und alle 16 Signposts — wird abgeleitet.** Heute rechnet das der „Storyform Builder" der Dramatica-Plattform. <https://platform.dramatica.com/docs/storyform-builder>

## Was ein Nutzer zurückgerechnet hat (nicht offiziell, aber mit der Arithmetik vereinbar)

Forum-Thread „Story Engine mechanics + games", Beitrag von *bobRaskoph*, 2016 (<https://discuss.dramatica.com/t/story-engine-mechanics-games/499>):

1. **Growth × Approach legt das OS-Klassenpaar fest:** „Stop+Do-er OR Start+Be-er → OS Domain in {Universe, Physics}; Stop+Be-er OR Start+Do-er → OS Domain in {Mind, Psychology}." Das ist genau das eine Bit, das 2^16 = 65 536 Kombinationen auf die offiziellen 32 768 halbiert.
2. **Approach legt die MC-Domain fest** (sein Beispiel: OS Universe → Do-er: MC Physics, Be-er: MC Psychology).
3. **Change-MC: MC-Problem = OS-Problem; MC-Issue = die Variation über diesem Element in der MC-Domain; IC-Issue = die Variation über demselben Element in der IC-Domain.**
4. **Steadfast-MC: MC-Symptom/Response = OS-Symptom/Response**, und die Issues folgen der Variation über diesem Paar.
5. **RS-Problem:** bei Outcome Failure gleich dem OS-Problem; sonst ein Element im Quad, der in der RS-Domain das OS-Symptom/Response-Paar enthält.

## Unsere Storyforms gegen diese Regeln (Lesung dieser Sitzung)

| Regel | A (Kael) | B (AEGIS) |
|---|---|---|
| 1 Growth × Approach → OS | **✗ Start + Be-er verlangt OS Universe/Physics; A hat OS Psychology** | ✓ Stop + Do-er, OS Physics |
| 2 Approach → MC-Domain | ✓ Be-er → Mind (innen) | ✓ Do-er → Universe (außen) |
| 3 Change: MC-Problem = OS-Problem; Issues | ✓ Inertia = Inertia; MC-Issue Suspicion (über Inertia in Mind) ✓; IC-Issue Prediction (über Inertia in Universe) ✓ | — |
| 4 Steadfast: MC-Focus/Direction = OS-Focus/Direction | — | **✗ AEGIS hat Unending/Ending, das OS Reconsideration/Consideration.** Nach Regel 4 läge AEGIS' Kette unter Future/Openness (Problem Faith/Disbelief), nicht unter Progress/Fantasy/Test |
| 5 RS-Problem | **✗ wahrscheinlich:** Success → RS-Problem im Quad mit Knowledge/Thought in Physics = Instinct (Ability/Desire), nicht Senses/Perception | **✗ wahrscheinlich:** Failure → RS-Problem = OS-Problem Feeling (in Psychology), nicht Test |

**Folgerung:** Die Werte unterhalb der 12 Antworten, die wir Schritt für Schritt von Hand gewählt haben, sind in Dramatica **abgeleitet**. Einige davon widersprechen den zurückgerechneten Regeln. Die Signposts lassen sich aus den 12 Antworten nur mit der Engine bestimmen; ihre Funktion ist nicht veröffentlicht.

## Die 12 Antworten, wie sie heute stehen

| | A | B |
|---|---|---|
| Limit / Resolve / Outcome / Judgment | Optionlock / Change / Success / Good | Timelock / Steadfast / Failure / Bad |
| Growth / Driver / Approach / Style | Start / Decision / Be-er / Holistic | Stop / Action / Do-er / Linear |
| OS Domain / Concern / Issue / Problem | Psychology / Conceptualizing / State of Being / Inertia | Physics / Obtaining / Approach / Feeling |

A ist nach Regel 1 keine der 32 768 Storyforms; B ist es.
