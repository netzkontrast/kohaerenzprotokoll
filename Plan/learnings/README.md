# Learnings — one file per workflow step

These files are the bridge between doing a step by hand and building the tool
for it. `PRINCIPLES.md` P3 says *by hand first, automate what has proved its
shape* — this directory is where the shape gets recorded while it is still
fresh, so that writing the tool later is transcription rather than
re-derivation.

They are working notes, not documentation. They are allowed to be ugly. What
they may not be is vague: a learning without a number, a path or a reproduction
is an impression, and an impression cannot be built against.

## One file per step

| file | step | what it feeds |
|---|---|---|
| `fetch.md` | Drive → `Sources/drive/` | `scripts/sources.py` |
| `extract-terms.md` | a source → its term census in `Sources/terms/` | `scripts/capture.py`, `scripts/profile.py`, the `ingest` skill |
| `read-source.md` | a source → its notes | the note format, the extract step, its model choice |
| `gather-term.md` | notes → a term page | the page schema, the compile step, the conflict detector |
| `review-promote.md` | candidate → `Wiki/terms/` | the review checklist, what a person must keep deciding |
| `ask.md` | a question → a cited answer | the retrieval path: `scripts/graphrag.py` |

The one-time reset of 2026-09-16 has no learnings file; decision 001 and
`Plan/concept/repo-and-workflow-concept_2026-09-16.md` explain the shape it left.

## The format

Each file carries the same six sections, so a later reader can scan across them:

**Status** — how many times the step has run, by hand or by tool. A learning
from one run is a hypothesis; from ten it is a pattern. Say which.

**What the step is** — one or two lines. If this is hard to write, the step is
not a step yet.

**Learnings** — numbered, each with its evidence. A number, a path, a command
that reproduces it. The test: could someone who was not there act on this?

**What the tool must handle** — the direct feed into automation. Every entry
here should be traceable to a numbered learning above it. This is the section
that gets read when the tool is finally written.

**What stays judgement** — the parts that must not be automated, and why. Under
P1 there are only two honest categories, so anything not decidable belongs here
explicitly rather than by omission.

**Measurements** — real numbers from real runs. Sizes, counts, durations, costs,
failure rates. These make later decisions cheap, and they are the first thing
that goes stale, so each carries its date.

## Rules for writing in them

- **Append, do not rewrite.** A learning that turned out wrong gets a line
  saying so underneath, not a deletion. Knowing that we believed something and
  why we stopped is worth more than a clean file.
- **Record the surprise, not the success.** A step that worked exactly as
  expected teaches nothing. What it did that you did not predict is the content.
- **Write the failure with its symptom.** "It broke" is useless; "the call
  returned an error naming a spill path, and the content was in that file" is a
  design.
- **Date anything that can rot.** Model names, prices, API shapes, file counts.

## When a file gets consumed

Once a step is automated and its tool is stable, its learnings file stops
growing and becomes the rationale for that tool — the *why* behind decisions
the code can only state as *what*. It stays where it is. Nothing here is
deleted, because the reasoning behind a tool is the part that cannot be
recovered by reading the tool.
