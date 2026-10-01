# LocationRegistry — the testbed's results

> LocationRegistry — the named places one document tabulates or profiles.
> provisional — first design, 2026-09-24; never run on the corpus
> derived from: document 6's own master table (roman-lokalitaeten-konzept-und-ausarbeitung
> L185: Location Name | Reality Level | Source | Narrative Relevance/Function | Key
> Associated Characters). The five fields are that document's columns, not a preference.
> applies to: a document that tabulates or profiles places, and no other
> may not: create a page, decide which places get one (that rule came from document 6
> itself — CLAUDE.md, the sixth reconciliation), supply a count, or assign a level
> retire when: the next document that tabulates places does not fit these five columns

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/locationregistry-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.0395, 11.3 s. **0 rows**: 0 candidates, 0 refused, 0 duplicates.

Staging refused the run: `empty or invalid candidate list: not a successful extraction`

The model returned no row on this document.

## `2026-09-14-kap25-vertiefung-md`

8 calls (0 failed), 8 chunks (0 without a valid reply), $0.1332, 47.4 s. **12 rows**: 0 candidates, 0 refused, 0 duplicates, 12 not staged.

Staging refused the run: `candidate lacks nonempty string fields: source, target, type, quote, stance`

| # | kind | status | name | level | source | function | characters | quote | lines |
|---|---|---|---|---|---|---|---|---|---|
| 1 | item | not staged | Station 7 |  |  |  | Einheit |  |  |
| 2 | item | not staged | Platte 204 |  |  | Abzweigung | Kael |  |  |
| 3 | item | not staged | Delta-Sieben |  |  |  | Kael |  |  |
| 4 | item | not staged | KW3 |  | Canon-Weltanker für Kap 25 |  |  |  |  |
| 5 | item | not staged | Schleusen des Misstrauens | KW3 | [S] — gefiltert: dekanonisierte Guardians (Cerberus, Nox, Echo, Limina) nicht übernommen | Hintergrund für Kontrollpunkt-/Überwachungslogik |  |  |  |
| 6 | item | not staged | Gänge der Paranoia | KW3 | [S] — gefiltert: dekanonisierte Guardians (Cerberus, Nox, Echo, Limina) nicht übernommen | Hintergrund für Kontrollpunkt-/Überwachungslogik |  |  |  |
| 7 | item | not staged | Panoptikum | KW3 | [S] — gefiltert: dekanonisierte Guardians (Cerberus, Nox, Echo, Limina) nicht übernommen | Hintergrund für Kontrollpunkt-/Überwachungslogik |  |  |  |
| 8 | item | not staged | Konstrukt-Stadt |  |  |  |  |  |  |
| 9 | item | not staged | Datenknoten |  |  |  |  |  |  |
| 10 | item | not staged | Wohneinheit 734 |  |  |  |  |  |  |
| 11 | item | not staged | Treppenkopf | KW3 |  |  |  |  |  |
| 12 | item | not staged | Wartungsebene | KW3 |  |  |  |  |  |
