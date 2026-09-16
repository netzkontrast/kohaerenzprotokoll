---
description: >-
  Compile a batch of exported Drive sources into candidate wiki pages with
  BatchCompile: triage, cited claims, concepts merged across the whole batch, a
  knowledge diff, and drafts in Wiki/candidates/ that a human promotes later.
  Ingests in chunks by default, carrying each concept's claim history across
  them so contradictions are found whether or not two documents arrived in the
  same chunk. --extract-only runs the cheap half alone.
  Usage: /research-ingest [--slug … | --category … | --tier … | --chunk N]
argument-hint: "[--slug <slug> | --category audit | --tier T3-work] [--chunk N] [--extract-only] [--merge-role auto|task|worker]"
---

# Research ingest — sources become candidates, never pages

Phase B+C of the knowledge system (`Plan/wiki/knowledge-system-concept_2026-09-15.md`
§4). The program is `tools/kpwiki` `BatchCompile` (skill `dspy-wiki-compile`);
this command runs it and files what it drafted. It writes
`Wiki/candidates/<kind-dir>/<partition>/**`, `Wiki/graph/edges.jsonl` and `Wiki/log.md` and nothing
else — `Wiki/sources/`, `Wiki/concepts/` and `Canon/` belong to
`/wiki-promote` and to the author (`Wiki/schema/writers.yaml`).

## Step 1: Pick the batch (deterministic, free)

```bash
python3 scripts/source_inventory.py --check     # the manifest is current
.venv-dspy/bin/python -m tools.kpwiki.research_ingest_cli --category audit
```

The dry run is the default: it prints the selected records, the existing
pages the merge can land on, the glossary terms, and stops before the first
LM call. Records without an export, truncated exports and the tiers the
contract never ingests (`T0-duplicate`, `T1-superseded`, `T4-out-of-scope`)
are dropped with a reason each. `--batch` defaults to the ingest batch size
in `Wiki/schema/conventions.yaml`.

Order of work across batches (concept §4 B): T3 kernkonzept and audits first,
then storyform, characters, worldbuilding, plot; T2 theory last.

## Step 2: Run it (`--write` is the author's flag)

```bash
.venv-dspy/bin/python -m tools.kpwiki.research_ingest_cli --category audit --write \
    --out tools/kpwiki/eval_runs/<date>-<selector>.json
```

**Never set `--write` on your own** — user-facing flags are user-owned
(`writers.yaml → user_flags`). Ask first, with the dry-run output in hand.

### One document at a time, by default

`chunk_size` is **1** (`Wiki/schema/conventions.yaml`). Each document plans,
merges, writes its pages and updates the indexes on its own, so a run resumes
at a document boundary and you read real pages after the first one rather than
the last.

Ingesting one at a time does **not** narrow what gets found. Detection is driven
by concept clusters, not by which documents happened to arrive together: a
concept is reconciled from every claim it has ever been given, so document 40
contradicting document 1 is caught when document 40 lands.

### The wiki is contradiction-free; the ledger remembers

A concept page states what the sources agree on. No contradictory statement is
ever rendered onto it — `Where they disagree` is not a section any more. Where
sources clash, three things happen:

| artifact | role |
|---|---|
| the concept page | keeps the agreed content, flips to `contested`, points at the ledger through `contradiction_ref` |
| `contradictions/concept/<slug>.md` and `contradictions/entity/<slug>.md` | the ledger: every clash ever recorded for that subject, with each position, its source and its citation |
| `questions/incorrectness/<slug>.md` | the worklist: one open question per unresolved clash, routing to `/tetraframe` and a D-xx |

The ledger has two trees because one argument is usually reachable from several
sides: the probe found the alter count disputed under both `die-13-alter` and
`tsdp`, and the Kael–Juna bond under both `juna` and `moonshine-link`. Keyed by
entity as well as concept, those are one subject's history rather than four
unrelated notes.

**Append-only.** `_extractions/_contradictions.json` is the store and the
Markdown ledgers are its rendering, the same way `Graph/` is the record and
`Codex/` its view. A settled clash moves from Open to Resolved with what settled
it; nothing is deleted. That permanence is the point — a document arriving much
later is checked against clashes found long before it, which a list of
currently-open questions could not do.

A ledger is evidence, never a verdict. It records that sources disagree;
deciding which is right is `/tetraframe`, a D-xx, and the author.

**What makes chunking safe.** Naive chunking would merge each concept from the
claims in the chunk at hand, so a document in chunk 5 contradicting one in
chunk 1 would produce two agreeable pages and no disagreement — a wiki that
looks clean because it stopped checking. Two artifacts prevent that:

| artifact | holds |
|---|---|
| `Wiki/candidates/_extractions/<slug>.json` | every claim a source yielded, so a source is read once ever |
| `Wiki/candidates/_extractions/_concepts.json` | `{concept slug: [source:index, …]}` — every claim a concept has ever been given |

Before merging, a concept's claims from this chunk are joined with everything
earlier chunks assigned to it, deduplicated on `(source, index)`. A concept is
therefore always merged from its full history, and `--chunk` changes cost and
resumability, never what gets found.

Chunk 2 also reads chunk 1's candidate drafts when planning, so a concept keeps
one slug across chunks instead of spawning a parallel page.

### Merge routing, and why it is the real lever

`--merge-role auto` (the default) picks the model per concept:

- claims from **more than one source** → the `task` model. A cross-source
  disagreement is possible here, and this is the step that finds it.
- claims from **exactly one source** → the `worker` model. Such a concept
  cannot hold a cross-source contradiction by construction, so the strong model
  buys nothing.

In the pilot that split was 26 against 20: **43% of merge calls were spent
where no contradiction was possible.** `--merge-role task` or `worker` forces
one model everywhere, which is what to use when comparing quality.

### The two halves, and why the split exists

A batch is a cheap per-source half and an expensive batch-wide half:

| half | calls | produces |
|---|---|---|
| triage + extract, **per source** | 2 per source (6 of the pilot's 53) | cited claims, one source page each |
| plan + merge + decide + diff, **batch-wide** | 47 of the pilot's 53 | concepts, agreements, disagreements |

By call count the first half is a tenth; by output tokens closer to a quarter,
because extraction calls are individually the largest (the pilot's three
slowest calls were all extractions). Either way the concept layer is where the
money goes.

`--extract-only` runs the first half alone:

```bash
.venv-dspy/bin/python -m tools.kpwiki.research_ingest_cli --tier T3-work \
    --extract-only --write
```

It writes each source's candidate page and caches its claims as
`Wiki/candidates/_extractions/<slug>.json`. Extraction depends on the document
alone, never on the batch it arrives in, so a cached source is never extracted
twice: re-running resumes rather than restarts, and the concept layer can run
later over the cache without re-reading a single body.

**What a basic ingest does not give you.** Contradiction detection lives
entirely in the merge step. Source pages carry each document's own claims, so
two documents that disagree sit side by side without anything saying so. That
is the point of the concept layer, and deferring it defers that.

A basic ingest fills `Wiki/candidates/sources/` and leaves the concept index
empty; the chunked concept run later picks those cached claims up without
re-reading a body.

Without `ANTHROPIC_API_KEY` the run goes through the `claude` CLI
(`KP_LM_BACKEND=auto`); `KP_LM_CLI_LOG` shows one line per call so a long
batch stays observable. Budget roughly two calls per source plus one
clustering call plus one call per concept.

## Step 3: Read the knowledge diff before anything else

The run prints, in this order: how many sources were extracted and which were
skipped, how many claims and how many of them no concept used, one line per
decision (`create` / `update` / `flag` with its conflicts verbatim), the diff
per existing page (reinforced · challenged · new · gaps), which concepts are
`contradicted` because a disagreement is pending, and every place the model's
triage disagreed with the manifest (the manifest wins; the disagreement is
worth a look). Then the `compile_metric` score with its named deficits.

A `flag` is not a failure. It is the moment the wiki learned that a new source
disputes a page the author already reviewed.

## Step 4: Check what was written

The run lints every page it wrote (required fields, enums, citations resolve,
no `[K]`) and prints the findings. Then, free:

```bash
python3 scripts/render_wiki_views.py          # the views count candidates, so re-render
python3 scripts/wiki_lint.py --health
python3 scripts/render_wiki_views.py --check
```

The rendered views are a different writer (`writers.yaml`), which is why the
ingest does not touch them: run the renderer yourself after a batch, or
`--check` reports `index.md` and `coverage.json` stale.

A candidate with findings is never promoted — fix the draft or re-run that
slug. Candidates older than the age limit in `conventions.yaml` are reported
by the lint; promote or drop them.

## Step 5: Hand over

Present to the author: the knowledge diff, the metric score, the contradicted
concepts and the triage disagreements. Promotion is `/wiki-promote` and a
human decision. On any canon, scope or wording ambiguity: AskUserQuestion
(Rule 0). A merge, supersession or deletion of a reviewed page needs
`/tetraframe` first.
