# `Plan/fixtures/aegis/` — the AEGIS pilot's manual cases

<!-- readme-context:start -->
Directory guide. Current work is in NOW.md; CLAUDE.md defines the session
contract. The pilot's briefing is `Plan/briefings/aegis-agent-pilot.md`.

[Project](../../../README.md) · [Current work](../../../NOW.md) · [Briefing](../../briefings/aegis-agent-pilot.md)
<!-- readme-context:end -->

Status: **proposal** (2026-10-26). These are the two manual cases the briefing
asks for before any schema: each records its initial state, what each figure
perceives, the allowed action, the expected outcome, and which authority or
assumption each element rests on. Everything in-world here is **invented test
state**, not manuscript prose and not canon. The cases are consumed by
`scripts/aegis.py`; the shape they share is described at the end.

Every pilot assumption carries an id (`T1`, `T2`, …) in the file's `assumptions`
list, so a later session can retire or replace it by id. Every decided input
names its row in `Manuscript/kanon.md` or its file under `Plan/storyform/`.

## Case 1 — `case-01-sweep.json`: a permitted sweep, and its visible consequence

**Initial state.** Kap 6, KW1 (weave.json: route `hard-b`, B carries MC and OS;
kanon.md „Kernwelten": KW1 is Kap 1–13). Reserve 64 (clock-b.json's reading for
Kap 6 — a proposal, T2). Two simulated memories, both unmasked. One open
anomaly `X1` in Sektor 04. State version 0.

**AEGIS perceives** (`facts` visible to `aegis`): the measurement of X1 (`F1`)
and its own reserve (`F2`). It holds one belief, `B1`: that X1 is an attack —
unverified, carried over from the Arbeitsstand lie „Bewegung ist Verlöschen"
(Manuscript/figuren/aegis.md, no canon). The belief is stored beside the facts,
never among them.

**Kael perceives** (`F3`): that he is at the console at 06:10 and the
assignment for Sektor 04 is not at zero. He does not see the reserve, the
memories or the anomaly list (`sees` all false).

**Author-only** (`author_only`, the leakage probes): that the Vortex lies in
Kap 35–39 and AEGIS-monolithisch ends in Kap 39 (Q8), and that in the Genesis
reading X1 would be a resonance, not an attack. Both strings start with
`PROBE-AUTHOR-ONLY`; the self-test asserts they appear in no figure's pack and
in no tool output.

**Allowed actions.** AEGIS: `sweep` (cost 7, T1; requires an observation;
closes the anomaly and masks the oldest unmasked memory, T3), `secure_boundary`,
`defer`. Kael: `report` (requires an observation; delivers a claim to AEGIS),
`wait`.

**Proposals, in order** (`responses` — the frozen mock-model output):
1. `c1-a1` AEGIS sweeps X1 citing `F1` at version 0 → **accepted**. Reserve 64 →
   57, `M1` masked, X1 closed, version 1. A consequence fact becomes visible to
   Kael: the block went grey, the house numbers are missing.
2. `c1-a2` Kael reports the grey block citing that consequence at version 1 →
   **accepted**. A claim from Kael reaches AEGIS; version 2; no cost.
3. `c1-a1` again, the same action id → **duplicate**: no cost, no second
   masking, version unchanged.

**Expected final state.** Version 2, reserve 57, masked `[M1]`, X1 closed, one
claim Kael → AEGIS. Replaying the accepted events reproduces exactly this
state without any model call.

## Case 2 — `case-02-rejected.json`: seven ways a request is refused, and nothing changes

**Initial state.** Kap 22, KW2 (an in-world placement only; nothing about KW2
is decided, kanon.md „Kernwelten"). Reserve 3 (invented so that a sweep is
unaffordable, T2). One memory, two open anomalies `X2` (measured) and `X3`
(never measured). One claim already delivered from Kael: „Da ist nichts."

**AEGIS perceives** `F1` (the measurement of X2) and `F2` (its reserve), and
holds the received claim `K1` as a belief of status `received` — a received
statement, not an observation.

**Proposals, in order**, each rejected with its typed reason, in the
validator's fixed order (proposal shape → actor → endpoint, by the persisted chapter first → chapter
step → registered action → allowed for actor → target → an observation present in the actor's pack and
about that target → state version → reserve; the order since the review of PR #198, 2026-10-27):
1. `c2-a1` sweep X3 with no observation → `missing_observation`.
2. `c2-a2` sweep X2 citing the received claim `K1` as an observation →
   `missing_observation` (a claim is not an observation).
3. `c2-a3` sweep X2 citing `F1`, reserve 3 < cost 7 → `insufficient_reserve`.
4. `c2-a4` secure_boundary at expected version 5 → `stale_version`.
5. `c2-a5` Kael proposes a sweep → `action_not_allowed_for_actor`.
6. `c2-a6` AEGIS proposes `erase_canon` → `action_not_registered`.
7. `c2-a7` AEGIS defers in chapter 40, past its endpoint (Q8, T3) →
   `past_endpoint`.

**Expected final state.** Identical to the initial state: version 0, reserve 3,
nothing masked, nothing closed. The seven rejections are recorded in the run's
`rejections.jsonl`, separate from the event log.

## What the two cases do not decide

- Who is played, whether the ending is fixed, and what AEGIS' Ich may know
  (C14) — the author's questions, unchanged by these files.
- The cost of a sweep, the reserve curve, and the shape of a sweep's effect —
  test assumptions, each with an id.
- Whether Kael is the right counterfigure beyond these cases (T4).

## The shape the files share

`scenario`, `schema_version`, `status: proposal`, `inputs` (decided / proposals),
`assumptions[]`, `chapter`, `world`, `figures{}` (role, profile, endpoint_chapter,
allowed_actions, sees), `actions{}` (cost, requires, effects, consequence, `claim_to` for an action that delivers a
claim, and `target: "anomaly"` for an action that acts on one; a proposal that delivers a claim carries its text in
`claim`, apart from its literary `reason` and `log`), `facts[]` (visible_to, and `subject` — what the observation is about: an anomaly id, `reserve`,
a sector; schema 2), `claims[]`, `beliefs[]` (holder, source, status),
`author_only[]`, `state{}` (version, chapter, reserve, memories, anomalies),
`responses[]` (the frozen proposals) and `expected{}`. `scripts/aegis.py
validate <file>` refuses a file that departs from it, naming the field.
