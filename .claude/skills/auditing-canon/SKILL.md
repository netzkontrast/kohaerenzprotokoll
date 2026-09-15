---
name: auditing-canon
description: >-
  Verifies canon status, naming compliance, frontmatter completeness, writing
  standards, and cross-reference validity across worldbuilding files. Use when
  checking naming consistency, verifying frontmatter, auditing prose standards,
  or when user says "canon audit", "check names", "verify frontmatter", "writing
  standards check", or "naming audit". Does NOT check physics equations — use
  /auditing-physics for that.
model: sonnet
effort: high
---

# Auditing Canon

Verify naming, frontmatter, writing standards, and cross-references.

## Prerequisites

Read CLAUDE.md, `WRITING.md` (locked spellings, forbidden terms per act, file
format) and `Plan/drafting/drafting-brief.md` §3–§4. Run the deterministic
lint first — it covers frontmatter, status enum, Act-I fences, voice labels,
R-5 and R-9 exactly, and never produces a finding without file + line:

```bash
python3 scripts/lint_chapter.py            # all chapters (exit 1 on violation)
python3 scripts/render_codex_views.py --check
```

## Chain of Draft Mode

```
Name check. Human term found. Science dir. #### VIOLATION.
Frontmatter. status field missing. #### VIOLATION.
Spelling. Variant found. #### VIOLATION: use canonical form.
Cross-ref. Link resolves. #### PASS.
```

## Checks

### Naming
1. Diegetic vocabulary in Act I (Konsolidierung, Ausgleich, Abweichung,
   Wartungsfenster, Bestand, Restwert, Ausnahme); no DKT terms; AEGIS name absent
2. Locked spellings match `WRITING.md` → `locked-spellings`
3. Nothing from the dekanonisiert list appears as an active figure

### Frontmatter (chapter files)
4. YAML frontmatter with `type: novel.chapter`, `chapter_number`, `title`, `pov`, `status`
5. `status` ∈ {outlined, drafted, revised, final}; template header unchanged
   except `status`/`pov`; draft-provenance comment present (`<!-- Draft … -->`)

### Writing Standards (chapter prose)
6. R-1…R-10 (Canon welt-sensorik §10.1) — semantic ones by reading, not grep
7. Sprach-DNA hard rules (§12.7); voices never labeled
8. Genre mode per act (§11) not leaking; word count within plan ±15 %
9. Direktiven bold VERSALIEN, logs in code blocks with D-03 fields only

### Cross-References
10. Plan/Canon links resolve; new terms have a codex entry (`Codex/GLOSSARY.md`)
11. Deviations from plan have a decision-log entry (D-xx)

## Output

- **STYLE** — writing standard violation
- **META** — self-referential document language
- **DRIFT** — spelling or naming inconsistency
- **ORPHAN** — referenced entity has no file
- **BROKEN-REF** — link to nonexistent file

Do NOT fix anything. Report only.

## Out of Scope

Does NOT check physics consistency or equations (use /auditing-physics).
Does NOT treat cross-civilization differences as contradictions.
