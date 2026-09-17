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

**`juna.md` is titled by a name none of the read sources uses.** `partnerin` was
an open question about whether it names the same entity as `Julia`/`Juna` — one
source now states that link directly (`kohaerenz-protokoll-konzept`, reconciled
2026-09-17): `Partnerin` (V5) is replaced by `Julia`. Recorded as that
document's own claim on `partnerin.md`, not resolved into a merge — whether the
corpus's other `Partnerin` occurrences (23 documents) agree is still open.

**Whether the quote convention or the quote checker changes.**
254 <!--state:quotes.unchecked--> quotations cannot be checked at all, because
they carry no citation on their own line — usually a table cell whose line number
sits in another column. One of the two has to give.

Document 6 made this worse in a useful way: writing the citation *into* the table
cell fixes it, and doing that for nine new pages was the difference between 0 and
9 unchecked on them. The convention that would close this is „a quotation carries
its reference in the same cell", and nothing has decided it.

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

The sixth is done. It was chosen because `kern-welten` asked for `KW2` or `KW4`
and Q4 asked for `Wächter` in an analytic sentence, and it supplied both.

What the wiki now asks for, in its own words:

- **Q1** still wants a document that states the Guardian/AEGIS relation outside a
  question. Two documents now support *components* and neither says it.
- **C5** wants a source that places a garden inside a named Kern-Welt, or that
  uses both `Möglichkeits-Garten` and `Garten der Möglichkeiten`.
- **Q3** wants the alter count. Document 6 bounded the world count and left this
  exactly where it was, because every level names its Alter with „wie".
- **`nexus`** wants anything relating `Nexus`, `Überraum` and `Nexus-Interface`.
  Document 6's table says the third name came from `Plot Teil 1`, which points at
  a plot document.

**And one thing to watch rather than to look for.** Two documents now use
`Wächter` and `Guardian` in complementary distribution with no overlap, and the
index maps neither word to the other. The next document that uses both is worth
more than the next document that uses either.

## Postponed, and safe to postpone because the record proves it

**`orte-konzept-fuer-kohaerenz-protokoll` was reconciled twice and both are
stale.** Each recorded `state_before: 46`; the chain now ends at 58, so both must
be redone against the current wiki. The work is not lost — the censuses, notes
and candidate lists in the two worktree branches stand, and only the
reconciliation depends on the state that moved.

Nothing has to remember this: `Plan/runs/<slug>/reconcile.json` holds
`state_before` → `state_after` for every document and `account.py order` compares
them. **Done is a measurement here, not a tick**, which is what makes postponing
a task safe rather than a promise.

That case is also what `Plan/concept/task-queue_2026-09-17.md` is for. Merging
document 6 invalidated those two reconciliations, left ten pages unlinked and
moved the `fold()` baseline from 65% to 58% — three consequences of one
intended change, none of them written down by anyone. The concept's whole
premise is that a task is derived from measured state, so it cannot be forgotten
and cannot go stale in a list.

## Known failing

**17 <!--state:quotes.unresolved--> quotations do not resolve to the line they
cite.** All predate `scripts/quotes.py`; every page written since is clean. An
independent design (`dspy-wiki-compile`) weights this axis heaviest of six, at
0.30 — so on that reading these are the highest-value open item here, not
cleanup.

`scripts/read.py --find` splits them into two piles that need different work:

- **6 carry the document's own words and point at the wrong place.** Five cite a
  line the phrase is not on; one is a table column holding a bare `128` where a
  `^[L128]` belongs, so the checker paired the quote with the row above.
- **11 quote words the document does not contain on any line.** The nearest line
  is usually the cited one, at 37–79% in common — German declension bent to fit
  an English sentence, inside quotation marks.

**Neither pile is mechanical, and the tempting one is the trap.** „blinder
Hausmeister" on `Wiki/candidates/aegis.md` cites L207 and those exact words are
at L221 — but L207 carries the metaphor the page is actually reading, in the
genitive. Repointing the number would make the citation resolve and the page
wrong. Each correction is a reading decision, one commit per page naming its
source document.

## Not open

The novel. The `Legacy/` shelf. The 247 `plot-outline` rows, the 39 `md` and the
one `mp3` — deferred by decision, not forgotten.
