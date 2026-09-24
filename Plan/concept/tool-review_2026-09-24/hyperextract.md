# Tool review — Hyper-Extract (`he`, `he-mcp`)

*2026-09-24. Documents 5 (`aegis-subplots-kapitelweise-system-exploration-docx`)
and 6 (`roman-lokalitaeten-konzept-und-ausarbeitung`) under decision 007. Router
at `http://127.0.0.1:8787/v1` (`scripts/route.py serve`), free model only,
`TIKTOKEN_CACHE_DIR` set as `Plan/concept/tool-review-plan_2026-09-24.md`
specifies.*

## Result in one line

**The write side is NOT REACHED for all four project templates.** `he parse -t
<path>.yaml` cannot load a template from a file path at all in the installed
CLI (Hyper-Extract 0.10.3) — this is a code-path limitation, reproduced
identically and instantly (no model call, no chunking) for every one of
`TermCensus`, `LocationRegistry`, `TermReadings`, `StatedRelations`, on both
documents. The read side (`he info`, `he search`, the three `he-mcp` tools
exercised) works, checked against a real Knowledge Abstract built from
document 5 with a built-in template, which also proves `he parse` itself,
the router, and the free model all work end to end when the CLI can find the
template.

## Write side: `he parse` and the four templates

**Root cause, from the installed package** (not from this repository):

```
he parse Sources/drive/aegis-subplots-kapitelweise-system-exploration-docx.md \
  -t Plan/hyperextract/TermCensus.yaml -l en \
  -o Plan/runs/tooltest/hyperextract/aegis-subplots-kapitelweise-system-exploration-docx/TermCensus-a1 \
  --source aegis-subplots-kapitelweise-system-exploration-docx --no-index
# Error: Template 'Plan/hyperextract/TermCensus.yaml' not found
```

`hyperextract/cli/cli.py:331` resolves `-t` with `Template.get(template)`
(`hyperextract/utils/template_engine/template.py:92`), which only checks
`method/<name>` or `Gallery.get(path)`. `Gallery` (`gallery.py:12`) is built
once at import from the package's own bundled
`hyperextract/templates/presets/**/*.yaml` — 40 built-in templates, listed by
`he list template` and by the `mcp__hyper-extract__list_templates` tool
(pasted in full below; none of `TermCensus`/`LocationRegistry`/
`TermReadings`/`StatedRelations` appear, because nothing registers them).
There is no `he template add`/`install` command — `he template` has exactly
one subcommand, `validate`, which *does* take an arbitrary file path (that is
why `python3 scripts/templates.py check` and the optimiser's report, both
built on `validate`, never hit this). The Python API `Template.create()`
docstring even shows a file-path example (`"/path/to/template.yaml"`), but
`he parse`'s CLI never calls `create()` for template resolution, only `get()`.

I ran the identical command for all four templates on both documents (8
calls); all 8 failed with the same message, instantly (well under a second,
confirmed by the fact no router call appears in the ledger for these 8
attempts). Per P18 this needed no second attempt — nothing model-dependent
ran, so a repeat would reproduce the identical deterministic error, not a
different outcome. This is the CLI as shipped, not this repository's
templates or router: `he template validate` (used by
`scripts/templates.py check`) passes all four with the same file paths that
`he parse -t` rejects.

**What would reach it (P15):** either a `he template add <path>` /
`--template-file <path>` command that this CLI version does not have, or
copying the YAML into the installed package's own
`hyperextract/templates/presets/<domain>/` directory so `Gallery` picks it up
at import — a workaround, not a fix, and one this review did not take: it
would edit files inside a shared, uv-tool-managed installation outside this
repository and outside `Plan/runs/tooltest/hyperextract/` (the sandbox this
review was told to write in), so it is reported rather than done. A future
session could try it in a throwaway copy of the venv and confirm; it is not a
claim this review makes.

## Proving the rest of the chain still works

To separate "the CLI cannot find our four templates" from "he parse doesn't
work here," I ran `he parse` on document 5 with a **built-in** template
(`general/set`, the closest gallery match to `TermCensus`'s shape: name/type/
description, `set` autotype):

```
he config llm -p openai -u http://127.0.0.1:8787/v1 -k route:hyperextract:aegis-subplots-kapitelweise-system-exploration-docx:1 -m free
he config embedder -p openai -u http://127.0.0.1:8787/v1 -k route:hyperextract:aegis-subplots-kapitelweise-system-exploration-docx -m local
he parse Sources/drive/aegis-subplots-kapitelweise-system-exploration-docx.md \
  -t general/set -l en \
  -o Plan/runs/tooltest/hyperextract/aegis-subplots-kapitelweise-system-exploration-docx/general-set-a1 \
  --source aegis-subplots-kapitelweise-system-exploration-docx --no-index
```

Succeeded in 2m33s real time, 259 items written to `.../general-set-a1/data.json`.
`python3 scripts/route.py ledger` (run right after) shows the `hyperextract`
purpose: **241 chat calls ok, 0 refused, 0 unreached, cost $0.000000**,
answered by `cohere/north-mini-code:free`, plus 28 local embedding calls by
`local/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`. So the
router, the free model, the forced-tool-call shape Hyper-Extract sends, and
`he parse`'s chunking/merge pipeline all work on this corpus — the failure
above is specifically the `-t <path>` argument, nothing downstream of it.

One reliability note from the run's own log, not scored further here: a
`stage=batch_filter none_results_detected` warning fired once with
`none_count=67 total=126` — 67 of 126 per-chunk extraction calls in one batch
returned no parseable result before the run's retry/merge logic still
produced 259 items overall. Worth remembering if a future run is scored on
completeness rather than just reachability: a free model dropping half a
batch is not visible in the `ok`/`refused`/`unreached` ledger buckets.

**Names, scored** (the only scoring this run's output permits — `general/set`
is not `TermCensus`, so this is a mechanics check, not the template's own
score):

```
python3 scripts/entities.py score aegis-subplots-kapitelweise-system-exploration-docx \
  --names Plan/runs/tooltest/hyperextract/aegis-subplots-kapitelweise-system-exploration-docx/general-set-a1-names.json
```
```
reader 60, model 209 verified, shared 22 (folded); 48 refused (not in the document word for word), 0 set apart as lens
precision 0.11  recall 0.37  F1 0.16  — two readers scored 0.66 (P27)
```
209 of 259 names verify word-for-word against the document (the rest are
`general/set`'s free-text `description` field bleeding paraphrase into what
should be exact terms — expected, since that template was never asked to
copy exactly, unlike `TermCensus`'s guideline). F1 0.16 is below both human
readers (0.66, P27) and the Haiku entity list on this document (0.25) — as
expected for a template with no exact-copy instruction, scored on names
alone. **This number describes `general/set`, not `TermCensus`, and is not
this tool's real score** — it exists only to prove the score path itself
(`entities.py score --names`) runs against genuine `he parse` output.

`LocationRegistry`, `TermReadings` and `StatedRelations` never produced
output, so their planned scorers could not run against real data:

- `Plan/runs/tooltest/hyperextract/score_location_registry.py` — written as
  asked, parses document 6's own master table from L185 (51 rows, confirmed:
  `awk 'NR>=185 && /^\|/' Sources/drive/roman-lokalitaeten-konzept-und-ausarbeitung.md`
  minus header/divider rows), and would report which `name`s came back and
  whether each `source` cell matches exactly. It has not been run against a
  `LocationRegistry` Knowledge Abstract because none exists.
- `TermReadings` on document 5: the planned check (`python3 scripts/read.py
  <slug> --find "<quote>"` per placed quote, against the 17 `^[Lnn]`
  citations in `Sources/notes/aegis-subplots-kapitelweise-system-exploration-docx.md`)
  is NOT REACHED for the same reason.
- `StatedRelations` on document 6: NOT REACHED for the same reason.

## Read side: `he info`, `he search`, `he-mcp`

Run against the one real Knowledge Abstract this review could build
(`general/set` on document 5, above):

- `he info <ka> --sources` / `mcp__hyper-extract__info(include_sources=true)`:
  returns template, language, created/updated, index status and a per-source
  row. **`nodes: 0`, `edges: 0` and `raw_items: 0`**, even though `data.json`
  holds 259 items — `set` autotypes are not stored as a node/edge graph, so
  0/0 there is expected, but `raw_items: 0` while the KA plainly holds 259
  items is a discrepancy this review did not chase further (time-boxed); it
  is reported, not explained.
- `he build-index` (7.4s) then `he search <ka> "AEGIS Guardian" -n 3` /
  `mcp__hyper-extract__search`: both return the same three ranked items
  (`Kael`, `AEGIS-System`, `Guardians`) in 2.7s — local embeddings, no router
  call, matches `CLAUDE.md`'s "no free embedding model accepted the policy"
  finding. `talk`/`ask` (LLM-backed Q&A over the KA) was not exercised —
  out of the time budget, and it would be one more model call this review
  did not need to answer "does the read side work."
- `mcp__hyper-extract__list_templates(include_methods=false)`: returned
  exactly the 40 built-in gallery templates (education, finance, general,
  industry, legal, medicine, tcm) — independent confirmation that none of our
  four templates are registered anywhere the read or write side can see.

**What the read side does, in this project's terms:** it is a query
interface (info/search/ask/export) over a Knowledge Abstract that already
exists on disk — it extracts nothing itself and reads exactly what `he
parse`/`he feed` wrote. With the write side unreachable for our templates,
the read side has nothing of ours to serve; it was only provable against the
`general/set` stand-in.

## Where this could enter the loop, and what it may not do

None of this can enter the loop today — the write side that would produce
project-shaped output is NOT REACHED. If a future session gets a template
loaded (via an upstream fix or the package-directory workaround named
above), the templates' own design already states the limits
(`Plan/concept/hyperextract-templates_2026-09-24.md`), unchanged by anything
found here:

| phase | template | may | may not |
|---|---|---|---|
| 2 · ingest | `TermCensus` | a **second reader**, compared to a person's `03-candidates.md` by name only, after it exists | seed or replace it; supply a count; create a page |
| 3 · reconcile | `LocationRegistry` | machine-check a future gazetteer's own Source column, the way `score_location_registry.py` is built to | decide which places get a page; assign a level |
| — | `TermReadings` | place quotes for a person to read, via `read.py --find` | write a note or settle a stance (decision 004) |
| — | `StatedRelations` | surface relation candidates for a person to keep or reject | become a `[[link]]`; detect a conflict (never mechanised) |

A model's output from any of them is a reading, same standing as an entity
list or a `knowledge-graph-extract` triple: it may not merge two surfaces,
and conflict detection stays a person's job.

## Recommendations

1. **park** — do not wire `TermCensus`/`LocationRegistry`/`TermReadings`/
   `StatedRelations` into the loop yet. Evidence: 8/8 identical, instant,
   code-level failures (`Template.get()` only resolves gallery keys or
   `method/…`, `hyperextract/cli/cli.py:331` and
   `template.py:92,104`), reproduced on both documents. May not: be worked
   around inside this review's sandbox (the fix lives in a shared
   installation `Plan/runs/tooltest/hyperextract/` was not scoped to touch).
   `templates.py check`'s green result did not catch this because it only
   calls `validate`, never `parse`.
2. **trial** — a maintainer or a throwaway venv should try registering one
   template by copying it into the installed package's
   `templates/presets/general/` (or filing/checking for a `he template add`
   in a newer Hyper-Extract release) and re-run this same `TermCensus`
   command once that path exists; only then does scoring against
   `entities.py score` become meaningful for the real template. Evidence:
   `Gallery._load_config` (`gallery.py:100`) scans exactly that directory at
   import. May not: happen inside `Plan/runs/tooltest/hyperextract/`, and
   may not use a paid model or a document outside decision 007.
3. **trial** — keep `score_location_registry.py` (this review's file) for
   that day: it already parses document 6's 51-row master table correctly
   (checked by eye against L185–L235) and needs no gold beyond the document
   itself, which is why the template design page called it the one
   end-to-end-decidable score. Evidence: the script's own output above.
   May not: score anything until a `LocationRegistry` KA exists.
4. **adopt** — nothing. There is no working write-side path today, so no
   recommendation can be adopted; the read side has no project data to serve
   until one exists.
5. **park** — the read side (`he info`/`he search`/`he-mcp`) as a query
   layer over *some other* tool's output. It is fast (2.7s local search,
   7.4s index build on 259 items) and works over the router/local embedder
   exactly as designed, but there is nothing of this project's shape for it
   to serve yet, and building one only to exercise the read side (as this
   review did with `general/set`) produces a reading with no template
   guarantees — not worth keeping as a fixture. Evidence: the `general/set`
   run above. May not: be treated as if it tested `TermCensus`.

## Ledger

`python3 scripts/route.py ledger` at review time: 360 rows total, `hyperextract`
purpose 241 chat + 28 embed calls, all `ok`, 0 refused, 0 unreached, **cost
$0.000000** over 307 priced calls. No paid call was made; no document outside
decision 007's two was sent (the router's own consent guard, not just this
review, enforces that — `scripts/route.py selftest` passed its "declaring a
document outside the consent is refused" case before this run started).
