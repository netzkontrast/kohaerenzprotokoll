# `ask` — asking the source documents a question, without vectors, on GraphQLite

**2026-09-30 · Proposal. Nothing is built but a throwaway spike.** On the author's requests: a way to ask the corpus a question without qmd's vectors — a Sonnet agent given only the context useful for this one question (built from graph knowledge), an excerpt of the skills that apply, and the question; the same package usable by Jules or a free OpenRouter model — and **„Use https://github.com/colliery-io/graphqlite intensivly in your Architecture"**.

Reading done for this note: `scripts/graphrag.py`, `graph.py`, `route.py`, `lmrun.py`, `claude_lm.py`, `jules.py`, `quotes.py`, `read.py`, `digest.py`, `entities.py`, `qmd.py`, `lint_readings.py`, `.claude/agents/wiki-reader.md`, decisions 007, 011, 014, 015, 016, `PRINCIPLES.md`, and GraphQLite's README, Python binding README and `examples/llm-graphrag`. No source document was read.

## 0. What GraphQLite is, and what the spike measured

GraphQLite (MIT, v0.8.0 on PyPI) is an SQLite extension: a property graph inside an ordinary SQLite file, queried in Cypher (openCypher TCK 97.7 % by its own README), with algorithms built in — PageRank and **personalized PageRank**, Louvain, label propagation, betweenness, closeness, degree, Dijkstra and A\*, BFS and DFS, connected components, Jaccard similarity, triangle counts. Because it is SQLite, the same file can hold **FTS5 full-text tables with `bm25()`** — keyword retrieval with no vectors and no qmd.

Spike, 2026-09-30, in a throwaway venv (`graphqlite` 0.8.0, Python 3.12; the dry run into `.venv-dspy` resolves too), scratch files only:

| step | result |
|---|---|
| `graph.py --json` loaded as nodes and typed edges, one upsert per row | 181 nodes, 4,418 edges, **26 s** (the batch API is untested and should be faster) |
| Cypher: conflicts by number of contested pages | correct rows, instant |
| `personalizedPageRank` seeded on `term:juna`, `term:aegis` | ranked list, **0.17 s** |
| FTS5 over every non-empty line of the 586 landed documents | **125,620 rows in 2.7 s**; file 53 MB |
| `Juna AND erscheint`, ranked by `bm25()` | five hits with slug and line in **2 ms**, the outline's Kap-38 line among them |

What the spike did not test: batch upserts, Louvain and paths on this graph, German stemming (FTS5's `unicode61` tokenizer does not stem; inflected forms need a prefix query or a trigram table).

## 1. The gap

The process diagram in `CLAUDE.md` ends with `ask`. `graphrag.py ask` is its retrieval half: seeds by folded surfaces, personalized PageRank over the typed graph, verified quotations out, never prose. What it cannot do:

- **It only knows reconciled documents.** The graph holds the 51 reconciled ones (`state.py --get documents.reconciled`, 2026-09-30). The other 535 of 586 landed documents are reachable only through qmd, entity lists or a count.
- **It returns quotations already on wiki pages,** not document text around them.
- **Its one model step is tied to `lmrun`.** Claude CLI and free models work, but not a session subagent or Jules.
- **Its graph lives in Python dicts rebuilt on every call,** so a question cannot ask the graph anything the code did not anticipate.

## 2. Principles this must keep

| rule | what it means here |
|---|---|
| P13 no merge, P12 quote | an answer is claims, each attributed to one document, each carrying a verbatim quotation |
| P26 ask for an identifier | a model writes a line number only as a hint; code places or rejects every quotation |
| P15 | statuses `answered`, `refused`, `unparsed`, `unreachable`, never a score in their place |
| P25, P9 | the store is **derived**: rebuilt from the files, never edited, never committed |
| P6 one encoding | where GraphQLite replaces an existing computation (PageRank), both run until the bench shows they agree; then one is retired |
| P8 | the store is checked against what it was built from, every build |
| links are never inferred (`CLAUDE.md`) | stated edges and model proposals live apart; no query that feeds the wiki reads a proposal |
| decisions 006, 007, 011, 014 | an answer decides nothing; Claude is first party; OpenRouter and Jules only under the author's consent, which `route.py` and `jules.py` already enforce |

An answer has the standing of an entity list: a model's reading, recorded and verified by code, usable to point at a place, never a count, a page, a link or a merge.

## 3. The architecture

```
                      ┌──────────────── Plan/derived/ask.db  (one SQLite file, GraphQLite + FTS5) ───────────────┐
 files ──build──►     │ stated graph: Term·Doc·Conflict·Question·Chapter·Sheet, typed edges with `via` file:line  │
 (graph.py,           │ proposal graph: Entity·Gloss·Answer (label :Proposal), never mixed into stated queries    │
  entities, sheets,   │ FTS5: lines(slug,line,text) over 586 documents · quotes(slug,line,text) over 9,022 evidence │
  Sources/drive)      │ tables: packs · answers · claims · quote_checks · ledger                                   │
                      └──────────────────────────────────────────────────────────────────────────────────────────┘
question ─► 1 route (Cypher + algorithms + bm25) ─► 2 pack ─► 3 backend ─► 4 verify ─► 5 record (back into ask.db)
                                                          ▲                      │
                                                          └── 6 one expansion round: the model asks, code answers
```

### 3.1 The store: `Plan/derived/ask.db`

One file, built by `scripts/askdb.py build`, git-ignored like everything under `Plan/derived/`, rebuilt by a new `install.sh` component `askdb` (about 30 s estimated; measured in phase 1).

**Stated graph** (only what files state; every edge keeps `via`, the file line that states it):

| from | built from | adds over `graph.py` |
|---|---|---|
| `:Term`, `:Doc`, `:Conflict`, `:Question` and the seven edge types | `graph.py --json`, unchanged | nothing: the same graph, now queryable |
| `:Chapter` and `(:Chapter)-[:READS]->(:Doc)` | the chapter pages' reading headings | a question about a chapter starts at its page |
| `(:Doc)-[:DATED]` as a property `date`, `category`, `tier`, `read: bool` | `Sources/manifest.jsonl` | the 535 unread documents exist as nodes |
| `:Sheet` and `(:Sheet)-[:DEPENDS_ON]->(:Sheet)` | the heads of `Plan/weichen/*.md` (decision 016) | the decision process becomes a graph (§3.7) |

**Proposal graph** (label `:Proposal` on every node and relation type prefixed `P_`; no stated query names either):

| node | built from |
|---|---|
| `:Entity:Proposal` and `(:Entity)-[:P_NAMED_IN {line}]->(:Doc)` | verified entity lists (`entities.py matrix`) — the route to unread documents |
| `:Gloss:Proposal` | `graph.proposals()` glosses (German ↔ English) |
| `:Answer:Proposal` and `(:Answer)-[:P_CLAIMS {line}]->(:Doc)` | verified answers of this tool (§3.6) |

**Full text**: `lines(slug, line, text)` over every non-empty line of every landed document, and `quotes(slug, line, text, page)` over the 9,022 verified evidence quotations. Both `unicode61 remove_diacritics 2`; a trigram table is added in phase 1 only if the bench shows inflection losing hits.

**Check** (P8): `askdb.py check` compares node and edge counts per type with `graph.py`, lines per document with the files, and fails on any difference.

### 3.2 Route — which documents and which lines (code, in the store)

Every finder is a query; the router merges their (document, line) anchors and records which finder produced each.

1. **Seeds**: the question's folded surfaces matched against `:Term.surfaces` (the rule `graphrag.seeds` uses, ported, not changed).
2. **Spread**: `personalizedPageRank(seeds)` in Cypher. Down-weight by `degreeCentrality`, because the bench showed the hubs (`aegis`, `juna`, `kael`, `alters`) crowding gold pages out of the top eight (`CLAUDE.md`, *The knowledge graph*).
3. **Neighbourhood**: for a `compare` question, `shortest_path` between the two seed terms. Every hop carries its `via` line, so the pack can show why two terms are connected.
4. **Community**: Louvain on the stated graph; the pages in a seed's community that no other finder reached fill one slot. This is GraphQLite's own GraphRAG example's step 3.
5. **Unread documents**: `(:Entity)-[:P_NAMED_IN]->(:Doc {read:false})` for entities matching the seeds.
6. **Keyword**: `bm25()` over `lines` with the seed surfaces and the question's content words, all 586 documents. This replaces qmd's `search` for `ask`; qmd stays for people.
7. **Evidence**: `bm25()` over `quotes`, then the MMR with relevance floor `graphrag.select_mmr` already implements.
8. **Counts**: a counting question goes to `read.py --count` or `corpus.py` and stops before any model.

Anchors are ranked by a printed rule: evidence first, then documents reached by several finders, then by one.

### 3.3 Pack — the only context the model sees (code)

`Plan/runs/ask/<id>/pack.md`, identical for every backend, and `pack.json`:

| part | content | from the store |
|---|---|---|
| A. Question | verbatim, and `kind`: `locate`, `position`, `compare`, `explain` (named by the asker) | — |
| B. Rules card | about 30 fixed lines: answer only from the pack; one claim, one document; quote verbatim in „…"; one quotation, one passage; „nicht im Paket" rather than a guess; no comparison without both quotations | constant |
| C. Graph excerpt | top pages' lead and `## Where the sources differ` (`digest.py`); records touching them, position table only; the path for `compare`, each hop with its `via` | Cypher + `digest.py` |
| D. Source windows | ±N lines around each anchor, **numbered as `read.py` numbers them**, windows of a document merged | `lines` table |
| E. Skill excerpt | one or two skills whose description overlaps the question above a floor; description plus one named section (a small table in `ask.py`, provisional under P4) | `SKILL.md` files |
| F. Output schema | §3.5 | constant |

`pack.json` records each part's size, **`sends_text_of`** (documents whose text is in D — what consent is checked against), the finder behind each anchor, the budget, what the budget cut, and the pack's hash.

### 3.4 Backends — one contract, four doors

| backend | how | isolation | who may run it |
|---|---|---|---|
| **claude-cli** (proposed default) | `lmrun.call` with `make_lm("claude-cli/sonnet")`: `claude -p`, no tools | **enforced**: only the pack | first party (decision 011) |
| **session** | subagent `.claude/agents/source-asker.md` (Sonnet, `tools: Read`) reads `pack.md`, writes `answer.json` | by instruction | first party |
| **route** | `route.chat`, `purpose=ask`; `route.screen` refuses any request holding twelve words of a document outside `consent.json` | not needed | today only packs inside decision 007's two documents |
| **jules** | pack committed to a branch; `jules.dispatch` („read only the pack, write `answer.json`, submit"); `jules.verify`, `patch` | none: the whole repository | only with `--approval` naming an author decision |

### 3.5 Answer contract

```json
{ "answerable": "yes | partly | no",
  "claims": [ { "doc": "<slug>", "says": "<one sentence>",
                "quotes": [ { "text": "<verbatim>", "line_hint": 123 } ] } ],
  "differ": [ "<slug-a> vs <slug-b>: <what differs>" ],
  "gaps":   [ "<what the pack does not hold>" ],
  "need":   [ { "term": "<surface>" } | { "doc": "<slug>", "lines": [a, b] } ],
  "next":   [ { "doc": "<slug>", "why": "<one line>" } ] }
```

### 3.6 Verify, render, record (code)

1. A quoted document must be **in the pack**; otherwise `outside-pack`.
2. `quotes.verdict` at `line_hint`, else `read.locate`: placed, or `unresolved`.
3. A claim keeps placed quotations only; with none it is `unsupported` and printed apart.
4. `lint_readings.lint_lines` over `says` and `differ`; a `differ` line survives only if both documents have a supported claim.
5. `answer.md` is rendered by code, claims grouped by document in date order, every quotation as `„…" ^[slug.md:Lnn]`, so `quotes.py` checks the file like any other.
6. **Back into the store**: `answers`, `claims`, `quote_checks` rows, and an `:Answer:Proposal` node with `P_CLAIMS` edges to the documents it quoted. A later question can find earlier answers with Cypher (`MATCH (a:Answer)-[:P_CLAIMS]->(d:Doc {slug:$s}) RETURN a`) and the bench can count them. Nothing from this graph enters `Wiki/`.

### 3.7 One expansion round

The model may name what it lacks in `need`: a term, or a document range. Code answers it from the store (a term becomes seeds for §3.2 steps 1–4, a range becomes a window from `lines`), appends it to the pack as part G, and calls the same backend once more. One round only, so cost stays bounded and every token the model saw is still in the pack file.

### 3.8 The same store serves the decision process

Decision 016 made the sheets' heads machine-readable. Loaded as `:Sheet` nodes with `DEPENDS_ON` edges, the cross-read of a round becomes queries instead of prose:

- what a sheet unlocks: `MATCH (s:Sheet)<-[:DEPENDS_ON]-(t) RETURN s.id, collect(t.id)` (the field `/simplify` removed, derived here);
- cycles: strongly connected components;
- the order of a round: a topological order over the open key questions;
- blockers: `MATCH (s:Sheet {status:'offen'})-[:DEPENDS_ON]->(x) WHERE NOT (x:Sheet) OR x.status IS NULL` — W12 and W15 appear because they have no sheet;
- the sheet's evidence: `ask` questions whose pack is seeded by the sheet's records.

This is the checking script decision 016 deferred until after round 1: when it comes, it is a query file over `ask.db`, not a second parser.

## 4. How it is judged

Gold from the records: each conflict and question record lists positions per document with lines. The record's question is the bench question, and the record's node is **removed from the stated graph first**, as `graphrag.py bench` removes it. Caveat: the same hand wrote question and label.

Measured per run, never folded into one number (P11): **pack recall** (record positions inside the pack's windows, no model), **finder yield** (which of the eight finders produced the anchors that held gold — this decides which finders stay), **placed rate**, **document recall and precision**, **outside-pack rate** (should be 0), **calibration** on cases built to be unanswerable. Every model case runs twice (P18); a second Claude run is the ceiling for other backends (P27). `baseline.py` records the numbers.

**Parity bench before any replacement** (P6): GraphQLite's `personalizedPageRank` and `graphrag.pagerank` on the 24 bench cases, and FTS5 `bm25()` against qmd `search` on the same queries. GraphQLite's version replaces the existing one only where it is at least as good on the bench; otherwise both stay, named.

## 5. Implementation plan

| phase | builds | gate |
|---|---|---|
| **0. Decide** | done: decision 017 | — |
| **1. Store** | `scripts/askdb.py build`, `check`, `selftest`; `install.sh askdb`; `graphqlite` in `.venv-dspy` (dry run resolves); batch upserts | `check` holds; build time and file size measured; `selftests.py` runs it |
| **2. Parity** | `askdb.py bench --parity`: PPR vs `graphrag`, bm25 vs qmd, with and without degree down-weighting, Louvain slot on and off | numbers in `baselines.jsonl`; which finder stays is decided by them |
| **3. Route and pack** | `scripts/ask.py route`, `pack`, `bench --pack` | pack recall on all record cases; budget chosen |
| **4. Verify and render** | `ask.py verify`, `render`, `replay`, write-back to the store; fixture answers from `lm_fixture` carrying each defect | each defect named by its own check |
| **5. Claude CLI** | `--backend claude-cli`, 8 cases × 2 runs on Sonnet, with and without the skill excerpt and the expansion round | numbers recorded; the author sees two rendered answers |
| **6. Session agent** | `.claude/agents/source-asker.md`, `ask.py collect` | same bench |
| **7. Free models, Jules** | `--backend route`, `--backend jules` | only after §6 answers allow it |
| **8. Decision process** | the sheet queries of §3.8 as `askdb.py sheets` | used in the next cross-read |

**Reused**: `graph.py --json`, `graphrag.seeds` and `select_mmr`, `digest`, `read.numbered` and `locate`, `quotes.verdict`, `entities` matrix, `lint_readings.lint_lines`, `lmrun.call`, `claude_lm`, `route.chat`, `jules.dispatch`/`verify`/`patch`, `lm_fixture`, `baseline.py`. **New**: `scripts/askdb.py`, `scripts/ask.py`, `.claude/agents/source-asker.md`, an `install.sh` component, a `selftests.py` line.

## 6. Answered — decision 017

The author, 2026-09-30: „Die Antworten werden protokolliert und sind wie sources zu behandeln" and „Darüber hinaus dürfen auch openrouter und Jules für entsprechende Fragen genutzt werden - die nutzt Du immer vielleicht erst mal als Probelauf - hier kannst Du frei experimentieren".

- **An answer lands like a source:** `Sources/ask/<id>.md`, immutable, checksummed, in `Sources/ask/manifest.jsonl`, tier `M-ask`, written by `ask.py land` only. §3.6 step 6 writes the store *and* lands the rendered answer. It stays out of the corpus counts.
- **OpenRouter free models and Jules may answer**, as trials beside the default, for any pack. `consent.json` gets a purpose entry for `ask`; Jules dispatches cite decision 017.
- **Default backend** claude-cli/Sonnet; **GraphQLite** for `ask` and the sheets until the parity bench and the author say more.

## 7. What this cannot do

- It finds what the finders reach. A passage no edge, entity, keyword or count points at is not in the pack; `answerable: no` is then right.
- FTS5 does not stem German. A question in another word form finds less until a prefix or trigram query is added.
- A placed quotation proves the words stand on the line, not that the claim reads them rightly. The claim is still a model's reading.
- Only claude-cli enforces the context limit; the session agent and Jules keep it by instruction.
- GraphQLite is v0.8, young, and 2.3 % of the openCypher TCK fails (its README). The store is derived and replaceable; nothing but `ask` and the sheet queries depends on it until the parity bench says more.
