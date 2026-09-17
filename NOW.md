# Now

*What is open. One page, hard limit. Finished work leaves this file — git
remembers it. If this does not fit on a page, too much is open at once.*

**Updated:** 2026-09-17

## Done and closed

**Document 4 (`guardians-und-kern-welten-konzept`) is through the whole pipeline**
— census, note, reconciliation against the 32-page state, 14 new pages, 4 new
readings, conflict C4, six judgements. `python3 scripts/account.py order` holds:
every document with a census has a note and a reconciliation, each ran against
the state the previous one left, and the wiki matches what the newest run
recorded leaving.

Four of 409 files done. **The files are 357 distinct documents** — see
`scripts/duplicates.py`.

## Next — and it is chosen, not arbitrary

**`aegis-subplots-kapitelweise-system-exploration`**, because C4 names it.

The blind spot now has two bearers — AEGIS and each Guardian — and neither
document mentions the other's. A corpus search finds a passage in that document
that appears to settle it („Modelliert den Guardian als funktionale Komponente
innerhalb der AEGIS-Architektur"), quoted in the conflict record as evidence
about what to do next and added to no page.

**Four near-copies of it are landed.** One must be chosen and the choice recorded
— `python3 scripts/duplicates.py --groups`. That decision has no precedent yet.

## Open

**`kael-julia-bindung` is probably misnamed (J13).** 1 document, 16 occurrences,
one day. `Kael-Juna-Verbindung`: 9 documents, 31 occurrences, across 14 months.
The page is named after the one document that was read. Renaming it needs a rule
for what a page is called when the corpus and the read sample disagree — there
isn't one.

**`juna.md` is titled by a name none of the four read sources uses**, and
`partnerin` (30 occurrences in document 4, no name given) may be a third surface
for the same entity. Nothing read links them.

**17 quotations do not resolve to the line they cite.** All predate
`scripts/quotes.py`; the pages written during document 4 are clean. They are
mostly German declension changed to fit an English sentence, inside quotation
marks — the same class the check was built for. `python3 scripts/quotes.py`
lists them.

**155 quotations cannot be checked at all**, because they carry no citation on
their own line — usually a table cell whose line number sits in another column.
Either the convention or the checker has to change; neither has been decided.

## Not open

The novel. The `Legacy/` shelf. The 247 `plot-outline` rows, the 39 `md` and the
one `mp3` — deferred by decision, not forgotten.
