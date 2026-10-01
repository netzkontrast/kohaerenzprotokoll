# Pitch — the testbed's results

> Pitch — how a source positions the book — logline, hook, genre, comparable titles, audience — with the sentence.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: the developmental-editor's intake (genre and comps, publication path) and agent-first-pages (what a Leseprobe and Exposé promise to a stranger): both begin
> with how the book is positioned, and the sources hold it in scattered sentences.
> measured against: the author's own positioning once given; until then, a record whose subject and phrase stand inside its quote is the precise subset. A quote is placed by read.py --find (P26).
> may not: write a pitch, decide the genre or the comps, or judge whether the book fits — positioning is the author's; a record here is a P_HE_PITCH proposal
> retire when: on three documents a person keeps no positioning beyond the author's own

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/pitch-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.0426, 14.0 s. **0 rows**: 0 candidates, 0 refused, 0 duplicates.

Staging refused the run: `empty or invalid candidate list: not a successful extraction`

The model returned no row on this document.

## `2026-09-14-kap25-vertiefung-md`

8 calls (0 failed), 8 chunks (0 without a valid reply), $0.1093, 32.0 s. **1 rows**: 1 candidates, 0 refused, 0 duplicates.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | Kapitel | wer trifft die Wahl | promise | asserts | das Kapitelversprechen lautet *wer trifft die Wahl* | 21 |
