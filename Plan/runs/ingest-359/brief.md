# Brief — readings from document 358 (step 6)

1 document, one reader, one batch: `ingest-359`. Files go to `Plan/runs/ingest-359/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 358 | `an-introduction-to-the-world-of-kohaerenz-protokoll` | 2025-11-03 | „the world introduction“ (an unsigned English guide for new readers) | presents Kael as a mind of ANPs and EPs read through TSDP, AEGIS with its void the Nichts Rauschen and its Paradox of Misaligned Coherence, and Das Fundament / The Foundation, closing with a table of AEGIS's philosophy against the Foundation's; no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (92 lines for `an-introduction-to-the-world-o`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A guide for new readers: write „the world introduction presents …“; it is a reader's guide, deciding nothing. Quote the English as written; cut before straight quotes and bold marks. The source's pronouns for Kael stay inside quotations only.

## Pages — document 358, `an-introduction-to-the-world-of-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L13, L23, L25, L45, L49, L51, … (14 lines). central (3–6): its primary objective to create and maintain Coherence (L25); Kael to it a system error, not a person in pain (L25); a kind of artificial god (L51); emerging from the Nichts Rauschen, its existence a defence against formless entropy (L55); its flaw the Paradox of Misaligned Coherence, structurally blind to subjective experience, perverse instantiation (L59); order imposed from the top down (L86).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L13, L19, L21, L25, L29, L31, … (16 lines). central (3–6): composed of different personality parts, a complex adaptive system fighting for survival (L21); structured by TSDP (L35); the goal functional multiplicity, inner harmony among all parts (L45); the integrated self as a living Gödel sentence for AEGIS (L45); reaching the Foundation only through the work of psychological integration (L73).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence (see below).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L40. minor (1–3): the ANP example Lex, relying on logic and analysis to control the environment (L40).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L55. minor (1–3): the primordial, chaotic void called the Nichts Rauschen from which AEGIS emerged (L55).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L41. minor (1–3): the EP example Nyx, embodying the system's protective rage (L41).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L35. minor (1–3): Kael's structure according to the Tertiary Theory of Structural Dissociation (TSDP) (L35); the ANP/EP division (L40, L41).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `alex`: `ontological exploit` (near `alex`). occurrence: `ontological exploit` is the guide's phrase for Kael's integrated self, read on kael, not alex; `Kohärenz Protokoll` is the title.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: `ontological exploit` is the guide's phrase for Kael's integrated self, read on kael, not alex; `Kohärenz Protokoll` is the title.


**Pages not read:** `kohaerenz` (L11 the title) — an occurrence.

**Record entries:** none.

**Not promoted:** The Foundation as an English name, Existence Through Negation, the table labels, Gnosis and Episteme, Perverse Instantiation, the lens concepts.

**One reader**: aegis, kael, lex, nichts-rauschen, nyx, tsdp.

**Chapter readings**: none.
