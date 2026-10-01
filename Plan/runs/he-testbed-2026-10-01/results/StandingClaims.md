# StandingClaims — the testbed's results

> StandingClaims — what a document says about its own standing or another document's — canon, draft, superseded — with that sentence.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: GOAL.md: sources tiered by precedence. The documents make claims about their own standing; failures.md records the defect
> of applying one. The censuses note them by hand, one section each, and nothing carries them into the graph.
> measured against: the canon claims the censuses record under `What the extraction ran into`; a subject that resolves to a document title or a wiki term is the attachable subset. A quote is placed by read.py --find (P26).
> may not: apply a claim — CLAUDE.md: record what the document says of its own standing and never let it decide anything — rank two documents, or say which canon is true
> retire when: on three documents a person keeps no claim beyond what the census's own canon paragraph holds

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/standingclaims-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.04, 11.3 s. **0 rows**: 0 candidates, 0 refused, 0 duplicates.

Staging refused the run: `empty or invalid candidate list: not a successful extraction`

The model returned no row on this document.

## `2026-09-14-kap25-vertiefung-md`

8 calls (0 failed), 8 chunks (0 without a valid reply), $0.1485, 56.7 s. **7 rows**: 5 candidates, 2 refused, 0 duplicates.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | Weltanker für Kap 25 | Canon | canon | asserts | Das löst den Canon-Weltanker für Kap 25 ein | 23 |
| 2 | relation_reading | candidate | Guardians (Cerberus, Nox, Echo, Limina) | dekanonisierte | deprecated | asserts | dekanonisierte Guardians (Cerberus, Nox, Echo, Limina) | 39 |
| 3 | relation_reading | candidate | Co₁/McL/B/Ly-Taxonomie | nicht der aktuelle KW-Kanon | canon | denies | Co₁/McL/B/Ly-Taxonomie ist nicht der aktuelle KW-Kanon | 41 |
| 4 | relation_reading | refused: joined or shortened quote | Material aus \[S\]-Quellen | wurde als Kanon behandelt | canon | denies | Kein Material aus \[S\]-Quellen wurde als Kanon behandelt | 43 |
| 5 | relation_reading | refused: joined or shortened quote | Material aus [S]-Quellen | Kanon | canon | denies | Kein Material aus [S]-Quellen wurde als Kanon behandelt | 43 |
| 6 | relation_reading | candidate | Vielheit | kanonisch gefordert | canon | asserts | Vielheit wird benannt, **kanonisch gefordert** für 25–26 | 47 |
| 7 | relation_reading | candidate | sensorischer Anker von Vortex 1 Beat 3 | Kanonischer | canon | asserts | Kanonischer sensorischer Anker von Vortex 1 Beat 3 ist | 57 |
