---
name: ingest
description: Take one research document from Sources/drive/ all the way to a reconciled state a person can review — profile, candidate list written while reading, counts, census, note, reconciliation, judgements. Use this whenever a document is being read, extracted, censused, noted, reconciled or "ingested", when a new source has just landed from Drive, when an open question or conflict has named the next document to read, or when asked to add a document to the wiki. Also use it when only part of that arc is wanted — the gates and refusals it carries are what make the part safe.
allowed-tools: Bash(python3 scripts/*), Bash(scripts/*), Bash(git:*), Bash(qmd:*)
---

# Ingest one document

One document, from the file on disk to a reconciliation `account.py order`
accepts. It wraps scripts that already exist and adds the things a script cannot
enforce: the order, the refusals, and what stays a person's call.

**The whole arc, and where each gate sits:**

```
capture ──► read the briefing ──► READ with line numbers ──► 03-candidates.md
                                                                   │
                        ┌──────── --count refuses without it ◄──────┘
                        ▼
                     counts ──► census ──► note ──► quotes.py
                                                       │
                     reconcile.py ◄── wiki_index.py ◄───┘
                        │
                        ├── decided by lookup → nothing to do
                        └── to judgement → a rule stated in words → ledger
                                                       │
                     pages / readings ──► reconcile.json ──► Wiki/compare/
```

## The one finding that shapes all of it

The pipeline this replaces scored its own runs **0.987** and **0.967** across 53
LM calls. One of its five axes was `coverage`, and it returned `1.0` whenever no
gold fragments were passed — and the caller passed none. **The recall term was
pinned and the score could not fall for missing anything.** Both runs measured
whether the output was well-formed, cited and still in German. Neither measured
whether it found what a person would have found.

So the rule this skill is built around: **every run produces a gold artifact or
it produces nothing.** `03-candidates.md`, written while reading, before any
count. It is the only artifact of a run a program cannot produce, and the only
thing anything automated can ever be scored against. `capture.py --count` already
refuses without it. Do not weaken that refusal, and do not reconstruct the list
afterwards — four reconstructed lists exist, are marked as reconstructions, and
`trainset.py` refuses them.

**And a gold list is one reading, not the truth.** Two independent readings of
one document, neither seeing the other, produced **131 and 113 candidates with 80
shared** — F1 **0.66** against each other; a second pair gave 109 against 143,
and one of the two raised a conflict the other never saw. So „the model scored
0.7" means nothing on its own: **0.66 is the human ceiling**, and a score clearly
above it is most likely fitted to one reader. When you compare lists, print both
difference lists by name — a miss is not automatically an error and an invention
is not automatically wrong.

## 1 · Open the run

```bash
python3 scripts/capture.py <slug>                 # 01-profile.txt, 02-probes.txt
python3 scripts/profile.py --frontmatter <slug>   # the census header, from the manifest
```

Read `01-profile.txt` **before forming any impression of the document.** Headings,
tables, invisible characters, repeated labels and escapes change the shape of the
extraction — a document with 39 repeated field labels is read differently from
one with two headings, and noticing that afterwards is noticing it too late.

**Never type a `drive_id`, title or date.** `--frontmatter` draws them from the
manifest. One was fabricated once, and a wrong identifier looks exactly like a
right one.

## 2 · Read the briefing, then the document

```bash
cat Plan/briefings/extract.md
```

That file carries **procedural** knowledge — what German Drive exports do, what
questions to hold while reading — and never **document** knowledge, no slug, no
count, no term from another source. That distinction is what makes it safe to
read first: document knowledge would decide in advance what this document is
allowed to say, which is the failure the census exists to prevent.

```bash
python3 scripts/read.py <slug>                    # every line prefixed NNN|
python3 scripts/read.py <slug> --from 200 --to 320
```

The numbers are **file** lines, which is what a citation names. Extraction starts
after the frontmatter; citations count from line 1. Two line bases over one file,
on purpose.

**Write every candidate into `Plan/runs/<slug>/03-candidates.md` as you read**,
one `- term` per line. A prose section for open observations is fine and is
filtered out — only `- term` lines are read as candidates.

Counting first anchors the list to whatever a regex proposes, and **roughly half
of what has been found so far is invisible to one**: German capitalises every
noun, so grepping for capitalised words finds sentence starts and misses inflected
forms. See `references/german.md` before trusting any pattern.

## 3 · Count, then write the census

```bash
python3 scripts/capture.py <slug> --count         # 04-counts.txt, counts.json
```

Each term is reported **twice** — standing alone, and including compounds —
because one number cannot answer it in German, and the inflected surfaces found
are listed. **A term at `0 word` is written differently here, not absent.**

The census goes to `Sources/terms/<slug>.md`. **It describes one document and
nothing else**: no count, comparison or expectation from another source appears
in it. That independence is what makes the next step safe — if the accumulated
wiki could reach into extraction, it would decide in advance what a new document
may say.

## 4 · Write the note

`Sources/notes/<slug>.md` harvests what this document *says* about the terms that
matter. It quotes, and every quotation carries its line.

```bash
python3 scripts/read.py <slug> --find "<the words you want to quote>"
python3 scripts/quotes.py Sources/notes/<slug>.md
```

**Ask for the citation rather than typing it next to the quote.** `--find`
answers with `^[Lnn]`, or refuses and names the nearest line. Both it and
`quotes.py` run the same comparison over the same normalised line, so a citation
`--find` produced cannot fail the check. The defects this prevents are the ones
that look right: a correct line, a correct meaning, and **words the document
never contained** — a nominative written for a genitive, „das Management" for
„dem Management".

**And qualify every citation on a page that will carry a second document.** A
bare `^[Lnn]` resolves against the page's single `ingested:` entry, so the moment
a page gains a second one `quotes.py` stops checking it — correctly, since it
refuses to guess which document is meant. Adding one document's readings moved
**95 verified quotations into the unchecked bucket with nothing going red**,
because an unchecked quote is not a failure. Write `^[slug.md:Lnn]` on any page
you add a second source to, and compare the *checked* count before and after, not
only the failures.

Five rules govern a quotation here, four of them inherited and one checked:

- no citation → the claim is dropped, not kept unsourced
- quote verbatim from the numbered lines
- **never translate a source** — canon prose is German and stays German
- any term the claim itself puts in quotation marks must stand verbatim in the
  cited line
- do not merge two statements into one claim

## 5 · Reconcile against the wiki

```bash
python3 scripts/wiki_index.py                     # derive Wiki/index.json
python3 scripts/reconcile.py <slug>               # pre-classify: lookup vs judgement
```

**Reconciliation never reads the wiki.** It answers by lookup against
`Wiki/index.json`, so cost per document is `O(census) + O(judgement)` and not
`O(wiki)`. Never route this through qmd, and never let it grow into a comparison
against every earlier document — the first three comparisons were exactly that
and each superseded the last.

What the lookup settles is settled. What it hands to judgement is a person's
call, and each one is recorded in `Plan/runs/judgements.jsonl` **with a rule
stated in words** — not „these are the same" but „a German definite article is
never a term boundary". A rule in words is what can later be mechanised and then
replayed:

```bash
python3 scripts/judgements.py                     # replay; re-renders judgements.md
```

`DISAGREES` means go and look. And note what a green replay cannot see: `fold()`
was right the whole time its *caller* excluded exact fold-equality and reported
three worlds as six new terms. **A green replay says the recorded decisions still
hold, not that the code around them is right.**

## 6 · Record what the run left

```bash
python3 scripts/link.py --apply                   # a new page arrives linked to nothing
```

Ten pages from one reconciliation arrived as ten orphans, and the graph said the
wiki had grown *less* connected by growing. `link.py` marks only terms the prose
already wrote and never touches a line carrying a `^[` citation — run `quotes.py`
after it anyway, because the first such pass put a link inside two quotations and
that is how it was found.

**Then read every open conflict and question against the document, not only the
ones its readings reached.** Reconciliation walks from the census to the pages,
so a record is reached only through a page a new reading touched. Document 9
restated the subjects of C1, C2, C3, Q1, Q3 and Q4 without a new surface, and the
first pass reached none of them; collecting the author's questions found all six.
The list is short — `ls Wiki/conflicts Wiki/questions` — and each record's
subject line is enough to ask whether the document speaks to it.

Write `Plan/runs/<slug>/reconcile.json` with `state_before` and `state_after`, and
`Wiki/compare/reconcile-NN-<slug>.md` as the prose record. `references/artifacts.md`
has the exact fields. Then:

```bash
python3 scripts/account.py order                  # must hold
python3 scripts/state.py --prose                  # no number in prose may drift
python3 scripts/quotes.py
```

`account.py order` is what catches a half-done ingest: it checks that every
document with a census has a note and a reconciliation, that each ran against the
state the previous one left, and that the wiki matches what the newest run
recorded leaving.

Commit as you go. A page in `Wiki/` is one commit per page and **the first line
names the source document** — `guardians: five named bearers from
guardians-und-kern-welten-konzept`. Without that, `git log` says a page changed
and not why, and finding which source added a claim means reading every version.

## What this skill may not do

These are not style preferences. Each is a failure that has already happened
here or in the pipeline this replaces.

**Never create a page from an occurrence.** A term page collects a source's
*reading* of a term. A document that uses a word in a proposal it is itself
questioning supplies an occurrence. Document 5 raised sixteen such candidates and
**added zero pages on purpose** — that was the correct outcome, recorded with the
lines so the next document that actually defines one opens its page with a
reading attached. A page created from an occurrence says nothing and looks like
it says something.

**Never resolve a conflict.** An ingest proposes; it never resolves. The
predecessor honoured a document's own `[DEPRECATED]` claim — letting a source
grant itself authority — and its metric counted „contradicted" from *pending*
disagreements only, so such a page dropped out of the review queue silently. Two
defects lined up and nothing was visible. Where sources disagree, the page says
so and stops; which reading is right is the author's call.

**Never mechanise conflict detection.** Two readings can only be compared by
reading them. A program that guessed would reproduce the `Zero-Trust` false
conflict.

**Never let a number come from a search result.** qmd ranks; it does not
enumerate. `Kernwelt` is in 144 landed documents and a forty-hit list is not a
census of that — measured, the line defining `KW1` is not in the top forty,
because BM25 favours short, early chunks. Every number in a page or a learning
comes from `corpus.py`, `duplicates.py` or a count that says what it counted.

**Never accept a candidate a model did not cite.** The first `dspy.RLM` run ran
out of REPL budget before finishing the document and its reasoning says it would
„reconstruct from outputs" — assembling the text from its own truncated
scrollback and handing that over as a reading. It only failed to land because the
answer would not parse. From a model a reconstruction is **invisible**: the list
looks the same. So each candidate comes back as `- term ^[Lnn]` and every line is
checked against the document; unverified and uncited candidates are reported, not
dropped, and a mostly-unverified list names itself in `written_by:`. An
incomplete reading is a fact and usable. A complete-looking reconstruction is
neither.

**Never write `03-candidates.md` from a model.** A model's list goes to
`03-candidates-rlm.md` and states `written_by:`, which `state.py` reads. The gold
list and the thing gold scores must not be able to become each other, and the
prose is not enough to tell them apart: „does the head contain 'reconstruct'"
once passed a model's list and failed a list whose prose *denied* being a
reconstruction.

**Never grade your own candidate list.** Extraction's independence is what makes
reconciliation safe, and a self-scored recall term is that same defect moved one
step along. If a model produced the list, say so in the run; it is not gold.

**Never describe a step that does not exist.** The predecessor declared a section
abolished that 41 pages still carry, specified a `Wiki/contradictions/` ledger no
code ever wrote, and referenced nine command names that were not files — one of
them in the machine-readable policy. If a rule here can be broken without a check
failing, it is a convention a person upholds, and it says so rather than
pretending to be enforced.

## Where qmd belongs

Orientation only, and only `search` — 0.22s against 2m41s for `query`, measured
on this corpus after embeddings completed. It finds a document worth reading. It
decides nothing, it never becomes a number, and it is never called inside a loop
or inside reconciliation. `.claude/skills/qmd` has the collections.

## References

- `references/german.md` — the German findings that defeat naive matching:
  capitalisation, inflection, umlaut slugs, typographic normalisation, and the
  substring trap that has now appeared four times.
- `references/artifacts.md` — the exact shape of every file a run writes, and
  which of them `account.py order` reads.

## Provisional

```yaml
name: ingest            # provisional
# may not: create a wiki page from an occurrence, resolve a conflict,
#          grade its own candidate list, or let a number come from a search
# retire when: three documents run through it with no correction needed
```
