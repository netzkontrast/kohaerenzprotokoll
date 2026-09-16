---
description: >-
  Derive a Kernwelt, level or population of Kohärenz Protokoll from first
  principles using the project's derivation chain: Ebene → Logik-Regime → DKT
  expression → Sensorik → Bewohner/Kognition → Ordnung → Sprachregister →
  Geschichte. Orchestrates existing skills in enforced sequence with hard
  checkpoints. Use for a new sub-locality, a new Guardian domain, or when
  re-deriving an existing Kernwelt that feels imported rather than derived.
  Usage: /civilization-build [kernwelt-or-population-name]
argument-hint: "[kernwelt-or-population-name]"
---

# Kernwelt Build — Derivation-Chain Pipeline

You are orchestrating a derivation build. Follow the chain exactly. Do not
skip layers, do not reorder. Every layer derives from the one below it.

In this universe the "planet" is a **Kernwelt** (KW1–KW4), the Überwelt or
the Externe Ebene: a level of one system's inner reality, each with its own
logic regime (Canon `kernwelten-vollstaendig` §1). The "biology" is the DKT
substrate (Coheronen/Erasonen, K₀/K₁) as it expresses itself on that level.
The "species" are the level's Bewohner — Einheiten, Anteile, Guardians — whose
cognition is the level's logic regime seen from inside. A Kernwelt that could
be described without its regime is a reskin, not a derivation.

## The Derivation Chain

```
Ebene → Logik-Regime → DKT-Ausdruck → Sensorik → Bewohner/Kognition → Ordnung → Sprachregister → Geschichte
```

Each step MUST be complete and author-approved before proceeding (AskUserQuestion
at every checkpoint — Rule 0). No forward references.

## Step 0: Prerequisites

1. Read CLAUDE.md, `.claude/skills/PROJECT_REFERENCES.md`, `novel-architect-world/SKILL.md`
2. Read `Canon/…kernwelten-vollstaendig…` (§1 Grundsatz + the target level's §),
   `Canon/…welt-sensorik…` §1–§3 (Welt-Bibel, Sensorik-Lookup, Risse), the relevant `Codex/worlds/<world>.md`
3. Check existing sub-localities and Bewohner of the level to differentiate against
   (`list_world(world_id)`); check the dekanonisierte list — nothing revived
4. Determine build type: new sub-locality inside an existing Kernwelt, a new
   population, or a re-derivation audit of an existing level
5. Create the plan file: `Plan/worldbuilding/YYYY-MM-DD-build-[name].md`

## Step 1: Ebene (Skill: novel-architect-world)

Fix the level and its status: physisch (KW-Diegese) vs nicht-physisch
(Überwelt, Externe Ebene). Which act(s) it serves. Which Guardian dominates
or is absent. What the level is NOT (§1.2 — not a "true reality", not an exit).

**Checkpoint 1:** Author approves the level framing.

## Step 2: Logik-Regime (Skills: /interrogating-design, dramatica-theory)

Derive the level's rules of inference: what counts as a valid step, what
"Abweichung" means here, how time behaves (KW1 deterministic surface, KW2
memory-resonance, KW3 protector logic, KW4 emergence). A KW transition
changes the logic regime, not just the scenery.

**Test:** can a reader who knows only the regime predict how the level
answers a contradiction? If not, the regime is decoration.

**Checkpoint 2:** Author approves the regime.

## Step 3: DKT-Ausdruck (Skills: /writing-science, /auditing-physics)

How do Coheronen/Erasonen, the Landauer signature (kaltes Ozon) and the
Coheron trace (quellenlose Wärme) show up on this level? Which Riss types
belong here (Anteils-Risse vs Welt-Risse, §3)? The heat polarity rule (R-5)
holds everywhere except Vortex 1 Beat 4. Nothing here becomes vocabulary in
prose — it becomes phenomena.

**Checkpoint 3:** Author approves the DKT expression; `@worldbuilder-physicist` audits.

## Step 4: Sensorik (Skill: novel-architect-world, /designing-worlds)

Derive the sensory default set from Steps 1–3: temperature, smell, sound,
light, texture, somatic default of the POV-Anteil. One dominant anomaly
concept per scene. Metaphernverbot in KW1. Sensorik must serve a chapter
action (world skill operating rule).

**Checkpoint 4:** Author approves the sensory palette.

## Step 5: Bewohner / Kognition (Skills: /deriving-social-systems, /auditing-human-assumptions)

Who lives here and how do they think? Einheiten are not "citizens"; Guardians
are not "gods"; Anteile are not "characters in a room". Derive from the regime:
what can a Bewohner perceive, remember, refuse? Run `/auditing-human-assumptions`
— the core question is "derived or imported?" (imported: nation-state,
market, nuclear family, hero's-journey rebellion).

**Checkpoint 5:** Author approves the population derivation.

## Step 6: Ordnung (Skills: /deriving-social-systems, /interrogating-design)

Derive coordination: what the Ordnungsprotokoll/AEGIS does here, how
Konsolidierung/Ausgleich/Wartungsfenster appear, what an "Ausnahme" costs.
Name structures functionally before any familiar label. Negative derivation:
which familiar institutions do NOT emerge? AEGIS is a preservation function,
never a villain (Hard-Constraint 2).

**Checkpoint 6:** Author approves the order layer.

## Step 7: Sprachregister (Skill: novel-architect-character)

Derive the level's language: diegetic vocabulary (Bestand, Restwert,
Abweichung …), Direktiven in VERSALIEN, log field set (D-03), which Anteile
may surface here and under which Riss-Mandate (§7), Stilebene 1/2/3. No DKT
terms in Act I; AEGIS never says "Ich"; voices are never labeled.

**Checkpoint 7:** Author approves the register.

## Step 8: Geschichte (Skills: /designing-lore, novel-architect-structure)

Derive the level's history from everything above: Genesis relation, what
the level remembers/erases, which StoryTimeEvents anchor it, how it changes
across acts (Kapitel-Welt-Mapping). Record events with `record_story_event`.

**Final Checkpoint:** full review for internal consistency against Canon locks (§12).

## Step 9: Record and Audit

1. `create_world` / `create_world_axiom` / `create_codex_entry` (kind `location`,
   `**Kategorie:** …`) via an `execute` block — provenance, not files
2. `python3 scripts/render_codex_views.py`
3. `/auditing-human-assumptions` on the derivation notes
4. `/auditing-canon` for locked spellings and register
5. `/cross-checking` on every new term
6. `find_axiom_contradictions(world_id)`

## Rules

- **Never skip a checkpoint.** Each layer builds on the one below.
- **Derive, don't assume.** Even familiar-looking structures emerge from the regime.
- **Nothing dekanonisiert returns.** Cerberus, Kairos, Sophia, LogOS are names, not figures.
- **Flag the gaps.** A decision the author hasn't made is `[L]` or a question — never a guess.
- **Kernwelt differences are features.** Incompatible regimes across levels are correct.
- **Worldbuilding serves a chapter action.** No lore for its own sake.

## After Completion

- Update `Canon/README.md` only if a new canon document was produced (author decision)
- Update `.claude/skills/PROJECT_REFERENCES.md` if the data map changed
- Log completion in `Plan/sessions/<YYYY-MM-DD>-learnings.md` + `reflect_note` (scope `world`)
