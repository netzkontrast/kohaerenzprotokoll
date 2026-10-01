# OpenPoints — the testbed's results

> OpenPoints — what the document itself marks as open, unclear or still to decide, with the sentence.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: GOAL.md: self-generated questions. The wiki's question pages come from readings and from the author; what a document itself
> leaves open is the cheapest source of the next question, and the censuses record it only in prose, one paragraph per document.
> measured against: the open points the wiki's question pages cite; a topic that resolves to a wiki term is the attachable subset. A quote is placed by read.py --find (P26).
> may not: answer the point, write a question page, or say that two documents leave the same point open — a point is a P_HE_OPEN proposal
> retire when: on three documents a person keeps no point that the wiki's question pages do not already ask

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/openpoints-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.0395, 11.9 s. **0 rows**: 0 candidates, 0 refused, 0 duplicates.

Staging refused the run: `empty or invalid candidate list: not a successful extraction`

Beside the Haiku pilot of 2026-09-30 on this document: the candidates stand on 0 lines here and 3 there, 0 of them the same.

The model returned no row on this document.

## `2026-09-14-kap25-vertiefung-md`

8 calls (0 failed), 8 chunks (0 without a valid reply), $0.1181, 36.9 s. **7 rows**: 7 candidates, 0 refused, 0 duplicates.

| # | kind | status | term | stance | quote | lines |
|---|---|---|---|---|---|---|
| 1 | reading | candidate | AEGIS-Benennung ab Akt II | asks | Soll der Name — und das Log-Format — irgendwo in Akt II leserseitig freigegeben werden, und wenn ja, ab welchem Kapitel? | 55 |
| 2 | reading | candidate | Schleier-Benennung | asserts | Autorentscheid nötig. | 56 |
| 3 | reading | candidate | Klick-Motiv-Budget | asks | Ist die lokale Vorform hier gewollte Eskalationsstufe oder vorweggenommenes Material? | 57 |
| 4 | reading | candidate | Header-Szenenplan | asks | Soll der Szenenplan in einem separaten Outline-Pass nachgezogen werden? | 58 |
| 5 | reading | candidate | Einheit Station 7 | asks | Trägt sie in Akt III weiter (Kap 27/28) oder bleibt sie eine Delta-Sieben-Figur? | 59 |
| 6 | reading | candidate | KW-Progression | asks | Ist das die gewünschte Lesart der KW-Progression (Filterregime statt Ortswechsel), oder sollen 14–26 in einem eigenen Pass stärker nach KW2/KW3 verschoben werden? | 60 |
| 7 | reading | candidate | Kernwelt-Mapping Akt II | hedges | Das ist die größte offene Frage des Laufs. | 60 |
