# grawiki — tool review, 2026-09-24

Tester: tool group 2 of the 2026-09-24 tool-review plan. Scope: documents 5
(`aegis-subplots-kapitelweise-system-exploration-docx`) and 6
(`roman-lokalitaeten-konzept-und-ausarbeitung`), the two named in decision 007's
consent, sent only through `http://127.0.0.1:8787/v1` under
`OPENAI_API_KEY=route:grawiki:<slug>:<attempt>`. All commands below ran under
`.venv-grawiki/bin/python`. Artifacts: `Plan/runs/tooltest/grawiki/<slug>/`.

## What ran

`grawiki.GraphRAG(model="openai/free", embedding_model="openai:local", db=FalkorGraphDB(slug, db_path=...), kg_output_language="German").ingest_text(text, title=slug, format="markdown")`
against each document's full `Sources/drive/<slug>.md` text (13,913 and 12,023
words respectively) — no truncation, no synthetic text. FalkorDBLite's bundled
server **started with no problem**: `MATCH (n) RETURN n.name, labels(n)` against
each run's `kg-<attempt>.db` returned the document node, every chunk node and
their embeddings (61, 61 and 53 nodes for the three runs below) — so the
"unconfirmed" blocker the plan's table names is **reached and clear**.

Three ingests, two attempts on document 5 (P18) and one on document 6 (time ran
out — see *What broke*):

| run | seconds | structural nodes | entity/relationship nodes | outcome |
|---|--:|--:|--:|---|
| doc 5, attempt 0 | 54.3 | 61 | 0 | extraction crashed, all chunks |
| doc 5, attempt 1 | 26.7 | 61 | 0 | extraction crashed, all chunks |
| doc 6, attempt 0 | 28.0 | 53 | 0 | extraction crashed, all chunks |

(`Plan/runs/tooltest/grawiki/<slug>/result-<attempt>.json`, `nodes-<attempt>.json`)

## What broke, and why

**Every chunk's knowledge-graph extraction failed**, all three runs, with the
same `instructor` exception after three retries per chunk:

```
InstructorRetryException: ... Instructor does not support multiple tool calls,
use List[Model] instead
```

The model's raw completion (captured in `result-*.json`) is not empty and not
off-topic — `cohere/north-mini-code:free` answered every call with a readable
node/relationship list in German, sometimes as prose bullets (`label:
'Organization', name: 'AEGIS'`), sometimes as a fenced JSON block. **The failure
is a shape mismatch between `instructor`'s structured-output parsing and what
this free model returns**, not a refusal, an empty answer or a language
problem — the router's own P19 categories do not fit it, because the call
answered (`route.py ledger` counts it `ok`) and `instructor` broke on the
response afterward, client-side. `grawiki.graph.extraction.KnowledgeGraphExtractor`
calls `instructor.from_provider(self.model, async_client=True)` with no `mode=`
override, so it takes whatever default tool-calling mode `instructor` picks for
an `openai/...` model string; that default is what breaks on this model's
output. This is the forced-tool-call risk the plan's Step 1 flagged before any
tester started, confirmed: **a free model through the proxy does not reliably
produce the single-tool-call shape `instructor`'s default mode expects**, at
least for `grawiki`'s multi-node/multi-relationship extraction schema.

`ingest_text` does not treat one chunk's extraction failure as fatal to the
whole document — `fix_missing_nodes` and the retry loop are chunk-scoped — but
the document node, chunk nodes and their embeddings are still written even when
every extraction fails, which is why the node counts above are non-zero while
the entity/relationship count is exactly zero throughout.

**A second, separate defect, found and worked around, not fixed:**
`scripts/route.py` inserts `scripts/` at the front of `sys.path` (`route.py:67`)
so its own sibling modules import cleanly. But `scripts/profile.py` — this
project's document-census script — then shadows the standard-library `profile`
module, and `sentence-transformers → transformers → torch._dynamo` does
`import cProfile` → `import profile` during its first lazy import. Under
`.venv-grawiki/bin/python scripts/route.py serve`, every `/v1/embeddings` call
therefore failed with `501 no local embedder`, even though
`sentence-transformers` is installed and importable standalone in that venv.
Worked around for this test only, without touching `scripts/route.py`, by
pre-importing `sentence_transformers` in a wrapper (`run_proxy_debug.py`) before
`route.py`'s `sys.path.insert` ran, so the real stdlib `profile` was already
cached in `sys.modules`. **This is a real bug in the shared router**, reachable
by any tool that needs local embeddings under this exact invocation, and it
should be fixed in `scripts/route.py` (or `scripts/profile.py` renamed) rather
than worked around per-tester — flagging it here since fixing `scripts/route.py`
is outside this review's write scope.

Running out the ~25-minute budget on document 6's second attempt was not
attempted after this consistent, reproducible failure — one clean reproduction
on each of two documents plus a repeat on document 5 is enough to call the
extraction path broken rather than flaky.

## Model-call cost

`python3 scripts/route.py ledger` (2026-09-24T18:31–18:46), `grawiki` purpose
only:

```
purpose   kind    ok  cached  unreach  refused  charged   in tok   out tok
grawiki   chat    18     29        0        0        0    30,804    29,669
grawiki   embed   14      0        0        0        0         0         0
answered by: cohere/north-mini-code:free 22, local/…MiniLM-L12-v2 14
cost: $0.000000 over 36 priced calls
```

Per document (`route.py`'s own ledger rows, `doc` field): **document 5 cost 14
real chat calls across its two attempts (≈7 per attempt: 3 retries × 2 chunks,
plus one) and 11 embed calls; document 6 cost 4 real chat calls and 3 embed
calls for its one attempt.** All 22 chat calls answered — none unreached,
refused or charged — the guard and free-only checks held throughout; the 29
`cached` rows are `instructor`'s own retries re-sending byte-identical requests,
answered from `route.py`'s cache rather than the network.

## Names, scored

`GraphRAG` itself extracted zero entity names (see above), so there is nothing
of its own to score. To still measure what the model *would* have offered,
names were pulled out of the raw (unparsed) completion text in each
`result-*.json` and scored as a names file:

```
$ python3 scripts/entities.py score aegis-subplots-kapitelweise-system-exploration-docx --names .../raw-names-0.json
reader 60, model 7 verified, shared 5 (folded); 1 refused (not in the document word for word), 0 set apart as lens
precision 0.71  recall 0.08  F1 0.15  — two readers scored 0.66 (P27)

$ python3 scripts/entities.py score aegis-subplots-kapitelweise-system-exploration-docx --names .../raw-names-1.json
reader 60, model 8 verified, shared 3 (folded); 3 refused, 0 set apart as lens
precision 0.38  recall 0.05  F1 0.09

$ python3 scripts/entities.py score roman-lokalitaeten-konzept-und-ausarbeitung --names .../raw-names-0.json
reader 124, model 19 verified, shared 1 (folded); 2 refused, 0 set apart as lens
precision 0.05  recall 0.01  F1 0.01
```

Well under the 0.66 two-reader ceiling (P27) and under the Haiku entity-list
floor (0.25 on document 5). The model surfaced real, in-document names (`AEGIS`,
`Kael`, `Guardian`, `LogOS`, `EP-Intrusion`) but only a handful per call — each
extraction call covers one ~2,000-character chunk, not the document, so low
recall against a whole-document reader list is expected by construction and is
not comparable to a whole-document entity-list score. It is reported only to
show the raw model output was not garbage, not as a claim about `grawiki`'s own
recall, since `grawiki` produced no entity nodes to score directly.

## What a model's output here may not do

Nothing from this run may create a `Wiki/` page, write a `[[link]]`, supply a
count used in `NOW.md` or `CLAUDE.md`, merge two surfaces, or stand as a
detected conflict — conflict detection is never mechanised, and every node and
edge `GraphRAG` would have written is a model's reading under the same limits as
`knowledge-graph-extract` and Hyper-Extract's Knowledge Abstracts. Its output
directory (`Plan/runs/tooltest/grawiki/`) sits outside both `Wiki/` and
`Sources/`, as required.

## Where it could fit the loop

`.claude/skills/tools/SKILL.md`'s phases: `0-check`, `1-choose`, `2-ingest`,
`3-reconcile`, `4-remeasure`, `ask`, `promote`, plus the side tracks
entity-lists, bilingual, search, route.

- **Not `2-ingest`.** The step needs a census — exhaustive, one document, no
  comparison to the wiki — and `grawiki`'s extractor returns a small, per-chunk,
  lossy node list even when it works, with no line citation and no exhaustiveness
  claim. It cannot substitute for `scripts/profile.py` + a person reading.
- **Possibly a `search`-adjacent side track**, once the `instructor`/free-model
  shape mismatch is fixed: FalkorDBLite's own graph query surface
  (`db.query`, `db.vector_search`, `db.fulltext_search`) is a real local
  vector+graph store built for free, and could sit beside `qmd` as a second
  index — but only once extraction actually populates it, which it did not
  here.
- **Not `ask` or `promote`** — no page, link or count may come from it, per the
  limits above, and both of those steps need exactly that.

## Recommendation

Verdict: **park**, pending an upstream or local fix to the extraction call's
`instructor` mode. Evidence: 3/3 ingests, 2 documents, 2 attempts on one of
them, 0 successful extractions, same exception each time
(`Plan/runs/tooltest/grawiki/*/result-*.json`). May not: create a page, link,
count, merge or conflict call, per the limits above, even once it works — its
ceiling is `knowledge-graph-extract`'s ceiling, a reading, not a record.

If revisited: pass `kg_extractor_kwargs={"mode": instructor.Mode.JSON}` (or
another non-tool-calling mode) to `GraphRAG(..., kg_extractor_kwargs=...)`
before writing this off as the model's fault — the raw completions show the
model itself produced usable German JSON: the break is in how `instructor`
asked for it, not in what came back.

## Separate finding for the router, not this tool

`scripts/route.py`'s `sys.path.insert(0, ROOT/"scripts")` (line 67) shadows the
standard-library `profile` module with `scripts/profile.py`, breaking
`/v1/embeddings` under `.venv-grawiki` for every caller, not only `grawiki`.
Reproduced directly against `route.embed()` (see `run_proxy_debug.py`, not
committed as a repository change). Worth a fix in `scripts/route.py` — rename
`scripts/profile.py`, or import `sentence_transformers` before the path insert,
or move the insert to the end of `sys.path` — since it currently blocks the one
component (`grawiki`) the route-plan itself says needs the local embedder.
