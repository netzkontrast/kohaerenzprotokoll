# `Plan/storyform/` — the novel's two Dramatica storyforms

The plot's structure, as the author decided it step by step (decision 024). Start with **`overview.md`**.

| file | what | who writes it |
|---|---|---|
| `a.json`, `b.json` | the source of truth: classes, dynamics, the four throughlines, plot story points, signposts, casting, open points, the work-language texts for NCP, and a `provenance` entry for every value | the author's answers, recorded by a session |
| `overview.md` | everything above on one page, plus where it disagrees with the engine derivation | `scripts/storyform.py` — never by hand |
| `ncp/storyform-a.ncp.json`, `ncp/storyform-b.ncp.json` | the same as NCP 1.3.0 (`draft`) | `scripts/storyform.py` — never by hand |

How to change anything: the `storyform` skill (`.agents/skills/storyform/SKILL.md`). The history — the session
that built this, the engine rules, the source search for signposts, the validation — is in
`Plan/runs/storyform-2026-10-02/`.
