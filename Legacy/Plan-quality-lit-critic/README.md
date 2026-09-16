# lit-critic reports

`scripts/lit_critic_gate.py` writes one report per chapter here:

- `kap-NN.md` — the readable report: every finding with severity, lens, the
  chapter file and line it points at, its evidence, its impact and its options.
- `kap-NN.json` — the same findings machine-readable, for diffing runs.

Each run overwrites its chapter's report, so git history shows how a chapter's
editorial state moved between passes. Reports are committed on purpose: they are
the evidence that a chapter passed its prose gate before advancing.

A report is **not** canon and not a to-do list. Findings are proposals — see
`.claude/skills/lit-critic/SKILL.md` for how to triage, accept or reject them.
