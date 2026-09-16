# Novel Architect — World

Use this skill for KW1–KW4, Überwelt, Externe Ebene, sensorics, world axioms, locations, diegetic technology, and world-consistent anomaly design.

## Authoritative data

- [Shared current reference map](../PROJECT_REFERENCES.md)
- [World + sensorics + drafting discipline](../../../Canon/kohaerenz-protokoll_welt-sensorik-drafting_2026-06-10.md)
- [Core worlds](../../../Canon/kohaerenz-protokoll_kernwelten-vollstaendig_2026-06-10.md)
- [Terms + concepts](../../../Canon/kohaerenz-protokoll_begriffe-und-konzepte_2026-06-10.md)
- [Current arc plans](../../../Plan/drafting/)

## Operating rule

Worldbuilding must serve a chapter action. Do not add lore merely because it is interesting. A new location, rule or anomaly must either constrain behavior, externalize a character/state conflict, create a usable cause/effect chain, or pay off an established motif.

## Key locks

- KW1: sterile, geometric, deterministic surface; theory remains invisible.
- Ozone/cold/sharp = AEGIS suppression signature.
- Warmth = relational/Juna trace, first explicit warmth in Kap. 3; keep polarity distinct outside locked convergence beats.
- Rifts are experienced phenomena, not technical lectures.
- KW transitions change the logic regime, not just the scenery.
- External Cologne is not a simplistic 'real world outside the simulation'; preserve the mirror ontology.

## Workflow

1. Identify current KW/level and its permitted logic regime.
2. Pull the relevant sensoric set and location canon.
3. Check which anomaly/rift type belongs to the triggering function.
4. Use one dominant anomaly concept per scene.
5. Check whether the detail has already been established in adjacent prose.
6. Record truly new world decisions as `[V]` until canonized.

## Building a new level or population

A whole new Kernwelt, sub-locality or population is a derivation, not a
sketch: run `/kp-world`, which walks Ebene → Logik-Regime → DKT-Ausdruck →
Sensorik → Bewohner/Kognition → Ordnung → Sprachregister → Geschichte with an
author checkpoint at every layer and lands the result in `Graph/`. What
follows is what that chain is testing for, and applies to any world change
large or small.

### Derived or imported?

The question to ask of every structure on the page: does this follow from this
level's logic regime and DKT substrate, or did it arrive from a familiar Earth
template? Each of these is a red flag until the derivation is written down —
nation-state, market, money, nuclear family, school, police, prison, church,
newspaper, hero's-journey rebellion, a council that votes.

Name a structure **functionally** before reaching for a familiar label: "the
thing that decides which memories stay addressable" is a finding, "the
archive" is a reskin. Run the negative derivation too — which familiar
institutions do *not* emerge here, and why not? Absences are evidence that the
regime is doing work.

Einheiten are not citizens. Guardians are not gods. Anteile are not characters
in a room. What a Bewohner can perceive, remember and refuse comes from the
regime, and nowhere else.

### Physical and sensory foundations

Sensorik is derived, never decorated: temperature, smell, sound, light,
texture and the POV-Anteil's somatic default all follow from the level's
regime and its DKT expression. One dominant anomaly concept per scene. The
heat polarity is a hard lock — cold/sharp ozone is the Landauer signature of
AEGIS suppression, quellenlose Wärme is the Coheron trace — and it holds
everywhere except Vortex 1 Beat 4.

### History, myth and relics

A level's history is an **output** of everything above, never an input. Derive
it last: its relation to Genesis, what it remembers and what it erases, which
StoryTimeEvents anchor it, how it shifts across the acts. A founding legend, a
relic or a sacred object earns its place only when the regime explains why
*that* story and *that* object, and when some chapter action needs it.

Nothing dekanonisiert returns. Cerberus, Kairos, Sophia and LogOS are names in
the record, not figures to revive.

### Checking a world change

```bash
python3 scripts/world_check.py            # axiom pairs worth reading together
python3 scripts/render_codex_views.py     # Graph/ -> Codex/
python3 scripts/kp_check.py               # every free gate
```

`world_check.py` reports axiom pairs from one world that share rare motifs
where exactly one side carries a negation. It narrows the 111 axioms to the
handful worth reading side by side; it cannot decide whether they conflict. A
flagged pair is a question for the author, and resolving one changes canon, so
it goes through `/tetraframe` and a D-xx decision.
