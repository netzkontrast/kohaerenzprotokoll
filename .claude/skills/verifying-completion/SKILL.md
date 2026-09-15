---
name: verifying-completion
description: >-
  Runs a mandatory completion checklist before declaring any worldbuilding task
  finished. Catches missing frontmatter, broken cross-references, unlinked glossary
  terms, and deferral language. Use after writing any content, before reporting task
  complete, or when user says "is this done", "verify", "check my work", or
  "completion check". Does NOT write content — only verifies.
model: sonnet
effort: medium
---

# Verifying Completion

Mandatory checklist before declaring ANY worldbuilding task complete.

## Checklist

For EVERY file created or modified:

1. **Deterministic checks pass** —
   `python3 scripts/lint_chapter.py <chapter>` (exit 0),
   `python3 scripts/check_enrichment.py --base <rev>` after any enrichment pass,
   `python3 scripts/render_codex_views.py --check` after any graph write
2. **Frontmatter** — chapter files: `type: novel.chapter`, `status` in the enum,
   template header untouched except `status`/`pov`; Plan/ syntheses: title, tags, status
3. **Content** — no TODO / TBD / "wird später ergänzt"; gaps are `[L]` with an
   owner, not silence; no empty sections
4. **Cross-References** — links resolve; every new term has a codex entry
   (`Codex/GLOSSARY.md`) with triggers; dated facts are StoryTimeEvents
5. **Canon Consistency** — obeys `Codex/WORLD-AXIOMS.md`, locks (Canon welt-sensorik
   §12), knowledge fences (`what_does_X_know_as_of`); nothing dekanonisiert revived
6. **Writing Standards** — `WRITING.md` tokens: German prose, act-specific forbidden
   terms, R-1…R-10, Sprach-DNA hard rules, word count within plan ±15 %
7. **Decisions recorded** — every deviation from plan/canon has a decision-log
   entry (D-xx) or `record_storyform_decision`; lesson captured via `reflect_note`
8. **Self-review checklist** — Canon welt-sensorik §10.3 walked per scene; Chapter
   Readiness Gate (enrichment masterplan) for drafted chapters
9. **Status flips** — before `drafted → revised → final`, the lit-critic gate has run
   (`python3 scripts/lit_critic_gate.py --chapter N`, skill `lit-critic`) and no
   `critical` finding is open

## Red Flags — DO NOT Declare Complete If:

- `lint_chapter.py` reports a VIOLATION
- Any section heading has no content below it
- Any cross-reference doesn't resolve
- A new term was introduced but has no codex entry
- Canon/ or ncp*.json was changed without an explicit author decision
- The graph was written but `Codex/` was not re-rendered

## Out of Scope

Does NOT write content. Does NOT audit the full repo.
