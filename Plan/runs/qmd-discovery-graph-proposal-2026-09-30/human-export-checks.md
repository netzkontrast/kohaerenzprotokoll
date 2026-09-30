# Human graph export — validation

The final deliverable is a human-readable atlas, not a portable database.
The author changed the intended purpose; binary snapshots, machine manifests,
restore/import commands and their implementation were removed.

- Seven offline atlas fixtures pass: deterministic generation, readable topic
  relationships, source-reading/citation distinction, no passage or row dump,
  missing-data visibility, recommendation/decision separation, output-only
  derivation and startup for local/remote Claude sessions.
- Fifteen native GraphQLite reader integration tests pass, including the
  wrong-first/right-second citation regression. The evidence generator now
  chooses the actual verifying reference.
- The branch incorporates main through c74f279. Human pages are generated from
  the matching, fresh database and compared with the authoritative wiki graph.
- The atlas consists of one page per wiki term, source relationships, conflicts,
  questions, decision dependencies, discovery limits and small CLI recipes.
  No source passage, source-line list, evidence payload or physical graph row is
  included. Builders never read Graph and `kg.py restore` is rejected.

The source-scoped Assertion/Reading/template-lineage schema additions remain
prioritized proposals in the content review. No new source reading, model call,
source rewrite or canon promotion was performed.

## Abschließende Prüfung

- Standard-Selftests: 37 bestanden, keine Fehler.
- Native Graph-Integration: 15 bestanden.
- Export: 113 Markdown-Seiten für 106 Begriffe; keine defekten internen Links.
- Keine binären Snapshot-Dateien unter `Graph/`; kein Import- oder Restore-Befehl.
- `git diff --check`: bestanden.
