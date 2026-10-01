# Attributions — the testbed's results

> Attributions — which source a passage reports — a person, a theory, a study, another document — with the passage.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: the lab of 2026-09-30 (Plan/runs/reader-lab-2026-09-30/README.md): the class of defect no check saw was voice — a reader
> wrote what the line reports as if the document said it. claims.py flags a report by a list of cue words; this is the
> contract that names the source, so that the graph can tell a document's own voice from the voices it reports.
> measured against: the sentences of a note that a reviewer marks `source:` in the claims table; a pair whose source name stands inside its quote is the precise subset. A quote is placed by read.py --find (P26).
> may not: decide whether the reported source is right, or promote a reported claim to the document's own; a report is a P_HE_SAYS proposal for a reader
> retire when: on three documents a person keeps no attribution beyond what claims.py's cue list finds

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/attributions-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.0498, 16.5 s. **2 rows**: 2 candidates, 0 refused, 0 duplicates.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | Kael | Große Stille | defines | cites | Kael nennt dies die „Große Stille“. | 20 |
| 2 | relation_reading | candidate | AEGIS | Primären Beobachtungs-Einheit | claims | cites | AEGIS spricht in seinen Statusberichten oft von der „Primären Beobachtungs-Einheit“ oder dem „Externen Taktgeber“. | 27 |

## `2026-09-14-kap25-vertiefung-md`

8 calls (0 failed), 8 chunks (0 without a valid reply), $0.1319, 45.0 s. **6 rows**: 3 candidates, 3 refused, 0 duplicates.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | Canon §0 Schleier-Disziplin | Kap 25–26 | recommends | cites | Canon §0 Schleier-Disziplin verlangt genau das für Kap 25–26 | 21 |
| 2 | relation_reading | candidate | Canon §5 | AEGIS bemerkt Kaels neue Klarheit | recommends | cites | Canon §5 verlangt „AEGIS bemerkt Kaels neue Klarheit | 22 |
| 3 | relation_reading | refused: quote not placed | Sprach-DNA | ab Akt II | recommends | cites | die Sprach-DNA es „ab Akt II“ vorsieht |  |
| 4 | relation_reading | refused: quote not placed | Canon | offen benannt | recommends | cites | Canon verlangt „offen benannt“ in 25–26 |  |
| 5 | relation_reading | candidate | Drafting-Brief | Änderungen am Kopf | recommends | cites | Der Drafting-Brief verbietet Änderungen am Kopf außer status. | 58 |
| 6 | relation_reading | refused: quote not placed | Akt I | namenlos | recommends | cites | bleibt aber namenlos („Einheit“), wie es Akt I verlangt |  |
