# Precedence — the testbed's results

> Precedence — what the document puts before or after what — phases, steps, chapters, events — with the sentence.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: the wiki's chapters and plot pages (decision 013), whose order is the unit of the novel, and the phase and act structures the
> plans give differently; the stated graph has no ordering relation between terms or events.
> measured against: the order the chapter pages and `Wiki/overview/plot.md` give; a pair whose endpoints resolve to a wiki term or a chapter is the attachable subset. A quote is placed by read.py --find (P26).
> may not: build a timeline, reconcile two documents' orders, or say a plan and a draft disagree — an order is a P_HE_BEFORE proposal for a reader
> retire when: on three documents a person keeps no order beyond what the chapter pages already give

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/precedence-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.0468, 15.1 s. **0 rows**: 0 candidates, 0 refused, 0 duplicates.

Staging refused the run: `empty or invalid candidate list: not a successful extraction`

The model returned no row on this document.

## `2026-09-14-kap25-vertiefung-md`

8 calls (0 failed), 8 chunks (0 without a valid reply), $0.1338, 42.9 s. **2 rows**: 2 candidates, 0 refused, 0 duplicates.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | Packet | Prosa | before | asserts | Packet: Plan/sessions/2026-09-14-kap25-enrichment-packet.md (vor der Prosa ausgefüllt) | 13 |
| 2 | relation_reading | candidate | sechsmal | siebten Bestand | before | asserts | sechsmal vor dem siebten Bestand | 25 |
