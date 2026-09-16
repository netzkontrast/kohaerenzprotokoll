---
description: >-
  Answer a complex question about Kohärenz Protokoll by searching Canon, Plan,
  Manuscript and the codex graph, citing sources, and filing the answer back as
  a synthesis page if it is worth keeping.
  Usage: /query [question]
argument-hint: "[your question about the novel's canon, world, characters or structure]"
---

# Query — Codex Query with Compounding

You are answering a question by searching the project corpus and filing the
answer back if it produces a high-value synthesis. The key insight: if an
answer required synthesising 5+ documents, that synthesis should become a
permanent page so it compounds — never re-derived from scratch.

## Step 1: Search the Corpus (in hierarchy order)

1. `python3 scripts/wiki_fts.py search "<key terms>" --scope codex --limit 5`,
   then open only the returned detail pages/line ranges; use
   `match_codex_entries(novel_id, <question text>)` for trigger-based graph hits
2. `.claude/skills/PROJECT_REFERENCES.md` for which document owns the topic
3. `grep -r` across `Canon/`, `Plan/drafting/`, `Manuscript/**/chapters/`
4. Read the full content of each relevant small page, not whole Codex indexes
5. Graph transforms where they fit: `what_does_X_know_as_of`,
   `list_story_events_up_to`, `narrative_order`, `list_world`
6. The matching `Codex/timeline/<phase>.md` and `Codex/worlds/<world>.md` pages
   for dated facts and rules
7. Legacy material only as evidence, never as authority

## Step 2: Synthesise the Answer

Answer with direct citations to specific files and sections.
Format: "Laut `Canon/...` §x, [claim]." / "According to [file], [claim]."
Mark each cited fact's provenance: `[K]` locked, `[V]` proposal, `[L]` gap.

If documents disagree: report the disagreement explicitly with both sources and
which one wins under the hierarchy (storyform-und-outline is normative in Canon;
existing prose beats abstract theory on telling details — report, don't rewrite).
If the answer isn't in the corpus: say so — don't invent (Rule 0: ask).

## Step 3: Evaluate for Filing

**File it if:** the answer synthesised 3+ documents, resolved an ambiguity,
connected concepts not previously linked, or revealed a gap/contradiction.
**Don't file if:** simple lookup from one file, session logistics, or the
content already exists as a codex entry or Plan document.

## Step 4: File the Answer (if warranted)

Create `Plan/queries/YYYY-MM-DD-<slug>.md`:

```markdown
---
title: "[Synthesis Topic]"
tags: [synthesis, <relevant-tags>]
status: draft
source: "Synthesized from [list of source files]"
query: "[The original question]"
---

# [Synthesis Topic]

[The synthesised answer, German for canon content, with file cross-references]

## Quellen
[Every file read to produce this answer]
```

If the synthesis defines a term the codex lacks, propose a codex entry via
`create_codex_entry` (kind per CLAUDE.md §3) and re-render `Codex/`. Capture a
`reflect_note` (scope `project`) so the graph carries the finding.

## Step 5: Report Back

1. The answer
2. Whether it was filed (and where)
3. Any gaps or contradictions discovered — as candidates for the decision log

## Rules

- Never invent content that isn't in the corpus
- Cite specific files, not vague references
- Filing is optional — only file genuinely useful syntheses
- Filed pages get `status: draft` — the author promotes to canon
