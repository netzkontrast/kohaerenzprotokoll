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

Next: item 4, stable Codex entities and required fields — has direction
from item 2 (retire `kind=concept`) and two open sub-questions from item 3
(the stale entry, the `R-N`/`DR-N` naming collision) to carry forward.
