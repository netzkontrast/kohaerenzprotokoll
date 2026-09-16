# Kohärenz Protokoll

A German hard-SF novel (Hard SciFi / Cosmic Horror / Psychological Thriller) and
the research corpus behind it.

**This repository is currently building one thing: a wiki of the project's own
terms, derived from its research sources.** What a term means, which source says
so, and where the sources disagree. The novel itself rests until that exists.

## Layout

```
Sources/     680 research documents from Drive, plus the manifest that indexes them
             — the only source of truth. 27 landed so far.
Wiki/        term pages derived from those sources. Not created yet; the first
             ones are written by hand so the schema can follow them.
scripts/     sources.py — fetch, check, land, status
Plan/        concept/ (what is being built and why) · learnings/ (one file per
             workflow step) · decisions/ · quality/ (measurements)
Legacy/      everything the project used to be, parked and read by nothing
```

## Start here

- **`PRINCIPLES.md`** — read before building anything. The rules, each with the
  evidence that produced it, plus the catalogue of ideas kept for later.
- **`CLAUDE.md`** — the working agreement and the current state.
- **`Plan/concept/wiki-process_2026-09-16.md`** — the process, end to end.

## Where things stand

```bash
python3 scripts/sources.py status     # 27 of 680 landed, by category and tier
python3 scripts/sources.py check      # manifest against disk
```

Free, offline, no API key.

## `Legacy/`

Holds the previous shape of this project — the novel manuscript, the fact graph,
the rendered codex, the canon documents, the old planning record and the retired
command surface — parked at commit `608cbb5` when the wiki became the focus.
Nothing in the working system links to it or reads it.

The full tree as it stood before the reset is also on the branch
`backup/pre-restart-2026-09-16`.

## Licence

See `LICENSE`.
