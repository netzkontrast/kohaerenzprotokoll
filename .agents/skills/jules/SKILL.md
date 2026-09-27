---
name: jules
description: Spawn a Google Jules session — Google's remote coding agent, which clones a GitHub repository into a VM, plans, edits and publishes a branch — and drive it to a verified result with scripts/jules.py; write its prompt so the work is actually published, approve its plan before that state times out, answer its questions, read what COMPLETED means for this session, and recover work that stayed in the VM. Use when asked to hand a coding task to Jules, dispatch or spawn a Jules session, check on one, approve its plan, message it, or find out why a session that says COMPLETED left nothing on the remote — and before any Jules call, because a session takes the whole repository, corpus included, to Google.
---

# Jules — a remote agent, driven by one script

Ported on 2026-09-26 from `netzkontrast/agency` — the code from
`agency/capabilities/jules/`, the doctrine from its `AGENCY_PROTOCOL.md`, specs
012 and 013, and its lessons learned. `references/agency.md` maps every piece to
its source and records where those sources disagree. `scripts/jules.py` is the
one encoding (P6): this page says when to run what and what the output means.

## Before anything: the author's yes

A session is Google's agent working on a clone of the repository — `Sources/`,
`Wiki/` and every draft included. That is corpus text leaving the repository,
so the rule `NOW.md` states for Jev and free models applies: **`dispatch` and
`message` refuse without `--approval` naming the author's decision.** Never
write an approval the author has not given. If there is none, note the question
in `NOW.md` under *Questions for the author* and carry on without it.

Reading is not sending: `sources`, `list`, `status`, `activities`, `plan`,
`patch` and `triage` send only the key. `netzkontrast/kohaerenzprotokoll` is a
connected source (2026-09-26).

**Decide before dispatching.** A dispatch is a one-way door: the API has no
cancel. Jules earns its cost on a task that can wait (agency's rule: 30 minutes
or more of slack), is self-contained, and can be audited as a pull request.
Never answer a direct question from the person by dispatching — answer it.

## The loop

```bash
python3 scripts/jules.py dispatch --prompt-file task.md --branch main --title "…" \
    --scope scripts/,Plan/ --approval "<the author's decision>" --dry-run   # read it first
python3 scripts/jules.py dispatch …same, without --dry-run…                # prints the session
python3 scripts/jules.py triage <session>        # what the state means, and what to do next
python3 scripts/jules.py plan <session>          # when triage says a plan waits
python3 scripts/jules.py approve <session>
python3 scripts/jules.py message <session> --prompt-file answer.md --approval "…"
python3 scripts/jules.py patch <session> --out <scratchpad>   # diff sizes; bodies to files
```

Print the session's `url` (`https://jules.google.com/session/<id>`) for the
person every time — it is where they can see and steer it.

### 1. The prompt

Write the task. `dispatch` prepends the preamble (`jules.py preamble` prints
it), which:

- names the five canonical tools — **`submit` is the only one that publishes**;
  prose like „open a PR when done" leaves the work in the VM, the failure that
  cost agency most;
- tells a session on this repository to read `CLAUDE.md`, `PRINCIPLES.md` and
  `NOW.md` first, and states the canon rules;
- turns `--scope` into a hard allow-list: outside it, the session publishes a
  `BLOCKED:` branch and stops;
- forbids asking and then idling, and forbids committing PR text or scratch files.

`--raw` sends your text alone, and `dispatch` refuses it unless it names the
tools itself (`lint`). Never tell a session „don't open a PR": sessions
conflate it with „don't push".

Give parallel sessions **disjoint files**. They share a base commit, and a
broad „do everything" prompt is how scope creep starts.

### 2. The gates

| flags | meaning |
|---|---|
| default | the plan waits for `approve`; the agent confirms the PR |
| `--auto-pr` | the plan waits; an approved plan ends in a PR on its own (`automationMode: AUTO_CREATE_PR`) |
| `--auto-pr --no-plan-approval` | zero-touch — only with a tight `--scope` |

**Never approve without reading the plan.** It is the cheapest review point
there is: no PR exists yet, and `plan` is the only view of the intent. Approve
promptly — a plan left waiting is discarded and the session ends COMPLETED with
nothing (how soon is unmeasured). A `message` asking for a revision while a
plan waits can end the session: `triage` afterwards and expect PLANNING, not
COMPLETED. **`--auto-pr` is unconfirmed**: agency recorded one session where it
was silently ignored. Check the first time that a PR really opens.

### 3. Reading the state — `triage`

COMPLETED alone says nothing. `triage` reads the session, its activities, its
pull request's branch on the session's own repository (`git ls-remote`) and its
diffs, and answers with one action:

| action | when | do |
|---|---|---|
| `wait` | QUEUED, PLANNING, IN_PROGRESS | poll again later; reads lag, so trust a transition only after two polls |
| `review_and_approve_plan` | a plan waits — including COMPLETED with a plan never approved | `plan`, then `approve` |
| `answer_agent_question` | AWAITING_USER_FEEDBACK; `evidence.agent_message` is the question | `message` a concrete answer. A session left waiting on its own question times out and fails |
| `verify_pr` | COMPLETED, its branch on the remote, a PR attached | review the PR against the scope |
| `open_pr` | the branch is there, no PR | open it |
| `recover_silent_fail` | COMPLETED, a diff exists, no branch | the work stayed in the VM — see 4 |
| `dispatch_fresh` | FAILED, or COMPLETED with no diff and no branch | dispatch again, narrower. `message` cannot revive FAILED |
| `inspect_and_resume` | PAUSED | often transient while a message is processed; poll twice before acting |
| `terminal` | CANCELLED | nothing |

Poll at a pace that fits the work: agency's watcher used 10 s in the first five
minutes after a transition, 30 s up to twenty, 300 s after that, and backed off
on a 429. In a Claude Code session, schedule a check-in rather than looping.

### 4. When the work stayed in the VM

**Never re-dispatch while a diff exists** — that throws the work away. Probe
once with `message` (needs `--approval`): „Your state is COMPLETED but there is
no branch on origin. Push your branch and reply with the PR URL, or reply
EMPTY." Wait, triage again, and allow two or three probes about five minutes
apart. Then `patch <session> --out <scratchpad>` writes each diff to a file
that `git apply` takes; stdout carries only its size. A diff can be taken while
a session still runs, from its newest activity. **Two silent fails on one task:
stop dispatching it, and do it locally.**

## What a session may not do here

The preamble says it, and a session's pull request is reviewed against it like
any other: canon prose stays German and untranslated; `Sources/drive/` and the manifest
are never changed, and under `Sources/` only a census and a note are written, by
`ingest`; a `Wiki/` page is committed with its source document named in the
first line; a decision that would rest on a guess is asked with
`request_user_input`. A session's reading is a reading, never a promotion: P0's
two decisions stay the author's.

Every dispatch, message and approval is a line in
`Plan/runs/jules/ledger.jsonl` — the full prompt, the approval, and whether it
was answered, refused or unreached.

## Provisional

```yaml
name: jules            # provisional
# may not: dispatch without the author's decision named in --approval,
#          promote a page, settle a conflict, or approve a plan unread
# retire when: ten dispatched sessions show it adds nothing over a Claude session
```
