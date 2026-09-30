# Kohärenz Protokoll: qmd discovery graph and initialization proposal

**Status: discovery-graph proposal and tested demonstration, with a tool initializer and reader extraction bridge in this PR.**
**2026-09-30.** Unification is explicitly deferred on the author's instruction while the other agents finish. The PR adds initialization, reader/template skills, agents and candidate staging. It leaves source/wiki authoring and production graph schemas unchanged.

Original proposal snapshots (historical; #119 and #123 are now on main):
- main: `afeb0b86a53adf847f9cdb932751f03ddf6dfd15`
- PR #119: `2607576f2339d15f12633f53a7ce08d03535a481`
- PR #120: `f690ebab13f3cc71ba02295dd64d6f01f5316c71`

## Recommendation

Use qmd to populate a **discovery graph**: what was searched, where it returned a candidate passage, under which index snapshot, and which question motivated the search. Keep source-attributed wiki evidence as the existing evidence graph. Extracted relationships become individually attributed proposal records for review.

This gives the reading agent three distinct answers:
1. What has already been read and cited?
2. Where might additional information be found?
3. Which source-specific relation candidates should a reader inspect?

A retrieved passage is not a verified claim. A correctly placed quote proves its words and location; it does not establish that the model's relationship interpretation is correct.

## What exists already

| Capability | Current location | Implication |
|---|---|---|
| Hash-checked GraphQLite projection, atomic replacement, verified evidence IDs | `scripts/kg.py`, `graph-context` skill | Reuse the contract when integration is ready; do not replace it now. |
| Corpus lines, BM25, document catalogue, decision sheets, answer workflow | #119: `askdb.py`, `ask.py` | Let its agents finish; propose interoperability without choosing a winner. |
| qmd JSON adapter | `scripts/qmd.py` | One place to resolve qmd URIs and parse search output. |
| Committed qmd configuration and full local setup | `.qmd/index.yml`, `setup_qmd.sh` | Preserve the configuration; never invoke `qmd init` or overwrite the project's qmd skill. |
| qmd candidate logs for conflicts and chapters | `Plan/runs/qmd-scan-2026-09-26/`, `qmd-chapters-2026-09-26/` | Import these historical candidates before commissioning new expensive searches. |
| HyperExtract project templates and recorded trial | `Plan/hyperextract/`, `tool-review_2026-09-24/hyperextract.md` | Template validation worked; custom-template parsing did not work in the tested installation. |
| Graphify code-only output and KGE validation scripts | `tool-review_2026-09-24/graphify-cgr.md`, `kge-semantica.md` | Useful for operation/code navigation and proposal validation, not a new canon authority. |

The current `kg.py` graph uses `:Core` with `kind` and serialized `payload`, plus `:Evidence`. The #119 store uses different labels. The current-main queries in this pack intentionally target **kg.py's schema**, not askdb.py's schema. Labels are not silently interchangeable.

## One initialization command

Implemented preparation interface (discovery import remains proposed):

```bash
python3 scripts/knowledge.py init --profile full
```

The PR adds `scripts/knowledge.py`: reader/research/full profiles orchestrate existing installers, derived inputs, separate graph stores, qmd update and capability checks. Subagents use `--check` without writes; only the coordinator initializes. Full explicitly runs the existing qmd-models installer. The `reader-tools` skill teaches these commands. The discovery query registry and graph import in phases 5–6 below remain proposed.

| Phase | Action | Gate and resumability |
|---|---|---|
| 1. Tools | Use `install.sh`'s component definitions and pins; the full profile installs the suite, including optional packages. | Per-component success, failure, or unavailable state. No global green bit. |
| 2. qmd | Use `setup_qmd.sh`: package, pinned local models, update, embeddings. | Collections match config; coverage passes; embeddings actually complete. |
| 3. Catalogue | Enumerate authoritative manifests and files, not top-k search results. | Every in-scope original source is addressable; missing and unsupported files reported separately. |
| 4. Existing graphs | `kg.py index/check`; research/full also `askdb.py build/check`, each in its own store. | Independent freshness/check results; no writes across implementations while unification is deferred. |
| 5. Discovery | Import historical hit logs and run the bounded registered-query set for the selected profile. | URI/path resolves, hashes recorded, anchors checked, failures retained. |
| 6. Graph adapter | After the agents finish, import the durable discovery records into the agreed GraphQLite projection. | Native fixture queries and provenance checks pass before publishing the new snapshot. |
| 7. Report | Write the phase result, versions, hashes, missing inputs and capability availability. | Exit nonzero if a capability required by the chosen profile is unavailable; retain completed checkpoints. |

The first full qmd setup includes approximately 2.1 GB of local model downloads according to the repository's setup reference. It can take substantial CPU time. A second run should skip unchanged packages, files, embeddings and query snapshots.

A lightweight reading profile can use the existing session component set, BM25 and the current graph. A full profile additionally prepares semantic retrieval and optional tools. Installation does not constitute a successful extraction trial: a HyperExtract installation can be present while project-template parsing is still unavailable.

Initialization builds catalogue, indexes, documented graph structure and retrieval candidates. It must not imply that every source's semantic relationships have been extracted. Semantic relation extraction remains an explicit, bounded subsequent task; no corpus-wide LLM extraction or third-party call is a hidden init step.

## qmd → graph population contract

Keep an append-only JSONL discovery record as the durable input. Both future store implementations can consume the same record. During the current parallel work, this contract and its fixtures can be developed without touching either database.

Example normalized record:

```json
{
  "version": 1,
  "query_id": "<hash of owner, query text, language and collection>",
  "run_id": "<hash of query, backend configuration and collection snapshot>",
  "owner_id": "sheet:W9",
  "query": "Wann erscheint Juna zum ersten Mal direkt?",
  "collection": "sources",
  "method": "bm25",
  "rank": 1,
  "raw_score": 0.79,
  "qmd_ref": "qmd://sources/<slug>.md",
  "source_id": "doc:<manifest-slug>",
  "source_sha256": "<hash>",
  "line_hint": 152,
  "anchor": {
    "status": "placed",
    "first_line": 150,
    "last_line": 156,
    "text_sha256": "<hash>"
  },
  "index_snapshot": "<collection input fingerprint>",
  "tool_version": "<observed installed version>",
  "freshness": "current"
}
```

Values above are illustrative, not a measured corpus hit.

Required importer behavior:
- Resolve the original file by collection and canonical path. A matching filename stem alone is insufficient: a note, chapter, original source and model answer can share names.
- Deduplicate overlapping collections by canonical file identity. Preserve distinct passages and distinct retrieval runs.
- Treat qmd's line as a hint. Retrieve original file text and use the existing quote/location comparison for final line placement. A snippet with omitted text is not a valid citation.
- Preserve `unplaced`, invalid paths, unknown hashes and parse failures as reported states. Do not turn an adapter exception or invalid JSON into “no results.”
- Historical logs lacking version/config/source hashes remain `historical` or `unknown`; they can guide discovery but cannot be presented as current retrieval or verified evidence.
- An added or deleted document changes the collection snapshot even when existing hit files are unchanged. Rankings depend on the collection, so source hashes alone do not make old search ranks current.
- Cache by query + backend/version/model/config + collection snapshot. Preserve old records; derive the current view.
- Raw BM25 and vector scores are not comparable. Fuse document/passsage rankings in code with an explicit RRF rule, preserving each backend's rank. The example queries display raw audit ranks; they are not a fair combined ranking function.

qmd's internals should remain qmd-owned. Do not write its SQLite tables, copy its embeddings into GraphQLite, or couple the integration to undocumented internal SQL schemas. Use the existing CLI adapter first; a pinned SDK adapter can follow if batching actually reduces overhead.

### What to search during initialization

Populate a finite query registry from things already present:
- existing term surfaces;
- conflict/question records;
- decision-sheet questions;
- existing chapter-question files;
- operation/process questions from explicit documentation.

Keep German queries for original sources and English queries for engineering/process decisions, as the project's qmd skill describes. Name collections explicitly.

Default to cheap BM25. Use vector retrieval for paraphrases, unknown vocabulary, or defined low-coverage cases after embeddings are complete. Full `qmd query` expansion/reranking should be exceptional, budgeted and cached. The repository measured minutes per full reranked query on CPU, so it should not run in an unbounded initialization loop.

## Minimal graph shape

| Node or edge | Meaning |
|---|---|
| `:Core(kind=doc)`, `:Core(kind=term)`, existing conflict/question nodes | Original project entities and records. |
| `:Evidence` with `HAS_EVIDENCE` and `CITED_FROM` | Existing source-attributed quotations. |
| `:SearchRun -[:RAN]-> :SearchQuery` | One immutable retrieval event under a snapshot. |
| `:Sheet -[:HAS_QUERY]-> :SearchQuery` | The explicit question that motivated retrieval. |
| `:SearchQuery -[:P_RETRIEVED]-> :Hit -[:AT_DOC]-> :Core` | A ranked candidate location, not a term-to-term fact. |
| `:Claim -[:SUBJECT]-> :Core`, `OBJECT`, `CITED_FROM` | One source-specific extracted relation proposal with quotation and review status. |
| `:Skill -[:USES_COMMAND]-> :Command` | An explicitly declared tool binding from a maintained registry or verified documentation. |

Add chapter/decision/skill/command nodes only from real existing files or explicit bindings. Do not derive “skill X enforces rule Y” merely from a semantic similarity search. Keep the operation graph separate in queries and ranking from the novel's source graph.

A proposal claim should be keyed by document version, passage, source surface, predicate, object surface and extraction identity. A plain `source|type|target` key can merge away the different sources or quotations that make this project useful.

Do not merge aliases by embedding similarity. Use existing author judgements for canonical identity; otherwise preserve document-scoped surface forms. Record uncertainty, negation or scope where the reading actually needs them. Do not invent a global relation vocabulary or hypergraph layer before representative instances justify it.

Graph algorithms need explicit projections. Running PageRank/Louvain/shortest-path on all evidence, search-hit and operation edges can make retrieval popularity influence supposed factual structure. Evidence serving should use the stated graph's allowed edge types. A discovery path is allowed to explain why a document was suggested, but cannot establish a relationship between novel entities.

## How the existing skills help

| Skill/tool | Use here | Boundary |
|---|---|---|
| qmd | Collection choice, German compound searches, URI resolution, search then bounded get. | Candidate discovery; never counts, completeness or facts from rank. |
| graph-context | Existing evidence lookup, exact IDs, small context, freshness checks. | Run after freezing the independent extraction of a new document. |
| HyperExtract brainstorm + graph-designer | Refine `StatedRelations` from actual passages; choose entity/relation structure. | Schema design, not evidence approval. |
| HyperExtract template-optimizer + yaml-validator | Schema/guideline separation, identifiers, loading and output validation. | A green YAML check must be accompanied by a real parse fixture. |
| HyperExtract TermReadings | Quote-candidate extraction for targeted relation review. | Cannot settle a stance or replace a reading note. |
| HyperExtract LocationRegistry | Documents that genuinely tabulate places. | Preserve that document's table cells; do not infer reality levels. |
| knowledge-graph-extract | Immutable chunk plan, resume manifest, triple structure/domain checks. | Quote placement must be added; its Neo4j/Memgraph DDL must not be imported blindly into GraphQLite. |
| graphify | Small code-only operation graph and dependency browsing. | Its recorded code pass still contained heuristic INFERRED edges; preserve that distinction. |

The historical HyperExtract 0.10.3 review found the CLI file-path lookup broken. Merged PR #123 now provides `scripts/templates.py parse`, extending that lookup without editing the installed package and preserving the template beside the KA. This PR reuses it, adds a native offline factory/feed/schema smoke test, and stages source-hashed candidates. A real-model corpus extraction remains unmeasured; a synthetic smoke pass does not establish template quality.

The current `StatedRelations` template discards questions and hedged possibilities. That is useful for a strict affirmative-relation trial but will not describe every research question in a speculative novel project. Keep discarded possibilities visible as limitations; the added `RelationReadings` passage-list template keeps those source-specific candidates separate, including contrary passages with the same endpoints. Its synthetic fixtures establish schema/merge behavior only.

## Reader workflow and token saving

Two reader modes must be explicit.

**Independent first reading:** read the document using the ingest workflow, freeze its candidate list and note. Do not give it qmd recommendations, existing graph claims or glossary expansions first. Otherwise the “second reader” evaluation and genuine discovery become contaminated.

**Reconciliation or targeted inquiry:** request a small graph context; inspect existing conflicts/questions; ask the discovery graph for candidate passages; read exact source windows; verify quotations; write a proposed reading; let the existing reconciliation process accept or reject it.

An agent should receive IDs, titles, statuses and line ranges before receiving prose. Then fetch only selected windows. Deduplicate overlapping windows; preserve complete quotations. Use a hard byte cap, report omitted candidates and incomplete coverage, and record actual model usage separately. A byte budget is not an exact tokenizer count.

Use named recipes instead of asking a model to generate unrestricted Cypher every turn. The named query runner should bind parameters, cap traversal and output, enforce an engine timeout, and serve a checked snapshot. Arbitrary raw Cypher should be an advanced interface with database-enforced read-only behavior; a string search for “DELETE” is not a read-only security boundary.

## Query pack and verification

The reproducible pack in `Plan/runs/qmd-discovery-graph-proposal-2026-09-30/` contains:
- 12 parameterized Cypher recipes in `queries/`;
- their parameters, schema requirements and expected fixture row counts in `query-catalog.json`;
- `verify_queries.py`, which builds the demonstration graph and runs the real native extension;
- `validation.json`. A demonstration database can be generated by the same script; derived databases are not committed.

Five recipes target the current main schema: verified evidence, source impact, existing conflicts, open questions and shared source readings. Seven require the proposed additions: unread candidates, sheet candidates/prerequisites, attributed relation proposals, skill commands, sheet discovery impact and retrieval audit.

All 12 ran successfully on GraphQLite 0.8.0. Two additional checks confirmed that parallel READS/CITES edges survive and a quoted identifier cannot expand a parameterized selection. This validates syntax and the demonstration result contract, **not** real corpus coverage or retrieval quality. No qmd indexing, model extraction or full pipeline initialization was run.

To reproduce from the repository root in an isolated venv:

```bash
cd Plan/runs/qmd-discovery-graph-proposal-2026-09-30
uv venv .venv-query-demo
uv pip install --python .venv-query-demo/bin/python graphqlite==0.8.0
.venv-query-demo/bin/python verify_queries.py
```

To build another NEW demonstration database:

```bash
.venv-query-demo/bin/python verify_queries.py --db /tmp/new-demo.db
```

The script refuses an existing target. Never point it at a production index. Recipe parameters are supplied through `Graph.query(text, params)`, not by substituting strings into Cypher.

The raw recipe queries displaying mixed retrieval backends show audit ranks. Candidate selection should use a separately tested rank-fusion function; ranks and scores in this synthetic graph have no empirical quality meaning.

## Delivery sequence after the parallel agents finish

1. Freeze a supported source-resolution and snapshot contract for the finished stores.
2. Pilot the included init orchestrator with the finished installers; no model extraction is hidden in init.
3. Add the qmd JSONL normalizer with historical-log, overlapping-collection, invalid-output and changed-collection fixtures.
4. Import discovery records through the chosen graph adapter; ship the named query catalogue and a thin skill.
5. Benchmark current BM25 + graph against the qmd-assisted pack on the existing held-out records. Measure passage recall, distinct source coverage, false/out-of-pack claims, bytes, cold/warm latency and actual model tokens separately.
6. Pilot quote-backed relation extraction on a small approved sample, twice, preserving source-specific differences. Expand only after native validation and human review establish utility.

The included `reader-tools` and `hyperextract-learning` skills and `hyperextract-template-agent` teach offline tests, source-hash staging, semantic review and budgeted learning when reviewed examples exist. No DSPy optimization or corpus quality claim is made.

No unification step is scheduled or performed by this deliverable. It remains pending until the other agents complete their work.

## Sources inspected

Repository links below use the inspected main snapshot:

- [GraphQLite CLI](https://github.com/netzkontrast/kohaerenzprotokoll/blob/afeb0b86a53adf847f9cdb932751f03ddf6dfd15/scripts/kg.py)
- [Graph context skill](https://github.com/netzkontrast/kohaerenzprotokoll/blob/afeb0b86a53adf847f9cdb932751f03ddf6dfd15/.agents/skills/graph-context/SKILL.md)
- [qmd skill](https://github.com/netzkontrast/kohaerenzprotokoll/blob/afeb0b86a53adf847f9cdb932751f03ddf6dfd15/.agents/skills/qmd/SKILL.md)
- [Installer](https://github.com/netzkontrast/kohaerenzprotokoll/blob/afeb0b86a53adf847f9cdb932751f03ddf6dfd15/scripts/install.sh)
- [HyperExtract templates](https://github.com/netzkontrast/kohaerenzprotokoll/blob/afeb0b86a53adf847f9cdb932751f03ddf6dfd15/Plan/concept/hyperextract-templates_2026-09-24.md)
- [HyperExtract trial](https://github.com/netzkontrast/kohaerenzprotokoll/blob/afeb0b86a53adf847f9cdb932751f03ddf6dfd15/Plan/concept/tool-review_2026-09-24/hyperextract.md)
- [Graphify trial](https://github.com/netzkontrast/kohaerenzprotokoll/blob/afeb0b86a53adf847f9cdb932751f03ddf6dfd15/Plan/concept/tool-review_2026-09-24/graphify-cgr.md)
- [KGE trial](https://github.com/netzkontrast/kohaerenzprotokoll/blob/afeb0b86a53adf847f9cdb932751f03ddf6dfd15/Plan/concept/tool-review_2026-09-24/kge-semantica.md)
- [qmd upstream](https://github.com/tobi/qmd/blob/main/README.md)
- [GraphQLite Python API](https://github.com/colliery-io/graphqlite/blob/main/bindings/python/README.md)
- [HyperExtract upstream design guide](https://github.com/yifanfeng97/Hyper-Extract/blob/main/hyperextract/templates/DESIGN_GUIDE.md)

