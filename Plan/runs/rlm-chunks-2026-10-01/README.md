# Which chunk size helps a reader find the evidence — an RLM agent over the index

**2026-10-01.** On the author's „Überarbeite #76 so dass es auf Stand Main funktional ist — und erfolgreich zum chunk
optimieren genutzt wird". PR #76 tried a `dspy.RLM` agent over the wiki graph (`scripts/rlm_retrieval.py`); this run
puts the same kind of agent over the chunk index (`novelgraph rlm`, `novelgraph/src/novelgraph/rlm.py`) and lets its
success choose the chunk size. **This section was written before the run** (evaluation audit, §3 item 2).

## The question and the variants

The static bench (`sweep-k8/bench.json`, `sweep-k50/bench.json`, no model) cannot separate the sizes:

| chunker | target tokens | chunks | hybrid doc recall@8 | @50 | lines per hit |
|---|---|---|---|---|---|
| `heading200@v1` | 150–250 | 26 059 | 0.067 | 0.230 | 8.0 |
| `heading@v1` | 350–450 | 15 339 | 0.068 | 0.229 | 13.4 |
| `heading800@v1` | 700–900 | 9 228 | 0.051 | 0.189 | 21.4 |

A ranked list is not how a reader uses a chunk. So the agent gets two tools over one chunker — `search_chunks`
(eight hits: ref, heading, 200 characters) and `read_chunk` (one chunk it was shown, lines numbered, ≤ 4 000
characters) — and returns refs as evidence. `section@v1` and `window400@v1` are left out: a whole section is
not a size a reader can be handed, and the window is a baseline the static bench already places below.

## Pre-stated

- **Cases:** the 24 of `ask.bench_cases()`, unchanged; each under all three chunkers, case by case.
- **Model:** Claude Haiku through `claude -p` (`lmrun.make_lm("claude-cli/haiku")`), `approval="decision 011"`,
  one call at a time. `max_iters` 6, `max_llm_calls` 2, 3 000 characters of output shown per step.
- **Metric:** line recall — the share of the record's gold lines inside the accepted evidence. Evidence is
  accepted in the agent's order up to **3 200 tokens of chunk text** (the same text for every chunker, so a
  large chunk cannot win by its size), only refs a search showed. Document recall beside it.
- **Unscored:** a forced answer (`max_iters` spent; DSPy built the output from the trajectory) and any call that
  did not answer. They are counted, not scored as 0.
- **Comparison:** paired, per case, against `heading@v1`, on the cases both scored.
- **Decision rule:** a size replaces `heading@v1` only if its mean paired line-recall difference is above
  **+0.027** — the smallest effect the evaluation audit estimates 24 such cases can show — and it is better in
  more cases than it is worse. Otherwise `heading@v1` stays, and the result is recorded as such.
- **Stop rule:** the run stops when its recorded cost passes **$15** (pilot: $0.19 a case).
- **What it cannot say:** the gold is the lines the conflict and question records cite (92 % of them quoted on
  wiki pages too, evaluation audit §0). A passage the agent finds that says the same thing in another document
  scores nothing. The comparison between sizes is fair; the absolute numbers are a floor.

## Pilot (before the design was fixed)

Two cases under `heading@v1` with 10 000 characters of output per step (`pilot/`): C1 answered with 8 refs and
0 gold lines (14 gold documents; the agent cited an AEGIS biography and design documents the record does not);
Q1 was forced. $0.21 and $0.17, about 2 minutes each, 85 % of the tokens re-read earlier steps — hence the
3 000-character cap and the instruction to submit by step 5.

## Result

*Written after the run.*
