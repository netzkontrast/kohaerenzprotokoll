# Chapter evidence pilot — Kap 2, 2026-09-25

**Scope:** read-only comparison of one existing draft with its chapter plan, the
newly read proposal and the NCP. This is a trial of a chapter as a retrieval
unit; it creates no chapter node, alters no prose or NCP, and promotes no `[V]`
claim to canon.

## Inputs and authority

| Source | What it can establish here |
|---|---|
| [`Legacy/…/chapters/02-der-erste-riss.md`](../../Legacy/Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/chapters/02-der-erste-riss.md) | The current chapter text, including its own outline and draft v0.2; read-only. |
| [`Legacy/Plan/drafting/chapter-information-expanded_2026-09-11.md`](../../Legacy/Plan/drafting/chapter-information-expanded_2026-09-11.md) | A dated plan for the draft, not proof of what prose does. |
| [`Sources/drive/kp-plot-konkretisierung-13-ideen-f1-faden-2026-06-10-md.md`](../../Sources/drive/kp-plot-konkretisierung-13-ideen-f1-faden-2026-06-10-md.md) | An earlier plot proposal, explicitly `[V]` (L17, L108, L291). |
| [`Legacy/…/ncp.json`](../../Legacy/Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/ncp.json) | Storyform A's global slots; `scenes`, `storybeats`, and `moments` are empty (L12–L14). |

## Claims answered by this chapter

| Question | Evidence in the draft | Proposal / plan | Result |
|---|---|---|---|
| Does the corrected value return as an actionable event? | Chapter lines 105–145 put sequence 114 back at the same decimal position; Kael marks it, checks the empty prior-event field and confirms it. | F1 L229 proposes a returning value in Kap 2; the plan L40–L41 asks for the same causal test. | **Present in prose.** Do not draft a second return scene. |
| Is a local spatial Riss shown without explanation? | Lines 239–315 compare 204 light fields with 211 floor plates, show the viewpoint-dependent wall and a console response that denies an anomaly. | Plan L43 sets 211 versus 204 and cold ozone; F1 L229 sets the return and a foreign draft but does not prescribe this spatial test. | **Present in prose**, and more specific than F1. The geometric disagreement is a scene fact, not a fault to normalise. |
| Does the chapter prepare Lex without naming him? | Lines 343–379 place a conditional, syntactically foreign sentence beside the official closed record; the prose never identifies its writer. | Plan L41, L44 and F1 L229 propose a foreign syntax. | **Present in prose.** The identity remains an interpretation, not a statement by Kael. |
| Does the draft establish that every work deviation is a K₁ trace? | The chapter shows a repeated value and a spatial anomaly; it does not state their ontology. | F1 L116 proposes the equation, then labels it an author decision at L251 and L262. | **Open.** Store the proposal as a question, never infer it from the scene. |
| Which NCP constraint is checkable here? | The draft's first-person Kael narration and incompatible console/report positions are visible at lines 105–145 and 369–379. | NCP L20–L41 gives MC `Memory`, `Falsehood vs. Truth`, Avoidance → Pursuit. | A **thematic fit** can be observed; the NCP has no chapter-level beat or scene ID to validate Kap 2 mechanically. |

## What the pilot changes about the next implementation

The smallest useful chapter record is a **read-only index** with a stable chapter
path, draft status, cited event spans, the corresponding dated proposal and plan,
and explicit `observed` / `proposed` / `open` labels. A source date or `[K]` tag
inside a proposal cannot change an observed scene. The index should link to the
NCP's global slots while saying that no NCP scene mapping exists; it must not
invent scene IDs. This one example establishes the fields before a schema or
new page type is introduced.

The immediate editorial consequence is concrete: Kap 2 already contains the
returning value, spatial discrepancy and foreign draft. The remaining decision
is F1-1, whether those work deviations are *necessarily* K₁ traces. Resolve
that before encoding F1 in later chapters; no change to Kap 2 follows from this
pilot alone.
