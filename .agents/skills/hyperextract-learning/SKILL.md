---
name: hyperextract-learning
description: Build, update, test and improve HyperExtract extraction templates for this corpus with the hyperextract-template-agent. Use when readers need structured passage or relation candidates, when templates fail loading or quote placement, or when considering learned guideline improvements with DSPy/GEPA. Covers existing templates.py parse from PR 123, offline native smoke fixtures, source-checked staging and evaluation before promotion.
---

# Learn extraction templates from measured failures

Read `PRINCIPLES.md` and the assigned agent's scope. Use the existing
HyperExtract skills under `.claude/skills/`: `hyper-extract` to route design,
`hyperextract-record-designer` for passage lists, `hyperextract-graph-designer`
for explicit relation structures, `hyperextract-template-optimizer` for design
review, and `hyperextract-yaml-validator` for structure. Load only the relevant
references. Keep project rules in the executable checks rather than vendored skills.

Relationship content does not require a graph template: choose record-designer
and a list for distinct passage readings. The generic skills' graph routing and
automatic field-renaming suggestions do not override that project contract.

## Choose the existing template

| Template | Use | Limit |
|---|---|---|
| TermCensus | source-only term-name second reader | cannot replace the independent census or provide counts |
| LocationRegistry | the document's own location registry | score with `Plan/runs/tooltest/hyperextract/score_location_registry.py` |
| TermReadings | quoted passages with assertion/hedge/question/citation labels | one-line quotation placement; meaning awaits reader review |
| StatedRelations | narrowly stated affirmative relations | excludes uncertainty and can collapse repeated endpoint/predicate passages |
| RelationReadings | separate attributed relation passages, including uncertainty/denial/questions | list preserves passage variants; never a verified graph edge |

Begin from a real failed or missing instance. Freeze the reader's independent
census/note first. Scope a pilot to one source and a bounded set of passages.
Write candidate revisions and their fixtures under your assigned
`Plan/runs/<batch>/hyperextract-templates/<revision>/`; do not edit the active
template, installation, source, wiki, another agent's run, or a graph database.
Keep corpus names/examples in evaluation fixtures, never in production
guidelines. `name:` must match the YAML file stem for saved KA reloads.

## Build and test

1. Specify the task and expected output from actual passages. Identify positive,
   negative, uncertain, contradictory, duplicate and export-damaged cases. Preserve
   wording and language. Use few fields, no model-supplied line numbers, explicit
   non-LLM merge options where the chosen type requires them.
2. Review the candidate with the designer and optimizer skills. Every guideline
   change names a measured failure. Do not accept a suggested field rename that
   breaks the normalizer or fixture. Prefer passage lists when deduplication
   would erase contrary readings.
3. Run `python3 scripts/templates.py check <candidate.yaml>` and inspect **each**
   validate/load/resolve/project check. Unreached is not passed. The coordinator
   runs corpus-name checks; a blind document-reader receives the result rather
   than running the check that reads other sources and wiki surfaces.
4. Run the actual factory/extraction pipeline offline with a canned response:

```bash
<he-python> scripts/reading_extract.py smoke <candidate.yaml> \
  --text <synthetic-source.txt> --response <native-response.json>
python3 scripts/reading_extract.py selftest
```

`<he-python>` is the interpreter beside the installed `he` executable (the same
one `templates.he_python()` resolves). The committed synthetic fixtures are in
`Plan/hyperextract/fixtures/`. `smoke` uses explicit fake clients, exercises
`Template.create` and `feed_text`, and builds no embedding index. It proves
loading/schema/merge behavior, **not** prompt quality or model recall. Test a
bad payload as well; it must fail. Capture the installed versions.

Use the helper's returned Python object to serialize an export; HyperExtract
logs precede CLI stdout, so a redirected smoke log is not a JSON envelope.
The extraction helper and stage both reject empty data; native HyperExtract may
catch a chunk's schema failure and return empty `items` without raising.

5. For a live pilot, use the existing route/consent and call-recording workflow
   from `.agents/skills/dspy/SKILL.md`; inspect the current decision and consent
   file for this purpose/source. Never widen them. PR #123's wrapper is:

```bash
python3 scripts/templates.py parse <one-source-file> \
  -t <candidate.yaml> -l en -o <new-ka-directory> --source <slug> --no-index
```

This calls the configured provider. The MCP server exposes read/export tools;
it does not create a KA. For explicit approved clients, use
`reading_extract.extract(template_path, document(slug), llm, embedder, extractor)`
and save its returned JSON envelope in your assigned trial directory. It fixes
one source/template snapshot and produces native `items` or `nodes`/`edges`.
For a KA from the CLI wrapper, wrap `data.json` only with hashes captured **before**
the run and checked afterwards, source slug and the recorded extractor/model
identifier. Missing historical provenance means re-run, never invent it.
6. Stage the envelope:

```bash
python3 scripts/reading_extract.py stage <slug> <candidate.yaml> <export.json> --run <new-name>
```

Inspect `Plan/runs/<slug>/hyperextract/<new-name>/report.json` and
`candidates.jsonl`. A refusal remains in the report; ambiguous quotations list
all matching lines for passage selection. Resolve by revisiting the original
source and running a new attempt, never patch a quotation to manufacture a pass.
Only a reader can judge the relation, stance, world/external-work boundary and
whether the excerpt is enough. Re-check against current hashes before handoff.

## Evaluate and learn

Freeze the baseline YAML hash and provider version. Keep whole documents in one
split so overlapping windows cannot leak between train/dev/test. Obtain two
independent readings for evaluation; record their agreement and difference lists
instead of calling one list truth. Keep the final holdout unavailable to the
template designer and reflection model.

Report separately: reachable/answered/parsed attempts, rows inspected, quote
placement, ambiguous passages, unsupported/invented relations, stance errors,
precision/recall against adjudicated passage examples, each disagreement list,
distinct source coverage, latency, actual tokens and cost. Empty extraction,
schema errors or unavailable runs never score as success. Uncertainty becoming
assertion, cross-source merging or an invented quote is a veto, not an average
penalty. Re-run with cache disabled to measure reliability.

Use manual guideline corrections first. If recurring residual errors remain
and a reviewed train/dev set and budget exist, read the DSPy skill's
`references/metrics.md`, `data.md`, `optimizers.md` and `text-artifacts.md`.
Use GEPA text optimization for YAML guideline text, or DSPy for a separately
defined typed extraction program; do not assume optimizing a DSPy prompt
optimizes HyperExtract's own prompt assembly. Keep the YAML schema, provenance
fields and stage checks fixed. Evaluate each proposed guideline through the
**actual HyperExtract pilot** with the same placement gate and human semantic
labels. Apply an explicit call budget; no unbounded optimizer in initialization.

Save each learned candidate as a new revision with parent hash, failure examples,
dataset/split hashes, provider/optimizer versions, call ledger and held-out report.
The coordinator promotes only a reviewed candidate that improves the fixed
baseline without a veto; retain the previous template for rollback. Do not claim
a template is learned because a smoke fixture passed. No learned template or
corpus-quality improvement has been measured by the committed synthetic tests.

Return the template diff, examples it fixes/regresses, stage report, repeat
results, usage and recommendation: retain, revise, pilot, or promote for review.
