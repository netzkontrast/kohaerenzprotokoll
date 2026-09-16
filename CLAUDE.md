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

## Two layers

| layer | what it is | who writes it |
|---|---|---|
| `Sources/` | research documents fetched from Drive, immutable once landed | `scripts/sources.py`, nothing else |
| `Wiki/` | term pages derived from those sources, promoted by a human | a person, for now |

There is no third layer. Everything else the project used to have is parked
under `Legacy/` and read by nothing.

`Sources/manifest.jsonl` is the spine: 680 rows, each with `drive_id`, `title`,
`slug`, `category`, `tier` and, once landed, `export_path` and two checksums.
Anything derived traces back to a `drive_id`.

## State, as of 2026-09-16

**409 of 680 source documents are landed.** The 271 that are not are the 247
`plot-outline` rows, deferred with the novel, plus the 39 `md` and one `mp3` that
have no route. Every category the wiki needs is complete.

**3 of the 409 landed documents have been read**, and their notes are in
`Sources/notes/`. **2 have a full term census**, in `Sources/terms/`, and the one
comparison between them is in `Wiki/compare/`. `Wiki/candidates/` holds **1 term page**, written by hand. The
schema follows the pages rather than preceding them, so neither `Wiki/terms/`
nor a page format exists yet.

Check it yourself rather than trusting this paragraph:

```bash
python3 scripts/sources.py status     # by category and tier
python3 scripts/sources.py check      # manifest against disk
```

## The process

Seven steps. Three of them are a person.

```
Drive ──fetch──→ Sources/drive/*.md ──┬──extract──→ Sources/terms/*.md
                                      │                    │
                                      └──read─────→ Sources/notes/*.md
                                                           │
                                                       compare ──→ Wiki/compare/*.md
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
treatment mechanical rather than a promise: every census opens with the same
probes in the same order. Documents meet only in the `compare` step, so what the
comparison finds is a result rather than an assumption carried in.

`Plan/learnings/extract-terms.md` has the fourteen special cases the first two
censuses found, and why the first comparison inverted the premise the step was
built on. A term page collects every source's reading of one term,
**attributed and unmerged** — where sources disagree the page says so and stops.
Which reading is right is the author's call, never the page's.

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

44 of the 680 rows are markdown or audio, which the connector does not list as
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
