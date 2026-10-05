# Deletion chain — session claim

Session: deletion-chain-1-13

The author's go of 2026-10-06 authorizes a comparison of the three proposed
deletion targets for chapters 1/12/13 and concrete consequences of 06:10 for
chapter 2. This session produces a decision-ready planning proposal; it does
not select a manuscript draft or change canon or either storyform.

## Plan

1. Read the current structural decisions, relevant chapter proposals, scene
   lists, knowledge table and complete chapter-1 variants.
2. Compare the three explanations with chapter-level actions, information,
   costs and continuity requirements; recommend explicitly, retain alternatives.
3. Record the comparison under `Plan/runs/writing/book/`, link it from the
   existing plot-development handover and regenerate only if proposals change.
4. Verify storyform freshness, pipeline order and the required app refresh;
   report editorial and publishing limitations separately from check results.

## Coordination

The session board showed no open claim for this task. The active
`claude/q8-clock-weave-check` branch develops Akt III/Vortex; this session owns
only the deletion alternatives and chapter-2 consequences. Shared generated
storyform files are left to their existing owner unless a merge is necessary.

## Completion

The German comparison is
`Plan/runs/writing/book/scene-architecture_loeschziele_2026-10-06.md`:
all nine complete opening drafts, three deletion explanations, three ways to
enforce 06:10, a recommended chapter-2 beat and a knowledge/consequence chain
through chapter 13. It separates operative linkage from Q7's open identity
question, and identifies the bank's repeated deletion and the already-confirmed
entry as execution questions. No alternative was selected.

The existing plot-development report, NOW.md and the author's question list
link the decision-ready comparison. `development.json`, the generated NCP,
approved storyform inputs, canon and manuscript prose are unchanged.

## Verification and limitations

`storyform.py --check` passed; `account.py order --summary` reported no
violations. The claim's app build reported zero defects; web and stamp checks
passed for tree `89cb98d624af52bc0fd04538f86c9ec6f74bcede`.
The final committed tree is rebuilt and checked before the PR is made ready;
its stamp, invariant/selftest results and GitHub status belong in the PR body.

The reader initializer refreshed the graph but could not install qmd; this
comparison uses direct file reads, with no qmd search or model call. App checks
do not establish literary quality. No blind-reader simulation was performed.
Wide/narrow browser inspection remains unverified: the browser explicitly
denied the local preview earlier; the hosted site requires authentication.
No Artifact tool is available, so the private canvas was not published.
The Vercel deployment/preview status is reported in the PR, not inferred from
a successful local build.
