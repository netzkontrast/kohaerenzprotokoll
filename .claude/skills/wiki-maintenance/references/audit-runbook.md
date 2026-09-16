# Full Wiki audit runbook

Use this for requests such as “check every page”, “clean up the Wiki”, or
“verify the new rules”. The audit is incomplete unless every phase is covered.

## 1. Inventory

- Enumerate every file under `Wiki/`, grouped as authored page, candidate,
  rendered view, schema, template, or operational document.
- Compare actual directories with the partitions declared in
  `Wiki/schema/conventions.yaml` and `entities.yaml`.
- Record counts by kind, status, partition, and candidate/promoted state.

## 2. Page-by-page checks

For every authored and candidate Markdown page, verify:

- frontmatter parses and required fields/sections exist;
- path equals kind-derived partition and slug is globally unique;
- one semantic entity, focused title, and page-size budget;
- claims retain citations and links resolve;
- lifecycle and authority are not silently changed;
- manuscript-facing pages have a truthful ≤40-word context summary, priority,
  chapter window, and spoiler ceiling;
- `chapter_start <= chapter_end` and spoiler metadata is conservative when
  uncertain.

Do not infer that an empty Wiki is fully audited merely because lint passes:
system pages, schemas, templates, renderers, and navigation still require
inspection.

## 3. Navigation and retrieval

- Render all views and inspect the global index plus every local `README.md`.
- Verify each partition is reachable from `Wiki/index.md` and back-links are
  obvious.
- Confirm empty partitions have no stale nested index.
- Inspect `Wiki/context-map.md`: it must contain routing metadata, exclude raw
  source bodies, and link to the smallest relevant pages.
- Test one early-chapter and one whole-novel retrieval path using
  `references/context-loading.md`.

## 4. Rule adequacy

Challenge each new rule with both a passing and a failing fixture. At minimum
cover wrong partition, duplicate slug, oversized page, broken navigation,
stale rendered index, invalid context window, and overlong context summary.
If a meaningful structural defect can still pass, improve the machine rule or
state explicitly why it requires human review.

## 5. Verification and report

Run compile checks, focused tests, `wiki_lint.py --health`, renderer write then
`--check`, and `git diff --check`. Report exact results, unavailable test
dependencies, every page inspected, and unresolved author decisions. Never
claim a full audit from a sample.
