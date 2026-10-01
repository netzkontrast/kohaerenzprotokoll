# ProseRules — the testbed's results

> ProseRules — a rule for how the book is written — voice, diction, device, lock, formatting, ban — with its scope and the sentence.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: the plan's rulebook (Phase 2d: the prose rules the author keeps, each with its chapter range and a mark for whether code can check it), GOAL.md 5.4's
> discipline table and the drafting brief's R-1 to R-10, all of which count as proposals; and writing-skills rule 4: a designed crack is not a slip,
> so the line-editor, copy-editor and continuity-editor each take a list of pre-cleared devices from the rulebook, and until it exists ask the author.
> measured against: the rulebook once the author has decided it; until then, a rule whose subject and constraint stand inside its quote is the precise subset. A quote is placed by read.py --find (P26).
> may not: clear a device, keep a rule or say a rule is decided — the rulebook is the author's; a rule here is a P_HE_PROSERULE proposal; nor write a line of prose to show a rule
> retire when: on three documents the author's rulebook keeps no rule offered

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/proserules-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.0661, 26.8 s. **4 rows**: 4 candidates, 0 refused, 0 duplicates.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | den finalen Twist | müssen wir subtile „Glitch-Momente“ und systemische Hinweise einbauen | structure | asserts | Um den finalen Twist vorzubereiten – dass Kael die Manifestation des Lesers ist und seine Welt mit dem Zuklappen des Buches stirbt –, müssen wir subtile „Glitch-Momente“ und systemische Hinweise einbauen. | 13 |
| 2 | relation_reading | candidate | Kapitel 39 | beschreiben, wie Kael spürt, dass die Aufmerksamkeit schwindet | structure | asserts | In Kapitel 39 müssen wir beschreiben, wie Kael spürt, dass die Aufmerksamkeit schwindet. | 48 |
| 3 | relation_reading | candidate | das „Du“ | in Schlüsselmomenten | pov | asserts | Nutze in Schlüsselmomenten das „Du“. | 53 |
| 4 | relation_reading | candidate | AEGIS-Protokolle | Kursivschrift | format | asserts | Nutze Kursivschrift für AEGIS-Protokolle, die den „Beobachtungsstatus“ abfragen. | 54 |

## `2026-09-14-kap25-vertiefung-md`

Not run yet.
