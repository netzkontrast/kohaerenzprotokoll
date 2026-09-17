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

**Whether the quote convention or the quote checker changes.**
173 <!--state:quotes.unchecked--> quotations cannot be checked at all, because
they carry no citation on their own line — usually a table cell whose line number
sits in another column. One of the two has to give.

**Eight pages carry five identical sentences each — measured, not yet decided.**
`ani` `ars` `ecr` `pms` `rsa` `snk` `ztv` `nullpunkt-protokoll` are the eight
protocols of an „AEGIS-Postulat" that one source analyses rather than authors.
Each page restates the same group fact: the doubly-attributed shape, that the
postulate itself is not in the corpus, and that the term exists only as an
object of criticism. 320 lines, most of them the same.

**Left alone on purpose.** The repetition is what makes each page stand alone,
which is a term page's job, and a construct's test here is use rather than
argument. What would settle it: a later source using one of these protocols as
project vocabulary — which each page's Open section already names as the thing
to watch for. Then the group needs a page and the eight can point at it.

**Which qmd backend this corpus actually wants.** `qmd bench` is an IR
evaluation harness — four backends, precision@k, recall@1/3/5, MRR, latency —
and it has never been run here. `CLAUDE.md`'s advice to write structured
`lex:`/`vec:`/`hyde:` queries rather than a plain phrase is reasoning about
German compounds that nothing has tested. The fixture is nearly free: every
`Wiki/questions/` page and conflict record already says „a search finds this in
`<slug>`". Plan: `Plan/concept/skills_2026-09-17.md`.

**`fold()`'s real baseline is 65%, not 82%, and the misses are systematic.**
Adding thirteen judgements took the trainset from 17 to 26 balanced examples and
the baseline fell from 14/17 to 17/26. Every new miss is a plural or an
inflection — `Guardian`/`Guardians`, `Riss`/`Risse`, `Alter`/`Alters`,
`AEGIS`/`Rest-AEGIS`. `fold()` strips the German definite article and does
nothing else. **The next improvement is a rule, not a model**, and writing it is
a decision about how much morphology a safe deterministic rule may claim.

## Next document — not yet chosen

The fifth is done. Nothing currently names a sixth the way C4 named the fifth, so
choosing it is open. Q1 asks for a document that states the Guardian/AEGIS
relation outside a question; Q4 asks for one using `Wächter` in an analytic
sentence; `kern-welten` would be settled by anything mentioning `KW2` or `KW4`.

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
