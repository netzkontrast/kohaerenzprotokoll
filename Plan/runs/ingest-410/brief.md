# Brief — readings from document 409 (step 6)

1 document, one reader, one batch: `ingest-410`. Files go to `Plan/runs/ingest-410/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 409 | `primzahlen-als-metapher-in-kohaerenz-protokoll` | 2025-04-25 | „the prime-number report“ (an unsigned German evaluation, „Primzahlen als Metapher in „Kohärenz Protokoll““) | evaluates prime numbers as a metaphor system for the novel against the core elements an analysis brief gives (AEGIS, the Monstergruppe M, Kael and Juna, Moonshine, the core conflict), maps properties onto them in a table, and ends in a conditional recommendation (L215); a proposal, no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (286 lines for `primzahlen-als-metapher-in-koh`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An evaluation of a proposed metaphor: write „the prime-number report gives as background …“ for the core elements it restates from its brief (L21–L26), and „it proposes mapping …“ for its table (L85–L100); neither is the novel. Quote the German as written; cut before straight and nested quotes, bold markers and glued footnote digits. No gendered pronoun for Kael or Juna — use the names. Never write a real person's name; describe a theorem or conjecture without one.

## Pages — document 409, `primzahlen-als-metapher-in-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L23, L25, L44, L49, L69, L74, … (28 lines). minor (1–3): as background, „Eine fragile Künstliche Intelligenz, deren Existenz durch Negation definiert ist“, striving for stability through analysis and control, a reductionist approach (L23); the core conflict of AEGIS's reductionist control against M's holistic coherence (L25); proposed mappings — AEGIS's axioms as 'prime', AEGIS trying to 'factorise' M and Kael, AEGIS failing when it treats unique entities as replaceable (L86, L89, L97).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L44. not read: an occurrence — emergence in the report's general sense (L44).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L24, L69, L85, L95, L98, L112, … (15 lines). minor (1–3): as background, Juna with Kael a manifestation of M's coherence, the bond of the two „Moonshine“, non-local and sub-protocol (L24); the bond of Kael and Juna analogous to twin primes, two distinct, irreducible entities in a rare, close relation (L98).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L24, L54, L69, L74, L85, L89, … (22 lines). minor (1–3): as background, Kael and Juna as specific, potentially emergent manifestations of M's coherence, called „Baby-Monster“ (L24); proposed mappings — Kael and Juna as unique, irreplaceable 'prime' identities (L95), the bond of Kael and Juna analogous to twin primes (L98), the nature of M and Kael hard for AEGIS to analyse (L100).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L88, L93. minor (1–3): named only with the Potentialmeer in the proposed mappings (L88, L93).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — the title (L11).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L88, L93, L181. minor (1–3): a proposed mapping: certain rules „im Potentialmeer/Kernwelten“ absolute and unbreakable, 'prime' (L88); fundamental truths thinly scattered in the chaotic Potentialmeer (L93).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebenen` alone on L39. not read: an occurrence — levels of reality in the general sense (L39).
- **`rsa`** (minor, 1–4): the census's surfaces — `RSA` L73, L74, L124, L280, L281, L282, … (9 lines). not read: an occurrence — RSA the cryptosystem (L73), not the novel's Rekursive semantische Autogenese.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `moonshine-link`: `Moonshine` (near `moonshinelink`). decided with the pages above: `M/Kael/Juna` and `Kael/Juna` read on kael and juna; `Moonshine` the bond of Kael and Juna, read on moonshine-link; `Potentialmeer / Kernwelten` read on both pages; `Twin Primes` the report's mathematics.


**Pages beyond the draft:**
- **`moonshine-link`** (minor, 1–2): as background, the connection of Kael and Juna „als emergentes Phänomen namens“ Moonshine, non-local and sub-protocol (L24); Moonshine possibly like the rarest primes (L99).

**Record entries:** none.

**Pages not read:** rsa, emergenz, kohaerenz, realitaetsebenen — occurrences.

**Not promoted:** Monstergruppe (M), Baby-Monster, Kernkonflikt, Simplicity, Complexity, Kernlogik, Fehlklassifikation, Primzahlzwillinge, and the mathematical concepts.

**One reader**: aegis, kael, juna, potentialmeer, kern-welten, moonshine-link.

**Chapter readings**: none — the document names no chapter.
