# Brief — readings from document 419 (step 6)

1 document, one reader, one batch: `ingest-420`. Files go to `Plan/runs/ingest-420/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 419 | `parakonsistenz-aegis-und-nicht-existenz` | 2025-04-21 | „the paraconsistency report“ (an unsigned German „Bericht“) | applies paraconsistent logic to „einem hypothetischen System namens „aegis““ defined by a self-referring sentence (L31, L33), and reads it as a guardian separating existence from non-existence (L308); a report on an imagined system, no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (423 lines for `parakonsistenz-aegis-und-nicht`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analysis of a hypothetical system: write „the paraconsistency report analyses a hypothetical Aegis …“; it calls its Aegis imagined (L354), so nothing it argues is the novel's AEGIS. Quote the German as written; cut before straight and nested quotes, bold markers and glued footnote digits. Never write a real person's name, nor a term carrying one.

## Pages — document 419, `parakonsistenz-aegis-und-nicht-existenz`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `Aegis` L11, L37, L38, L39, L45, L49, … (55 lines). minor (1–3): the report analyses a hypothetical system „aegis“ defined by the self-referring sentence „aegis ist, was aegis verbindet, das es nicht ist“ (L31, L33); it reads Aegis as „Wächter, der Existenz von Nicht-Existenz trennt“ (L308), a guardian function that follows from the contradictory self-definition (L322); it calls the system imagined (L354).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L41. not read: an occurrence — coherence in the logical sense of the report (L41).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `archiv-der-grenzen`: `Grenze` (near `archivdergrenzen`). decided with the page above: `Aegis-System`, `Aegis-Definition`, `Aegis-Paradoxon` read on aegis; `Wächter`, `Wächterfunktion`, `Grenzwächter` the report's reading of Aegis, read on aegis; `Existenz`, `Grenze`, `Parakonsistente Kohärenz` the report's logical vocabulary, not K0-Existenz, the Archiv der Grenzen or the Große Mauer.
- `grosse-mauer`: `Grenze` (near `groemauersystemgrenze`), `Grenze` (near `systemgrenze`). decided with the page above: `Aegis-System`, `Aegis-Definition`, `Aegis-Paradoxon` read on aegis; `Wächter`, `Wächterfunktion`, `Grenzwächter` the report's reading of Aegis, read on aegis; `Existenz`, `Grenze`, `Parakonsistente Kohärenz` the report's logical vocabulary, not K0-Existenz, the Archiv der Grenzen or the Große Mauer.
- `k0-existenz`: `Existenz` (near `k0existenz`). decided with the page above: `Aegis-System`, `Aegis-Definition`, `Aegis-Paradoxon` read on aegis; `Wächter`, `Wächterfunktion`, `Grenzwächter` the report's reading of Aegis, read on aegis; `Existenz`, `Grenze`, `Parakonsistente Kohärenz` the report's logical vocabulary, not K0-Existenz, the Archiv der Grenzen or the Große Mauer.
- `kohaerenz`: `Parakonsistente Kohärenz` (near `koharenz`). decided with the page above: `Aegis-System`, `Aegis-Definition`, `Aegis-Paradoxon` read on aegis; `Wächter`, `Wächterfunktion`, `Grenzwächter` the report's reading of Aegis, read on aegis; `Existenz`, `Grenze`, `Parakonsistente Kohärenz` the report's logical vocabulary, not K0-Existenz, the Archiv der Grenzen or the Große Mauer.


**Record entries:** none.

**Pages not read:** kohaerenz — an occurrence.

**Not promoted:** Aegis-Definition, Aegis-Paradoxon, Wächterfunktion, Grenzwächter, Parakonsistente Kohärenz, and the borrowed logic vocabulary.

**One reader**: aegis.

**Chapter readings**: none — the document names no chapter.
