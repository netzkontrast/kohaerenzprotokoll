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

**`heading@v1` stays.** Neither variant meets the pre-stated rule. 72 runs, Claude Haiku, $7.67, 83 minutes,
no call failed (`results.jsonl`, `report.json`, every call in `lm/`).

| chunker | scored / 24 | forced | line recall | doc recall | refs | tokens used of 3 200 | paired line Δ vs `heading@v1` (90 % CI) | better / worse | refused refs (invented) | cost |
|---|---|---|---|---|---|---|---|---|---|---|
| `heading200@v1` | 22 | 2 | 0.037 | 0.067 | 3.6 | 677 | **+0.015** [−0.009, +0.040], 17 pairs | 4 / 4 | 6 (3) | $2.42 |
| `heading@v1` | 18 | 6 | 0.032 | 0.062 | 3.7 | 959 | — | — | 2 (2) | $2.52 |
| `heading800@v1` | 20 | 4 | 0.018 | 0.050 | 4.2 | 1 834 | **−0.019** [−0.046, +0.006], 15 pairs | 3 / 7 | 1 (1) | $2.73 |

Intervals: 10 000 bootstrap resamples of the paired differences. Means are over the cases each chunker scored.

- **Smaller is not worse; larger leans worse, not established.** `heading200@v1` is ahead by +0.015 — below the +0.027 the rule asks for, with
  as many cases worse as better and an interval that includes 0 — so it does not replace `heading@v1`.
  `heading800@v1` is behind in 7 of 15 pairs and ahead in 3; the interval just includes 0, so it is not
  established as worse, but nothing here argues for it. The static bench said the same in its own terms (0.051 at k = 8).
- **The budget did not bind.** The agent cited 3.6–4.2 chunks and used a fifth to a half of the 3 200 tokens. It
  stops on its own; what limits it is finding, not room to cite.
- **`heading@v1` was forced most often** (6 of 24 against 2 and 4): six runs spent their six steps without
  submitting. Whether its chunks invite more reading or this is chance across 24 cases is not measured.
- **The agent invents evidence, and the gate catches it.** Nine refs were refused because no search had shown them;
  six of them name documents the corpus does not hold. The first, in C10, came from a whole tool output Haiku wrote
  itself (`Output (7,644 chars) … Search 7`) — a document `kapitel-1-durchschlag-arbeitsdokument-2026-06-10-md` that
  does not exist, which `read_chunk` refused and the agent cited anyway. An agent's evidence is accepted from its
  tools' record, never from its answer (P26).
- **Absolute recall is a floor.** In 17 of 24 cases some chunker found at least one gold line; the gold is the lines the
  records cite, and a passage that says the same in another document scores nothing (*What it cannot say*, above).

**Recorded:** `Index/methods.toml` names this run beside `heading@v1` and beside each variant, as a comment (the
registry stamp, and so every chunk id, is unchanged). The variants stay, provisional, for the measurement that can
overturn this: an independent gold set (evaluation audit §3 item 4), on which chunk size may matter more than here.
