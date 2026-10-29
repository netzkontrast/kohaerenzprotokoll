# AEGIS pilot — the two manual cases, run offline (2026-10-26)

Status: **proposal** evidence for `Plan/briefings/aegis-agent-pilot.md`. No model
was called, no network was used, nothing under `Manuscript/`, `Wiki/` or
`Sources/` changed. The scenarios are `Plan/fixtures/aegis/case-01-sweep.json`
and `case-02-rejected.json`; their README states every pilot assumption by id.

The commands, as actually run from the repository root:

```
python3 scripts/aegis.py run    Plan/fixtures/aegis/case-01-sweep.json    --out Plan/runs/aegis-pilot-2026-10-26/case-01   > case-01.run.json
python3 scripts/aegis.py run    Plan/fixtures/aegis/case-02-rejected.json --out Plan/runs/aegis-pilot-2026-10-26/case-02   > case-02.run.json
python3 scripts/aegis.py replay Plan/runs/aegis-pilot-2026-10-26/case-01                                                  > case-01.replay.json
python3 scripts/aegis.py replay Plan/runs/aegis-pilot-2026-10-26/case-02                                                  > case-02.replay.json
python3 scripts/aegis.py status Plan/runs/aegis-pilot-2026-10-26/case-01                                                  > case-01.status.json
python3 scripts/aegis.py fork   Plan/runs/aegis-pilot-2026-10-26/case-01 Plan/runs/aegis-pilot-2026-10-26/case-01-fork --upto 1 > case-01.fork.json
python3 scripts/aegis.py pack   Plan/fixtures/aegis/case-01-sweep.json kael                                               > case-01.pack-kael.json
python3 scripts/aegis.py selftest
```

What the files show:

| file | result |
|---|---|
| `case-01.run.json` | `c1-a1` (AEGIS sweep) accepted, `c1-a2` (Kael's report) accepted, the repeated `c1-a1` a duplicate: reserve 64 → 57, `M1` masked, `X1` closed, one claim Kael → AEGIS; `status: held` against `expected` |
| `case-02.run.json` | seven proposals refused in the validator's order (`missing_observation` ×2, `insufficient_reserve`, `stale_version`, `action_not_allowed_for_actor`, `action_not_registered`, `past_endpoint`); state and reserve unchanged |
| `case-0N.replay.json` | the state derived from `events.jsonl` alone equals `final.json`; `model_calls: 0` |
| `case-01.status.json` | both figures active in Kap 6; AEGIS holds one pending claim |
| `case-01.fork.json` | a fork with the first event only; `case-01/` unchanged (its `meta.json` sha256 pins the scenario) |
| `case-01.pack-kael.json` | Kael's view before the run: one fact, no reserve, no memories, `omitted: {facts: 2, author_only: 2, …}` — the omissions counted, their content absent |

`grep -r PROBE-AUTHOR-ONLY` over this directory finds the marker only inside
the pinned `scenario.json` copies, which are the author's input, never a pack or
a tool response. `python3 scripts/aegis.py selftest` repeats every assertion of
the briefing's acceptance list on a temporary copy (41 lines, each able to fail).

**Regenerated 2026-10-27** with the commands above, after the review of PR #198: facts now name their `subject`,
the fixtures are schema 2, and the validator refuses an unrelated observation, a backdated chapter, a missing or
unknown target and a malformed proposal; a pack shows a masked memory by its id alone. The two cases' outcomes are
unchanged. A second pass the same day followed the spec panel's review (`spec-review_2026-10-27.md`, answered in
`Plan/concept/aegis-loop-spec_2026-10-27.md`): a report's claim text now travels in `claim`, apart from its
literary `reason` and `log`; a proposal carrying the probe marker is refused; a commit halts when the pinned scenario
changed; a closed anomaly is not swept again; a run is refused a directory under the canon folders. A run pinned to schema 1 is refused by `replay` by name; git holds the earlier run (`git log -- Plan/runs/aegis-pilot-2026-10-26`).

Each `case-*/` holds: `scenario.json` (pinned), `meta.json` (scenario sha256,
responses sha256, git revision at run time), `events.jsonl` (accepted events,
append-only, one effect list per event), `rejections.jsonl`, `logs.jsonl` (the
proposals' literary lines, separate from the events), `final.json` (a recorded
snapshot the replay compares against; disposable).

What this run does **not** show: a live model, a voice, a playable scene, any
canon. The next extension, per the briefing, is one serial recorded model call
replacing the frozen `responses` list — only with a provider and input scope that
already has the author's permission.
