---
description: >-
  Run every free, deterministic gate in the repository at once — wiki health,
  rendered views, source manifest, claim provenance, both storyforms, chapter
  drift, and optionally every chapter lint — then read the findings and fix or
  report them. No API key, no network, no cost.
argument-hint: "[--chapters]"
---

# Check — the whole repository, deterministically

```bash
python3 scripts/kp_check.py              # the standing gates
python3 scripts/kp_check.py --chapters   # also lint every chapter file
```

Run this before saying any piece of work is finished. It is free, so there is
never a reason to skip it.

## What each gate proves

| gate | proves |
|---|---|
| wiki health | `Wiki/**` satisfies the contract in `Wiki/SCHEMA.md` — required fields, enums, citations that resolve |
| wiki views | `Wiki/index.md` and `coverage.json` match the pages on disk |
| codex views | every rendered file under `Codex/` matches `Graph/` — the three navigation routers, the `entries/`, `axioms/` and `timeline/` trees, and no orphan left behind by a renamed slug |
| source manifest | `Sources/manifest.jsonl` matches the files in `Sources/` |
| claim provenance | no `NovelClaim` points into `Wiki/` (D-W2) |
| storyform | both NCP files still satisfy the decidable Dramatica rows |
| chapter drift | where `Graph/` chapter bodies and the `Manuscript/` files diverge |
| chapter lints | R-rules and the Act-I fences, per chapter file |

## Reading the output

A failing gate names what to re-run. Two results are expected and are not
defects:

- **Storyform B fails rows 2 and 10.** Those are the documented heterodox
  linear-progressive signposts, Canon-Lock. Never "fix" them.
- **Chapter drift reports `ahead` for most chapters.** `Manuscript/` is the
  source of truth for prose; the graph holds outline stubs. `behind` is the
  one worth a look.

## What a lint cannot tell you

A lint proves a forbidden word is absent. It can never show that something
required is missing. After the gates pass, still read the work: frontmatter
complete, every cross-reference resolving, every new term carrying a codex
entry in `Graph/nodes/codex_entry.jsonl`, and no sentence that defers work
instead of doing it.

For prose quality, the LLM pass is separate and costs tokens:
`python3 scripts/lit_critic_gate.py --chapter N` (skill: `lit-critic`).
