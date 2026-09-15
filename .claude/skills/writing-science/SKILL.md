---
name: writing-science
description: >-
  Writes new science files following academic prose standards: third-person voice,
  present tense for laws, in-universe terminology, consistent equation formatting,
  citation format. Use when creating new physics, chemistry, biology, or science
  files, expanding existing science content, or when user says "write", "create",
  "draft", "formalize", or "derive" in a science context. Does NOT write civilization
  or narrative content — use /writing-worldbuilding for that.
model: sonnet
effort: high
---

> **Kohärenz Protokoll adaptation.** In this repo a "science file" is a DKT substrate document
(`Plan/worldbuilding/dkt-*.md`, or a proposed addition to
`Canon/kohaerenz-protokoll_begriffe-und-konzepte_2026-06-10.md` §1/§14): the
physics of Coheronen/Erasonen, K₀/K₁, Landauer signature, persistence equation.
Theory is substrate, never surface — nothing written here appears as vocabulary
in chapter prose (zero DKT terms in Act I). Ground claims with
`/researching-papers` → `Plan/research/`, record them with `capture_claim`, and
audit with `@worldbuilder-physicist` before proposing them as `[V]` canon.

# Writing Science

Write new science files following canon standards.

## Prerequisites

1. Read CLAUDE.md for conventions
2. Read `references/writing-standards.md` for detailed prose rules
3. Read all files this content depends on (upstream science)
4. Search for relevant research if grounding is needed (/researching-papers)

## Process

1. Write in dependency order — define terms before using them
2. Every mechanism derives from established upstream science
3. Use in-universe terminology in science files
4. Add YAML frontmatter: title, tags, status: draft
5. Add ## References with citations and one-sentence annotations
6. Add ## Cross-References with relative paths to related files
7. Status: draft — author promotes after review

## Out of Scope

Does NOT write civilization or narrative content (use /writing-worldbuilding).
Does NOT audit existing content (use /auditing-physics or /auditing-canon).
Does NOT search for research papers (use /researching-papers).
