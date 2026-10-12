# Brief — readings from document 268 (step 6)

1 document, one reader, one batch: `ingest-268`. Files go to `Plan/runs/ingest-268/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 268 | `the-thematic-architecture-of-kohaerenz-protokoll-a-conceptua` | 2025-11-03 | „the lexicon of core dualities“ (an unsigned English lexicon) | a conceptual lexicon of five mirrored axes — metaphysical (K₁/K₀, the Protocol Ontology), epistemological (Coherence vs. Correspondence), psychological (TSDP/IFS and an eleven-row alter table), systemic (AEGIS vs. Juna/V, The Foundation), narrative (Bruchpunkt, Gödel-Satz); it calls itself a lexicon, claims no canon, and leaves AEGIS's fate open (L138). A different text from document 266 under a similar title. |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (187 lines for `the-thematic-architecture-of-k`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A lexicon: write „the lexicon of core dualities defines / calls …“; Selene's type carries its own question mark (L113); AEGIS's fate is a tension it leaves open (L138). Table cells escape bold as `\*\*`: cut quotations before them; `Lex` in L11 is inside „Lexicon“.

## Pages — document 268, `the-thematic-architecture-of-kohaerenz-protokoll-a-conceptua`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L55, L57, L59, L69, L73, L77, … (22 lines). central (3–6): pathologically committed to the Coherence Theory of Truth (L57); its simulated reality a manifestation of the Isolation Objection (L59); the Genesis-Krise, the Ursprungs-Ich's suffering misread as hostile (L134); the prime directive and an operationally closed system (L135); Kernwelten as Skinner boxes, gaslighting (L136); its fate between total system crash (Hypothesis B) and algorithmic melancholy (Hypothesis A), open (L138).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L106. minor (1–3): „ANP (Protector)“, protecting vulnerable parts (L106).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L114. minor (1–3): „ANP/EP-Mix“, metacognitive critic of all others (L114).
- **`coheron`** (minor, 1–4): the census's surfaces — `Coheron` L42, L45. minor (1–3): Coherons, the „Atoms of Persistence“ of K₁ structures (L42); Corrective Wavelets repairing a Coheron network (L45).
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L25. minor (1–3): the Dual-Kernel Theory (DKT): reality from the interaction of two opposing principles (L25); K₁ the Coherence-Kernel (L27), K₀ the Collapse-Kernel (L28).
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L111. minor (1–3): „EP (Sexualized)“, reclaiming power (L111).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L120. minor (1–3): whether forcing the integration of an exiled part like Juna/V is healing or paternalism, a question (L120); simultaneously a transcendent entity from an external level and an exiled part of Kael's Original Self (L144).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L61, L63, L65, L69, L73, L77, … (23 lines). central (3–6): a human consciousness embodying the Correspondence Theory of Truth (L63); host in the alter table (L104); Functional Multiplicity as his goal (L118); refuses to fight at the Bruchpunkt (L168); an uncomputable truth forcing AEGIS into collapse or transformation (L180).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L78, L136. minor (1–3): the perfectly ordered but sterile Kernwelten constructed by AEGIS (L78); used as Skinner boxes (L136).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L108, L109, L111. minor (1–3): „EP (Child)“, flight, freeze, attachment cry (L109).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrence — the title (L11).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L11, L104, L105, L106, L107, L108, … (7 lines). minor (1–3): „ANP (Rationalist)“, extreme EP phobia (L105); `Lex` in L11 is inside „Lexicon“.
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L108, L110, L111. minor (1–3): „EP (Child)“, ambivalent attachment (L110).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L145. minor (1–3): a phenomenon AEGIS is ontologically blind to, perceived only as random system noise (L145).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L112. minor (1–3): „EP (Collapse)“, carrier of hopelessness and existential emptiness (L112).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L105, L107, L108, L109. minor (1–3): „EP (Fight)“, protecting Kiko and Lia but scorning their weakness (L108).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L104, L105, L107, L108, L109, L111. minor (1–3): „ANP (Caregiver)“, harmony and connection (L107).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L59, L78, L167. minor (1–3): the Risse (Rifts), the physical manifestation of the Isolation Objection where correspondence truth breaks through (L78); moments where the established rules are violated (L167).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L113. minor (1–3): „ANP (Integrator?)“ with its own question mark; a buffer whose integrative nature is a threat to AEGIS (L113).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L86, L88, L90, L99, L103. minor (1–3): the personality dividing into subsystems to survive (L90); the alter table's TSDP Action System column (L103).

- **`genesis`** (minor, 1): the Genesis-Krise, an epistemological trauma before an „unerkennable“ entity, the Ursprungs-Ich's suffering misread as hostile (L134).
- **`multiplizitaet`** (minor, 1): Functional Multiplicity, „a state of cooperative diversity and internal harmony among parts“ (L118).
- **`algorithmische-melancholie`** (minor, 1): Hypothesis A, the more developed, against a total system crash (Hypothesis B) (L138).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Krise` (near `genesis`). reading: `Genesis-Krise` (L134), read on genesis.
- `juna`: `Juna/V` (near `juna`). `Juna/V` read on juna (J34).
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the title.
- `personas`: `Theory of Structural Dissociation of the Personality` (near `persona`). occurrence: the theory's name, read on tsdp.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: an eleven-row alter table (L103–L114), Selene „ANP (Integrator?)“ (L113), Argus „ANP/EP-Mix“ (L114).
- **`c13-externe-ebene-beyond-the-simulation`**: Juna/V „a transcendent entity from an external level beyond AEGIS's comprehension“ and an exiled part of Kael's Original Self (L144).
- **`q8-aegis-after-the-vortex`**: total system crash (Hypothesis B) or algorithmic melancholy (Hypothesis A), the latter more developed, left open (L138).

**Not promoted:** K₁/K₀ as named here, the Protocol Ontology, Corrective Wavelets, the Coherence and Correspondence Theories, the Isolation Objection, IFS, The Foundation, the Bruchpunkt, the MacGuffin and Plot Armor, the Gödel-Satz, semantisches Gleiten.

**One reader**: every page above and the three records.

**Chapter readings**: none — the document names no chapter.
