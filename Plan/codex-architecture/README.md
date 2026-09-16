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

Next: item 3, overlaps/drift between Canon, Codex, Wiki, NCP and Manuscript
— check the corpus against the authority matrix's rulings.
