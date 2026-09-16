---
description: >-
  Health-check the Kohärenz Protokoll corpus: contradictions between Canon /
  Plan / prose, stale claims superseded by decision logs, orphan documents,
  ghost entities (named in prose but absent from the codex), stale Codex views.
  Usage: /lint-wiki [scope: all | Canon | Plan/drafting | chapters | entity-name]
argument-hint: "[all | directory path | entity name]"
---

# Lint Wiki — Corpus Health Check

For Wiki structure, navigation, page moves, or splits, load the
`wiki-maintenance` skill first. Deterministic `page-location`, `page-size`,
`duplicate-slug`, `navigation-link`, `context-window`, and rendered-index
checks belong to `scripts/wiki_lint.py`; this command adds semantic corpus
review and never hand-edits an index.

You are running a systematic health check on the project corpus. This is NOT
a DKT/physics audit (use /auditing-physics), not a prose-rule audit (use
/auditing-canon or `scripts/lint_chapter.py`) and not a storyform check (use
ncp-author / `novel_coherence_check`). This checks structural integrity.

## Check 0: Generated views are fresh (deterministic)

```bash
python3 scripts/render_codex_views.py --check
```
Stale → re-render before anything else; a lint over an outdated glossary is noise.

## Check 1: Contradiction Detection

For the scope, find documents that make conflicting claims about the same
entity, event, rule or timeline fact.

1. Build a claim map: entity → [file, claim] for each factual statement
2. Flag pairs where two files disagree on the same fact
3. Decide which wins under the hierarchy (PROJECT_REFERENCES.md): Manuscript
   prose on telling details > Plan/drafting decisions > Canon (storyform-und-outline
   normative) > NCP > Legacy. Both Storyforms A and B being different is by design.
4. Different Kernwelten having different logic regimes is NOT a contradiction;
   different Anteile perceiving differently is NOT a contradiction.

Output: `| Entity | File A | Claim A | File B | Claim B | Winner | Verdict |`

## Check 2: Stale Claims

Find claims superseded by newer decisions.

1. Read `Plan/drafting/decision-log_2026-09-11.md` and `decision-log_akt2-3_2026-09-11.md`
   (D-xx entries) and `Canon/…welt-sensorik…` §12 (lock index)
2. grep Plan/ and chapter outline headers for terminology or facts those decisions changed
   (e.g. AEGIS naming in Act I, D-05 name reveal, dekanonisierte Alter list)
3. Check each relevant `Codex/worlds/<world>.md` against
   `find_axiom_contradictions(world_id)`

Output: `| File | Stale Claim | Current Decision | Action |`

## Check 3: Orphan Documents

Plan/ and docs/ documents no other document links to or names.

```bash
for f in $(find Plan docs -name "*.md"); do
  n=$(basename "$f" .md)
  c=$(grep -rl --include="*.md" "$n" . | grep -v "^./$f$" | grep -v "^./Codex/" | wc -l)
  [ "$c" -eq 0 ] && echo "ORPHAN: $f"
done
```
Orphans are candidates for linking from `README.md`, `Canon/README.md`,
`PROJECT_REFERENCES.md` or the drafting brief — or for archival.

## Check 4: Ghost Entities

Named things in chapter prose with no codex entry. German capitalises every
noun, so do NOT grep for capitalised words. Instead:

1. Collect candidate names: `scan_proper_nouns(body)` per chapter, then keep
   only tokens that are names in context (Einheiten, Stationen, Orte, Direktiven,
   Anteile, Guardians, Objekte with a fixed designation such as "Station 11")
2. Cross-reference through `scripts/wiki_fts.py search "<name>" --scope codex`
   (or `match_codex_entries(novel_id, text)` per chapter)
3. Flag names appearing in 2+ chapters with no entry as GHOST

Output: `| Entity | Chapters | Mentions | Action (create entry / rename / ignore) |`

## Check 5: Knowledge-fence violations (graph)

For chapters with Scene nodes, run `flag_anachronistic_reference` for facts
named in the prose that the POV-Anteil has not yet learned (`what_does_X_know_as_of`).

## Scope Options

- `all` — full corpus (slow; use before a milestone or monthly)
- `Canon` / `Plan/drafting` / `chapters` — one directory
- `[entity-name]` — everything about one entity (`/compiling-entities` first)

## Output Format

- **CRITICAL** — direct contradiction between two normative sources
- **WARNING** — stale claim, or orphan with inbound mentions elsewhere
- **INFO** — orphan with no mentions
- **GHOST** — entity in 2+ chapters with no codex entry

## After the Report

Do NOT fix anything automatically. Present the report for author review.
Approved fixes: `/ingest` for missing entries, `update_codex_entry` for drift,
a decision-log entry for canon resolutions, then re-render `Codex/`.
Append the outcome to `Plan/sessions/<YYYY-MM-DD>-learnings.md`.

## Recommended Cadence

- After every `/ingest` (new content creates new ghosts)
- Before promoting a chapter from `drafted` to `revised`
- Before any composite gate (`developmental_gate`, `line_gate`, …)
