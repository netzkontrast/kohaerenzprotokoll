# Where `jules.py` came from, and what agency's sources disagree on

Read from `netzkontrast/agency` on 2026-09-26, at the head of its default branch
that day. Paths are that repository's.

## The code, piece by piece

| here (`scripts/jules.py`) | there | changed |
|---|---|---|
| `_request`, `_paginate`, `_translate_http_error`, `short_id` | `agency/capabilities/jules/api.py` | `urllib` for `httpx`; a 5xx body is kept whole |
| `resolve_source`, `coerce_source`, `owner_repo` | `api.py` `_resolve_github_source`, `_coerce_source` | the direct name `sources/github/<owner>/<repo>` is asked first; the listing only on a 404 |
| `dispatch` | `api.py` `jules_create`, `_main.py` `dispatch` | refuses without `--approval`; refuses a final prompt `lint` fails; records to a ledger, not a graph |
| `status` | `api.py` `jules_get` | adds each output's pull request url and `headRef` |
| `list_sessions`, `activities`, `plan`, `approve`, `message` | `api.py` | `message` refuses without `--approval`; summaries are not cut to 280 characters |
| `patch` | `api.py` `jules_patch_extract`, `_main.py` `patch_body` | falls back to the newest activity artifact; `--out` writes bodies to files instead of a 4 KB slice |
| `verify` | `_main.py` `verify`, `agency/capabilities/_vcs.py` | `git ls-remote --heads` directly |
| `TOOLS`, `DOCTRINE`, `assemble`, `lint`, `MUST_NAME` | `preambles.py` | the doctrine points at this repository's `CLAUDE.md`, `PRINCIPLES.md`, `NOW.md`; Mode B (clone agency read-only into a foreign repository) dropped; lessons 01, 02 and 12 added to the preamble |
| `triage`, `ACTIONS` | `watch.py` `_classify`, `INSTRUCTIONS`; `AGENCY_PROTOCOL.md` §1 | one-shot, no previous state; adds `open_pr` (§1 case 3's sub-case); the branch comes from the session's pull request, checked on the session's own repository |

Not ported: the watcher's poll loop, event queue and heartbeat (`watch.py`); the
probe-and-recover cycle (`_main.py` `recover`); the patch → GitHub MCP planner
(`patch.py` `build_recovery_plan`, which only handles whole-file rewrites);
aliases, bulk approval, quota and `status_all`; the six walkable skills in
`skills.py` (their content is in `SKILL.md`); `review_comment` (its tail is the
preamble's `reply_to_pr_comments` line).

## The doctrine, and where it stands there

- COMPLETED is not done, four cases — `AGENCY_PROTOCOL.md` §1 (L14–48).
- Name `submit` and `pre_commit_instructions` — §2 (L50–75); dogfood evidence
  in `Plan/inprogress/012-…/DOGFOOD-NOTES.md` L77–87: both sessions ended
  COMPLETED with outputs and no branch.
- Scope is a hard allow-list, `BLOCKED:` outside it — §3.
- Questions through `request_user_input`, never `message_user` — §4.
- Probe, then recover from the patch; never respawn over a diff — §5,
  `docs/vision/LESSONS.md` L14–32.
- The flag matrix — §7; `Plan/done/013-…/DESIGN.md` L225–240.
- Two silent fails → do it locally — `Plan/_research/agency-system-import/skills/agentic/jules-orchestrator-discipline/SKILL.md`.
- Never ask and idle; `[BLOCKED: …]` instead — lessons 02 and 12 in
  `Plan/_research/agency-system-import/Plan-_lessons-learned/`.
- Jules commits scratch files — lesson 01.
- After `message`, poll two cycles; PAUSED is transient during a message —
  lessons 09 and 10.
- Plan approval is the cheapest review; never auto-approve —
  `…/skills/jules/references/parallel-orchestration.md`, spec 012 OQ4.
- Dispatch is a one-way door; disjoint scopes —
  `skills/jules-dispatch/SKILL.md` L28–50.
- When Jules and not a local agent — spec 040 L204–243.

## Where the sources disagree

1. **Where a session's diff lives.** `api.py` reads
   `outputs[].changeSet.gitPatch.unidiffPatch`; `…/references/harvest-patterns.md`
   says diffs „do NOT live in `outputs`", only in activity artifacts.
   **Measured, 2026-09-26, one COMPLETED session:** both. The output carried the
   final diff (`baseCommitId`, `suggestedCommitMessage`, `unidiffPatch`) and a
   second output the pull request (`url`, `headRef`, `baseRef`); 17
   `progressUpdated` activities carried one diff artifact each. `patch` reads
   outputs first and artifacts second.
2. **Whether `AUTO_CREATE_PR` works.** `AGENCY_PROTOCOL.md` recommends it;
   `harvest-patterns.md` recorded it silently ignored on one session.
   **Unmeasured here.** The session read on 2026-09-26 echoed no
   `automationMode` at all, so an echo cannot tell.
3. **How long an unapproved plan waits.** §1 says indefinitely; the imported
   `state-machine.md` says it is discarded; `watch.py` says „~5 min" with no
   source. **Unmeasured.** The skill says: approve promptly.
4. **Whether `message` during plan approval is safe.** `caveats.md` trap 2: it
   can end the session. Not contradicted anywhere; the skill carries it.
5. **How to word publishing.** `silent-fail-recovery` says never tell Jules to
   push; `AGENCY_PROTOCOL.md` §2 says name `submit`; `harvest-patterns.md` says
   „don't open a PR" gets read as „don't push". The preamble names `submit` and
   never says „don't open a PR".
6. **Auto-approval.** Imported workflows default to approving; agency's own
   rule is never. The port has no bulk approval.
7. **Code drift there.** `watch.py`'s recovery `verify_pr` instruction is the
   literal `"..."`; re-emission keys on activity id where spec 012's review
   says ids are unstable; `AGENCY_PROTOCOL.md` names a `network_error` action
   the code does not have. None of it was ported.
