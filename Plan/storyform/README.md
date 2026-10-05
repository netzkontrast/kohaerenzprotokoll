# `Plan/storyform/` — the novel's two Dramatica storyforms

The plot's structure, as the author decided it step by step (decision 025). Start with **`overview.md`**.

| file | what | who writes it |
|---|---|---|
| `a.json`, `b.json` | the source of truth: classes, dynamics, the four throughlines, plot story points, signposts, casting, open points, the work-language texts for NCP, and a `provenance` entry for every value | the author's answers, recorded by a session |
| `anteile.json` | when, how and where Kael's alters show: the thirteen parts, the three channels (body, syntax, trace; a name only from Kap 13), the camps of the Juna arc and the appearances by chapter, checked by `storyform.py` against the weave and the canon (decision 025 step 32) | the author's working basis of 2026-10-05, from the session's proposal |
| `weave.json` | the storyweaving scaffold: every chapter 0–40 with its route (hard-a, hard-b, bridge and its anchor) and the throughlines of A and B it carries, checked by `storyform.py` (decision 025 step 23) | the author's answers, recorded by a session |
| `overview.md` | everything above on one page, plus where it disagrees with the engine derivation | `scripts/storyform.py` — never by hand |
| `ncp/kohaerenz-protokoll.ncp.json` | the same as one NCP 3.0.0-rc.1 document (decision 025 step 24): the core envelope; in the `dramatica:` payload one story with both narratives (players, logline and genre overviews) and the 41 chapters as story moments that reference both. Validate with the author's fork, `netzkontrast/narrative-context-protocol`: `node tests/validate-file.js <file>`; the `ncp-author` skill's validator knows only 1.3.0 | `scripts/storyform.py` — never by hand |

How to change anything: the `storyform` skill (`.agents/skills/storyform/SKILL.md`). The history — the session
that built this, the engine rules, the source search for signposts, the validation — is in
`Plan/runs/storyform-2026-10-02/`.
