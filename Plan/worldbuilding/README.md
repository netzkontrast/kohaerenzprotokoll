# Plan/worldbuilding — Kernwelt builds, DKT substrate notes, world decisions

Working notes for the world layer. The facts themselves live in `Graph/`
(World, WorldAxiom, CodexEntry records) and render into `Codex/`; these files
are the derivation behind them.

- `YYYY-MM-DD-build-<name>.md` — the plan file of a `/kp-world` run, one
  section per layer of the derivation chain (Ebene → Logik-Regime →
  DKT-Ausdruck → Sensorik → Bewohner/Kognition → Ordnung → Sprachregister →
  Geschichte), each written as the author approves it.
- `dkt-*.md` — substrate documents. They ground the physics and are never
  quoted in prose; `@worldbuilder-physicist` audits them.
- `decisions/YYYY-MM-DD-<topic>.md` — outcomes of a world question that needed
  stress-testing. A decision that supersedes canon or resolves a contradiction
  goes through `/tetraframe` first and is recorded as a D-xx.

Drafting decisions stay in `Plan/drafting/decision-log*.md`; structural ones
are `DecisionRecord` records in `Graph/nodes/decision_record.jsonl`.

`python3 scripts/world_check.py` reads the 111 axioms and reports the pairs
worth reading side by side before a build adds more.
