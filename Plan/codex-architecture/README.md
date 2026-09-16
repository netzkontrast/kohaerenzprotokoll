# Plan/codex-architecture — Codex/Wiki/Canon/NCP/graph information model

Started 2026-09-16 for the `todo.md` task "Codex- und Wiki-Architektur für
kontext-effiziente Romanarbeit". Own migration track per that task's
`Arbeitsmodus` — not mixed with normal Wiki maintenance (`Plan/wiki/`, which
covers the Sources→Wiki→Canon research-ingest pipeline specifically).
Engineering language is English; canon prose stays German.

- [codex-inventory_2026-09-16.md](codex-inventory_2026-09-16.md) — item 1:
  full inventory of `Codex/`, `Wiki/`, `Canon/`, NCP/manuscript files and
  the provenance graph (`.agency/session.db`) — files, sizes, generators,
  real graph node/edge census, and every consumer/reference. Read-only;
  decides nothing.
- [authority-matrix_2026-09-16.md](authority-matrix_2026-09-16.md) — item 2:
  which layer is the single source of truth for each of 13 information
  kinds. 11 rows formalize an already-enforced rule; 2 rows (the flattened
  `kind=concept` CodexEntry bucket, and adopting character-knowledge
  tracking) were new calls the inventory surfaced and went to the author
  before being marked settled.

- [overlaps-drift_2026-09-16.md](overlaps-drift_2026-09-16.md) — item 3:
  overlaps/drift between Canon, Codex, Wiki, NCP and Manuscript, checked
  against the authority matrix. Two concrete verified findings (a stale
  `CodexEntry` the 2026-09-11 Canon lock never reached; a mis-citation
  between two non-corresponding rule-numbering series) and one hypothesis
  ruled out (NCP does not need to encode the Slot-16 POV lock). Targeted
  sample, not an exhaustive audit — see its §Method.

- [entity-model-proposal_2026-09-16.md](entity-model-proposal_2026-09-16.md)
  — item 4: 7 new `entity_type` values (`narrative-constraint`, `motif`,
  `philosophy-entry`, `technique`, `note`, `sensorik`, `structural-note`,
  `unclassified`) plus the 4 unchanged `kind` values, and the required-field
  set answering `todo.md`'s knowledge-dimension question (`introduced_in`,
  `valid_chapters`, `revealed_in`, `writer_safe_from`; character knowledge
  stays a graph edge, not an entity field). Two-phase: a body-field rollout
  now, a real engine `kind` extension later if `agency_doctor`/`get_schema`
  confirm it's possible (unverified this session — no agency MCP access).
  All 3 open forks went to the author; the `R-N`/`DR-N` numbering
  collision is explicitly deferred to item 9, not resolved here.

- [knowledge-dimensions_2026-09-16.md](knowledge-dimensions_2026-09-16.md) —
  item 5: maps `todo.md`'s 5 named knowledge dimensions onto item 4's
  fields/mechanisms. 4 of 5 already covered; one real gap found and left
  open — no aggregate "reader knowledge as of scene N" query exists
  (only per-entity `revealed_in` and character-specific
  `what_does_X_know_as_of`), distinct from the `writer_safe_from` fence.
  Filed as a candidate for item 10 or a future engine capability, not
  fixed here.

Next: item 6, deriving the target folder structure exclusively from item
4's stable entity/graph fields — no invented topic folders.
