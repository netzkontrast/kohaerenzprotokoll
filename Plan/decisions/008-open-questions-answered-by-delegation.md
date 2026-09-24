# 008 — The tool review's open questions, answered by the session on the author's delegation

**Date:** 2026-09-24 · **Decided by:** the session, because the author said „Answer the questions for me yourself" · **Status:** chosen; each answer is reversible by the author at any time

## How these were answered

The author delegated. So every answer below takes the **conservative** side —
the one that sends no new corpus text, builds nothing unproven, and changes
nothing outside this repository — unless the evidence clearly argues otherwise.
None of them is a promotion or a user-facing flag, the two decisions P0 says are
never a session's to make. Where an answer is a recommendation about the author's
own machine or workspace, it is marked as advice, because a session cannot decide
it.

## The review's six (`Plan/concept/tool-review_2026-09-24.md`)

| # | question | answer | why |
|---|---|---|---|
| 1 | May documents 5 and 6 be sent again, each tool run alone? | **Yes, bounded:** the same two documents, the same tools, free models, `data_collection: deny`, through `route.py` — added to decision 007's scope. **Not run now.** | Their text has already gone to these endpoints, so a rerun exposes nothing new; the three tools that failed did so for reasons a rerun can separate (rate limits from sharing, `instructor` parsing). Worth running only when someone wants the answer. |
| 2 | Hyper-Extract templates: patch the fork, copy into the install, or wait? | **Wait.** | The stand-in `general/set` scored F1 0.16, below the Haiku floor of 0.25. Changing a fork or a shared install for templates of unproven value inverts P3. Revisit when any extractor clears the floor. |
| 3 | Widen Jev's consent — more documents, more context per pair? | **No.** | 16 of 26 overall and 2 of 5 on the one class it would serve. That does not justify sending more corpus text. It stays a trial on paper. |
| 4 | The Notion workspace „Kohärenz Protokoll" (2026-03-26): retired, or a read-only mirror of `NOW.md`? | **Neither is done: no mirror, nothing touched.** Treated as outside the project. | A mirror is a second copy that drifts (P6, P20). Retiring or deleting the author's own workspace is not a session's action. |
| 5 | Does the author run oh-my-openagent against this repository on their own machine? | **Advice, not a decision: don't, or only with `OPENCODE_PURE=1`.** | With the plugin loaded it read a file outside its working directory without asking and contacted a remote server by itself. |
| 6 | A Docker daemon in the cloud environment, for `cgr check`? | **No.** | Jev scored that proposal lowest of all (0.15), and `cgr` reads no markdown. |

## The templates page's four (`Plan/concept/hyperextract-templates_2026-09-24.md`)

| question | answer |
|---|---|
| Carry `scope` (world / lens) as a field? | **Yes, provisional as marked** — it costs nothing until a template runs, and the scorer already uses it. |
| May a model's stance label order what a person reads? | **No.** Decision 004 gives stance to the person, per passage; ordering by a model's label is the first step of letting it decide. |
| Is a person's review of `StatedRelations` worth the time? | **No, not now.** No template runs (answer 2); there is nothing to review. |
| May the templates restate rules from the extraction briefing and the entity-lists prompt? | **Yes, while provisional.** Generating one from the other is building ahead of use. |

## `NOW.md`'s three encodings of one rule

**No refactor now.** `lmrun.py` stays the gate for DSPy programs, `route.py` for
third-party tools and direct calls, `rlm_ingest.py` and `bilingual.py` as they
are. They agree today; unifying them is work with no instance asking for it.
Revisit when one of them changes its rule and the others do not.

## What would change these answers

The author saying so — each answer above is the author's to overturn, with no
decision file needed beyond noting it here. Or evidence: an extractor that clears
the Haiku floor reopens 2 and the `StatedRelations` question; a cheaper signal
for near matches failing reopens 3.
