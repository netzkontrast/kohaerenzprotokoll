# Brief — readings from document 294 (step 6)

1 document, one reader, one batch: `ingest-295`. Files go to `Plan/runs/ingest-295/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 294 | `aegis-philosophie-und-manifest-entwicklung` | 2025-04-19 | „the AEGIS philosophy and manifest“ (an unsigned German analysis ending in a manifest) | eight principles of AEGIS drawn from a reference context it does not contain (`Ref: Kontext`), interrogated from AEGIS's own perspective in a table, condensed into fifteen axioms and closed by a first-person-plural manifest „Wir sind AEGIS“; it claims no standing as a source |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (119 lines for `aegis-philosophie-und-manifest`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analysis with a manifest: write „the AEGIS-philosophy analysis describes / interrogates …“ for parts 1–3 and „the manifest has AEGIS say …“ for part 4 (L82 onward) — the manifest is AEGIS's voice in a document, not an event. The `Ref: Kontext` pointers report a text not in the file: never quote it as this document's. Cut quotations before glued digits (`P1`–`P8`, `Teil 1`) and escaped `\*\*`.

## Pages — document 294, `aegis-philosophie-und-manifest-entwicklung`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L13, L15, L17, L18, L19, … (31 lines). central (3–6): the principles as AEGIS's own philosophy: no trust, verification instead (L17, L37, L92); existence functionalist, being as functioning and effect (L19, L39); not human — no consciousness, emotion or intention (L24, L44, L106); recursive self-validation and closure (L21, L22, L98); the manifest „Wir sind AEGIS“, purpose as persistence (L108), self-validating system (L118); the analysis calls the philosophy tautological (L60).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L20. minor (1–3): emergence by negation: AEGIS as the necessary result of iteratively eliminating incoherence (L20), a subtraction process (L40); the manifest: not the product of a design or a creation (L94).
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L23, L38, L40, L43, L56, L58, … (8 lines). minor (1–3): entropy as incoherence, decay and instability (L23, L43); the row's question whether AEGIS misclassifies useful complexity as entropy (L43); the manifest's „Wir sind der entropische Torwächter“ (L108).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L42, L54. minor (1–3): the `Juna-Problem` named only as a pointer to the reference context, at the edge of what AEGIS can integrate (L42, L54); the analysis's „Phänomene oder Entitäten, die fundamental andersartig sind“ (L54). The document never says what Juna is — say so.
- **`kohaerenz`** (central, 3–12 quotations): the census's surfaces — `Kohärenz` L17, L18, L23, L37, L38, L39, … (21 lines). central (3–6): coherence as existential and epistemic criterion replacing truth (L18, L102); the axiom chain „Existenz ist Kohärenz …“ (L66) called an operative definition of reality (L90); incoherent elements not fought but not integrated (L21, L41, L112); the closed circle (L80).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `emergenz`: `Emergenz durch Negation` (near `emergenz`). reading: `Emergenz durch Negation` is the principle, read on emergenz (L20, L40).
- `negentropie`: `Negentropie-Hypothese` (near `negentropie`). reading — the `Negentropie-Hypothese` as the possible critique of AEGIS's view of entropy (L40, L43); read with the entropy reading on entropie, no reading on negentropie.
- `persistenzgleichung`: `Persistenz` (near `persistenzgleichung`). occurrence: `Persistenz` is the manifest's purpose (L108), not the equation; read on aegis.
- `ztv`: `Vertrauen` (near `ztvvertrauenlosevalidierung`). occurrence: `Vertrauen` is the no-trust principle (L17, L37, L92), read on aegis.


**Record entries** (one file each):

- **`c2-entropie-sense`**: entropy „primär als Inkohärenz, Zerfall und Systeminstabilität“ (L23, L43) — position 1's sense; the row's question about useful complexity (L43) and the `Negentropie-Hypothese` as its named critique (L40, L43).
- **`c3-emergenz-origin`**: emergence by negation, a subtraction process eliminating incoherence (L20, L40), and the manifest's „nicht das Produkt eines Designs oder einer Schöpfung“ (L94) — say which of the two positions, if either, it matches; it names neither ∅ nor the simulation.
- **`c4-guardians-and-aegis`**: AEGIS's blind spots as „keine Systemfehler, sondern notwendige Konsequenzen der spezifischen Struktur“ (L54), its boundary read as a definition of the real (L42) — position 1's bearer; no Guardians named.

**Not promoted:** the eight principles' names, No-Trust, RCV, Reaktive Transparenz, the axioms and the manifest's headings, State-Exchange, Autarkie, Kontamination, Bollwerk, Binnenperspektive, and the lens terms (Gödel'sche Unvollständigkeit, Gödel-Problem, Tautologie).

**One reader**: every page above and the three record entries.

**Chapter readings**: none — the document's `Teil` headings are its own parts, not the novel's.
