# Retrieval, ranking and knowledge graphs — for `ask`

This is `scripts/graphrag.py`'s world: the wiki as a knowledge base, a typed
graph derived from it (`scripts/graph.py`), and a retriever over both. `ask` is
the last arrow in the process diagram (`CLAUDE.md`), and this is the retrieval
half of it — it hands back attributed evidence, never a written answer.
`Plan/concept/graphrag_2026-09-23.md` is the design note this file expands;
`api.md` has the DSPy signatures this page only points at.

**None of it is embeddings.** Seeding is folded substring containment,
relevance is a hand-written bag-of-words cosine, and ranking is a hand-written
personalized PageRank. `graphrag.py` imports `dspy` in exactly one function
(`answer`, the one model step) and nowhere else. Where this file says "DSPy
retrieval primitives," it is cataloguing what the nine repositories teach, not
describing something `graphrag.py` calls.

## In this repository

### `graphrag.py`, end to end

Four steps, run by `retrieve()` (`scripts/graphrag.py`):

| step | function | mechanism |
|---|---|---|
| 1. seed | `seeds()` `scripts/graphrag.py` | folded containment via `fold()` — no embeddings, nothing guessed |
| 2. spread | `pagerank()` `scripts/graphrag.py` | personalized PageRank over `graph.py`'s typed edges |
| 3. select | `select_mmr()` `scripts/graphrag.py` | MMR with a relevance floor — the *Selection* section below |
| 4. return | the dict `retrieve()` builds | quotations, conflicts, questions, documents, unread routes — never prose |

**Seeding** (`scripts/graphrag.py`): for every term page, for every
surface `wiki_index` folds to it, a folded substring match scores
`1.0 + len(f)/100` (a small bonus for the longer surface); failing that, a
bare token overlap scores `0.5 × (shared tokens / that surface's own tokens)`.
The best-scoring surface per page wins. **`fold()` is not a stemmer**: it
strips the leading article, case and diacritics, but `Kern-Welt` and
`Kern-Welten` do not fold together (`scripts/wiki_index.py`), so a plural
question does not, by itself, seed its singular's page — plurals and
inflections are among `fold()`'s recorded misses, and
`python3 scripts/trainset.py` prints each. With
`glosses` (only in the `ppr+gloss` method), a corpus-stated `A (B)` pairing can
also seed the German page at a fixed `GLOSS_WEIGHT=0.6`, but only when nothing
scored higher — "a gloss routes, it does not name"
(`scripts/graphrag.py`).

**Spreading** (`scripts/graphrag.py`): every typed edge becomes two
directed walk edges (both ways), weighted by `WEIGHTS`; personalized PageRank
restarts at the seed distribution, walks `ITERATIONS=40` fixed steps (no
convergence check), and returns dangling mass to the seeds rather than losing
it.

| constant | value | role |
|---|---|---|
| `WEIGHTS` | `links` 1.0, `contests`/`raised_by` 0.8, `concerns` 0.5, `reads`/`cites`/`asks` 0.3 | per-edge-type weight in the walk |
| `DAMPING` | 0.85 | standard PageRank damping |
| `ITERATIONS` | 40 | fixed power-iteration count |
| `TOP_TERMS` | 8 | ranked term-pages that feed the evidence pool |
| `BUDGET` | 8 | quotations `select_mmr` returns |
| `DIVERSITY_LAMBDA` | 0.65 | λ in the MMR formula — see *Selection* |
| `MIN_RELEVANCE` | 0.15 | the relevance floor — see *Selection* |
| `MIN_SURFACE` | 4 | a folded surface or token shorter than this cannot seed or count toward relevance |
| `GLOSS_WEIGHT` | 0.6 | fixed seed weight for a gloss match |

**Selecting**: the evidence pool is every quotation with `status == "verified"`
(plus `"unchecked"` under `--unchecked`) on the top 8 ranked term-pages.
Each candidate's relevance is `0.5 × node_rank + 0.5 × cosine(query, quote)`
(`scripts/graphrag.py`) — half how central the *page* is in the graph, half
how much the *specific quotation* lexically overlaps the question. `select_mmr`
then picks up to `BUDGET` of them; redundancy is cosine similarity between
candidate quotations, never against the query.

### What it returns, and never returns

The pack `retrieve()` builds: `seeds`, `terms` (ranked pages with their
conflict, if any), `evidence` (quote, `doc`, `line`, `status`, `page`,
`section`, `relevance`), `not_selected` and `below_floor` counts, `conflicts`,
`questions`, `documents` the rank reached, and `unread_routes` — unread
documents naming a ranked term, from `graph.proposals()`'s entity layer, "a
model chose the name, code placed the line" (`scripts/graphrag.py`).

**No synthesis.** "`Agentic-Dspy-Rag`'s synthesizer merges sources into
unattributed prose, which is the operation this wiki exists to refuse"
(`scripts/graphrag.py`, P13). Every quotation is printed verbatim with
its `doc:line`; nothing here writes a sentence that spans two sources.

### `--answer`: the one model step, and it cannot quote

```python
class ChooseEvidence(dspy.Signature):
    """Wähle aus den nummerierten Belegen diejenigen, die die Frage beantworten.
    Schreibe keine Zitate ab und formuliere keine eigene Antwort: nenne nur die
    Nummern. Wo die Belege die Frage nicht beantworten, nenne die Lücke in `gaps`.
    Widersprechen sich Belege, wähle beide."""
    question: str = dspy.InputField()
    evidence: str = dspy.InputField(desc="nummerierte, zitierte Belege")
    chosen: list[int] = dspy.OutputField(desc="Nummern der Belege, die antworten")
    gaps: list[str] = dspy.OutputField(desc="was die Belege nicht beantworten")
```
`scripts/graphrag.py`. The model sees the evidence numbered and
quoted; it returns `chosen: list[int]` and `gaps: list[str]`, never text. Code
prints the quotations those numbers point at — "a model that cannot type a
quotation cannot misquote one" (P26, applied to answering). An out-of-range
number is dropped and named in `invalid_numbers`, never silently kept.

Runs through `lmrun.call`, so the cache is off and the call is recorded
(`scripts/graphrag.py`). `--dry-run` uses `lm_fixture.FixtureLM` with a
scripted `chat(chosen="[1, 2, 99]", ...)` reply and writes into a throwaway
temp directory — "a rehearsal leaves no record in `Plan/runs/`"
(`scripts/graphrag.py`). A real run needs `--model` and `--approval`, or
the call is refused with a usage message (exit 2). Run live here:

```
$ python3 scripts/graphrag.py ask "Wie hängen die Guardians mit AEGIS zusammen?"
Seeds: `guardians` via „guardians", `aegis` via „aegis", …
## Pages, by graph rank
- 1.00  [[aegis|AEGIS]] — conflict: C1, C8
- 0.84  [[guardians|Guardians]] — conflict: C4, C6
…
## Evidence — 8 verified quotations, 292 not selected (191 below the relevance floor)
1. „AEGIS und die zwei Guardians sprechen in 3. Person" ^[kohaerenz-protokoll-storyform-und-outline-2026-06-10-md.md:L206]  …
## Sources disagree here — read the record before using the evidence
- C1 — AEGIS: expansion of an acronym
- C6 — Guardians and Kern-Welten: one arrangement, two versions a year apart …
```
(run 2026-09-24, this repository, trimmed). `--answer --dry-run` on the same
question chose evidence 1 and 2, dropped the scripted `99` as
`invalid_numbers`, and printed `Probelauf — keine echte Auswahl` as its gap.

**Nothing here has sent a real call yet.** `graphrag.py ask "…" --answer` is
one of three model runs that are each one command away and each wait on the
author's yes, because each sends corpus words to OpenRouter (`NOW.md`, *Which
model runs are allowed*). **How far `--answer` may ever go is undecided by
design**: "whether an answer should ever be more than chosen quotations — a
framing sentence, a summary marked as the model's — is the author's to decide,
and nothing builds it until then" (`NOW.md`).

**`--answer` is one call, not a session**, so nothing here needs the pattern
`dspy-session` teaches for keeping bulky retrieval out of a conversation:

```python
session = sessionify(dspy.Predict(RAGAnswer), exclude_fields={"context"}, max_turns=10)
# history messages keep question/answer; turn.inputs still holds the full context
```
`exclude_fields` drops a named input from what the model sees as history while
`turn.inputs` still records it for training data; `history_input_fields` is the
allow-list form, and where a field is in both, `exclude_fields` wins
(`dspy-session:README.md:239-299`,
`dspy-session:dspy_session/session.py:1024-1034`). Each
`--answer` call builds its own numbered-evidence prompt fresh from `pack`, with
no accumulated turns to bloat — the pattern waits for a multi-turn `ask`, which
does not exist yet (see *Not taken*).

### `bench`: what it scores, and what it does not

`cases()` (`scripts/graphrag.py`) reads the wiki's own labels: each
question's `raised_by` pages and each conflict's `pages` become gold sets.
`without()` (`scripts/graphrag.py`) removes the case's own node and
edges first, so a case cannot retrieve itself. `bench()` scores three methods
— `seeds` (folded containment alone, the floor), `ppr` (personalized
PageRank), `ppr+gloss` — as `recall@8 = |got ∩ gold| / |gold|` over the top 8
ranked term-pages, plus precision.

| method | recall@8, current |
|---|--:|
| seeds only | 47 <!--state:graphrag.recall_seeds-->% |
| personalized PageRank | 66 <!--state:graphrag.recall_ppr-->% |

over 20 <!--state:graphrag.cases--> cases (`python3 scripts/state.py --get
graphrag.cases`). `ppr+gloss` scores identically to `ppr` — no bench case is
English-only, so a gloss changes nothing here; the case it exists for is
`graphrag.py selftest`'s own English-question check.

**What the number is not.** "Seventeen cases, written by the same hand that
wrote the pages, so the labels and the graph share an author" (P27 applies:
this is agreement with one author, not ground truth). `Q2` finds no seed at
all — its question names „the seven protocol terms" and none of them by
surface. Precision reads low wherever a conflict has one gold page, because 8
pages are always returned. "It says the graph adds something over lexical
seeding; it does not say the retriever is good"
(`Plan/concept/graphrag_2026-09-23.md`).

**The recorded baseline is a point in time, not the live number.**
`Plan/runs/baselines.jsonl`'s `graphrag-retrieval` rows were written at `n=14`
(seeds 45.3%, ppr 62.0%) after document 8's C7–C10; document 9's C11 and C12
and the author's C6 decision (Q5) then grew the bench to 17 without a record,
and the rows caught up on 2026-09-24, after document 14 (seeds 41.9%, ppr
62.9%). They fall behind
again whenever a question or conflict is added, until `graphrag.py bench
--record` runs; the state above is what `python3 scripts/state.py` and a fresh
`graphrag.py bench` both report right now.

```bash
python3 scripts/graphrag.py bench [--k 8] [--record]   # --record appends to Plan/runs/baselines.jsonl
python3 scripts/graphrag.py selftest                   # 9 of 9 cases hold, exit 0
```

### `graphrag.py` vs `qmd.py` — two retrievals, not one

`scripts/qmd.py`'s whole role is to shell out to the `qmd` binary and hand
back a typed `Hit` — `collection`, `path` resolved to a real file, `line`,
`score`, `title`, `snippet` — plus `hit.document()`, the one handoff into
`subject.py`'s measured world. **A `Hit` carries where to look and no claim
about the corpus** (`scripts/qmd.py`); the module deliberately makes
the search→measurement handoff a visible step rather than something a caller
can skip. This is BM25/vector search over the repository's markdown, sitting
entirely outside `graphrag.py`'s pipeline: qmd never appears in
`graph.py`, `graphrag.py`, or `reconcile.py`.

**A search result is never a number.** `.claude/skills/qmd/SKILL.md` states
this as the load-bearing rule and measures it: `Kernwelt` occurs in 144 of 346
landed documents, but a 40-hit search list is not that census — the line that
defines `KW1` sits at line 152 of its document and is outside the top 40,
because BM25 favours short, early chunks (`.claude/skills/qmd/SKILL.md`).
**Nothing in the wiki-building pipeline depends on qmd**: `reconcile.py`
answers by lookup against `Wiki/index.json`, so its cost stays
`O(census) + O(judgement)`, never `O(corpus)`; a qmd hit finds candidates to
read, it decides nothing (`CLAUDE.md`, *Searching the corpus*). `state.py` has
no `qmd.*` measurement at all — there is nothing for the rule to be checked
against, by construction.

## DSPy retrieval primitives

**`graphrag.py` calls none of these.** They are catalogued here because the
skill teaches DSPy 3.3.1, not because the pipeline uses them.

`api.md` has `dspy.Embedder(model, batch_size=200, caching=True)` and
`dspy.Embeddings(corpus, embedder, k=5, callbacks=None, cache=False,
brute_force_threshold=20000, normalize=True)`. **Note the flag name and
default change between the two**: `Embedder.caching` defaults `True`,
`Embeddings.cache` defaults `False` — the same word, two parameters, two
opposite defaults. `api.md`'s surface list stops there; the rest of this
topic's DSPy surface, checked directly against the installed package:

```surface
dspy.Retrieve(k=3, callbacks=None)
dspy.ColBERTv2(url='http://0.0.0.0', port=None, post_requests=False)
dspy.EmbeddingsWithScores(corpus, embedder, k=5, callbacks=None, cache=False, brute_force_threshold=20000, normalize=True)
```
`EmbeddingsWithScores` is a subclass of `Embeddings`, same constructor, and its
`forward` adds `scores` to the returned `Prediction` alongside `passages` and
`indices` (`dspy:retrievers/embeddings.py:242-261`). Neither `Retrieve` nor
`ColBERTv2` carries a deprecation warning in 3.3.1
(`dspy-agent-skills:skills/dspy-retrieval/reference.md:129-135`).

- **FAISS threshold**: `Embeddings` builds an `IndexIVFPQ` over an
  `IndexFlatL2` quantizer only at or above `brute_force_threshold` (20,000
  passages); below it, brute-force search. Missing `faiss-cpu` above the
  threshold raises exactly `"Please \`pip install faiss-cpu\` or increase
  \`brute_force_threshold\` to avoid FAISS."` (`dspy:retrievers/embeddings.py:78`).
- **Persisted indexes**: `search.save(path)` writes `config.json`,
  `corpus_embeddings.npy` and, if built, `faiss_index.bin`.
  `Embeddings.from_saved(path, embedder)` is a **classmethod**
  (`dspy:retrievers/embeddings.py:209-210`) — `dspy-agent-skills`'s own
  `dspy-agent-skills:skills/dspy-retrieval/reference.md:18` calls it a
  staticmethod, which is wrong.
- **An index manifest** (recipe, not built here): persist embedding model id,
  chunk-rule version, corpus hash and build time beside the index, and compare
  on load — "mismatch means rebuild — never 'probably fine'"; nothing raises if
  two models' vectors get mixed otherwise
  (`dspy-agent-skills:skills/dspy-retrieval/reference.md:56-59,87-99`).
- **Chunking** (claim, unmeasured here): one idea per passage, 100–500 words,
  10–20% overlap, prefix each chunk with its title or section, chunk
  deterministically and version the rule
  (`dspy-agent-skills:skills/dspy-retrieval/reference.md:74-85`).
- **A local embedder**: `dspy.Embedder(SentenceTransformer("all-MiniLM-L6-v2").encode)`
  — it must accept `list[str]` and return a 2D array
  (`dspy-agent-skills:skills/dspy-retrieval/SKILL.md:89-94`).
- **The retriever-interface pattern**: "any callable returning an object with
  `.passages`. That is the entire interface … Swapping the backend changes one
  line" (`dspy-agent-skills:skills/dspy-book-agents/SKILL.md:74-77`).
  `graphrag.py`'s own retriever has the same single-seam shape — one
  `retrieve(query, ...) -> dict` — but the dict carries evidence records, never
  bare `.passages`, because a passage without its verdict and citation is not
  what this wiki serves.
- **Two traps neither of which applies here, and why**: copying `MultiHopQA`'s
  `dspy.ColBERTv2(url="http://20.102.90.50:2017/wiki17_abstracts")` "pointed at
  a public endpoint that is frequently unreachable"
  (`dspy-agent-skills:skills/dspy-book-metrics/SKILL.md:137`); an external
  vector store where "vector dimensions, vector name, embedding model and
  document field must all match... or retrieval silently returns nothing
  useful" (`dspy-agent-skills:skills/dspy-book-agents/SKILL.md:79-81`). Both
  are moot for `graphrag.py`: the corpus lives on disk in this repository, and
  nothing here calls a remote retrieval endpoint.

## Selection: MMR and the relevance floor

### The formula, and which way λ points

Three implementations of the same idea, two conventions that are mirror
images of each other under λ ↦ 1−λ
(`Plan/concept/dspy-extract_2026-09-24/details-drg-mmr.md`, section B.1):

| | upstream `dspy-refrag` | `dspy-agent-skills` (`kp_canon_retriever.py`) | `graphrag.py` |
|---|---|---|---|
| formula | `mmr = λ·relevance − (1−λ)·redundancy` | `score = (1−λ)·relevance − λ·redundancy` | `score = (1−λ)·relevance − λ·redundancy` |
| λ weights | **relevance** (higher λ → *less* diverse) | **diversity** (higher λ → *more* diverse) | same as `kp_canon_retriever.py` |
| default λ | 0.5 | 0.65 | 0.65 |
| floor field | `min_score` | `min_relevance` | `min_relevance` |
| floor applied inside MMR? | **no** — only in the `SIMILARITY` strategy | yes, before the loop | yes, before the loop |

`select_mmr`'s body, verbatim (`scripts/graphrag.py`):

```python
def select_mmr(relevance, similar, budget=BUDGET,
               diversity_lambda=DIVERSITY_LAMBDA, min_relevance=MIN_RELEVANCE):
    remaining = [i for i, r in enumerate(relevance) if r >= min_relevance]
    chosen = []
    while remaining and len(chosen) < budget:
        best, best_score = remaining[0], -math.inf
        for i in remaining:
            redundancy = max((similar(i, j) for j in chosen), default=0.0)
            score = (1 - diversity_lambda) * relevance[i] - diversity_lambda * redundancy
            if score > best_score:
                best, best_score = i, score
        chosen.append(best)
        remaining.remove(best)
    return chosen
```
Identical in shape to `dspy-agent-skills:scaffolding/kp_canon_retriever.py:92-143`,
generalised to take precomputed relevance and a similarity callable instead of
raw vectors (`scripts/graphrag.py`). **Even upstream gets its own
convention backwards once**: `dspy-refrag`'s own `example_usage()` labels
`diversity_lambda=0.7` "High diversity," but by its own formula (line 166 of
`sensor_advanced.py`) λ=0.7 weights relevance more and redundancy less — that
is *less* diverse than the 0.5 default, not more
(`Plan/concept/dspy-extract_2026-09-24/details-drg-mmr.md`, B.1). The pack's
own `dspy-agent-skills:skills/dspy-refrag/reference.md:56` makes the matching
error in the other direction, describing upstream's `diversity_lambda` as
"higher favours diversity over relevance," which is true of the pack's own
port and false of the file it is documenting.

### The measured failure without a floor

The fixture is four passages — two near-duplicates, one relevant-but-distinct,
one unrelated — and the failure is that unguarded MMR can prefer the unrelated
one to the near-duplicate's more distant relevant cousin, because zero
relevance with zero redundancy outscores high relevance with high redundancy.
Measured twice, against `graphrag.py`'s real `select_mmr` (not a
reimplementation), on two fixtures
(`Plan/concept/dspy-extract_2026-09-24/details-drg-mmr.md`, B.2):

| fixture | floor | picks below the crossover | picks at/above it |
|---|---|---|---|
| A — this file's own `selftest()` (`relevance=[0.9,0.88,0.6,0.0]`) | off | λ≤0.35 dup+dup; **0.40–0.54 dup+distinct** | λ≥0.55 dup+**unrelated** |
| A — same fixture | on (0.15) | λ≤0.35 dup+dup | λ≥0.40 dup+distinct, **never flips**, up to λ=1.0 |
| B — the reader's original vectors | off | λ≤0.498 dup+dup | λ≥0.50 dup+**unrelated** |
| B — same vectors | on (0.15) | λ≤0.53 dup+dup | λ≥0.534 dup+distinct |

Fixture B never reaches the relevant-distinct passage without the floor, at
any λ tested 0.0–1.0. The floor is not universally decisive, though: for
λ≤0.35–0.47 both fixtures pick the duplicate pair whether or not the floor is
on — the floor only changes the outcome once λ is high enough to already favour
diversity over the duplicate.

**`min_score` is real upstream, and MMR never reads it.** Freshly run against
the actual `AdvancedSensor.select`: identical output with and without
`min_score=0.15` at every λ tested for the `MMR` strategy, while the same flag
correctly filters under the `SIMILARITY` strategy
(`Plan/concept/dspy-extract_2026-09-24/details-drg-mmr.md`, B.1, B.2). So
"vendor `sensor_advanced.py`" (`dspy-agent-skills:skills/dspy-refrag/SKILL.md:143`)
does not by itself hand you a working floor for MMR — `graphrag.py`'s
pre-loop filter (`scripts/graphrag.py`) is not upstream's; it is
`kp_canon_retriever.py`'s own addition, ported forward.

### Does `graphrag.py`'s docstring match its code?

**Yes, and it did not always.** The module docstring now states the fixture
boundary precisely: "at every λ from 0.5 to 0.8 — on this file's own selftest
fixture from 0.55" (`scripts/graphrag.py`), and `select_mmr`'s own
docstring states the formula and the upstream contrast directly: "The score is
`(1 - λ) · relevance - λ · redundancy`: λ weights diversity. Upstream
dspy-refrag writes `λ · relevance - (1 - λ) · redundancy` and never applies its
`min_score` inside MMR" (`scripts/graphrag.py`). The
`DIVERSITY_LAMBDA` comment states the two conventions' relationship rather than
comparing raw numbers: "λ weights diversity here and relevance in upstream
dspy-refrag, so this is upstream's 0.35" (`scripts/graphrag.py`).

That correction is the direct output of the verification in
`Plan/concept/dspy-extract_2026-09-24/details-drg-mmr.md` (section B), which
found the version before it comparing "above upstream's 0.5" — "arithmetically
correct and semantically misleading in the same breath," since the two λ's run
in opposite directions and 0.65 here corresponds to upstream's 0.35, not
something above its 0.5. `graphrag.py selftest` still passes 9 of 9 after the
fix, because only the prose changed, never the formula.

### The rest of the package, left behind

Beyond MMR-with-a-floor, `dspy-refrag` is not adopted: `FAISSRetriever` and
`PineconeRetriever` raise `NotImplementedError`; the `weaviate-client` pin
conflicts with its own v4-only import; the package needs `psycopg2` just to
import; LM errors are swallowed into an `"Error calling LM: ..."` string; and
its `UNCERTAINTY` strategy is non-deterministic (unseeded
`np.random.choice`) while `ENSEMBLE` silently ignores your λ, temperature and
floor (`dspy-agent-skills:skills/dspy-refrag/reference.md:75-88`,
`Plan/concept/dspy-extract_2026-09-24/das-rlm-rag.md`, TRAP). **The headline
feature — context compression — is also missing**: selection is computed and
annotated, but the prompt is still built from every passage:

```python
context_str = "\n".join(
    f"Passage {i}: {p['text']} (selected: {p.get('selected', False)})" ...
)
```
(`dspy-agent-skills:skills/dspy-refrag/SKILL.md:47-48`). "Token cost is
identical to passing everything" — the fix is prompt assembly from
`selected_idxs` only, roughly ten lines
(`dspy-agent-skills:skills/dspy-refrag/SKILL.md:43-51`). This matches the
toolchain's own conclusion for every package scanned: nothing was installed —
"the value is a pattern of 10–60 lines, and the package would bring a DSPy
pin, a Python floor, a key requirement or a runtime this project does not need"
(`Plan/concept/dspy-toolchain_2026-09-23.md`).

## Multi-hop and budget control

**`graphrag.py` is single-hop.** One query, one seed pass, one PageRank spread,
one MMR selection — nothing re-queries from what was retrieved. The
repositories describe two shapes for when that stops being enough:

- **Agent-controlled**: `dspy.ReAct("question -> answer, sources: list[str]",
  tools=[...], max_iters=12)` — the model decides when to stop, cost varies.
- **Fixed-depth**: a loop of `num_hops` (default 3, no early exit) over three
  predictors — `question, notes -> query`; `question, notes, context ->
  new_notes: list[str]`; `question, notes -> answer` — for a predictable
  retrieval budget.

Both from `dspy-agent-skills:skills/dspy-book-agents/SKILL.md:83-94`,
`dspy-agent-skills:skills/dspy-book-agents/reference.md:72-85`. **Dedupe
between hops, or hop two re-retrieves hop one**:
`list(dict.fromkeys(existing + new))`
(`dspy-agent-skills:skills/dspy-book-agents/example_agent_budget.py:95-97`).
`dspy-retrieval`'s own multi-hop recipe adds: generate the next query from the
context accumulated so far, cap at 2–3 hops, log the query per hop — "a
degenerate second query that merely restates the first is the most common
multi-hop failure" — and optimize the query generator against the *retrieval*
metric, never the answer metric
(`dspy-agent-skills:skills/dspy-retrieval/SKILL.md:96-123`). A rough sizing
table for `max_iters`: 5 for a narrow check, 8 moderate, 12 broad, 15 for open
research (`dspy-agent-skills:skills/dspy-book-agents/example_agent_budget.py:19`).

## RAG shapes in the nine repositories

### classify → route, and the free-text trap

`Agentic-Dspy-Rag`'s pipeline: optional history condensation → classify intent
→ route → inside the chosen agent, expand the query (up to 3 rephrasings) →
retrieve (k=20 per query, pooled and deduplicated) → rerank (a second
bi-encoder) → generate
(`Agentic-Dspy-Rag:src/agentic_rag/components/agents.py:18-59`,
`Agentic-Dspy-Rag:src/agentic_rag/main.py:113-152`). The routing itself:

```python
def forward(self, question):
    prompt = f"Classify the user's question. Choices: Factual, Comparative, Multi-step. Question: {question}"
    intent_prediction = self.classifier(question=prompt)
    user_intent = intent_prediction.intent
    if "Comparative" in user_intent:
        prediction = self.comparative_rag_agent(question=question)
    elif "Multi-step" in user_intent:
        prediction = self.multi_step_rag_agent(question=question)
    else:
        prediction = self.simple_rag_agent(question=question)
    prediction.intent = user_intent
    return prediction
```
(`Agentic-Dspy-Rag:src/agentic_rag/components/agents.py:107-127`, condensed).
Both the classifier prompt and a later rephraser prompt are smuggled in as the
*value* of an input field rather than the signature's instructions, so neither
can be optimized and the field carries no constraint
(`Agentic-Dspy-Rag:src/agentic_rag/components/agents.py:109-110`,
`Agentic-Dspy-Rag:src/agentic_rag/components/data_modules.py:46-47`). Measured
offline, with scripted classifier outputs:

| classifier output | routed to | correct? |
|---|---|---|
| `Comparative` | ComparativeRAG | yes |
| `comparative` | SimpleRAG | **no** |
| `Multi-Step` | SimpleRAG | **no** |
| `Not Comparative` | ComparativeRAG | **no** — negation |
| `Multi-step (Comparative)` | ComparativeRAG | **no** — check order |

every miss silent, because the `else` defaults to Factual
(`Agentic-Dspy-Rag:src/agentic_rag/components/agents.py:109-123`). The fix
verified on 3.3.1: a `Literal["Factual","Comparative","Multi-step"]` output
field, which the adapter rejects off-list — this is the general shape `api.md`
already states for this repository's own decisions (`pairs.py`'s `Literal`
decision). `--answer`'s own `chosen: list[int]` is the same discipline: a typed
field the adapter parses or refuses, never a string a caller greps.

**One more trap worth naming, since it bears directly on P13**: `MultiStepRAG`
answers each sub-question with `SimpleRAG`, then hands the synthesizer only the
assembled Q&A string — the retrieved *passages* are gone by the time an answer
is produced (`Agentic-Dspy-Rag:src/agentic_rag/components/agents.py:73-90`).
`graphrag.py` cannot do this: it never assembles an answer at all, so there is
no synthesis step for the evidence to disappear into.

### Self-corrective TARA: a 4D score and progressive leniency

`dspy-tara-rag`'s seven tools (the README says six):
`search_passages`/`search`, `decompose_query`/`decompose`,
`evaluate_passages`/`evaluate`, `get_passage_detail`/`inspect`,
`list_document_sections`/`structure`, `get_terminology`/`terminology`,
`calculate` (`dspy-agent-skills:skills/dspy-tara-rag/reference.md:26-39`). Its
evaluator scores four independent dimensions rather than one:

```python
@dataclass(frozen=True)
class ContextScore:
    """The 4D assessment. Each dimension localizes a different failure."""
    relevance: int    # 0-30
    coverage: int     # 0-25
    specificity: int  # 0-25
    sufficiency: int  # 0-20

    @property
    def total(self) -> int:
        return self.relevance + self.coverage + self.specificity + self.sufficiency

    def weakest(self) -> str:
        """Which dimension to act on — the point of scoring four instead of one."""
        fractions = {"relevance": self.relevance / 30, "coverage": self.coverage / 25,
                     "specificity": self.specificity / 25, "sufficiency": self.sufficiency / 20}
        return min(fractions, key=fractions.get)
```
(`dspy-agent-skills:skills/dspy-tara-rag/example_tara.py:34-65`, condensed —
the range-validating `__post_init__` is omitted). It emits `action`
(`output`/`refine`/`route_to_agent`) plus `keywords_to_add`,
`keywords_to_remove` and `suggested_query`, "so a failing score carries its own
repair instruction" (`dspy-agent-skills:skills/dspy-tara-rag/SKILL.md:64-66`).

**Progressive leniency is the anti-pattern, stated three times with three
different numbers**: `effective_threshold = max(quality_threshold - retry*5,
20)` (default 40, 3 retries) — the skill's own SKILL.md claims "only a context
below 20 is ever routed away," but its own shipped example computes 22 total
routed away at retry 3, so the floor of 20 is reached only at retry 4
(`dspy-agent-skills:skills/dspy-tara-rag/SKILL.md:68-83`,
`dspy-agent-skills:skills/dspy-tara-rag/example_tara.py:81-86,115,137-139`).
Upstream's real behaviour is looser still: `self-corrective-rag`'s loop always
outputs a context on the final
retry, and on diminishing returns, regardless of score — `route_to_agent`
only fires at zero passages
(`Plan/concept/dspy-extract_2026-09-24/das-rlm-rag.md` TRAP, *TARA outputs any context*). "Decide
deliberately whether 'eventually accept something mediocre' is the behaviour
you want" (`dspy-agent-skills:skills/dspy-tara-rag/SKILL.md:82-83`) — this is
P15's distinction stated as a design choice: a retry ladder that ends by
lowering the bar can no longer say "not answered," only "answered badly."
`graphrag.py`'s own floor is the opposite shape: `min_relevance` excludes a
candidate outright rather than admitting it at a lower bar, and nothing here
retries with a softened threshold.

### REFRAG: selection without compression

Covered under *Selection* above — the formula and floor are what this
repository took; the rest, including the missing prompt-compression step and
the non-deterministic/ignoring-your-config strategies, was read and left.

### LanceDB: schema, hybrid fusion, and where it silently degrades

`dspy-agents`' schema: `chunk_id, doc_path, domain, title, chunk_index,
content, content_tokens, content_hash, source_signature, embedding
fixed_size_list<float32, dim>`, upserted with
`merge_insert("chunk_id").when_matched_update_all().when_not_matched_insert_all()`
(`dspy-agents:skills/rag/lancedb_store.py:361-406,561-568`). Its "hybrid" fusion
does not normalize before combining:

```python
if v_weight > 0:
    for row in table.search(embedding[0]).limit(limit * 3).to_list():
        score = 1.0 / (1.0 + float(row.get("_distance", 0.0)))   # bounded (0, 1]
        vector_results[row["chunk_id"]] = (row, score)
if s_weight > 0:
    try:
        rows = table.search(query, query_type="fts").limit(limit * 3).to_list()
    except RuntimeError:
        rows = []                                                 # FTS missing — silently vector-only
    for row in rows:
        scalar_results[row["chunk_id"]] = (row, float(row.get("_score", 0.0)))  # raw BM25, unbounded

for chunk_id, (row, score) in vector_results.items():
    scores[chunk_id] = (row, score * v_weight)
for chunk_id, (row, score) in scalar_results.items():
    prev_row, prev_score = scores.get(chunk_id, (row, 0.0))
    scores[chunk_id] = (row, prev_score + score * s_weight)
```
(`dspy-agents:skills/rag/lancedb_store.py:485-517`, condensed). An unbounded
BM25 `_score` is added straight to a `(0, 1]` vector score at equal default
weights. **And the FTS leg is silently absent** in the repo's own
environment — `tantivy`/`pylance` are not in `requirements.txt`, the resulting
`ImportError` is logged at DEBUG, and "hybrid" degrades to vector-only with no
visible sign (`dspy-agents:skills/rag/lancedb_store.py:428-450,496-501`).
Separately, one changed mtime forces re-embedding of the **whole** corpus,
because `source_signature` is corpus-wide, not per file
(`dspy-agents:skills/rag/lancedb_store.py:264,642`), and the runtime guard that
should catch a stale index is itself skipped whenever the offline docs are
missing or empty (`dspy-agents:skills/rag/lancedb_runtime.py:143-199`).

`graphrag.py`'s own fusion avoids the un-normalized-hybrid trap by
construction rather than by design intent: `node_rank` is divided by the
ranked set's own peak (`scripts/graphrag.py`) and `cosine()` returns a
value in `[0, 1]` for the non-negative term-count vectors it is given
(`scripts/graphrag.py`), so the `0.5/0.5` blend combines two quantities
on the same scale.

## Knowledge graphs

### `graph.py`: the typed graph this repository actually has

Every node and edge is read out of files that already exist; nothing is
extracted or inferred by a model (`scripts/graph.py`, decision 005).

| node | from |
|---|---|
| `term:<slug>` | a page in `Wiki/candidates/` |
| `doc:<slug>` | a document a page reads or cites |
| `conflict:<Cn>` | `Wiki/conflicts/` |
| `question:<Qn>` | `Wiki/questions/` |

| edge | stated by |
|---|---|
| `links` | `[[slug]]` — the only term→term edge |
| `reads` | a page's `ingested:` |
| `cites` | `^[slug.md:Lnn]`, every cited line |
| `contests` | a conflict's `pages:` |
| `raised_by` | a question's `raised_by:` |
| `asks` | a question's `documents:` |
| `concerns` | a question's `conflict:` |

**Every edge carries `via: file:line`** (`scripts/graph.py`), and
`evidence_of()` (`scripts/graph.py`) attaches every page's quotations
with the same verdict `quotes.py` itself checks with (`quotes.pairs` /
`quotes.verdict`, unified after the graph's own first pairing found 14
unresolved where the checker found 4 — `NOW.md`). `--check`
(`scripts/graph.py`) compares the graph against the filesystem (P7,
P8): an edge to a page that does not exist, a document no manifest row lands.
Exports: `--json`, `--graphml`, `--triples`, `--around <term> --hops N
[--mermaid]`.

**Current counts**: 155 <!--state:graph.nodes--> nodes,
2195 <!--state:graph.edges--> edges; the evidence layer holds
3179 <!--state:graph.evidence--> quotations, of which
3179 <!--state:graph.evidence_verified--> verify against their cited line.

**The graph is not a third layer** (P20): it is derived on every call, about
0.4s, exactly like `Wiki/index.json`, and holds no content a page does not
already hold. Repair it by fixing the page and re-deriving, never by hand
(P25) — `Plan/concept/graphrag_2026-09-23.md`.

### `graph.proposals()`: entities and glosses, kept apart

A second layer, explicitly never merged into `build()`'s graph
(`scripts/graph.py` asserts, in `--selftest`, that `names` and
`folds_to` edges never leak into the core edge set). Two kinds:

- **entities** — every name in a `Plan/entities/<slug>.md` list that passes
  `entities.py verify()` as a reading, with the document line that names it —
  "a model chose the name, code placed the line" (`scripts/graph.py`).
  An entity whose fold matches a page surface gets a `folds_to` edge.
- **glosses** — from `Plan/runs/bilingual/stated.jsonl`, the `A (B)` shape
  written in `GLOSS_MIN_DOCS=2`+ documents where exactly one side is a page
  surface. **The relation is unjudged** — `Kael (Host)` is a role, not a
  synonym — so a gloss may route a question to a page (`--gloss`) and is
  always labelled as a gloss; it never merges a surface into a page
  (`scripts/graph.py`, P13). A surface glossing two different pages
  (`Ordnung` → Kohärenz and AEGIS) is dropped: "says nothing about which"
  (`scripts/graph.py`).

**Current counts**: 300 <!--state:proposals.entities--> entities from lists
that verify as readings, 53 <!--state:proposals.entities_paged--> of them
folding to a page, 195 <!--state:proposals.glosses--> glosses.

### drg-kg: what it would do, and why it is not used that way

`drg-kg` builds an `EnhancedKG` from a declarative schema plus DSPy-backed
extraction; its own boundary statement: "DRG is **not** a GraphRAG, RAG or
retrieval stack. It produces a graph artifact"
(`dspy-agent-skills:skills/dspy-drg-kg/SKILL.md:20-24`). Relevant defaults:
`extract_typed`'s `enable_implicit_relationships` is **`True`** by default —
"it adds LLM-inferred edges you did not state" — and
`prune_isolated_nodes=True` in `build_enhanced_kg`
(`dspy-agent-skills:skills/dspy-drg-kg/SKILL.md:84-88,97-103`). Windowed
extraction multiplies model calls without a flag once a document passes 6
chunks or 25 entities (`dspy-agent-skills:skills/dspy-drg-kg/SKILL.md:128-135`).

**This repository is installed for exactly one module — the evaluation
scorer — never extraction**: `from drg.evaluation._runner import _score_sets`
(`scripts/rlm_ingest.py`, its `score()` function). `_prf` is
non-vacuous by construction — `precision = tp/(tp+fp)`,
`recall = tp/(tp+fn)`, `f1 = 2pr/(p+r)`, each `0.0` on an empty denominator
(`Plan/concept/dspy-extract_2026-09-24/das-rlm-rag.md`, *Code worth keeping*) — unlike the retired
pipeline's `coverage()`, which returned 1.0 on no gold at all.

**What happens on import, measured freshly against `drg-kg==0.0.0.dev51`**:
the exact import `rlm_ingest.py` uses has **zero** side effects — `import drg`,
then `from drg.evaluation._runner import _score_sets`, then calling
`_score_sets(...)` — `dspy.settings.lm` stays `None`, `.env` is never read,
`litellm` is never reached, for the import or the call
(`Plan/concept/dspy-extract_2026-09-24/details-drg-mmr.md`, A.2). The
auto-configuring behaviour — reading `.env`, defaulting to
`openai/gpt-4o-mini`, calling `dspy.configure(lm=lm)` even with
`DRG_REQUIRE_LM` set — is real and was reproduced on the same install, but it
lives entirely behind `drg.config.configure_lm()`, reached only through
`drg.extract`'s own auto-config path (`drg/config.py`, `drg/extract/__init__.py`)
— a path `drg.evaluation._runner` never imports and this repository's one call
site never reaches (`Plan/concept/dspy-extract_2026-09-24/details-drg-mmr.md`,
A.2–A.3). **`drg-kg` is not currently installed in this container's
`.venv-dspy`** — `ModuleNotFoundError: No module named 'drg'`, checked here —
consistent with venvs not surviving a container; `rlm_ingest.py score()`
already handles that case with a plain `SystemExit`. A verified ~30-line
stdlib reimplementation of `_score_sets` exists as a fallback if a future
release ever routes the scorer through `drg.config`
(`Plan/concept/dspy-extract_2026-09-24/details-drg-mmr.md`, A.3).

### Decision 005, mechanically enforced

**A link is never inferred.** "Every one of the 133 links marks a term the
prose already wrote; no edge was invented"
(`Plan/decisions/005-the-wiki-links.md`). The same rule, restated for the
typed graph: "a guessed edge is indistinguishable from a stated one once it is
in the graph" (`scripts/graph.py`). It is checked, not only asserted:
`graph.py --selftest` fails if the proposal layer's `names`/`folds_to` edges
ever appear in `build()`'s core edge types (`scripts/graph.py`), and
`graphrag.py selftest` checks the entity-route case separately
(`scripts/graphrag.py`). This is why `drg-kg`'s extraction and graph
layers stay unused here even though the package is installed: a canon link is
written by a person, never inferred by a model.

## Scoring retrieval

### Recall, separate from answers

```python
def recall_at_k(gold, pred, trace=None, pred_name=None, pred_trace=None):
    """Fraction of gold passages retrieval surfaced; GEPA-compatible return."""
    got, want = {p.strip() for p in pred.context}, {p.strip() for p in gold.gold_passages}
    score = len(got & want) / max(len(want), 1)
    missing = want - got
    feedback = (f"Missed {len(missing)} gold passage(s): {sorted(missing)[:2]}"
                if missing else "All gold passages retrieved.")
    return dspy.Prediction(score=score, feedback=feedback)
```
(`dspy-agent-skills:skills/dspy-retrieval/example_retrieval.py:103-113`, runs
on 3.3.1). The diagnosis this recipe is built for
(`dspy-agent-skills:skills/dspy-retrieval/SKILL.md:125-149`): low recall and
low answer accuracy points at the corpus or chunking; high recall with a low
answer score points at the generator or the context field's type; low recall
with a *high* answer score means the model is "answering from parameters" and
the context is not what it looks like. Other axes:
recall@k when every gold passage is needed, MRR when one passage suffices and
its rank matters, precision@k when the context budget is tight, hit rate as a
coarse smoke test (`dspy-agent-skills:skills/dspy-retrieval/reference.md:113-120`).

### `bench`, and what its number is not

`graphrag.py bench` is exactly this pattern, already built and already run:
recall computed against the wiki's own labels, never against an answer, with
the label's own node removed first so a case cannot retrieve itself. There is
no equivalent bench for `--answer`'s chosen numbers — nothing here scores
whether the model's `chosen: list[int]` was the right evidence against a gold
set; `bench` measures retrieval only. The caveats already given under *In this
repository* — one author for the labels and the pages (P27), Q2's zero-seed
case, precision depressed by the fixed 8-page window — are what stop the
recall number from being read as more than a floor the graph clears.

## Not taken, or waiting

| idea | source | waits for |
|---|---|---|
| `qmd bench` scored against a free fixture — every `Wiki/questions/` and `Wiki/conflicts/` record already states "a search finds this in `<slug>`" | brief; `Agentic-Dspy-Rag`'s retrieve-then-rerank, measured instead of assumed (`Plan/concept/dspy-toolchain_2026-09-23.md`) | the author's go-ahead — `qmd bench` (4 backends: `bm25`/`vector`/`hybrid`/`full`) has never been run on this corpus (`NOW.md`, *Which qmd backend*) |
| qmd hits as a second seed source for `graphrag.py`, measured against folded seeding alone | `Plan/concept/graphrag_2026-09-23.md`, *Next* item 2 | a `cites`-edge line some qmd hit also names — catalogued, not built |
| a model *proposing* a graph edge the prose does not state | `Plan/concept/graphrag_2026-09-23.md`, *Next* item 5 | measurement against the 42/64% bench baseline, never argued abstractly — would live in a separate file, never a page |
| `--answer` producing more than chosen quotations (a framing sentence, a marked-as-the-model's summary) | `NOW.md` | the author's decision; nothing builds it until then |
| wrapping `ask` in a session that keeps bulky evidence out of history (`exclude_fields`) | `dspy-session` | a multi-turn `ask` — today every `--answer` call is independent, so there is no history to bloat |
| a reviewed-page rule flagging a new source that contradicts a promoted page, never applying the flag | `dspy-agent-skills`'s `dspy-wiki-compile` (`decision_legal()`, weighted 0.30 citations / 0.25 decisions / 0.20 merge / 0.15 diffs / 0.10 links) | the first page promoted out of `Wiki/candidates/` — the promoted-page tier does not exist yet |
| a persisted `dspy.Embeddings`/FAISS index over the corpus | `api.md`, `dspy-retrieval` | not needed while folded containment plus a bag-of-words cosine clears the bench floor |
| multi-hop, iterative retrieval | `dspy-book-agents`, `dspy-retrieval` | a question the single-shot pipeline cannot answer in one pass — none recorded yet |
| `qmd mcp` (an MCP server wrapping `query`/`get`/`multi_get`/`status`) | — | decided against on the author's call: "a skill whose job is to describe every step should name commands, not tool calls... an MCP tool call is invisible in exactly the way this project's process artifacts exist to prevent" (`Plan/concept/skills_2026-09-17.md`) |
