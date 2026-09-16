---
title: "Overlaps and drift — Canon/Codex/Wiki/NCP/Manuscript"
status: draft — targeted sample, not an exhaustive audit (see §Method)
date: 2026-09-16
scope: "todo.md item 3 of 10 — 'Überschneidungen und Drift... erfassen'"
---

# Overlaps and drift

Checked against the [authority matrix](authority-matrix_2026-09-16.md)
(item 2): where the corpus's actual state already matches the matrix's
rulings vs. where it doesn't yet. Two concrete, verified drift cases found;
one hypothesis checked and ruled out. `Wiki/` is excluded — it has 0 pages
(item 1), so there is nothing yet to drift from Canon.

## Method

No agency MCP / CLI access in this session (`.agency/session.db` was only
reachable read-only, via direct SQL — confirmed: no `capability_novel_*`
tool and no `/root/.local/bin/agency` binary available). So this pass used:

1. `git log` on `Canon/*.md` to find which files changed **after** the
   extraction manifests in `Plan/ingest/*.extraction.json` were generated
   (all pinned to the 2026-06-10 Canon versions, last `ingest_canon.py`
   code change 2026-06-13) — a Canon edit after that point is a drift
   candidate until proven otherwise.
2. For each candidate, read the actual diff, then check every downstream
   layer (graph `CodexEntry`/`WorldAxiom`, `ncp.json`/`ncp-b.json`,
   `dramatica.md`, `Plan/drafting/drafting-brief.md`, the affected chapter
   file, `scripts/lint_chapter.py`) for whether it reflects the new Canon
   state or the old one.

This is a **targeted sample** (3 Canon files touched post-ingestion, one
substantive commit), not an exhaustive diff of every CodexEntry against its
Canon source. For full coverage, run `/full-audit-canon canon` or
`/cross-checking` per term — this pass exists to give item 3 concrete
evidence, not to replace those tools.

## Finding 1 — stale `CodexEntry`: Slot-16 Hard-B chapter position

**Canon changed, the graph didn't.** Commit `722a0d2` (2026-09-11,
"Consolidate Akt I prework and chapter navigation") locked the Hard-B
establishing chapter to **Kapitel 5** specifically — previously it was
"one chapter within Kap 5–8, exact position to pin at Storyweaving Phase
6." The same commit added a new rule: AEGIS is never named in reader-facing
Akt I prose (only in Kapitel 5's subjektlose Funktions-Innensicht does the
ordering instance's presence become perceptible at all, still unnamed).

| layer | reflects the lock? |
|---|---|
| `Canon/…storyform-und-outline…` §2.4 | **yes** — "Slot-16-Lock (Autor-Lock 2026-09-11): Kapitel 5 … ist das einzige Hard-B-Kapitel" |
| `Manuscript/…/dramatica.md` line 254 | **yes** — "Akt-I-Präzisierung 2026-09-11 … Kapitel 5 als Hard-B-Innensicht" |
| `Plan/drafting/drafting-brief.md` §3 | **yes** |
| Chapter file `chapters/05-auge-des-sturms.md` | **yes** — frontmatter `pov: "… (Hard-B, …)"`, draft note cites the lock |
| `scripts/lint_chapter.py` (`ACT1-AEGIS` rule) | **yes** — enforces the naming ban, cites "Drafting-Brief §3" |
| **`CodexEntry` `slot-16-hard-b-etablierungskapitel`** (`codexentry:6e51dc32`) | **no** — body still reads: *"EIN Kapitel in Kap 5–8 ist Hard-B … Exakte Position bei Storyweaving (Phase 6) zu pinnen"* (the pre-lock, open state) |
| `Codex/GLOSSARY.md` (rendered from the entry above) | **no** — inherits the stale text |

Per the authority matrix (row 6), `CodexEntry` nodes are the graph-side
representation whose render feeds `Codex/GLOSSARY.md`; per row 1, Canon is
normative. The entry didn't drift *from* Canon so much as it was **never
updated when Canon was**: everything hand-touched in the 2026-09-11 session
(dramatica.md, drafting-brief, the chapter file) got the update; the one
thing that only a graph verb call can update did not.

**Not fixed here** — `update_codex_entry` needs the agency MCP/CLI, neither
available this session. Action item for the next session with engine
access: `update_codex_entry(entry_id="codexentry:6e51dc32", body=<new text
matching the Autor-Lock 2026-09-11 wording>)`, then
`render_codex_views.py`.

## Finding 2 — two non-corresponding rule-numbering series, one mis-citation

The graph holds **two independent, fully-populated rule series**:
`r-1`…`r-10` (10 entries, stylistic rules with roots in Kap-0/lit-critic
heritage) and `drafting-rule-dr-1`…`drafting-rule-dr-43` (43 entries,
canon-extracted drafting rules, e.g. `drafting-rule-dr-10` = "Juna ist nie
Subjekt, nur Wirkung"). They are not aliases of each other — `r-10` is the
Ouroboros-foreshadowing-motif rule, a completely different thing from
`drafting-rule-dr-10`.

`docs/worldcodex-integration.md` line 89 (before this pass's fix) attributed
"Juna never grammatical subject" to **`R-10`** — the wrong series; the
actual rule is `drafting-rule-dr-10`. Fixed in this pass (additive
clarification, not a meaning change) since it's an engineering doc, not
canon prose, and the correction is unambiguous once both entries are read.

**Not fixed**: `CLAUDE.md` §8 ("applicable hard rules R-1…R-10 … Juna never
as sentence subject") uses the same shorthand more loosely — it isn't
citing a specific wrong entry, just using "R-1…R-10" as an informal blanket
term for "the hard style/drafting rules," which happens to span both
series. Lower-priority than finding 1; flagged here rather than edited,
since disambiguating it well means deciding whether "R-N" should formally
mean only the 10-entry series or be retired as a shorthand in favor of
always citing `R-N` vs `DR-N` explicitly — a naming-convention call, not a
typo fix. Candidate input for `todo.md` item 4 (stable entities/fields).

## Hypothesis checked and ruled out — NCP vs. the Slot-16 lock

Before finding the `dramatica.md`/`drafting-brief.md` sync, the working
hypothesis was that `ncp.json`/`ncp-b.json` should also encode the Slot-16
Hard-B position and might be stale. Checked directly: neither file contains
any `hard`, `slot`, or `16`-related field. This is **not drift** — NCP's
schema (throughlines, dynamics, signposts, story points) doesn't model
per-chapter POV-routing mechanics at all; that mechanic lives entirely in
Canon → `dramatica.md`/drafting-brief/chapter frontmatter, correctly per
the authority matrix's row 1/row 2 split (NCP only encodes *storyform*
state, not prose-routing decisions). No action needed; recorded so the next
session doesn't re-check the same hypothesis.

## What wasn't checked (explicitly out of scope for this pass)

- A full CodexEntry-vs-Canon-source diff for all 602 entries (this pass
  found finding 1 via the narrower "which Canon files changed post-ingestion"
  method, which only catches entries tied to a changed source file's
  changed section — not silent drift on Canon files that haven't been
  touched since ingestion).
- `WorldAxiom` contradiction scanning — `find_axiom_contradictions(world_id)`
  needs the agency MCP; item 1's inventory already noted zero `CONTRADICTS`
  edges exist, meaning this check has likely never been run against the
  current 111-axiom set, not that no contradictions exist.
- Any chapters beyond 0–6 (still outline-only; nothing to drift from Canon
  yet in the manuscript-prose sense).

## Next step

`todo.md` item 4: **Stabile Codex-Entitäten und Pflichtfelder definieren**
— now has two concrete open sub-questions from this pass to carry forward:
the `kind=concept` split direction (already decided, item 2) and whether
the `R-N`/`DR-N` shorthand collision (finding 2) should resolve into a
single naming convention as part of the new entity design.
