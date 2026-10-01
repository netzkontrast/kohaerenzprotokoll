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

Twenty-seven further contracts were written on 2026-09-30, in four families — terms (`TermDefinitions`,
`TermContrasts`, `AliasPairs`, `Analogies`, `TermTaxonomy`), claims and sources (`CausalLinks`, `Rules`,
`Quantities`, `Attributions`, `StandingClaims`, `OpenPoints`, `Locks`), plot and chapters (`ChapterCards`,
`ChapterBeats`, `StructureBeats`, `Storypoints`, `Precedence`, `Anchors`, `ThemeMotifs`, `Pitch`) and cast and
voice (`CastRoles`, `CardFields`, `EntityFacts`, `Knowledge`, `ProseRules`, `DiegeticTerms`, `Utterances`). Which
to run on which document, and what each was worth on a pilot, is
`Plan/concept/graph-contracts_2026-09-30.md`; `hegraph.py` loads their rows into the store as `P_HE_<KIND>`
proposals and `python3 scripts/hegraph.py report` prints the yield.

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
4. Run the actual extraction pipeline offline with a canned response:

```bash
python3 scripts/reading_extract.py smoke <candidate.yaml> \
  --text <synthetic-source.txt> --response <native-response.json>
python3 scripts/hx.py prompt <candidate.yaml>     # the prompt and schema a model is sent
python3 scripts/reading_extract.py selftest
```

HyperExtract's engine is ported to `scripts/hx.py` (decision 020), standard library
only: the prompt, the JSON schema, the chunks and the merge are byte for byte what
upstream 395039e builds, and `python3 scripts/hx.py parity` holds it to the upstream
package when `scripts/install.sh hyperextract` has installed it. The committed
synthetic fixtures are in `Plan/hyperextract/fixtures/`. `smoke` answers every chunk
with the canned reply. It proves loading/schema/chunk/merge behavior, **not** prompt
quality or model recall. Test a bad payload as well; it must fail.

The extraction helper and stage both reject empty data; a chunk whose reply fails
the schema twice is dropped, as upstream drops it, and a run of nothing but such
chunks merges to empty `items`.

5. For a live pilot, use the existing route/consent and call-recording workflow
   from `.agents/skills/dspy/SKILL.md`; inspect the current decision and consent
   file for this purpose/source. Never widen them. PR #123's wrapper is:

```bash
python3 scripts/templates.py parse <one-source-file> \
  -t <candidate.yaml> -l en -o <new-ka-directory> --source <slug> --no-index
```

This needs the upstream package and calls its configured provider; no pipeline
step uses it. For an explicit approved client, use
`reading_extract.extract(template_path, document(slug), ask, extractor)` — `ask` is
`he_claude.Claude` or any callable `(prompt, schema, check) -> reply` — and save its
returned JSON envelope in your assigned trial directory.

**Claude is the approved client, first party (decision 011).**
`python3 scripts/he_claude.py run <slug> <template.yaml> --run <new-name> [--model haiku]` (a list, set or graph template)
extracts, stages, and records every call in `calls.jsonl` and `usage.json`. Its first
live pass (TermReadings on Haiku, 58 lines, $0.035) found a failure: the model closes
a German „…“ with a straight quote. The adapter now names the typography and puts
the mark back where a reply does not parse, counting each repair. The page
`.agents/skills/reader-tools/references/failures.md` lists this failure and the
others measured. It fixes
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

## What the pilot of 2026-09-30 measured

Thirty-seven runs on eight documents, $3.70, and 261 rows a reader labelled; then a second pass of three contracts, 36 runs on the twelve
documents that hold most of the bench's gold, $11.68, and 36 more labels (`Plan/runs/hyperextract-templates-2026-09-30/`).
Each rule below is enforced in code, because a prompt rule a Haiku reader ignored 8 times in 11 is not a rule:

1. **A contract that classifies the line under a heading is right more often than one that relates two names**
   (`ChapterBeats`, `StructureBeats`, `CardFields`, `ProseRules` 86–100 % against `AliasPairs` 40 %, `Precedence` 17 %).
   Its subject is the heading above the line, which the model may write and code finds anyway.
2. **A slot is a name, not a clause.** A clause the model reworded is refused by the gate (`surface absent from
   document`) though the quotation is right; such a row enters the store on its quotation (`hegraph`'s *quote*
   footing), the pages in it found by code. Do not ask a model to copy a proposition.
3. **A name of under four characters is a name.** `quotes.parts_of` drops fragments that short, so the gate could
   never find `Lex`, `Nyx`, `Lia` or `KW1`; `reading_extract.stands` does. A word a contract gives for „no name"
   (`unlabelled`) is in `reading_extract.NO_NAME`.
4. **A cue the contract is about is checked in code, only where it is the contract** — `hegraph.CUE_REQUIRED`
   (`ALIAS`, `BEFORE`). The grade over every contract did not predict a right row (57 %, 54 %, 71 % ok at grades
   0, 1, 2, over 297 rows), because a list item under a heading is right with no cue word in it.
5. **An empty answer is a result.** `Locks`, `Quantities`, `Attributions`, `StandingClaims`, `Pitch` answered every
   call and found nothing on documents that hold none. `hegraph report` counts them apart from failures.
6. **Run by category, and price it from the ledger.** About $7.3 for each megabyte a contract reads, so $190 for the
   whole corpus and $66 for the plot outlines; a contract that reads outlines has no use on a physics paper.
   `hegraph.gate` keeps only the paragraphs that hold a cue, and on `CausalLinks` it cut the cost and the yield alike
   (26 % of the lines for 29 % of the cost, `gate-ab.md`): it is a thinning, not a filter. The first estimate said $63, from „4.7 KB a call"; the
   call ledgers say 1.6 KB, and it took the scaled pass's 957 calls to see it. Sum `usage.json` calls against the
   bytes read before quoting a price (`claude_cli.totals` counts failed calls too).
7. **Label at least ten rows per contract before any number is quoted** — a precision of 79 % on 14 rows is
   79 % ± 20 points — and record every label in `labels.jsonl`.
8. **A pilot's precision is optimistic, so label again on the documents that will be run.** The three contracts of
   the scaled pass were 80 % `ok` on the pilot's 35 rows and 58 % on 36 rows drawn by hash from the twelve documents
   of the bench (none `wrong`; the drop is `ok` becoming `part`, and the defect is the slot, not the line).
9. **Coverage is not what limits a finder that spends a fixed number of lines — measure the next pass's first slice before
   paying for the rest.** After the scaled pass the `he-lines` finder added +0.029 document recall; a backfill then read five
   more documents that hold the bench's gold ($11.44, 14 runs, gold lines in read documents from 46 % to 57 %) and it added
   +0.029 again, the same seven cases. New documents' lines replaced old ones in the finder's 40; 182 of the gold-document slots
   the pack still missed were in documents a contract had read. Run `reach.py` and `ceiling.py`
   (`Plan/runs/hyperextract-backfill-2026-09-30/`) on the first slice, and stop when the bench does not move (decision 019).
   Order a pass by gold reached per dollar, not by gold count: the plan's order put a 372 KB document first, $0.35 a gold line
   where the other four cost $0.055.
