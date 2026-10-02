# Architecture session, 2026-10-01 — baseline, ownership, self-evaluation

The session `Plan/briefings/architecture-session.md` asks for (PR #139). This file holds parts A and B: the baseline
as measured, the map of who owns what, and the evaluation of the repository's own claims. It was written **before**
the architecture was chosen. The architecture is `SPEC.md`; the first migration step is `scripts/benchset.py`.
No corpus document was read, no model was called, nothing left the container.

## A. Baseline

| item | value |
|---|---|
| branch | `codex/strategic-learning-architecture-session` (PR #139), continued in a separate worktree so the open PR #140 branch stayed untouched |
| commit at start | `1fa5a8a4` (on `main` `219a3ee9`); clean |
| SessionStart | `knowledge.py init --profile research` ran at session start, `"ready": true`; not repeated |
| present | `derived`, `tools`, `typesafe`, `dspy`, `graphqlite`, `.venv-novelgraph` (with the `rlm` extra), the `claude` CLI 2.1.286 |
| absent (in this worktree) | `dspytools`, `grawiki`, `mflow`, `semantica`, `jev`, `graphify`, `cgr`, `hyperextract`, `omo`, `qmd`, `qmd-models` (`install.sh --check`). None is needed by a check run here; `hx.py parity` and qmd searches are the steps they would affect |
| open PRs | #139 (this), #140 (`claude/rlm-chunk-optimize`: #76 ported, `novelgraph rlm`, the chunk-size run — complete, 72/72, and corrected after #139's inspection at `bc764573`), #76 (unmergeable, superseded by #140) |

Every check the briefing names, run on the start commit; output and exit code in `checks/`:

| check | exit | result |
|---|---|---|
| `account.py order --summary` | 0 | order holds: 58 documents with a census, 0 violations |
| `state.py --prose` | 0 | 0 prose claims contradict the repository |
| `sources.py check` | 0 | every landed row matches its file (1 still to fetch, the mp3) |
| `quotes.py` | 0 | 21 969 cited quotes checked, 0 unresolved, 0 unchecked |
| `graph-lab-2026-09-30/eval-audit.py` | 0 | reproduces the circular gold; pack ceiling: mean cap 0.90 |
| `wiki_index.py --check` | 0 | 10 pages without `## Reading` (kept, reported) |
| `judgements.py --open` | 0 | 120: 8 agree, 0 DISAGREE, 106 judgement, 6 skipped |
| `chapters.py` | 0 | 41 pages, 585 readings, 0 defects |
| `overview.py --check` | 0 | current |
| `selftests.py` (all, not `--only std`) | 0 | **71 held, 0 failed, 0 not run** |

`GOAL.md` names `netzkontrast/agency` `Plan/010-novel-domain/spec.md` as required reading. It is public and was read:
it now sits under `Plan/superseded/` (closed 2026-06-09, replaced by specs 101–108 and 120–124). Its lasting lesson
for this project: of the eleven "decidable" storyform checks its source shipped, most were fixture-discriminating
heuristics and one module was a stub returning PASS; only a small structural subset (reference resolution, set
partition, slot presence) is genuinely decidable. `GOAL.md`'s pointer is stale; `SPEC.md` §8 takes the lesson.

## The map — who owns what, as the code is today

Built from `scripts/README.md`, then checked against imports and call sites (three read-only tracers; the claims
`SPEC.md` leans on were re-checked by hand, marked ✔).

| responsibility | owner today | consumers | notes |
|---|---|---|---|
| source identity, frontmatter boundary, file lines | `subject.py` (`Document.offset`) | ~40 scripts, novelgraph | one implementation ✔ |
| quotation identity | `quotes.py` (`normalise`, `verdict`), `read.py --find` | 12 modules | the check every other check rests on |
| reading → census → note → reconciliation → page | `capture`, `census`, `claims`, `readings`, `reconcile`, `record`, `brief`, `account` | the ingest skill, agents | source-local, frozen before the wiki is read |
| derived per-document facts | `derive.py` + `rules/` (cache by sha and rule version) | `corpus.py`, `overview.py` | the model the rest should follow for invalidation |
| stated graph | `graph.py` (edges with `via`, evidence with `status`) | 11 modules | built from frontmatter, `[[links]]`, citations |
| query projection | `askdb.py` → `Plan/derived/ask.db` (GraphQLite + FTS5 `lines`, `quotes`, `kp_fts`); `kg.py` CLI over it | ask, kg, aliases, bm25rel, graph_export, graphlab, crossdoc | one store; **two freshness records** for the same inputs (`askdb.fresh` on `stats.input_hash`, `kg.freshness` on `kp_meta.inputs`) and a copied `evidence_rows` ✔ |
| graph retrieval | `graphrag.retrieve` (seeds by `fold`, PPR, MMR over verified quotations) | ask, kg, graphlab, rlm_retrieval | |
| evidence pack | **two packers**: `ask.build_pack` (Markdown, 60 000 characters, a whole document cut when it does not fit) and `kg.bounded_context` (JSON, 12 000 UTF-8 bytes, per evidence) | ask's backends; the `graph-context` skill | the boundary the architecture has to settle |
| lexical search | **four query builders** — `askdb.fts_query` (stop list, ≤ 2 chars dropped), `kg.search` (every `\w+`), novelgraph `Index.bm25` (own stop list + lemmata), `bm25rel` (raw SQL on `lines`); three stop lists | | qmd is a fifth, external |
| chunks | `hx.split` (HyperExtract's characters), novelgraph `chunkers` (line ranges), `askextract` paragraphs | contracts / search / co-mention | different jobs; not duplicates in purpose |
| chunk index | `novelgraph/` (`Index/`, vectors, FTS, `search`, `verify`, `bench`; `rlm` on #140) | **no pipeline consumer** | committed `Index/` chunks; ignored vectors, lex, `_build/` |
| model calls | `lmrun.call` (approval, per-call record), `claude_lm`/`claude_cli`, `route.py` (consent file, free models), `rlm_ingest` (own `--approval`, direct LM), `he_claude`, `jules` | | four consent encodings, kept apart by decision 008 |
| proposals | `P_*` edges (`bm25rel`, `hegraph`, `askextract`), entity lists, glosses | the store, never the core graph | `askdb.check` refuses a `P_` type among stated types |
| answers | `ask.verify` (placed / outside-window / unresolved / outside-pack; unsupported claims), `land` → `Sources/ask/` (tier `M-ask`) | | an answer is citable like a source, excluded from corpus counts |
| checks | `state.py`, `selftests.py` (71 suites), `.github/workflows/checks.yml` | CI | |

**Defects and debts found while mapping** (each re-measured):

1. **BM25 anchors in frontmatter.** `askdb` indexes every non-empty *file* line, frontmatter included; `ask.route`
   does not filter. On the 24 bench questions, **7 of 720** `bm25-lines` anchors lie above the body, in 3 cases.
   Small, real: metadata enters the pack as source text and spends budget.
2. **Freshness recorded twice, `evidence_rows` copied** between `kg.py` and `askdb.py` (identical but for one line).
3. **Four lexical query builders and three stop lists** that disagree on what a query word is.
4. **Two packers with two budget units** (characters, UTF-8 bytes), and the novelgraph/RLM evidence budget in a
   third (regex tokens). No serialized budget includes the instructions and metadata a model also reads.
5. **`rlm_ingest.py` builds its own `dspy.LM` against OpenRouter** with its own `--approval`, outside `lmrun.call`'s
   per-call record — the one model path with no per-call ledger.
6. **`GOAL.md` points at a superseded spec**, and its §3 tiers / §4.4 automatic adjudication are suspended by
   decision 006 and `CLAUDE.md` ("conflict detection is never mechanised").

## B. Self-evaluation — the claims, against their evidence

Classes: **E** established behaviour (measured, reproducible), **S** supported inference, **P** provisional construct,
**U** unmeasured claim.

| claim | what was built | measured | counterexample | coverage limit | consequence for the design | class |
|---|---|---|---|---|---|---|
| Green quotation and schema checks mean a faithful reading | `quotes.py`, `census.py check`, `claims.py` | 21 969 quotations resolve, 0 unresolved | reader lab: Haiku notes passed every mechanical check while **4 of 16** claims were wrong (subject, voice, absence, count, R2); R3 **9 of ~30**; R4 10 of 74, with a new class "errors of explanation"; a same-model self-check wrote "Verified" over a wrong reading | the claims audits are small, one reader each | a check of **text identity** and a check of **interpretation** are different gates; the spec keeps both and never lets the first stand for the second | E (identity) / U (fidelity) |
| More gold, more graph edges improve retrieval | gold lists, HyperExtract contracts, `P_*` relations | backfill: paired Δ −0.0003 [−0.0028, +0.0021], 22 of 24 cases identical → stopped (decision 019); co-mention gain shrank to a third on the second label set | 92 % of gold lines (1 130 of 1 226) are lines pages already quote; no unread document is gold | 24 cases, one connected cluster (below) | no backend or relation is adopted on this bench; it is a **regression** fixture | E (null) |
| Fast warm retrieval makes the CLI cheap | novelgraph | warm hybrid P50 5.5 ms / P95 29.4 ms | a cold `novelgraph search` is ~15 s (model load); a cold `ask.py pack` is **8.8 s** with no model (measured here: 66 440 characters, 16 documents in, 23 cut by budget); session init ~1 min first time | one machine, 4 CPUs | cost is reported as **cold + warm + build**, never warm alone; a consumer that calls once pays the cold price | E |
| A second blind reader gives the truth | blind re-readings, `agree.py`, `goldrel.py` | two blind readers: F1 0.66 selecting, 0.82–0.93 listing exhaustively | every reader so far is Claude; two blind *relation* readers' agreement is unmeasured; contract precision against one reader 27–49 % | no author reading recorded | agreement is a **ceiling between readers of one family**, not truth; author calibration is the missing anchor | S |
| DSPy should optimize everything | `lmrun`, `pairs.py` ladder, `dspy-learning` proposals | the ladder: BootstrapFewShot 0.884 vs plural floor 0.698 on 51 model-seen pairs, $13.80 total; GEPA 0.847 at $5.38 did not beat it | the five surfaces of `dspy-learning_2026-09-30.md` have not run ("Nichts hier ist gelaufen"); one Jules failure exists where 5–20 are needed | 63–67 labelled pairs | only a surface with a **fallible metric, a held-out set, a budget and a veto** is optimized; today that is `pairs.py` alone | E (ladder) / U (others) |
| RLM wins because it compared chunk sizes | `novelgraph rlm` (PR #140) | 72 runs, $7.67: no size beats `heading@v1` by the pre-stated +0.027 (200: +0.015 [−0.009, +0.040]) | **only 156 of 282 accepted refs were read**; the rest were cited from a 200-character preview — the metric is chunk *selection*, not reading; Haiku invented a tool output and a document; all three arms are RLM | one controller, 24 dependent cases | the run informs **chunk size under RLM**, nothing about RLM against a fixed pack; adoption of RLM is not supported (E4 would be the test) | E (size, under RLM) / U (RLM vs simpler) |
| A novel-context tool can operate already | chapter pages, `kg.py context`, `ask` | 41 chapter pages, 585 readings | the writing plan's four questions are undecided; no model of reader / Kael / AEGIS knowledge per chapter exists; research narratives are not canon (author, 2026-09-26) | — | chapter context stays a **future** workflow with named prerequisites; nothing may present research as canon | U |

**Two further claims this session tested.**

- *"The bench can be held out."* `scripts/benchset.py clusters` on the frozen v1 set: 24 cases over 55 gold documents,
  one document gold in 23 cases, 54 documents gold in ≥ 2. Linked by any shared gold document the cases form **one
  group of 24**; still one group at ≥ 5 shared documents; at ≥ 12, one group of 20 and four singletons. **No clean
  held-out split exists**; a random split would be called independent and is not. → E. Consequence: every
  comparison is paired on all 24, reported as regression, and discovery waits for new, independent cases.
- *"Scores across weeks are comparable."* Until this session the cases were read live from the records, so the gold
  moved with every record edit. Now frozen (`Plan/eval/retrieval-cases-v1.json`, sha256 `b37d8010…`, 24 cases,
  1 670 gold lines counted per case); `benchset.py check` proves the file and reports drift. → E from now on.

**The strongest counterexample to this session's own recommendation** (`SPEC.md`: keep the deterministic
question-to-evidence path as the default and put one packing contract under every finder) is that a fixed pack
already misses most of the gold — its document recall is capped at a mean 0.90 by size, and 6 of 24 cases find no
seed at all — so an adaptive controller (RLM, bounded expansion) might be exactly what the cases need, and the
spec could be standardising the weaker path. What would change it: a matched comparison (E4) in which an adaptive
controller reaches more *read* gold evidence than the fixed pack **at the same total model cost and with no
invented evidence admitted**, on cases that are not the circular bench. Until that exists, the deterministic path
is the cheaper, auditable default and the adaptive ones remain optional finders behind the same contract.
