# Legacy — Novel & Dramatica Corpus (imported)

This folder is a **read-only reference snapshot** of all novel-writing and
Dramatica-related material harvested from the Agency backups repository. It is
the raw input for the **first-principles decomposition** that will define how
the *Kohärenz Protokoll* repository should be structured as a novel-writing
environment.

> **Working language for engineering work is English. The novel's canon prose is
> German — never translate canon prose.**

## Provenance

- **Source repo:** `netzkontrast/agency-backups`
- **Source commit:** `8090e3c8d4c39a4ad4e3b1f8c0e9a6d7b2c1f0a9` (branch `main`)
- **Imported:** 2026-05-30
- **Selection rule:** every file under `skills/ tasks/ research/ prompts/ tools/
  decisions/ maintenance/` whose path or content matched
  `novel | dramatica | ncp | storyform | throughline | narrative-context-protocol`.
- **Total:** ~4.7 MB, 521 files. Nothing was modified; structure is preserved
  relative to the source repo (`Legacy/<category>/<item>`).

## What's here

### `skills/` — the shipped capability, as Claude Code skills
| Skill | Role |
|---|---|
| `dramatica-theory` | Dramatica narrative theory (Phillips & Huntley, 4th ed.) — storyforming, throughlines, draft diagnosis. |
| `dramatica-vocabulary` | Active Dramatica vocabulary — 75 dynamic pairs, encoding, storyweaving, consistency checks. |
| `ncp-author` | NCP schema cheatsheet, canonical vocabulary (463 appreciations + 144 narrative_functions), validator, 10-stage workflow. |
| `novel-architect` | Method-driven novel-architecture orchestrator — 8 phases, hard exit gates, AskUserQuestion loops, NCP state persistence. |
| `novel-architect-character` | Character architecture — TSDP/IFS, Big Five (OCEAN), Enneagram, Jung archetypes → NCP `players[]`. |
| `novel-architect-structure` | Plot structures — 40-chapter matrix, Hero's Journey, Save the Cat, Dramatica Quad. |
| `novel-architect-world` | World & research — domain mapping, world bible, research briefs. |
| `novel-architect-scene` | Scene-level detail, Q1–Q5 scene-level bridge audit, drafting pre-checks. |
| `novel-architect-legacy` | DEPRECATED snapshot of the project-specific `novel-architect` v0.3.3 (the original Kohärenz Protokoll skill). |

### `tasks/` — the build history (25 task specs)
Dramatica scenarios (`078`–`082`), nav follow-ups (`042`), the novel-architect
epics & enforcement (`070`, `071`, `083`, `088`), linters & validation (`073`,
`074`, `084`, `085`, `086`), canon-status schema (`076`), scene-level bridge
(`075`), render pipeline/architecture (`087`, `090`), and the original
skill.md analysis (`003`), NCP integration (`015`), retirement of legacy (`089`).

### `research/`
- `ncp-novel-co-authoring-spec` — the NCP co-authoring specification research.
- `integrate-dramatica-ncp-skills` — how Dramatica + NCP skills interlock.
- `gemini/github-skillmd-novel-authoring-de-en` — bilingual authoring research.

### `prompts/`
- `dramatica-scenarios-foundation`, `github-skillmd-novel-authoring-de-en`,
  `integrate-dramatica-ncp-skills` — the prompts that produced the above.

### `tools/`
- `dramatica-nav` — the Dramatica navigation/lookup tool (`dramatica_lookup` port reference).
- `tests/fixtures/novel-architect-v111` — golden fixtures.

### `maintenance/schemas/narrative-ontology/`
- Precompiled narrative-ontology schemas: `novel.dual-storyform`,
  `novel.storyform-slot-fill`, `novel.character-arc`, `novel.act-pivot`,
  `novel.crucial-element-audit`, `novel.diagnose-flat-draft`.

### `decisions/`
- `0010-novel-architect-error-tier-linter-policy.md` — the linter error-tier ADR.

## How this gets used

The corpus is decomposed by five parallel Jules sessions (see
`../Plan/decomposition/`). Each session takes one slice of the novel capability,
reads the relevant `Legacy/` material **plus** the `netzkontrast/agency` plugin
contract (`search · get_schema · execute`; Intent · Capability · Lifecycle ·
Memory), and proposes how that slice should live in the Kohärenz Protokoll repo.
The five proposals are then synthesised into a single repo-design plan.
