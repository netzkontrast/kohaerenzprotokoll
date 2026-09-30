# Kohärenz Protokoll — working agreement

A German hard-SF novel and its research corpus. **Right now only the wiki is
being built.** The novel rests. A plan for writing it is proposed and not yet
decided: `Plan/concept/novel-writing-plan_2026-09-29.md`, whose four questions
for the author are in `NOW.md`.

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

**`GOAL.md` is the project's general goal** (2026-09-23, the author's brief, in
German): a git-versioned knowledge graph and wiki that helps write the novel —
sources tiered by precedence, conflicts found and never silently smoothed,
self-generated questions, the plot model as checkable rules. It describes the
*target*, not the repository: where it names paths or tools that do not exist
here, this page says what exists, and `NOW.md` holds where the two disagree.

**Then read `NOW.md`.** It is what is open right now — decisions waiting on the
author, work half-done, what failed — and it is the handover between sessions.

### A fresh container has none of the derived things

A cloud session starts from a clean clone. Everything git-ignored is absent.
**`scripts/install.sh` rebuilds all of it but the qmd models**, and
`.claude/hooks/session-start.sh` runs `scripts/install.sh --session` at every
cloud session start — `derived`, `tools`, `dspy`, `graphqlite`, `typesafe`,
`hyperextract` and `qmd`, what the pipeline and `selftests.py` call (decision 015;
GraphQLite added for the author's local CLI request); the rest install
on demand with `scripts/install.sh <name>`. Synchronously, so no step races an
install, and never blocking the session on a failed component. `scripts/install.sh --check` says what is present,
`--list` names the components, `scripts/install.sh <name>` installs one. The
first run here took about a minute with uv's cache already warm — a cold
container also downloads torch for `grawiki`, unmeasured; a second run is 4s.
The log is `.install.log`.

| absent at start | rebuild (`scripts/install.sh <name>`) | needed for |
|---|---|---|
| `Plan/derived/` | `derived` — `python3 scripts/derive.py`, about 3s | `corpus.py`'s index path |
| `.venv-tools`, `.venv-typesafe`, `.venv-dspy`, `.venv-dspytools`, `.venv-grawiki`, `.venv-semantica`, `.venv-mflow` | `tools`, `typesafe`, `dspy`, `dspytools`, `grawiki`, `semantica`, `mflow` | only the step that names each |
| `jev-decide` | `jev` | the vendored `jev*` skills in API mode |
| `graphify` CLI, with its `openai` extra | `graphify`, pinned to `4c73561` | the vendored `graphify` skill |
| `cgr` (code-graph-rag) | `cgr` | nothing in the pipeline |
| `he`, `he-mcp` (Hyper-Extract) | `hyperextract`, pinned to `395039e` | the `hyper-extract` MCP server in `.mcp.json` and the vendored `hyper*` skills |
| OpenCode and the oh-my-openagent plugin | `omo` — `~/.config/opencode/opencode.json`, `~/.omo/omo.jsonc`; no provider sign-in | nothing in the pipeline; a second agent harness |
| qmd package and the `/usr/local/bin/qmd` shim | `qmd` — `scripts/setup_qmd.sh --package` | searching; nothing in the pipeline |
| qmd's models (~2.1 GB), index and embeddings | `qmd-models` — `scripts/setup_qmd.sh`; **not** run at session start | vector search and `qmd query` |
| `.venv-graphqlite` | `graphqlite` — pinned Python package `graphqlite==0.8.0` | `scripts/kg.py`, the local graph CLI and its real-extension fixtures |
| `OPENROUTER_API_KEY`, `TYPESAFE_API_KEY` | the environment's settings, never a file or the chat | a real Jev call |
| `Plan/derived/ui/` | `python3 scripts/ui.py` | the project app's canvas files, to publish |

The standard-library scripts — `state.py`, `quotes.py`, `read.py`,
`reconcile.py`, `account.py`, `entities.py`, `ui.py` — need none of these.

## Two layers

| layer | what it is | who writes it |
|---|---|---|
| `Sources/` | research documents fetched from Drive, immutable once landed | `scripts/sources.py`, nothing else |
| `Wiki/` | term pages derived from those sources, promoted by a human | a person, for now |

There is no third layer. Everything else the project used to have is parked
under `Legacy/` and read by nothing.

`Sources/manifest.jsonl` is the spine: 587 <!--state:sources.total--> rows, each with `drive_id`, `title`,
`slug`, `category`, `tier` and, once landed, `export_path` and two checksums.
Anything derived traces back to a `drive_id`.

`Sources/duplicates.jsonl` holds the 93 <!--state:sources.folded--> rows that left it — the same shape plus
`duplicate_of`. Two files, two questions: the manifest says what is in the
corpus, and this says what Drive also holds and why it is not here. It exists so
that „not in the manifest" never has to mean „nobody knows".

## State, as of 2026-09-17

**586 <!--state:sources.landed--> of 587 <!--state:sources.total--> source documents are landed.** The one that is not
is `Coherence Protocol.mp3`: markitdown can only transcribe it by sending the audio
to a third-party speech service, which waits on the author's yes. The other 241
landed on 2026-09-26, on the author's „Download all of the Rest from the
Manifest": the 227 pre-May-2026 `plot-outline` gdocs deferred with the novel, the
13 remaining `md` and the one `pdf` — 0 failures, about four minutes, no model
reading any of them. 26 of the 241 were copies of another new file and were
folded away (below), so 215 new documents stand. `Sources/README.md` now ends
with every document and the names that matter in it (*Sources at a glance*,
below). Every category the wiki needs is complete, and
so, since 2026-09-24, is the canon era: all 33 <!--state:sources.canon_era--> rows
dated May 2026 or later, 33 <!--state:sources.canon_era_landed--> landed, and all 33 read
(documents 7 to 39) — the last eight, all of 2026-05-08, on 2026-09-27.

**Those files are 586 <!--state:sources.distinct--> distinct documents, and
that took work.** Drive holds up to five exports of the same document — a gdoc
export, a docx export, a `kopie` of each, a second run of both — and each landed
under its own `drive_id`. 409 files were 346 documents, so **every count phrased
as "N of 409" was counting copies.** Only 2 pairs were byte-identical, so
checksums found almost none of it.

`python3 scripts/dedupe.py` folded the
93 <!--state:sources.folded--> extra files away. The file left `Sources/drive/`,
the row left the manifest — 680 rows became 617, the canon-era landing's four
copies took it to 613, and the 26 copies among the plot outlines of 2026-09-26 to
587 — and the full row moved to
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

**54 <!--state:documents.with_census--> have a term census** in `Sources/terms/`, **54
<!--state:documents.with_note--> have a note** in `Sources/notes/`, and **51
<!--state:documents.reconciled--> are reconciled** — the three others are the first
extractions of step 6's sample, waiting for their reconciliation (see `NOW.md`).
Of the reconciled, five are `theorie-physik`,
five `worldbuilding`, one `aegis`, six `storyform`, six `charaktere`, ten
`kernkonzept`, thirteen `plot-outline`, one `theorie-psychologie`, one `theorie-logik`, one
`theorie-philosophie` and two `theorie-mathematik` — thirty-three of them from the canon era, and
documents 40–51 the first read from before it since document 6.

`Wiki/candidates/` holds **106 <!--state:wiki.pages--> pages**, `Wiki/conflicts/`
holds **15 <!--state:wiki.conflicts-->**, `Wiki/questions/` holds
**9 <!--state:wiki.questions-->**, and
`Wiki/compare/` holds the reconciliation record per document. The schema follows
the pages rather than preceding them, so `Wiki/terms/` does not exist and nothing
has been promoted.

**Beside the terms, the chapters (decision 013).** `Wiki/chapters/` holds
**41 <!--state:wiki.chapters--> chapter pages**, Kap 0 to Kap 40, with
**584 <!--state:chapters.readings--> readings** from the nine read documents
that go chapter by chapter, one that names six chapters, one that names three, a narrative text of two, an annotated narrative text of Kap 0 that names five, that text's prose without its annotation, a world bible that names nine, a philosophy catalogue that names nineteen, a drafting run's log that names three, a chapter file of Kap 25 that names two, a storyform companion that names nine, a theory report that names three, seven English documents of 2026-05-08 that name the Vortex's two chapters, and one of them Chapter 1 and Chapter 39, a Dramatica report that names the Vortex's two, three pre-2026 plans that go chapter by chapter from Kapitel 1 to 39, a storyform study that names nine, that report's earlier run, which names the Vortex's two, and a narrative text of twenty-two chapters, its own Kapitel 1–12 and 14–23; `Wiki/overview/` lays the chapters and the plot's
shape side by side. See *Chapters and the plot*, below.

**What each document added, and what reading it found, is in
`Plan/runs/reading-log.md`** — a table row and a paragraph per document up to
document 51, moved there from this page on 2026-09-29 (decision 015) — and, for
every document, in its reconciliation record `Wiki/compare/reconcile-NN-<slug>.md`.
From document 52 on the record alone carries it.

`Plan/runs/judgements.jsonl` holds **120 <!--state:judgements.total--> judgements**
about near matches, **8 <!--state:judgements.mechanised-->** mechanised and
replaying green, **0 <!--state:judgements.disagree-->** disagreeing.

**`python3 scripts/account.py order` does not hold** — `false`
<!--state:order.holds-->, and says so with exit status 1. The three step-6 documents
above have a census and a note and no reconciliation. It holds again when every
document with a census has a note and a reconciliation, each ran against the
state the previous one left, and the wiki matches what the newest run recorded
leaving. **Until 2026-09-30 the check exited 0 either way, and this line said
`true` over a red state.** The review of PR #110 found both. It was red from the 2026-09-25 scan
(below) until document 21: the scan's eleven pages were written outside a
reconciliation, the wiki held 105 pages where the newest run recorded 94, and the
check named exactly that. It was not loosened to excuse them. Document 21 started
from the 105 pages and recorded the state it left.

**Four question pages were promoted on 2026-09-29, from the pages alone.** Q6 asks how
the Nexus, the Überraum and the Überwelt relate; Q7 what the number 734 names; Q8 what
AEGIS is after the Vortex's fifth beat, and whether Oblivion takes over its function; Q9
where the Moonshine-Link's boundary lies. Each gathers what term pages already quote,
verified by `quotes.py`, and no document was read for them. Q8 and Q9 are open points the
sources name themselves, citing the Reset-Doc's Appendix C —
`kohaerenz-protokoll-struktur-kanon-reset-2026-04-30-md`, landed and unread.

**The 2026-09-25 scan added eleven pages outside the pipeline.** Following qmd
searches over the open records, ten unread documents each got a triage scan
from one Haiku reader (`Plan/runs/haiku-scan-2026-09-25/`). The raw scans cited
44 of 152 quotations to lines that did not hold them, and they resolve only after
a second pass. Page writers then quoted the ten scanned documents and the twenty
read ones directly, never through a scan, to write `vortex`, `goedel-gambit`,
`ouroboros-struktur`, `komponente-734`, `vermittler-stimme`, `genesis-klammer`,
`residual-echos`, `chaitin-konstante`, `kishotenketsu`, `tsdp` and
`thermodynamischer-phaenomenalismus`. Each page ends by saying that the scanned
documents have no census and no reconciliation; since document 21, the five pages
that quote it name its reconciliation instead. What the pages found and no record
holds is in `NOW.md`.

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
version: **a census lists the candidate terms of one document by a written rule**
— what it names in the novel's world, the words it uses as its own terms, the
borrowed concepts it applies (decision 012; the rule is in the briefing). A note
harvests what that document says about the terms that matter, quoting with line
numbers.

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

**And it sweeps the text for everything the wiki already knows** (decision 012).
A lookup matches only what the census listed, so `reconcile.py` also searches
the document for every surface of every page, standing alone. Each page the text
names without a matching candidate is decided: a reading, which goes on the
page, or an occurrence, such as a title, a reference or another sense. The call
is recorded in `Plan/runs/sweep.jsonl`: 127 <!--state:sweep.decided--> so far,
66 <!--state:sweep.readings--> of them readings the lookup had missed, and
0 <!--state:sweep.open--> undecided (`reconcile.py --sweep-open`). The sweep
asks the index, never the pages, so its cost is code's.

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

**A short quotation is checked when it is cited.** Until 2026-09-26 the pattern began at
eight characters, so a cited „(Ch13)" matched nothing — not checked, not counted — while its
citation named a line that did not hold it. Now every cited quotation is checked; an uncited
short one is a word the prose mentions and stays out of every count.

**A number is compared on its own.** The footnote rule drops a number after a
word on both sides, so until 2026-09-24 „Kap 33 Beat 3" resolved against a line
reading „Kap 38 Beat 3" — and a chapter outline carries hundreds of such numbers
and no footnote. Now every number a quotation writes must stand on its line, in
order. Measured before the change: none of the 298 verified quotations with a
number had one its line lacked, so no verdict moved.

**And `python3 scripts/read.py` serves the same text in the other direction, so
the defect need not be written first.** It prints the document with every line
prefixed by the file line a citation names, and `--find "<the words>"` answers
with `^[Lnn]` — or refuses, naming the nearest line. Both directions run the same
comparison on the same normalised line, so a citation `--find` produced passes
`quotes.py` by construction. Checking afterwards names a defect; asking for the
number instead of typing it is what stops one.

**And `python3 scripts/selftest.py` proves they can fail.** Twelve quotation cases,
six citation cases and ten `fold()` pairs (measured 2026-09-26; `selftest.py` prints the count), each carrying the exact defect the
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

**And GitHub runs the checks on every push to `main` and on every pull request**
(`.github/workflows/checks.yml`, since 2026-09-30). Each check is its own step: prose
numbers, pipeline order, quotations, frontmatter, the judgement replay, chapter pages,
the Sources overview, and `selftests.py --only std`, the suites the standard library
runs alone. The dspy, typesafe, GraphQLite and Hyper-Extract suites need their venvs,
so they run in a session and not on GitHub; `askdb.py`'s and `kg_selftest.py`'s are
among them. A pull request with a merge conflict is not checked at all: GitHub builds
no merge commit to run on. The review of #110 is why the workflow exists: it found
green results claimed for a commit nothing had checked.

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

**674 <!--state:wiki.relations--> links across
106 <!--state:wiki.pages--> pages, 19 <!--state:wiki.orphans--> of them with
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

The 531 <!--state:wiki.unmarked--> mentions still unmarked are ones where every
mention sits inside a quotation, a citation line or a heading — places the pass
may not touch, so they are a measurement and not a backlog: `link.py` proposes
none. **A page links a term once.** Until 2026-09-25 every run of `link.py`
marked the next free occurrence of each term, linked or not — on the pages as
they stood that day, 24 links to terms their pages already linked; it now skips
a term the page links (`python3 scripts/link.py selftest`).

### Chapters and the plot

On 2026-09-25 the author asked to „start to Focus on Plot and the Chapters a Bit
more" — decision 001's own condition for revising its unit. So the chapter is a
unit beside the term (decision 013), and the term pages stay as they are.

`Wiki/chapters/kap-NN.md` collects what every read source says about one chapter:
one `## Reading` per document, in date order, quoted and cited, attributed and
unmerged. Where the sources part — a title, a world, what happens — the page says
so under `## Where the sources differ` and stops. `records:` names the conflict
and question records about the chapter. `Wiki/chapters/README.md` has the format.

`Wiki/overview/` holds pages that place rather than define: `chapters.md`, every
source's title for every chapter, **derived** from the chapter pages; and
`plot.md`, each source's macro structure — chapter count, acts and blocks,
modes, the Vortex — with where they agree and differ.

```bash
python3 scripts/chapters.py            # check the pages; fails on any defect or a stale overview
python3 scripts/chapters.py overview   # re-derive Wiki/overview/chapters.md
python3 scripts/chapters.py missing    # read documents naming `Kap N` with no reading on its page
```

**98 <!--state:chapters.missing--> chapter mentions** in read documents have no
reading on their chapter's page yet — the character bible's Kap-33 scene among
them. The count sees `Kap N` written singly; a range and a numbered list without
`Kap` are invisible to it, so it under-counts. A range with an approximate bound,
`Kap 14–\\\~20` as the export escapes it, was read as a single Kap 14 until
2026-09-25. Reading a new document now ends,
where it names chapters, with its readings on those pages.

**Around the readings, navigation (2026-09-26).** Each chapter page opens with
what its readings say the chapter is about, placed in the story's structures, and
ends with its questions — eight basic ones filled with its plot, 10–12 of its own
against GOAL.md §4.5 and §5 — a table of unread candidate sources a qmd vector
search returned for them, and a link to qmd's raw answers, which stand beside the run
in `Plan/runs/qmd-chapters-2026-09-26/raw/kap-NN.md`. `scripts/chapter_sources.py`
writes all four from `Plan/runs/qmd-chapters-2026-09-26/`; none is a reading, and
the table finds plans of a chapter, not narrative text of it.

**Reading the chapter outlines side by side corrected a claim.** `NOW.md` said
every read source but one ended at Kap 39; seven of the eight count a Kap 40.
The konzept master report, read after, counts 39 chapters with no frame and one
Vortex — two of `plot.md`'s claims about every 2026 plan, corrected there.
The 39-chapter spec, read after that, is a second plan with 39 chapters and one Vortex,
so `plot.md`'s „every plan but one" became „every plan but two" — and the worldbuilding concept,
read after that, made it three.

### The knowledge graph, and retrieval over it

The wiki is also a typed knowledge graph, derived from the authoritative files:
`scripts/graph.py` reads frontmatter, `[[links]]` and `^[slug.md:Lnn]`
citations and builds **181 <!--state:graph.nodes--> nodes** (terms, documents,
conflicts, questions) and **4418 <!--state:graph.edges--> edges** (`links`,
`reads`, `cites`, `contests`, `raised_by`, `asks`, `concerns`). **Every edge
carries the file line that states it**, and none is inferred — the same rule as
the links, for the same reason.

Its evidence is every quotation on a term page: 9022 <!--state:graph.evidence-->
of them, **9022 <!--state:graph.evidence_verified--> verified** against their
line by `quotes.verdict` — the checker's own code, since `quotes.pairs` and
`quotes.verdict` became the one implementation both use. Building the graph
first with a pairing of its own found 14 unresolved where the checker found 4;
two encodings of one rule disagreed on the first run.

`scripts/graphrag.py` is the retrieval half of `ask`: seed by folded surfaces,
spread by personalized PageRank over the typed edges, select verified quotations
by MMR with a relevance floor. **It returns quotations, the conflicts and open
questions touching them, and the documents the rank reached — never prose.**
`--answer` lets a model choose evidence *numbers*; code prints the quotations.

**A disposable GraphQLite projection serves the same graph locally.**
`scripts/kg.py index` builds `Plan/derived/ask.db`, or does nothing when
its input hashes match. Changed inputs rebuild it; reads refuse stale snapshots.
The CLI provides FTS5 search, evidence IDs, bounded Cypher neighbours and
byte-capped context using the existing personalized PageRank/MMR. No model or
MCP server is needed. Use the `graph-context` skill for the command order and
`scripts/install.sh graphqlite` for the pinned interpreter. This is a cache,
not another authoritative layer; edit the files and re-derive.

```bash
python3 scripts/graph.py                       # counts and the check against the files
python3 scripts/graph.py --around nexus --hops 2 --mermaid
python3 scripts/graph.py --graphml > kg.graphml   # or --json, --triples
python3 scripts/graphrag.py ask "Wie hängen die Guardians mit AEGIS zusammen?"
python3 scripts/graphrag.py bench              # recall against the wiki's own labels
```

`bench` scores retrieval on the 24 <!--state:graphrag.cases--> cases the wiki
already labels (each question's `raised_by`, each conflict's `pages`), with the
case's own node removed first. Recall@8 is
**53 <!--state:graphrag.recall_seeds-->% from the seeds alone and
69 <!--state:graphrag.recall_ppr-->% with PageRank** — the graph earns its
step, on cases whose labels were written by the same hand as the
pages. Documents 7–9 added seven of them (C6–C12), the author's C6
decision an eighth (Q5), document 16 a ninth (C13) and document 17 two
more (C14, C15); on the original nine the numbers were 40 and 58.
Document 19 moved them from 48 and 67 by giving C11 three more pages: its
gold set grew from two pages to five, and the case fell from 1.0 to 0.6 with
PageRank. The fall is that label growing; on the labels that did not change,
retrieval rose — C6 from 0.29 to 0.43.
The eleven pages of the 2026-09-25 scan moved PageRank recall from 0.659 to 0.649,
measured against the tree before them. The only case that fell was C11, from 0.6
to 0.4: `vortex` and `thermodynamischer-phaenomenalismus` both concern C11 and now
rank in its top eight, and neither is in its record's `pages`. That is the label
lagging the graph. It is not retrieval getting worse.
Document 21 moved it back to 0.659, and again only C11 moved, from 0.4 to 0.6:
its reading went onto `hitze-polaritaetsregel`, which is in C11's `pages`.
Documents 23 and 24 left it at 0.659: their 29 readings each moved no case.
Document 27 moved it to 0.643: C11 from 0.6 to 0.4 and Q3 from 0.375 to 0.25, and in both the
pages crowding the gold out of the top eight are the central ones it gave a reading — `aegis`,
`juna`, `kael`, `coheron`, `vortex`, `alters`. The hubs grew faster than the pages around them.
Document 28 moved it to 0.637, only C4, from 0.556 to 0.444: `cerberus` left its top eight and `alters`
entered it, linked from the new readings on `cerberus`, `guardians` and `kern-welten`. Document 29 moved nothing, and neither did document 30. Document 31 moved it to 0.644, only Q5, from 0.286 to 0.429. Document 32 moved it to 0.654, only C11, 0.4 to 0.6; documents 33–39, measured together, moved it back to 0.644, again only C11 — the hubs again. Documents 40–43, measured together, moved it to 0.660: C11 from 0.4 to 0.6 and C4 from 0.444 to 0.556. Documents 44–46 moved nothing, and neither did document 47, nor documents 48–50. Document 51 moved it to 0.654, only C4, from 0.556 to 0.444. The four question pages of 2026-09-29, Q6–Q9, added four cases and moved it to 0.694 over 24, and seeds alone from 0.466 to 0.531; the twenty earlier cases scored exactly as before. The new cases score high because each question is worded in the terms of the pages that raise it — Q7 and Q9 1.0, Q6 0.833, Q8 0.75 with PageRank — which is the caveat above, the same hand writing question and label, four times more.
`bench --record` appends both to `Plan/runs/baselines.jsonl`.

**Beside the graph, never in it: the proposal layer.** `graph.proposals()`
reads what a model chose or the corpus merely co-states, and each item says so.
**300 <!--state:proposals.entities--> entities** come from the entity lists that
verify as readings — a model chose the name, code placed the line — and
53 <!--state:proposals.entities_paged--> of them fold to a page. **195
<!--state:proposals.glosses--> glosses** come from
`Plan/runs/bilingual/stated.jsonl`: `A (B)` written in two or more documents,
one side a page surface, and a surface glossing two pages dropped. A gloss's
relation is **unjudged** (`Kael (Host)` is a role), so `graphrag.py ask --gloss`
lets it route an English question to a German page, labelled as a gloss, and
never merges anything. Entities route a question to **unread** documents that
name it, with the line. On the bench, glosses change nothing (no case is
English-only); the English case they exist for is in `graphrag.py selftest`.

```bash
python3 scripts/graph.py --proposals [--missing]     # entities, glosses, entities with no page
python3 scripts/graphrag.py ask "What are the Core Worlds?" --gloss
```
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
A document landed after the index was built is in no search until `qmd update`
runs — 13 seconds for the 215 documents of 2026-09-26.

### Sources at a glance

`python3 scripts/overview.py` writes the end of `Sources/README.md`: every landed
document, by category, with its most important wiki names and other names. A name
is counted under the wiki page it belongs to and printed as that page names it:
the page's own surfaces, and a translation pair from `Plan/entities/bilingual.jsonl`
(one hop, de ↔ en, marked `†`). Names with no page come from the verified entity
lists and `bilingual.py`'s entities, printed as written. **Every number printed is
a count**; the order is tf-idf, so `AEGIS`, in most documents, sinks.

```bash
python3 scripts/overview.py scan       # the qmd first scan: each page's name, ranked documents
python3 scripts/overview.py            # write the section; --check fails when it is stale
python3 scripts/overview.py doc <slug> # one document's names, with df and weight
```

`scan` keeps qmd's ranking per page in `Plan/runs/qmd-scan/pages.json`, and the
README prints the first unread documents for each — a place to look, labelled as a
rank. The lookup keeps the project's rules: a pair is a proposal and merges nothing
outside that list, and a short token matches case and all, so `did` is not `DID`.

## The project app — the repository as one interactive canvas

`python3 scripts/ui.py` derives the whole project into one app: the pages,
conflicts, questions and reconciliation records, the graph, the manifest, the
invariants as they ran, the decisions, the principles, `NOW.md` and `GOAL.md`.
It writes them as the files of a claude.ai Design canvas into
`Plan/derived/ui/`, git-ignored like everything derived. **It infers nothing**:
a page is rendered from its own markdown, a relation is a `graph.py` edge, a
count is a `state.py` measurement, and a reading-log row is the document's own
`reconcile.json`.

```bash
python3 scripts/ui.py              # derive, run the invariants, write the canvas files
python3 scripts/ui.py --check      # also check what was written, the way the canvas reads it
python3 scripts/ui.py selftest     # each check handed the defect it exists to name
```

The app's source is `scripts/ui.html` and `scripts/ui.js`. `--check` exists
because the canvas reports none of this: an expression in a `{{hole}}` fails
silently, and a button inside a button or an unclosed element becomes a
different tree when the page is parsed.

**A script cannot publish it.** A Claude session does, with its Artifact tool, to
the canvas at https://claude.ai/artifact/1EyhQkX3MpiRTw3TxjTjYL, which is private
to the author. A data refresh sends `project/Main.dc.html` alone, so the canvas
keeps the author's arrangement. The app is a snapshot and names its commit on its
rail; whether it is rebuilt after every reading is a question for the author
(`NOW.md`).

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

**5 <!--state:entities.lists--> lists exist, 4 <!--state:entities.readings--> of
them pass verification**, and 395 <!--state:entities.rows_verified--> of
395 <!--state:entities.rows--> rows cite a line that holds the entity — by
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

**`Plan/entities/bilingual.md` maps German and English surfaces of one entity**
across the whole corpus. It is written by `scripts/bilingual.py`: code finds the
glosses the corpus writes itself, Jev judges which surfaces are entities, free
OpenRouter models propose counterparts from names alone, and Jev classifies each
pair. Every stage is cached under `Plan/runs/bilingual/`, so `--replay` reruns it
with no key and no network. It is a list of proposals: no pair has become a
judgement.

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

40 of the 587 rows are markdown or audio, which the connector does not list as
supported — but `md` comes through the text route: all 39 `md` rows are
landed, 4 on 2026-09-16, 22 on 2026-09-24 with
`fetch --since 2026-05-01 --include-md`, and the last 13 on 2026-09-26 with
`fetch --include-md --limit 1000`. `--include-md` is opt-in. The one `mp3` has no
route that keeps its content in this container.
`Plan/learnings/fetch.md` has the format census and the heading measurement.

## Installing anything

**Every dependency goes into a virtualenv. Never into the system Python** —
`pip install --break-system-packages` once broke `cryptography` for the whole
container. The table at the top of this page says what each component is for;
`.agents/skills/tools/references/install.md` has every venv, vendored skill and
third-party tool, how each is installed, and what it may not do (moved there from
this page on 2026-09-29, decision 015).

### The writing skills

**The writing skills are adapted, not vendored**, on the author's request of
2026-09-29: „Install https://github.com/netzkontrast/writing-skills/tree/main into
this repo", then „But optimieren ihn für dieses repo". There are thirteen
augmentation-only fiction skills from `netzkontrast/writing-skills` commit
`2fad031982cbbcb00c4da14c2fc9712d2daa78da` (MIT, © Rhymenoceros s. r. o.; the
licence is in each folder):

- editorial: developmental, line, copy and continuity editor;
- character: two character-card skills;
- critique: a beta-reader panel, an agent's first read, a workshop;
- craft: four drills.

**Their one rule is that no skill writes or rewrites the author's prose.** They
read, critique, simulate a reader or drill the writer.

Because they were changed, they are this project's skills. Each lives in
`.agents/skills/<name>/`, with `.claude/skills/<name>` linking to it, and
`check_skills.py` holds them as it holds `ingest`. A fourteenth skill,
`writing-skills`, is their entry point: which one to use when, the rules they
share here, and what was changed.

**What was changed:**

- every description names this book;
- each `## With Calliope (MCP)` section became `## In this repository`: canon is
  the author's decisions and approved chapters, never the wiki's readings; findings
  go to `Plan/runs/writing/`; every line is cited from `grep -n`;
- `copy-editor` follows the amtliches Regelwerk and the Duden instead of the
  Chicago Manual of Style.

Every rubric, lens and ladder is upstream's. They are the reading side of
`Plan/concept/novel-writing-plan_2026-09-29.md`, a proposal the author has not
yet decided on.

## Calling a model — the DSPy toolchain

Built 2026-09-23 from nine DSPy repositories read against this one
(`Plan/concept/dspy-toolchain_2026-09-23.md`; the readers' reports are in
`Plan/concept/dspy-repos_2026-09-23/`). No package was installed from them;
every piece is a pattern of tens of lines, ported with its source named.

| script | what it guarantees |
|---|---|
| `lmrun.py` | how `pairs.py` and `graphrag.py` call a model: `cache=False`, one record per call in `Plan/runs/<subject>/lm/`, status `answered` / `refused` / `unparsed` / `unreachable` — never a score — and **a real model refused without `approval=`** naming the author's decision. `make_lm()` builds three kinds of name (decision 011): `claude-cli/…`, `route/…` — one free OpenRouter model through `route.py`, pinned — or a LiteLLM string |
| `claude_lm.py` | Claude as a DSPy model through `claude -p`, first party (decision 011): no tools, no MCP, no settings, no session written, an empty working directory so no `CLAUDE.md` is loaded, thinking off unless asked, and cost and failures recorded the way `lmrun` reads them |
| `lm_fixture.py` | an offline `dspy.BaseLM`; `offline()` hides every `*_API_KEY` and replaces `litellm.completion` with a refusal, because a scanned repository's unmocked test made a live call from this container |
| `baseline.py` | `Plan/runs/baselines.jsonl`, append-only; `compare` fails a candidate that does not beat the **floor** — the floor candidate's newest row on the same trainset — not only one that fell since the last row, and a `vetoed` row fails whatever its score |
| `pairs.py` | one-term-or-two: a rule first (`fold()`, or the plural rule of decision 010), a model only on the residual, folds that keep a repeated surface pair together, repeats, and every compiled program asked the never-merge canaries as often as a held-out pair; J5 is excluded from model training, and the `labeled` rung reserves two demo slots for other hard negatives. `report` splits every ledger row into merges found and **false merges**, by judgement id; `--evidence` adds the document lines code places (never to a free model); `final` compiles once and saves the program |
| `check_dspy_surface.py` | asserts, by `inspect.signature`, each DSPy parameter this repository passes |
| `check_dspy_skill.py` | asserts what the `dspy` skill teaches: every parameter and default in its `surface` blocks, one offline probe per `[checked: …]` mark, every repository path it names |
| `check_skills.py` | the skill spec, and P6: `.claude/skills/<name>` is a symlink into `.agents/skills/` |

**89 <!--state:pairs.labelled--> labelled pairs; `fold()` decides
48 <!--state:pairs.fold_correct--> of them, and the plural rule of decision 010
decides 57 <!--state:pairs.plural_correct-->** — a row on the ledger, not part of
`fold()`, so reconciliation is unchanged. Every optimizer on the ladder —
`labeled`, `bootstrap`, `inferrules`, `simba`, `gepa` — runs end to end with
`--dry-run`. **On 2026-09-25 it ran on real models for the first time**, under
decision 011 — the author's „Use dspy Optimierung on the Scripts" and „Add
openrouter free Models in the mix": Claude through `claude -p`, and OpenRouter's
free models through `route.py`. `python3 scripts/pairs.py report` prints every
row; `Plan/concept/dspy-optimization_2026-09-25.md` reads them. **No model's
decision has entered `judgements.jsonl`**: a row on the ledger is a measurement,
and a merge a model proposes is still a person's call. `scripts/rlm_ingest.py`
requires `--approval`, turns its cache off, sets a call budget, hands the model
`find_line` and `count` as tools, and measures how far into the document its
verified citations reach.

**Not every model call goes through `lmrun.py`.** `rlm_ingest.py` builds its own
`dspy.LM` with the same two refusals — cache off, `--approval` required.
`bilingual.py` and `jev_entities.py` call OpenRouter and Jev directly, with
their own cache, and were written before it. `scripts/route.py` is the door for third-party tools and
for direct calls under decision 007: free models only, the consent file where
`lmrun` takes `approval=`, every call recorded and replayable offline, and a
repeat made fresh by `attempt > 0` rather than by turning the record off (P18).
One rule — no corpus text leaves without the author's decision — now has three
encodings, which is the drift P6 names. Decision 008 keeps all three as they are
until one changes its rule and the others do not. **For a DSPy program on a free
model they now compose rather than repeat**: `lmrun.make_lm("route/…")` sends the
program's calls through `route.py`'s proxy, so `lmrun` holds the approval and the
per-call record and `route.py` the price, the data policy, the twelve-word guard
and a pin to the one model the run measures.

**`.agents/skills/dspy` is where the knowledge behind these scripts lives**,
sorted by the job at hand: API, optimizers, metrics, data, testing, RLM,
retrieval, text artifacts, operations, patterns, and an index of the nine
repositories. On 2026-09-24 the nine repositories were read again, in full, for
everything they contain rather than for ideas; the readers' notes are in
`Plan/concept/dspy-extract_2026-09-24/`.

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

**A second: navigation on the chapter pages.** `## What this chapter is about`,
`## Questions for this chapter`, `## Candidate sources` and `## Raw qmd answers`
are written by `scripts/chapter_sources.py` from a run in
`Plan/runs/qmd-chapters-2026-09-26/`, carry no citation or reading, and are
replaced whole on every run. Their commit names the run, and changes nothing
outside those four sections. The raw answers are source text copied by code into
```` ```qmd ```` fences in `Plan/runs/qmd-chapters-2026-09-26/raw/kap-NN.md`; the page's
`## Raw qmd answers` section is one link to that file, and `quotes.py` skips that
info string and no other.

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
plainly rather than papering over it. **Which lists are gold is decided by rule**
in `scripts/gold.py` (decision 009): written while reading, counted, unchanged
since the count, and of its document — whoever wrote it.

**Every reader so far has been Claude**, the gold lists and P27's two readers
included; no reading by the author is recorded. Two saved workflows measure the
reading itself, and both ran once on 2026-09-24:

- **`.claude/workflows/blind-rereading.js`** has a document read again, blind.
  `python3 scripts/agree.py <slug>` compares the lists by F1, and by how much of
  each the other holds, because F1 falls with a longer list however well both
  read. Two blind readers agreed at 0.82–0.93 on documents 5, 6, 7 and 10, and
  each held 97–100 % of the committed list. Readers differ in what they select,
  not in what they see (`Plan/learnings/extract-terms.md`, *Blind re-readings*).
- **`.claude/workflows/record-audit.js`** checks what the conflict and question
  records attribute to a document, and what they miss. On documents 7–13, 274
  of 289 attributions were faithful. Of 83 findings, both skeptics upheld 9.
  Those nine, and five misstatements the text skeptic confirmed, are now in the
  records (`Plan/runs/record-audit-2026-09-24/`).

## Learnings

`Plan/learnings/` holds one file per step: what was learned, what the tool must
handle, what stays judgement, and real measurements. Steps that have not run yet
carry predictions instead, so the eventual learning can be checked against what
we expected.

**Write in them as you go.** They are how a step done by hand becomes a tool
later without re-deriving the reasoning.

## Tracking work

`NOW.md` holds what is open right now, one page, and things leave it when they
are done. **Questions for the author are noted there, under their own heading, and
work continues without waiting for the answer** — the author's instruction of
2026-09-24. `Plan/decisions/` holds one short file per decision, permanently —
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
