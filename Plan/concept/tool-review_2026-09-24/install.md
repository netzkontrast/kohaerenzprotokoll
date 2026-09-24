# install.sh + the session-start hook — tool review, 2026-09-24

Row 8 of `Plan/concept/tool-review-plan_2026-09-24.md`: `--check`, one
component's reinstall timed, review only. This tool moves no corpus text and
makes no model call, so decision 007's router, the API-key label rule and
P18's two-attempts rule do not apply here — there is nothing for them to bind.
**Reached: yes.**

## What ran

```
bash scripts/install.sh --list
bash scripts/install.sh --check
uv tool uninstall jev-skill && time bash scripts/install.sh jev
time bash scripts/install.sh --check
python3 scripts/selftests.py
```
Outputs saved: `Plan/runs/tooltest/install/list.txt`,
`Plan/runs/tooltest/install/check.txt`,
`Plan/runs/tooltest/install/selftests.txt`.

The script itself is `bash`, not `python3` — running it as `python3
scripts/install.sh` fails with a `SyntaxError` at the `case` statement (that
is a shebang mismatch on my part, not a defect in the file: its own shebang
line is `#!/usr/bin/env bash` and the doc block at the top of the file gives
the invocation as `scripts/install.sh`, which resolves the same way).

## Numbers

`bash scripts/install.sh --list`: 15 components (`Plan/runs/tooltest/install/list.txt`).
CLAUDE.md's own component table (the *A fresh container has none of the
derived things* section) currently lists seven venvs including `.venv-mflow`
and matches the 15-row `--list` output component-for-component; no drift found
between the prose and `--list`.

`bash scripts/install.sh --check`, this container (already past its own
session-start run): 14 of 15 `ok`, 1 `MISSING` — `qmd-models`, which CLAUDE.md
documents as excluded from the default set and not run at session start. This
matches; `present()` for `qmd-models` (line 79) is the only check that shells
out to another script (`scripts/setup_qmd.sh --check`) rather than testing an
import or executable directly.

**Reinstall of a cheap component, `jev`, forced from empty** (not merely
re-run against a present install, which is a 0.008s skip through `present()`):
```
uv tool uninstall jev-skill
time bash scripts/install.sh jev
```
```
Uninstalled 1 executable: jev-decide
  jev           installed (2s)
real    0m1.795s
```
The script's own per-component timer agrees with `time` to the second (`2s`
vs. `1.795s` real). `install_one jev` (install.sh:105-110) clones
`wuyoscar/jev-skill` at tag `v0.2.0` with `--depth 1` and runs `uv tool
install` on the clone — two network round trips, both small, both cached
proxy-side, which is why "seconds" holds for this one component but is not
representative of `dspy`, `grawiki` or `hyperextract`, whose installers pull
multi-hundred-MB dependency trees.

**Idempotent check-and-skip**, the common path: `bash scripts/install.sh
--check` end to end, all 15 components: `real 0m8.438s`. Every component's
`present()` (install.sh:65-81) is a fast import or executable probe except
`qmd-models`'s shell-out.

**`python3 scripts/selftests.py`: 18 held, 0 failed, 0 not run, of 18 suites**,
`real 0m59.080s`. Full pasted summary in
`Plan/runs/tooltest/install/selftests.txt`; last two lines:
```
held     graphrag answer dry-run    - Probelauf — keine echte Auswahl
18 held, 0 failed, 0 not run, of 18 suites
```
This is a repository-wide check, not scoped to `install.sh`, but it is the
number this row's task asked to paste, and its pass is evidence that
`install.sh` had in fact put every interpreter and CLI those 18 suites depend
on (`.venv-dspy`, `.venv-typesafe`'s `jev` case, `route.py`'s dependencies,
etc.) in a state where they run.

## What a fresh container still lacks

Read straight from `--check`'s one `MISSING` row plus CLAUDE.md's own table:
only **`qmd-models`** (~2.1 GB of models, index and embeddings) is absent by
design after `install.sh` runs with no arguments — needed for vector search
and `qmd query`, rebuilt by `scripts/setup_qmd.sh` on request, never at
session start. Nothing else in the 15-row list was missing in this container;
I did not test a genuinely clean container (see below), so this only confirms
that the default set, once installed, stays installed and `--check` reports it
accurately — it does not confirm every component installs clean from nothing
in this session.

## The cold-cache time that is unmeasured

CLAUDE.md says so itself, in the same paragraph that documents this hook: "The
first run here took about a minute with uv's cache already warm — a cold
container also downloads torch for `grawiki`, unmeasured; a second run is
4s." I could not measure it either, for the same reason the file gives none:
this container's uv cache, npm cache and the vendored clones' shallow history
are all already warm from this and earlier sessions' work, and forcing a
genuinely cold run means either a fresh container (outside what this
25-minute, review-only slot can spin up) or deleting the shared uv/npm caches
out from under a repository I was told to touch only under
`Plan/runs/tooltest/install/` and the review file — which a cache purge is not.
The one number I *could* add cleanly, the forced reinstall of `jev` above,
still ran against a warm `uv` and pip-proxy cache; it lower-bounds the
network-round-trip cost of one small component, nothing more. **This is a gap
in what this review can measure, not a claim that the time is fine** — the
biggest unknown named in CLAUDE.md (grawiki's CPU-torch download, ~2 GB) is
exactly the one component too expensive to force-reinstall inside this row's
budget just to time it.

## Whether the hook should stay synchronous

`.claude/hooks/session-start.sh` (read in full) runs `scripts/install.sh` with
no arguments, blocking, before the session's first turn, only when
`CLAUDE_CODE_REMOTE=true` (a no-op on a local machine — confirmed by reading
the early exit). Its own comment states the reason: "Synchronous: the session
starts once this finishes, so no step races an install." That reason holds
under what I measured: `--check` and the two selftests above both depend on
components (`.venv-dspy`, `jev-decide`, `.venv-typesafe`) that a step run in
parallel with a background install could catch half-built, and `present()`'s
checks are exact-version imports (`dspy.__version__ == '3.3.1'`,
`m.version('semantica') == '0.7.0'`) rather than "something is there" — a
race would not fail loudly, it would silently hand a step a different version
than the one pinned. A component that fails does not block the session (the
hook `cat`s the log and continues either way; confirmed in
`scripts/install.sh`'s trailing block, which reports `failed` but still exits
per-component rather than aborting the loop) — so "synchronous" here already
means "blocks other work, not other components."

The cost side is the warm-cache number above: about a minute when the caches
are warm (this session's actual `.install.log` shows every default component
already `ok` — no fresh installs happened this session, so I cannot time a
warm-but-needs-it run either), unmeasured cold with the grawiki/torch pull as
the likely long pole. A synchronous minute-ish wait at session start is a
different cost than a synchronous cold-container wait of unknown minutes; the
repository does not currently know which one a fresh cloud container pays.

## Names

Not applicable to this tool: `install.sh` and the session hook produce no
model output and read no document, so `scripts/entities.py score` has nothing
to score, and no names file was produced or attempted.

## Sending corpus text

None sent, none attempted. Nothing in this row touches `Sources/`, a document
slug, or the router; decision 007's two named documents were never opened by
this test.

## What broke, and why

Nothing broke. The only friction was mine: invoking the script with `python3`
first, which is not how the file or its own doc comment describe it.

## Where this tool's output could go, under the repository's limits

`install.sh`'s output is presence/absence and timing — never a reading of a
document, so the "a model's output is a reading" limits (no page, no
`[[link]]`, no count, no merge, no conflict detection) do not bind it at all;
there is no model output here to constrain. Its place in the loop
(`.claude/skills/tools/SKILL.md`'s phases) is **0-check**, literally: the
phase's own invariant table already lists `python3 scripts/account.py order`
as the pipeline's own well-formedness check, and `install.sh --check` is the
same kind of gate one layer down — "is the substrate here at all" before
"is the pipeline's state consistent." It has no bearing on 1-choose,
2-ingest, 3-reconcile, 4-remeasure, `ask`, `promote`, or the side tracks
(entity-lists, bilingual, search, route): none of those steps calls it, and
none should start calling it per-step, since its cost (seconds to a minute)
is a session-start cost, not a per-document one.

## Recommendation

**Adopt** (already adopted; this reviews what is running, not a change).
**Evidence**: `--check` reports 14/15 `ok` with the one documented exception;
a forced reinstall of one component took 1.8s real / 2s self-reported,
agreeing with each other; `selftests.py` holds 18/18 after whatever
`install.sh` last did in this container. **May not**: this review cannot
certify the cold-container number CLAUDE.md already flags as unmeasured —
adopting the hook's current shape is not the same claim as knowing its worst-
case cost. **Retire the trial-worthy gap when**: someone times one real cold
container start (a fresh `env_...`, not this one) end to end and either backs
the "about a minute plus an unmeasured torch pull" line with a number, or
replaces it with one that contradicts it — per CLAUDE.md's own rule, a claim
that survives uncounted is the thing to fix, not the file that flags it.

Second, smaller recommendation, **trial**: since `present()` already does
exact-version checks rather than mere existence checks for several
components, the same rigor could extend to `qmd-models`'s check, which
currently shells out to a second script rather than checking a size or count
directly (install.sh:79) — worth doing if `setup_qmd.sh --check`'s own cost
(unmeasured here, out of scope for this row) ever shows up as the slow line in
a `--check` run. **Evidence**: `--check`'s own 8.4s total already spends a
visible fraction of its wall time on the one component whose presence check is
not a plain import; nothing here quantifies how much. **May not**: this
recommendation is not itself a measurement — it names what to measure next,
not a result.
