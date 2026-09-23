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

**Then read `NOW.md`.** It is what is open right now — decisions waiting on the
author, work half-done, what failed — and it is the handover between sessions.

### A fresh container has none of the derived things

A cloud session starts from a clean clone. Everything git-ignored is absent, and
each has one command that rebuilds it:

| absent at start | rebuild | needed for |
|---|---|---|
| `Plan/derived/` | `python3 scripts/derive.py` (about 3s) | `corpus.py`'s index path |
| `.venv-tools`, `.venv-dspy`, `.venv-dspytools`, `.venv-typesafe` | the commands under *Installing anything* | only the step that names each |
| qmd, its models and index | `scripts/setup_qmd.sh` | searching; nothing in the pipeline |
| `jev-decide` | under *Installing anything* | the vendored `jev*` skills in API mode |
| `OPENROUTER_API_KEY`, `TYPESAFE_API_KEY` | the environment's settings, never a file or the chat | a real Jev call |

The standard-library scripts — `state.py`, `quotes.py`, `read.py`,
`reconcile.py`, `account.py`, `entities.py` — need none of these.

## Two layers

| layer | what it is | who writes it |
|---|---|---|
| `Sources/` | research documents fetched from Drive, immutable once landed | `scripts/sources.py`, nothing else |
| `Wiki/` | term pages derived from those sources, promoted by a human | a person, for now |

There is no third layer. Everything else the project used to have is parked
under `Legacy/` and read by nothing.

`Sources/manifest.jsonl` is the spine: 617 rows, each with `drive_id`, `title`,
`slug`, `category`, `tier` and, once landed, `export_path` and two checksums.
Anything derived traces back to a `drive_id`.

`Sources/duplicates.jsonl` holds the 63 rows that left it — the same shape plus
`duplicate_of`. Two files, two questions: the manifest says what is in the
corpus, and this says what Drive also holds and why it is not here. It exists so
that „not in the manifest" never has to mean „nobody knows".

## State, as of 2026-09-17

**346 <!--state:sources.landed--> of 617 <!--state:sources.total--> source documents are landed.** The 271 that are not are the 247
`plot-outline` rows, deferred with the novel, plus the 39 `md` and one `mp3` that
have no route. Every category the wiki needs is complete.

**Those 346 files are 346 <!--state:sources.distinct--> distinct documents, and
that took work.** Drive holds up to five exports of the same document — a gdoc
export, a docx export, a `kopie` of each, a second run of both — and each landed
under its own `drive_id`. 409 files were 346 documents, so **every count phrased
as "N of 409" was counting copies.** Only 2 pairs were byte-identical, so
checksums found almost none of it.

`python3 scripts/dedupe.py` folded the
63 <!--state:sources.folded--> extra files away. The file left `Sources/drive/`,
the row left the manifest — 680 rows became 617 — and the full row moved to
`Sources/duplicates.jsonl`, which is what `sources.py next` filters against so a
folded document is never fetched again. `python3 scripts/duplicates.py` now
reports 0 <!--state:sources.near_copies--> near-copies and its job is to keep
saying so after the next landing.

**Which copy survives is not the longest one.** The gdoc export is longer and
carries less: its extra words are `end list` markers — 195 in one document — and
its missing words are the URLs behind the footnotes, which only the docx export
keeps. In 11 of 11 groups holding both formats the docx export carried at least
as many source URLs, and in 10 strictly more. So the rule ranks on URLs first,
export artifacts second, and only then on the name. `scripts/dedupe.py` has the
full order and `Plan/runs/dedupe.json` has the decision per group.

A count over files is now a count over documents — AEGIS is in 269 of the 346 —
but the distinction was real while it lasted and the script that measures it
stays.

**6 <!--state:documents.with_census--> have a term census** in `Sources/terms/`, **6
<!--state:documents.with_note--> have a note** in `Sources/notes/`, and **6
<!--state:documents.reconciled--> are reconciled**. Three are `theorie-physik`,
two `worldbuilding`, one `aegis`.

`Wiki/candidates/` holds **56 <!--state:wiki.pages--> pages**, `Wiki/conflicts/`
holds **5 <!--state:wiki.conflicts-->**, `Wiki/questions/` holds
**4 <!--state:wiki.questions-->**, and
`Wiki/compare/` holds the reconciliation record per document. The schema follows
the pages rather than preceding them, so `Wiki/terms/` does not exist and nothing
has been promoted.

| document | new terms | new readings | new conflicts |
|---|--:|--:|--:|
| `entropie-aegis` | 14 | — | 0 |
| `aegis-emergenz-aus-der-leere` | 10 | 2 | 2 |
| `kohaerenzprotokoll-aegis-und-systementropie` | 8 | 7 | 1 |
| `guardians-und-kern-welten-konzept` | 14 | 4 | 1 |
| `aegis-subplots-kapitelweise-system-exploration-docx` | 0 | 2 | 0 |
| `roman-lokalitaeten-konzept-und-ausarbeitung` | 10 | 17 | 1 |

The fifth added no pages on purpose. It is a brief — 163 hedging words in 13,947,
and 32 of its 91 question marks in the field closest to assertion — so sixteen
candidates matched no page and none became one. **A page created from an
occurrence says nothing and looks like it says something.**

**The sixth is the opposite case and it needed a rule.** It is a gazetteer: 51
named locations, 49 of its 109 candidates matching no page. Creating all of them
would have doubled the wiki from one document. The document supplies two
mechanical criteria — a count of exactly 2 identifies a location it profiles, and
a `Source` column per row says whether it invented the name — and a page was
created only where both held. **The rule came from the document rather than from
a preference**, and the 40 it excludes are recorded with their lines.

`Plan/runs/judgements.jsonl` holds **45 <!--state:judgements.total--> judgements**
about near matches, **7 <!--state:judgements.mechanised-->** mechanised and
replaying green, **0 <!--state:judgements.disagree-->** disagreeing.

**`python3 scripts/account.py order` holds** — `true`
<!--state:order.holds-->. Every document with a census has a note and a
reconciliation, each ran against the state the previous one left, and the wiki
matches what the newest run recorded leaving.

### Do not trust the numbers above — they are checked

Every number on this page carries a `<!--state:key-->` marker naming the
measurement it came from, and **`python3 scripts/state.py --prose` fails if any
of them contradicts the repository.** It reads every markdown file outside
`Legacy/` and the vendored clones, not a list of three — that list was itself the
bug: `Plan/concept/plan_2026-09-17.md` carried three markers, went stale when the
corpus was deduplicated, and the check stayed green because it never looked
there.

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
269 documents is that term in each, then the merge.

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
decided mechanically, 4 to judgement.** Document 6 is the scale test: 109
candidates against 46 pages, **68 decided by lookup and 55 sent to judgement**,
and the wiki's size entered none of it. Reasoning:
`Plan/concept/reconciliation-by-lookup_2026-09-17.md`.

**A reference on a wiki page names its document.** A bare `^[Lnn]` resolves
against the page's single `ingested:` entry and stops being checked the moment a
second one arrives — which is not hypothetical: adding document 6's readings to
seventeen pages moved 95 verified quotations into the unchecked bucket silently.
A census and a note carry `source:` and may use the bare form; a page may not.

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

**And `python3 scripts/read.py` serves the same text in the other direction, so
the defect need not be written first.** It prints the document with every line
prefixed by the file line a citation names, and `--find "<the words>"` answers
with `^[Lnn]` — or refuses, naming the nearest line. Both directions run the same
comparison on the same normalised line, so a citation `--find` produced passes
`quotes.py` by construction. Checking afterwards names a defect; asking for the
number instead of typing it is what stops one.

**And `python3 scripts/selftest.py` proves they can fail.** Six quotation cases,
four citation cases and seven `fold()` pairs, each carrying the exact defect the
checker must name, so a case that fails for the wrong reason fails the test.
Nobody had ever seen any of them fail — which is the shape of the retired
pipeline's worst defect: a coverage term that returned 1.0 whenever no gold
fragments were passed, and was never passed any. Two live runs scored 0.987 and
0.967 on a number that could not fall for missing anything.

**Conflict detection is never mechanised.** Two readings can only be compared by
reading them, and a program that guessed would reproduce the `Zero-Trust` false
conflict.

**`python3 scripts/selftests.py` runs every self-test in the repository** — the
three above and each tool's own — and prints one line per suite: `held`,
`FAILED`, or `not run` when the suite's interpreter is absent. A suite that did
not run has not passed, and the exit status says so.

### The wiki links, and a link is not a mention

Two marks, two meanings: `` `Nexus` `` names the term, `[[nexus]]` points at the
page, and `[[nexus|Nexus-Vorstufe]]` points at it while leaving the prose exactly
as it read. `scripts/relations.py` derives the graph from `[[…]]` and from
nothing else, and reports a link pointing at no page rather than dropping it.

```bash
python3 scripts/relations.py              # the graph, the orphans, the open questions
python3 scripts/relations.py --unmarked   # links the prose makes and the markup does not
python3 scripts/link.py [--apply]         # mark them; dry run by default
```

**207 <!--state:wiki.relations--> links across
56 <!--state:wiki.pages--> pages, 17 <!--state:wiki.orphans--> of them with
nothing pointing in.** Decision 005 has why, and what it corrects: the wiki was
described here as having no links, which was a statement about `[[…]]` syntax
mistaken for a statement about linking. 48 links existed, written in backticks,
and 158 more mentions were sitting unmarked — `aegis` was an orphan whose name
stood unmarked in other pages 68 times.

**A link is never inferred.** Every one marks a term the prose already wrote.
Whether a model may propose an edge the prose does not state is a separate
question, to be asked against this baseline rather than instead of it — a guessed
edge is indistinguishable from a stated one once it is in the graph.

**And the migration is why `quotes.py` was built first.** Its first pass put a
link inside two quotations, because the quote mask was line-bounded and German
quotations wrap. The check went 17 → 19 and named both. After the fix the pass
was redone from a clean tree and the count was unchanged — which is the proof,
and the only kind worth having.

The 73 <!--state:wiki.unmarked--> mentions still unmarked are ones whose first
occurrence sits inside a quotation, a citation line or a heading. Those are
places the pass may not touch, so that number is a measurement and not a backlog.

### The knowledge graph, and retrieval over it

The wiki is also a typed knowledge graph, derived and never stored:
`scripts/graph.py` reads frontmatter, `[[links]]` and `^[slug.md:Lnn]`
citations and builds **71 <!--state:graph.nodes--> nodes** (terms, documents,
conflicts, questions) and **438 <!--state:graph.edges--> edges** (`links`,
`reads`, `cites`, `contests`, `raised_by`, `asks`, `concerns`). **Every edge
carries the file line that states it**, and none is inferred — the same rule as
the links, for the same reason.

Its evidence is every quotation on a term page: 378 <!--state:graph.evidence-->
of them, **308 <!--state:graph.evidence_verified--> verified** against their
line by `quotes.verdict` — the checker's own code, since `quotes.pairs` and
`quotes.verdict` became the one implementation both use. Building the graph
first with a pairing of its own found 14 unresolved where the checker found 4;
two encodings of one rule disagreed on the first run.

`scripts/graphrag.py` is the retrieval half of `ask`: seed by folded surfaces,
spread by personalized PageRank over the typed edges, select verified quotations
by MMR with a relevance floor. **It returns quotations, the conflicts and open
questions touching them, and the documents the rank reached — never prose.**
`--answer` lets a model choose evidence *numbers*; code prints the quotations.

```bash
python3 scripts/graph.py                       # counts and the check against the files
python3 scripts/graph.py --around nexus --hops 2 --mermaid
python3 scripts/graph.py --graphml > kg.graphml   # or --json, --triples
python3 scripts/graphrag.py ask "Wie hängen die Guardians mit AEGIS zusammen?"
python3 scripts/graphrag.py bench              # recall against the wiki's own labels
```

`bench` scores retrieval on the 9 <!--state:graphrag.cases--> cases the wiki
already labels (each question's `raised_by`, each conflict's `pages`), with the
case's own node removed first. Recall@8 is
**40 <!--state:graphrag.recall_seeds-->% from the seeds alone and
58 <!--state:graphrag.recall_ppr-->% with PageRank** — the graph earns its
step, on nine cases whose labels were written by the same hand as the pages.
`bench --record` appends both to `Plan/runs/baselines.jsonl`.
`Plan/concept/graphrag_2026-09-23.md` has the design and what it cannot do.

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

`qmd` (github.com/tobi/qmd) indexes seven collections named for purpose and
answers a German phrase with a file and a line. **`.claude/skills/qmd` is where
it is documented** — which collection answers which question, why `search` is
0.22s and `query` is 2m41s, how German compounds break exact matching, the full
command surface, and how the setup is rebuilt.

Two things belong here rather than only there, because they govern work that is
not searching:

**A search result never becomes a number.** qmd ranks; it does not enumerate.
`Kernwelt` is in 144 of the landed documents and a forty-hit list is not a census
of that — measured, the line that defines `KW1` is not in the top forty, because
BM25 favours short, early chunks. Every number in a page or a learning comes from
`corpus.py`, `duplicates.py` or a count, which say what they counted and how.

**Nothing in the pipeline depends on qmd.** Reconciliation answers by lookup
against `Wiki/index.json` so its cost stays `O(census) + O(judgement)`. Search
finds candidates to read; it decides nothing.

```bash
scripts/setup_qmd.sh            # install, models, index, embeddings, shim
scripts/setup_qmd.sh --check    # what is missing — run this when a search returns less than it should
python3 scripts/qmd_coverage.py # non-zero if a directory is in no collection
```

**A file in no collection is absent from every search and nothing says so.** That
is why coverage is checked rather than remembered. The configuration itself lives
in the committed `.qmd/index.yml`; **never run `qmd init` here**, it overwrites it.

## Entity lists — a model's reading per document, and a search over all of them

`Plan/entities/<slug>.md` is one model's list of the 50-100 entities it judged
most important in one document, each citing a file line. The saved workflow
`.claude/workflows/entity-lists.js` has one Claude Haiku reader per document,
blind to every other, write **names only** to `Plan/entities/names/<slug>.json`;
`entities.py place` then finds each name's first whole-word line and writes the
list, refusing any name the document does not contain. They are searched by
`scripts/entities.py`:

```bash
python3 scripts/entities.py verify            # does each cited line hold its entity?
python3 scripts/entities.py matrix            # every verified entity × every document
python3 scripts/entities.py missing           # used in N+ documents, no wiki page
python3 scripts/entities.py doc <slug>        # which known entities one document uses
python3 scripts/entities.py search <entity>   # where, how often, first line
python3 scripts/entities.py score <slug>      # against a reader's 03-candidates.md
python3 scripts/entities.py place <slug> <names.json>  # a model's names -> a list, lines by code
python3 scripts/entities.py selftest          # token matcher == \bterm\b, and holds()'s cases
```

**4 <!--state:entities.lists--> lists exist, 3 <!--state:entities.readings--> of
them pass verification**, and 317 <!--state:entities.rows_verified--> of
317 <!--state:entities.rows--> rows cite a line that holds the entity — by
construction, since code wrote every line (revision 3). The one list that is not a
reading is so because its reader reported stopping one line short. `NOW.md` has
the numbers per list, and the full run over every landed document has not
happened.

What they are for — `Plan/concept/entity-lists_2026-09-23.md` has the argument:
**`missing`** is P10's `MISSING` bucket, measured; **`doc`** is a document's
entity profile for choosing the next document; **`search`** counts multi-word
entities across line wraps, which `corpus.py`'s index cannot.

What they may not do: seed a census or a `03-candidates.md`, create a page,
supply a count (every number comes from the search), or merge two surfaces. A
list under 90% verified is a reconstruction and `matrix` leaves it out.
**`entities.py search` counts hyphen compounds and `corpus.py count` does not** —
`Guardian` is 448 in one and 334 in the other, and both are right about different
questions.

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

44 of the 617 rows are markdown or audio, which the connector does not list as
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

Four venvs are defined, all git-ignored, each for one reason. **None survives a
container**; each is rebuilt by the commands below when a step needs it:

| venv | python | why |
|---|---|---|
| `.venv-tools` | 3.11 | markitdown and its converters, for `sources.py land` |
| `.venv-dspy` | 3.11 | DSPy 3.3.1 with numpy — every `scripts/` step that calls a model or its fixture |
| `.venv-dspytools` | **3.12** | `dspytools`, which refuses 3.11 |
| `.venv-typesafe` | 3.11 | `typesafe-sdk`, for Jev — only `scripts/jev_entities.py`, a test |

```bash
uv venv --python 3.11 .venv-dspy
uv pip install --python .venv-dspy/bin/python 'dspy[numpy]==3.3.1'   # SIMBA raises without numpy
.venv-dspy/bin/python scripts/check_dspy_surface.py                   # the surface this repo calls
```

```bash
uv venv --python 3.12 .venv-dspytools
uv pip install --python .venv-dspytools/bin/python git+https://github.com/netzkontrast/dspytools
DSPYTOOLS_SKILLS_DIR=$PWD/.agents/skills .venv-dspytools/bin/dspytools skills list
```

```bash
uv venv --python 3.11 .venv-typesafe
uv pip install --python .venv-typesafe/bin/python git+https://github.com/typesafe-ai/typesafe-sdk-python
```

The key comes from `TYPESAFE_API_KEY` in the environment and is never written to
a file here. **Every call sends text to a third-party API**, so no corpus text
goes through it until a person has decided it may —
`Plan/concept/jev-in-ingestion_2026-09-23.md` has where it may help and where it
may not.
`.agents/skills/typesafe` is how to build with it: question wording, composition,
the limits the TypeSafe cookbooks measured, and the SDK as installed.

**`.claude/skills/jev*` is a vendored third-party collection**, not this project's
skills: eleven folders copied unchanged from `wuyoscar/jev-skill` tag `v0.2.0`,
commit `82c01055c80fa96d3e8a1b82132361693b6bf3a1`, MIT. They are real folders in
`.claude/skills/`, not symlinks into `.agents/skills/`, so `rlm_ingest.py`'s
`SkillManager` does not render them into its prompt. Their CLI is not in the
repository and does not survive the container:

```bash
git clone --depth 1 --branch v0.2.0 https://github.com/wuyoscar/jev-skill /tmp/jev-skill
uv tool install /tmp/jev-skill            # provides jev-decide; standard library only
jev-decide setup                          # which key is present — never its value
```

The route chosen for them is **A, real Jev**. Both keys are present in the
environment's settings as of 2026-09-23, never in chat or a file here. Every call still
needs the author's yes before corpus text is sent (see above).

Two packages make a `SKILL.md` written here reachable from DSPy rather than only
from a person, and they do different halves of it:

```bash
# the runtime half — a ReAct agent that discovers, activates and uses skills
uv pip install --python .venv-dspy/bin/python --no-deps \
    git+https://github.com/netzkontrast/dspy-skills-implementation-
uv pip install --python .venv-dspy/bin/python strictyaml

# the management half — list, search, compile and optimise skills as artifacts
uv venv --python 3.12 .venv-dspytools
uv pip install --python .venv-dspytools/bin/python git+https://github.com/netzkontrast/dspytools
```

`dspy_skills.SkillManager([Path(".agents/skills")])` discovers every skill
here, and `generate_skills_prompt_block(manager)` renders the
`<available_skills>` block a ReAct agent is given. **That block is built from the
`description` field and nothing else** — which is why the description is the part
worth optimising, and `dspy-book-coding-agents` optimises exactly that kind of
text with GEPA's `optimize_anything`.

`--no-deps` is load-bearing: the package asks for `dspy-ai>=2.5.0`, the old
distribution name, and resolving it would move this venv off the pinned DSPy
3.3.1.

A third, `drg-kg`, is installed for one module only — its evaluation scorer,
whose `_prf` returns **0.0** where the retired pipeline's `coverage()` returned
1.0. Its extraction and graph layers stay unused, because a canon link is
written by a person and never inferred by a model — not because the wiki has no
links. It has 207 <!--state:wiki.relations-->.

```bash
uv pip install --python .venv-dspy/bin/python "drg-kg[extract] @ git+https://github.com/netzkontrast/drg-kg"
```

**Nothing in the pipeline calls any of the three yet.** They are installed,
reachable, and measured against this repository —
`Plan/concept/continuous-improvement_2026-09-17.md` has what each is for and in
what order.

## Calling a model — the DSPy toolchain

Built 2026-09-23 from nine DSPy repositories read against this one
(`Plan/concept/dspy-toolchain_2026-09-23.md`; the readers' reports are in
`Plan/concept/dspy-repos_2026-09-23/`). No package was installed from them;
every piece is a pattern of tens of lines, ported with its source named.

| script | what it guarantees |
|---|---|
| `lmrun.py` | the only way a model is called: `cache=False`, one record per call in `Plan/runs/<subject>/lm/`, status `answered` / `refused` / `unparsed` / `unreachable` — never a score — and **a real model refused without `approval=`** naming the author's decision |
| `lm_fixture.py` | an offline `dspy.BaseLM`; `offline()` hides every `*_API_KEY` and replaces `litellm.completion` with a refusal, because a scanned repository's unmocked test made a live call from this container |
| `baseline.py` | `Plan/runs/baselines.jsonl`, append-only; `compare` fails a candidate that does not beat the **floor**, not only one that fell since the last row, and a `vetoed` row fails whatever its score |
| `pairs.py` | one-term-or-two: `fold()` first, a model only on the residual, stratified folds, repeats, and every candidate asked the never-merge canaries |
| `check_dspy_surface.py` | asserts, by `inspect.signature`, each DSPy parameter this repository passes |
| `check_skills.py` | the skill spec, and P6: `.claude/skills/<name>` is a symlink into `.agents/skills/` |

**36 <!--state:pairs.labelled--> labelled pairs; `fold()` decides
21 <!--state:pairs.fold_correct--> of them.** Every optimizer on the ladder —
`labeled`, `bootstrap`, `inferrules`, `simba`, `gepa` — runs end to end with
`--dry-run`. **None has run against a real model**: that sends corpus words to
a third party, and the author has not said yes to it. `scripts/rlm_ingest.py`
now requires `--approval` for the same reason, turns its cache off, sets a call
budget, hands the model `find_line` and `count` as tools, and measures how far
into the document its verified citations reach.

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
and a count over 346 showed a cliff.

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

**One exception: a corpus-wide re-measurement.** When the corpus itself changes
size — a landing batch, or `dedupe.py` folding duplicate exports away — every
page that wrote a denominator like „among the 409 landed" is wrong, and no source
document caused it. Such a commit names the measurement instead of a document,
changes no reading, and says so. It is rare and it is recognisable: if the diff
touches a claim rather than a number, it is not this.

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
