# E4 — fixed pack, bounded expansion, RLM: which controller reaches more read evidence at equal cost

**Design, written before any call. Status: not run.** Step 8 of `SPEC.md` §9. Decision 021 approves it: Claude only
(`claude -p`, decision 011), serial, **$20 for the whole experiment**. It runs only after the author has seen this
design (2026-10-02, „Ja bitte" to: design first, then show). Nothing below has been measured yet; every number in
it is a budget, a threshold or an estimate, and says so.

## The question

`SPEC.md` §8 keeps the deterministic pack as the default path and names the observation that would reverse that
choice: *an adaptive controller reaches more **read** gold evidence than the fixed pack, at the same total model
cost, with no invented evidence admitted*. PR #140 compared chunk sizes under one controller, RLM. It said nothing
about RLM against a fixed pack, and 45 % of the refs RLM cited there were never read. E4 is that missing comparison.

## Three arms, one answer format, one verifier

Every arm ends in the same JSON `ask` already asks for (`ask.RULES`, `ask.SCHEMA`: claims with verbatim quotes
and a `line_hint`). Every answer is checked by the same `ask.verify(answer, shown)`. `shown` is **exactly the lines
that arm put into the model's context** — nothing the arm could have shown but did not.

| arm | what the model gets | model calls per case | `shown` |
|---|---|---|---|
| **A — fixed pack** | `ask.build_pack` with the default finders, 72 000 bytes; one answer | 1 | the pack's lines (`meta["shown"]`) |
| **B — bounded expansion** | the pack; if the answer's `need` names terms or line ranges, code fetches them — a term through `askdb.bm25` (the pack's own lexical finder), a range through `Store.window`, at most 8 000 bytes per round — appends them, and asks again; **at most 2 extra rounds**, and a round only when `need` asks for something not yet shown | 1–3 | the pack's lines plus every fetched line |
| **C — RLM over chunks** | `novelgraph rlm`'s tools (`search_chunks`, `read_chunk`, `heading@v1`, PR #140), the same limits as that run (6 iterations, 2 sub-calls, 3 000 output characters a step); it submits the answer JSON | ≤ 8 | **only the lines of chunks it called `read_chunk` on** — a 200-character preview is not reading |

All three arms use the same question text: the frozen case's question, with `kind: position`. All three use the
same model, Claude Haiku through `lmrun.make_lm("claude-cli/haiku")`, and record every call with `lmrun.call`.

## The cases, and what they can and cannot show

- **The 24 frozen cases** (`Plan/eval/retrieval-cases-v1.json`), with each case's own record removed from the graph
  as `ask.py bench` does.
- **Two views of the gold:**
  - **all**: every cited line of the record;
  - **unquoted**: the gold lines no wiki page quotes. That is the 8 % the graph route cannot reach by construction,
    and the closest this bench has to discovery.
- **The reversal condition asks for cases outside the circular bench.** None exist (`NOW.md`, question 6). So E4 on
  these cases can **confirm** the default. It can **only support, not decide,** a reversal. A reversal would need the
  independent cases first.

## The metric — read gold, never selected gold

- **Read gold** for a case is the set of gold lines `L` such that:
  - an answer quote was **placed** by `ask.verify` on line `L` of document `d`;
  - `(d, L)` was in `shown`;
  - `(d, L)` is in the case's gold.
- **Read-gold recall** is read gold divided by gold. It is reported for both gold views.
- **Invented evidence** is a quote that is `unresolved` or `outside-pack`. It is counted, **never** scored as
  evidence, and reported per arm as a veto count.
- **A forced or failed run** (`refused`, `unparsed`, `unreachable`, or RLM's „Extract forced final output") has two
  readings. The primary one scores it as **0**: no evidence delivered, so an arm cannot win by dropping its hard
  cases. Beside it stands the complete-case view.

## Equal cost

- **Cap per case:** each arm gets the same cap per case, **$0.15**. Before every call, the arm's spend on the case
  plus that call's estimated worst case is checked against it; a call that could cross the cap is not made, and the
  case ends with what it has.
- **Spend as a result:** each arm's actual spend is reported, and the per-dollar view is reported beside recall.
- **Expected spend (from PR #140):** A ≈ $0.03 a case (one call over about 20 000 input tokens), C ≈ $0.10. B lies
  between them. These are estimates; the pilot replaces them.

## Order, pilot and stop rule

1. **Pilot:** 2 cases × 3 arms, about $0.50. It checks the answer format, the caps and the per-call cost. The design
   may change only in what the pilot shows to be broken, and any change is written here, dated, before the main run.
2. **Main run:** 24 cases × 3 arms, **case-major** (every arm on case 1, then case 2, …), so that a run that stops
   early still leaves complete triples. The arm order within a case rotates.
3. **Stop rule:**
   - The **whole experiment stops when recorded spend plus one worst-case call would exceed $20**. The check runs
     before every call, not between runs.
   - Worst case: 72 runs × $0.15 = $10.80, plus the pilot.
4. **Resume** is allowed only into the same run directory and the same fingerprint: code, model, limits, frozen-set
   sha. A changed input is a new run.

## Decision rule — stated now, applied as written

**An adaptive arm (B or C) replaces A as the recommended default only if all of these hold:**

1. Its mean paired read-gold recall (all gold) exceeds A's by **at least +0.03**, with a **90 % bootstrap interval
   that excludes 0** (10 000 resamples, seed 7), and it is **better in more cases than it is worse**.
2. It is **not worse than A on the unquoted view**: mean difference ≥ 0.
3. Its **invented evidence is no higher than A's**. Every invented quote is listed.
4. Its actual mean cost per case is **within the cap**. The per-dollar ratio is reported, not required.

Otherwise **A stays**, and the result is written down as such.

Even if B or C passes, the recommendation goes to the author as a **proposal**. It changes nothing in `SPEC.md` by
itself, because the reversal condition also asks for independent cases (above).

## What E4 cannot say

- **Read-gold recall measures evidence a model chose to quote from what it was shown.** It does not measure whether
  the answer is right.
- **The gold is circular.** A correct passage in a document the records do not cite scores nothing. Absolute numbers
  are a floor; the comparison between arms is the result.
- **One model, Haiku.** Any difference is a difference under Haiku.

## What it will produce

The run directory holds:
- this README with a `## Result` section appended;
- `results.jsonl` (one row per case × arm: status, forced, shown lines, placed / unresolved / outside-pack quotes,
  read gold in both views, cost, seconds, calls);
- `lm/` (every call, from `lmrun.call`);
- `analysis.json` (the paired comparisons, the intervals, the decision rule applied line by line).

The code is **new and offline-tested before the pilot**: one script with a fixture LM that produces all three
answer paths and every failure status, and that proves the caps and the stop rule refuse.
