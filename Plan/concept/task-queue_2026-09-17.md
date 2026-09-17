# A task queue that cannot be wrong — derived, not maintained

*2026-09-17. Concept, not a build. Written because work has started triggering
other work: merging document 6 silently invalidated two finished reconciliations,
and nothing but a person noticed.*

## First: the transcript exists, and it is what postpones the task safely

Reconciliation already keeps a complete, per-document record. Two files and one
check:

| | |
|---|---|
| `Plan/runs/<slug>/reconcile.json` | `state_before` → `state_after`, machine-readable |
| `Wiki/compare/reconcile-NN-<slug>.md` | the prose record of what happened |
| `python3 scripts/account.py order` | verifies the chain, and names the gap |

The chain today is unbroken:

```
entropie-aegis                                    0 → 14
aegis-emergenz-aus-der-leere                     14 → 24
kohaerenzprotokoll-aegis-und-systementropie      24 → 32
guardians-und-kern-welten-konzept                32 → 46
aegis-subplots-kapitelweise-system-exploration   46 → 46      ← zero, on purpose
roman-lokalitaeten-konzept-und-ausarbeitung      46 → 56
```

**So the two pending `orte-konzept-fuer-kohaerenz-protokoll` reconciliations are
provably stale rather than arguably stale.** Both recorded `state_before: 46`;
the chain now ends at 56. Nobody has to remember that — it is a comparison of two
numbers that are already written down.

That is what makes postponing safe, and it is also the whole design principle
below: the record of what is done is *evidence*, not a tick.

## The problem a queue has to solve, stated from the one case we have

Merging document 6 did four things at once:

1. left the wiki at 56 pages;
2. **invalidated** two completed reconciliations that assumed 46;
3. created 10 pages that nothing links to, which made `link.py` open again;
4. moved the `fold()` baseline from 65% to 58%, because the trainset grew.

Only (1) was intended. Three consequences fell out of it, and each is a task
nobody wrote down. **Work here triggers work, and the trigger is a change in
measured state** — not someone's plan.

## Why this is not the backlog `CLAUDE.md` forbids

`CLAUDE.md`: *„There is no board, no status field and no backlog."* That rule
stands, and this does not break it, for exactly the reason `state.py` does not
break „state is derived, never stored":

**A task is not recorded. It is measured.** Nothing is created, assigned, moved
or closed. A rule reads the repository and says what is incomplete right now. A
task disappears because the repository changed, never because someone ticked it.

The failure a backlog has — an item that is done and still listed, or done and
quietly undone — cannot occur, because there is no list to go stale.

So: **`done` is a measurement, not a flag.** That single decision removes the
entire class of defect this project keeps finding.

## The shape

The queue is the existing verb at a new scale. `account(subject, question)`
already covers a document, a term, a pair and the corpus. A task is:

    task = (verb, subject)        # ("reconcile", "orte-konzept-…")

and each verb is a rule, registered the way a measurement is:

```python
@task("reconcile", needs=("census", "note"))
def _open_reconciliations() -> list[str]:
    """Subjects whose reconciliation is missing or was run against a state
    the wiki has since left."""
```

Three states, all derived, none stored:

| state | means |
|---|---|
| **ready** | every precondition measures true; it can be started now |
| **blocked** | a precondition is false, and the queue names *which* task would satisfy it |
| **stale** | it was done, and the state it was done against has moved |

`stale` is the one that earns the build. It is how document 7 comes back on its
own, and how the three unintended consequences above would have appeared without
anyone noticing them.

## What it must refuse

**A task may not start while a task it depends on is open.** This is not advice;
the repository already enforces it in two places and the queue generalises them
rather than replacing them:

- `capture.py --count` refuses without `03-candidates.md`
- `account.py order` refuses to pass while any document is half-done

The queue's `--check` exits non-zero when a *started* task's preconditions do not
hold, so „I'll just do the reconciliation first and fix the census after" is
caught by a command instead of by a reviewer.

**And it may not invent a dependency.** A precondition is a measurement that
already exists — a file, a count, a `state_after`. If a dependency cannot be
measured, it is not expressed as one; it is a sentence in `NOW.md` for a person.
A guessed edge in a task graph is the same defect as a guessed edge in the wiki.

## What it must not become

- **Not a planner.** It says what is open and what blocks what. It does not
  choose, schedule or prioritise — which document to read next is answered by the
  open questions, and that stays a person's call.
- **Not a second source of truth.** It reads `state.py`, `account.py`,
  `relations.py` and the run records. It stores nothing and it writes nothing
  except its own output to stdout.
- **Not a replacement for `NOW.md`.** `NOW.md` holds what a *person* has to
  decide — open judgement, not open work. The queue holds what is mechanically
  incomplete. Two different questions; conflating them is how a board grows.

## The first rules, and only these

Small enough to be right, and each one is a case that has already happened:

| verb | needs | open when |
|---|---|---|
| `land` | — | a manifest row in a wanted category has no `export_path` |
| `census` | `land` | a landed document has no `Sources/terms/<slug>.md` |
| `note` | `census` | a census exists and no note does |
| `reconcile` | `census`, `note` | no `reconcile.json`, **or** its `state_before` is below the previous run's `state_after` |
| `link` | `reconcile` | `relations.py --unmarked` is above zero for a page written since the last pass |
| `quotes` | — | `quotes.py` reports an unresolved citation |

Six rules, five of which are two lines of existing code each. The sixth — the
`reconcile` staleness test — is the one that had to be learned, and it was
learned the expensive way today.

## The order

1. **The registry and the three states**, over the six rules above. It reports;
   it changes nothing.
2. **`--check`**, the refusal: non-zero when an open task's dependency is open.
   Add it to the invariants the `tools` skill runs first.
3. **Only then, if it has earned it:** a `--why <task>` that prints the chain of
   preconditions, because by then there will be a task whose blockage is not
   obvious.

**Retire when:** three sessions pass in which the queue reports nothing a person
had not already written in `NOW.md`. Then the measurement was the ceremony, and
`NOW.md` was enough.
