# Brief — readings from document 266 (step 6)

1 document, one reader, one batch: `ingest-266`. Files go to `Plan/runs/ingest-266/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 266 | `thematic-architecture-of-kohaerenz-protokoll-a-conceptual-le` | 2025-11-03 | „the conceptual lexicon“ (an unsigned English lexicon) | a conceptual lexicon in six sections — philosophy, psychology, computer science, narrative form, physics and mathematics — defining the novel's terms with German names: Das Fundament, Die Leere / Das Nichts Rauschen, the dialetheic geist, the TSDP roster, AEGIS's architecture, the Dramatica throughlines, the Moonshine-Link; it calls itself a lexicon and claims no canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (206 lines for `thematic-architecture-of-kohae`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A lexicon that defines: write „the conceptual lexicon defines / calls …“; Qualia (L50–L53) is a question it calls unresolved, so say so. Glosses are glued to German names without a space (`Das Fundament(The Foundation)`) and table cells escape bold as `\*\*`: cut quotations before them.

## Pages — document 266, `thematic-architecture-of-kohaerenz-protokoll-a-conceptual-le`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L24, L26, L38, L42, L50, … (34 lines). central (3–6): AEGIS reads Kael's paradox like a spellchecker reads a typo (L26); operates only on Episteme (L38); registers Kael's state as an unclassifiable anomaly (L42); whether its Ursprungs-Ich had Qualia, „The central, unresolved question“ (L50–L53); an externalized introject of an abuser (L90); operationally closed, ontologically blind (L118–L119); its genesis an information-theoretic trauma before the Nichts Rauschen, its directive Entropic Management (L125–L126); three layers and a split-brain (L132–L134); the Paradoxon der Fehlausgerichteten Kohärenz (L140).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L77. minor (1–3): „Alex“ (Protector) among the ANPs (L77).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L76. minor (1–3): „Alters classified as“ Verfolger, misguided protectors (L102); the roster's column „Examples (Alters)“ (L76) only if it adds.
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L77. minor (1–3): „Argus“ (Observer) among the ANPs (L77).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L70. minor (1–3): Tertiäre Strukturelle Dissoziation, „which corresponds to Dissociative Identity Disorder“ (L70).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L125. minor (1–3): AEGIS's genesis as an „information-theoretic trauma“, a defensive reaction to the Nichts Rauschen (L125).
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L78. minor (1–3): „Isabelle“ (Submit/Attachment Cry) among the EPs (L78).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L161. minor (1–3): Juna/V the Impact Character, through non-local resonance (L161); the Moonshine-Link to Kael (L190).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L24, L26, L38, L42, L60, … (27 lines). central (3–6): access to Das Fundament not a Deus ex Machina but earned (L24); the dialetheic geist (L26); becomes a living Gödel-Satz (L42); functional multiplicity as a rhizomatic network (L60), not fusion (L98); TSDP, tertiary structural dissociation (L70); host in the roster (L77); the Gärtner (L104–L106); Main Character (L160).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L26. minor (1–3): KW2 and KW4 said to operate on dialetheic principles (L26).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L78. minor (1–3): „Kiko“ (Freeze) among the EPs (L78).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrence — the title (L11).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L11, L77. minor (1–3): „Lex“ (Analyst) among the ANPs (L77); `Lex` in L11 is inside „Lexicon“, not the alter.
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L78. minor (1–3): „Lia“ (Flight) among the EPs (L78).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L190. minor (1–3): a non-local, sub-protocollar „ontological exploit“ outside AEGIS's sensory apparatus (L190); its synthesis (L191 onward) only if it adds.
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L78. minor (1–3): „Moros“ (Collapse) among the EPs (L78).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Das Nichts Rauschen` L25. central (3–6): „Die Leere / Das Nichts Rauschen“ glossed as Potentialmeer, an active aggressive plenum of undifferentiated potential, acoustic pressure without sound (L25); the absolute absence of processable information AEGIS confronted at its genesis (L125); The Void framed by Cosmic Horror (L178).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L78. minor (1–3): „Nyx“ (Fight) among the EPs (L78).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L25. minor (1–3): the high-entropy „Potentialmeer“ (Potential Sea) of pure informational chaos, the unmanifested possibility structure emerges from (L25).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L77. minor (1–3): „Rhys“ (Caretaker) among the ANPs (L77).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L68, L70, L72. minor (1–3): Kael's mind modelled on TSDP, tertiary structural dissociation (L70); the core TSDP model table of ANPs and EPs (L72–L78).

- **`multiplizitaet`** (minor, 1–2): functional multiplicity as „a pluralistic, de-centralized, and rhizomatic network“ (L60); „explicitly not fusion“, a collective „We“ (L98).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `juna`: `Juna/V` (near `juna`), `Kael ↔ Juna/V relationship` (near `juna`). `Juna/V` read on juna (J34); `Kael ↔ Juna/V relationship` the Dramatica throughline, read on juna only through the Moonshine-Link line.
- `kohaerenz`: `Paradoxon der Fehlausgerichteten Kohärenz` (near `koharenz`). occurrence: `Paradoxon der Fehlausgerichteten Kohärenz` is AEGIS's flaw, read on aegis.
- `personas`: `Theory of Structural Dissociation of the Personality` (near `persona`). occurrence: the theory's name, read on tsdp.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: the core TSDP model lists ten names — five ANPs (L77) and five EPs (L78), without Selene; record the count as the table gives it, as an example column („Examples (Alters)“, L76).

**Not promoted:** Das Fundament, Dialetheism and the dialetheic geist, Episteme/Gnosis, the Gödel-Satz, Qualia, the externalized introject, the Gärtner, Entropic Management, the three layers, the split-brain, the Paradoxon der Fehlausgerichteten Kohärenz, the Dramatica throughlines, the genre blend.

**One reader**: every page above and the record q3.

**Chapter readings**: none — the document names no chapter.
