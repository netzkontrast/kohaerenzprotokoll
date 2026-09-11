---
name: novel-architect-legacy
description: Historical evidence and migration skill for Kohärenz Protokoll; compares removed Legacy snapshots against current repo state without treating history as authority.
metadata:
  category: creative-writing
  source: repo
  version: "2.0.0"
  status: active
  date_updated: "2026-09-11"
---

# Novel Architect — Legacy Evidence

Use this skill only when older drafts, historical skills, prior plans or repository history are needed to recover intent, compare variants or explain provenance.

## Current-first rule

Start with [the shared current reference map](../PROJECT_REFERENCES.md). Historical material is **evidence, not authority**.

The old imported skill corpus previously lived under `Legacy/skills/` and was removed from current `main`. Its historical source can still be inspected at commit `bb7357e12472ebdc46a259bfcde035f08dd38f90`.

Historical skill set there included:

- `dramatica-theory`
- `dramatica-vocabulary`
- `ncp-author`
- `novel-architect`
- `novel-architect-character`
- `novel-architect-world`
- `novel-architect-structure`
- `novel-architect-scene`
- `novel-architect-legacy`

## Use cases

- Compare an older chapter/draft against current prose.
- Recover why a current lock exists.
- Find an idea that may still be useful but has not been promoted into current plans.
- Audit whether a current file still links to removed snapshots.

## Comparison protocol

1. Read current work/arc/chapter source first.
2. Fetch the historical artifact at its exact commit/path.
3. Separate facts into: still current / superseded / useful but provisional / conflicting.
4. Never copy old assumptions wholesale.
5. If an older idea is reintroduced, place it in a current decision log as `[V]` unless already supported by `[K]` canon.

## Important historical lesson

A previous session drafted against an outdated skill snapshot before comparing it with the newer repo canon. Therefore every legacy-assisted workflow must explicitly compare source dates/current branch state before writing.
