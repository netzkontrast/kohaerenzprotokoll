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
`.claude/hooks/session-start.sh` runs it at every cloud session start —
synchronously, so no step races an install, and never blocking the session on a
failed component. `scripts/install.sh --check` says what is present,
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

`Sources/manifest.jsonl` is the spine: 613 rows, each with `drive_id`, `title`,
`slug`, `category`, `tier` and, once landed, `export_path` and two checksums.
Anything derived traces back to a `drive_id`.

`Sources/duplicates.jsonl` holds the 67 rows that left it — the same shape plus
`duplicate_of`. Two files, two questions: the manifest says what is in the
corpus, and this says what Drive also holds and why it is not here. It exists so
that „not in the manifest" never has to mean „nobody knows".

## State, as of 2026-09-17

**371 <!--state:sources.landed--> of 613 <!--state:sources.total--> source documents are landed.** The 242 that are not all date from before May
2026: 231 `plot-outline` rows, deferred with the novel, 10 `md` in `storyform`
and `kernkonzept`, and one `mp3`. Every category the wiki needs is complete, and
so, since 2026-09-24, is the canon era: all 33 <!--state:sources.canon_era--> rows
dated May 2026 or later, 33 <!--state:sources.canon_era_landed--> landed, fourteen of them
read (documents 7 to 20).

**Those files are 371 <!--state:sources.distinct--> distinct documents, and
that took work.** Drive holds up to five exports of the same document — a gdoc
export, a docx export, a `kopie` of each, a second run of both — and each landed
under its own `drive_id`. 409 files were 346 documents, so **every count phrased
as "N of 409" was counting copies.** Only 2 pairs were byte-identical, so
checksums found almost none of it.

`python3 scripts/dedupe.py` folded the
67 <!--state:sources.folded--> extra files away. The file left `Sources/drive/`,
the row left the manifest — 680 rows became 617, and the canon-era landing's four
copies took it to 613 — and the full row moved to
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

**20 <!--state:documents.with_census--> have a term census** in `Sources/terms/`, **20
<!--state:documents.with_note--> have a note** in `Sources/notes/`, and **20
<!--state:documents.reconciled--> are reconciled**. Three are `theorie-physik`,
four `worldbuilding`, one `aegis`, two `storyform`, three `charaktere`, three
`kernkonzept`, three `plot-outline` and one `theorie-psychologie` — the last fourteen
from the canon era.

`Wiki/candidates/` holds **94 <!--state:wiki.pages--> pages**, `Wiki/conflicts/`
holds **15 <!--state:wiki.conflicts-->**, `Wiki/questions/` holds
**5 <!--state:wiki.questions-->**, and
`Wiki/compare/` holds the reconciliation record per document. The schema follows
the pages rather than preceding them, so `Wiki/terms/` does not exist and nothing
has been promoted.

**Beside the terms, the chapters (decision 013).** `Wiki/chapters/` holds
**41 <!--state:wiki.chapters--> chapter pages**, Kap 0 to Kap 40, with
**321 <!--state:chapters.readings--> readings** from the eight read documents
that go chapter by chapter and one that names six chapters; `Wiki/overview/` lays the chapters and the plot's
shape side by side. See *Chapters and the plot*, below.

| document | new terms | new readings | new conflicts |
|---|--:|--:|--:|
| `entropie-aegis` | 14 | — | 0 |
| `aegis-emergenz-aus-der-leere` | 10 | 2 | 2 |
| `kohaerenzprotokoll-aegis-und-systementropie` | 8 | 7 | 1 |
| `guardians-und-kern-welten-konzept` | 14 | 4 | 1 |
| `aegis-subplots-kapitelweise-system-exploration-docx` | 0 | 2 | 0 |
| `roman-lokalitaeten-konzept-und-ausarbeitung` | 10 | 17 | 1 |
| `kohaerenz-protokoll-storyform-und-outline-2026-06-10-md` | 4 | 17 | 1 |
| `kohaerenz-protokoll-charakter-bibel-2026-05-08-md` | 16 | 22 | 4 |
| `koharenz-protokoll-konzept-konsolidiert-2026-05-08-md` | 2 | 45 | 2 |
| `kapitel-kompendium-gather-2026-05-31-md` | 0 | 28 | 0 |
| `kohaerenz-protokoll-kernwelten-vollstaendig-2026-06-10-md` | 7 | 42 | 0 |
| `dramatica-dual-storyform-status-2026-05-07-md` | 0 | 16 | 0 |
| `kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md` | 7 | 43 | 0 |
| `koharenz-protokoll-strukturierter-outline-2026-05-18-md` | 0 | 43 | 0 |
| `koharenz-protokoll-konzept-iteration-genesis-md` | 1 | 22 | 0 |
| `kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md` | 0 | 53 | 0 |
| `kohaerenz-protokoll-anteile-profile-sprach-dna-2026-06-10-md` | 0 | 38 | 0 |
| `kp-plot-konkretisierung-13-ideen-f1-faden-2026-06-10-md` | 0 | 31 | 0 |
| `koharenz-protokoll-sprach-dna-2026-05-13-md` | 0 | 32 | 0 |
| `kohaerenz-protokoll-konzept-master-md` | 1 | 46 | 0 |

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

**The seventh is the first canon-era document, and it claims to be canon.** It
names itself „Source-of-Truth", labels every passage `[K]`/`[V]`/`[S]`/`[L]`,
never hedges, and states its own precedence rule — newer wins. **The wiki records
that claim and does not apply it**; a source granting itself authority is what
the predecessor honoured and this project does not. 275 of its candidates matched
no page. Four became pages, by a rule the document supplies: it says its figures
are only „outline-relevante Kurzanker" and its physics is elsewhere, so a page
needs a `[K]` reading of something in the world. It contradicts every earlier
source on the Guardians — two, not five, and „KEIN Guardian-1:1" — which is
conflict C6.

**The eighth is the character bible, and it disagrees with the seventh.** Dated a
month earlier, it relates C6's two versions itself — „Frühere Drafts hatten fünf
Guardians … Aktueller Kanon: zwei" — and gives the twelve Alters the profiles
document 7 said they would need. It also disagrees with document 7 in four
places (C7–C10): where Juna appears, AEGIS' Approach in Storyform B, what the
Konstrukt-Stadt is, and whether Kael's knuckles bleed in Kap 1. **Two canon-era
sources disagreeing is the case the wiki exists for**, and document 7's „newer
wins" would settle all four; the wiki records both and the dates. **And the
author has said it must not be settled that way**: „Alle alten Entwürfe kommen
wieder in Frage und müssen diskutiert werden — sources wird die neue
Ausgangslage" (decision 006). Every conflict is a discussion item, and no
document's date or claim to be canon retires another.

**The ninth is the consolidated concept, dated the same day as the eighth**, and
it names itself „autoritative Spec" — recorded, not applied. It sides with
document 7 on C7 and C8 and so disagrees with the character bible of its own
date; it counts the Genesis in four beats where the bible counts three (C12);
and it is the older outline document 7 overrides on Landauer warmth (C11), in
the exact words document 7 quotes. **Two sources of one date disagreeing is the
case no precedence rule by date can settle.** Two pages came from it, both
flat definitions from the physics it calls the literal law of the novel's world:
`erason` and `persistenzgleichung`.

**The tenth is the Kapitel-Kompendium, and it names its own filter.** A gather,
chapter by chapter, that labels every passage and says what it changed on the way
from its quarry: „Michael→Kael · Julia→Juna · 20 Kernwelten / 5 Guardians → 4 KW,
2 Guardians". So two renames the wiki had inferred from dates are now stated by a
source. Conflict C7's record named it as what would settle C7 and called it not in
`Sources/`; it was landed, and it does not settle C7 — it places no direct
appearance for Juna. **It added no pages**: a gather places, it does not define.

**The eleventh is „Kernwelten vollständig", and it shows how C7 might not be a
conflict.** It puts the character bible's Kap-33 garden down as Juna's *effect* —
„Setting der Juna-Wirkung" — and her appearance in Kap 38, so both earlier
positions have a place in one plan. It holds the Möglichkeits-Garten at both
scales (C5), applies document 7's cold-ozone lock and keeps Landauer warmth for
the transition out of KW1 (C11). Seven places got pages by a rule it supplies: a
canonical sub-location with a specific chapter.

**The twelfth is the Dramatica lock-in of 2026-05-07, and it explains C8.** It
mirrors the Approach — „A: Be-er (vorher Do-er). B: Do-er (vorher Be-er)" — and
says the older documents still have to follow. The character bible, dated the next
day, carries the „vorher". An explanation, not a decision: the author decides.

**The thirteenth is the glossary of the storyform document, and it ranks itself
below it** — „erläuternd, nicht normativ". It gave the physics its pages (`dkt`,
the two kernels, `atemporalitaet`, the three layers), gave the two most contested
subjects theirs (`hitze-polaritaetsregel`, `genesis`, each gathering every
source's version), added a fourth sense of Entropie to C2 — K₀ as „die Bedingung
für Ereignisse überhaupt" — and named the Kapitel-Kompendium as the source of
document 7's knuckle lock.

**The fourteenth is the chapter outline of 2026-05-18, and it placed things
rather than defining them**: no pages, readings on 43. It moved the chapter
conflicts. Juna's first direct appearance is Kap 38 Beat 3, stated five times
(C7). The knuckles are a standing trait of Kael's, in no chapter — a third
position for C10. The Landauer trace is warm in Kap 6 and Kap 36, in the
konsolidiertes Konzept's words (C11). The Genesis runs in both orders with a
fourth beat, two weeks before the Kapitel-Kompendium does the same (C12). It
also absorbs LogOS and Kairos two different ways in one document, and places
Sophia — latent, in KW4 — for the first time in a 2026 source (Q5). **Reading it
found the quotation check blind to its numbers**: every „Kap 38" was compared as
„Kap", so `quotes.py` now compares numbers on their own (*A quotation is checked
against its line*, below).

**The sixteenth is the drafting manual of 2026-06-10, and it contradicts itself on
C11.** „Welt, Sensorik, Drafting-Disziplin" restates every lock with its date and
source, and files the Landauer-Signatur under cold ozone — while its own first
foreshadowing strand, named `Landauer`, has the theme „Hitze als Symptom der
Wahrheitsvertuschung" and accumulates in Kap 6. The wiki keeps strand and
signature apart (J81) and records the tension in C11 rather than choosing. It
states two Guardians and retires the Guardian-world pairing by name (C6, Q5);
the author's decision for five stands. **No pages, readings on 53**: a manual's
vocabulary is its method, and its world lands on pages that exist.

**The seventeenth is the Alter profiles, and it places heat three ways.** „Anteile,
Profile, Sprach-DNA" profiles the thirteen Alters from the character bible, which it
calls „autoritativ" — recorded, not applied. It gives warmth to Silas, Juna's echo
inside the system, under the same 2026-05-30 lock that gives it to Juna. It also
makes Landauer heat the mark of the Silas–Oblivion conflict, and keeps heat as
Juna's trace in its foreshadowing list. All three go into C11. It is the first
document read under decision 012's list rule, and the sweep found one reading
the list had missed. **No pages, readings on 38.** A second, independent reading of it the same
day (pull request #88) found two conflicts this reading's pages held and no record
did: whether AEGIS gets a first-person chapter — a lock of 2026-05-30 says one, in
Kap 5–8, and this document gives AEGIS the third person and never prose (C14) — and
who carries Flight, Kiko and Lia or Lia and Isabelle (C15). It also gave C11 the
character bible's entry, which the record had never held.

**The eighteenth is the Plot-Konkretisierung, and it is a proposal about the locks.**
Thirteen plot generators and one, F1 „Der Sachbearbeiter der Abweichung“, worked out
from Kap 0 to a Kap 40 coda. Everything in it is `[V]` unless it cites a `[K]` lock, so
every reading from it opens by saying so. It works out the cold side of C11: cold ozone
after every Ausgleich, Kap 6 cold, and Kap 36 Beat 4 the „einziger kanonischer
Landauer-Wärme-Ort“. Silas' warmth is the Coheron-Echo. **No pages, readings on 31.**
**Its lookup found a defect in `fold()`**: `A:RS`, Storyform A's Relationship Story, folded
to `ars` and was filed as a reading on the ARS protocol's page. `fold()` now keeps the
colon (J87). No page surface contains one, and the self-test fails on the old code.

**The nineteenth is the Sprach-DNA of 2026-05-13, and it gives AEGIS an inside in the
third person.** A voice catalogue — nineteen voices in five fixed fields — that says it
consolidates the character bible and the konsolidiertes Konzept; recorded, not applied.
AEGIS never says `ich`, and still the reader is in its process, an „Operative
Interiorität" — neither the older sources' logs without an inner view nor the first
person the lock of 2026-05-30 gives one chapter (C14). Its Landauer warmth is „spürbar
als Ozon-Geruch oder Hitzeschlieren": both sides of C11 as one thing's two renderings,
seventeen days before the lock. It puts Juna's appearance in Kap 38 (C7) and the bleeding
knuckles in Nyx's voice, in no chapter (C10). **No pages, readings on 32.** It was read
beside the eighteenth on purpose: the other session's handover had named that one, and
the two sessions had already read documents 16 and 17 twice each.

**The twentieth is the konzept master report of 2026-05-08, and it counts 39 chapters
and one Vortex.** A theory report in sixteen chapters that calls every earlier PDF
„Steinbruch" and itself the „Fundament" — recorded, not applied. It dates its status
`Canon-Sync 2026-05-07` and sides with the character bible of its date on the Genesis —
three beats, locked (C12) — and with the Dramatica lock-in on AEGIS' Do-er (C8). Its
roster of thirteen has no alter with Flight, and its riss table gives Flight to Lia and
Isabelle „implizit" (C15). Heat and ozone are one signature of AEGIS' erasure (C11), and
Juna's revelation falls in Akt II, with no chapter (C7). **It gave the Truth-Rotation
its page**, gathered from all eight read sources that name it: they agree AEGIS = K₀ and
part on whether the name means the inversion or the moment the reading turns (J91).
**And it made two lines of `Wiki/overview/plot.md` false**: not every 2026 plan counts
41 movements, and not every one has two Vortices — this one, dated the same day as the
konsolidiertes Konzept, has neither. **It was read twice**, by two sessions following the
same handover (pull requests #94 and #95); the reading merged first is the wiki's, and the
other is a blind list, `03-candidates-blind-1.md`. `agree.py` measures the two at F1 0.76,
each holding 76–77 % of the other, both under decision 012's rule. The second reading
added two judgements on clipped words (J92, J93), a question on KW2's two names, and two
tool fixes — `chapters.py` read the escaped approximate range `Kap 14–\\\~20` as a single
Kap 14, and `link.py` marked another occurrence of an already-linked term on every run —
each with self-test cases the old code fails.

`Plan/runs/judgements.jsonl` holds **93 <!--state:judgements.total--> judgements**
about near matches, **8 <!--state:judgements.mechanised-->** mechanised and
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
is recorded in `Plan/runs/sweep.jsonl`: 33 <!--state:sweep.decided--> so far,
17 <!--state:sweep.readings--> of them readings the lookup had missed, and
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

**And `python3 scripts/selftest.py` proves they can fail.** Seven quotation cases,
six citation cases and nine `fold()` pairs, each carrying the exact defect the
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

**372 <!--state:wiki.relations--> links across
94 <!--state:wiki.pages--> pages, 27 <!--state:wiki.orphans--> of them with
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

The 227 <!--state:wiki.unmarked--> mentions still unmarked are ones where every
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

**91 <!--state:chapters.missing--> chapter mentions** in read documents have no
reading on their chapter's page yet — the character bible's Kap-33 scene among
them. The count sees `Kap N` written singly; a range and a numbered list without
`Kap` are invisible to it, so it under-counts. A range with an approximate bound,
`Kap 14–\\\~20` as the export escapes it, was read as a single Kap 14 until
2026-09-25. Reading a new document now ends,
where it names chapters, with its readings on those pages.

**Reading the chapter outlines side by side corrected a claim.** `NOW.md` said
every read source but one ended at Kap 39; seven of the eight count a Kap 40.
The konzept master report, read after, counts 39 chapters with no frame and one
Vortex — two of `plot.md`'s claims about every 2026 plan, corrected there.

### The knowledge graph, and retrieval over it

The wiki is also a typed knowledge graph, derived and never stored:
`scripts/graph.py` reads frontmatter, `[[links]]` and `^[slug.md:Lnn]`
citations and builds **134 <!--state:graph.nodes--> nodes** (terms, documents,
conflicts, questions) and **1814 <!--state:graph.edges--> edges** (`links`,
`reads`, `cites`, `contests`, `raised_by`, `asks`, `concerns`). **Every edge
carries the file line that states it**, and none is inferred — the same rule as
the links, for the same reason.

Its evidence is every quotation on a term page: 2360 <!--state:graph.evidence-->
of them, **2360 <!--state:graph.evidence_verified--> verified** against their
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

`bench` scores retrieval on the 20 <!--state:graphrag.cases--> cases the wiki
already labels (each question's `raised_by`, each conflict's `pages`), with the
case's own node removed first. Recall@8 is
**47 <!--state:graphrag.recall_seeds-->% from the seeds alone and
66 <!--state:graphrag.recall_ppr-->% with PageRank** — the graph earns its
step, on twenty cases whose labels were written by the same hand as the
pages. Documents 7–9 added seven of them (C6–C12), the author's C6
decision an eighth (Q5), document 16 a ninth (C13) and document 17 two
more (C14, C15); on the original nine the numbers were 40 and 58.
Document 19 moved them from 48 and 67 by giving C11 three more pages: its
gold set grew from two pages to five, and the case fell from 1.0 to 0.6 with
PageRank. The fall is that label growing; on the labels that did not change,
retrieval rose — C6 from 0.29 to 0.43.
`bench --record` appends both to `Plan/runs/baselines.jsonl`.

**Beside the graph, never in it: the proposal layer.** `graph.proposals()`
reads what a model chose or the corpus merely co-states, and each item says so.
**300 <!--state:proposals.entities--> entities** come from the entity lists that
verify as readings — a model chose the name, code placed the line — and
49 <!--state:proposals.entities_paged--> of them fold to a page. **182
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

40 of the 613 rows are markdown or audio, which the connector does not list as
supported — but `md` comes through the text route: 26 of the 39 `md` rows are
landed, 4 on 2026-09-16 and 22 more on 2026-09-24 with
`fetch --since 2026-05-01 --include-md`. `--include-md` is opt-in. The other 13
`md` and the one `mp3` stay deferred by decision.
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

Seven venvs are defined, all git-ignored, each for one reason. **None survives a
container**; `scripts/install.sh` rebuilds each, and the commands below are what
it runs:

| venv | python | why |
|---|---|---|
| `.venv-tools` | 3.11 | markitdown and its converters, for `sources.py land` |
| `.venv-dspy` | 3.11 | DSPy 3.3.1 with numpy and Deno — every `scripts/` step that calls a model or its fixture |
| `.venv-dspytools` | **3.12** | `dspytools`, which refuses 3.11 |
| `.venv-typesafe` | 3.11 | `typesafe-sdk`, for Jev — `scripts/jev_entities.py` (a test) and `scripts/bilingual.py` |
| `.venv-grawiki` | **3.12** | `grawiki[falkordblite,viz]` from `netzkontrast/grawiki` at `920d181`, which refuses 3.11; about 2 GB with CPU torch |
| `.venv-semantica` | 3.12 | `semantica==0.7.0`, the base package without extras — a knowledge-graph library with provenance tracking; about 480 MB |
| `.venv-mflow` | 3.11 | `mflow-ai`, M-flow's graph memory — nothing calls it |

```bash
uv venv --python 3.11 .venv-dspy
uv pip install --python .venv-dspy/bin/python 'dspy[deno,numpy]==3.3.1'   # SIMBA raises without numpy; dspy.RLM needs Deno
.venv-dspy/bin/python scripts/check_dspy_surface.py                        # the surface this repo calls
.venv-dspy/bin/python scripts/check_dspy_skill.py                          # the DSPy the dspy skill teaches
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

**Four more vendored folders are Notion skills**: `knowledge-capture`,
`meeting-intelligence`, `research-documentation` and `spec-to-implementation`,
copied unchanged (plus its `LICENSE`, MIT) from `netzkontrast/notion-skills`
commit `e1bab42f8337b93b833eb01d9edcde067125690f`, path
`plugins/notion-skills/skills/`. They are vendored rather than installed as a
plugin because that repository's `.claude-plugin/marketplace.json` fails
`claude plugin validate` — its `skills` field lists bare names where paths are
expected — so a settings-registered plugin would not load.

Their `NOTION_API_TOKEN` configuration does not apply here: Notion is reached
through the claude.ai Notion connector (`mcp__Notion__*`), which carries its own
auth, and no token is written to a file. Notion is outside the two layers: no
script reads it, and nothing in `Wiki/` or `Sources/` may cite a Notion page.
Anything sent there is corpus text leaving the repository, so the same rule as
Jev applies — the author's yes first.

**`.claude/skills/knowledge-graph-extract` is vendored too**, copied unchanged
(plus its `LICENSE`, MIT) from `netzkontrast/knowledge-graph-extract` commit
`542fffaeaf18f4db6eb3f32c7a93c2c54822f67c`. It has a model read a folder of
documents into subject–relation–object triples, with four standard-library
scripts to validate them and write Cypher. Its manifest passes
`claude plugin validate`; it is copied rather than registered only so all
third-party skills sit in one place, pinned the same way.

A triple it writes is a model's reading, in the same standing as an entity list:
it may not create a page, write a `[[…]]` link, supply a count, or merge two
surfaces — a guessed edge is indistinguishable from a stated one once it is in
the graph (see *The wiki links*). Its output directory goes outside `Wiki/` and
`Sources/`. Nothing in the pipeline calls it yet. **Run once, 2026-09-24, as a
second reader on document 14**, with Claude as the model so no text left: 200
triplets in 35 minutes, F1 0.37 against the reader's list, the best second reader
measured —
`Plan/runs/koharenz-protokoll-strukturierter-outline-2026-05-18-md/second-readers/README.md`, which also measures what
makes it faster.

**`.claude/skills/graphify` is the skill `graphify install --project` writes**,
from `netzkontrast/graphify` commit `4c735618f3d56fd622c2049771584621c31ba9ff`
(graphify 0.9.67, Apache-2.0 with MIT and NOTICE copied beside it). It drives the
`graphify` CLI, which is not in the repository — see the table at the top. Only
the skill folder was kept. The same install also appends rules to `CLAUDE.md`
and registers `PreToolUse` hooks on `Bash|Grep` and `Read|Glob` that run
`graphify hook-guard`; neither is here, because in a fresh container the binary
is absent and every one of those calls would run a failing hook, and the rules
would route questions to a graph ahead of `read.py`, `corpus.py` and qmd.
Its `INFERRED` edges are a model's reading under the same limits as
`knowledge-graph-extract`, and `graphify-out/` is git-ignored. Its document mode
needs no key — the skill has the host agent read — and ran once that way on
document 14 (the same README): its AMBIGUOUS edges found four of the document's
inner tensions by themselves.

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
links. It has 372 <!--state:wiki.relations-->.

```bash
uv pip install --python .venv-dspy/bin/python "drg-kg[extract] @ git+https://github.com/netzkontrast/drg-kg"
```

**Nothing in the pipeline calls any of the three yet.** They are installed,
reachable, and measured against this repository —
`Plan/concept/continuous-improvement_2026-09-17.md` has what each is for and in
what order.

`grawiki` is a library, not a skill: a model reads chunks of a document into a
graph held in FalkorDBLite, a local file with no server. It stands where
`knowledge-graph-extract` stands — the same author's framework, of which that
skill is the counterpart — and under the same limits: its graph is a model's
reading and supplies no page, link or count. `--torch-backend cpu` is
deliberate: `chonkie[st]` pulls sentence-transformers, and a container has no GPU.

`code-graph-rag` (`cgr`) is a uv tool on Python 3.12. Without
`--with "transformers>=4.40"` the resolver falls back to transformers 4.12.2,
whose tokenizers needs a Rust build that fails.

`semantica` is a library in the same family: context graphs with provenance
and reasoning over them. Only the base package is installed — its LLM, document
and embedding extras are not — so it builds and queries graphs a caller hands
it and extracts nothing by itself.

All three are installed and start; none has been run against the corpus, and
nothing in the pipeline calls them. Their graphs stand under the same limits as
`knowledge-graph-extract`: no page, link or count comes from one.

**Hyper-Extract** (`netzkontrast/Hyper-Extract` at
`395039ea49709b279971631a47569b931818abbb`, Apache-2.0) is three things here:

- **`he`**, a uv tool on Python 3.12 with the `mcp`, `ingest` and `anthropic`
  extras. `he parse` has a model read documents into a *Knowledge Abstract* —
  a graph, hypergraph, list or record set shaped by a YAML template — and
  `he template validate` checks a template without any model.
- **`he-mcp`**, registered as the `hyper-extract` server in `.mcp.json`. Its
  nine tools read and export an existing Knowledge Abstract (`list_templates`,
  `info`, `search`, `ask`, `export_obsidian|graphml|csv|jsonld|cypher`); none of
  them extracts. In a brand-new container the server can start before the
  session hook has installed `he-mcp` — reconnect it with `/mcp`.
- **Seven template-design skills**: `hyper-extract` (the entry point) and
  `hyperextract-brainstorm`, `-record-designer`, `-graph-designer`,
  `-yaml-validator`, `-template-optimizer`, `-multilingual`. Upstream nests them
  in one `hyperextract-skills/` folder, which Claude Code does not discover, so
  each is its own top-level folder with the prefix added; every file is
  unchanged. Two of the bundled cases, `battle-analysis.yaml` and
  `biography-events.yaml`, fail `he template validate` (HE-T001, not parseable)
  as shipped.

No provider is configured. `he` reads `~/.he/config.toml` and falls back to
`OPENAI_API_KEY` and `OPENAI_BASE_URL`; the key goes in the environment's
settings or `he config`, never in this repository. `he parse`, `search` and
`ask` send text to that provider, so the Jev rule applies — the author's yes
before corpus text goes. A Knowledge Abstract is a model's reading under the
same limits as `knowledge-graph-extract`: no page, link or count comes from it,
and it is written outside `Wiki/` and `Sources/`.

**Four project templates exist and none has run**: `Plan/hyperextract/`
(`TermCensus`, `LocationRegistry`, `TermReadings`, `StatedRelations`), each
copying the shape of something already here so code can score it, each marked
provisional. `python3 scripts/templates.py check` holds them to Hyper-Extract's
validator, to loading as `he parse` loads them — the validator passed a field
that loading rejects — and to five rules of this project: no line field (P26), no
model merge (P13), an explicit merge strategy, the provisional header, and no
corpus name in any text a model is sent. `selftest` shows each check failing on
its defect. `Plan/concept/hyperextract-templates_2026-09-24.md` has the design,
the optimiser's report and how each is scored.

**oh-my-openagent** is a different kind of thing from everything above: not a
library or a skill for Claude Code but a plugin for another agent harness,
[OpenCode](https://opencode.ai). `scripts/install.sh omo` installs
`opencode-ai@1.18.32` with npm and runs the plugin's own installer at `4.19.4`
with the author's answers (2026-09-24): OpenCode, Claude Max 20×, ChatGPT Plus,
Gemini, no Copilot. That writes `"oh-my-openagent@latest"` into
`~/.config/opencode/opencode.json` — so OpenCode loads whatever is newest, not
the pin — and the agent → model routing into `~/.omo/omo.jsonc`: `sisyphus` on
`anthropic/claude-opus-5`, `oracle` on `openai/gpt-5.6-sol`, and so on down its
roster. Both files are outside the repository and regenerated per container.

What it does not do, and why:

- **No provider is signed in.** It runs with `--skip-auth`; `opencode auth login`
  is a browser OAuth flow a container cannot finish, and its tokens would live
  in `~/.local/share/opencode/auth.json`, which the container loses. OpenCode
  with this plugin is usable where the author signs in — their own machine —
  and here only as far as `doctor` and `opencode agent list`.
- **`config migrate` is not run.** At 4.19.4, `doctor` reports the installer's
  own `variant`/`fallback_models` keys as deprecated and names `config migrate`
  as the fix; the migration rewrites agents to `models`, which the same
  validator then rejects, and `doctor` goes from warnings (exit 0) to eight
  errors (exit 1). The installer's output is kept as it writes it.
- `doctor` also warns that `sg` (ast-grep) and `gh` are absent. Neither is
  installed.

Its telemetry is on by default; `OMO_SEND_ANONYMOUS_TELEMETRY=0` turns it off.
Anything an OpenCode agent reads from the corpus goes to the providers above,
so the Jev rule applies to it as to everything else here.

**M-flow is installed on its own**, from the fork `netzkontrast/m_flow`, which
has no commits of its own. Its head, `0d585cd` of 2026-08-03, is an upstream
commit:

```bash
uv venv --python 3.11 .venv-mflow
uv pip install --python .venv-mflow/bin/python "mflow-ai @ git+https://github.com/netzkontrast/m_flow"
.venv-mflow/bin/mflow --help                # runs with no key and no network
```

It is not in `.venv-dspy`, because resolved beside DSPy 3.3.1 it moves four of
DSPy's packages down, `pydantic` 2.13.5 → 2.12.5 among them. It builds a
four-level graph — Episode → Facet → FacetPoint → Entity — in file-based Kuzu,
LanceDB and SQLite, and by its own account scores each Episode by the cheapest
path of evidence to the query. **Its default path breaks two rules this wiki
keeps:** `memorize` has a model write the Facets and FacetPoints, and `search`
has a model write the answer. Both steps call OpenAI by default, for the model
and for the embeddings, so running either on corpus text sends that text to a
third party. That waits on the author's yes. Its own unit suite passes 1232 of
1235, run against the installed package with every key hidden and the network
dead. One test is skipped, and the two failures time out retrying the embedding
call. Even `mflow add` refuses without a model key, because every pipeline run
first probes the model and the embeddings with the word „test". It writes only
inside the venv. **Nothing calls it.**
`Plan/concept/m-flow_2026-09-24.md` has the measurement, the two entry points
that keep the rules (`manual_ingest` and `search(only_context=True)`), and the
experiment that would decide whether it earns a place.

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

**79 <!--state:pairs.labelled--> labelled pairs; `fold()` decides
46 <!--state:pairs.fold_correct--> of them, and the plural rule of decision 010
decides 54 <!--state:pairs.plural_correct-->** — a row on the ledger, not part of
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
