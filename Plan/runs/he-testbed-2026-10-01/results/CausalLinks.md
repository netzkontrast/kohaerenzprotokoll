# CausalLinks — the testbed's results

> CausalLinks — what one thing brings about, allows, prevents or triggers in another, each with that sentence.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: the plot model GOAL.md wants as checkable rules, and the questions of the kind why does X happen that no stated relation
> type answers: StatedRelations types are open and mostly structural (part_of, controls, located_in).
> measured against: the causal chains a note quotes for the same document; a pair whose endpoints both resolve to a wiki term is the attachable subset. A quote is placed by read.py --find (P26).
> may not: say that a cause is true, order events in time, or detect a contradiction between two documents' causes — a cause is a P_HE_CAUSAL proposal for a reader
> retire when: on three documents a person keeps no pair beyond what StatedRelations already gives as causes or controls

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/causallinks-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.0729, 31.7 s. **5 rows**: 5 candidates, 0 refused, 0 duplicates.

Beside the Haiku pilot of 2026-09-30 on this document: the candidates stand on 4 lines here and 0 there, 0 of them the same.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | die „Einheit“ | das System abschalten | causes | hedges | dass die „Einheit“ sonst das Interesse verlieren und das System abschalten könnte | 27 |
| 2 | relation_reading | candidate | kognitiven Grenzen | das System | causes | asserts | Wenn das System unentscheidbar wird, liegt das daran, dass der Verstand des Beobachters (des Lesers) an seine eigenen kognitiven Grenzen stößt. | 35 |
| 3 | relation_reading | candidate | die Zeilen | dein Herz | causes | asks | dein Herz schlägt von selbst? Oder schlägt es nur, weil da draußen jemand die Zeilen liest | 41 |
| 4 | relation_reading | candidate | der Leser | Die Welt | requires | asserts | Die Welt existiert nur so weit, wie der Leser sie sich vorstellen kann. | 35 |
| 5 | relation_reading | candidate | narrative Spannung | System-Abschaltung | prevents | asserts | Erhöhe narrative Spannung, um System-Abschaltung zu verhindern | 58 |

## `2026-09-14-kap25-vertiefung-md`

8 calls (0 failed), 8 chunks (0 without a valid reply), $0.1488, 51.6 s. **2 rows**: 2 candidates, 0 refused, 0 duplicates.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | einer zweiten Spannung im selben Unterarm | die Hand | prevents | asserts | die Hand von selbst auf das Bestätigungsfeld — mit eigener Syntax (Verb vorn, keine Bedingung) und eigener Somatik (Schulter, Kiefer, flacher Atem) — und wird von einer zweiten Spannung im selben Unterarm gestoppt | 21 |
| 2 | relation_reading | candidate | agency-Capability-Verben | Provenienz | prevents | asserts | Die agency-Capability-Verben standen in diesem Lauf nicht zur Verfügung (kein MCP-Server, keine agency-CLI im Container) — die Prüfung erfolgte manuell gegen die JSON-Dateien; Provenienz wurde daher **nicht** in .agency/session.db geschrieben. | 51 |
