---
name: storyform
description: Work on the novel's plot structure — the two Dramatica storyforms A (Kael) and B (AEGIS) in Plan/storyform/ — reading them, putting a structural question to the author one step at a time with its consequences, recording the answer with its provenance, and regenerating the overview and NCP files. Use before any Dramatica, storyform, signpost, throughline, plot-story-point, archetype or casting work on the novel, before changing a.json or b.json, when a session needs to know what the plot's structure is, and when a check names storyform.py.
---

# The storyforms

The novel runs on two complete Dramatica storyforms (decision 025): **A**, Kael's healing (Triumph), and
**B**, AEGIS' collapse (Tragedy), under one premise — *„Vielheit ist keine Störung der Ordnung, sondern ihre
Bedingung."* W1 made Dramatica the recipe: the treatment is written from them, then checked against them.

## Read first

| what | where |
|---|---|
| the current state, in one page | `Plan/storyform/overview.md` (generated) |
| the source of truth, every value with its provenance | `Plan/storyform/a.json`, `b.json` |
| the storyweaving scaffold: each chapter's route and the throughlines it carries | `Plan/storyform/weave.json` (step 23) |
| when and how the alters show, by chapter and channel, and the camps of the Juna arc | `Plan/storyform/anteile.json` (step 32) |
| why each value is what it is, step by step | `Plan/decisions/025-dramatica-is-the-recipe.md` |
| the engine rules and their limits; what the sources say about signposts; the validation | `Plan/runs/storyform-2026-10-02/` — `engine-rules.md`, `signposts-in-sources.md`, `validation.md` |
| the open decision sheets for the novel | `Plan/weichen/` (W10 casting, WP plot points, …) |

Dramatica theory itself: the `dramatica-theory` skill (Anthropic skills); NCP fields: the `ncp-author` skill (it knows 1.3.0; the file is 3.0.0-rc.1 since step 24 — `Plan/runs/storyform-2026-10-02/ncp3-delta.md` has the difference and the validator).

## The tools, and how to read them

```bash
python3 scripts/storyform.py            # check, compare with the derivation, write overview.md and ncp/
python3 scripts/storyform.py --check    # what CI runs: refused, or stale files
python3 scripts/dramatica.py under Memory          # the variations and element quads of a type
python3 scripts/dramatica.py where Inertia         # where an element or variation sits, and its pair
python3 scripts/dramatica.py derive twelve.json    # what the engine fixes from the twelve answers
```

- **`ERROR`** — the storyform is refused and nothing is written: a value breaks the chart (R1–R8), or a value
  has no provenance. Fix the JSON.
- **`note`** — the stated value differs from what the reverse-engineered engine rules (D1–D7) derive. **That is a
  question for the author, never a silent fix**: present both, with what each means for the plot.
- **Two Guardians.** The Dramatica archetype is the *Guardian-Archetyp*; the novel's five Guardians (LogOS, Mnemosyne,
  Cerberus, Kairos, Sophia) are characters of the world. Never write one for the other.
- **What no tool can give:** the signpost order (licensed Dramatica intelligence, not published), B's IC problem,
  and every meaning. Those are the author's — chosen after searching the sources (`qmd`, `grep`, `read.py --find`).

## Changing a value

1. **Search first.** Before proposing a value the sources may already hold, look (`signposts-in-sources.md` shows
   how): the author asked for it, and two sources agreeing is the strongest proposal there is.
2. **Ask one question at a time** with `AskUserQuestion`. Each option says what it means for the plot (scenes,
   acts, who acts), the recommended one first; a preview shows the resulting chain. Never batch a decision into a
   recommendation the author did not see.
3. **Record** the answer in the JSON: the value, its `provenance` entry (`author, <date>, <what>` / `derived D… ` /
   `source <slug>`), and the work-language texts the NCP needs. Then run `storyform.py`.
4. **Write it down** in decision 025 (a new numbered step), or a new decision when an answer reverses an earlier one,
   and refresh the storyform line of `NOW.md`.
5. **Commit** naming the change; a revised Wiki page (a conflict a decision settles, like C8) gets its own commit.

## What this skill does not do

It does not decide for the author, write or rewrite prose (canon prose is the author's, `Manuscript/`), let a
derivation overwrite an author's answer without asking, edit `overview.md` or `ncp/` by hand, or send anything to
the Dramatica platform — the author chose to work without it (2026-10-05).

## Provisional

```yaml
name: storyform          # provisional
# may not: present a derived value as the author's, compute a signpost, or treat D1–D7 as official
# retire when: the treatment exists and the storyforms are checked against it (W1's B), or the author drops Dramatica
```
