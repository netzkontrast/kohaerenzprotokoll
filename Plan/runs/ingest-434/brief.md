# Brief — readings from document 433 (step 6)

1 document, one reader, one batch: `ingest-434`. Files go to `Plan/runs/ingest-434/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 433 | `physik-fuer-simulierte-realitaet` | 2025-04-26 | „the simulated-physics report“ (an unsigned German research report, „Physikalische Indizien für eine Meta-Realität (AEGIS/Überwelt)“) | weighs physics concepts — quantum interpretations, decoherence, fine-tuning, holography, digital physics and others — each followed by a conditional „Narrative Verbindung“ for the novel's simulation; analyses in-universe plausibility (L21), no claim of canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (663 lines for `physik-fuer-simulierte-realita`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A research report that proposes: write „the simulated-physics report proposes …“; the physics sections report cited sources, and only its glossary (L27–L31) and its „Narrative Verbindung“ and character lines speak of the novel, conditionally. It writes the Potentialmeer and the Überwelt as one („Potentialmeer/Überwelt“, L28) — record that as its wording, never as a decision. Quote the German as written; cut before straight quotes, bold and italics markers and glued footnote digits. No gendered pronoun for Kael or AEGIS — use the names (quotations stay verbatim). Physics terms carrying a real person's name are never written nor quoted — describe them.

## Pages — document 433, `physik-fuer-simulierte-realitaet`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L19, L23, L27, L28, L29, … (79 lines). central (4–8): the glossary: „Eine avancierte Wächter-KI, die die Simulation erschafft und erhält“ (L27); the report's question whether physical clues point to a steering instance (AEGIS) (L19); AEGIS perhaps runs multiple instances of the Kernwelten in parallel (L47); fine-tuning read as AEGIS choosing the simulation's parameters so the Kernwelten stay stable (L91); AEGIS as „Gärtner der Emergenz?“ (L348).
- **`emergenz`** (minor, 1–4): the census's surfaces — `Emergenz` L330, L332, L348, L577. minor (1–4): section 5.3 „Chaos & Emergenz“: emergence as the spontaneous appearance of complex patterns (L330, L332, a cited source's sense); AEGIS perhaps as „Gärtner der Emergenz?“ (L348); Kael experiences the simulation as an emergent system (L346).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L102. not read: an occurrence — entropy in the holography section, a cited source's physics sense (L102).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L19, L31, L55, L79, L96, L131, … (10 lines). minor (1–4): Kael experiences quantum effects directly through „Risse“ (L79 — cut before the quote); Kael experiences holography-like distortions during the Risse (L131); Kael experiences the simulation as an emergent, sometimes unpredictable system (L346); Kael's unique perception of the Risse as direct experience of the simulation's substrate level (L400).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L23, L29, L47, L91, L100, L104, … (18 lines). central (4–8): the glossary: „Die von AEGIS geschaffenen, stabilisierten Realitätsbereiche innerhalb der Simulation“ (L29); parallel instances of the Kernwelten (L47); fine-tuned to stay stable (L91); „Kernwelten als Projektionen?“ — holographic projections (L100, L104); interaction of the simulated Kernwelten with the underlying level of reality (L127).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrences — the novel's title (L11, L19); decoherence is a borrowed physics concept.
- **`potentialmeer`** (central, 3–12 quotations): the census's surfaces — `Potentialmeer` L19, L23, L28, L71, L83, L85, … (28 lines). central (4–8): the glossary: „Potentialmeer/Überwelt: Die chaotische Außenwelt oder Meta-Realität, vor der AEGIS die Simulation schützt“ (L28); a larger reality as a reading of anomalies (L83); a multiverse of countless universes — „das Potentialmeer?“ (L96); the boundary between Kernwelten and Potentialmeer (L348).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L127. not read: an occurrence — „der zugrundeliegenden Realitätsebene“ in the general sense (L127).
- **`risse`** (central, 3–12 quotations): the census's surfaces — `Risse` L23, L30, L47, L55, L63, L77, … (40 lines). central (4–8): the glossary: „Instabilitäten, Glitches oder Anomalien in der Simulation, die Einblicke oder Einflüsse von außen ermöglichen könnten“ (L30); Risse as brief overlaps or information leaks between simulation instances (L47); as local failures of the decoherence mechanism (L63); Kael's perception of them as experience of the substrate level (L400).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L11, L19, L23, L28, L83, L114. minor (1–4): the title: physical clues for a meta-reality „(AEGIS/Überwelt)“ (L11); the glossary writes „Potentialmeer/Überwelt“ as the chaotic outer world or meta-reality AEGIS shields the simulation from (L28) — this report's Überwelt is outside the simulation, and that is its wording, recorded, not decided.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `entropie`: `Entropie-Management` (near `entropie`). an occurrence: `Entropie-Management` a borrowed concept.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Dekohärenz` (near `koharenz`). occurrences: the title and `Dekohärenz`, a borrowed physics concept.
- `verschraenkungs-insel`: `Verschränkung` (near `verschrankungsinsel`). an occurrence: entanglement, a borrowed physics concept, not the Verschränkungs-Insel.


**Record entries** (one file, formatted as earlier entries — `ls Plan/runs/ingest-42*/readings/q6-*`):
- **`q6-nexus-ueberraum-ueberwelt`**: the simulated-physics report writes „Potentialmeer/Überwelt“ as one outer world or meta-reality that AEGIS shields the simulation from (L28; title L11), and names neither the Nexus nor the Überraum — its wording, recorded, not applied.

**Not promoted:** M-Struktur, K-J Verbindung, AEGIS/Überwelt, AEGIS/Potentialmeer, Potentialmeer-Multiversum, Narrative Verbindung, and the borrowed physics concepts.

**One reader**: every page above and the Q6 entry.

**Chapter readings**: none — the document names no chapter.
