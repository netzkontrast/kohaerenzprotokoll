# TermCensus — the testbed's results

> TermCensus — the terms of one document, as the document writes them.
> provisional — first design, 2026-09-24; never run on the corpus
> derived from: the reader's lists (Plan/runs/<slug>/03-candidates.md) and the entity-lists
> reader prompt (.claude/workflows/entity-lists.js), whose entity kinds it keeps
> may not: seed or replace a reader's 03-candidates.md, create a page, supply a count,
> or merge two surfaces. No field carries a line: names in, lines by code (P26).
> retire when: on documents 5 and 6 it scores below the Haiku entity lists against the
> same gold (entities.py score: F1 0.25 and 0.69)

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/termcensus-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.0586, 25.1 s. **18 rows**: 0 candidates, 0 refused, 0 duplicates, 18 not staged.

Staging refused the run: `candidate lacks nonempty string fields: term, quote, stance`

| # | kind | status | term | type | scope | quote | lines |
|---|---|---|---|---|---|---|---|
| 1 | item | not staged | Kael | person | world |  |  |
| 2 | item | not staged | AEGIS | system | world |  |  |
| 3 | item | not staged | Große Stille | concept | world |  |  |
| 4 | item | not staged | Glitch-Momente | concept | world |  |  |
| 5 | item | not staged | Primären Beobachtungs-Einheit | concept | world |  |  |
| 6 | item | not staged | Externen Taktgeber | concept | world |  |  |
| 7 | item | not staged | Einheit | concept | world |  |  |
| 8 | item | not staged | Kohärenz Protokoll | system | world |  |  |
| 9 | item | not staged | Juna | person | world |  |  |
| 10 | item | not staged | AEGIS-Protokolle | system | world |  |  |
| 11 | item | not staged | Beobachtungsstatus | concept | world |  |  |
| 12 | item | not staged | Gedanke eines Fremden | concept | world |  |  |
| 13 | item | not staged | Grenzen der Mathematik | work | lens |  |  |
| 14 | item | not staged | Wärmetod des Universums | concept | lens |  |  |
| 15 | item | not staged | Entropie | concept | lens |  |  |
| 16 | item | not staged | Dissoziation | concept | lens |  |  |
| 17 | item | not staged | Foreshadowing | concept | lens |  |  |
| 18 | item | not staged | Beobachter-Fokus | concept | world |  |  |

## `2026-09-14-kap25-vertiefung-md`

Not run yet.
