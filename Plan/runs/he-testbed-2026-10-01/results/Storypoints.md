# Storypoints — the testbed's results

> Storypoints — a storypoint a source assigns to a chapter or a throughline — signpost, dynamic, resolve — in one storyform or both.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: GOAL.md 4.3 (`Storyform` A and B, `Throughline` MC/IC/OS/RS, `Storypoint`, `Dynamic`, `Signpost`; edge `carries_storypoint`) and 5.2's dual storyform, which is never
> encoded A wholly before B. The storyform documents list the points by hand, one document at a time; the graph has no edge for them.
> measured against: the storyform pages of the wiki; a record whose chapter resolves to a page is the attachable subset. A quote is placed by read.py --find (P26).
> may not: decide a storypoint or which storyform holds — W1 is the author's; nor apply Dramatica as a checklist: a point here is a P_HE_STORYPOINT proposal, and theory is diagnosis, never recipe
> retire when: on three documents a person keeps no point beyond what the storyform pages already hold

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/storypoints-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.0384, 9.4 s. **0 rows**: 0 candidates, 0 refused, 0 duplicates.

Staging refused the run: `empty or invalid candidate list: not a successful extraction`

The model returned no row on this document.

## `2026-09-14-kap25-vertiefung-md`

8 calls (0 failed), 8 chunks (0 without a valid reply), $0.1254, 41.4 s. **3 rows**: 3 candidates, 0 refused, 0 duplicates.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | 14–22 | KW2 | storypoint | cites | Der Canon weist 14–22 KW2 | 60 |
| 2 | relation_reading | candidate | 23–28 | KW3 | storypoint | cites | 23–28 KW3 zu | 60 |
| 3 | relation_reading | candidate | Kap 25 | KW3 | storypoint | asserts | Kap 25 löst KW3 jetzt | 60 |
