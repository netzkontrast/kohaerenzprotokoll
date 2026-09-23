# Now

*What is open, and what a person still has to decide. **No counts live on this
page.*** Numbers come from `python3 scripts/state.py`; the few that appear in
prose here carry a `<!--state:key-->` marker and `--prose` fails if one drifts.

```bash
python3 scripts/state.py            # everything, derived now
python3 scripts/state.py --prose    # fail on any stale number in this file
```

## Open decisions — these are judgement, not measurement

**Whether corpus text may be sent to TypeSafe at all.** Jev is installed two
ways — the SDK in `.venv-typesafe` and the vendored `jev*` skills with their
`jev-decide` CLI — and nothing calls it. The author chose **route A, real Jev**
for the vendored skills; that chose a provider, not permission to send the
novel's research to a third party. Every call waits on that yes, and the first
real call uses a small synthetic input.
`Plan/concept/jev-in-ingestion_2026-09-23.md` has the three placements and what
each would send.

**Both Jev keys are present** in the environment (checked 2026-09-23, presence
only). That removes the technical block and none of the permission one above. A key pasted in chat earlier in
the session that installed this should be treated as spent and rotated.

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
203 <!--state:quotes.unchecked--> quotations cannot be checked at all, because
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

## Half-done — the entity lists

`scripts/entities.py` works; the lists it searches do not yet exist.
4 <!--state:entities.lists--> lists exist and 2 <!--state:entities.readings-->
pass verification — 337 <!--state:entities.rows_verified--> of
372 <!--state:entities.rows--> rows cite a line holding the entity.

**Revision 2 was re-piloted on the four slugs and the prompt rule did not hold.**
Measured per list:

| list | verified | |
|---|--:|---|
| `aegis-subplots-kapitelweise-system-exploration-docx` | 84/88 | reading |
| `kohaerenz-protokoll` | 92/93 | reading, read to L2498 of 2498 |
| `ki-agenten-kohaerenz-und-prompt-generierung` | 73/88 | reconstruction |
| `roman-lokalitaeten-konzept-und-ausarbeitung` | 88/103 | **not re-read** |

- **Haiku still typed lines.** Every failing row checked on `ki-agenten` is a
  form `--find` refuses or places elsewhere: „Qualitatives Sprung" is refused
  (the text has „qualitative Sprung", L301) and was written anyway; „Wissensgraph"
  was cited at L321, which says „Knowledge Graph". The prompt asked for
  `--find`; nothing enforced it.
- **The `roman-lokalitaeten` reader did not redo the list.** Its only change was
  relabelling the revision 1 file „(revision 2)", and it returned „written" with a
  summary. The relabel was reverted; the file is revision 1's list.
- `score`: gazetteer F1 0.67 (unchanged — same list); `aegis-subplots` F1 0.28,
  up from 0.13, still the research vocabulary rather than the world.

**The fix is structural, not a better prompt (P26).** The model returns entity
names only; code runs `--find` on each and writes the line, dropping a refused
name. A line a model cannot type cannot be wrong, and „written" becomes a file
code produced rather than a claim. The same split is what makes a cheaper route
possible — candidates by script, a typed judgement per candidate (Jev) — see
`Plan/concept/jev-in-ingestion_2026-09-23.md`; that still waits on the author's
yes to send passages.

**Next, in this order:**

1. Revision 3 of `.claude/workflows/entity-lists.js`: names only, lines by code.
   Re-pilot on the same four slugs; `verify` and `score` as before.
2. Only if every list verifies as a reading: the other landed documents. The
   revision 2 pilot cost 442,682 subagent tokens and 7.5 minutes for four
   documents; say what the full run costs before starting it.
3. Then `entities.py matrix`, `missing`, and `doc` on the candidates for the next
   document below.

**Open question the pilot raised:** on `aegis-subplots` the model took the
research vocabulary where the reader took the world (F1 0.13, against 0.67 on the
gazetteer). Which of the two a corpus-wide entity list should hold is the
author's call, and the prompt's definition of an entity is where it would be
written. `Plan/concept/entity-lists_2026-09-23.md` has the argument.

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
stale.** Each recorded `state_before: 46`; the chain now ends at 56, so both must
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

## In flight on GitHub

Branch `claude/intelligent-davinci-1rujwj`, pull request
netzkontrast/kohaerenzprotokoll#52: the TypeSafe SDK and project skill
(`.agents/skills/typesafe`), the Jev concept, the vendored `jev*` skills,
`scripts/entities.py`, the entity pilot and the saved workflow. No CI runs on this
repository. It waits on the author's review.

## Not open

The novel. The `Legacy/` shelf. The 247 `plot-outline` rows, the 39 `md` and the
one `mp3` — deferred by decision, not forgotten.
