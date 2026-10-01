# Knowledge — the testbed's results

> Knowledge — who knows, wrongly believes or cannot yet know what, and where, with the sentence.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: the plan's reader-knowledge ledger (Phase 2c: what the reader, Kael and AEGIS each know, wrongly believe and cannot yet know), GOAL.md 4.3
> (`ReaderKnowledgeState`, edge `knows_at`) and 5.5's information balance (knows for certain, wrongly assumes, cannot yet know, learns here,
> misreads afterwards). The continuity-editor's knowledge state and the beta-reader-panel's comparison with the treatment read the same thing.
> measured against: the reader-knowledge lines the treatment will hold once it exists; until then, a record whose knower and fact stand inside its quote is the precise subset. A quote is placed by read.py --find (P26).
> may not: say what the reader will know, or that a reveal has landed — the beta-reader-panel measures that against readers — or decide which document's knowledge state is right; a state here is a P_HE_KNOWS candidate
> retire when: on three documents a person keeps no state beyond what the plan's reader-knowledge lines will hold

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/knowledge-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.0725, 33.0 s. **6 rows**: 6 candidates, 0 refused, 0 duplicates.

Beside the Haiku pilot of 2026-09-30 on this document: the candidates stand on 5 lines here and 2 there, 0 of them the same.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | Kael | dass die Zeit im Konstrukt nicht linear fließt | learns_here | hedges | Kael sollte früh bemerken, dass die Zeit im Konstrukt nicht linear fließt | 17 |
| 2 | relation_reading | candidate | Kael | dass er nicht allein war | suspects | asserts | In diesen Momenten spürte Kael, dass er nicht allein war. | 21 |
| 3 | relation_reading | candidate | Kael | die Wahrheit | learns_here | asserts | Juna ist diejenige, die Kael die Wahrheit flüstert | 39 |
| 4 | relation_reading | candidate | Kael | dass die Aufmerksamkeit schwindet | learns_here | hedges | In Kapitel 39 müssen wir beschreiben, wie Kael spürt, dass die Aufmerksamkeit schwindet. | 48 |
| 5 | relation_reading | candidate | Er | Wenn der letzte Punkt gesetzt ist, wird er aufhören zu atmen | knows | asserts | Er weiß: Wenn der letzte Punkt gesetzt ist, wird er aufhören zu atmen. | 48 |
| 6 | relation_reading | candidate | du | dein Herz schlägt von selbst | wrongly_believes | asks | Glaubst du wirklich, dein Herz schlägt von selbst? | 41 |

## `2026-09-14-kap25-vertiefung-md`

Not run yet.
