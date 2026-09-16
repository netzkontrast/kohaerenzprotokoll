---
description: >-
  Health-check the Kohärenz Protokoll corpus: contradictions between Canon /
  Plan / prose, stale claims superseded by decision logs, orphan documents,
  ghost entities (named in prose but absent from the codex), stale Codex views.
  --quick runs only a read-only Wiki/** structure snapshot instead.
  Usage: /lint-wiki [--quick | scope: all | Canon | Plan/drafting | chapters | entity-name]
argument-hint: "[--quick | all | directory path | entity name]"
---

# Lint Wiki — Corpus Health Check

For Wiki structure, navigation, page moves, or splits, load the
`wiki-maintenance` skill first. Deterministic `page-location`, `page-size`,
`duplicate-slug`, `navigation-link`, `context-window`, and rendered-index
checks belong to `scripts/wiki_lint.py`; this command adds semantic corpus
review and never hand-edits an index.

## Quick mode (--quick)

Read-only structure/health snapshot of `Wiki/**` — no contradiction scan, no
ghost-entity scan, no fixes. Use before deciding whether the full corpus
review below is warranted, or whenever a session needs to know what the
Wiki currently looks like before writing into it.

1. **The contract**: read `Wiki/SCHEMA.md` §"Directory contract" and
   summarise in one line each — the four page kinds and their canonical
   path pattern (`sources/<category>/`, `concepts/<kind_detail>/`,
   `questions/<axis>/`, `syntheses/<YYYY>/`); which files are rendered
   (never hand-edited: `index.md`, `concept-table.md`, `context-map.md`,
   `graph/coverage.json`, every partition `README.md`); page budgets from
   `Wiki/schema/conventions.yaml`.
2. **Deterministic health** (free, no LLM):
   ```bash
   python3 scripts/wiki_lint.py --health
   python3 scripts/render_wiki_views.py --check
   ```
   Report verbatim: errors/warnings/info counts, pages by kind, pages by
   status, candidate count, open questions by axis, contested pages, sources
   ingested vs. manifest total, edge count, and whether views are stale.
3. **Partition inventory** — for each occupied kind directory (`sources/`,
   `concepts/`, `questions/`, `syntheses/`), list its partitions and page
   counts:
   ```bash
   for d in Wiki/sources Wiki/concepts Wiki/questions Wiki/syntheses; do
     [ -d "$d" ] || continue
     echo "== $d =="
     find "$d" -mindepth 1 -maxdepth 1 -type d | while read -r p; do
       n=$(find "$p" -maxdepth 1 -name "*.md" ! -name "README.md" | wc -l)
       echo "  $(basename "$p"): $n page(s)"
     done
   done
   ```
   Empty taxonomy (0 pages everywhere) is a valid, expected state early in
   the research-ingest pipeline — report it as such, not as a failure.
4. **Candidates awaiting promotion**: step 2's `--health` output already
   printed `candidates: N` — that's the count. Candidates are drafts from
   `/research-ingest` that only `/wiki-promote` (human-gated) moves into
   `sources/` or `concepts/`; promote nothing here.

Report format: contract summary, health output, partition inventory,
pending-candidates count (from step 2), then the single most useful next
action (e.g.
"views stale → render_wiki_views", "12 candidates, 0 promoted → run
/wiki-promote", "0 pages → run /research-ingest first"). Stop here — do not
continue to Check 0 below unless the user asks for the full health check.

You are running a systematic health check on the project corpus. This is NOT
a DKT/physics audit (ask `@worldbuilder-physicist`), not a prose-rule audit
(`scripts/lint_chapter.py`) and not a storyform check (use
ncp-author / `scripts/storyform_check.py`). This checks structural integrity.

## Check 0: Generated views are fresh (deterministic)

```bash
python3 scripts/kp_check.py            # every deterministic gate, including the two below
python3 scripts/render_codex_views.py --check
python3 scripts/world_check.py         # axiom pairs worth reading together
```
Stale → re-render before anything else; a lint over an outdated glossary is noise.
Everything `kp_check.py` reports is decidable and free: fix those first, because
the semantic checks below cost tokens and should not be spent on drift a script
already found.

## Check 1: Contradiction Detection

For the scope, find documents that make conflicting claims about the same
entity, event, rule or timeline fact.

1. Build a claim map: entity → [file, claim] for each factual statement
2. Flag pairs where two files disagree on the same fact
3. Decide which wins under the hierarchy (PROJECT_REFERENCES.md): Manuscript
   prose on telling details > Plan/drafting decisions > Canon (storyform-und-outline
   normative) > NCP > repository history. Both Storyforms A and B being
   different is by design.
4. Different Kernwelten having different logic regimes is NOT a contradiction;
   different Anteile perceiving differently is NOT a contradiction.

Output: `| Entity | File A | Claim A | File B | Claim B | Winner | Verdict |`

## Check 2: Stale Claims

Find claims superseded by newer decisions.

1. Read `Plan/drafting/decision-log_2026-09-11.md` and `decision-log_akt2-3_2026-09-11.md`
   (D-xx entries) and `Canon/…welt-sensorik…` §12 (lock index)
2. grep Plan/ and chapter outline headers for terminology or facts those decisions changed
   (e.g. AEGIS naming in Act I, D-05 name reveal, dekanonisierte Alter list)
3. Run `python3 scripts/world_check.py`; it reports axiom pairs from one world
   that share rare motifs where exactly one side is negated. A flagged pair is
   a question, not a verdict — resolving one changes canon and goes through
   `/tetraframe`.

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

1. Collect candidate names per chapter: Title-Case tokens that are names in
   context (Einheiten, Stationen, Orte, Direktiven, Anteile, Guardians, objects
   with a fixed designation such as "Station 11"). Sentence-initial nouns are
   not evidence on their own.
2. Cross-reference against the codex the way the graph already allows — every
   entry carries `triggers`, so a name already covered will match one:

```python
from tools import kpgraph
from pathlib import Path
g = kpgraph.load()
text = Path("Manuscript/.../chapters/NN-….md").read_text(encoding="utf-8").lower()
covered = {t.strip().lower() for e in g.nodes("CodexEntry")
           for t in e.get("triggers", "").split(",") if len(t.strip()) >= 4
           and t.strip().lower() in text}
# a candidate name that matches nothing in `covered` is a ghost candidate
```

3. Flag names appearing in 2+ chapters with no entry as GHOST

Output: `| Entity | Chapters | Mentions | Action (create entry / rename / ignore) |`

## Check 5: Reveal-order violations (graph)

What the graph supports today: `StoryTimeEvent` records linked by
`REVEALED_IN` to a `Scene`, and `SCENE_OF` from that scene to its chapter. So
for the 15 Kap-0 scenes you can ask whether prose names an event before the
chapter that reveals it.

```python
from tools import kpgraph
g = kpgraph.load()
for event in g.nodes("StoryTimeEvent"):
    for scene in g.targets_of(event["_nid"], "REVEALED_IN"):
        chapter = g.targets_of(scene["_nid"], "SCENE_OF")
        print(event["label"], "revealed in", scene.get("slug"), chapter)
```

Per-character knowledge is **not** checkable: it needed `KnownFact` nodes and
the graph holds none. Treat a suspected anachronism as a question for the
author rather than a finding, and say which of the two it is.

## Scope Options

- `all` — full corpus (slow; use before a milestone or monthly)
- `Canon` / `Plan/drafting` / `chapters` — one directory
- `[entity-name]` — everything about one entity; gather it first with
  `python3 scripts/wiki_fts.py search "…"` plus a trigger scan of the codex

## Output Format

- **CRITICAL** — direct contradiction between two normative sources
- **WARNING** — stale claim, or orphan with inbound mentions elsewhere
- **INFO** — orphan with no mentions
- **GHOST** — entity in 2+ chapters with no codex entry

## After the Report

Do NOT fix anything automatically. Present the report for author review.
Approved fixes: `/kp-canon` for missing entries, a `Graph/` record edit for drift,
a decision-log entry for canon resolutions, then re-render `Codex/`.
Append the outcome to `Plan/sessions/<YYYY-MM-DD>-learnings.md`.

## Recommended Cadence

- After every `/kp-canon` (new content creates new ghosts)
- Before promoting a chapter from `drafted` to `revised`
- Before the editorial gate `python3 scripts/lit_critic_gate.py --chapter N`
