# Hyper-Extract here — four templates, checked, not yet run

*2026-09-24. Everything below is designed and checked; **nothing has been run on the
corpus.** The run belongs to the tool review (`tool-review-plan_2026-09-24.md`),
under decision 007: documents 5 and 6, free models, through `scripts/route.py`.*

The author asked the template optimizer for a Hyper-Extract plan for this
project. There were no templates to optimise, so the skill chain ran from the
start — brainstorm → design → optimise → validate — and the optimiser's report is
below. Each template copies the shape of something the repository already holds
(P3, P4), so its output can be scored by code against a person's work rather than
admired.

## Brainstorm — what earns a template, and what does not

| need | the instance it mirrors | type | |
|---|---|---|---|
| every term of one document | a reader's `03-candidates.md` (genuine for documents 5 and 6) and the entity lists' kinds | `set` | **built** — `TermCensus` |
| the places a document tabulates | document 6's own master table, L185: *Location Name, Reality Level, Source, Narrative Relevance/Function, Key Associated Characters* | `set` | **built** — `LocationRegistry` |
| what a document says about a term | the notes, whose readings each cite their line | `list` | **built** — `TermReadings` |
| relations a document states | nothing — the wiki's `[[links]]` are untyped | `graph` | **built as a trial** — `StatedRelations`, so the graph tools are compared on equal terms |
| the questions a document asks | code already finds a question mark (P1) | — | not built |
| a timeline of chapters or plot | the novel rests; the plot outlines are deferred | — | not built |
| a hypergraph of anything | no instance asks for one | — | not built |
| any `llm_*` merge strategy | two readings merged into one delete what the wiki exists for (P13) | — | never |

## The four templates — `Plan/hyperextract/`

Each file's header carries the three lines `CLAUDE.md` asks of a new construct:
`provisional`, what it **may not** do, and what would **retire** it.

| template | fields | scored by code against | may not |
|---|---|---|---|
| `TermCensus` | `term`, `type`, `scope` (world / lens) | the reader's `03-candidates.md`, through `entities.py score --names`, `world` only; `lens` counted apart | seed or replace a reader's list, create a page, supply a count, merge two surfaces |
| `LocationRegistry` | `name`, `level`, `source`, `function`, `characters` | **the document's own master table**: which rows came back, and whether each `source` is the table's cell character for character | create a page, decide which places get one, assign a level |
| `TermReadings` | `term`, `quote`, `stance` | the note's cited lines: each `quote` placed by `read.py --find`, refused quotes counted (paraphrase, P12) | write a note, reading or page; merge readings; settle a stance for the record |
| `StatedRelations` | entities `name`, `type`; relations `source`, `target`, `type`, `quote` | nothing yet — each `quote` placed by `read.py --find`, then a person keeps or rejects | become a `[[link]]`; detect a conflict |

**No field carries a line.** Names and quotes go in, lines come from code (P26) —
the rule revision 3 of the entity lists paid for. **No template names a term of the
corpus**: a guideline is sent with every document, so a corpus example would carry
one document's knowledge into another's census, which `Plan/briefings/extract.md`
forbids. The rules carry procedural knowledge only — export escaping, glued
reference numbers, what is not a term.

`LocationRegistry` is the one template whose gold is decidable end to end: the
document's own table is the answer key, so scoring it needs no person and no
model. It is also the only one tied to a document shape — it applies to a
document that tabulates places, and retires if the next such document does not fit
its five columns.

## Optimisation report

### Changes made

| file | issue | fix | level |
|---|---|---|---|
| `TermReadings.yaml` | the stance values were defined in the guideline — schema content in a rule | definitions moved into the field's description; the guideline now says *how*: judge the passage alone, never from elsewhere in the document | auto-fix |
| `TermCensus.yaml` | field `register` shadows a pydantic `BaseModel` attribute. **`he template validate` passes it**; loading warns | renamed `scope` | auto-fix, found by loading |
| all set and graph templates | the default merge strategy, `keep_incoming`, lets a later chunk silently overwrite an earlier one | explicit `merge_field` (fills empty fields, no model) or `keep_existing` | auto-fix |
| `TermCensus.yaml` | export damage covered escaping and emphasis only | glued reference numbers added — and *keep the number when unsure*, because names here end in digits and the entity lists once lost the `2` of `KW2` to exactly this rule | suggest, applied |
| `StatedRelations.yaml` | `quote` is described as verbatim in the schema and again in a rule | kept: the rule adds a creation condition — no exact copy, no relation — not a definition | suggest, no change |
| `LocationRegistry.yaml` | five fields, at the limit | kept: they are the document's own five columns | suggest, no change |
| all | English fields contain German tokens (`Wort\-Teil`, `Begriff`) | kept: they are the data the escaping rule is about, and no token is a corpus name (checked) | review |

**Summary:** auto-fix 3 · suggestions 3, one applied · manual review 1, plus the
author decisions at the end.

**One finding that looked like a defect and was not.** The first rendering of a
template showed its rules as a Python list literal, with the escaping example
doubled to `Wort\\-Teil`. That was the test calling the parser without
`localize_template`, which `he parse` always runs first; rendered properly, the
rules are numbered lines with a single backslash. Recorded so that nobody „fixes"
the templates for it.

### The rules the skill does not know, and the check that holds them

`python3 scripts/templates.py check` runs seven checks per template and reports
each on its own (P11): Hyper-Extract's `validate`; `load`, which renders the
template the way `he parse` does and fails on any warning; and five project
rules — `no-line` (P26), `no-llm-merge` (P13), `merge-set`, `provisional`, and
`procedural`, which searches the text a model is sent for every wiki surface and
verified entity name and says which ones it cannot check (P23: the two of two
characters or fewer). **All four templates pass all seven.**
`python3 scripts/templates.py selftest` shows each check failing on the defect it
exists for, and the clean fixture passing `validate` and `load` — the second half
was added after the first `check` failed every good template: the self-test had
proved each check could fail and never that it could pass.

## How they run — next session, under decision 007

```bash
.venv-grawiki/bin/python scripts/route.py serve --port 8787 &     # free models + local embeddings
export TIKTOKEN_CACHE_DIR=$PWD/.venv-dspytools/lib/python3.12/site-packages/litellm/litellm_core_utils/tokenizers
he config llm      -p openai -u http://127.0.0.1:8787/v1 -k route:hyperextract:<slug>:<attempt> -m free
he config embedder -p openai -u http://127.0.0.1:8787/v1 -k route:hyperextract:<slug> -m local
he parse Sources/drive/<slug>.md -t Plan/hyperextract/TermCensus.yaml -l en \
    -o Plan/runs/tooltest/hyperextract/<slug>/TermCensus --source <slug> --no-index
```

**Correction, measured by the tool review the same day: this command does not
run.** `he parse` resolves `-t` with `Template.get()` (`hyperextract/cli/cli.py:332`)
and exits when no gallery template has that name; the branch that copies a
`.yaml` file into the output folder (`cli.py:394`) comes after that exit and is
never reached. This page first said `-t` takes a file path, from reading that
later branch alone. Only `he template validate` takes a path. So the four
templates have not run; running them needs them copied into the installed
package's `templates/presets/<domain>/`, where the gallery finds them —
`tool-review_2026-09-24/hyperextract.md` has the detail.

`he config` writes `~/.he/config.toml` globally, so the key — which names the
document for the router's consent check — is set again per document and per
attempt (P18: two attempts, since `route.py` replays an identical call from its
record). Read from the installed code since this page was first written: `openai`
and `vllm` are both safe providers, and `anthropic` or `google` would ignore the
base URL; **every `he parse` loads tiktoken's `cl100k_base` even with
`--no-index`**, because the embedder is always built — the `TIKTOKEN_CACHE_DIR`
line serves a copy whose hash matches instead of downloading it; and a model name
like `gpt-5.6-sol` or anything `*-pro` would send langchain to `/v1/responses`,
which the proxy does not serve — hence `-m free`. **Still unmeasured:** whether a
free model answers the forced tool call Hyper-Extract sends for each chunk.

## Where they could enter the loop — for the tool review's synthesis to judge

| phase (`.claude/skills/tools/SKILL.md`) | template | how, and the limit |
|---|---|---|
| 2 · ingest | `TermCensus`, `TermReadings` | a **second reader** after the person's `03` and note exist — the two P27 difference lists by name. Never before: counting first decides what gets seen |
| 3 · reconcile | `LocationRegistry` | document 6's page rule rested on the Source column; for the next document that tabulates places, the column becomes machine-readable and the rule code-checkable |
| side track: entity lists | `TermCensus` | the same job as the Haiku reader workflow, on a free model — compared at equal gold, with the ledger's cost beside it |
| `ask` (does not exist) | `TermReadings` | passages retrieved by term, each placed by `read.py --find` — one candidate shape for a cited answer. Not built: a command waits for two hand-done instances |

## Open for the author — judgement, not measurement (P0)

1. **`scope` (world / lens)** rests on one instance: document 6's note, which names
   the two registers. Worth carrying as a field, or kept as a check the scorer
   runs?
2. **A model's stance label** would only order what a person reads first — but
   decision 004 gives stance to the person, per passage. May a model's label be
   used even for ordering?
3. **`StatedRelations` has no gold.** A person's keep-or-reject pass over its
   relations would be the first instance. Worth the time?
4. **The rules restate** parts of `Plan/briefings/extract.md` and the entity-lists
   prompt (P6). Acceptable while the templates are provisional, or should one be
   generated from the other?
