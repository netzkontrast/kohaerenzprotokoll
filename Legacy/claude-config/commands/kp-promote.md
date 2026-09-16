---
description: >-
  Promote a reviewed candidate page out of Wiki/candidates/ into Wiki/sources/
  or Wiki/concepts/. The human review is the point; the command only performs
  the move once the author has decided.
argument-hint: "<candidate slug>"
---

# Promote — a reviewed candidate becomes a wiki page

`/research-ingest` drafts candidates. Nothing leaves `Wiki/candidates/` without
a person reading it. This command is that step, and it is the author's
decision, never the session's.

## 1. Read the candidate against its sources

```bash
cat Wiki/candidates/<slug>.md
python3 scripts/wiki_lint.py --health
```

Check, by reading rather than by trusting the draft:

- every citation resolves, and every quoted fragment stands verbatim in the
  lines it cites — in the source's own language;
- claims are in the language of the source they came from;
- `codex_ref` names a codex slug that exists, or is empty;
- a disagreement carries at least two distinct sources and one position each;
- nothing asserts a story fact the cited lines do not carry.

The pilot run found the quoting rule to be the one models break most often —
a German paraphrase of an English source putting a German term in quotation
marks. `Plan/wiki/pilot-run_2026-09-16.md` records the case.

## 2. Decide

`status: reviewed` is a protected state and means a person vouched for the
page. A page that contradicts an existing reviewed page, supersedes one, or
merges two needs `/tetraframe` first — four isolated positions, a contradiction
map, and the author choosing. A promotion that contradicts `Canon/` is an open
question, not a correction: Canon is `unverified` inside this loop and there is
no default winner (D-W12).

Run `/clarify` on any claim whose scope or terms are not already explicit.

## 3. Move it

A promotion is a move plus a status change plus a log line:

- `Wiki/candidates/<slug>.md` → `Wiki/sources/<slug>.md` or `Wiki/concepts/<slug>.md`
- `status: draft` → `status: reviewed`
- one line appended to `Wiki/log.md` in the grammar
  `## [YYYY-MM-DD] promote | <title> | skill=… | sha256=…`
- `python3 scripts/render_wiki_views.py` — the views count candidates, so they
  go stale on every promotion

Then `python3 scripts/kp_check.py` to confirm the wiki is still clean.

## What promotion is not

It does not write `Canon/` or `Graph/`. Research reaching canon is a separate,
author-locked step: a D-xx decision and `/kp-canon`.
