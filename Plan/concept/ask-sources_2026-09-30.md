# `ask` — asking the source documents a question, without vectors

**2026-09-30 · Proposal. Nothing is built.** On the author's request: a way to ask the corpus a question without qmd's vectors — a Sonnet agent given only the context useful for this one question (built from the graph), an excerpt of the skills that apply, and the question; the same package usable by Jules or a free OpenRouter model. Reading done for this note: `scripts/graphrag.py`, `route.py`, `lmrun.py`, `claude_lm.py`, `jules.py`, `quotes.py`, `read.py`, `digest.py`, `entities.py`, `qmd.py`, `lint_readings.py`, `.claude/agents/wiki-reader.md`, decisions 007, 011, 014, 015, and `PRINCIPLES.md`. No source document was read.

## 1. What exists, and the gap

The process diagram in `CLAUDE.md` ends with `ask`. Its retrieval half exists: `graphrag.py ask` seeds by folded surfaces, spreads by PageRank over the typed graph and returns verified quotations, the conflicts and questions that touch them, and the documents the rank reached — never prose. `--answer` lets a model pick evidence **numbers**. What it cannot do:

- **It only knows reconciled documents.** The graph holds the 51 reconciled ones (`state.py --get documents.reconciled`, measured 2026-09-30). The other 535 of 586 landed documents are reachable only through qmd, entity lists or a count.
- **It returns quotations from wiki pages,** not the document text around them. A question the wiki has not already quoted an answer to gets nothing.
- **Its one model step is tied to `lmrun`,** so Claude CLI and free models, but not a session subagent or Jules.

So the gap is: a **context package** that reaches unread documents, a **backend-neutral** answer contract, and a **verification** that holds any backend to the rules the wiki keeps.

## 2. Principles this must keep

| rule | what it means here |
|---|---|
| P13 no merge, P12 quote | an answer is claims, each attributed to one document and carrying its own verbatim quotation |
| P26 ask for an identifier | the model may write a line number only as a hint; code places or rejects every quotation |
| P15 reached ≠ answered | `answered`, `refused`, `unparsed`, `unreachable` — never a score in place of a status |
| P5, P18 | every run keeps its artifacts and replays offline; one attempt measures nothing |
| P1, P6 | pack building, verification and rendering are code; one encoding of each rule |
| decision 006 | an answer is a reading of sources, never a decision; it never enters `Wiki/` by itself |
| decision 007, 014, 011 | Claude is first party. OpenRouter and Jules receive corpus text only under the author's consent, and `route.py` and `jules.py` already refuse otherwise |

**An answer has the standing of an entity list**: a model's reading, recorded, verified by code, usable to point at a place, never a count, a page, a link or a merge.

## 3. The architecture

```
question ──► 1 route (code) ──► 2 pack (code) ──► 3 backend ──► 4 verify (code) ──► 5 record
             graph · entities ·   rules card ·       claude-cli     place every quote     Plan/runs/ask/<id>/
             qmd BM25 · counts    graph excerpt ·    session agent  drop unsupported     answer.md rendered
                                  source windows ·   route (free)   lint comparisons     by code
                                  skill excerpt ·    jules          status per claim
                                  schema
```

### 3.1 Route — which documents and which places (code)

Four finders, each a place to look, none a number (the qmd rule):

1. **Graph** — `graphrag.retrieve()`: ranked pages, their verified quotations with document and line, the conflicts and questions touching them, the documents the rank reached.
2. **Entities** — `entities.py search` on the seed names: unread documents that name them, with the first line.
3. **qmd BM25** — `qmd.py search`, collection `sources`, `search` only (never `query` or `vsearch`): hits with document and line. The index must be current (`qmd update`, 30 s).
4. **Counts** — `read.py --count` or `corpus.py` when the question is a count, answered by code before any model.

The router merges the four into a ranked list of **(document, line)** anchors. Ranking is plain and printed: graph evidence first, then documents reached by two finders, then one. A question the router answers with a count stops here.

### 3.2 Pack — the only context the model sees (code)

One file, `Plan/runs/ask/<id>/pack.md`, and its manifest `pack.json`. The pack is identical for every backend, so their answers are comparable.

| part | content | from |
|---|---|---|
| A. Question | verbatim, plus `kind`: `locate`, `position`, `compare` or `explain` (the asker names it; no classifier) | the caller |
| B. Rules card | about 30 fixed lines: answer only from the pack, one claim one document, quote verbatim in „…", one quotation one passage, say „nicht im Paket" rather than guess, never compare two documents without quoting both, German quotations stay German | a constant in `ask.py` |
| C. Graph excerpt | for the top pages, `digest.py`'s lead and `## Where the sources differ`; the records touching them, position table only; the MMR-selected verified quotations with `slug:Lnn` | `graphrag.retrieve`, `digest.py` |
| D. Source windows | for each anchor, the document lines around it, **numbered as `read.py` numbers them**, ±N lines, windows of one document merged | `read.numbered` |
| E. Skill excerpt | the one or two skills whose description best overlaps the question, description plus one named section | §3.3 |
| F. Output schema | the JSON the model must return | a constant |

`pack.json` records every part's size, the documents whose text is in D (**`sends_text_of`** — what consent is checked against), the finders that produced each anchor, the budget and the hash of the pack. A budget (characters, default to be measured in phase 1) cuts D from the lowest-ranked anchor up, and the manifest says what was cut.

### 3.3 Skill excerpt (code, provisional)

The asker wants „an excerpt of useful skills for the task". Two parts, both deterministic:

- **Selection:** fold-token overlap between the question and each `SKILL.md` description — the block `dspy_skills.generate_skills_prompt_block` already renders from the same field (`rlm_ingest.py`). Top one or two, and only above a floor.
- **Excerpt:** a named section per skill, listed in a small table in `ask.py`. It starts with the three that have a use today: `writing-skills` (what counts as canon), `dramatica-vocabulary` (glossary lines for a named term), `ingest` (quoting rules, already in the rules card, so usually none).

Provisional under P4: the table grows only when a question needed a skill it lacked. It retires if bench answers do not differ with and without it (measured in phase 3).

### 3.4 Backends — one contract, four doors

Each backend takes `pack.md` and returns `answer.json` in the schema below, or a status.

| backend | how | isolation | who may run it |
|---|---|---|---|
| **claude-cli** (default) | `lmrun.call` with `make_lm("claude-cli/sonnet")`: `claude -p`, no tools, no MCP, empty working directory | **enforced**: the model sees the pack and nothing else | first party (decision 011); scriptable and parallel |
| **session** | the session spawns a subagent `.claude/agents/source-asker.md` (Sonnet, `tools: Read`), told to read only `pack.md` and write `answer.json` | by instruction only: `Read` can open other files | first party; for interactive use |
| **route** | `route.chat` with the pack as prompt, `purpose=ask`, `doc` = the first of `sends_text_of` | none needed — `route.screen` refuses any request holding twelve words of a document outside `consent.json` | **today only packs whose `sends_text_of` lies inside decision 007's two documents**; any wider use needs the author's consent |
| **jules** | the pack is committed to a branch; `jules.dispatch` with a prompt „read only `Plan/runs/ask/<id>/pack.md`, write `answer.json`, submit"; `jules.verify` and `patch` collect it | none: a Jules session holds the whole repository, corpus included | **only with `--approval` naming an author decision**; decision 014 covered one ingest, not this |

Only claude-cli can promise „only this context". The other three are useful for comparison or scale, and their answers pass the same verification.

### 3.5 The answer contract

```json
{
  "answerable": "yes | partly | no",
  "claims": [
    { "doc": "<slug>", "says": "<one sentence, the model's words>",
      "quotes": [ { "text": "<verbatim>", "line_hint": 123 } ] }
  ],
  "differ": [ "<slug-a> vs <slug-b>: <what differs>" ],
  "gaps": [ "<what the pack does not hold>" ],
  "next": [ { "doc": "<slug>", "why": "<one line>" } ]
}
```

A claim is about one document. „Sources differ" is only a line in `differ`, and only when both documents have a verified claim.

### 3.6 Verify and render (code)

For every quotation, in order:

1. The document must be **in the pack**. A quotation of a document the pack did not contain is `outside-pack` — the model knew it from somewhere else, or invented it.
2. `quotes.verdict` against `line_hint`; if that fails, `read.locate` finds the line. Found once: placed. Found on several lines: the one nearest the hint. Not found: `unresolved`.
3. A claim keeps only placed quotations. A claim with none is `unsupported` and is printed apart, never mixed with supported ones.
4. `lint_readings.lint_lines` over `says` and `differ`: a comparison without both documents quoted is flagged.
5. `differ` lines survive only when both documents have a supported claim.

`answer.md` is rendered by code: supported claims grouped by document, in the documents' date order, each quotation with `^[slug.md:Lnn]` — so `quotes.py` can check the file like any other. Then `differ`, `gaps`, `next`, the unsupported claims last and labelled, and a footer: backend, model, pack hash, status counts, cost.

### 3.7 Record

`Plan/runs/ask/<id>/` holds `question.txt`, `pack.md`, `pack.json`, `raw.<backend>.json` (the model's reply as received), `answer.json`, `answer.md`, and one line in `Plan/runs/ask/ledger.jsonl`. `<id>` is date plus a short hash of the question. `ask.py replay <id>` re-renders from the stored raw reply with no model.

## 4. How it is judged

**Gold from the records, with the known caveat.** Each conflict and question record lists positions per document with lines. The record's own question becomes the bench question, and the record is **removed from the graph and the pack first**, as `graphrag.py bench` removes it. The caveat is `graphrag`'s: the same hand wrote question and label.

Measured per run, never folded into one number (P11):

- **pack recall** — share of the record's (document, line) positions that fall inside the pack's windows (phase 1, no model);
- **placed rate** — placed quotations over all quotations;
- **document recall and precision** — documents with a supported claim against the record's documents;
- **outside-pack rate** — should be 0;
- **calibration** — `answerable: no` on questions the pack cannot answer (a few cases built to be unanswerable).

Every model case runs twice (P18). A second Claude run is the ceiling to compare other backends against (P27), and it is the same model family, so it measures stability, not truth. `baseline.py` records the numbers.

## 5. Implementation plan

Each phase ends with a gate (P22). Nothing in a later phase starts before the gate before it.

| phase | builds | gate |
|---|---|---|
| **0. Decide** | the author answers §6 | answers recorded in a decision file |
| **1. Route and pack** (code only) | `scripts/ask.py route`, `pack`; `selftest` with a fixture corpus; `bench --pack` over the records | pack recall measured on all record cases; budget chosen from it; `selftests.py` holds |
| **2. Verify and render** (code only) | `ask.py verify`, `render`, `replay`; fixture answers from `lm_fixture` carrying each defect: wrong words, wrong line, outside pack, a claim with no quotation, a comparison without both quotes | each fixture defect named by its own check (the `selftest.py` pattern) |
| **3. Claude CLI** | `ask.py run --backend claude-cli` through `lmrun.call`; 8 record cases × 2 runs on Sonnet; with and without the skill excerpt | placed rate, recall, outside-pack and cost recorded in `baselines.jsonl`; the author sees two rendered answers before phase 4 |
| **4. Session agent** | `.claude/agents/source-asker.md` (`tools: Read`); `ask.py collect <id>` reads the answer file it writes | same bench, compared with phase 3 |
| **5. Free models** | `--backend route` | only after the author's consent covers what a pack sends; P19 language check; compared with phase 3 |
| **6. Jules** | `--backend jules`, asynchronous: `run` dispatches, `collect` verifies and patches | only with an approval naming an author decision; one case first |
| **7. Use** | the cross-read before a decision round asks W12 and W15's preparing questions through `ask`; the chapter pages' question lists become bench material | a round prepared with it; its answers checked by the author |

**Reused, not rewritten:** `graphrag.retrieve`, `digest`, `read.numbered` and `read.locate`, `quotes.verdict`, `entities` search, `qmd.search`, `lint_readings.lint_lines`, `lmrun.call` and `make_lm`, `claude_lm`, `route.chat` and its guard, `jules.dispatch`, `verify` and `patch`, `lm_fixture`, `baseline.py`. **New:** `scripts/ask.py` (route, pack, run, verify, render, replay, bench, selftest), `.claude/agents/source-asker.md`, and a line in `selftests.py`.

## 6. Questions for the author

1. **Free models:** may a pack go to OpenRouter's free models (data collection denied), and for which documents: none beyond decision 007, the read 51, or any landed document?
2. **Jules:** may `ask` dispatch Jules sessions, each holding the whole repository, and with what limit (per question with your yes, or a standing budget)?
3. **Default backend:** claude-cli with Sonnet, as proposed?
4. **Where an answer may be used:** only as a place to look (like an entity list), or may a reader quote a verified answer's quotations onto a page, going through the normal reading step?

## 7. What this cannot do

- It finds what the four finders reach. A passage no graph edge, entity, BM25 hit or count points at is not in the pack, and `answerable: no` is then the right answer, not a failure.
- BM25 on German misses compounds and inflection (`.claude/skills/qmd`); a question in the wrong word form finds less.
- A verified quotation proves the words stand on the line, not that the claim built on them reads them correctly. The claim is still a model's reading.
- Only claude-cli enforces the context limit. The session agent and Jules are held to it by instruction.
