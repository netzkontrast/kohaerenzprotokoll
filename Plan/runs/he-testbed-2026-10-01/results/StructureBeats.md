# StructureBeats — the testbed's results

> StructureBeats — a structural beat, turn or shape a source places in the book — inciting incident, midpoint, crisis, climax, frame, mode change — and where.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: the developmental-editor's craft criteria (spine, structure, arc: the beats where the book claims them, or the deliberate alternative shape) and GOAL.md 5.1
> (four simultaneous levels: the Kishōtenketsu clamp, the dual storyform, three narrative modes, and the brackets between chapters). Three
> transitions are structurally different and never confused: a mode change, the storyform turn, the consolidation.
> measured against: `Wiki/overview/plot.md` and the chapter pages, where each source's macro structure is laid side by side; a beat whose place resolves to a chapter is the attachable subset. A quote is placed by read.py --find (P26).
> may not: decide the book's structure, or that a lens applies — W1 is the author's; a beat here is a P_HE_STRUCT candidate laid beside the treatment as a finding, never a fault
> retire when: on three documents a person keeps no beat beyond what plot.md already tabulates

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/structurebeats-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.0527, 17.9 s. **1 rows**: 1 candidates, 0 refused, 0 duplicates.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | Kael spürt, dass die Aufmerksamkeit schwindet | In Kapitel 39 | resolution | asserts | In Kapitel 39 müssen wir beschreiben, wie Kael spürt, dass die Aufmerksamkeit schwindet. | 48 |

## `2026-09-14-kap25-vertiefung-md`

8 calls (0 failed), 8 chunks (0 without a valid reply), $0.1547, 59.0 s. **7 rows**: 7 candidates, 0 refused, 0 duplicates.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | Schleier-Disziplin | Kap 25–26 | mode_change | cites | Canon §0 Schleier-Disziplin verlangt genau das für Kap 25–26 | 21 |
| 2 | relation_reading | candidate | Hook-in | Kap 24 | bracket | asserts | Hook-in aus Kap 24 explizit | 25 |
| 3 | relation_reading | candidate | neuer Hook-out | Kap 26 | bracket | asserts | neuer Hook-out: die Restzahl steht nach Schichtende bei 34 statt 31 und wird morgen früh nicht bei sechs stehen → trägt direkt in Kap 26 | 25 |
| 4 | relation_reading | candidate | Schwelle, nicht Konfrontation | Kap 25 | turn | cites | Kap 25: Schwelle, nicht Konfrontation | 31 |
| 5 | relation_reading | candidate | KW2 | 14–22 | beat_of_n | cites | Der Canon weist 14–22 KW2 und 23–28 KW3 zu | 60 |
| 6 | relation_reading | candidate | KW3 | 23–28 | beat_of_n | cites | Der Canon weist 14–22 KW2 und 23–28 KW3 zu | 60 |
| 7 | relation_reading | candidate | KW3 | Kap 25 | beat_of_n | asserts | Kap 25 löst KW3 jetzt **sensorisch** ein | 60 |
