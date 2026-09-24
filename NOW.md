# Now

*What is open, and what a person still has to decide. **No counts live on this
page.*** Numbers come from `python3 scripts/state.py`; the few that appear in
prose here carry a `<!--state:key-->` marker and `--prose` fails if one drifts.

```bash
python3 scripts/state.py            # everything, derived now
python3 scripts/state.py --prose    # fail on any stale number in this file
```

## Open decisions — these are judgement, not measurement

**How far the yes to TypeSafe reaches.** On 2026-09-23 the author said yes twice.
First to „a small test on the two documents with a reader's list", which sent
those two documents' passages. Then, the same day, to using Jev and OpenRouter's
free models for the German–English entity mapping (below). That run sent Jev up to
two lines of context per surface for 18,026 surfaces and up to four lines per pair
for 11,277 pairs, drawn from across the landed corpus. The free models got **names
only**, because a free endpoint may keep what it is sent. Anything beyond those two
uses should be asked for again, with its cost.
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

**Which model runs are allowed — the toolchain is built and has called no
model.** On 2026-09-23 the author asked for the wiki to become a knowledge base
and a knowledge graph for GraphRAG, and for everything usable from the nine DSPy
repositories to be ported. It is (`CLAUDE.md`, *The knowledge graph* and
*Calling a model*). Three runs are now one command each, and each sends corpus
words to OpenRouter, so each waits on its own yes — `--approval` is required
and refused when empty:

- `pairs.py run --optimizer labeled` — the cheapest rung, on the residual
  `fold()` leaves. Cost: the surface pairs and their rules, a few thousand tokens.
- `graphrag.py ask "…" --answer` — a model picks evidence numbers. Cost: the
  question and eight quotations per call.
- `rlm_ingest.py <slug>` — a whole document. Needs Deno as well.

**How far `ask` may go.** `graphrag.py` returns verified quotations and never
prose, because prose over two sources is a merge (P13). Whether an answer should
ever be more than chosen quotations — a framing sentence, a summary marked as
the model's — is the author's to decide, and nothing builds it until then.

**Where `GOAL.md` and this repository's rules disagree — the author's to settle
before Phase 0 of the goal starts.** `GOAL.md` is now the project's general
goal. Four places where it and the working agreement cannot both hold as
written:

- **The novel's sources — decided for Drive, open for the rest.** The author
  said on 2026-09-23 that the sources are all in `Sources/`: the manifest
  catalogues every Drive document, the canon-era ones included, so they land
  through `sources.py` like any other. 33 <!--state:sources.canon_era--> rows date
  from May 2026 on and 33 <!--state:sources.canon_era_landed--> are landed, since
  2026-09-24 (see *Landed* below); none has been read yet. Still open: the
  manuscript and the NCP files, which are not Drive documents and sit only under
  `Legacy/`, and the claude.ai exports the goal names, which are in no catalogue.
- **Conflict detection.** The goal wants a detector: deterministic comparison per
  predicate, then model adjudication of candidates, with quotations. `CLAUDE.md`
  says conflict detection is never mechanised, because a guesser reproduced the
  `Zero-Trust` false conflict. The goal's deterministic half may fit P1; its
  model half is the open question.
- **Layout.** The goal specifies `kg/`, `wiki/`, `tools/kpkg/`, a `kp` CLI and
  `SPEC.md`. This repository has `Sources/`, `Wiki/`, `scripts/` and two layers
  (P20). `graph.py` and `graphrag.py` already cover part of `kg/` and `kp ask`.
- **Status tags.** The goal's `[K] [V] [S] [L] [D] [M]` and tiers T0–T5 do not
  exist on any page here; the wiki's pages carry readings attributed by source
  and date. Whether they are added, and how they map, is a schema decision (P4:
  no field without instances).

## Handover — the next session starts here

Run `python3 scripts/selftests.py` first; it builds nothing and says in one line
per suite what holds. In a fresh container the DSPy suites report `not run`
with the command that creates `.venv-dspy`.

In order, and none of it needs a model:

1. **More retrieval cases.** `graphrag.py bench` has
   9 <!--state:graphrag.cases--> cases, all written by the hand that wrote the
   pages. The `## Open` sections (`relations.py --open`) are a second source;
   write `(question, gold pages)` by hand first. `Plan/concept/graphrag_2026-09-23.md`
   has why and the next four steps after it.
2. **The morphology rule** — once its reach is decided (above), it is one entry
   in `pairs.py`'s `RULES` and `pairs.py score --rule <name> --record` puts it on
   the ledger against `fold()`'s floor.
3. **qmd as a second seed source for `graphrag.py`**, measured on the bench
   against folded seeding — the floor row is already in `Plan/runs/baselines.jsonl`.
4. **Record routing failures** — each time an agent loaded the wrong skill or
   none. Five to twenty of them are job 4's dataset; there are none, so it has
   not started.
5. **English retrieval cases, to measure the glosses.** `graphrag.py ask --gloss`
   routes `Core Worlds` to `kern-welten` through a gloss the corpus writes, and
   the bench cannot see it — every case names a German term. The four questions
   asked in English, by hand, are the cheapest honest test.
6. **The entity layer grows with the entity lists, not by itself.** Only lists
   that verify as readings feed `graph.proposals()`, and only one unread
   document has one. The full entity run (above, *Half-done*) is what makes
   `graphrag.py`'s unread-document routes worth having.

Two things the build found, fixed in place:

- `Plan/trainsets/surface-pairs.jsonl` had gone stale — 17 rows against a
  ledger that had grown. Re-exported; `pairs.py` reads the ledger live.
- `graph.py`'s first pairing of quotations to citations disagreed with
  `quotes.py` (14 unresolved against 4). The pairing moved into
  `quotes.pairs` / `quotes.verdict` and both use it; `quotes.py`'s own numbers
  did not change.

## Half-done — the entity lists

`scripts/entities.py` works; the lists it searches exist for four documents.
4 <!--state:entities.lists--> lists exist and 3 <!--state:entities.readings-->
pass verification — 317 <!--state:entities.rows_verified--> of
317 <!--state:entities.rows--> rows cite a line holding the entity.

**Revision 3 made the rule structural, and it held.** The reader returns names
only, into `Plan/entities/names/<slug>.json`; `entities.py place` writes every
line and refuses a name the document does not contain word for word. Re-piloted
on the same four slugs, 2026-09-23:

| list | rows placed | names refused | | F1 (rev 2 → 3) |
|---|--:|--:|---|--:|
| `aegis-subplots-kapitelweise-system-exploration-docx` | 70 | 14 | reading | 0.28 → 0.25 |
| `kohaerenz-protokoll` | 82 | 13 | **one line unread** | — |
| `ki-agenten-kohaerenz-und-prompt-generierung` | 68 | 22 | reading | — |
| `roman-lokalitaeten-konzept-und-ausarbeitung` | 97 | 0 | reading | 0.67 → 0.69 |

- **Every row verifies because no row was typed.** The refusals are the forms
  revision 2 would have written anyway: `McLaughlin-Graph` where the text has
  `McLaughlin-Graphen`, `Nicht-Lokalität`, `Koherentz Lücke`. They are listed in
  each file's `refused:` line rather than lost.
- **`kohaerenz-protokoll` is not a reading by one line.** Its reader reported
  `read_to_line` 2497 of 2498. `verify` treats any stated gap as disqualifying,
  and that rule was left alone: whether a one-line gap should demote a list is a
  decision, not a fix. Also: `read_to_line` is still the reader's claim. `place`
  prints the furthest line any name landed on beside it, which is code's — but a
  lower bound only, since a name is placed at its first occurrence.
- **Revision 3 found a defect in the checker, not only in the reader.**
  `quotes.normalise` drops a one- or two-digit number glued to a word (footnote
  debris), so on the line `(KW2),` became `(KW),` while the name stayed `KW2` —
  a name ending in a digit could never verify. Revision 2's gazetteer lost
  `KW2`–`KW4`, `Kern-Welt 1`–`4` and `Silent Hill 2` to it and blamed the reader.
  `entities.py` now asks one question for placing and verifying, `holds()`:
  whole word, one line, the normalisation minus the footnote rule. It is
  stricter than revision 2's substring test (`Kontakt` no longer passes on
  `Kontaktaufnahme`), and `selftest` carries seven cases that prove it can fail.
  Quotations are untouched: there the footnote rule is symmetric.
- The four readers cost 423,531 subagent tokens and about 75 s wall-clock, run
  in parallel as four Haiku agents with the workflow's prompt verbatim, not
  through the Workflow tool.

**Jev was tested on the same two documents, and it lost on quality.**
`scripts/jev_entities.py` takes candidates from a script (every capitalised
token, compound and bold/code/table-cell span, with its first file line) and asks
Jev one Noul per candidate over the 40-line window it first occurs in. Recorded
in `Plan/runs/jev/<slug>/`; `--replay` reruns it with no key.

| | gazetteer F1 | `aegis-subplots` F1 | lines right | time / doc | input tokens / doc |
|---|--:|--:|--:|--:|--:|
| Haiku, revision 1/2 | 0.67 | 0.28 | 85–95% | ~2 min | ~110k |
| Jev, top 100 by p | 0.47 | 0.10 | 99% — by code | 6 s | ~410k |
| every script candidate | 0.09 | 0.04 | — | — | — |

- **Faster by about 20×, cheaper by about 4× in money, not in tokens.** Jev is
  $0.042 per million input tokens and output is free (OpenRouter, 2026-09-23);
  Haiku is $1/$5. The whole corpus, 110,796 lines, is roughly $3 with Jev.
  The token count is high because each of ~2,100 questions per document repeats
  its wording; the state is paid once per window.
- **The candidate script caps recall at 0.80 and 0.63.** It misses multi-word
  names with a space in them (`Externe Ebene`, `Kern-Welt 1`) and splits none of
  the slashed forms (`Juna/V`). That ceiling is code's, and fixable.
- **Jev says yes to 20% of candidates** and ranks cited authors highest
  (`Sartre`, `Camus`, `Chinese_room` from footnote URLs) on `aegis-subplots`. It
  did what the question asked — the definition includes „a cited work or
  author" — which is the same open question the Haiku pilot raised, answered
  more sharply: the definition decides the list, not the model.
- Near-duplicates crowd the top 100 (`Neuromancer`, `Neuromancer (Roman, 1984)`);
  folding parentheticals is code, not judgement.

**What this means:** Jev is not a replacement for a reader here, but it is a
cheap filter behind a better candidate script. The gold lists are noisy too —
each carries a reader's notes as `- ` lines, which no list can match.

**Next, in this order:**

1. Decide whether a one-line stated gap disqualifies a list (above), or have the
   reader of `kohaerenz-protokoll` finish the line.
2. The other landed documents. Four readers cost about 424k subagent tokens; at
   that rate 342 more documents are roughly 36M, scaled by length rather than
   count. Say what the full run costs before starting it, and ask.
3. Then `entities.py matrix`, `missing`, and `doc` on the candidates for the next
   document below.

**Open question the pilot raised:** on `aegis-subplots` the model took the
research vocabulary where the reader took the world (F1 0.13, against 0.67 on the
gazetteer). Which of the two a corpus-wide entity list should hold is the
author's call, and the prompt's definition of an entity is where it would be
written. `Plan/concept/entity-lists_2026-09-23.md` has the argument.

## German and English names — mapped, not merged

`scripts/bilingual.py` maps the German and English surfaces of one entity across
the whole corpus. `Plan/entities/bilingual.md` holds the pairs and
`Plan/entities/bilingual.jsonl` holds every judged entity with its counterparts.

- **stated**: code found 12,526 glosses the corpus writes itself, `A (B)` and `A/B`,
  8,129 of them with at least one side an entity.
- **entities**: Jev accepted 6,989 of 18,026 surfaces as entities or key terms.
  The spot check was sound: `Wächter` 0.83, `Guardian` 0.93, `Ziel` 0.17, `Die` 0.11.
  One article got through, `Das` at 0.73, and the write stage now drops bare articles.
- **propose**: four free models, given names only, proposed counterparts.
  2,312 entities have one the corpus contains, and 34 names were never answered.
- **pairs**: Jev chose one relation for each of the 11,277 pairs:
  3,785 translation (2,474 at p ≥ 0.8), 989 abbreviation, 250 variant,
  2,465 role or part, 3,783 distinct.
- **Cost**: 1,015 Jev calls and 10.9M input tokens, about $0.46. Plus 99 free
  calls, which took 70 minutes, because only `nemotron-3-super` and
  `dots-3-note` answered a batch of 80 reliably.

**What needs a person.** The high tier reads right on the pairs the wiki cares
about: `Kernwelten`/`Core Worlds` in 8 documents, `Überwelt`/`Overworld` in 5,
`Risse`/`Rifts` in 3, `Handlungsfähigkeit`/`Agency`, `Erleben`/`Qualia` in 15.
Even there it holds naming relations Jev called translations: `Logik`/`LogOS` 0.85
is a guardian named for its domain. Below 0.8 the list is noisy, with
`Signposts`/`Transits` 0.63. No pair has entered `judgements.jsonl`. Reviewing the
high tier into it is the next step, and it is a person's.

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

**`Wächter` and `Guardian` do meet, and the corpus says so.** Two read documents
use them in complementary distribution, and that held for those two only. Across
the corpus 44 documents contain both, and
`umfassendes-lokalitaeten-konzept-fuer-roman` L31 writes „den entsprechenden
Wächter (Guardian) von AEGIS". That is the document that line was waiting for:
it states the equation rather than leaving it to be inferred. It has not been
read. Whether the two are one term is still `judgements.jsonl`'s question.

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

## Landed

**The canon-era documents, 2026-09-24, on the author's yes.** `sources.py fetch
--since 2026-05-01 --include-md` landed the 29 remaining rows dated May 2026 or
later, none failing. 26 were `md`, which `fetch` skipped before: the two new flags
are opt-in, and `md` takes the same text route that landed the four `md` rows on
2026-09-16. `dedupe.py --apply` then folded four copies — three `-2` exports two
bytes apart, and `25-wegkreuzung-md`, the chapter-25 text of `kp-kap25-2026-09-14-md`
in another escaping — so 37 canon-era rows became 33, all landed. **None is read:**
no census, note or reconciliation. Which to read first is the author's call, and
`GOAL.md` §2 lists them. The copy under `Legacy/Canon/` (six of the 2026-06-10
documents) has not been compared against the landed files.

Pull request netzkontrast/kohaerenzprotokoll#52 merged on 2026-09-23: the TypeSafe
SDK and project skill (`.agents/skills/typesafe`), the Jev concept, the vendored
`jev*` skills, `scripts/entities.py`, the entity pilot and the saved workflow.
Nothing from it is in flight; what it left open is under the headings above.

## Not open

The novel. The `Legacy/` shelf. The 242 unlanded rows, all dated before May 2026:
231 `plot-outline`, 10 `md` in `storyform` and `kernkonzept`, and the one `mp3` —
deferred by decision, not forgotten.
