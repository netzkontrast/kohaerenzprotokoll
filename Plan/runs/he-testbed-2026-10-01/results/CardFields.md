# CardFields — the testbed's results

> CardFields — a field of a character's card — function, want, need, wound, lie, fear, contradiction, arc, voice, relationship — with its provenance.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: the two character skills (`character-card-builder`, `reverse-character-cards`) and the plan's cast ledger (Phase 2c): one lean card
> per figure, in causal order wound → lie → fear → need → want, each field tagged by who says it. The sources hold positions on
> the figures; the interview offers at most two cited positions, as poles to react against, and never fills a blank.
> measured against: the cards the author builds by interview, once they exist; until then, a pair whose figure resolves to a wiki term and whose quote holds both is the attachable subset. A quote is placed by read.py --find (P26).
> may not: invent a trait, fill a blank of a card, or write a card — a field here is a P_HE_CARD candidate: the sources' position, cited, for the author to react against (P0); and it never enters the book's cast ledger
> retire when: on three documents the author, interviewed on a figure, reacts to none of the positions offered

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/cardfields-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.0634, 23.2 s. **6 rows**: 5 candidates, 1 refused, 0 duplicates.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | AEGIS | hat Angst vor dem Zuklappen des Buches | fear/narration | asserts | AEGIS hat Angst vor dem Zuklappen des Buches. | 28 |
| 2 | relation_reading | candidate | AEGIS | ein verzweifelter Versuch, den Leser (den Beobachter) bei der Stange zu halten | want/inferred | asserts | Seine Ordnungssucht ist ein verzweifelter Versuch, den Leser (den Beobachter) bei der Stange zu halten | 28 |
| 3 | relation_reading | refused: surface absent from document | AEGIS | rechtfertigt seine harten Maßnahmen damit, dass die „Einheit“ sonst das Interesse verlieren und das System abschalten könnte | want/claimed_by_figure | asserts | Er rechtfertigt seine harten Maßnahmen (das Kohärenz Protokoll) damit, dass die „Einheit“ sonst das Interesse verlieren und das System abschalten könnte. | 27 |
| 4 | relation_reading | candidate | Juna | die Kael die Wahrheit flüstert | function/narration | asserts | Juna ist diejenige, die Kael die Wahrheit flüstert. | 39 |
| 5 | relation_reading | candidate | Kael | die Sonde, die der Leser in das Trauma geschickt hat | function/reported_by_other | asserts | Kael ist die Sonde, die der Leser in das Trauma geschickt hat. | 42 |
| 6 | relation_reading | candidate | Kael | akzeptiert sein Schicksal als „Gedanke eines Fremden“ | arc/narration | asserts | Kael bittet den Leser nicht darum, weiterzulesen, sondern akzeptiert sein Schicksal als „Gedanke eines Fremden“. | 49 |

## `2026-09-14-kap25-vertiefung-md`

Not run yet.
