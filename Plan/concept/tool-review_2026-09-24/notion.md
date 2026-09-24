# Notion connector + the four vendored Notion skills — tool review, 2026-09-24

Scope, per the plan's row 7 and this job's instructions: **read-only, no corpus
text.** No document (5 or 6, or any other) was sent to Notion, no page was
created, updated or commented on. The review is on paper: what the connector
already holds, what the four skills promise, and where either could or could
not sit next to `NOW.md`, `Plan/decisions/` and `Wiki/questions/`.

**Reached: yes**, for the read-only surface. `mcp__Notion__*` tools that write
(`create_pages`, `update_page`, `create_comment`, …) were **not reached on
purpose** — they were not called, per the task's rule, not because they failed.

## What ran

1. `mcp__Notion__notion-get-tool-access {}` — the access map for this
   connection.
2. `mcp__Notion__notion-search {"query": "Kohärenz"}` — a generic project word,
   not corpus text from either permitted document.
3. Read the four skills' `SKILL.md` in full:
   `.claude/skills/knowledge-capture/SKILL.md`,
   `.claude/skills/meeting-intelligence/SKILL.md`,
   `.claude/skills/research-documentation/SKILL.md`,
   `.claude/skills/spec-to-implementation/SKILL.md`.

Raw results: `Plan/runs/tooltest/notion/search-kohaerenz.json`.

## Numbers

- `notion-get-tool-access`: `search.status = "available"`;
  `ai_search.status = "plan_required"` (Business/Enterprise upsell) — so the
  legacy `search` tool was used, not `ai_search`, exactly as its own
  instructions say to do when `ai_search` is unavailable.
- `notion-search("Kohärenz")`: **10 results**, all under one root page
  „📖 Kohärenz Protokoll". Nine are dated 2026-03-26; the root page itself was
  last edited 2026-09-24T17:08.
- No entity-scoring number applies here: this task sent no document text to
  any model and extracted no names, so `scripts/entities.py score` was not
  run. (Contrast with the other tool rows, which read documents through the
  router; this one is explicitly read-only.)

## What the search found, and why it matters more than expected

The workspace is **not empty**. It already holds a Notion-native planning
surface for this novel — „📖 Kohärenz Protokoll" and nine child pages:
Kohärenz-Prüfung, Szene vorbereiten, Alter-Stimme aktivieren, Konflikt klären,
Kapitel planen, Projekt-Dashboard, Foreshadowing-Audit, Entitäten-Landkarte,
Canon-Status ändern. The root page's own highlighted text says what it is for:
„Es dient nicht als Archiv oder Wiki, sondern als Arbeitsumgebung für drei
konkrete Tätigkeiten: Schreiben, Entscheiden und …" — a workspace for writing
and deciding, by its own description, not an archive or wiki. Page bodies were
not fetched (out of scope for this review; titles and the search highlight
were enough to place it).

This predates the current repository's process (nine of the ten pages are
dated 2026-03-26, before the two-layer rediscovery of decision 005 and before
`Sources/`/`Wiki/` existed in their present form) and sits **outside** both
layers this project keeps: no script here reads it, and per `CLAUDE.md`
nothing in `Wiki/` or `Sources/` may cite a Notion page. It is a parallel,
disconnected planning surface for the same novel, already containing a
„⚖️ Konflikt klären" page and a „🔮 Canon-Status ändern" page — names that
describe exactly what `Wiki/conflicts/` and decision 006 already do inside the
repository, under git.

## Reading the four skills

All four (`knowledge-capture`, `meeting-intelligence`, `research-documentation`,
`spec-to-implementation`) are unchanged upstream copies (per `CLAUDE.md`) from
`netzkontrast/notion-skills`. Read on paper, none of the four maps well onto
this project's actual objects:

| skill | what it produces | nearest repository object | fit |
|---|---|---|---|
| `knowledge-capture` | a Notion page from a conversation: key points, decisions, action items, cross-links | `Plan/decisions/*.md`, `NOW.md`'s "Questions for the author" | poor — decisions here are one short file each, append-only, under git, with evidence inline; the skill's "create/update Notion pages" step is a write this task must not make, and its output would sit exactly where `CLAUDE.md` says nothing in `Wiki/`/`Sources/` may point |
| `meeting-intelligence` | a Notion agenda from a "meeting database" and "attendee database" | nothing — there is no meeting cadence or attendee roster in this repository; the project's "meeting" is the author reading `NOW.md` | no fit at all |
| `research-documentation` | a Notion research database with citation formats (APA/MLA/…) | `Sources/`, `Wiki/candidates/`, `Wiki/compare/` | poor — this project's citation unit is `^[Lnn]` verified by `quotes.py` against the landed text itself, not an academic citation style; a second, parallel "research database" in Notion would duplicate `Sources/manifest.jsonl` without the checksum/tier machinery that makes it trustworthy |
| `spec-to-implementation` | task breakdown, timelines, effort estimates, ownership, a Notion dashboard | nothing current — `NOW.md` says explicitly "There is no board, no status field and no backlog" | actively contrary to how this repository tracks work |

All four assume a **Notion API integration token** and named database IDs
(`NOTION_DATABASE_ID`, `MEETING_DATABASE_ID`, …) in `.env`-style config. That
is not how this connector is reached here — Notion is reached only through the
claude.ai-connected `mcp__Notion__*` tools, which carry their own auth, and
`CLAUDE.md` already says no token is written to a file in this repository. So
even where a skill's *idea* might apply, its *configuration* section does not
describe how this project would actually invoke it.

## Why the two-layer rule limits all four, on paper

`CLAUDE.md`: "Notion is outside the two layers: no script reads it, and
nothing in `Wiki/` or `Sources/` may cite a Notion page." That is not a
technical limit on the connector — the MCP tools work, `search` returned real
results — it is a boundary this project has already drawn, for the same
reason `Legacy/` is a shelf and not a layer: a third place to look is a third
place that goes stale, and this repository's whole state-checking apparatus
(`scripts/state.py --prose`, `judgements.py`'s replay, `quotes.py`'s
line-verification) exists because untracked claims rot. Anything written into
Notion by one of these four skills would be:

- **outside git**, so it has no commit that names the source document (the
  rule "every revision of a page in `Wiki/` is committed immediately, and the
  commit message names the source document" has no equivalent there);
- **outside `scripts/state.py`'s reach**, so a number written into a Notion
  dashboard can go stale exactly the way this page's own numbers went stale
  four times before `--prose` was built — except nothing would ever catch it;
- **a second copy** of something `NOW.md`, `Plan/decisions/` or
  `Wiki/questions/` already holds under version control, which is the same
  failure this project already lived through with `Legacy/` becoming a
  competing layer.

Genuinely already-Notion-native material (the pre-existing „Kohärenz
Protokoll" workspace found above) is exactly the case `CLAUDE.md`'s rule
anticipates: it exists, it is real, and it is still outside both layers,
because nothing here reads it and nothing in `Wiki/`/`Sources/` may cite it.

## What a model's output through Notion could and could not be, under this project's limits

None of the four skills' Notion writes were exercised (out of scope). If they
had been: a Notion page built by `knowledge-capture` or `research-documentation`
from corpus text would be a **model's reading**, in the same standing as an
entity list or a `knowledge-graph-extract` triple (`CLAUDE.md`, "A model's
output here is a reading"). It could not:

- create a `Wiki/` page (only a person promotes a candidate);
- write a `[[link]]` (a link marks a term the prose already wrote, never
  inferred);
- supply a count (every number comes from `corpus.py`, `duplicates.py`, or a
  named command);
- merge two surfaces (`fold()` and its judgement ledger own that call);
- detect a conflict (conflict detection is never mechanised — `CLAUDE.md`
  states this twice, once generally and once by name against the retired
  pipeline's `Zero-Trust` false conflict).

At best it could sit beside the repository the way `Plan/entities/` or
`graphify-out/` sit — a proposal a person reads, cites by hand if it holds up,
and never a place the pipeline writes to or reads from automatically.

## Recommendation

**The one use worth trialling, if any: none of the four skills as installed.**
The evidence above is that all four assume a role (meeting prep, spec-to-task
breakdown, an API-token-configured research database) this project does not
have, and the one role that might fit — capturing a decision or a discussion —
already has a better-fitted, git-native, checked home (`Plan/decisions/`,
`NOW.md`) that these skills cannot improve on: they cannot add a commit that
names its source document, cannot be checked by `state.py`, and would create
exactly the second-layer drift `CLAUDE.md`'s two-layer rule was written to
prevent.

**Verdict: park**, for the four Notion skills (`knowledge-capture`,
`meeting-intelligence`, `research-documentation`, `spec-to-implementation`).
Evidence: their `SKILL.md` files' own "Requirements"/"Configuration" sections
name database shapes (meeting databases, attendee databases, task databases,
citation-format settings) this repository has none of; `NOW.md` explicitly
states "There is no board, no status field and no backlog", which
`spec-to-implementation` exists to build. May not: create a page, link, count,
merge or conflict-flag, per `CLAUDE.md`'s limits on any model reading —
so even a trial run's output could only ever be a proposal a person reads by
hand, which `Plan/decisions/*.md` already is, without the second layer.

**Verdict: park**, for the Notion connector itself, as a place for this
project's own artifacts. Evidence: it already holds a disconnected,
out-of-repository planning surface for the same novel (`search("Kohärenz")`,
10 results, one root page + 9 children, 2026-03-26) whose own text says it is
not meant as an archive or wiki — i.e. even Notion's existing content for this
project does not want the job `Wiki/` and `Sources/` already do. May not:
be cited from `Wiki/` or `Sources/` (CLAUDE.md, stated rule); may not carry a
number `state.py` can check. If the author ever wants a *read* surface for
people who do not use git — a rendered, human-facing mirror of `NOW.md` or the
conflict table, refreshed by a script rather than by a skill's own judgement —
that would be the one narrow use worth trialling later: a one-way,
mechanical **push** of already-committed markdown (not a skill choosing what
to write), which sidesteps every objection above because the git-tracked file
stays the source of truth and Notion holds a derived copy, not a second
original. That is not what any of the four installed skills do today, so
nothing here is being adopted or trialled — this review found the evidence for
why, and named the shape a future trial would have to take.
