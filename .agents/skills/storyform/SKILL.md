---
name: storyform
description: >-
  Develop and review Kohärenz Protokoll's dual Dramatica plot against the current
  author-decided storyforms. Use before storyform, throughline, signpost, casting,
  plot or NCP work, when comparing chapter variants, or when storyform.py fails.
  Protect approved structural values, translate them into causal chapter proposals,
  distinguish canon from drafts, record evidence and open choices, then regenerate
  the local NCP 3 document. Never silently decide a storypoint or rewrite prose.
---

# Develop the plot from the storyforms

Read `NOW.md`, `CLAUDE.md` and `PRINCIPLES.md`. Follow the newest instruction and
coordinate with the session board and open PRs before selecting work. Use the
repository's existing initializer; delegated agents check it, never rebuild
shared reading views.

## Read the authority, then the chapter

| Input | Authority and use |
|---|---|
| `Plan/storyform/a.json`, `b.json` | Approved structural values and their provenance. A is Kael's healing, B AEGIS' collapse, under the shared premise (decision 025). |
| `Plan/decisions/025-dramatica-is-the-recipe.md` | Read the relevant numbered steps and subsequent corrections; a later correction wins. |
| `Plan/storyform/weave.json` | The chapter routes, throughlines, act/world bands and driver transitions. |
| `Plan/storyform/anteile.json` | The working basis for alters' appearances and channels; not permission to declare draft manifestations canon. |
| `Manuscript/kanon.md` | Explicitly decided content. Trace rows to the author's decision; drafts and Wiki readings cannot supply new canon. |
| `Plan/storyform/development.json` | Proposal-only chapter development, separate from the approved scaffold; inspect its schema before updating. |
| `Plan/storyform/overview.md`, `ncp/kohaerenz-protokoll.ncp.json` | Generated views. Never edit them by hand. |
| Chapter drafts, scene lists and `Plan/weichen/` | Evidence, working bases and open options. Selection or a recommendation alone is not canon (step 38). |
| `Wiki/chapters/`, `Wiki/conflicts/`, `Wiki/questions/`, source lines | Research and competing readings; retrieve only what the chapter question needs. |

Load the relevant sections rather than the whole corpus. For the theory, use the
available `dramatica-theory` skill and the local chart. The engine's reconstructed
rules and limits are in `Plan/runs/storyform-2026-10-02/engine-rules.md` and
`validation.md`. Signpost choices belong to the author; their ordering function
is licensed and unpublished. The older `ncp-author` skill targets NCP 1.3 and is
not this project's generator or NCP 3 authority; read `ncp3-delta.md` instead.

## Use the local tools

```bash
python3 scripts/storyform.py --check    # check structure and generated-file freshness
python3 scripts/dramatica.py under Memory
python3 scripts/dramatica.py where Inertia
python3 scripts/dramatica.py derive twelve.json  # actual twelve-answer input file
python3 scripts/storyform.py            # regenerate overview and the NCP 3 document
python3 scripts/check_skills.py         # after a repository skill changes
```

- **ERROR:** distinguish a malformed input, missing provenance or illegal chart
  combination from a stale generated file. Fix only the defect actually reported;
  do not alter an author's structural answer to make a check green.
- **note:** a value disagrees with the reconstructed derivation. Record both and
  their consequences as a question; a note is neither an author decision nor an
  official DSM ruling.
- Use the author's NCP 3 fork's `node tests/validate-file.js <file>` when installed;
  name whether that schema check ran. A successful generator check does not prove
  scene quality or acceptance of a proposal.

## Develop a chapter without changing the storyform

1. **Freeze the structural contract.** Name chapter, act, world, route, A/B
   throughlines and signposts from `weave.json`; identify its relevant plot story
   points and next approved driver transition. Cite the inputs. Do not claim every
   scene must embody every throughline, or treat a signpost label as a scene.
2. **Read the complete variants.** Enumerate chapter files with `rg --files` and
   read each prose draft in full, separately from README recommendations. For Kap 1,
   the current A–I set must all be accounted for; re-enumerate on every new review.
   Cite exact file lines obtained from `nl -ba` or `rg -n`, and label whether each
   fact is decided, draft-only, inferred or missing. Prefer no variant by recency.
3. **Test the dramatic argument.** Distinguish overall conflict (OS), personal
   difficulty (MC), pressure to reconsider (IC) and the relationship's evolution
   (RS). For both A and B, state who wants what, what resists it, and how a choice
   or action changes the next available options. Keep B's own pursuit and costs
   visible; AEGIS is a protagonist in B, not merely an obstacle in A.
4. **Test execution separately.** Use `scene-architecture`'s planning/review mode
   for goal, opposition, action, turn, cost and therefore/but seam. Track what Kael,
   AEGIS, other figures and the reader know before/after. A trace of Juna and Juna's
   direct presence are different; do not erase the approved first present encounter.
5. **Propose concrete improvements.** Each recommendation names the observed
   weakness, a scene/beat operation, its gain, cost, structural compatibility and
   unresolved choice. Prefer consequences of existing mechanics and competing
   wants to extra terminology or an unsupported new world rule. Show why a scene
   becomes harder or a later choice changes, not merely why lore becomes larger.
6. **Record, regenerate, verify.** Put review findings in
   `Plan/runs/writing/<target>/storyform-review_<YYYY-MM-DD>.md`. When updating chapter
   proposals, use `development.json`'s current schema and retain proposal status,
   chapter id, source references and open choices. Include goal, opposition, action,
   turn, cost, knowledge, reader information, next consequence, timing and storypoint
   grounding. Run the generator and `--check`; inspect the generated NCP diff for
   references, settings, provenance and the proposal status. A generated event or
   moment does not make proposed content approved.

## Avoid false structural diagnoses

- **Change is the overall resolve**, not a ban on an early refusal, insight or
  experiment. Compare the character's problem-solving pattern across the whole
  arc and the decisive pivot; show a causal contradiction before flagging one.
- **Be-er describes the preferred approach to personal problems**, not a ban on
  bodily action or an external task. Action can test an internal coping strategy.
- **Optionlock is the overall finite-options limit**, not a ban on a local clock.
  A deadline becomes a structural issue only if it replaces the approved limit.
- **Decision/Action drivers name what forces major turns**, not every act of
  choosing or moving. Preserve both halves of the approved A/B transitions.
- **An IC is a perspective that pressures the MC**, not a required present-tense
  conversation in every IC chapter. Ground any remembered or trace-based pressure
  in what the chapter actually shows; do not invent Juna's intent from Kael's view.
- **Guardian archetype and Guardians of the world are distinct.** Keep Help/
  Conscience separate from the five named world figures and their assigned B roles.
- **A designed crack is not automatically an error.** Distinguish reader uncertainty
  from a continuity defect that breaks an explicit decision. Preserve uncertainty
  while making the action, consequence and needed reader information legible.

## Change an approved value only on an answer

Search the existing decisions and relevant sources first. If the author requests
an interactive structural choice, present one question with alternatives, each
with its consequences for scenes, acts and both storyforms; recommend explicitly.
Otherwise note the unresolved choice and continue independent review and proposal
work, as `NOW.md` instructs. Do not turn a request for plot improvement into approval
of a particular new storypoint.

Once the author answers, record the value and precise provenance in the source
JSON, append the decision's numbered step (or a new decision for a reversal), and
regenerate. Review the impact on weave, appearances, chapter proposals and NCP;
refresh the handover. Preserve author-decided A/B values until then. Follow the
repository's commit and pre-PR `app-refresh` procedure after checks pass.

## Limits

Do not write, rewrite or continue manuscript prose in this workflow. Do not send
corpus text to a third party or to the Dramatica platform without authorization.
Do not promote a source's claim, a model inference, a selected variant, a provisional
want or a chapter proposal to canon. Record what would settle it and continue.

## Provisional

```yaml
name: storyform
# may not: decide author values, compute licensed signposts, claim official DSM validation,
#          or make generated chapter development canon
# retire when: treatment checks show this workflow adds nothing, or the author drops Dramatica
```
