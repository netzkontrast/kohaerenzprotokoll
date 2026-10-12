# Brief — readings from document 364 (step 6)

1 document, one reader, one batch: `ingest-365`. Files go to `Plan/runs/ingest-365/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 364 | `protokoll-ontologie-roman-konzeptentwicklung` | 2025-11-03 | „the Protokoll-Ontologie exposé“ (an unsigned German concept exposé, a „World Bible“) | defines a Protokoll-Ontologie — Kohärenz K₁ against Kollaps K₀, Overhead, Corrective Wavelets, the Korrespondenz-Check — on the Dual Kernel Theory, and applies it to world, magic system, characters, the antagonist AEGIS and a five-step plot cycle; it calls its glossary „definitiv“, recorded, not applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (246 lines for `protokoll-ontologie-roman-konz`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A concept exposé: write „the Protokoll-Ontologie exposé defines / proposes …“; its definitions and its „definitives Glossar“ are its own claims, deciding nothing. Name no real researcher it cites. Cut before inner quotation marks and glued reference digits.

## Pages — document 364, `protokoll-ontologie-roman-konzeptentwicklung`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L210, L241. minor (1–3): AEGIS's narrative as a perfect template, its defining protocol a closed logical loop unable to process external truths (L210); the antagonist not defined as malicious by nature (L208).
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Cache-Kohärenz` alone on L97. minor (1–3): cache-coherence protocols from computer architecture as the technical analogue of the Overhead of persistence (L78); the glossary table's source column (L97).
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L44. minor (1–3): Kohärenz and Kollaps based on a speculative framework named the Dual Kernel Theory (L44).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L47. not read: L47 uses entropy in the borrowed physical sense of the kernels' account.
- **`kael`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kael` alone on L156. minor (1–3): System Kael as a case study, a fragmented identity as a system of conflicting sub-protocols (L156) — what the line says.
- **`kohaerenz`** (central, 3–12 quotations): the census's surfaces — `Kohärenz` L38, L42, L46, L51, L78, L97, … (18 lines). central (3–6): Kohärenz as the structure-preserving, information-preserving principle against Kollaps, not a moral conflict (L42); existence as continuous execution of an information-preserving protocol (L24); the central dogma, no static things, only protocols (L59); persistence as an economic calculation (L82); coherent and decoherent zones of the world (L122).
- **`kollaps-kernel`** (minor, 1–4): the census's surfaces — `Kollaps-Kernel` L51. minor (1–3): the Kollaps-Kernel equated with quantum decoherence (L51).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L122; `Glitches` L122. minor (1–3): decoherent zones as unstable, chaotic regions, with Risse and Glitches (L122).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cache-kohaerenz`: `Cache-Kohärenz-Protokolle` (near `cachekoharenz`). occurrence: the exposé's generic `Protokoll` and `Validierung`, not the named protocols; `Cache-Kohärenz-Protokolle` is read on cache-kohaerenz; `System Kael` on kael.
- `entropie-resonanz`: `Protokoll` (near `entropieresonanzentropieresonanzprotokolleerp`), `Protokoll` (near `entropieresonanzprotokolle`). occurrence: the exposé's generic `Protokoll` and `Validierung`, not the named protocols; `Cache-Kohärenz-Protokolle` is read on cache-kohaerenz; `System Kael` on kael.
- `kael`: `System Kael` (near `kael`). occurrence: the exposé's generic `Protokoll` and `Validierung`, not the named protocols; `Cache-Kohärenz-Protokolle` is read on cache-kohaerenz; `System Kael` on kael.
- `nullpunkt-protokoll`: `Protokoll` (near `nullpunktprotokoll`). occurrence: the exposé's generic `Protokoll` and `Validierung`, not the named protocols; `Cache-Kohärenz-Protokolle` is read on cache-kohaerenz; `System Kael` on kael.
- `protokoll-v14`: `Protokoll` (near `protokollv14`). occurrence: the exposé's generic `Protokoll` and `Validierung`, not the named protocols; `Cache-Kohärenz-Protokolle` is read on cache-kohaerenz; `System Kael` on kael.
- `trennungsprotokoll`: `Protokoll` (near `trennungsprotokoll`). occurrence: the exposé's generic `Protokoll` and `Validierung`, not the named protocols; `Cache-Kohärenz-Protokolle` is read on cache-kohaerenz; `System Kael` on kael.
- `ztv`: `Validierung` (near `ztvvertrauenlosevalidierung`). occurrence: the exposé's generic `Protokoll` and `Validierung`, not the named protocols; `Cache-Kohärenz-Protokolle` is read on cache-kohaerenz; `System Kael` on kael.


**Record entries:** none.

**Not promoted:** Protokoll-Ontologie, Overhead, Corrective Wavelets, Korrespondenz-Check, Selbst-Protokoll, the archetypes, Validierungskrieg, the plot cycle, Kohärente and Dekohärente Zonen, Protokoll-Agenten; the borrowed concepts (systems theory, quantum decoherence, signal processing, Alternative Systems Objection).

**One reader**: aegis, cache-kohaerenz, dkt, kael, kohaerenz, kollaps-kernel, risse.

**Chapter readings**: none — the exposé names no chapter.
