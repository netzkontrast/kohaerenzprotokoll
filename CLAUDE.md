# Kohärenz Protokoll — working agreement

A German hard-SF novel and its research corpus. **Right now only the wiki is
being built.** The novel rests.

**Canon prose is German and is never translated. Engineering and work language
is English.**

## Read this first

`PRINCIPLES.md` is the one place to look before writing a new skill, command,
script, check or page type. It holds the rules we follow, each with the evidence
that produced it, and a catalogue of ideas kept but not yet built.

Everything else on this page describes what currently exists. If you find a
statement here that is not true of the repository, the statement is the defect —
fix it in the same change, or delete it. A description that outruns what exists
is how the previous version of this project failed.

## Two layers

| layer | what it is | who writes it |
|---|---|---|
| `Sources/` | research documents fetched from Drive, immutable once landed | `scripts/sources.py`, nothing else |
| `Wiki/` | term pages derived from those sources, promoted by a human | a person, for now |

There is no third layer. Everything else the project used to have is parked
under `Legacy/` and read by nothing.

`Sources/manifest.jsonl` is the spine: 680 rows, each with `drive_id`, `title`,
`slug`, `category`, `tier` and, once landed, `export_path` and two checksums.
Anything derived traces back to a `drive_id`.

## State, as of 2026-09-17

**409 <!--state:sources.landed--> of 680 <!--state:sources.total--> source documents are landed.** The 271 that are not are the 247
`plot-outline` rows, deferred with the novel, plus the 39 `md` and one `mp3` that
have no route. Every category the wiki needs is complete.

**Those landed files are 357 <!--state:sources.distinct--> distinct documents.**
52 <!--state:sources.near_copies--> of them are near-copies of
another — Drive holds several exports of many documents, and each landed under
its own `drive_id`. Only 2 pairs are byte-identical, so checksums find almost
none of it. `python3 scripts/duplicates.py` measures it, and **a count over files
is not a count over documents**: AEGIS is in 315 files and 276 documents.
Proportions usually survive and sometimes do not — `Entropie` is 50% of files and
45% of documents. Say which one you mean.

**4 <!--state:documents.with_census--> have a term census** in `Sources/terms/`, **4
<!--state:documents.with_note--> have a note** in `Sources/notes/`, and **4
<!--state:documents.reconciled--> are reconciled**. Three of the four are `theorie-physik`, the fourth
`worldbuilding`.

`Wiki/candidates/` holds **46 <!--state:wiki.pages--> pages**, `Wiki/conflicts/`
holds **4 <!--state:wiki.conflicts-->**, and
`Wiki/compare/` holds the reconciliation record per document. The schema follows
the pages rather than preceding them, so `Wiki/terms/` does not exist and nothing
has been promoted.

| document | new terms | new readings | new conflicts |
|---|--:|--:|--:|
| `entropie-aegis` | 14 | — | 0 |
| `aegis-emergenz-aus-der-leere` | 10 | 2 | 2 |
| `kohaerenzprotokoll-aegis-und-systementropie` | 8 | 7 | 1 |
| `guardians-und-kern-welten-konzept` | 14 | 4 | 1 |

`Plan/runs/judgements.jsonl` holds **19 <!--state:judgements.total--> judgements**
about near matches, **7 <!--state:judgements.mechanised-->** mechanised and
replaying green, **0 <!--state:judgements.disagree-->** disagreeing.

**`python3 scripts/account.py order` holds** — `true`
<!--state:order.holds-->. Every document with a census has a note and a
reconciliation, each ran against the state the previous one left, and the wiki
matches what the newest run recorded leaving.

### Do not trust the numbers above — they are checked

Every number on this page carries a `<!--state:key-->` marker naming the
measurement it came from, and **`python3 scripts/state.py --prose` fails if any
of them contradicts the repository.**

That check exists because this section has gone stale four times. It has claimed
27 of 680 landed, then 3 documents read, then 32 wiki pages, 11 judgements, and a
reconciliation of 19/12/7 — each true when written, each wrong within a day, each
caught by a person rather than a command.

**State is derived, never stored.** `scripts/state.py` measures the repository;
`Plan/state.json` is the artifact of a run and not the source of truth. Any tool
that needs a number calls `value("wiki.pages")` instead of hardcoding one, and a
new measurement is a decorated function.

```bash
python3 scripts/state.py            # derive everything, write Plan/state.json
python3 scripts/state.py --prose    # fail on any stale number in prose
python3 scripts/state.py --check    # fail if Plan/state.json has drifted
python3 scripts/state.py --get wiki.pages
```

## One operation, at several scales

The steps below grew one at a time, each with its own script and artifact format.
They are the same operation with different arguments:

    account(subject, question) -> account

| subject | the account |
|---|---|
| a document | the census, the note |
| a term | the page |
| two surfaces | one term or two — `Plan/runs/judgements.jsonl` |
| the corpus | a count, a plan, a timeline |

And each decomposes into the same operation on smaller subjects: a term across
315 documents is that term in each, then the merge.

**A pipeline of N steps needs N rule sets, N formats and N learnings files, and
grows forever.** One recursive operation needs one, and what grows instead is the
library of decompositions in `scripts/rules/` — the part a project actually
learns. `scripts/account.py` is the verb; `scripts/subject.py` is the substrate
every script asks, which is why the frontmatter boundary now has exactly one
implementation instead of four.

That framing is `Plan/concept/rlm-the-real-one_2026-09-17.md` and it is **newer
than the steps below**, which still describe how the work is actually done.

## The process

Seven steps. Three of them are a person.

```
Drive ──fetch──→ Sources/drive/*.md ──┬──extract──→ Sources/terms/*.md
                                      │                    │
                                      └──read─────→ Sources/notes/*.md
                                                           │
                                                      reconcile ──→ Wiki/compare/*.md
                                                           │
                                                        gather
                                                           ▼
                                                Wiki/candidates/*.md
                                                           │
                                                   review (a person)
                                                           ▼
                                                   Wiki/terms/*.md ──→ ask
```

Written out in full in `Plan/concept/wiki-process_2026-09-16.md`. The short
version: **a census lists every candidate term in one document, exhaustively.**
A note harvests what that document says about the terms that matter, quoting with
line numbers.

**A census describes one document and nothing else** — no count, comparison or
expectation from another source. `scripts/profile.py` makes that identical
treatment mechanical rather than a promise, and `Plan/briefings/extract.md` is
read before the document: it carries **procedural** knowledge (what German Drive
exports do) and never **document** knowledge (what some other file said).

Documents meet in `reconcile`, which compares one frozen census against the
**current pages** rather than against every earlier document. Its record is
per document and append-only. The first three comparisons were full
re-comparisons and each superseded the last — that was the step telling us it did
not scale.

**Extraction's independence is what makes reconciliation safe.** The census is
frozen before the wiki is consulted, so the accumulated state cannot decide in
advance what a new document is allowed to say.

**And reconciliation never reads the wiki.** `scripts/wiki_index.py` derives
`Wiki/index.json` from page frontmatter; `scripts/reconcile.py` answers by lookup
and prints only what no lookup settles. Cost per document is `O(census) +
O(judgement)`, not `O(wiki)` — measured on document 4 against 32 pages: 22
candidates, **3 surface groups folded to one term first, then 19 candidates, 15
decided mechanically, 4 to judgement.** Reasoning:
`Plan/concept/reconciliation-by-lookup_2026-09-17.md`.

### A quotation is checked against its line

`python3 scripts/quotes.py` verifies that every „…" ^[Lnn] in a census, note or
wiki page still resolves to the line it cites. Nothing checked this before, and
the first run found quotations that were right about the line and the meaning and
**wrong about the words** — „das Management" for „dem Management", a nominative
written for a genitive. A citation that looks precise around a sentence the
document never contained is the worst shape a defect takes here.

Most of building it was learning what is *not* a defect: export escaping,
markdown emphasis, blockquote wrapping, glued footnote numbers, inline
attribution markers. It says how many quotes it could not check rather than
counting them as passed.

**Conflict detection is never mechanised.** Two readings can only be compared by
reading them, and a program that guessed would reproduce the `Zero-Trust` false
conflict.

### A mechanised rule stays checkable

Every decision about a near match is recorded in `Plan/runs/judgements.jsonl`
with the two surfaces, the decision, the rule, and whether any code now claims
the case. `python3 scripts/judgements.py` **replays all of them against the
current code**:

- `agrees` — the code still decides what the person decided
- `DISAGREES` — go and look. The code changed, the record is wrong, or a rule has
  met its first exception
- `judgement` — no code claims this; still a person's call

**Run it after touching `fold()` or any matching rule.** A rule that was
mechanised and then quietly stopped holding is invisible otherwise — which is not
hypothetical: the check's *first run* found that `fold()`'s own docstring claimed
behaviour it did not have, and the same false claim had been repeated in two other
files.

**And note what it cannot see.** `fold()` was correct the whole time
`reconcile.py` excluded exact fold-equality from its own intra-list check, which
reported three worlds as six new terms. The ledger replayed green throughout,
because no recorded judgement covered the caller. **A green replay says the
recorded decisions still hold, not that the code around them is right.**

`Plan/learnings/extract-terms.md` has the fourteen special cases the first two
censuses found, and why the first comparison inverted the premise the step was
built on.

**Format is measured; stance is read, per passage; neither is a document type.**
There is no enum of document kinds — how a document came to be says nothing about
how it is built, and a single document holds several stances and usually marks
them itself (decision 004).

A term page collects every source's reading of one term, **attributed and
unmerged** — where sources disagree the page says so and stops. Which reading is
right is the author's call, never the page's.

## Searching the corpus

`qmd` (github.com/tobi/qmd) indexes five collections — `sources`, `wiki`,
`census`, `notes`, `plan` — and answers a lowercase German phrase in about 0.2s
with file and line. `scripts/corpus.py` cannot: its index holds capitalised
tokens only, and anything else falls back to reading all 409 files.

```bash
export PATH="$PWD/.tools-node/node_modules/.bin:$PATH"
qmd search "blinder Fleck kategoriale Unfähigkeit" -c sources -n 6
```

**It finds candidates; it does not produce answers.** A ranked result is a place
to look, and every number that goes into a page or a learning still comes from
`corpus.py`, `duplicates.py` or a count — which say what they counted and how.
Nothing in the pipeline depends on qmd, and `.qmd/` and `.tools-node/` are
git-ignored; `qmd init` and five `collection add` calls rebuild it.

Its first real query is what exposed the 52 near-duplicates above.

## Fetching

The one automated step. Documents are large and the bytes never need to pass
through a model:

```bash
python3 scripts/sources.py next --category theorie-physik --limit 5
```

For each `drive_id` returned, call `mcp__Google_Drive__read_file_content`. The
result does not come back inline — it spills to a file and the call reports a
path in what looks like an error. That is the good path. Then:

```bash
python3 scripts/sources.py land --drive-id <id> --consume
```

which parses the spill, normalizes, writes `Sources/drive/<slug>.md`, records
both checksums into the manifest and verifies. Never open the spill yourself.

44 of the 680 rows are markdown or audio, which the connector does not list as
supported — though 4 of the 43 `md` rows landed anyway, so the list is not the
whole truth. The remaining 39 and the one `mp3` stay deferred by decision.
`Plan/learnings/fetch.md` has the format census and the heading measurement.

## Installing anything

**Every dependency goes into a virtualenv. Never into the system Python.**

`pip install --break-system-packages` was tried once and broke `cryptography`
for the whole container, which took the system interpreter down with it.

```bash
python3 -m venv .venv-tools
.venv-tools/bin/pip install <package>
```

`.venv-tools/` holds the tooling dependencies — markitdown and its converters
today — and is git-ignored. `scripts/sources.py` stays standard-library and
shells out to that interpreter for the one thing that needs it, so the tool
keeps running whether or not the venv exists and says exactly how to create it
when it does not.

## Changing your mind

Two different things get corrected here, and treating them the same way is how
this project has gone wrong in both directions at once.

### A claim is measured, or marked unmeasured

A claim says something is true of the repository or the corpus. „Google Docs lose
their headings." „Both names changed on the same day." **A claim is either backed
by a count or explicitly marked as not yet counted.** When a measurement
contradicts it, it is simply wrong: change it, and leave the correction beside it
with how it went wrong.

The failure mode here is **too slow**. The heading claim was generalised from one
document and survived three successive learnings that built on it before anything
counted the other 359. Three documents looked like a timeline for the renaming,
and a count over 409 showed a cliff.

### A construct is demoted, not deleted

A construct is a field, a category, a name, a folder, a template — `kind`,
`status: asked`, `Wiki/compare/`. **It is not true or false. It is useful or it
is not, and its test is use, not argument.**

The failure mode here is **too fast**, and it is the newer one. When `kind: brief
| critique | result` drew the objection *don't commit to fixed document types*,
the right response was to stop it carrying weight. Instead it was removed
outright, in the same turn, with a decision file arguing the removal. „Don't
commit to it" is not „delete it", and the deletion cost something concrete: the
finding that *a result closes a question an earlier brief asked* needs that
distinction to even be sayable.

**So: a construct is never deleted on first objection.** It is demoted, in place:

```yaml
kind: brief          # provisional — a first-pass guess, not established
                     # may not: explain format, decide how a passage is read
                     # retire when: 20 documents show it predicts nothing
```

Three lines, and they do the work an argument was doing:

- **`provisional`** says out loud that it is a guess, so nothing downstream may
  lean on it without saying so.
- **`may not`** is the objection, kept — usually the objection is not that the
  thing should not exist but that it was reaching too far. Write down the reach
  it loses.
- **`retire when`** names the evidence that would end it, so the next argument is
  a measurement instead of a preference.

A construct that has carried a `may not` for twenty documents without once being
useful can go, and then it goes quietly — no decision file is needed to stop
using something nobody used.

### When a construct really does have to go

Delete it when it is **actively wrong**, not merely unproven: when keeping it
would make someone assert something false. Then it leaves with a decision file
and its idea is written down where it can be picked up again — `PRINCIPLES.md`
has a catalogue for exactly that, and a shelved idea with its use case attached
costs nothing to keep.

### The asymmetry, stated plainly

**Be quick to measure a claim and slow to remove a construct.** The two feel like
the same virtue — being responsive to evidence — and they are opposites. A claim
that survives because nobody counted is a lie the repository tells itself. A
construct that dies on first objection takes with it every question it was the
only way to ask.

## Committing a wiki page

**Every revision of a page in `Wiki/` is committed immediately, and the commit
message names the source document the change came from.**

Not at the end of a batch, not once per session. One page changed is one commit,
and the first line says which document caused it:

```
aegis: second expansion from aegis-emergenz-aus-der-leere
entropie: schöpferische Matrix from aegis-emergenz-aus-der-leere, conflict C2
guardians: five named bearers from guardians-und-kern-welten-konzept
```

Several pages may share a commit **only when one source document caused all of
them in one reconciliation**, and the message still names that document.

### Why

A term page accumulates readings from many documents over months. Without this,
`git log` says a page changed and not why, and the only way to find out which
source added a claim is to read every version. With it, `git log --oneline
Wiki/candidates/aegis.md` is the page's provenance — which document contributed
what, in order, for free.

It also makes a wrong reading removable. If a document turns out to have been
misread, every page it touched is one `git log --grep=<slug>` away.

**A commit that changes a page without naming a source document is the defect**,
the same way a false statement on this page is.

## Every step keeps its artifact

A census is the output of six steps. Five of them used to run in a terminal and
vanish, which made the process impossible to study — you could not tell how a
census was arrived at, compare a model against a person, or see what a probe
would have caught.

`Plan/runs/<slug>/` holds one directory per document: the profile, the probes,
**the candidate list written while reading**, the counts, the verification runs,
and the timings. `scripts/capture.py` writes what is deterministic and refuses to
count before a candidate list exists, because counting first decides what gets
seen.

**The candidate list is the one artifact a program cannot produce**, and it is
the baseline anything automated gets scored against. The first four documents
have none — it was never written down — so their reconstructions are marked as
reconstructions and **cannot serve as a gold set.** `Plan/runs/README.md` says so
plainly rather than papering over it.

## Learnings

`Plan/learnings/` holds one file per step: what was learned, what the tool must
handle, what stays judgement, and real measurements. Steps that have not run yet
carry predictions instead, so the eventual learning can be checked against what
we expected.

**Write in them as you go.** They are how a step done by hand becomes a tool
later without re-deriving the reasoning.

## Tracking work

`NOW.md` holds what is open right now, one page, and things leave it when they
are done. `Plan/decisions/` holds one short file per decision, permanently —
what was chosen, what was rejected, what would change our mind. Git holds
everything that happened. There is no board, no status field and no backlog.

## `Legacy/`

The novel, the graph, the codex, the old planning record and the retired
commands are parked there. No script reads it, nothing in `Wiki/` or `Sources/`
mentions it, and it is not part of any workflow. `README.md` says in one
sentence what it holds.

It is a shelf, not a layer. If it starts being referenced, it has become a layer
again — and that is the thing being removed.

**One exception, and it is deliberate:** `Plan/` cites it where a measurement
came from there — the two live pilot runs of the retired pipeline are the only
data on what this work costs at scale, and evidence without its provenance is
just a number someone asserted. Citing where a fact came from is not the same as
depending on the file. Nothing is read from `Legacy/` at run time.
