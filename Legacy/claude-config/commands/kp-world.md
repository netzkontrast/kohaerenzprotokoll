---
description: >-
  Derive a Kernwelt, level, sub-locality or population from first principles
  through the project's chain — Ebene → Logik-Regime → DKT-Ausdruck → Sensorik →
  Bewohner/Kognition → Ordnung → Sprachregister → Geschichte — with a hard
  author checkpoint at every layer, then land the result in Graph/ so it renders
  into Codex/. Usage: /kp-world [kernwelt, level or population name]
argument-hint: "[kernwelt-or-population-name]"
---

# World — derive a level, then put it in the Codex

In this universe the "planet" is a **Kernwelt** (KW1–KW4), the Überwelt or the
Externe Ebene: a level of one system's inner reality, each with its own logic
regime (Canon `kernwelten-vollstaendig` §1). The "biology" is the DKT substrate
(Coheronen/Erasonen, K₀/K₁) as it expresses itself on that level. The "species"
are the level's Bewohner — Einheiten, Anteile, Guardians — whose cognition *is*
the level's logic regime seen from inside.

**A Kernwelt that could be described without its regime is a reskin, not a
derivation.** That is what this chain exists to prevent.

## The chain

```
Ebene → Logik-Regime → DKT-Ausdruck → Sensorik → Bewohner/Kognition → Ordnung → Sprachregister → Geschichte
```

Each layer derives from the one below it. Do not skip a layer, do not reorder,
no forward references. Every checkpoint is an `AskUserQuestion` to the author
(Rule 0) — the chain never self-approves.

## Step 0: what already exists

```bash
python3 scripts/world_check.py                  # axiom pairs worth reading
python3 scripts/wiki_fts.py search "…"          # anything the wiki knows
```

```python
from tools import kpgraph
g = kpgraph.load()
for w in g.nodes("World"):
    print(w["slug"], len(g.axioms_of(w["_nid"])), "axioms")
```

Read `novel-architect` → [reference/world.md](../skills/novel-architect/reference/world.md),
`Canon/…kernwelten-vollstaendig…` (§1 plus the target level's §),
`Canon/…welt-sensorik…` §1–§3, and the target world's axioms at
`Codex/axioms/<world-slug>.md` (`Codex/WORLD-AXIOMS.md` routes to them; read the
one world you are deriving, not all 111 axioms).

Decide the build type: a new sub-locality inside an existing Kernwelt, a new
population, or a re-derivation audit of a level that feels imported. Open the
plan file `Plan/worldbuilding/YYYY-MM-DD-build-<name>.md` and write each layer
into it as it is approved.

Nothing dekanonisiert returns: Cerberus, Kairos, Sophia and LogOS are names in
the record, not figures to revive.

## Step 1 — Ebene

Fix the level and its status: physisch (KW-Diegese) or nicht-physisch (Überwelt,
Externe Ebene). Which act(s) it serves. Which Guardian dominates or is absent.
What the level is **not** (§1.2 — not a "true reality", not an exit).

## Step 2 — Logik-Regime

Derive its rules of inference: what counts as a valid step, what "Abweichung"
means here, how time behaves. KW1 deterministic surface, KW2 memory-resonance,
KW3 protector logic, KW4 emergence. A KW transition changes the logic regime,
not the scenery.

**Test:** could a reader who knows only the regime predict how this level
answers a contradiction? If not, the regime is decoration.

## Step 3 — DKT-Ausdruck

How do Coheronen/Erasonen, the Landauer signature (kaltes Ozon) and the Coheron
trace (quellenlose Wärme) appear here? Which Riss types belong to this level —
Anteils-Risse or Welt-Risse (§3)? The heat-polarity rule R-5 holds everywhere
except Vortex 1 Beat 4. None of this becomes vocabulary in prose; it becomes
phenomena. Have `@worldbuilder-physicist` audit the layer.

## Step 4 — Sensorik

Derive the sensory default set from Steps 1–3: temperature, smell, sound, light,
texture, and the somatic default of the POV-Anteil. One dominant anomaly concept
per scene. Metaphernverbot in KW1. **Sensorik serves a chapter action** — a
palette that no scene needs is lore, and lore is not the deliverable.

## Step 5 — Bewohner / Kognition

Who lives here and how do they think? Einheiten are not "citizens", Guardians
are not "gods", Anteile are not "characters in a room". Derive from the regime:
what can a Bewohner perceive, remember, refuse?

Then the question that matters most — **derived or imported?** Walk the
structures you just wrote and ask of each one whether it follows from this
level's regime and substrate, or whether it arrived from a familiar Earth
template. Nation-state, market, nuclear family, school, police, hero's-journey
rebellion: each is a red flag until the derivation is on the page. Name every
structure functionally before reaching for a familiar label.

## Step 6 — Ordnung

Derive coordination: what the Ordnungsprotokoll and AEGIS do here, how
Konsolidierung / Ausgleich / Wartungsfenster appear, what an "Ausnahme" costs.
Run the negative derivation too: which familiar institutions do **not** emerge
here, and why? AEGIS is a preservation function and is never a villain.

## Step 7 — Sprachregister

Derive the level's language: diegetic vocabulary (Bestand, Restwert,
Abweichung …), Direktiven in VERSALIEN, the log field set (D-03), which Anteile
may surface here and under which Riss-Mandate (§7), Stilebene 1/2/3. No DKT
terms in Act I. AEGIS never says "Ich". Voices are never labelled.

## Step 8 — Geschichte

Derive the level's history from everything above: its relation to Genesis, what
it remembers and what it erases, which StoryTimeEvents anchor it, how it shifts
across acts. A myth, a relic or a founding legend belongs here and nowhere
earlier — it is an output of the regime, never an input to it.

## Step 9 — land it in the Codex

`Graph/` is the fact layer and `Codex/` renders from it. Write the approved
layers as records, not as prose files:

```python
from tools.kpgraph.writer import GraphWriter
w = GraphWriter(".")
world = w.apply("create_world", {"slug": "…", "name": "…"})
w.apply("create_world_axiom", {"text": "…", "severity": "hard",
                               "world_id": world["world_id"]})
w.apply("create_codex_entry", {"slug": "…", "name": "…", "kind": "location",
                               "body": "**Kategorie:** …\n\n…",
                               "triggers": "…", "novel_id": "novel:9d170c31"})
w.apply("record_story_event", {"label": "…", "when_story": "…",
                               "novel_id": "novel:9d170c31"})
w.flush()
```

`kind` is closed: `concept`, `location`, `faction`, `artefact`,
`minor-character`. Anything else is stored as `concept` with its original
category as the first body line. Writes are idempotent — re-running finds the
record instead of duplicating it.

Then:

```bash
python3 scripts/render_codex_views.py     # Graph/ -> Codex/
python3 scripts/world_check.py            # new axiom against the existing 111
python3 scripts/kp_check.py               # every gate
```

`world_check.py` reports axiom pairs that share rare motifs where exactly one
side is negated. A flagged pair is a question, never a verdict: resolving one
changes canon, so it goes through `/tetraframe` and a D-xx decision.

## Rules

- **Never skip a checkpoint.** Each layer builds on the one below.
- **Derive, don't assume.** Even a familiar-looking structure must emerge from
  the regime, or it does not belong here.
- **Flag the gaps.** A decision the author has not made is `[L]` or a question
  to them — never a guess, and never deferral language.
- **Incompatible regimes across levels are correct**, not a defect to smooth.
- **Worldbuilding serves a chapter action.** No lore for its own sake.

## After completion

Log the build in `Plan/sessions/<YYYY-MM-DD>-learnings.md`. Update
`Canon/README.md` only if a new canon document was produced, and that is the
author's decision. Update `.claude/skills/PROJECT_REFERENCES.md` if the data
map changed. Commit `Graph/` and the re-rendered `Codex/` together.
