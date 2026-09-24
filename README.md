# Kohärenz Protokoll

A German hard-SF novel (Hard SciFi / Cosmic Horror / Psychological Thriller) and
the research corpus behind it.

**This repository is building one thing right now: a wiki of the project's own
terms, derived from its research sources.** What a term means, which source says
so, where the sources disagree, and what none of them settles. The novel rests
until that exists. `GOAL.md` says where it is going: a git-versioned knowledge
graph and wiki that helps write the novel.

## Start here

| read | for |
|---|---|
| `PRINCIPLES.md` | the rules, each with the evidence that produced it — before building anything |
| `GOAL.md` | the author's brief, in German: the target, not the repository |
| `CLAUDE.md` | the working agreement, and what exists now |
| `NOW.md` | what is open: questions for the author, work half-done, what failed |

## Layout

| folder | holds |
|---|---|
| `Sources/` | the research documents from Drive and the manifest that indexes them — the only layer that is true — and, beside each document read, its census and its note |
| `Wiki/` | term pages derived from those sources, conflict records, question pages, and the record of each reconciliation |
| `Plan/` | how the work is done: concepts, decisions, learnings, and every artifact of every run |
| `scripts/` | the tools, one job each |
| `.agents/skills/` | this project's skills; `.claude/skills/` links to them and holds the vendored ones |
| `Legacy/` | everything the project used to be, parked and read by nothing |

Each of these but `Legacy/` has a README that says what is in it.

## Where things stand

**371 <!--state:sources.landed--> of 613 <!--state:sources.total--> documents
are landed, 13 <!--state:documents.reconciled--> are read and reconciled, and
the wiki holds 92 <!--state:wiki.pages--> pages,
12 <!--state:wiki.conflicts--> conflicts and 5 <!--state:wiki.questions-->
questions.** Every number here is measured, and checked:

```bash
python3 scripts/state.py            # every measurement, derived now
python3 scripts/state.py --prose    # fail on any marked number that has gone stale
python3 scripts/selftests.py        # every checker, one line each: held, FAILED, or not run
python3 scripts/sources.py check    # the manifest against the disk
```

The standard-library scripts need no key and no network. A cloud session runs
`scripts/install.sh` at start, which builds the virtualenvs and tools the other
steps need; `scripts/install.sh --check` says what is present.

**A model proposes, it never decides, and nothing leaves the container without
the author's yes** (`GOAL.md`, rule 13). Every model call goes through a script
that refuses it without an approval for that run.

## `Legacy/`

Holds the previous shape of this project — the novel manuscript, the fact graph,
the rendered codex, the canon documents, the old planning record and the retired
command surface — parked at commit `608cbb5` when the wiki became the focus.
Nothing in the working system links to it or reads it.

The full tree as it stood before the reset is also on the branch
`backup/pre-restart-2026-09-16`.

## Licence

See `LICENSE`.
