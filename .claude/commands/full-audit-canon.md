---
description: >-
  Run a full canon audit cycle for Kohärenz Protokoll — scope → scan → triage →
  fix → verify. Orchestrates the worldbuilder-physicist (DKT consistency) and
  worldbuilder-editor (R-rules, Sprach-DNA, locked spellings) agents.
  Usage: /full-audit-canon [scope: physics | canon | continuity | storyform | full]
argument-hint: "[physics | canon | continuity | storyform | full]"
---

# Full Audit Canon — Complete Audit Cycle

You are orchestrating a full canon audit. Follow this sequence exactly.
Do not skip steps or combine phases.

## Step 1: Scope Selection

If the user specified a scope, use it. Otherwise ask (AskUserQuestion):
- `physics` — DKT consistency: Coheron/Erason atemporality, Landauer/ozone
  signature, persistence equation, K₀/K₁ inversion, across Canon + chapter prose
- `canon` — locked spellings, frontmatter/status enum, R-1…R-10, Act-I fences,
  Sprach-DNA hard rules, cross-references
- `continuity` — cross-chapter proper nouns, POV signature per chapter,
  knowledge fences, Türschloss-style micro-continuity from the enrichment packets
- `storyform` — NCP A/B vs Canon storyform vs prose (ncp-author drift checks,
  `novel_coherence_check`, `validate_appreciations`)
- `full` — all four (split across sessions, physics first)

Prioritise by churn:
```bash
git log --since="30 days ago" --name-only --pretty=format: | grep "\.md$" | sort | uniq -c | sort -rn | head -20
```

## Step 2: Load Audit References

- **physics:** `Canon/…begriffe-und-konzepte…` §1–§2 and §14, `Codex/WORLD-AXIOMS.md`,
  `auditing-physics/references/`
- **canon:** `WRITING.md`, `Plan/drafting/drafting-brief.md` §2–§4,
  `Canon/…welt-sensorik…` §10 + §12, `auditing-canon/references/`
- **continuity:** `Plan/drafting/enrichment-packets_*.md`, `chapter-information-expanded`,
  `coherence-pass_01-05`
- **storyform:** `.claude/skills/ncp-author/SKILL.md`, `dramatica-vocabulary`
- **Chain of Draft mode:** compress each reasoning step to ≤5 words, mark
  conclusions with ####:
  ```
  Kap 7 body. "AEGIS" found. Akt I. #### VIOLATION: Drafting-Brief §3.
  ```

## Step 3: Scan (present scope for approval first)

List the files to be scanned. Wait for author approval before starting.

Deterministic first — they are free and never wrong on what they check:
```bash
python3 scripts/lint_chapter.py                      # canon scope
python3 scripts/render_codex_views.py --check        # all scopes
python3 scripts/check_enrichment.py --base <rev>     # continuity, after enrichment passes
```
Graph transforms next: `check_continuity(novel_id)`, `check_pov_consistency(novel_id)`,
`find_axiom_contradictions(world_id)` per World, `check_voice_consistency(bodies)`.

Then invoke `@worldbuilder-physicist` for physics scope, `@worldbuilder-editor`
for canon/continuity scope, and the ncp-author skill for storyform scope.

Each agent:
- Reads only the reference files it needs (not the whole Canon)
- Reports findings in pinned format with exact file and line
- Applies the metascience filters (see /canon-rules)
- Does NOT fix anything during the scan

## Step 4: Triage

Present findings grouped by severity (Canon §10.2 mapping in brackets):

- **CONTRADICTION** — two sources disagree on a rule, fact or timeline [Kritisch]
- **VIOLATION** — R-rule, locked spelling, Act-I fence or Sprach-DNA rule broken [Kritisch/Mittel]
- **DRIFT** — terminology inconsistency, superseded name [Mittel]
- **BROKEN-REF** — link or slug to nonexistent file/entry [Niedrig]
- **META** — narrator telling, explained irony (R-1/R-2) [Kritisch]
- **GAP** — `[L]` that a downstream chapter now depends on [Mittel]

Author decides: fix now, defer (as a decision-log entry), or reject.

## Step 5: Fix (one severity batch at a time)

For approved findings:
- Physics contradictions → `@worldbuilder-physicist` proposes; author applies to Canon
- Prose/naming violations → `@worldbuilder-editor` (minimal edit; enrichment
  discipline: insert, never rewrite existing paragraphs — verify with `check_enrichment.py`)
- Storyform drift → ncp-author workflow only

Each fix: targets only the approved finding · minimal change · `/verifying-completion`
after · diff presented before commit. Maximum 2 attempts per finding; then defer and flag.

## Step 6: Verify and Close

- Re-run the deterministic checks from Step 3
- `/cross-checking` on any term renamed or corrected; `update_codex_entry` +
  re-render `Codex/` if a definition changed
- Record: `record_storyform_decision` for structural outcomes, decision-log entry
  (D-xx) for drafting outcomes, `reflect_note` for lessons
- Append to `Plan/sessions/<YYYY-MM-DD>-learnings.md`:
  `[YYYY-MM-DD] AUDIT (<scope>): N scanned, N fixed, N deferred, N rejected`

## Rules

- Never skip scope approval (Step 3) or verification (Step 6)
- Findings without an exact file + line reference are rejected
- Storyform A ≠ Storyform B is design, not contradiction; Kernwelt logic regimes differ by design
- Demand the mechanism: "File A contradicts File B because [specific rule/lock]"
- One severity batch at a time — never mix criticals and moderates
- German prose stays German; never "fix" the two documented heterodox rows of Storyform B
