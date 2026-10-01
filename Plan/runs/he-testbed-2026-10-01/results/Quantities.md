# Quantities — the testbed's results

> Quantities — a number the document binds to what it counts, measures or names, with that sentence.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: the wiki's question on what the number 734 names, and the chapter counts the sources give differently (39 or 40).
> A number is not a term, so the mechanical MENTIONS relation never carries one; the subject a number belongs to is a
> reading of the sentence.
> measured against: the numbers the wiki's pages and conflict records quote; a value that stands inside its quote is the precise subset, and code checks it. A quote is placed by read.py --find (P26).
> may not: compare two documents' numbers — a difference between them is a conflict, and conflicts are read, never detected — or decide which is right
> retire when: on three documents a person keeps no quantity beyond what the pages already quote

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/quantities-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.0568, 20.7 s. **5 rows**: 5 candidates, 0 refused, 0 duplicates.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | „Stasis-Lücken“ | Teil 1 | duration | asserts | Das Phänomen der „Stasis-Lücken“ (Teil 1) | 15 |
| 2 | relation_reading | candidate | „Höhere Metrik“ | Teil 2 | duration | asserts | AEGIS und die „Höhere Metrik“ (Teil 2) | 23 |
| 3 | relation_reading | candidate | „Rendering-Grenzen“ | Teil 1 & 2 | duration | asserts | Die „Rendering-Grenzen“ (Teil 1 & 2) | 30 |
| 4 | relation_reading | candidate | Kael spürt, dass die Aufmerksamkeit schwindet | Kapitel 39 | duration | asserts | In Kapitel 39 müssen wir beschreiben, wie Kael spürt, dass die Aufmerksamkeit schwindet. | 48 |
| 5 | relation_reading | candidate | Beobachter-Fokus | 85% | parameter | asserts | Beobachter-Fokus bei 85% | 58 |

## `2026-09-14-kap25-vertiefung-md`

Not run yet.
