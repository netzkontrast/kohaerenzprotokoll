# Now

*What is open, and what a person still has to decide. **No counts live on this
page.*** Numbers come from `python3 scripts/state.py`; the few that appear in
prose here carry a `<!--state:key-->` marker and `--prose` fails if one drifts.

```bash
python3 scripts/state.py            # everything, derived now
python3 scripts/state.py --prose    # fail on any stale number in this file
```

## Open decisions — these are judgement, not measurement

**A reviewed page has no rule yet.** Nothing has been promoted, so the case has
never arisen: when a new source contradicts a page a person signed off, neither
can silently win. `dspy-wiki-compile` answers it — flag, list the conflicts,
never update in place — and decision 003 does not cover it, because 003 governs
conflicts *between sources*. Needed before the first promotion.
See `Plan/concept/wiki-compile-second-opinion_2026-09-17.md`.

**`kael-julia-bindung` is probably misnamed (J13).** 1 document, 16 occurrences,
one day, against `Kael-Juna-Verbindung` in 9 documents over 14 months. Renaming
needs a rule for what a page is called when the corpus and the read sample
disagree. There is no such rule.

**`juna.md` is titled by a name none of the read sources uses**, and `partnerin`
may be a third surface for the same entity. Nothing read links them.

**Which copy of a near-duplicate is the one to read.** The next document has four
landed near-copies (`scripts/duplicates.py --groups`). One must be chosen and the
choice recorded. No precedent.

**Whether the quote convention or the quote checker changes.**
161 <!--state:quotes.unchecked--> quotations cannot be checked at all, because
they carry no citation on their own line — usually a table cell whose line number
sits in another column. One of the two has to give.

## Next document, and it is chosen rather than next in order

**`aegis-subplots-kapitelweise-system-exploration`**, because conflict C4 names
it: a corpus search finds a passage there that appears to settle whether the
Guardians sit inside AEGIS, in a document with no census, note or reconciliation.
Quoted in the conflict record as evidence about what to do next, and added to no
page.

## Known failing

**17 <!--state:quotes.unresolved--> quotations do not resolve to the line they
cite.** All predate `scripts/quotes.py`; every page written since is clean.
Mostly German declension changed to fit an English sentence, inside quotation
marks. An independent design (`dspy-wiki-compile`) weights this axis heaviest of
six, at 0.30 — so on that reading these are the highest-value open item here,
not cleanup.

## Not open

The novel. The `Legacy/` shelf. The 247 `plot-outline` rows, the 39 `md` and the
one `mp3` — deferred by decision, not forgotten.
