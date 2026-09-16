---
description: >-
  Compile a batch of exported Drive sources into candidate wiki pages with
  BatchCompile: triage, cited claims, concepts merged across the whole batch, a
  knowledge diff, and drafts in Wiki/candidates/ that a human promotes later.
  Usage: /research-ingest [--slug … | --category … | --tier … | --batch N]
argument-hint: "[--slug <slug> | --category audit | --tier T3-work] [--batch N]"
---

# Research ingest — sources become candidates, never pages

Phase B+C of the knowledge system (`Plan/wiki/knowledge-system-concept_2026-09-15.md`
§4). The program is `tools/kpwiki` `BatchCompile` (skill `dspy-wiki-compile`);
this command runs it and files what it drafted. It writes
`Wiki/candidates/**`, `Wiki/graph/edges.jsonl` and `Wiki/log.md` and nothing
else — `Wiki/sources/`, `Wiki/concepts/` and `Canon/` belong to
`/wiki-promote` and to the author (`Wiki/schema/writers.yaml`).

## Step 1: Pick the batch (deterministic, free)

```bash
python3 scripts/source_inventory.py --check     # the manifest is current
.venv-dspy/bin/python -m tools.kpwiki.research_ingest_cli --category audit
```

The dry run is the default: it prints the selected records, the existing
pages the merge can land on, the glossary terms, and stops before the first
LM call. Records without an export, truncated exports and the tiers the
contract never ingests (`T0-duplicate`, `T1-superseded`, `T4-out-of-scope`)
are dropped with a reason each. `--batch` defaults to the ingest batch size
in `Wiki/schema/conventions.yaml`.

Order of work across batches (concept §4 B): T3 kernkonzept and audits first,
then storyform, characters, worldbuilding, plot; T2 theory last.

## Step 2: Run it (`--write` is the author's flag)

```bash
.venv-dspy/bin/python -m tools.kpwiki.research_ingest_cli --category audit --write \
    --out tools/kpwiki/eval_runs/<date>-<selector>.json
```

**Never set `--write` on your own** — user-facing flags are user-owned
(`writers.yaml → user_flags`). Ask first, with the dry-run output in hand.

Without `ANTHROPIC_API_KEY` the run goes through the `claude` CLI
(`KP_LM_BACKEND=auto`); `KP_LM_CLI_LOG` shows one line per call so a long
batch stays observable. Budget roughly two calls per source plus one
clustering call plus one call per concept.

## Step 3: Read the knowledge diff before anything else

The run prints, in this order: how many sources were extracted and which were
skipped, how many claims and how many of them no concept used, one line per
decision (`create` / `update` / `flag` with its conflicts verbatim), the diff
per existing page (reinforced · challenged · new · gaps), which concepts are
`contradicted` because a disagreement is pending, and every place the model's
triage disagreed with the manifest (the manifest wins; the disagreement is
worth a look). Then the `compile_metric` score with its named deficits.

A `flag` is not a failure. It is the moment the wiki learned that a new source
disputes a page the author already reviewed.

## Step 4: Check what was written

The run lints every page it wrote (required fields, enums, citations resolve,
no `[K]`) and prints the findings. Then, free:

```bash
python3 scripts/render_wiki_views.py          # the views count candidates, so re-render
python3 scripts/wiki_lint.py --health
python3 scripts/render_wiki_views.py --check
```

The rendered views are a different writer (`writers.yaml`), which is why the
ingest does not touch them: run the renderer yourself after a batch, or
`--check` reports `index.md` and `coverage.json` stale.

A candidate with findings is never promoted — fix the draft or re-run that
slug. Candidates older than the age limit in `conventions.yaml` are reported
by the lint; promote or drop them.

## Step 5: Hand over

Present to the author: the knowledge diff, the metric score, the contradicted
concepts and the triage disagreements. Promotion is `/wiki-promote` and a
human decision. On any canon, scope or wording ambiguity: AskUserQuestion
(Rule 0). A merge, supersession or deletion of a reviewed page needs
`/tetraframe` first.
