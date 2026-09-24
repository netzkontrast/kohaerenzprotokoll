---
name: tools
description: The loop that keeps extending the wiki — which command runs when, what each consumes and produces, and how the wiki names its own next document. Use before running any pipeline script, when deciding what to do next, or when a check goes red.
allowed-tools: Bash(python3 scripts/*), Bash(scripts/*), Bash(git:*), Bash(qmd:*)
---

# The loop

The wiki is not built by walking a list of documents. **It is built by a cycle
that names its own next step**, and that is the whole design: a reconciliation
raises a question, the question chooses a document, the document answers or
narrows it, and the reconciliation of *that* raises the next one.

Conflict `C4` named document 5 before anyone else did. That is the loop working.

```
        ┌──────────────── 0 · INVARIANTS ────────────────┐
        │  free, deterministic, no model, run first      │
        └───────────────────────┬────────────────────────┘
                                ▼
   4 · RE-MEASURE ◄───── 1 · CHOOSE ──────► what is open?
   state · order · relations      │         questions/ · conflicts/
   trainset · commit              ▼
        ▲               2 · INGEST one document
        │               capture → read → candidates → count → census → note
        │                          │
        └──── 3 · RECONCILE ◄──────┘
              wiki_index → reconcile → judgements → pages → record
```

**Each phase is a gate, not a suggestion.** Phase 2 refuses to count before a
candidate list exists. Phase 3 refuses to reconcile a document with no census.
Phase 4's `account.py order` refuses to pass while any of it is half-done.

---

## 0 · Invariants — run before anything, and after everything

Seven checks, all free, all deterministic, none uses a model. The value is in
what a red one *means*:

| command | red means |
|---|---|
| `python3 scripts/account.py order` | the pipeline is half-done somewhere — it names the document and the missing step |
| `python3 scripts/state.py --prose` | a number written in prose contradicts the repository. Reads every `.md` outside `Legacy/` |
| `python3 scripts/judgements.py` | **DISAGREES** — the code changed, the record is wrong, or a rule met its first exception. Go and look |
| `python3 scripts/quotes.py` | a quotation no longer resolves to the line it cites. Distinguishes *unresolved* from *uncheckable* and never conflates them |
| `python3 scripts/duplicates.py` | a landed file is a near-copy of another. Should stay 0 after `dedupe.py` |
| `python3 scripts/qmd_coverage.py` | a directory is in no collection, so it is silently unsearchable |
| `python3 scripts/relations.py` | **BROKEN LINKS** — a `[[slug]]` pointing at no page. It also reports orphans and the mentions the markup does not mark |
| `python3 scripts/link.py` | a page the prose connects and the markup does not. **Run it after any reconciliation that created pages** — ten new pages arrive linked to nothing |
| `python3 scripts/sources.py check` | the manifest and the disk disagree, in either direction |
| `python3 scripts/selftest.py` | **a checker stopped reporting what it claims to report.** Every other check on this list is only worth its output if this one passes |

**A green check is worth what its coverage is worth.** Three guards here have
been found reporting green over a gap they could not see: `state.py --prose`
missed 8 of its 49 markers because a number that wrapped to the line above left
its marker matching nothing; `capture.py` dropped every candidate over 40
characters; and the retired pipeline's `coverage()` returned 1.0 whenever it was
passed no gold. Each printed a pass. So when a check reports, **read what it says
it could not check** — `quotes.py` separates *unresolved* from *uncheckable* and
`state.py --prose` now names a marker nothing could read, precisely because
neither number may quietly become the other.

`selftest.py` is the one that guards the others. Each case carries the exact
defect the checker must name — a declension error, a wrong line, a fabricated
sentence, a pair `fold()` must never merge — so a case that fails for the wrong
reason fails the test. Counting reported problems would pass while reporting the
wrong ones, which is how the retired pipeline scored 0.987 on a coverage term
that could not fall.

**A green replay says the recorded decisions still hold, not that the code around
them is right.** `fold()` was correct the whole time `reconcile.py` excluded
exact fold-equality and reported three worlds as six terms.

---

## 1 · Choose — the wiki says what it needs

Not „the next document in the manifest". The open records name it:

```bash
ls Wiki/questions/                                  # what nothing read can answer
ls Wiki/conflicts/                                  # where sources disagree
qmd search "<the question, in German>" -c sources   # which unread document speaks to it
```

A hit here is **a candidate to read, never an answer**. Quoting an unprocessed
document onto a page is exactly what the per-document order exists to prevent —
and reading document 5 showed why: the passage that chose it turned out to be the
opening of a chapter arguing the opposite of what the snippet suggested.

**This step has no command yet.** See „What is missing". Once the entity lists
exist (`NOW.md` says whether they do), `python3 scripts/entities.py doc <slug>`
profiles a candidate before it is read and `missing` names what the corpus uses
widely and the wiki lacks — both counts, both candidates, neither a decision.

---

## 2 · Ingest one document

```bash
python3 scripts/sources.py next --category <cat> --limit 5   # if not landed yet
# → mcp__Google_Drive__read_file_content for each drive_id
python3 scripts/sources.py land --drive-id <id> --consume    # never open the spill

python3 scripts/capture.py <slug>                # 01-profile, 02-probes, opens the run
cat Plan/briefings/extract.md                    # procedural knowledge only, read BEFORE the document
python3 scripts/read.py <slug>                   # the document, every line prefixed NNN|
#   write Plan/runs/<slug>/03-candidates.md AS YOU GO
python3 scripts/capture.py <slug> --count        # 04-counts: two numbers per term, plus surfaces
#   write Sources/terms/<slug>.md   (the census)
#   write Sources/notes/<slug>.md   (the note, every quotation ^[Lnn])
python3 scripts/read.py <slug> --find "<the words>"   # the citation, or a refusal
python3 scripts/quotes.py Sources/notes/<slug>.md
```

**Do not type a citation next to a quote — ask for it.** `--find` answers with
`^[Lnn]` when the words are on one line, and refuses when they are not, naming
the nearest line instead. A citation it produced passes `quotes.py` by
construction: both ask the same question of the same normalised line. The three
quotation defects the checker first found were all of one shape — right line,
right meaning, wrong words — and that shape cannot survive being asked.

Three refusals that are the point of the phase:

- **`--count` will not run without `03-candidates.md`.** Counting first anchors
  the list to whatever a regex proposes, and roughly half of what has been found
  so far is invisible to one.
- **The candidate list is written *while* reading, never reconstructed.** It is
  the one artifact a program cannot produce and the baseline anything automated
  is scored against. Four reconstructed ones exist and are marked unusable.
- **A census describes one document and nothing else** — no count, comparison or
  expectation from another source. That independence is what makes phase 3 safe.

`capture.py --count` reports each term twice, as a word and including compounds,
and lists the inflected surfaces it found. A zero means „written differently
here", not „absent".

---

## 3 · Reconcile against the wiki

```bash
python3 scripts/wiki_index.py                    # derive Wiki/index.json from frontmatter
python3 scripts/reconcile.py <slug>              # pre-classify: lookup vs judgement
#   record each judgement in Plan/runs/judgements.jsonl, with a RULE STATED IN WORDS
#   write pages / readings, then quotes.py on each
#   write Plan/runs/<slug>/reconcile.json  (state_before, state_after)
#   write Wiki/compare/reconcile-NN-<slug>.md
python3 scripts/judgements.py                    # replay; also re-renders judgements.md
```

**Reconciliation never reads the wiki** — it answers by lookup against
`Wiki/index.json`, so cost stays `O(census) + O(judgement)` and not `O(wiki)`.
Never route this through qmd.

**Conflict detection is never mechanised.** Two readings can only be compared by
reading them.

A page may be created from a *reading*, never from an occurrence. Document 5
added zero pages on purpose: sixteen candidates matched nothing and none became
one, because a brief supplies occurrences.

---

## 4 · Re-measure, and commit

```bash
python3 scripts/state.py                         # derive everything, write Plan/state.json
python3 scripts/state.py --prose                 # fail on any stale number anywhere
python3 scripts/account.py order                 # must hold again
python3 scripts/relations.py                     # new orphans, new open statements
python3 scripts/trainset.py                      # did the baseline move?
qmd update && python3 scripts/qmd_coverage.py
```

**The baseline moving is a finding, not an error.** `fold()` went 82% → 65% when
the ledger grew from 17 to 26 examples, and every new miss was a plural or an
inflection — which said the next improvement is a rule, not a model.

Commit per `CLAUDE.md`: one page changed is one commit and the first line names
the source document. The one exception is a corpus-wide re-measurement, which
names the measurement instead.

---

## 5 · The loop closes

The reconciliation of document N raises the questions that choose document N+1.
Document 5 narrowed `Q1`, changed `C4`'s kind and raised `Q4` — three inputs to
the next turn of the cycle.

---

## The commands, as combinations

Nothing below is a new capability. Each is a name for a sequence that is run by
hand today, and **only the ones marked ✓ exist**.

| command | is | status |
|---|---|---|
| `check` | the seven invariants, with what a red one means | **to build** — the scripts exist, the one command does not |
| `next` | open questions + a corpus search → the next document and why | **to build** — phase 1 has no command at all |
| `ingest <slug>` | phase 2, with its three refusals | **to build** — `capture.py` holds two of the three |
| `reconcile <slug>` | phase 3 | ✓ `reconcile.py` does the pre-classification; the rest is by hand |
| `account <subject>` | the recursive verb over `document`, `term`, `pair`, `corpus`, `order` | ✓ `account.py` |
| `ask <question>` | attributed evidence from the wiki, `doc:line` behind every quotation | ✓ retrieval: `graphrag.py ask`. It returns quotations, never prose; `--answer` lets a model pick evidence numbers, needs `--approval` |
| `promote <term>` | a person's review, candidate → `Wiki/terms/` | **to build**, and it is a person's gate, not a command that decides |

**Write no command for a step that has not been done by hand twice.** The
previous version of this project declared nine command names that never existed
as files, ten log operations of which two were ever written, and a contradiction
ledger specified in three places whose directory does not exist.

---

## What is missing, stated plainly

- **Phase 1 is not automated at all.** A person reads the question pages and
  writes the qmd query. This is the step where the loop currently needs a human
  to turn the crank.
- **`ask` retrieves but does not answer.** `graphrag.py ask` returns verified
  quotations from the graph; turning them into prose would merge sources, which
  a page may not do either. Whether an answer ever becomes more than chosen
  quotations is the author's call.
- **`promote` does not exist**, and `Wiki/terms/` therefore does not exist:
  nothing has been promoted, and there is no rule yet for what happens when a new
  source contradicts a page a person signed off.
- **Extraction is not yet trained.** Nine `Plan/runs/<slug>/03-candidates.md`
  carry no reconstruction mark — documents 5 to 13 — and four are reconstructions
  (counted 2026-09-24 by each file's header; this line said „one" until then).
  Only documents 5 and 6 have been scored against, and no extractor tested so far
  reaches the Haiku floor on them (`Plan/concept/tool-review_2026-09-24.md`).

`references/commands.md` has every script's full surface and its artifacts.
For where DSPy could enter this loop and what data that needs first, read
`Plan/concept/optimizers-and-data_2026-09-17.md`.
