# The optimal system — a Sources-first term wiki

**Date:** 2026-09-16
**Status:** plan for author review; nothing executed
**Scope:** the wiki only. The novel rests.
**Supersedes in intent:** the five-layer model in `CLAUDE.md`

---

## 0. The decisions this plan implements

Taken by the author, 2026-09-16:

1. **Full reset.** `Canon/` is deleted. `Sources/` becomes the only source of truth.
2. **`Manuscript/` is emptied.** The novel is out of scope for now.
3. **Export all 680 Drive documents**, with the cheap export separated from the
   expensive LLM ingest.
4. **Rebuild the wiki machinery from scratch.** The existing schema is not carried over.
5. **Everything not needed moves to a top-level folder**, not deleted.
6. **Every workflow must be provably exercised**, and the models serving it measured.
7. **Focus is the wiki.** Nothing else competes for attention.

Recoverable throughout: `backup/pre-restart-2026-09-16` on `origin` holds the
whole tree at `608cbb5`.

---

## 1. Why the reset is correct, in numbers

Not opinion — measured in the anatomy read
(`Plan/concept/repo-and-workflow-concept_2026-09-16.md`):

| symptom | measurement |
|---|---|
| the research layer never ran | **26 of 680** documents exported; 654 have no `export_path` at all |
| the wiki never filled | 56 candidates, **2** promoted pages |
| its routing was empty | `Wiki/context-map.md` renders `_no routable pages yet_` |
| instruction without payload | ~3,400 tokens per session routing to that empty layer |
| rules restated instead of run | R-rules in **four** places; 4 of 10 have no executable encoding |
| workflows that cannot run | `lit_critic_gate.py` exit 2; `.venv-dspy` absent; `/kp-decide` never written |
| commands referenced but absent | **seven** |
| broken links inside `.claude/` | 25 of 92 |

One sentence: **the system was described far more than it was exercised.** The
export that everything depended on covered 3.8 % of its input, and no gate
anywhere reported that, because no gate looked.

That is the failure this plan is designed against.

---

## 2. Design principles

**P1 — Two layers, not five.** `Sources/` (immutable, fetched) → `Wiki/`
(derived, human-promoted). Nothing else exists while the wiki is being built.
Every layer beyond two was a place for the same fact to be stated differently.

**P2 — The manifest is the spine.** `Sources/manifest.jsonl` already carries
what a provenance system needs, for all 680 documents: `drive_id`, `title`,
`slug`, `category`, `tier`, `export_path`, `sha256`, `index_date`. Everything
derived traces to a `drive_id`. No second registry is built.

**P3 — Cheap and expensive are separated.** Fetching is deterministic, free and
complete. Compiling is LLM work, costly and selective. They never run in one
step, so a budget decision never blocks a completeness decision.

**P4 — Every workflow carries its own proof.** A workflow that cannot be run
offline against a fixture does not ship. This is the direct corrective to §1: the
old surface could not be exercised, so it drifted silently for months.

**P5 — Model choice is measured, never assumed.** Every LLM stage declares a
fixture and a metric, and the model serving it is chosen from a benchmark table.
Per stage, not globally — a model good at extraction can be bad at merging.

**P6 — Rule 1 survives.** Anything decidable is a program; everything else is
named as judgement. Nothing in between.

**P7 — Rule 0 survives.** Promotion is a human act. A program proposes; the
author decides.

---

## 3. The page unit — decided

The author left this to the plan. **One term = one page, and the page holds the
per-source readings rather than a merged definition.**

The reasoning is the author's own phrasing: *"welche Begriffe wie wo was
bedeuten — entscheidet die Research Source."* That is not a request for a
glossary. It is a request to know **which source says what about a term** — so
merging readings into one definition would destroy exactly the information
wanted. The page is therefore a *dossier*, not an entry.

```
Wiki/terms/<slug>.md
---
term: Coheron
aliases: [Coheron-Spur, Kohäron]
status: draft | reviewed
sources: [<drive_id>, …]        # every source that says something
readings: 3                     # distinct meanings found
conflict: true | false          # two readings that cannot both hold
---

## Readings
### [S012] „DKT-Fundament", 2025-11-03, tier T2-theory
<what this source says, quoted or closely paraphrased>  ^[Sources/drive/<slug>.md:120-134]

### [S044] „Architecture Synthesis 2", 2026-02-18, tier T3-work
<what this source says>  ^[…:88-91]

## Conflict
S012 and S044 cannot both hold, because …      ← stated, never resolved

## Open
<what no source answers>
```

**What is deliberately not a page type**, on evidence rather than taste:

- **No source pages.** The manifest already indexes every document, and the
  document itself is on disk. A source summary page is a second encoding of a
  file that is right there — and it is what produced 56 unread candidates.
- **No contradiction pages.** The old schema declared a `contradiction` entity
  with 8 required fields, its own status enum, 5 prose rules and a 62-line
  template. It has **zero instances**. A conflict is a property of a term, on
  the term's page, where anyone looking up the term will see it.
- **No synthesis or question pages yet.** Both were near-unused. They earn
  their existence when a real need appears, not before.

**One entity type.** That is the whole schema. It can grow on evidence; it
starts at one because the five-type schema produced two pages.

---

## 4. The pipeline

Four stages. Each declares inputs, outputs, its check, and its fixture.

```
Drive ──fetch──→ Sources/drive/*.md ──extract──→ terms + citations
                       │                              │
                  manifest.jsonl                   compile
                   (the spine)                        │
                                              Wiki/candidates/
                                                      │
                                                  promote (human)
                                                      │
                                                 Wiki/terms/
```

### Stage 1 — `fetch` · deterministic, free, complete

Reads the manifest, pulls every document with no `export_path` through the Drive
connector, writes `Sources/drive/<slug>.md`, fills `export_path`, `sha256`,
`exported_at`. Idempotent: a document with a matching checksum is skipped.

- **check:** every manifest row has a file whose `sha256` matches. This is the
  gate that was missing — §1's headline defect was invisible precisely because
  nothing compared the manifest against the disk.
- **fixture:** a three-row manifest against a local directory; no network.
- **cost:** no LLM. Runtime only.

### Stage 2 — `extract` · one LLM call per document, cheap model

Per document: the terms it defines or uses, each with the exact line range that
supports it. No judgement, no merging — a mechanical harvest.

- **output:** `Sources/_extractions/<slug>.json`, one file per source, cacheable
  and re-runnable.
- **check:** every citation resolves — file exists, line range exists, the quoted
  text is inside it. Deterministic, and it is the check the pilot run showed
  matters most (its most-broken rule was a paraphrase presented as a quotation).
- **fixture:** one source with known terms and known line numbers.

### Stage 3 — `compile` · the expensive stage, strong model

Groups extractions by term across all sources, writes one candidate page per
term carrying every reading, and flags where two readings cannot both hold.

- **output:** `Wiki/candidates/<slug>.md`
- **check:** every reading cites a source; no reading is invented; a page with
  `conflict: true` names both sides.
- **judgement it must never take:** whether a conflict matters, and which side
  is right. It states both and stops.
- **fixture:** two sources that disagree about one term on purpose, so the
  conflict detector is proven to fire rather than assumed to.

### Stage 4 — `promote` · human

Moves a reviewed candidate to `Wiki/terms/`. The review is the point; the
command performs the move.

---

## 5. The check suite

Four buckets, adopted from the audit-ledger idea and mapped onto this wiki.
Three of four are decidable, which is what makes them worth building:

| bucket | decidable? | what it asks |
|---|---|---|
| `FOUND` | **yes** | does every citation resolve to real lines containing the quoted text? |
| `CONFLICTING` | **yes** | do two readings of one term assert incompatible values? |
| `MISSING` | **yes** | is a term used across sources with no page, or a page with no reading? |
| `INFERRED` | **no** | is a synthesis across sources sound? — surfaced, never settled |

`MISSING` is the one the old system could not express. `CLAUDE.md` states the
gap in its own words — *"a lint proves a forbidden word is absent; it can never
show that something required is missing"* — and then leaves it open. Over a term
wiki it is straightforwardly computable: terms that appear in extractions but
have no page, pages with no reading, sources no page cites.

---

## 6. Proving the workflows — P4 and P5 made concrete

This is the part the old system lacked entirely, and the author has made it a
requirement.

**Every stage ships with a fixture** that runs offline, free, with no API key,
exactly as `tools/kpwiki/smoke.py` does today — the one piece of the old
machinery that genuinely worked. One command runs all of them, and a stage whose
fixture fails is not usable.

**Every LLM stage declares a metric**, so quality is a number rather than an
impression, and the same metric serves the benchmark and the live run. One
encoding, per Rule 1.

**Model choice comes from a table, per stage.** `scripts/lm_bench.py` already
does this for one program; it generalizes to a stage argument. Candidates are
run against each stage's fixture and scored by that stage's metric, so the output
is an assignment, not a ranking:

| stage | shape of the work | what the benchmark decides |
|---|---|---|
| `extract` | mechanical, high volume, strict citations | the cheapest model that never fabricates a line number |
| `compile` | cross-source reasoning, conflict detection | the cheapest model that still *finds* the planted conflict |

**On the free models specifically**, three findings from today's sweep already
constrain the answer, and the fixtures must keep testing for them:

- Five models held a typed schema on every attempt; **two were free**
  (`nex-n2.5-pro:free`, `dots-3-note-preview:free`, both scoring 1.00).
- A reasoning model burned an entire 400-token budget on chain of thought and
  returned **empty content with no error**. The same model was correct at 4096.
  So every stage fixture must assert non-empty output, not merely absence of an
  exception.
- The free router returned correct German claims while its summary came back in
  **English**. Since the corpus is German, **language of output belongs in every
  metric**, not only content correctness.

Those three are why P5 says *per stage*: the sweep measured one program at one
token ceiling, and two of the three failure modes were invisible to it.

---

## 7. Rule 1 sorting

| lives in | what goes there |
|---|---|
| **tool** (`scripts/`, `tools/`) | fetch, checksum verification, citation resolution, conflict detection, the MISSING computation, the benchmark |
| **schema** (one YAML) | the term page's fields, the tiers, the categories, the page budget |
| **skill / command** | when to reach for a stage, how to read its output, what judgement is left |
| **reference** | why a rule exists and what it deliberately cannot see |

**Named as judgement, not faked into a script:** whether a conflict matters,
which reading is right, whether a synthesis holds, and every promotion.

---

## 8. Layout after the move

```
Sources/            manifest.jsonl + drive/*.md + _extractions/    ← the only truth
Wiki/               terms/ + candidates/ + one schema YAML
scripts/ tools/     the four stages, the checks, the benchmark
Plan/               rebuilt: decisions/ and concept/ only
Attic/              everything else, moved not deleted
  ├── Canon/            8 documents, 51,967 words
  ├── Graph/            1,180 records
  ├── Codex/            644 rendered files
  ├── Manuscript/       41 chapters, 97,361 words
  ├── Plan-2026-09/     the old planning record
  └── claude-2026-09/   the retired commands, skills, agents, hooks
```

`Attic/` is readable and citable and read by nothing. That matters more than it
sounds: §1's losses were invisible because tools do not read git history, and an
archived directory is the only form of "kept" that an agent can actually consult.

---

## 9. Sequence

Each phase ends in something demonstrable, and none starts before the one
before it is proven.

| # | phase | ends when | cost |
|---|---|---|---|
| 1 | **Move to `Attic/`**, rebuild `Plan/`, rewrite `CLAUDE.md` to the two-layer model | the tree is the §8 layout and `CLAUDE.md` describes what exists | none |
| 2 | **Build `fetch` + its check + its fixture** | the manifest/disk gate runs and reports 26 of 680 | none |
| 3 | **Run `fetch` for all 680** | every manifest row has a file and a matching checksum | runtime only |
| 4 | **Build `extract` + `compile`, their fixtures and metrics** | all fixtures pass offline with no key | none |
| 5 | **Benchmark candidates per stage** | an assignment table exists, free models included | small |
| 6 | **Extract all, compile a pilot slice** | candidate term pages exist for one category | measured in 5 |
| 7 | **Review and promote** | the first real `Wiki/terms/` pages exist | author time |

Phase 1 is the one with a deadline in it: `CLAUDE.md` must stop describing five
layers before anything is built against it, or the new system inherits the old
system's central defect — a description that outruns what exists.

---

## 10. Costs

**Export (phase 3)** costs no LLM tokens. Wall clock only.

**Ingest** is the expensive half, and the old pilot is the only real datum:
3 sources, 53 LM calls, 54 minutes, **$8.38** — about **$2.79 per document** on
Opus. Naively, 680 documents ≈ **$1,900 and 8.5 days**.

Three levers make that number soft rather than fixed, which is why phase 5 comes
before phase 6:

- **`extract` is the volume stage** and needs the cheapest model that cites
  correctly — this is where the free models earn their place.
- **The pilot measured a documented 43 % waste**: 20 of 46 merge calls went to
  the strong model where no cross-source contradiction was possible.
- **`T0-duplicate` documents (2) need no ingest at all**, and `tier` lets the
  compile stage be run per slice rather than all at once.

A realistic plan is therefore: benchmark first, extract everything on a cheap
model, and compile selectively by category.

---

## 11. What is deliberately not in this plan

The novel. `Graph/`, `Codex/`, the storyform machinery, the R-rules, the prose
gates and the drafting commands all go to `Attic/` intact. They are not wrong —
`Graph/` in particular is the healthiest artefact in the repository — but they
are downstream of knowledge that does not exist yet, and trying to hold them
open while the wiki is built is exactly the "everything at once" the author named
as the problem.

They come back when there is a wiki to build them from, and they come back as a
decision, not by default.

---

## 12. What the author still decides

1. **`CLAUDE.md`** — I propose rewriting it to the two-layer model in phase 1.
   It is the file every session loads, and it currently describes a system that
   will not exist.
2. **Drive access at scale** — 654 fetches through the connector. Whether that
   runs in one pass or in category batches is an operational call.
3. **The `Attic/` name.** `Legacy/` and `Archive/` are equally good; the name
   appears in every future path, so it is worth choosing once.
4. **Where the ingest budget stops.** Phase 5 produces the number; phase 6 spends
   it. `tier` and `category` are the available dials.
5. **The term-page shape in §3** — the field list is a proposal, and it is
   cheaper to change now than after 680 documents are compiled against it.
