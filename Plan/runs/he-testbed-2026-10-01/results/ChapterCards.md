# ChapterCards — the testbed's results

> ChapterCards — what a source says a chapter's story is — who, what they want, what stands in the way, what it costs, how it begins and ends.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: the plan's treatment (Phase 2b: one paragraph per movement — who, what the figure wants and does, with which object and where, what it
> costs and what cannot be undone, hook-in and hook-out as events, in Akt I the chapter's one concrete falsehood) and
> the September packet's scene load (GOAL.md 5.5: a local goal, two counterforces, two bad options, irreversibility). The
> developmental-editor's scene-chain audit asks the same of every scene: who wants what, what happens if not, why now.
> measured against: the readings on the chapter pages; a card whose chapter resolves to a page of the wiki is the attachable subset. A quote is placed by read.py --find (P26).
> may not: write a treatment paragraph or decide what a chapter is — a field is a P_HE_CHAPTER candidate for the paragraph the session proposes and the author approves; nor reconcile two plans' chapters
> retire when: on three plot-outline documents the treatment's paragraphs use none of the fields offered

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/chaptercards-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.0472, 14.5 s. **1 rows**: 1 candidates, 0 refused, 0 duplicates.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | Kapitel 39 | Kael | who | asserts | In Kapitel 39 müssen wir beschreiben, wie Kael spürt, dass die Aufmerksamkeit schwindet | 48 |

## `2026-09-14-kap25-vertiefung-md`

8 calls (0 failed), 8 chunks (0 without a valid reply), $0.1615, 63.1 s. **6 rows**: 6 candidates, 0 refused, 0 duplicates.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | Masterplan-Zeile 25 | zwei genuine Zukunftsverluste | cost | cites | Masterplan-Zeile 25 verlangt „zwei genuine Zukunftsverluste | 17 |
| 2 | relation_reading | candidate | Kap 26 | ihr Vorbeigehen an der Tür | who | asserts | ihr Vorbeigehen an der Tür in Kap 26 ist vorbereitet | 22 |
| 3 | relation_reading | candidate | Kap 25 | Wartungsschächte | place | asserts | Das löst den Canon-Weltanker für Kap 25 ein (KW3, Wartungsschächte, Anker 734 dritte Wiederkehr) | 23 |
| 4 | relation_reading | candidate | Kapitel 25 | Kapitel 25 ist in keiner der beiden Dateien encodiert | object | asserts | Kapitel 25 ist in keiner der beiden Dateien encodiert. | 51 |
| 5 | relation_reading | candidate | Kap 25 | **Abwesenheit** des Klicks | object | asserts | Kap 25 verwendet die **Abwesenheit** des Klicks lokal | 57 |
| 6 | relation_reading | candidate | Kap 25 | Treppenkopf, Wartungsebene | place | asserts | Kap 25 löst KW3 jetzt **sensorisch** ein (Treppenkopf, Wartungsebene) | 60 |
