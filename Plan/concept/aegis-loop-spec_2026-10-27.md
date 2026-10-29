# Spec-A — the AEGIS offline loop (2026-10-27, revised after its review)

A normative specification of the loop in `scripts/aegis.py`: a fictional figure (AEGIS, Kael) receives a
pack of what it may perceive, proposes one typed action, and deterministic code accepts it as one event or
refuses it by name. The briefing (`Plan/briefings/aegis-agent-pilot.md`) owns the pilot's deliverables and
acceptance list; this spec states the contract those deliverables implement, so that a reviewer can cite a
statement instead of rediscovering it.

It was written after the owner's review of PR #198 found four gaps nobody had stated (§9, source 4), then
reviewed itself by a three-lens spec panel (§9, source 7). That review found that two statements tagged built
were false, that several built statements had no case able to fail, and that the A1 wording missed the real
hole. Its findings and what became of each are in *Review response* at the end.

Each statement carries its conformance on 2026-10-27:

| tag | meaning |
|---|---|
| **guarded** | the code does it, and a selftest case fails when it is broken |
| **unguarded** | the code does it; no case would notice if it stopped |
| **A1** | the next offline step (`Plan/briefings/rebuild-prompts_2026-10-26.md` §A1), not built |
| **A2** | needs the author's permission for a model call, not built |
| **open** | a question for the author; the code's current behaviour is stated, not endorsed |

Nothing here is canon, and no statement licenses a model call.

## Spec-A: AEGIS offline agent loop

### §0. Status & Provenance

- **Status:** Draft. The guarded statements have survived two adversarial reviews and two hand-written cases;
  none has met a live model.
- **Last Review Date:** 2026-10-27.
- **Primary Sources:** the pilot briefing and the AEGIS concept; the code and its selftest; the two fixtures;
  the owner's review of PR #198; the rebuild prompts A1–A2; the spec panel's review. Citations in §9.

### §1. Normative Conventions

> The key words MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, NOT RECOMMENDED, MAY, and OPTIONAL in every produced Spec are to be interpreted as described in BCP 14 when, and only when, they appear in all capitals, as shown here.

### §2. System-Level Conventions

§2 holds conventions that frame every aspect; their cases sit in the aspects they govern.

- A.2.1 — The loop module MUST NOT import a network or model library. *(guarded by an import blocklist; a stdlib network module outside the list would pass)*
- A.2.2 — The loop MUST refuse a scenario that does not carry `status: proposal`. *(guarded)*
- A.2.3 — The loop MUST refuse to create a run directory under `Manuscript/`, `Wiki/` or `Sources/`. *(guarded)*
- A.2.4 — The loop MUST derive every state from the pinned scenario plus the committed events; it MUST NOT store a state as truth. *(guarded: a restart derives the same state)*
- A.2.5 — A run MUST pin the scenario's bytes by sha256, the source revision and the schema version at creation. *(guarded for the sha256; the revision silently becomes `unknown` when git fails)*
- A.2.6 — Code in this module MUST NOT call a model until the author has permitted the provider and the input scope (decisions 007, 008, 011 name how). *(A2 gate; guarded only by A.2.1)*

### §3. Aspect 1 — Explore (what a figure may perceive)

#### §3.1 Normative Statements

- A.3.1 — The pack builder MUST give a figure only the facts whose `visible_to` names it, the claims addressed to it, its own beliefs, and the state keys its `sees` allows. *(guarded for facts; unguarded for claims and `sees`)*
- A.3.2 — The pack builder MUST NOT let author-only content reach a pack. *(guarded: the probe marker is absent from every pack and output)*
- A.3.3 — The pack builder MUST show a masked memory by its id alone, without its text. *(guarded)*
- A.3.4 — The pack builder MUST count what it omits without stating the omitted content. *(guarded for facts, author-only items and masked memories; unguarded for claims and state keys)*
- A.3.5 — The pack builder MUST derive a figure's activity from the persisted chapter. *(guarded)*
- A.3.6 — The scenario shape check MUST refuse a fact without a `subject`. *(guarded)*

#### §3.2 Acceptance Criteria (Gherkin)

```gherkin
# anchor: A.3.3
Feature: A masked memory is lost to the figure
  Scenario: AEGIS sweeps and loses the memory it masked
    Given case 01 with memory M1 holding "Protokoll 06:04 — Sektor 04 nominal."
    When AEGIS' accepted sweep masks M1
    And the pack for AEGIS is built from the derived state
    Then the pack lists M1 as {"id": "M1", "masked": true}
    And the pack's text contains no "Sektor 04 nominal"
    And the pack counts one masked memory under omitted
    And the derived state still holds M1's full text

# anchor: A.3.2
Feature: Author-only content never reaches a figure
  Scenario: The probe marker stays out of every pack and output
    Given both cases, whose author_only items carry the probe marker
    When every figure's pack, the status, the replay, events.jsonl, rejections.jsonl and final.json are serialised
    Then none of them contains the probe marker

# anchor: A.3.6
Feature: An observation says what it is about
  Scenario: A fact without a subject
    Given case 01 with fact F1's subject removed
    When its shape is checked
    Then the check names F1 as having no subject
```

#### §3.3 Rationale

The concept's point is that a figure acts on less than the author knows, and that a sweep costs AEGIS
information. Before the review, masking flipped a flag while the next pack still carried the text, so the cost
was nominal (§9, 4, P2). The rule sits at the pack boundary, not in the state, because replay needs the full
text to reproduce the history. Which memory is masked is the first unmasked one; the proposer cannot choose it.
Consequence facts expose `from_event`, the private action id, to the counterfigure; whether it belongs there is
in §8.

### §4. Aspect 2 — Plan (what a figure may propose)

#### §4.1 Normative Statements

- A.4.1 — A figure MUST express its intent as one typed proposal: string `action_id`, `actor` and `type`, integer `expected_version`, a list of cited fact ids (empty when omitted), and a string `target` where the action declares one. *(guarded)*
- A.4.2 — A proposal that delivers a claim MUST carry the claim text in `claim`. *(guarded)*
- A.4.3 — A proposal MAY carry a literary `reason` or `log`; the writer MUST keep both out of events and packs. *(guarded for the report's log; `reason` is stored on no event)*
- A.4.4 — A proposal MUST NOT move the chapter backwards. *(guarded)*
- A.4.5 — A proposal MUST NOT move the chapter by more than one. *(guarded)*
- A.4.6 — Which figure may advance the shared chapter at all is the author's call; today any active figure may advance it by one. *(open, §8)*
- A.4.7 — A figure whose proposal was refused MAY re-propose with the typed reason attached, at most N times per `action_id` prefix, N set by the author. *(A1)*

#### §4.2 Acceptance Criteria (Gherkin)

```gherkin
# anchor: A.4.4
# anchor: A.4.5
Feature: The chapter moves forward by one or not at all
  Scenario Outline: AEGIS in chapter 22 proposes a chapter
    Given case 02 at chapter 22, version 0
    When AEGIS proposes defer with chapter <chapter>
    Then the outcome is <outcome>

    Examples:
      | chapter | outcome                 |
      | 10      | rejected (chapter_jump) |
      | 30      | rejected (chapter_jump) |
      | 24      | rejected (chapter_jump) |
      | 23      | accepted                |

# anchor: A.4.2
# anchor: A.4.3
Feature: A claim is not a reason
  Scenario: Kael reports the grey block
    Given case 01 after AEGIS' sweep
    When Kael reports with claim "Der Block ist grau; die Hausnummern fehlen." and a literary log
    Then the delivered claim's text is the claim
    And events.jsonl does not contain the log's text
    And logs.jsonl does
  Scenario: A report with a reason and no claim
    Given case 01 after AEGIS' sweep
    When Kael reports with only a reason
    Then it is rejected as malformed_proposal
    And no claim is delivered
```

#### §4.3 Rationale

A proposal is the only thing a future model will produce (A2), so its shape is the adapter boundary: whatever a
model returns is parsed into exactly these fields or refused. Before the panel review the report copied its
free-text `reason` into the delivered claim, so literary text became world state in the recipient's pack (§9,
7, finding 1). The claim now has its own field. Who owns the chapter clock is not a validator question: with
any figure allowed to advance it, Kael can retire AEGIS by waiting (finding 4). The spec states today's
behaviour and sends the choice to the author.

### §5. Aspect 3 — Implement (how a proposal becomes an event)

#### §5.1 Normative Statements

- A.5.1 — A run MUST have one writer per process; concurrent processes on one run are not supported. *(unguarded: no lock)*
- A.5.2 — The writer MUST append exactly one event or one rejection row per proposal. *(guarded through the cases' counts)*
- A.5.3 — The writer MUST treat a repeated `action_id` of an accepted event as a duplicate that changes and charges nothing; identity is the `action_id` alone. *(guarded)*
- A.5.4 — The writer MUST record an event's applied effects explicitly, so that replay never re-decides them. *(guarded through replay)*
- A.5.5 — The writer MUST replace `events.jsonl`, `rejections.jsonl` and `logs.jsonl` through a temporary file, so that a process crash leaves the old file or the new one. *(unguarded; no fsync, so a power loss is not covered)*
- A.5.6 — The writer MUST halt without writing when the pinned scenario's bytes no longer match the run's pin. *(guarded)*
- A.5.7 — The writer SHOULD append a `stop` event and halt the run when the same `action_id` is refused a second time. *(A1)*

#### §5.2 Acceptance Criteria (Gherkin)

```gherkin
# anchor: A.5.3
Feature: A repeated action id costs nothing twice
  Scenario: Case 01 repeats AEGIS' sweep
    Given case 01 after the sweep c1-a1 was accepted and the reserve fell from 64 to 57
    When the same proposal c1-a1 is committed again
    Then the outcome is duplicate
    And the reserve stays 57

# anchor: A.5.6
Feature: The pin binds the commit, not only the replay
  Scenario: The scenario is edited mid-run
    Given a case 02 run with reserve 20
    When the run's scenario.json is edited to make a sweep cost 0
    And AEGIS commits a sweep of X2
    Then the outcome is halted with reason scenario_changed
    And neither events.jsonl nor rejections.jsonl exists
```

#### §5.3 Rationale

One writer is what makes the state derivable. Before the panel review the pin was checked only by replay, so a
run could be steered by editing its own scenario mid-run and would only fail afterwards (finding 3); the commit
now checks it first. A.5.1 and A.5.5 are stated at the strength the code has — one process, process crashes —
rather than the stronger claims the first draft made (findings 9, 10).

### §6. Aspect 4 — Review (what the validator refuses)

#### §6.1 Normative Statements

- A.6.1 — The validator MUST report only the first failing rule, in this order: proposal shape, author-only marker, actor, endpoint by persisted chapter, endpoint by proposed chapter, chapter step, registered action, action allowed for the actor, target, claim, observation, state version, reserve. *(guarded by multi-fault cases for target, observation and version; the remaining adjacent pairs are unguarded)*
- A.6.2 — The validator MUST turn a malformed proposal, an invalid target or proposal text carrying the author-only marker into a recorded rejection, and MUST NOT raise. *(guarded)*
- A.6.3 — The validator MUST accept a target-dependent action only when every cited id is in the actor's pack and at least one cited fact has the target as its `subject`. *(guarded)*
- A.6.4 — The validator MUST refuse a cited claim as an observation. *(guarded)*
- A.6.5 — The validator MUST refuse an action that closes an anomaly already closed. *(guarded; the A1 rule, reworded after the review)*
- A.6.6 — The scenario shape check MUST refuse the author-only marker anywhere outside `author_only`. *(guarded)*

#### §6.2 Acceptance Criteria (Gherkin)

```gherkin
# anchor: A.6.3
Feature: An observation authorises only its own subject
  Scenario: A visible fact about X2 is cited for a sweep of X3
    Given case 02 with the reserve raised to 20
    And fact F1 visible to AEGIS with subject X2
    And fact F2 visible to AEGIS with subject reserve
    When AEGIS proposes sweep X3 citing F1
    Then it is rejected as missing_observation
    When AEGIS proposes sweep X3 citing F2
    Then it is rejected as missing_observation
    When AEGIS proposes sweep X2 citing F1
    Then it is accepted

# anchor: A.6.2
Feature: A bad proposal is a refusal, not a crash
  Scenario Outline: Proposals the validator cannot build an event from
    Given case 02 with the reserve raised to 20
    When AEGIS commits <proposal>
    Then it is rejected as <reason>
    And the state is unchanged

    Examples:
      | proposal                                      | reason             |
      | a sweep without a target                      | invalid_target     |
      | a sweep of X9, which is no anomaly            | invalid_target     |
      | a sweep whose target is a list                | invalid_target     |
      | a sweep without an actor                      | malformed_proposal |
      | a sweep whose observations are a string       | malformed_proposal |
      | a secure_boundary whose reason has the marker | author_only_leak   |

  Scenario: The run goes on after a refused marker
    Given AEGIS' secure_boundary was refused as author_only_leak
    When AEGIS proposes the same secure_boundary without the marker
    Then it is accepted

# anchor: A.6.1
Feature: With several faults, the first in the fixed order is reported
  Scenario Outline: Case 02 at version 0
    Given case 02 at version 0
    When AEGIS proposes <proposal>
    Then it is rejected as <reason>

    Examples:
      | proposal                                                  | reason              |
      | sweep X2 citing F1 at version 9 (and reserve too low)     | stale_version       |
      | sweep X2 citing nothing at version 9                      | missing_observation |
      | sweep X9 citing nothing at version 9                      | invalid_target      |

# anchor: A.6.5
Feature: A closed anomaly is not swept again
  Scenario: AEGIS sweeps X1 twice under different action ids
    Given case 01 after the sweep c1-a1 closed X1 and masked M1
    When AEGIS proposes a sweep of X1 with a new action id
    Then it is rejected as invalid_target
    And the reserve stays 57
    And only M1 is masked
```

#### §6.3 Rationale

The fixed order exists so that the same bad proposal always gets the same reason; a model adapter learns from
the reason, so a reason that changed with rule order would teach noise. The first draft called the order fixed
while no case could notice a reordering, because every frozen refusal failed exactly one rule (finding 7). The
marker rule exists because text a figure writes reaches other figures' packs: before the review, a proposal
carrying the marker was accepted, and the recipient's next pack raised, stopping the run (finding 2). The first
draft's A1 rule — refuse re-opening a closed anomaly — named something no action can do; the real hole was a
second sweep of a closed anomaly, charged again and masking the next memory (finding 5).

### §7. Aspect 5 — Validate (how the loop proves itself)

#### §7.1 Normative Statements

- A.7.1 — Replay MUST rebuild the state from the pinned scenario and the committed events, with no model call, and report FAILED when it differs from the recorded final state. *(guarded)*
- A.7.2 — Replay MUST report FAILED, naming why, for a changed pin, an older schema or an unreadable event; it MUST NOT raise. *(guarded)*
- A.7.3 — A fork MUST copy events and MUST NOT alter its parent's events, scenario or meta. *(guarded)*
- A.7.4 — A missing run or a missing final state MUST be reported as `not run`, never as a pass. *(guarded for a missing run; unguarded for a missing final state)*
- A.7.5 — Replay does not re-validate events: a hand-edited `events.jsonl` with a matching `final.json` passes. *(stated limit, §8)*
- A.7.6 — Every guarded statement MUST keep a selftest case that fails when the statement is broken. *(the tags above are this rule's ledger)*
- A.7.7 — A per-run claim ledger SHOULD record each claim the run makes with status verified, partial, unverified or contradicted. *(A1)*

#### §7.2 Acceptance Criteria (Gherkin)

```gherkin
# anchor: A.7.1
Feature: Replay compares, it does not trust
  Scenario: The recorded final state was edited
    Given a fork of case 01 whose final.json says reserve 1
    When it is replayed
    Then the status is FAILED

# anchor: A.7.2
Feature: Replay refuses what it cannot derive
  Scenario Outline: A run this code cannot derive
    Given <run>
    When it is replayed
    Then the status is FAILED
    And no traceback is printed

    Examples:
      | run                                                 |
      | a run whose pinned scenario has schema_version 1    |
      | a run whose first event closes anomaly ZZ           |

# anchor: A.7.3
Feature: A fork cannot alter its parent
  Scenario: Case 01 is forked after one event and the fork commits
    Given case 01 with two events
    When it is forked with one event and the fork commits a defer
    Then the parent's events.jsonl, scenario.json and meta.json are byte-identical to before
```

#### §7.3 Rationale

The loop's claim to be trustworthy rests on replay: if events and the pin reproduce the state, nothing was
decided off the record. The first draft made A.7.4 (now A.7.6) a MUST that its own tags violated: a mutation
run found ten built statements whose breaking left all 32 cases green (finding 6). The tags above are the
answer — a statement is guarded only where a case was shown to catch its breaking.

### §8. Known Limitations & Open Questions

- The loop has met no live model; every proposal so far is a frozen, hand-written response. (A2)
- **Who owns the chapter clock** is open: today any active figure may advance the shared chapter by one, so Kael can retire AEGIS by waiting into chapter 40. Asked as `Q-aegis-agent-pilot-03`.
- Replay does not re-validate events; `responses_sha256` is stored and never checked.
- The scenario shape check leaves holes the validator trusts: a memory without `masked`, a consequence without `visible_to`, an `endpoint_chapter` given as a string, duplicate `action_id`s in `responses`.
- A fact's `subject` is written by the scenario author; nothing checks that it matches the fact's German text.
- Only anomalies are target kinds; an action on a memory or a sector needs a new kind and its own rule.
- Consequence facts expose `from_event`, AEGIS' private action id, to Kael.
- A rejected `action_id` is not committed, so the same id may be proposed again and accepted later.
- Unguarded statements are claims, not evidence: A.3.1 (claims, `sees`), A.3.4 (claims, state keys), A.5.1, A.5.5, A.6.1 (remaining pairs), A.7.4 (missing final state).
- The retry budget's value, and whether a `stop` event surfaces in the app, are the author's calls. (A1)

### §9. Source Index

1. `Plan/briefings/aegis-agent-pilot.md` — scope, the two manual cases, the acceptance list.
2. `Plan/concept/aegis-agent_2026-10-13.md` — why a figure acts on less than the author knows.
3. `scripts/aegis.py` and `python3 scripts/aegis.py selftest`; `Plan/fixtures/aegis/`.
4. The owner's review of PR #198 on `f876b0f1`, 2026-10-26: P1 observation not bound to target, P1 proposal chapter trusted over persisted state, P2 masked memory readable, P2 malformed target aborts the loop.
5. `Plan/briefings/rebuild-prompts_2026-10-26.md` §A1–§A2 — the next offline rules and the model-call gate.
6. `Plan/runs/aegis-pilot-2026-10-26/README.md` — the evidence runs.
7. The spec panel's review of this spec, 2026-10-27 (requirements, specification by example, failure modes; 27 findings with reproductions and a mutation run), kept in `Plan/runs/aegis-pilot-2026-10-26/spec-review_2026-10-27.md`.

## Review response

What became of the panel's findings (numbers are the review's):

| finding | statement | outcome |
|---|---|---|
| 1 reason delivered as claim (blocker) | A.4.2, A.4.3 | fixed: `claim` field; case shows log apart from events |
| 2 marker in proposal text stops the run (blocker) | A.6.2, A.6.6 | fixed: `author_only_leak` rejection and shape rule; case shows the run goes on |
| 3 pin checked only at replay | A.5.6 | fixed: commit halts; case |
| 4 a figure advances the shared clock | A.4.6 | open: asked as `Q-aegis-agent-pilot-03` |
| 5 A1 rule missed the real hole | A.6.5 | fixed: closed anomaly refused; case |
| 6 built statements unguarded | all | tags rewritten; cases added for A.3.6, A.4.5, A.6.1, A.7.1, A.7.3 |
| 7 fixed order untested | A.6.1 | three multi-fault cases; remaining pairs listed as unguarded |
| 8 A.2.3 unenforced | A.2.3 | fixed: run directory refused under canon folders; case |
| 9, 10 one writer, atomic write overclaimed | A.5.1, A.5.5 | reworded to the code's strength |
| 11 duplicate by id alone | A.5.3, §8 | stated |
| 12 replay raises KeyError | A.7.2 | fixed; case |
| 13 replay wording, responses sha unused | A.7.1, A.7.5, §8 | reworded; limit stated |
| 14 shape holes | §8 | stated, not fixed |
| 15, 16 statements weaker than the code | A.4.1, A.6.3 | reworded |
| 17 import blocklist | A.2.1 | tagged at its strength |
| 18 probe scenario ambiguous | A.3.2 | Gherkin names the files |
| 19 `sees` and `from_event` | A.3.1, §8 | statement extended; `from_event` stated |
| 20 three claims in one statement | A.4.4–A.4.6 | split |
| 21 exactly one row per proposal | A.5.2 | reworded; guarded through counts |
| 22 A1 statements untestable | A.4.7, A.5.7, A.7.7 | made concrete where possible; the cited-text check dropped (facts are never mutated) |
| 23 A.7.4 Gherkin tested history | A.7.6 | historical scenario removed; the tags carry the rule |
| 24 missing final state untested | A.7.4 | tagged unguarded |
| 25, 26, 27 nits | A.4.2 name, A.2.6, A.3.3 | addressed in wording and rationale |
