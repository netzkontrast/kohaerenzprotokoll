---
description: >-
  Print a read-only structure/health snapshot of the research Wiki
  (Wiki/**): the schema contract, page counts by kind and partition, lint
  health, and view freshness. Simplified companion to /lint-wiki — a status
  check, not a full corpus audit. Usage: /wiki-structure
argument-hint: ""
---

# Wiki Structure — Snapshot

Read-only. Writes nothing, fixes nothing. Use this before deciding whether
a full `/lint-wiki` or `/research-ingest` run is warranted, or whenever a
session needs to know what the Wiki currently looks like before writing
into it.

## Step 1: The contract (what a page is allowed to be)

Read `Wiki/SCHEMA.md` §"Directory contract" and summarise in one line each:

- The four page kinds and their canonical path pattern (`sources/<category>/`,
  `concepts/<kind_detail>/`, `questions/<axis>/`, `syntheses/<YYYY>/`)
- Which files are rendered (never hand-edited): `index.md`, `concept-table.md`,
  `context-map.md`, `graph/coverage.json`, every partition `README.md`
- Page budgets from `Wiki/schema/conventions.yaml` (split before the hard max)

## Step 2: Deterministic health (free, no LLM)

```bash
python3 scripts/wiki_lint.py --health
python3 scripts/render_wiki_views.py --check
```

Report verbatim: errors/warnings/info counts, pages by kind, pages by
status, candidate count, open questions by axis, contested pages, sources
ingested vs. manifest total, edge count, and whether views are stale.

## Step 3: Partition inventory

For each occupied kind directory (`sources/`, `concepts/`, `questions/`,
`syntheses/`), list its partitions and page counts:

```bash
for d in Wiki/sources Wiki/concepts Wiki/questions Wiki/syntheses; do
  [ -d "$d" ] || continue
  echo "== $d =="
  find "$d" -mindepth 1 -maxdepth 1 -type d | while read -r p; do
    n=$(find "$p" -maxdepth 1 -name "*.md" ! -name "README.md" | wc -l)
    echo "  $(basename "$p"): $n page(s)"
  done
done
```

Empty taxonomy (0 pages everywhere) is a valid, expected state early in the
research-ingest pipeline — report it as such, not as a failure.

## Step 4: Candidates awaiting promotion

```bash
find Wiki/candidates -name "*.md" 2>/dev/null | wc -l
```

Candidates are drafts from `/research-ingest` that only `/wiki-promote`
(human-gated) moves into `sources/` or `concepts/`. Report the count; do
not promote anything from this command.

## Output format

One compact report:

1. **Contract** — the one-line summary from Step 1
2. **Health** — `wiki_lint --health` output verbatim + view-freshness line
3. **Inventory** — partition table from Step 3
4. **Pending** — candidate count from Step 4, and open-question count by axis
5. **Next action** — the single most useful next step given the numbers
   above (e.g. "views stale → render_wiki_views", "12 candidates, 0
   promoted → run /wiki-promote", "0 pages → run /research-ingest first")

Do not fix, promote, or edit anything — this command only reports.
