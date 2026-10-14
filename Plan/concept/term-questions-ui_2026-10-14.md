# Term questions and the authoring interface

Author request, 2026-10-14: 100 additional reading questions for each wiki term, including cross-term questions; reconsider the complete UI and make promoted terms visible.

Implementation targets:
- `Wiki/questions/reading/`: one checked, stable question bank per term. Reading prompts are proposals with an unchecked answer status, not new unresolved canon conflicts.
- `scripts/reading_questions.py`: coverage, identity, source anchors, relationships and offline refusal fixtures.
- `scripts/ui.py`, `scripts/ui.js`, `scripts/ui.html`: question workshop with search, term/category filters, pagination, deep links, local notes and export; separate term pages, reviewed ledgers and candidates; a promotion dossier and direct reading-to-question actions.
- `agents/`: the same question identities, paths and addresses available to tools.

Verification: exact per-term counts, valid anchors and unique IDs/texts, UI route roundtrips, filter and storage behavior, repository checks, desktop/mobile inspection. Promotion and canon remain the author's decisions.

The current Vercel URL is a deployment snapshot. This branch receives its own preview on push; a merge is needed to update production.
