# Jev, as the judge layer — tool review, 2026-09-24

Tested: `.venv-typesafe/bin/python scripts/route.py jev --purpose jev-judgements
--doc <slug>`, stdin `{"state": ..., "questions": ...}`, against the 26 rows of
`Plan/runs/judgements.jsonl` whose `document` is `aegis-subplots-kapitelweise-
system-exploration-docx` (13 rows) or `roman-lokalitaeten-konzept-und-
ausarbeitung` (13 rows) — the two documents decision 007 permits. Read
`.agents/skills/typesafe/SKILL.md` first, as required.

**Reached: yes.** All 4 calls answered (`jev-1.13.0`), 0 refused, 0 unreached.

## What ran

1. `python3 scripts/read.py <slug> --find "<surface>"` for each of the 52
   surfaces across the 26 rows, to get the citing line; then `--from L-1 --to
   L+1` for one line of context each side. 8 of 52 surfaces did not resolve to
   an exact line (`Entropie-Score` written as `'Entropie-Score'` with quotes,
   `IntegrityGuardian` and `Kern-Welt`/`KW1` as inflected or hyphenated
   variants, `Guardians`, `Möglichkeits-Garten`, `Grenzfeste` similarly) —
   `read.py --find` named the nearest line each time (44–100% word overlap) and
   that line was used for context, flagged in
   `Plan/runs/tooltest/jev/contexts.json` as `"note": "nearest match, not exact
   --find hit"`. This is `read.py` doing exactly what it says it does — refusing
   rather than guessing a citation — and it is not a defect in either tool.
2. Built one batched state per document: 13 pairs each, `state.pairs[i]` =
   `{surface_a, surface_b, context}`. Two questions per row, referencing
   `pairs.<i>` by index (per the skill's "structure in the state, word the
   idea" rule):
   - `<id>_score`, a 3-level Score — *two terms* / *related, a person
     decides* / *one term* — matching the plan's shape and this repository's
     ledger vocabulary (levels ordered 0→2 so `round(score)` maps directly to a
     decision).
   - `<id>_noul`, "is either surface not a term at all", for the Noul the plan
     asks for beside the Score.
   All 13 pairs' 26 questions went in one `route.py jev` call per document (per
   attempt), i.e. state paid once, per the skill's parallel-questions rule.
3. Two attempts per document (P18): `state["attempt"]` set to 1 or 2 so the
   call's digest differs and the router does not serve a cached answer for
   attempt 2. Command, run four times (2 docs × 2 attempts):
   ```
   cat Plan/runs/tooltest/jev/jev_batch_<doc>_a<n>.json | \
     .venv-typesafe/bin/python scripts/route.py jev \
     --purpose jev-judgements --doc <doc> > jev_out_<doc>_a<n>.json
   ```
   Each call answered in under 1 second of Jev time (`seconds` in the record:
   0.92–1.3s); the whole tool ran in under 15 seconds wall-clock, far under the
   25-minute budget.
4. Mapped the person's `decision` to the same 3 levels (`one-term`→2,
   `judgement`→1, `two-terms`→0) and separately to `not-a-term` where that was
   the person's call; compared to Jev's `round(score)` (clamped to the Noul
   override: `noul > 0.5` → `not-a-term`, overriding the Score).
5. `jev-decide setup` (presence only, no call): both `openrouter` and
   `typesafe` report `available: true`; `jev_called: false`. No key value
   printed or written.

## Numbers

Command: `python3 scripts/route.py ledger`

```
purpose          kind  ok cached unreach refused charged   in tok  out tok
jev-judgements   jev    4      0       0       0       0   46,182        0
```

4 answered jev calls, 0 cached (attempt marker worked), 0 refused, 0
unreached. **46,182 input tokens total** across both documents and both
attempts (roughly 11.5k tokens per call — 13 pairs × 2 questions plus the
shared state, batched). Jev's own `input_tokens` field per call, summed from
`jev_out_*.json`, matches the ledger exactly. No cost: `cost: $0.000000 over
308 priced calls; 4 answered calls carry no price (Jev reports input tokens,
not cost)` — correctly not read as free, per the ledger's own caveat.

Command: `python3 -c "…"` over
`Plan/runs/tooltest/jev/{jev_batch_*, jev_out_*}` and the source
`judgements.jsonl` (script kept at `/tmp/score_analysis.py`, not committed —
its output is below and reproducible from the committed inputs/outputs).

Agreement per class (person's `decision` vs. Jev attempt 1's decision,
Score rounded to nearest level, Noul>0.5 overriding to `not-a-term`):

| class | n | Jev agrees | agreement |
|---|--:|--:|--:|
| one-term | 12 | 8 | 0.667 |
| judgement | 5 | 2 | 0.400 |
| two-terms | 7 | 4 | 0.571 |
| not-a-term | 2 | 2 | 1.000 |
| **overall** | **26** | **16** | **0.615** |

Repeat consistency (attempt 1's decision == attempt 2's decision, same
document, same pairs, fresh call): **25/26 = 0.962** — only J20 (`Wächter` /
`Guardian`) flipped, `one-term` (score 1.58) on attempt 1 to `judgement`
(score 1.43) on attempt 2, both readings straddling the 1.5 rounding boundary.
This is Jev's own instability near a boundary (the typesafe skill's own
"repeatability is not correctness" point, illustrated on data from this
corpus for the first time), not a router or prompting defect.

## Difference lists (P27), by surface pair, with the probability where they differ

**Person said `one-term`, Jev disagreed (4 of 12):**

| id | surfaces | Jev a1 | score (probs) | noul |
|---|---|---|---|---|
| J21 | Entropie-Score / globaler Entropie-Score | judgement | 1.28 ({0:.13 1:.46 2:.41}) | 0.22 |
| J25 | Alter / Alters | judgement | 0.57 ({0:.63 1:.17 2:.20}) | 0.47 |
| J29 | AEGIS / Rest-AEGIS | **two-terms** | 0.49 ({0:.54 1:.42 2:.04}) | 0.46 |
| J37 | Kern-Welt / KW1 | judgement | 1.39 ({0:.12 1:.37 2:.51}) | 0.46 |

**Person said `judgement`, Jev disagreed (3 of 5):**

| id | surfaces | Jev a1 | score (probs) | noul |
|---|---|---|---|---|
| J20 | Wächter / Guardian | one-term (a1) / judgement (a2) | 1.58 / 1.43 | 0.17 / 0.15 |
| J30 | Simulation / Simulations-Engine | **not-a-term** | 0.31 ({0:.78 1:.13 2:.09}) | **0.90** |
| J33 | Wächter / Guardians | **not-a-term** | 1.17 ({0:.31 1:.20 2:.49}) | **0.61** |

**Person said `two-terms`, Jev disagreed (3 of 7):**

| id | surfaces | Jev a1 | score (probs) | noul |
|---|---|---|---|---|
| J22 | Guardian / IntegrityGuardian | judgement | 1.17 ({0:.10 1:.63 2:.27}) | 0.16 |
| J27 | Entropie / Prä-Entropie | judgement | 0.52 ({0:.53 1:.42 2:.05}) | 0.16 |
| J38 | Limina / Liminale Räume | judgement | 1.35 ({0:.21 1:.24 2:.55}) | 0.26 |

Two shapes stand out. First, **Jev pulls toward the middle**: 8 of the 10
disagreements land on `judgement` — every `two-terms` disagreement and half the
`one-term` ones. The person's decisions in `judgements.jsonl` were made with
more context than one line each side (full document knowledge, the wiki's
existing pages); Jev, working from a short window plus surface pair, hedges
where the person was confident. That is the shape the middle level was
designed for (the skill's "the middle level of a Score is the policy"), so this
looks like Jev correctly reporting *its own* uncertainty rather than
mis-scoring — but it means Jev's Score cannot be trusted to reproduce a
confident `two-terms` call without more context than one line each side.
Second, **the Noul disagreed with the person's plain-language read** on J30
and J33 at high confidence (0.90, 0.61) — both are `Wächter`/`Simulation`-family
cases the person marked `judgement`, not `not-a-term`; on the one line of
context given, `Simulations-Engine` and (in J33) `Guardians` may genuinely not
read as separate named things, which is a smaller state than the person had.

## Sending corpus text

Both documents are in `Plan/runs/route/consent.json` (decision 007); the
`jev()` wrapper in `scripts/route.py` calls `screen()` before every request
(shingle guard, 12-word runs against undeclared documents) and stamped every
row `outcome: ok` in the ledger — no refusal fired, and none should have, since
only one line of context per surface (well under the shingle threshold on its
own, and only from the two consented documents) went in the state.

## Names

Not applicable to this tool: Jev's output here is Score/Noul judgements over
pairs already named by `judgements.jsonl`, not a list of entity names, so
`scripts/entities.py score` has nothing to score. No names file was produced.

## What broke, and why

Nothing broke. The 8 unresolved `--find` lookups are `read.py` working as
documented (refuse rather than guess); they cost one extra grep-style read
each and are recorded, not silently patched over.

## Where a Jev answer here could go, under the repository's limits

Per `CLAUDE.md` and the typesafe skill: **a Jev answer may direct attention,
never enter the record.** No page, `[[link]]`, count, merge or conflict comes
from a Score or a Noul. Concretely, against `.claude/skills/tools/SKILL.md`'s
phases:

- **3-reconcile** (`reconcile.py`'s `judgement` bucket): a Score run this way
  could rank the bucket — route the 40% it disagrees with the person on to the
  front of the queue as "needs care", and let the 60% it agrees on sit lower —
  but it may never *decide* the bucket, and at 0.615 overall agreement (0.40 on
  the `judgement` class itself) it should not shrink the bucket size. It is a
  triage hint, not a second opinion strong enough to replace a person.
- **the Noul, alone**, is a cheaper first pass for `not-a-term` filtering
  (100% agreement here, n=2 — too small to trust beyond a prompt to look
  closer) — worth widening the sample before using it even for triage.
- It may **not** enter `Plan/runs/judgements.jsonl` as a `mechanised_by`
  value: the ledger's own replay contract (`judgements.py`) is for a rule the
  code enforces deterministically, and a Jev Score is neither deterministic
  (0.962 repeat consistency, not 1.0) nor code.

## Recommendation

**Trial**, not adopt: use a batched Score+Noul call, in this exact shape
(pairs indexed in one state, one call per document, two attempts required, all
under consent), as a triage signal ahead of the reconciliation `judgement`
bucket — never to answer it. **Evidence**: 16/26 overall agreement, 0.40 on the
`judgement` class itself (the case it would need to be good at to help there),
25/26 repeat consistency, 0 refused/unreached, 46,182 input tokens for the full
26-row test (cost unpriced but token-bounded and cheap). **May not**: decide a
near match, write `mechanised_by`, create a page, a link, a count, or a
conflict; run on any document outside decision 007's two without a fresh
consent row. **Retire the trial when**: 20+ more judgement-class rows show the
same sub-50% agreement, or the Noul's disagreement on J30/J33 turns out to be
right once a person re-reads with fuller context — either would mean Jev needs
more state (more surrounding lines) before it is worth the call at all.
