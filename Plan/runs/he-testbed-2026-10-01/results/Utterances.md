# Utterances — the testbed's results

> Utterances — what a figure says in a narrative text, each utterance copied with its speaker and its kind.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: the dialogue-gym's voice drills (distinct voices without speaker tags: cover the tags and see whether you can still tell who speaks), the character card's Voice field, and
> the brief's voice sample of about 200 words. The corpus holds narrative texts of several chapters; who speaks a line is a reading of the attribution.
> measured against: the voice samples a reviewer picks from approved chapters, once they exist; until then, an utterance whose speaker stands within a line of it is the precise subset. A quote is placed by read.py --find (P26).
> may not: write dialogue, attribute a line the text leaves unlabelled — voices the book never labels stay unlabelled — or judge a voice; an utterance here is a P_HE_UTTERANCE sample
> retire when: on three narrative texts a person picks no sample from the utterances offered

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/utterances-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.053, 20.8 s. **3 rows**: 3 candidates, 0 refused, 0 duplicates.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | Juna | Glaubst du wirklich, dein Herz schlägt von selbst? | speech | asks | Juna könnte Kael fragen: *„Glaubst du wirklich, dein Herz schlägt von selbst? | 41 |
| 2 | relation_reading | candidate | Kael | Was tust DU gerade mit mir? | thought | asks | sondern als interne Stimme Kaels, die sich fragt: *„Was tust DU gerade mit mir?“* | 53 |
| 3 | relation_reading | candidate | unlabelled | STATUS: Beobachter-Fokus bei 85%. | log | asserts | STATUS: Beobachter-Fokus bei 85%. Erhöhe narrative Spannung, um System-Abschaltung zu verhindern. | 58 |

## `2026-09-14-kap25-vertiefung-md`

Not run yet.
