# `Plan/storyform/` — the novel's two Dramatica storyforms

The plot's structure, as the author decided it step by step (decision 025). Start with **`overview.md`**.

| file | what | who writes it |
|---|---|---|
| `a.json`, `b.json` | the source of truth: classes, dynamics, the four throughlines, plot story points, signposts, casting, open points, the work-language texts for NCP, and a `provenance` entry for every value | the author's answers, recorded by a session |
| `weave.json` | the storyweaving scaffold: every chapter 0–40 with its route (hard-a, hard-b, bridge and its anchor) and the throughlines of A and B it carries, checked by `storyform.py` (decision 025 step 23) | the author's answers, recorded by a session |
| `overview.md` | everything above on one page, plus where it disagrees with the engine derivation | `scripts/storyform.py` — never by hand |
| `ncp/storyform-a.ncp.json`, `ncp/storyform-b.ncp.json` | the same as NCP 1.3.0 (`draft`), with the players, the logline and genre overviews, and one moment per woven chapter | `scripts/storyform.py` — never by hand |

How to change anything: the `storyform` skill (`.agents/skills/storyform/SKILL.md`). The history — the session
that built this, the engine rules, the source search for signposts, the validation — is in
`Plan/runs/storyform-2026-10-02/`.
