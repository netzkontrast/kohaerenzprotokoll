# DRG-KG examples — what's worth stealing, and what is not

*2026-09-17. Every file under `netzkontrast/drg-kg/examples/` read (20 files:
`full_pipeline_example.py`, `evaluation_framework_example.py`,
`incremental_update_example.py`, `event_extraction_example.py`,
`multi_document_reasoning_example.py`, `query_layer_example.py`,
`temporal_query_example.py`, `optimizer_demo.py`, `mcp_demo.py`,
`api_server_example.py`, the three `quickstarts/*.py` scripts plus their
`README.md`, and the four `benchmarks/*.json`/`.py`/`.md` files), plus the two
docs an example points at (`docs/benchmarking.md` from
`examples/benchmarks/official_suite.json`, `docs/schema_design.md` from
`examples/quickstarts/README.md`).*

**Scope note before the findings.** `Plan/concept/continuous-improvement_2026-09-17.md`
already installed `drg-kg` and measured its evaluation module directly against
this repository — `_prf()`'s zero guards, `_score_sets()`'s alias lookup and
`false_negative_keys` feedback, and the document-5 hazard (a metric that scores
"found nothing" as 0.0 is right on a candidate list and wrong on a page count).
That work is done and this file does not repeat it. What is left to mine is the
rest of `examples/` — the graph, reasoning, merge, query, temporal, API-server
and optimizer demos — which that file correctly declined to use for extraction
or graph purposes but which I had not yet read end to end. This file is that
reading.

**The honest result: one thing worth building, one thing worth writing down as
grounding evidence against a rule already held, and a long rejected list.**
Most of `examples/` is a knowledge-*graph* toolkit — chunking, cross-document
merging, mechanised multi-hop inference, temporal validity windows, a
Neo4j-backed visualization server — built for a project that models the world
as a graph. This one deliberately does not (`CLAUDE.md`: "Two layers until a
third earns itself"), so most of it does not transfer, and I would rather say
that plainly than pad the catalogue.

---

## Worth building this week

### 1. A drift check between two `Plan/state.json` snapshots

**The idea**, from `drg/evaluation/_compare.py` (`compare_reports()`, lines
20–101, and `render_regression_markdown()`, lines 199–233) and demonstrated in
`examples/evaluation_framework_example.py` §6 (lines 158–171) and
`docs/benchmarking.md` ("Regression comparison" / `drg eval compare
--fail-on-regression`, lines 111–127): keep a baseline report, run a candidate,
diff every shared metric, and print a table of `metric | baseline | candidate |
delta | status` where `status` is `regressed` when the drop exceeds a named
threshold. Nothing here calls a model; it is a pure diff over two already-computed
numbers.

**Does it survive contact with this project's rules?** Only in a narrow form.
Most of what `Plan/state.json` measures already has a live pass/fail check that
does not need history at all — `quotes.py` exits 1 the moment `unresolved > 0`,
`judgements.py` prints `DISAGREES` the moment a mechanised rule stops holding,
`state.py --check` fails the moment the artifact drifts from a fresh derivation.
Building a second, history-based version of those would be **P6** twice over —
restating a rule a tool already enforces — and it would create a stored number
(the baseline snapshot) that competes with "state is derived, never stored"
if anyone started treating the old snapshot as ground truth rather than a diff
input.

But two of the counts this repository already names as open gaps have **no**
absolute pass/fail line, because there is not supposed to be one: `wiki.orphans`
(21 of 46) and `relations.py --unmarked` (158) can both go up for a perfectly
good reason — a new page that has not been linked into yet, prose that has not
been marked yet — so a hard threshold on either would be exactly the kind of
check `PRINCIPLES.md` warns against, one that reports the same known-good class
forever (P14) or asserts something false about "should never happen" (P9's
sibling problem, applied to a threshold instead of a dependency). What is
missing is not a verdict, only a **delta that a person looks at once per
session**: did orphans jump by twelve in one commit because a promotion
happened without its links, or drift by one because that is what a new page
always does. `Plan/state.json` is already committed to git on every run (its
own history has three separate commits touching it in the last day), so the
"baseline" `compare_reports()` needs already exists for free — no new store, no
second source of truth, just a read of `git show HEAD:Plan/state.json` against
a fresh `derive()`.

**Cheapest version.** A script of about thirty to forty lines,
`scripts/drift.py`, with:

```python
WATCH = ["wiki.orphans", "wiki.relations_unmarked", "quotes.unresolved", "quotes.unchecked"]
```

— a short, named allow-list, not every key in `state.py`, because most keys
(`sources.landed`, `documents.with_census`, `wiki.pages`) only move when a
person does something and "it changed" is not itself informative. For each
watched key it prints `key: <git-HEAD value> -> <current value>  (Δ+N)` with no
pass/fail exit code — it is a report a person reads, the same way
`judgements.py --open` is, not a gate that blocks a commit. That keeps it out of
CI-shaped territory this project has already rejected for judgement-shaped
things (conflict detection, promotion) while still answering the one question
nothing today answers: *did this session's change make the known gaps bigger
or smaller, and by how much.*

**Cost:** under an hour, against `scripts/state.py`'s existing `value()` and
`derive()` and one `git show` call. No new dependency, no new file to keep in
sync (the watch-list lives beside the four counts it watches, in the same
file), no state stored anywhere `state.py` does not already write it.

---

## Worth writing down, not worth building

### 2. `GraphMerger`'s silent conflict absorption, as grounding evidence

**The idea**, from `drg/graph/incremental.py`: three node-merge policies decide
what happens when a second document's node matches an existing one by id or
by normalized name. `PREFER_EXISTING` (lines 564–581) at least records a
`merged_from` audit entry with the incoming document's properties, so the fact
that two documents disagreed survives, buried in metadata. `PREFER_NEW` (lines
583–593) does not: `existing.properties = dict(incoming.properties)` replaces
the old values outright. `UNION` (lines 595–605) does not either:
`merged_props.update(incoming.properties)` — the incoming document's value wins
on every key collision, silently, with no check for whether the two values
actually differed and no record produced when they did.

**Does it survive contact with this project's rules?** No, and it is useful
precisely because of how cleanly it does not. `CLAUDE.md` states plainly that
"conflict detection is deliberately never mechanised, and a canon link is
written by a person, never inferred by a model," and `PRINCIPLES.md`'s P13
("never merge readings into one definition... merging deletes exactly the
information the wiki exists to provide") and its catalogue entry "a gather step
proposes; it never resolves" — with the exact prior evidence that "one pipeline
believed such a claim and silently dropped the concept out of its own contested
count" — describe this precisely. `UNION` and `PREFER_NEW` are working code that
does that dropping, today, in a real package, on every property collision. It
is not a hypothetical failure mode; it is the default merge behaviour of a
maintained knowledge-graph library. (`MergeStrategy.node_policy` defaults to
`PREFER_EXISTING`, so a caller who never sets a policy is protected by default
— but the two-line change from default to `UNION` is exactly the kind of change
a project without this rule stated in `CLAUDE.md` makes without noticing.)

**Cheapest version: none.** There is nothing to build from this — the value is
entirely as a citation. It is worth one line in a future argument for why
reconciliation stays lookup-only and conflict-free, the same way the
predecessor's `coverage()` term is cited as evidence for why a scoring term must
be able to fall. Filed here so it is available the next time someone proposes
"just merge the two readings automatically, we can flag conflicts later" — the
answer is this file and line, not a hypothetical.

---

## Considered and rejected

**`MultiDocumentReasoner`** (`multi_document_reasoning_example.py`,
`query_layer_example.py`) — mechanised cross-document edge inference
(`ReasoningConfig(min_confidence=0.25)`, rule names like `path_bridge`,
inferred edges written back into the graph and tagged `[INFERRED]`). This is
the model-guesses-an-edge shape `Plan/concept/continuous-improvement_2026-09-17.md`
already named and rejected ("what was rejected by decision is a model
*guessing* edges... canon links must be explicit"). Nothing here changes that;
it is the same rejection with a concrete implementation attached.

**`full_pipeline_example.py`'s community reports** (step 8,
`CommunityReportGenerator(kg).generate_all_reports()`) — an LLM writing prose
summaries of a graph cluster. This is generation, not derivation, and
`PRINCIPLES.md`'s "Retired deliberately" section is explicit: "world and lore
*generators* were dropped on purpose... anything that would invent rather than
derive stays out."

**`api_server_example.py` and `mcp_demo.py`** — a FastAPI + optional Neo4j
graph-visualization server and an MCP tool wrapper around an in-memory KG
store. No instance need: the corpus is not modelled as a graph, nobody has
asked to browse it as one, and P3/P4 ("by hand first," "no construct without
instances") argue against building UI infrastructure for a data shape the
project has not adopted.

**`temporal_query_example.py`** (`role_holders_at`, `temporal_conflicts` over
`start_time`/`end_time`-stamped edges) — a real-world-clock-indexed relation
store. The corpus's readings are attributed to documents, not dated to a
timeline of world-events with validity windows; adopting this shape would mean
building the graph layer the project has already decided against, for a need
(when did a role change hands) this project does not have.

**`optimizer_demo.py`** (DSPy `BootstrapFewShot`/MIPRO over a `KGExtractor`,
scored by `EntityExtractionMetric`/`RelationExtractionMetric`) — superseded by
what this repository already has. `scripts/trainset.py` is a stricter version
of the same idea for the term-matching task: it scores with `dspy.Prediction(score,
feedback)` where `feedback` is the recorded human rule (closer to what GEPA
actually reads than a bare F1 number), and it *refuses* the four unlabelled
census reconstructions outright rather than merely tagging them as
lower-confidence, which is what this example's `_manual_fallback_events()`
pattern would suggest instead. For the actual blocker named in the task — "only
one gold candidate list exists so extraction is not trainable" — this example
does not help either: the gap is a missing second and third *document read by
hand*, not a missing metric shape. Nothing in `examples/` manufactures the
missing gold list.

**Schema-first extraction** (`docs/schema_design.md`, all three
`quickstarts/*.py`) — declare an entity/relation ontology up front, then run
`extract_typed()` against it. `PRINCIPLES.md`'s P3 names the exact failure this
would repeat, with its own prior evidence: "five page types, 26 lint rules,
three DSPy programs and a schema across five YAML files produced two pages."
The census/note process here is deliberately schema-light and text-first — a
person reading prose and listing what is there, not typing entities against a
declared ontology — and forty-six pages, none typed this way, argue for staying
that way.

**The External Adapter Contract** (`docs/benchmarking.md`, "External systems do
not need to import DRG. They only need to write prediction JSON.") — a
plain-JSON schema that decouples scoring from the tool that produced the
prediction. This is a genuinely clean idea and it maps onto the future step
`continuous-improvement_2026-09-17.md` already named ("a recall term over
candidate lists, using DRG's `_score_sets` with `fold()` as the key... because
by then there is gold for it to fall against") — but there is exactly one
producer of candidate lists today (a person, via `capture.py`), so a contract
for comparing several is a construct with no instance yet. P4 says not to build
it before it is needed; worth re-reading this file when a second producer
(human or model) exists.

**Event extraction's honest `extraction_method="manual"` labelling**
(`event_extraction_example.py`, `_manual_fallback_events()`, lines 166–272) —
tagging hand-authored fallback data so it is never confused with a model's
output. This is fully compatible with this project's practice and not a new
idea: `Plan/runs/README.md` already marks the first four census
reconstructions as reconstructions, and `trainset.py` goes further by refusing
them as gold entirely rather than merely tagging them at a lower confidence.
Convergent evidence that the practice is right; nothing to add.

**The offline-fixture discipline across most of `examples/`** — five of the ten
substantial scripts (`evaluation_framework_example.py`,
`incremental_update_example.py`, `multi_document_reasoning_example.py`,
`query_layer_example.py`, `temporal_query_example.py`) state up front that they
need no LLM and no API key, and run a real assertion at the end (e.g.
`multi_document_reasoning_example.py`'s `assert dry_report.edges_added == 0`).
This is the same fixture requirement as `CLAUDE.md`'s P5 ("a workflow ships
with a fixture that runs offline, free, with no API key"), arrived at
independently. Worth noting as confirmation that the rule generalizes beyond
this project; not a new construct to add here.

---

## On the "does the README claim more than the code does" question

I did not find a case in `examples/` or the two docs it points to where a
claim outran the code. The quickstarts' shared `README.md` says each script
"prints a human-readable summary and writes a `.json` KG dump beside itself,"
and all three (`01_wikipedia_article.py`, `02_financial_news.py`,
`03_biomedical.py`) do exactly that, including the same API-key guard
(`if not (os.getenv("OPENAI_API_KEY") or os.getenv("GEMINI_API_KEY")): ... return
1`) repeated consistently across all three files rather than promised in one
and missing in another. `docs/schema_design.md`'s "Gelecek Geliştirmeler"
(future work) section is honestly labelled as not built (schema versioning,
automatic schema inference, property type validation) rather than described as
present. The one real capability gap in this codebase — that its graph and
reasoning modules do real, working, well-tested things this project should not
want — was already found and correctly declined by
`continuous-improvement_2026-09-17.md`, not newly discovered here.
