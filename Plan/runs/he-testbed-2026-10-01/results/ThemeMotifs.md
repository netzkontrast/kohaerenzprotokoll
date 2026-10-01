# ThemeMotifs — the testbed's results

> ThemeMotifs — a premise, a theme or a motif's meaning a source states, with the sentence.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: the developmental-editor's spine (one dramatic question the whole book answers) and workshop-critique's reading of what a piece is about; GOAL.md's tonal
> axis and 5.3's architecture constants (a formula inverted, a lexeme carrying both readings). The wiki's term pages hold every passage about a term; none marks a
> premise or a motif's meaning as such.
> measured against: the author's decision on the book's premise, once taken; until then, a statement whose subject and content stand inside its quote is the precise subset. A quote is placed by read.py --find (P26).
> may not: decide the book's theme, or that a source's premise is the book's — a statement here is a P_HE_THEME proposal for a reader
> retire when: on three documents a person keeps no statement beyond what the term pages already quote

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/thememotifs-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.066, 27.0 s. **7 rows**: 5 candidates, 2 refused, 0 duplicates.

Beside the Haiku pilot of 2026-09-30 on this document: the candidates stand on 5 lines here and 4 there, 3 of them the same.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | Kael | die Manifestation des Lesers | premise | asserts | dass Kael die Manifestation des Lesers ist und seine Welt mit dem Zuklappen des Buches stirbt | 13 |
| 2 | relation_reading | candidate | Ordnungssucht | ein verzweifelter Versuch, den Leser (den Beobachter) bei der Stange zu halten | motif_meaning | asserts | Seine Ordnungssucht ist ein verzweifelter Versuch, den Leser (den Beobachter) bei der Stange zu halten | 28 |
| 3 | relation_reading | candidate | Die Welt | existiert nur so weit, wie der Leser sie sich vorstellen kann | theme | asserts | Die Welt existiert nur so weit, wie der Leser sie sich vorstellen kann. | 35 |
| 4 | relation_reading | refused: surface absent from document | das System | der Verstand des Beobachters (des Lesers) stößt an seine eigenen kognitiven Grenzen | theme | asserts | Wenn das System unentscheidbar wird, liegt das daran, dass der Verstand des Beobachters (des Lesers) an seine eigenen kognitiven Grenzen stößt. | 35 |
| 5 | relation_reading | candidate | Kael | die Sonde, die der Leser in das Trauma geschickt hat | motif_meaning | asserts | Kael ist die Sonde, die der Leser in das Trauma geschickt hat. | 42 |
| 6 | relation_reading | refused: surface absent from document | Er | das Werkzeug, mit dem der Leser versucht, seine eigene Dissoziation zu heilen | theme | asserts | Er ist das Werkzeug, mit dem der Leser versucht, seine eigene Dissoziation (seine Trennung von der Welt) zu heilen. | 42 |
| 7 | relation_reading | candidate | Das Zuklappen des Buches | der „Wärmetod des Universums“ (Entropie) | motif_meaning | asserts | Das Zuklappen des Buches wird als der „Wärmetod des Universums“ (Entropie) geframt. | 46 |

## `2026-09-14-kap25-vertiefung-md`

Not run yet.
