# SPEC — the recommended architecture

**Status: adopted by the author, 2026-10-01 — `Plan/decisions/021-the-architecture-spec-adopted.md`.** It was written
as the recommendation of the architecture session (PR #139); its migration order (§9) is now binding, and E4 may run
within decision 021's limits. Where it and an older decision differ, the older decision stands until a step changes
it. The baseline, the ownership map and the self-evaluation it rests on are in
`Plan/runs/architecture-session-2026-10-01/README.md`.

Three kinds of statement appear below, always marked:

- **[built]** is true of the repository at this commit and has a path;
- **[migrate]** is a proposed change, with its step in §9;
- **[author]** is a choice only the author can make; it is listed in `Plan/questions-for-the-author.md`, or decided in decision 021.

## In one paragraph

Keep the system that exists. It has two layers of authority (`Sources/`, `Wiki/`), one source-identity module
(`subject.py`), one quotation check (`quotes.py`), one derived query store (`Plan/derived/ask.db`) and one
deterministic question-to-evidence path (`ask.route` → pack → answer → `ask.verify`). Do not add a layer, a
backend or a controller. Repair three things first: the **evaluation**, so that a regression and a discovery can
be told apart; the **pack**, so that every finder delivers the same kind of hit into one budgeted, serialized
context with an explicit `incomplete` flag; and the **duplicates**: the doubled freshness record, the four query
builders, and the model path that keeps no per-call record. The adaptive finders — novelgraph, and
RLM over chunks or the graph — stay **optional finders behind the same hit contract**. They earn a default place
only through E4, a matched comparison at equal total cost. This is H0 of the options document plus its first half
of H1, made consistent. It is not H2–H5.

```
                      authority (git, written by people / by one script)
  Sources/drive ─ manifest ─ terms/notes ─ Wiki/{candidates,conflicts,questions,chapters,compare}
        │                          judgements.jsonl, sweep.jsonl, decisions/, eval/  (frozen)
        │
        ▼  derive (disposable, rebuildable, refuses when stale)
  Plan/derived/ask.db  (GraphQLite graph + FTS5 lines/quotes)     Index/ (chunk rows; vec/lex/_build ignored)
        │                                                             │
        ▼                                                             ▼
   finders:  graph-evidence · bm25-lines · entity-unread · co-mention · parallel │ novelgraph · rlm  (optional)
        │                                 Hit contract (§4.2)                                  │
        └──────────────────────────────────────►  pack(hits, budget) ◄────────────────────────┘
                                                      │  Pack contract (§4.3)
                     ┌────────────────────────────────┼────────────────────────────┐
                     ▼                                ▼                            ▼
             ask backends (claude -p)       kg.py context (JSON)          a reader / an agent
                     │
                     ▼
              ask.verify → land as M-ask (citable, never gold, never counted as corpus)
```

## 1. Purpose and workflows

| workflow | who | today | status |
|---|---|---|---|
| **Evidence lookup**: a question gets the source lines that bear on it, with their disagreements | the author, a session, an agent | `ask.py pack/run/verify/land`, `kg.py context`, `graphrag.py ask`, skill `graph-context` | [built]; two packers ([migrate] step 4) |
| **Source-local reading**: one document becomes a census and a note, frozen before the wiki is read | Claude as reader (decision 015), later the author | skill `ingest`, agent `document-reader`, `capture.py`, `census.py`, `claims.py` | [built]; **paused** by the author |
| **Reconciliation**: a census is answered by lookup and its readings go on the pages, attributed and unmerged | a session | `reconcile.py`, `readings.py`, `record.py`, `account.py order` | [built] |
| **Disagreements and prepared decisions**: a conflict or question is a record; a decision sheet gathers what an author needs to decide | the author decides | `Wiki/conflicts/`, `Wiki/questions/`, decision sheets (decision 016), `Plan/questions-for-the-author.md` | [built] |
| **Chapter context**: what the sources say about chapter N, without presenting research as canon | the author while writing | `Wiki/chapters/kap-NN.md` (decision 013) | readings [built]; *context for writing* is **future** |
| **Writing support** | the author | 13 augmentation-only skills (`writing-skills`) | [built] as tools; the plan is undecided |

**Unmet prerequisites of chapter context and writing support.** These are named so that no tool claims them:

- the four questions of the writing plan (`NOW.md`) [author];
- a per-chapter model of what the reader, Kael and AEGIS know, which does not exist;
- a rule for what counts as canon. The author's position of 2026-09-26 is that research narratives are not canon,
  and that canon is the author's decisions and approved chapters.

Until all three exist, a "chapter context" is an evidence pack scoped to a chapter page and nothing more.

## 2. Authority and persistence

| fact | owned by | written by | may never be derived from |
|---|---|---|---|
| a source's bytes, identity, tier, date | `Sources/manifest.jsonl` + `Sources/drive/*.md` | `sources.py` only; immutable once landed | anything downstream |
| what one document says | `Sources/terms/<slug>.md` (census), `Sources/notes/<slug>.md` (note) | a reader, frozen before the wiki is consulted | the wiki, another document, a model's proposal |
| a reading on a page | `Wiki/candidates/*.md`, `Wiki/chapters/*.md` | reconciliation; one commit per source document | an `ask` answer, a `P_*` edge, an entity list |
| a disagreement | `Wiki/conflicts/*.md`, `Wiki/questions/*.md` | a person reading two readings | any program (conflict detection is never mechanised) |
| one term or two | `Plan/runs/judgements.jsonl` | a person; code may claim a rule only if replay agrees | a model's merge |
| an author decision | `Plan/decisions/NNN-*.md`, author lines in `NOW.md` | the author (or a delegated decision that names its delegation) | a session's recommendation, including this file |
| a frozen evaluation set | `Plan/eval/*.json` [built, step 1] | `benchset.py freeze`, never rewritten | answers (`M-ask`), proposals, the system scored on it |
| an answer | `Sources/ask/` (tier `M-ask`, decision 017) | `ask.py land` | — and it is **never** gold, never a census input, never counted as corpus |

**Disposable** — rebuilt from the above, refused when stale, never an authoring input:

- `Plan/derived/` (derive cache, `ask.db`, `ui/`);
- `Wiki/index.json`, committed but derived by `wiki_index.py --check`;
- `Graph/` (the atlas, output only);
- the novelgraph vectors, lex and `_build/`;
- qmd's index.

**No circular derivation** [built, kept]:

- An answer cites lines; it is not a line.
- A proposal (`P_*`, entity list, gloss, HyperExtract edge) sits beside the graph. `askdb.check` refuses a `P_` type
  among the stated types.
- Gold for a retrieval case comes from the conflict and question records, which people wrote. That is what makes
  the bench circular (92 % of gold lines are page quotations). It is not a reason to fill gold from a model.

## 3. Modules and ownership

The smallest runtime per responsibility, and the verdict.

- *Retained*: stays as is.
- *Consolidated*: one implementation replaces two or more ([migrate]).
- *Optional*: works, has no pipeline consumer, and earns a default only by a named measurement.
- *Retired*: removed, its idea kept in `PRINCIPLES.md`.

| responsibility | path | runtime | inputs → outputs | consumers | verdict |
|---|---|---|---|---|---|
| source identity, frontmatter, file lines | `scripts/subject.py` | stdlib | `Sources/drive` → `Document(slug, offset, lines)` | ~40 scripts, novelgraph | **retained**, the root of the dependency graph |
| quotation identity | `scripts/quotes.py`, `read.py --find` | stdlib | a cited quote → `verified/unresolved/unchecked` | 12 modules, CI | **retained** |
| fetch and land | `scripts/sources.py`, `dedupe.py`, `duplicates.py` | stdlib | Drive → `Sources/` | — | **retained** |
| reading, census, note, reconciliation, pages | `capture`, `census`, `claims`, `readings`, `reconcile`, `record`, `account`, `wiki_index`, `link`, `relations` | stdlib | a document → a census → page readings | the `ingest` skill, agents | **retained**; paused |
| derived per-document facts | `scripts/derive.py` + `scripts/rules/` | stdlib | a source + a rule version → a cached fact | `corpus.py`, `overview.py` | **retained**, and the **model for invalidation** (§5) |
| the stated graph | `scripts/graph.py` | stdlib | frontmatter, `[[links]]`, `^[slug.md:Lnn]` → nodes, typed edges with `via`, evidence with `status` | 11 modules | **retained** |
| the query store | `scripts/askdb.py` → `Plan/derived/ask.db` | `.venv-graphqlite` | graph + `Sources/` → GraphQLite + FTS5 | ask, kg, graphlab, bm25rel, aliases, crossdoc, graph_export | **retained as the one store**; freshness and `evidence_rows` **consolidated** into it (step 3) |
| graph retrieval | `scripts/graphrag.py` (`retrieve`: fold seeds, PPR, MMR) | stdlib | question + graph → seeds, verified evidence, conflicts, questions | ask, kg, rlm_retrieval, graphlab | **retained** as a finder |
| lexical search | `askdb.fts_query`, `kg.search`, novelgraph `Index.bm25`, `bm25rel` | — | — | — | **consolidated**: one `query_words(text)` in `askdb.py`; novelgraph keeps its lemmata (step 5) |
| routing (finders → anchors) | `ask.route` | `.venv-graphqlite` | question → anchors with finder names | `build_pack`, bench | **retained**; emits hits in the shared contract (step 4) |
| packing | `ask.build_pack` (Markdown), `kg.bounded_context` (JSON) | — | — | — | **consolidated** into one `pack.py` (step 4); two renderers stay |
| answering | `ask.py run/verify/land`, `claude_lm.py` | stdlib + `claude` | pack → answer → verified claims → `Sources/ask/` | the author | **retained** |
| graph CLI | `scripts/kg.py` (`index`, `search`, `context`, `evidence`, `export`) | `.venv-graphqlite` | `ask.db` → JSON / `Graph/` | skill `graph-context` | **retained**; its store code moves to `askdb.py` (step 3) |
| chunk index | `novelgraph/` → `Index/` | `.venv-novelgraph` (+0.5 GB embedder) | `Sources/` → chunk rows, vectors, BM25 | **none in the pipeline**; `rlm` | **optional**; becomes a finder behind the hit contract (step 6), default only after E2/E4 |
| RLM over chunks or wiki | `novelgraph rlm`, `scripts/rlm_retrieval.py` | `.venv-novelgraph[rlm]`, `.venv-dspy`, Deno | question → refs | runs only | **optional** (an experimental comparator, H3) |
| RLM ingest | `scripts/rlm_ingest.py` | `.venv-dspy` | a document → candidates | none | **optional**; its LM goes through `lmrun` (step 7) |
| HyperExtract | `hx.py`, `he_claude.py`, `hegraph.py`, `Plan/hyperextract/` | stdlib | contracts → `P_HE_*` proposals | `he-lines` finder (off) | **optional**; the backfill stays stopped (decision 019) |
| model calls | `lmrun.py`, `claude_lm.py`/`claude_cli.py`, `route.py`, `he_claude.py` | | | | **retained**, four consent encodings kept apart (decision 008); every call recorded |
| DSPy surfaces | `pairs.py` (the one with a held-out ladder), `baseline.py`, `check_dspy_*` | `.venv-dspy` | | | **retained**; new surfaces only through gate L5 |
| evaluation sets | `scripts/benchset.py` → `Plan/eval/` | stdlib | live records → frozen, hashed cases | every bench [migrate] | **new** [built, step 1] |
| search for people | qmd (`setup_qmd.sh`) | Node | | nobody in the pipeline | **optional**, unchanged |
| project app | `scripts/ui.py` | stdlib | the repository → canvas files | the author | **retained** |
| the agent harness | `.claude/agents/`, `.agents/skills/`, `knowledge.py init` | | | | **retained** |

**Graph and store ownership**, resolved:

- `graph.py` owns what the graph says.
- `askdb.py` owns how it is stored and queried, and whether the store is fresh.
- `kg.py` and `ask.py` are clients and hold no store logic of their own.
- There is one store. novelgraph's `Index/` is a second index over the same sources, owned by `novelgraph/`. It is
  read through the hit contract and never joined into `ask.db`.

**Retired**: nothing in this session. Every module above has a consumer or a pending measurement. The agency
spec 010's lesson (§8) applies to future checks, not to existing modules.

## 4. Data and query contracts

### 4.1 What exists, by example [built]

| thing | example (abridged, real) |
|---|---|
| source identity | `Sources/manifest.jsonl`: `{"drive_id": "1icDtMmu…", "slug": "kohaerenz-protokoll-konzeptentwicklung", "tier": "T3-work", "category": "kernkonzept", "export_path": "Sources/drive/…md", "sha256": "618b53b8…"}` |
| a line | `subject.Document.offset`: a citation names a **file** line; the body starts at `offset` |
| a quotation on a page | `„…" ^[slug.md:L63]`, resolved by `quotes.verdict` |
| graph evidence | `graph.py`: `{"quote": "AEGIS-System-Vokabular wie …", "ref": "kap0-v1-annotiert-md.md:L63", "doc": "kap0-v1-annotiert-md", "line": 63, "page_line": 31, "section": "Reading — …", "status": "verified"}` |
| a typed edge | `graph.py`: edge `{type, from, to, via: "Wiki/candidates/aegis.md:L31"}`; proposals typed `P_*` |
| a chunk | `Index/sources/<slug>/chunks/heading@v1.jsonl`: `{"id": "bfa3b0e7ed11", "line_start": 11, "line_end": 27, "heading_path": […], "sha": "d03b6ce6…", "tokens": 477}` — no text; `id = sha1(slug|method|start|end|content_sha)[:12]` |
| a judgement | `Plan/runs/judgements.jsonl`: `{"id": "J1", "surfaces": ["Die Konstrukt-Stadt", "Konstrukt-Stadt"], "decision": "one-term", "rule": "strip leading der/die/das …"}` |
| a pack (ask) | `Plan/runs/ask/<id>/pack.json`: `sends_text_of`, `cut_by_budget`, `budget` (characters of source windows), `chars`, `shown {doc: [lines]}`, `finders {doc: [names]}`, `hash` |
| a pack (kg) | `kg.bounded_context`: `query, seeds, terms, conflicts, questions, evidence[], omitted, incomplete, no_evidence, max_bytes` — whole quotations; refused if the metadata alone does not fit |
| a verified answer | `ask.verify`: per quote `placed / outside-window / unresolved / outside-pack`; unsupported claims kept |
| a model call | `Plan/runs/<subject>/lm/<step>.jsonl`: one record per call, `status ∈ answered/refused/unparsed/unreachable`, cost, raw output |

### 4.2 The hit [migrate, step 4 — proposed fields]

Every finder returns hits; no finder returns prose.

```json
{"doc": "kap0-v1-annotiert-md", "line_start": 61, "line_end": 65, "anchor": 63,
 "finder": "graph-evidence", "rank": 1, "score": 0.42,
 "source_sha": "…", "why": "term:aegis, quoted on Wiki/candidates/aegis.md:L31",
 "proposal": false}
```

- **Identity** is `(doc, line_start, line_end)`. Two hits with the same identity merge, keeping every `finder`.
  Overlapping spans in one document merge into one span.
- **`source_sha`** is the manifest sha256 the finder read. The packer refuses a hit whose sha is not the current one.
  This is the `Stale` rule of novelgraph and of `novelgraph rlm` since PR #140's review, applied to every finder.
- **`proposal: true`** marks a hit a model chose (`he-lines`, `rlm`). It is packed under its own heading and never
  counted as a stated relation.
- A hit on a line above the document's `offset` is dropped (defect 1).

### 4.3 The pack [migrate, step 4 — proposed]

One function `pack(question, hits, budget, unit) -> Pack`; two renderers — Markdown for `ask` backends, compact
JSON for `kg.py context`.

| part | rule |
|---|---|
| **order of sections** | question → rules → disagreements touching the hits (conflicts, questions, their ids) → graph evidence → source windows → schema |
| **what is never cut** | the question, the rules, the schema and **every conflict and question record the hits touch**. If these alone exceed the budget the pack is refused, as `kg.bounded_context` refuses today |
| **the budget** | counted over the **whole serialized pack**, not the windows alone (`ask` counts windows only: 60 000 characters of windows became 66 440 characters sent) |
| **unit** | UTF-8 bytes, which is what `kg` uses and what a transport carries. Characters and regex tokens are reported beside it. No model tokenizer is assumed. When a backend's tokenizer is available, its count is recorded beside the bytes, never instead of them |
| **cut granularity** | the document, as today: a document block that does not fit is skipped and the next one tried, and every skipped identity is listed. Span-level trimming was measured and does not help (§4.4) |
| **de-duplication** | a window line is sent once. A graph-evidence quotation whose line is already in a window is shown as a reference to that line, not repeated |
| **status** | `complete` (nothing omitted) · `incomplete` (`omitted_hits > 0`, the omitted identities listed) · `no_evidence` (no hit) · `refused` (metadata over budget, stale source). `incomplete` is never silent |
| **identity** | `sha256` of the serialized pack. A pack is immutable (as `cmd_pack` does today) |

### 4.4 How the `ask` pack should spend its budget — measured [built as a measurement, migrate as step 4]

The author asked how the ask packs can be optimised (2026-10-01). The packing step was replayed offline on the 24
frozen cases under four variants, with the route held fixed:

- `body`: drop frontmatter anchors;
- `ranked`: when a document's anchors exceed 60 lines, keep the strongest rather than the earliest;
- `fill`: trim a document to its strongest spans instead of cutting it whole;
- `all`: the three together.

The script and results are `Plan/runs/architecture-session-2026-10-01/packs/` (`pack_variants.py`,
`pack_variants.json`, README).

**The result: packing is not where recall is lost.**

- `current` reproduces `build_pack` exactly, on 24 of 24 cases.
- No variant improves line or document recall at 15 000, 30 000 or 60 000 characters.
- Trimming is slightly worse at 15 000 (−0.007 [−0.016, +0.002], 1 case better and 5 worse), because a trimmed
  document displaces later whole ones.
- With no budget and no cap at all, the route's anchors reach line recall **0.102** and document recall **0.307**.
  The default pack already sends 0.100, so **98 % of what the route finds is sent**.
- **73 %** of the anchored lines lie in documents with no gold line for the case.

Per finder, in gold lines per 10 000 characters:

| finder | gold lines per 10 000 characters |
|---|---|
| `graph-evidence` | 2.47 |
| `bm25-lines` | 1.20 (the most gold overall) |
| `parallel` | 0.93 |
| `co-mention` | 0.35 |
| `entity-unread` | no anchor on any of the 24 questions |

Capping co-mention at 3 paragraphs cuts the whole pack by 13 % (48 010 → 41 915 characters) and sends the same gold
lines (111 against 109; 2 cases better, 1 worse).

Consequences:

- The pack is specified for **cost and honesty**, not recall: a whole-pack byte budget, an explicit `incomplete`,
  no frontmatter, duplicates sent once.
- Span-level trimming is **not** adopted.
- Recall work moves to the **route**: per-finder budgets by measured yield, one BM25 query builder (step 5), and
  novelgraph as a finder (step 6). Each is judged on an independent set (G1–G2), since `graph-evidence`'s lead is
  partly the bench's circularity.
- The co-mention default is the author's (question 2(4) on `NOW.md`). The measurement goes there, and the default
  is unchanged.

### 4.5 Disagreement metadata

A pack lists the conflict and question records whose cited lines or terms its hits touch, with their ids and the
sources on each side [built in `kg` and in `graphrag.retrieve`]. A pack never states which side is right. An answer
that resolves a disagreement is flagged by `ask.verify` as unsupported unless a placed quotation supports each side.

## 5. Update and restart behaviour

| store | invalidation key | rebuild | stale read |
|---|---|---|---|
| `Plan/derived/` (derive) | source sha × rule version | per document, about 3 s for all [built] | recomputed |
| `ask.db` | one input hash over graph inputs + sources | full rebuild by `kg.py index`, run by `knowledge.py init` at session start [built] | **refused** by `askdb.fresh`. Today `kg.freshness` keeps a second record of the same thing; step 3 makes `askdb` the one owner |
| `Index/` chunk rows | source sha × `methods.toml` stamp (chunker version) | per source, incremental [built] | **refused** (`Stale`) by `search.Index` |
| `Index/` vectors, lex, `_build/` | chunk id × embedder fingerprint | about 3 min from nothing; the embedder is 0.5 GB | refused; a publish is atomic under a lock, and an interrupted build leaves `.building`, which readers refuse [built] |
| `Graph/` atlas | — | `kg.py export` | output only, never read back |
| qmd | — | `qmd update` | nothing depends on it |

Decisions:

- **`Index/` chunk rows stay committed.**
  - Why: they hold no text, take 28 MB, and are what a run record's refs resolve against without the novelgraph
    venv.
  - Vectors, lex and `_build/` stay ignored and rebuildable.
  - Reverse if: the committed rows cost review noise on a source landing that outweighs their use. The test is the
    first landing batch after the reading pause.
- **`Graph/` stays committed** as documentation, regenerated by `kg.py export`.
  - Proposed [migrate, step 3]: a `--check` that fails when it is stale, as `overview.py --check` does, so it cannot
    drift silently.
- **Stable identities**:
  - a source: its `drive_id` and slug;
  - a line: file line × source sha;
  - a chunk: content-addressed;
  - a graph edge: its `via` line;
  - a pack: its hash.

  A title change re-keys nothing but the label. A code or rule change invalidates by version stamp, never by date.
  A model change is a new run directory (PR #140's `--run`), never a resume.
- **Deletion.** A source is never deleted from `Sources/`. A folded duplicate moves to `Sources/duplicates.jsonl`.
  Each index refuses until it is rebuilt without it ("the index covers other sources than are landed").
- **Concurrency.**
  - One writer per store, under its own lock (`Index/.lock` [built]). `ask.db` has a single builder,
    `kg.py index` / `knowledge.py init`.
  - Readers refuse during a publish.
  - Model runs are serial (the author's limit).

## 6. Learning and evaluation — L1–L7 as gates

| kind | question | fixture | what may be concluded |
|---|---|---|---|
| **regression** | did a change lose evidence the system found before? | `Plan/eval/retrieval-cases-v1.json` (24 cases, frozen, hashed) | only "no worse on these 24" |
| **discovery** | does it find evidence it did not already quote? | **does not exist yet**. The proxy: gold lines no page quotes (§4.4, the `unquoted` view), a small and dependent set | nothing general until independent cases exist |
| **extraction** | does a reader or contract find what a document says? | gold lists (decision 009), `goldeval.py`, `goldrel.py` | agreement with one reader of one family |
| **semantic fidelity** | is a reading right? | claims audits (reader lab) | per audited claim only |
| **answer utility** | does a pack or answer reduce the author's work? | none | nothing without the author (E6) |
| **cost** | cold + warm + build + model calls | run records | per machine |

Gates — each must hold before what it guards:

- **G1 (L1) — before any retrieval change is called an improvement.**
  - A frozen set, scored paired on all its cases, with a bootstrap interval.
  - The cases form **one connected cluster** (`benchset.py clusters`: one group of 24 at any sharing of a gold
    document). So there is **no clean held-out split**, and none may be reported.
  - A discovery claim needs new cases written blind to the system: by the author, or by a reader who has not seen
    the packs.
- **G2 (L2) — before a backend joins the default.**
  - Identical questions, source snapshot and serialized byte budget (§4.3).
  - Report the marginal **novel** gold (lines no other finder sent), duplicates, and cold and warm cost.
- **G3 (L3, L4) — before a reading procedure or a relation type is adopted.**
  - Defect-class claims audit, not quote-check success.
  - A relation type earns a place by a downstream gain on a set it was not tuned on. Decision 019's null stands
    until then.
- **G4 (L5) — before a DSPy surface is compiled.** It needs all of:
  - a fallible metric;
  - frozen train/dev/test membership;
  - a deterministic baseline and an unoptimised baseline;
  - a declared budget;
  - hard vetoes: no fabricated evidence, no false merge.

  Today only `pairs.py` meets this.
- **G5 (L6) — before a question loop runs unattended.** It stops on any of:
  - a repeated question (normalised text, or the same evidence set);
  - no new supported evidence in a round;
  - an exhausted budget;
  - a question only the author can decide.

  It never resolves a disagreement.
- **G6 (L7) — before a module is called integrated.**
  - It passes from a fresh clone: `knowledge.py init` reports its capability.
  - Stale input is refused.
  - A missing optional tool reports `not run`, never a pass.

**`M-ask` answers are never gold**, never a census input, and never evidence for the system that produced them.
`benchset.py freeze` reads only the conflict and question records.

## 7. Model and judgement boundaries

| decides | what |
|---|---|
| **code** | quotation identity, line resolution, freshness, budgets, de-duplication, ordering, refusal, a matching rule that `judgements.py` replays green |
| **a model may propose** | candidate terms, entity lists, glosses, `P_*` relations, hits (`rlm`, `he-lines`), answers to a pack — each marked as a proposal, each recorded per call |
| **a person (reader)** | a census, a note, a reading on a page, a conflict or question record, a judgement |
| **the author** | canon, which reading is right, the tiers' precedence (suspended, decision 006), consent for text to leave the container, spend, the reading pause, the writing plan |

**Consent and accounting** [built, kept]:

- No corpus text leaves the container without a decision that names the recipient.
- Claude through `claude -p` is first party (decision 011).
- The four consent encodings stay separate (decision 008). The one gap is `rlm_ingest.py`, which builds its own
  OpenRouter LM outside `lmrun.call` (step 7).
- Every model call leaves a record, including failed ones. PR #140 closed the same gap for `rlm_retrieval.py`.

## 8. Architectural choices

| | **recommended: H0 made consistent** | **H0 unchanged** | **alternative: adaptive controller (H2/H3 default)** |
|---|---|---|---|
| retrieval | deterministic route; optional finders behind one hit contract | deterministic route; novelgraph and RLM disconnected | an agent (RLM) chooses searches and reads |
| packing | one contract, whole-pack byte budget, `incomplete` explicit, skipped documents listed | two packers, three units, whole-document cuts | the agent's history is the context |
| evaluation | frozen sets, paired, no false holdout | live gold, moves with every record edit | needs read-evidence scoring that does not yet exist |
| cost per question | one pack, about 4–9 s, no model until an answer is wanted | same | $0.10–0.30 and 1–2 min per question (PR #140), invented evidence to gate |
| evidence | the pack's lines are exactly what a model saw | same, with silent cuts | 55 % of the refs it cited were read; the rest came from previews |

The consequential choices:

| choice | evidence | cost | rejected | reversed by |
|---|---|---|---|---|
| keep the deterministic path as the default | PR #140: no chunk size wins under RLM; the agent invents evidence; 156 of 282 refs read | none | RLM default (H3) | **E4**: an adaptive controller reaches more *read* gold at equal total cost, with no invented evidence admitted, on cases outside the circular bench |
| one pack contract, bytes over the whole pack | `ask` sends 66 440 characters for a 60 000-character budget; `kg` already counts whole output | one module, two renderers | keeping both | a backend that needs a different unit natively — it then reports both |
| the pack is tuned for cost and honesty, the route for recall | §4.4: the default pack sends 98 % of the route's ceiling; no packing variant moves recall; co-mention costs a third of the anchored characters (404 of 1 224 thousand) for 14 gold lines | none | optimising the packer for recall (span trimming, anchor ranking) | a route that finds far more than a pack can hold — then §4.4's variants are re-run, as they are written to be |
| freeze the bench, report no holdout | `benchset.py clusters`: one group of 24 | done | random split | independent cases that do not share gold documents |
| novelgraph optional, not removed | no pipeline consumer; static bench cannot separate sizes; cold 15 s | its venv and 0.5 GB | adopt it as a default finder; delete it | G2: marginal novel gold at equal bytes |
| chunk rows committed | 28 MB, no text; refs resolvable without the venv | review noise on landings | ignoring them | the first landing batch's diff noise |

**Reconciling `GOAL.md`.** `GOAL.md` is the author's brief of 2026-09-23 and describes a target, not a repository.

- *Tiered precedence and "newer wins"* (§3) — suspended by decision 006. The spec keeps tiers as **metadata in the
  pack**, never as a resolution rule.
- *Automatic conflict adjudication* (§4.4) — replaced by "conflict detection is never mechanised" (`CLAUDE.md`). The
  spec flags disagreements and stops.
- *The plot model as checkable rules* — the agency spec 010, which `GOAL.md` cites, was superseded on 2026-06-09.
  Its lesson: of eleven "decidable" storyform checks, most were fixture heuristics and one was a stub returning
  PASS; only reference resolution, set partition and slot presence were decidable. So a plot rule enters as a check
  only if a fixture can make it fail. Decision 013's chapter pages are the unit it checks against.
- *A self-questioning loop* — kept as G5, with its stop rules.
- *A HyperExtract backbone* — decisions 019 and 020: ported, measured, the backfill stopped. Its proposals stay
  beside the graph.
- *The decisions that already chose* — decision 015 (the pipeline plan) and decision 018 (questions by delegation)
  stand. This spec changes neither.

## 9. Ordered migration and acceptance

The order follows the briefing: evaluation repair before any backend or optimisation. Each step is one PR, reviewable
alone, offline, and rolled back by reverting it.

| # | step | touched paths | acceptance (offline) | rollback |
|---|---|---|---|---|
| **1** | **Freeze the retrieval cases** — [built, PR #139] | `scripts/benchset.py`, `Plan/eval/retrieval-cases-v1.json`, `scripts/selftests.py`, `scripts/README.md`, `Plan/README.md` | `benchset.py selftest`: 6 cases, each mutation-tested; `benchset.py check`: hash and every gold line inside its body; drift reported | revert; the live bench is untouched |
| **2** | **Benches read the frozen set** — [built] | `benchset.cases()`, read by `ask.py bench` (`--live` to read the records), `novelgraph` (`repo.bench_cases`: `bench`, `rlm`), `Plan/runs/graph-lab-2026-09-30/eval-audit.py` | `ask.py bench` frozen and `--live`: identical rows on all 24 cases (`Plan/runs/ask/bench-2026-10-02-60000-*597b8e05.json`); the evaluation audit's output byte-identical to its recorded run; `benchset.py selftest`: a bench ignores an edited record and refuses a tampered file (8 cases, mutation-tested). **Not covered:** `graphrag.py bench` — its gold is wiki pages, not lines, and needs its own frozen set; dated run scripts under `Plan/runs/` keep the live cases they ran on | revert; `--live` kept |
| 3 | **One store owner** | `askdb.py` (`fresh`, `evidence_rows`), `kg.py` (imports them), `graph_export.py --check` | `kg.py` selftests and GraphQLite parity unchanged; a fixture where the two old freshness records disagree now cannot be built | revert |
| 4 | **One hit and pack contract** | new `scripts/pack.py`; `ask.build_pack` and `kg.bounded_context` become renderers; `ask.route` emits hits | the `current` pack is byte-identical through the new code (fidelity, as in §4.4); then the budget covers the whole pack (in bytes, characters reported beside); `incomplete` set when anything is omitted; frontmatter anchors dropped | revert; the pack hash in old run records still identifies the old packs |
| 5 | **One query-word function** | `askdb.query_words`, used by `fts_query`, `kg.search`, `bm25rel`; novelgraph keeps lemmata and imports the stop list | per-query diff of the words on the 24 questions, reviewed; bench unchanged or the difference reported | revert |
| 6 | **novelgraph as an optional finder** | `ask.route` (`finders=("novelgraph",)`, off by default), an adapter to the hit contract | G2 run: paired novel gold at equal bytes; cold cost reported; **default stays off** unless G2 holds | turn the finder off |
| 7 | **`rlm_ingest` through `lmrun`** | `scripts/rlm_ingest.py` | an offline fixture: an answered and a failed call each leave a record, as `rlm_retrieval --record-selftest` does | revert |
| 8 | **E4** — approved (decision 021): Claude only, serial, $20 for the whole run, after steps 2 and 4 | a run directory under `Plan/runs/` | fixed pack vs bounded expansion vs RLM at equal total cost, read evidence only | — |

Steps 2–7 need no model call and no corpus reading. Step 8 has the author's yes on spend (decision 021).

**What remains unmeasured**:

- discovery: there is no independent case set;
- semantic fidelity at scale: the claims audits are small;
- answer utility: no author calibration exists;
- RLM against a fixed pack: E4 has not run;
- the value of any relation type downstream;
- chapter-context sufficiency.

Each is named with the gate that would measure it (§6).
