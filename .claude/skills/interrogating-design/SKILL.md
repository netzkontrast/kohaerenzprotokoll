---
name: interrogating-design
description: >-
  Systematically interrogates a worldbuilding decision, lore proposal, or science
  derivation through exhaustive questioning until all implications, contradictions,
  and dependencies are resolved. Use when stress-testing a new concept, validating
  a proposed rule, or when user says "grill me", "stress test this", "what are the
  implications", "does this break anything", "think through this with me",
  "challenge this idea", or "red team this". Does NOT write content — interrogation only.
model: opus
effort: max
---

# Interrogating Design

Interview me about every aspect of this decision until we reach shared
understanding. Walk down each branch of the decision tree, resolving
dependencies one by one. For each question, provide your recommended answer.
Ask one question at a time. If a question can be answered by exploring
existing documents, explore them instead.

## OODA Loop Mode (Boyd)

Run the interrogation as an iterative cycle:
- **Observe:** Read all relevant files, grep for related terms
- **Orient:** Synthesize against foundational constraints — destroy outdated
  mental models if new data contradicts them
- **Decide:** Formulate a specific hypothesis
- **Act:** Test the hypothesis against the repo

## Dependency-Order Walkthrough

Check implications in layer order (Kohärenz Protokoll hierarchy):
1. DKT foundation — contradicts K₀/K₁, atemporality, the Große Inversion?
   (`Codex/WORLD-AXIOMS.md`, Canon begriffe §1–§2)
2. Storyform — breaks a locked slot of Storyform A or B, a signpost order,
   the Vortex mechanics? (Canon storyform-und-outline, ncp-author drift checks)
3. Kernwelt regime & sensorics — violates the level's logic regime, the heat
   polarity rule, a Riss mandate? (Canon kernwelten / welt-sensorik)
4. Anteile & reveal discipline — breaks a Sprach-DNA hard rule, the
   Multiplizitäts-Schleier, the reveal timeline (§6.2), a knowledge fence?
5. Existing prose — contradicts a telling detail already drafted? (prose wins
   over theory on details — report, don't rewrite)

## Adversarial Red Teaming Escalation

1. Does it contradict any explicit rule?
2. Does it contradict any implicit constraint (downstream implications)?
3. Does it survive cross-civilization application?
4. Would a hostile reader find it inconsistent?
5. Strip the narrative beauty — is the bare mechanism still valid?

## Russell Conjugation Check

Restate the proposal in the most boring, clinical language possible.
If it only works in emotive framing, it's aesthetic, not physics.

## After Validation

1. Self-review for placeholders, contradictions, ambiguity
2. Present in digestible sections
3. Record: drafting outcome → new D-xx entry in `Plan/drafting/decision-log*.md`;
   structural outcome → `record_storyform_decision(novel_id, decision, rationale)`;
   world outcome → `Plan/worldbuilding/decisions/YYYY-MM-DD-<topic>.md`
4. Transition to /planning-worldbuilding or /writing-science

## Out of Scope

Does NOT write content. Does NOT modify files. Only interrogates and validates.
