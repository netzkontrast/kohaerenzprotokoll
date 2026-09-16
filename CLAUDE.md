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

**27 of 680 source documents are landed.** The rest have never been exported.
`Wiki/` does not exist yet — the first term pages are written by hand, and the
schema follows them rather than preceding them.

Check it yourself rather than trusting this paragraph:

```bash
python3 scripts/sources.py status     # by category and tier
python3 scripts/sources.py check      # manifest against disk
```

## The process

Five steps. Two of them are a person.

```
Drive ──fetch──→ Sources/drive/*.md ──read──→ Sources/notes/*.md
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
version: a note harvests what one document says about which terms, quoting with
line numbers. A term page collects every source's reading of one term,
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
supported. They need a decision, and none has been tried —
`Plan/learnings/fetch.md` has the format census.

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
commands are parked there. Nothing links to it, no script reads it, and it is
not part of any workflow. `README.md` says in one sentence what it holds.

It is a shelf, not a layer. If it starts being referenced, it has become a layer
again — and that is the thing being removed.
