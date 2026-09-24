# Tool review, cost-routed — the plan the next session executes

*Written 2026-09-24 as a handover; approved by the author. Delete or mark done
when the workflow has run — this page describes work that has not happened yet.*

## The request

The author, 2026-09-24: *develop a workflow with a cost optimizer (OpenRouter and
Jev) that tests all the freshly installed tools, and write reviews of what we
could implement in the repository's main workflows.* Then: *next session.*

Four author answers bind it (asked, not assumed — P0):

| question | answer |
|---|---|
| which text may leave | two documents already in the wiki → **documents 5 and 6** (decision 006 says why these two) |
| budget | **free OpenRouter models only**; Jev per call |
| checkpoint | **straight through** once the router passes its selftest and one real call; the author reviews on PR #58 |
| Notion | reviews stay **in the repository**; Notion is tested read-only |

Tools under test, all installed 2026-09-24: Notion MCP + the four Notion skills,
`knowledge-graph-extract`, `graphify`, `cgr` (code-graph-rag), `grawiki`,
`semantica`, Hyper-Extract (`he`, `he-mcp`, seven skills), OpenCode +
oh-my-openagent, `install.sh` + the session hook; `jev-decide` as the judge.

## Done

- **Decision 006** and `Plan/runs/route/consent.json`, its one machine encoding.
- **`scripts/route.py`**, the cost router — free only (listed price 0, and a
  charged call stops the run), consent (a declared document outside it, or twelve
  consecutive words of any landed document outside it, is refused before
  sending), recorded (cache + ledger + `--replay`), an OpenAI-compatible proxy for
  third-party tools (API key `route:<purpose>:<doc>[:<attempt>]`, any requested
  model answered by a free one, SSE, local embeddings), and a Jev wrapper with JSON
  question specs. **`selftest`: 25 cases hold**, offline, no key, no network —
  run it under `.venv-typesafe/bin/python` for the Jev case.

Measured on 2026-09-24, before the router existed: under
`provider.data_collection = "deny"` six free chat models answered
(cohere/north-mini-code, dots-3-note-preview, ling-3.0-flash-fin and -sante,
nex-n2.5-mini and -pro); four were rate-limited (gemma-4 ×2, qwen3.8-27b,
glm-5.2); the nvidia, poolside and liquid free models refused the policy with a
404. **No free embedding model accepted the policy**, so embeddings are local:
`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` in `.venv-grawiki`
(384 dimensions, about 60 s to load the first time). A reasoning model returned
`content: None` on a small token budget — P19 is live, and the router treats it
as a defect.

## Step 1 — the router, against the world

```bash
python3 scripts/route.py models                    # writes Plan/runs/route/models.json
python3 scripts/route.py guard roman-lokalitaeten-konzept-und-ausarbeitung   # may be sent
python3 scripts/route.py guard entropie-aegis      # must be refused
echo "<a short German instruction about doc 6>" | \
  python3 scripts/route.py complete --purpose smoke --doc roman-lokalitaeten-konzept-und-ausarbeitung --expect de
python3 scripts/route.py ledger                    # cost $0.000000, 0 charged
```

## Step 2 — one scorer for every tool

Add `score <slug> --names <file.json>` to `scripts/entities.py`: the names file has
the shape of `Plan/entities/names/<slug>.json`; each name is placed and verified
in memory with the existing `place()` / `first_line()` / `holds()`, folded with
`wiki_index.fold`, and compared with the reader's `03-candidates.md` exactly as
`cmd_score` does — both difference lists by name, P/R/F1, and the 0.66 ceiling
(P27). Names the document does not contain word for word are reported as refused,
which is also what catches a translated name (P19).

**Proof before use:** scored through the new path, the existing Haiku lists must
reproduce their current numbers — F1 0.25 on document 5, 0.69 on document 6.

## Step 3 — the workflow, `.claude/workflows/tool-review.js`

Start the proxy first, under the interpreter that has the embedder:

```bash
.venv-grawiki/bin/python scripts/route.py serve --port 8787    # background
```

Pass `args = {date, port: 8787, docs: [doc 5, doc 6]}` — a workflow script may
not call `Date.now()`.

**Cost tiers.** Code for everything decidable (scoring, validation, the ledger).
Free OpenRouter models through the proxy for every extraction a tool does. Jev
for the one judgement stage. Sonnet testers (`model: 'sonnet'`, `effort:
'medium'`). The synthesis on the session model. At most ten agents.

**Phase Test** — `pipeline()` over eight tool groups, one tester each. Every
tester: documents 5 and 6 only; every model call through the proxy or
`route.py`; writes only under `Plan/runs/tooltest/<tool>/`; never `Wiki/`,
`Sources/` or Notion; at least two attempts wherever a model is involved (P18,
the `attempt` key part); a tool that cannot be reached is **not reached**, never
failed (P15); names scored with `entities.py score --names`; its review written
to `Plan/concept/tool-review_<date>/<tool>.md`.

| # | tool group | what the tester runs |
|---|---|---|
| 1 | knowledge-graph-extract + semantica | free-model extraction in the skill's format → `validate_triples.py`, `generate_cypher.py`; load the triples into semantica with provenance and test its dedup and conflict API; score subjects and objects |
| 2 | grawiki | ingest documents 5 and 6 into FalkorDBLite through the proxy; score its entities |
| 3 | Hyper-Extract | a template designed with the `hyperextract-*` skills (a gazetteer for 6, a brief for 5); `he parse` through the proxy (LLM and local embedder); `he-mcp` info, search, export; score |
| 4 | graphify + cgr | the AST graph of `scripts/` with no model; graphify's document mode on 5 and 6 through the proxy if its backend honours a base URL; `cgr index` and `cgr check` on `scripts/` |
| 5 | Jev | the **26** near-match judgements in `Plan/runs/judgements.jsonl` whose `document` is 5 or 6 (12 one-term, 7 two-terms, 5 judgement, 2 not-a-term) as the typesafe skill's entity-alignment shape — a three-level Score *one term / related, a person decides / two terms*, plus a Noul for not-a-term; agreement per class, both difference lists; `judgement` rows map to the middle level |
| 6 | OpenCode + oh-my-openagent | a custom OpenAI-compatible provider pointed at the proxy — **not** the built-in `openrouter` provider, which would bypass the guard; `opencode run` on a non-corpus task; does the plugin's routing override `--model`? |
| 7 | Notion MCP + Notion skills | read-only; no corpus text; the skills judged on paper against how `NOW.md` and the decisions are kept |
| 8 | install.sh + session hook | `--check`, one component's reinstall timed; review only |

Configuration already confirmed: Hyper-Extract takes any OpenAI-compatible
endpoint through its vLLM provider — `he config llm -p vllm -u
http://127.0.0.1:8787/v1 -k route:hyperextract:<doc> -m <any>`, and the same for
`he config embedder` — and writes `~/.he/config.toml`, which then holds no real
key. graphify parses code with tree-sitter and no model; whether its `openai`
backend honours a base URL is unconfirmed. `cgr index` and `cgr check` need no
model. grawiki uses pydantic-ai, whose OpenAI provider takes a `base_url`.

**Tester output** (schema): `tool`, `reached` (yes / partial / no), `runs`
(document, command, outcome, seconds), `scores` (document, gold, model, shared,
P, R, F1, refused), `ledger_purpose`, `artifacts`, `review_path`, and
`recommendations` — each with `step`, `proposal`, `evidence`, `may_not`,
`effort` and a verdict of adopt / trial / park. `step` is a phase of the loop as
`.claude/skills/tools/SKILL.md` names it: `0-check`, `1-choose`, `2-ingest` (the
`03` list is a person's; a tool may only be a **second reader** for a P27
comparison, never seed it), `3-reconcile`, `4-remeasure`, `ask`, `promote`, or a
side track — `entity-lists`, `bilingual`, `search`, `route`.

**Phase Check** — one Haiku agent (`effort: 'low'`) over all recommendations;
the barrier is justified because it needs them all. Per recommendation one Jev
Score through `route.py jev`: *is this proposal supported by the evidence it
cites?* — supported / partly / not. Nothing is dropped by code; the score stands
beside the proposal.

**Phase Synthesize** — one agent on the session model reads every review, the
scores and `route.py ledger`, and writes `Plan/concept/tool-review_<date>.md`:
per step of the loop, what could be implemented, with its evidence, its cost, and
the `CLAUDE.md` limit it must respect — a model's reading supplies no page, link
or count; conflict detection is never mechanised; names in, lines by code (P26).
It must answer the tools skill's *What is missing* list directly: can any tool
close „phase 1 is not automated", „`ask` does not exist", „extraction is not
trainable — one usable gold list"?

## Step 4 — document and commit

- `CLAUDE.md`: a short section on `route.py` — what it is, its three guards, its
  commands — and the `tool-review` workflow beside `entity-lists`.
- `NOW.md`: the open decisions the reviews raise, with no count lacking a marker.
- Check `du -sh Plan/runs/route/calls` before committing the recordings
  (`bilingual.py`'s are committed: 1,114 files, 5.1 MB), then commit, push, and
  update PR #58.

## Done when

- `route.py selftest` holds; `route.py ledger` shows `$0.000000` and 0 charged,
  with unpriced Jev rows listed apart; exit 0.
- One tool, rerun through `serve --replay` with `ROUTE_REPLAY=1`, reproduces its
  output with no network (P5).
- The new scoring path reproduces 0.25 and 0.69 on the Haiku lists.
- `state.py --prose`, `scripts/selftest.py`, `entities.py selftest` and
  `qmd_coverage.py` stay green; nothing under `Wiki/` or `Sources/` changed.
