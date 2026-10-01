# The ingest pipeline, in steps — and its new first step

**2026-10-01 · A plan, not a description.** On the author's „Lass uns strategisch vorgehen… und die rag Pipeline mal in
klaren steps planen … erkläre in einer readme.md die neue ingest Pipeline - fokussierend auf dem aller ersten Schritt".
Every step below carries a status: **exists** (a command runs it today, named), **partly** (some of it runs, the rest is
named as missing) or **proposed** (nothing runs it yet). `CLAUDE.md` describes only what exists; this page is where the
plan lives until a step exists, and then the step's line here is changed to name its command.

## 0. Why a new first step

Today a document goes from Drive to `Sources/drive/<slug>.md` and then straight to a *reader*: a person or an agent
reads it, writes a candidate list, a census, a note, and a reconciliation puts its readings on the wiki's pages. The
graph (`graph.py`, `askdb.py`) is built afterwards — from the wiki, and from what `askextract.py` can read off the raw
lines. Two consequences, both measured:

- **Most of the corpus is in no graph that knows its structure.** 58 <!--state:documents.with_census--> of 586 <!--state:sources.landed--> documents have a census; the rest enter
  `ask.db` as lines, paragraphs and mentions of the wiki's own surfaces, and nothing more. A question whose evidence is in
  an unread document is answered from flat text (`Plan/concept/evaluation-audit_2026-09-30.md`, §0.2: discovery cannot
  even be scored).
- **What the project has learned about its documents is spread over a dozen scripts.** The export damage
  (`rules/export_damage.py`), the heading structure (`rules/structure.py`), the capitalised surfaces (`rules/surfaces.py`),
  the attribution markers (`rules/attribution.py`), the profile (`profile.py`), the blocks and their kinds
  (`askextract.py`), chapter references (`chapters.py`, `askextract.py`), the stance markers `[K] [V] [S] [L]`, the
  contracts' cues (`hegraph.gate`) — each computed where it was first needed, several twice, none of them together in one
  place a retriever can read.

So the new first step is **one record per document that holds everything code can know about it, every fact with the
line it stands on** — the *document schema*. Every later step reads it instead of re-reading the text, and the graph is
built from it, not around it. It is the step that turns a text file into something a graph can be built from.

## 1. The steps

| # | step | input → output | status | command today |
|---|---|---|---|---|
| 0 | **land** | Drive → `Sources/drive/<slug>.md`, a manifest row with `sha256` | exists | `sources.py next`, `sources.py land` |
| 1 | **prepare** — the document schema | one landed file → `Plan/derived/<slug>.json`, every fact with its lines | **partly**: four rules run | `derive.py` |
| 1b | **propose** — the model's layer of the schema | the schema + a contract → proposal rows, each placed on a line by code | partly: 32 contracts, one run at a time | `he_claude.py run` (on `hx.py`) |
| 2 | **read** — a census and a note | the document (and its schema) → `Sources/terms/`, `Sources/notes/` | exists, paused by the author | skill `ingest`, `census.py draft` |
| 3 | **reconcile** — readings onto the pages | census + note → `Wiki/compare/`, `Wiki/candidates/`, `Wiki/chapters/` | exists | `reconcile.py`, `readings.py` |
| 4 | **graph** — the store | schemas + wiki → `Plan/derived/ask.db` | exists, reads the text, not a schema | `askdb.py build`, `kg.py index` |
| 5 | **retrieve** — a context pack | a question → verified lines, records, documents | exists | `ask.py`, `graphrag.py ask`, `kg.py context` |
| U | **update-ingest** — what changes when something changes | a new document, a new rule version, a new contract | partly: `derive.py` re-derives exactly | `derive.py --stale` |

Steps 2 and 3 stay what they are: the part a program cannot do, and the part that keeps the wiki honest (a reading is
attributed, never merged). What changes is that step 1 runs on **every** landed document, read or not, and that steps 2,
4 and 5 read its output.

## 2. Step 1 in detail — `prepare`: a text file, made ready for a graph

### 2.1 What it already is

`scripts/derive.py` applies every rule in `scripts/rules/` to every landed document and writes `Plan/derived/<slug>.json`.
A rule is a small, named, **versioned** function of one document (`NAME`, `VERSION`, `applies(doc)`, `derive(doc)`), and
the cache key is `(sha256, rule version)`: a document never changes once landed, so a fact stays true until its rule
changes, and bumping one rule's version re-derives that rule alone, on every document, in seconds. An exception
(`Plan/rules/exceptions.jsonl`) is a person saying a rule must not run on a document, and why — reported on every run,
never silent. **That contract is the right one for step 1 and is kept.** The four rules today:

| rule | facts | what it is for |
|---|---|---|
| `structure` | words, headings, bold-only lines, table rows, formula lines, repeated labels | how the document is built — counts only |
| `export_damage` | invisible characters, glued footnote numbers, backslash escapes, quote-glyph families | what defeats exact matching |
| `attribution` | `[User Query]` and its escaped forms, with lines | where the document reports another voice |
| `surfaces` | every capitalised token, its count and its lines | the lookup that makes a corpus question not a re-read |

What is missing is everything *between* the counts and the text: the structure itself, with spans.

### 2.2 What the record should hold — the document schema

One JSON object per document, every element addressed by **file line** (the line `^[slug.md:Lnn]` cites; `subject.py`
finds the frontmatter boundary, never assumes it). Each part is one rule, so each is versioned, cached and testable on
its own. Marked **have** where code already computes it somewhere in the repository, **new** where nothing does.

| part | holds | have / new — and where it is today |
|---|---|---|
| `identity` | slug, drive id, sha256, title, date, category, tier, language, format | have — manifest, `subject.Document` |
| `text` | the line map (file line ↔ body line), and per line the normalised form a match runs on beside the original a citation quotes | have — `subject._split`, `quotes.normalise`, `read.py`; unescaping in `rules/attribution` |
| `damage` | the export damage, per line, so a match knows where it must not trust a string | have (counts) — `rules/export_damage`; **new**: the lines |
| `outline` | the section tree: heading level, title, span; bold-only lines that act as headings; numbered parts (`Teil I`, `Kap 7`, `### A.`) | partly — `askextract` (`HAS_SECTION`/`SUB`), `rules/structure` (counts), `Plan/learnings/fetch.md` §7 (bold headings) |
| `blocks` | paragraphs as blocks with a kind — `heading`, `table`, `list`, `quote`, `text`, `formula` — and their spans; tables as rows of cells | have — `askextract` (block kinds); **new**: table cells, formula blocks |
| `markers` | stance marks `[K] [V] [S] [L]`, attribution (`[User Query]`), hedges (`könnte`, `vielleicht`, `möglicherweise`), questions, the document's statements about its own standing (`verbindlich`, `final`, `Entwurf`) | partly — `askextract` (stance), `rules/attribution`; hedges and standing are prose in the readers' notes, **new** as a rule |
| `surfaces` | capitalised tokens with lines; compounds and their heads (`Kael-Julia-Bindung` → `Kael`); joined forms `A/B`, `A (B)` | have — `rules/surfaces`, `corpus.py family`, `bilingual.py` (glosses) |
| `mentions` | every wiki surface standing alone on a line, folded (`wiki_index.mention`, `fold()`, the plural rule of decision 010) | have — `askextract` `MENTIONS`; it depends on the wiki, so it is the one part re-derived when a page is added |
| `references` | chapter numbers (`Kap N`, `Kapitel N`, `Chapter N`), act and part numbers, dates, URLs, cited works | have — `askextract` (chapters, URLs); **new**: dates, acts, cited works |
| `quantities` | numbers with their unit and the noun they count (`39 Kapitel`, `734`, `13 Alters`) | **new** — the `Quantities` contract found nothing on its one document; a rule can find every number, a reader judges which matter |
| `chunks` | retrieval units with spans: **by structure** (a section, or a block group under its heading, never across a heading) and, beside them, HyperExtract's 2048-character chunks (`hx.split`) so a contract's rows map back | have — `hx.split`; **new**: structural chunks |
| `cues` | per contract, the blocks that hold its cue words (`hegraph.gate`) | have — `hegraph.gate`; measured: a cheaper pass is not a better one (graph-contracts §4.6) |
| `proposals` (1b) | per contract run: rows with their placed lines and status (`candidate`, `refused` and why), the model and run that made them — and the run's **outcome**, `found nothing` included: that a contract of the wrong kind returns an empty list is knowledge about the document (and the model: Haiku and Sonnet differ on it) | have — `Plan/runs/<slug>/hyperextract/<run>/` (`he_claude.py`, `reading_extract.stage`); the per-source overview `Plan/runs/<slug>/contracts.{json,md}` and the matrix `Plan/runs/contracts.md` (`contracts.py`); **new**: indexed into the record by run, never merged into it |

Three rules hold for every part, because each of them is how this project once went wrong:

1. **Every fact carries its line**, or a span of lines. A fact without one cannot be checked, and a graph edge built from
   it is indistinguishable from a guessed one (decision 005, `graph.py`'s docstring).
2. **Nothing in the record is a judgement.** It says what stands where; it never says what matters, what a term means or
   which of two readings is right. A model's output is a `proposal`, kept apart, with the run that produced it.
3. **One document, nothing else** — except `mentions`, which reads the wiki's surfaces and says so. The record of
   document A never holds what document B said: that independence is what makes reconciliation safe
   (`Plan/briefings/extract.md`, *two kinds of knowledge*).

### 2.3 How it is built — the plan

1. **Grow `derive.py`, do not replace it.** Each part of §2.2 is a rule in `scripts/rules/`. The ones that exist move
   there from `askextract.py`, `profile.py` and `hegraph.py` (which then read the record instead), so each is computed once.
2. **Two test ingests first.** The two documents of the HyperExtract testbed (§3) are the fixtures: their records are
   written, read by a person, and committed as snapshots under `Plan/runs/he-testbed-2026-10-01/schema/`; a rule's
   self-test holds its output on them. Both have a census and a gold candidate list (decision 009), so a rule that claims
   to find terms is scored against what a reader listed, not argued.
3. **Then the corpus.** `derive.py` over every landed document takes seconds; the proof is a rerun of the retrieval bench with
   `askdb.py build` reading the records instead of the text — the same store, a paired comparison, as every change
   there has been measured.
4. **Then step 4 reads the record.** `askdb.collect` builds `Section`, `Paragraph`, `Line`, `Chapter` and the rest from
   the schema rather than from its own parse.

### 2.4 Update-ingests

`derive.py` already knows what is stale and why (`--stale`). What the record needs beyond it:

| what changed | what re-runs |
|---|---|
| a new document lands | every rule on that document, nothing else; corpus statistics (co-mention, tf-idf in `overview.py`) recount |
| a rule's version | that rule on every document |
| a wiki page is added or renamed | `mentions` on every document (the one part that reads the wiki) |
| a contract (template) changes | nothing automatically: a proposal run costs money and waits on the author's word; the record marks the old run's `template_sha256` as stale |
| a document is corrected upstream | it is a new document (a new `sha256`, a new manifest row); the old one stays, folded by `dedupe.py` |

The second test ingest is therefore an **update**: change one rule, re-derive, and show that exactly that rule's part of
both snapshots changed — the check that the cache is exact.

### 2.5 The master files — a derived, enriched copy of each source

On the author's „lass uns pro Quelldatei eine abgeleitete Datei definieren … eine Master.json, in der die Transformationen
… konfiguriert sind, und eine Master.md — eine angereicherte abgeleitete Datei, die Quelle für zusätzliche Chunks, die das
System selbst erstellt und pflegt". **Proposed; nothing builds it yet.**

Per landed document, two files:

| file | what it is | where | committed? |
|---|---|---|---|
| `<slug>.master.json` | the **configuration**: which transforms run, in which order, at which version, with which parameters; the chunk settings; the measurements that chose them | `Plan/master/` | **yes** — it is a decision, and its history is the system's learning |
| `<slug>.master.md` | the **output**: the source after the transforms, enriched, every line carrying content | `Plan/derived/master/` | no — derived, rebuilt from the source and the json in seconds |
| `<slug>.master.map.json` | the **line map**: for every line of the master, where it came from | `Plan/derived/master/` | no — derived with the master |

**The source never changes, and a citation always names the source.** `Sources/drive/<slug>.md` stays immutable and every
`^[slug.md:Lnn]` keeps naming its line; a master line number is never cited. That is why the line map exists: each master
line is one of

- `src: [a, b]` — source lines a to b, transformed (unescaped, joined, a table row normalised);
- `ins: <transform>` — inserted, with its provenance: a link from `Wiki/index.json` at its version, an annotation from
  `other-slug.md:Lnn`, a heading the structure rule recovered.

So anything built on the master — a chunk, an edge, a retrieval hit — resolves back to source lines, and `quotes.py` keeps
checking against the source.

**The transforms** are rules with the `derive.py` contract (`NAME`, `VERSION`, `applies`, `derive`), each one small, each
switchable per document in the json, applied in order:

| transform | does | care |
|---|---|---|
| `unescape` | undoes the Drive export's backslash escapes, zero-width spaces, glued footnote numbers | `rules/export_damage` and `rules/attribution` already know the patterns |
| `headings` | turns a bold-only line acting as a heading into a heading; numbers `Teil I`, `### A.` into the tree | `Plan/learnings/fetch.md` §7 |
| `compact` | removes empty lines and joins a sentence wrapped over lines, so every line carries content | an empty line is a **paragraph boundary** — `askextract` reads blocks by it; the boundary is kept in the map (`block: n`), not thrown away |
| `tables` | one row per line with its header repeated as a prefix, so a row stands alone in a chunk | a table is never split mid-row |
| `mentions` | marks every wiki surface standing alone as `[[page|surface]]{auto}` | decision 005: **a link is never inferred** — the `{auto}` mark keeps an inserted mention apart from a link a person wrote, and it is re-derived when a page is added |
| `annotations` | adds, as a marked callout after a line, what other sources say about the same term or chapter: `> [!other] other-slug.md:L42 — „…“` | the independence rule: a census is written from the **source**, never from the master, because the master carries other documents' knowledge (`Plan/briefings/extract.md`) |
| `context` | the heading chain as a prefix of each block (`Titel › Teil I › A.`) | the free form of contextual retrieval; a model-written prefix is a separate, paid transform and a proposal |

**The chunks are written from the master, and the system maintains them by measurement, never by taste.** The json holds the
chunk settings (target size, minimum, overlap, which transforms feed them), and every chunk carries its source span through
the map. Self-optimisation is a loop the existing laboratory already runs for relations: a variant of the settings is built,
the retrieval bench scores it against the current one in a paired comparison (`graphlab.py`'s method), and the json records
the winner **with the measurement that chose it** (`chosen_by: {bench, cases, recall, interval}`). A setting nobody measured
is marked `provisional`. This needs a gold set that does not reward the wiki's own wording (`Plan/concept/evaluation-audit_2026-09-30.md`) —
without one the loop optimises towards the bench's bias, so the gold set comes first.

**Update-ingests** fall out of the versions: a transform's version or a document's json changes → that master is rebuilt; a
wiki page is added → `mentions` and `annotations` re-derive on every master; the chunk settings change → only that
document's chunks. The two testbed documents (§3) are the first two masters, and their second build after one transform's
version is bumped is the first update-ingest.

## 3. The HyperExtract testbed — step 1b on two small documents

`Plan/runs/he-testbed-2026-10-01/`: every one of the 32 contracts in `Plan/hyperextract/` on two small documents that
have a census and a gold list — `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik` (4.2 KB, a theory document;
the Haiku pilot ran eleven contracts on it, so Sonnet's rows can be set beside Haiku's) and `2026-09-14-kap25-vertiefung-md`
(10.4 KB, a chapter outline). Sonnet through `claude -p` (decision 011), one run at a time (`run.sh`), every call
recorded. `results.py` writes **one file per contract** in `results/`, with every row of both documents — staged,
refused and why, its quotation and the line code placed it on — so a person can read what a contract does to a document
before deciding which contracts belong in step 1b. `README.md` there has what it cost and what it found.

## 4. What this page does not decide

- whether step 1 runs on every landed document before the author says so — it calls no model, so it may; step 1b calls one,
  so it waits (decision 019, the standing instruction on usage);
- which contracts enter step 1b — the testbed's files are the evidence for that decision, not the decision;
- whether `ask.db` keeps reading raw text beside the record during the change-over — measured, not argued (§2.3, 3).
