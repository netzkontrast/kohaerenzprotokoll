# The wiki process, and how we track work

**Date:** 2026-09-16
**Scope:** the wiki only, built entirely from the Source documents
**Posture:** easy and flexible — by hand first, automated only where the shape is proven

---

## The one rule about the archive

Everything the reset parks — the novel, the graph, the codex, the old planning
record, the retired commands — moves to a single top-level folder and then
**disappears from the working system**.

Concretely, and these are checkable:

- No wiki page links to it.
- No script scans it. Every tool takes the working root, and the archive is not
  under it.
- `CLAUDE.md` does not describe it. A session that reads `CLAUDE.md` learns the
  wiki and nothing else.
- Exactly **one** pointer to it exists, in `README.md`, in one sentence: what it
  holds and which commit it came from.

It is a shelf, not a layer. If it starts getting referenced, it has become a
layer again, and that is the thing we are removing.

---

## Why by hand first

The old system had five page types, twenty-six lint rules, three DSPy programs,
a schema across five YAML files — and produced **two pages**. The machine was
built before anyone knew what a page needed to contain.

So the order here is inverted on purpose:

> **Write about twenty term pages by hand. Then look at what they actually
> contain, and automate that.**

A schema written after twenty real pages describes something. A schema written
before them describes a guess, and every later page pays for the guess.

This is also what keeps the project flexible: nothing built by hand is expensive
to throw away.

---

## The wiki in one picture

```
Drive (680 docs)
   │  fetch — deterministic, free, complete
   ▼
Sources/drive/*.md  +  manifest.jsonl          ← the only truth
   │  read — what terms does this document define or use?
   ▼
Sources/notes/*.md                              ← one note per source
   │  gather — every reading of one term, across all sources
   ▼
Wiki/candidates/*.md
   │  review — a person decides
   ▼
Wiki/terms/*.md                                 ← the wiki
   │
   └── ask — the reason the whole thing exists
```

Five steps. Two of them are a person. Three can eventually be programs, and none
of them has to be one today.

---

## Step 1 — Fetch

**In:** manifest rows with no `export_path` (654 of 680 today)
**Out:** `Sources/drive/<slug>.md`, and the row filled in with `export_path`,
`sha256`, `exported_at`
**Who:** a script through the Drive connector
**Costs:** no LLM tokens. Runtime only.

Idempotent — a document whose checksum already matches is skipped, so the fetch
can be re-run, interrupted, and resumed without thought.

**The check that was missing and matters most:** compare the manifest against the
disk and report any row without a file. That single comparison is what nobody
had; it is why "26 of 680" went unnoticed long enough to become the shape of the
project.

This is the one step worth scripting immediately, because it is pure mechanics
and there are 654 of them.

---

## Step 2 — Read a source

**In:** one source document
**Out:** `Sources/notes/<slug>.md` — the terms it defines or uses, each with the
exact lines that support it
**Who:** Claude, reading the file. **By hand at first.**

A note is deliberately dumb. It harvests, it does not think:

```markdown
# Notes on: "DKT-Fundament Kohärenz Protokoll"
source: Sources/drive/dkt-fundament-kohaerenz-protokoll-md.md
drive_id: 1abc…
tier: T2-theory · category: theorie-physik

## Terms
- **Coheron** — „<exact quote>" ^[L120-134]
- **K₀ / K₁** — „<exact quote>" ^[L88-91]
- **Atemporalität** — „<exact quote>" ^[L140-152]

## Uses without defining
- Kernwelt, AEGIS, Multiplizitäts-Schleier

## Says nothing about
- <anything expected here and absent>
```

Two things make this cheap and safe. It is **one document at a time**, so it
never needs the whole corpus in context. And it **quotes rather than
paraphrases**, so the next step has something to stand on. The old pilot's
single most-broken rule was a paraphrase presented as a quotation — quoting is
the fix, and it costs nothing.

*Later, when the shape is stable:* one cheap LLM call per document. There are
680 of them, so this is the volume stage and the one where a cheap model pays.

---

## Step 3 — Gather a term

**In:** every note that mentions term X
**Out:** `Wiki/candidates/<term>.md`
**Who:** Claude. **By hand at first.**

The page holds **one reading per source**, not a merged definition:

```markdown
# Coheron

## Readings

### DKT-Fundament · T2-theory · 2025-11
<what this source says>  ^[Sources/drive/dkt-fundament…md:120-134]

### Architecture Synthesis 2 · T3-work · 2026-02
<what this source says>  ^[Sources/drive/…-synthesis-2.md:88-91]

## Where they disagree
The first makes it a particle; the second makes it a trace.
Both cannot hold. — *named, not resolved*

## Open
No source says what happens at the boundary.
```

**The rule that gives the wiki its value:** never merge readings into one
definition. The question being answered is *which source says what* — merging
deletes exactly that. Where sources agree, the readings will simply look alike,
and that is itself the finding.

**And a rule about judgement:** the page names a disagreement and stops. Which
side is right is the author's call, never the page's.

---

## Step 4 — Review and promote

**In:** a candidate page
**Out:** `Wiki/terms/<term>.md`
**Who:** the author. This step is a person by definition.

The review asks four things, and they are quick because the page is short:

1. Does every reading actually say what the page claims?
2. Does every citation point at real lines?
3. Is the disagreement real, or an artefact of different wording?
4. Is anything important missing?

Promotion is a move plus a status flip. Nothing else happens automatically —
research becomes knowledge because a person said so.

---

## Step 5 — Ask

The wiki exists to be asked. A question is answered from the term pages, with
the file and line each claim came from, and never from memory.

Today that is `grep` plus reading the pages, and for a few hundred pages that is
genuinely enough. A search index is worth building when grep stops being
pleasant — not before.

If an answer cannot be given from the pages, that is a finding, not a failure:
it names a term that needs a page or a source that needs fetching.

---

## Keeping it honest

Four questions. Three are decidable and become small scripts as soon as they
have something to run against; the fourth never becomes one.

| | question | decidable |
|---|---|---|
| **FOUND** | does every citation resolve to real lines containing the quoted text? | yes |
| **CONFLICTING** | do two readings of one term assert incompatible things? | yes — flagged by a person at first, then by a check |
| **MISSING** | which terms appear in notes but have no page? which pages have no reading? which sources has nothing read yet? | yes |
| **INFERRED** | is a synthesis across sources sound? | **no** — surfaced, never settled |

`MISSING` is the one the old system could not express, and the one that would
have caught "26 of 680". It is the cheapest to compute and the most valuable, so
it comes first.

---

## What is automated, and when

| step | today | becomes a script when |
|---|---|---|
| fetch | **script now** | immediately — 654 mechanical operations |
| manifest/disk check | **script now** | immediately — it is ten lines and it is the missed defect |
| read a source | by hand | the note format has stopped changing |
| gather a term | by hand | ~20 pages exist and the page shape has settled |
| MISSING check | by hand | notes and pages exist to compute it from |
| review | **never** | it is the human act |
| ask | grep | grep stops being pleasant |

Nothing on this list is urgent except the first two. Everything else earns
automation by being done a few times first.

---

## Task management

The old `todo.md` grew to 351 lines and ~3,000 tokens, was read at the start of
every session by instruction, and mixed live work with rescued ideas and
archaeology. It became a cost paid every session for information that was mostly
history.

Three places instead, each with one job:

**`NOW.md` — what is open, right now.** One page, hard limit. It holds only
current work: what is being done, what is next, what is blocked and on what.
When something finishes it comes **out** — git remembers, and the file is for
deciding what to do next, not for recording what was done. If it does not fit on
a page, the project has too much open at once, and that is the signal, not a
formatting problem.

**`Plan/decisions/` — what was decided, and why.** One short numbered file per
decision, permanent. A decision record is the only thing here worth keeping
forever, because it is the thing nobody can reconstruct later: *what we chose,
what we rejected, and what would change our mind.* Everything else can be
re-derived from the sources.

**Git — everything that happened.** Finished work, old plans, superseded
structure. It is already a complete record and needs no second copy.

Plus, inside a working session: the ephemeral task list the agent keeps while
executing. It vanishes with the session, which is correct — it is scaffolding,
not a record.

**What this deliberately drops:** no status fields, no priorities, no estimates,
no board. With one person and one agent, the overhead of tracking work exceeds
the cost of just doing it. If several things genuinely run in parallel later,
GitHub issues are there and cost nothing until used.

---

## What we are deliberately not deciding yet

Named here so the gaps are visible rather than implied:

- **The term page's exact fields.** Twenty hand-written pages decide it. Fixing
  it now would be a guess, and a guess in a schema is paid for by every page.
- **Which model runs which step.** Two free models already held a typed schema
  perfectly in testing, but a reasoning model also returned empty content with
  no error, and the router answered German with an English summary. Model choice
  gets measured per step, against a real example of that step — and no step has
  a real example yet.
- **Whether notes stay markdown or become JSON.** Markdown while a person writes
  them; JSON if a script does. The switch is cheap and the answer is obvious
  once step 2 is automated.
- **How the novel comes back.** It is on the shelf. It returns as a decision,
  when there is a wiki to build it from.

---

## The first move

One category, end to end, by hand.

`theorie-physik` has 45 documents in the manifest and zero exported — and it is
where the load-bearing terms live. Fetch those 45, read three of them, gather the
terms they share, and look at what the pages actually turned out to need.

That is a day's work, it costs almost nothing, and it produces the one thing the
whole plan is currently missing: a real example of the thing being built.
