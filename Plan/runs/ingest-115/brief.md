# Brief — readings from document 115 (step 6)

1 document, one reader, one batch: `ingest-115`. Files go to `Plan/runs/ingest-115/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 115 | `roman-outline-stilmittel-perspektiven-umsetzung` | 2026-02-23 | „the drafting compendium“ (titled `Narratologisches Kompendium und systemische Architekturen: Ein Ausformulierungsleitfaden für das „Kohärenz Protokoll“`) | a German guide of 2026-02-23 for writing out the outline, the same day and reference list as document 112: it reports the author's documents (references 1–7 and others, numbers glued on) and instructs — three entropies and Landauer (L19–L37), the Dual Kernel Theory K1/K0 as two prose styles (L39–L61), the Genesis as the model of the switch (L63–L77), IFS parts seated in KW1–KW3 (L79–L119), Architectural Storytelling and the Uncanny Valley (L121–L143), the arc in dramatic phases (L145–L166). It calls its closing points „verbindliche Richtlinien“ (L172) |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (215 lines for `roman-outline-stilmittel-persp`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A drafting guide: two voices kept apart. What it **reports** of the author's documents (a reference number on the line) is written „the drafting compendium reports …“; what it **instructs** („muss“, „Anweisung zur Ausformulierung“, „Stilistische Vorgabe“, the closing „verbindliche Richtlinien“) is written „the compendium instructs / recommends …“ — never as the novel's fact. Kael is male. Its K1/K0 kernels are the DKT's, applied to style.

## Pages — document 115, `roman-outline-stilmittel-perspektiven-umsetzung`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L21, L25, L26, L27, L33, … (21 lines). central (3–5): the expansion „Autonomous Entropic Gatekeeper for Integrity Systems“ (L21), defined by its fight against entropic decay; it reduces the Überwelt to predictable states and classifies emotion, qualia and Juna as noise (L26); its erasures make „digitale Abwärme“ that manifests as the Risse — the harder it acts, the less stable the world (L33); Ashby's law, AEGIS lacks requisite variety (L37); the Genesis switch from K0 to K1 (L65, L75–L77).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L81, L95, L103, L111, L163, L165. minor (1–2): the Alters seated by IFS role: Limina, Index, Eos (KW1, L95); Echo, Oblivion, Silas (KW2, L103); Nox, Praetor (KW3, L111); the Alter System MOC planning who fronts when (L154).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L112, L153, L176. minor (1): KW3's Guardian, „Das paranoide Immunsystem der Simulation“ (L112).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L81. minor (1): the Kern-Welten as the externalisation of Kael's DID (L81).
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L41. minor (1–2): the Dual Kernel Theory with the ARCHON Runtime Stack recommended to split the narrative reality (L41); the table of K1 and K0 modes (L59–L61).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L15. occurrence unless more: `Emergenz` at L15 and L164 (the Ly-Welt's chaos) — read only if the line says more.
- **`entropie`** (central, 3–12 quotations): the census's surfaces — `Entropie` L19, L21, L23, L25, L26, L27, … (13 lines). central (2–4): the „triadische Struktur der Entropie“ — thermodynamic, information-theoretic, psychological (L23–L27); Landauer (L31); entropy as „der primäre konzeptuelle Antagonist“ (L21).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L63. minor (1): the foreword and the chapter „Genesis der Existenz“ as the blueprint of the K0/K1 conflict (L63–L65), the autopoietic „Klick“ (L73–L77).
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L107, L113, L163, L176. minor (1): KW3, „Eine klaustrophobische Architektur der Angst“ (L113).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L47, L163, L176, L188, L204. minor (1): the confrontations with Guardians in each Kern-Welt as confrontations with an IFS part (L176).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L15, L26, L33, L51, L61, L115, … (12 lines). central (2–4): classified as noise (L26); the Self of IFS, tied to a reality beyond the simulation, which AEGIS and LogOS cannot compute — „entropischer Kontaminant“ (L117); K0 with the Risse (L61); AEGIS's attempt to erase her by partitioning (L163).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L27, L33, L37, L51, L61, … (18 lines). central (3–5): begins as the ANP or Host with amnesia (L87), takes the Risse as the Konstrukt-Stadt's programming faults (L89); the arc in phases (L161–L166) — Universal Reboot, Risse, falling into the Resonanz-Landschaft and Grenzfeste, the Gödel knot, functional multiplicity as „Gärtner“, the Wir-Geflecht; K0 scenes in his Deep POV (L53, L61).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kern-Welten` L33, L81, L176, L188, L204; `Kern-Welt` L33, L81, L97, L105, L113, L176, … (8 lines). minor (1–2): the Kern-Welten as the externalisation of Kael's DID, AEGIS's attempt to lock the Alters into closed simulations (L81); the Risse in them (L33).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: the title and the protocol's name (L11, L15) — occurrence (J9).
- **`kohaerenz-kernel`** (minor, 1–4): the census's surfaces — `Kohärenz-Kernel` L43. minor (1): K1, the reversible, phase-coherent computation, order and Hard Canon — when AEGIS rules (L45), written clinical and minimal (L47).
- **`kollaps-kernel`** (minor, 1–4): the census's surfaces — `Kollaps-Kernel` L49. minor (1): K0, irreversible entropy, trauma, qualia, when Kael's psyche breaks through the Risse or Juna intervenes (L51), written in Deep POV (L53).
- **`komponente-734`** (minor, 1–4): the census's surfaces — `Komponente 734` L77. minor (1): at the Genesis switch the pronoun „Ich“ is replaced by „das System“ or „Komponente 734“ (L77), reported from reference 5.
- **`konstrukt-stadt`** (central, 3–12 quotations): the census's surfaces — `Konstrukt-Stadt` L47, L60, L89, L91, L97, L123, … (10 lines). central (2–3): KW1 of the Manager parts, „euklidischer Geometrie, kausalem Determinismus“ (L97); K1 scenes there in a clinical style (L47, L60); Architectural Storytelling for the first chapter (L123–L130); its constructs, the Therapeut-Konstrukt and the „Normale Nachbar“ (L141).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L47, L60, L96, L117, L174. minor (1–2): KW1's Guardian, „Die Personifikation von Logik und Systemarchitektur“ with a blind spot for the irrational (L96); K1 scenes from LogOS's perspective (L47).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L104. minor (1): KW2's Guardian, empathic but caught in the past, treating trauma as data (L104).
- **`moeglichkeits-garten`** (minor, 1–4): the census's surfaces — `Möglichkeits-Garten` L165. minor (1): Kael as „Gärtner“ in the Möglichkeits-Garten (L165); the Ly-Welt's chaos he must face at the climax (L164).
- **`mosaik-herz`** (minor, 1–4): the census's surfaces — `Mosaik-Herz` L166. minor (1): the Mosaik-Herz beating in an unstable, living balance against AEGIS (L166).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L37. minor (1): Kael applies „funktionalen Multiplizität“, synchronising the Alters (L165).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L25. minor (1): thermodynamic entropy as the „Nichts Rauschen“ in the novel (L25).
- **`oblivion`** (minor, 1–4): the census's surfaces — `Oblivion` L103. minor (1): KW2, „im Freeze-Zustand eingefrorener Trauma-Halter“ (L103).
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L99, L105, L163. minor (1): KW2, a non-linear dream world whose weather answers suppressed emotions, grief as rain or ruins (L105).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L33, L51, L61, L89, L162, L163, … (7 lines). minor (2): the Risse as the digital waste heat of AEGIS's erasures (L33); Kael first reads his flashbacks as the Konstrukt-Stadt's Risse (L89); the inciting incident (L162); the closing instruction to render them phenomenologically (L177).
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L103. minor (1): KW2's Exiles include Silas „(Caretaker)“ (L103).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L26. minor (1): AEGIS reduces the Überwelt to predictable, compressible states (L26).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). occurrence: `Guardian` is the world guardians.
- `genesis`: `Genesis der Existenz` (near `genesis`). a reading — on genesis above.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the title (J9).
- `multiplizitaet`: `funktionalen Multiplizität` (near `multiplizitat`). a reading — L165, on the page above.
- `residual-echos`: `Echo` (near `residualechos`). occurrence: `Echo` a child Alter (L103, L163).


**Record entries** (one file each):

- **`c1-aegis-expansion`**: position 1 again, „Autonomous Entropic Gatekeeper for Integrity Systems“ (L21).
- **`c11-landauer-warmth-or-cold-ozone`**: the Landauer heat, „digitale Abwärme“, manifesting as the Risse (L33) — an instruction to the author, no chapter, no ozone; the drone welding a crack (L130). Record only if it adds to the entries of documents 111 and 112; else no file, and say why.
- **`q3-how-many-kern-welten-and-alters`**: the Alters seated in three worlds by IFS role — KW1 Limina, Index, Eos; KW2 Echo, Oblivion, Silas; KW3 Nox, Praetor (L95, L103, L111); Juna as the Self (L117); KW4 named only as the Möglichkeits-Garten and Ly-Welt (L164–L165). Dated 2026-02-23, before the author's answers.
- **`q5-guardians-and-kern-welten`**: LogOS–KW1, Mnemosyne–KW2, Cerberus–KW3 (L96, L104, L112); no Guardian for KW4.
- **`q7-what-734-names`**: „Komponente 734“ replaces the pronoun „Ich“ at AEGIS's autopoietic click (L77), reported from the Genesis (reference 5).

**Not promoted:** the three entropies, Landauer, Ashby's law, IFS categories, Deep POV, Third-Person Objective, Uncanny Valley, Architectural Storytelling, Maps of Content (MOCs) — borrowed tools; ARCHON Runtime Stack, System Architect, Sensory Drafter; Limina, Index, Eos, Echo, Nox, Praetor; the Therapeut-Konstrukt and the „Normale Nachbar“; Risiko-Assessment-Marker.

**Split into two readers, one after the other:**
- Reader 1: aegis, entropie, juna, dkt, kohaerenz-kernel, kollaps-kernel, komponente-734, genesis, nichts-rauschen, ueberwelt, risse, did, emergenz, and the entries c1, c11, q7.
- Reader 2: kael, konstrukt-stadt, kern-welten, alters, guardians, logos, mnemosyne, cerberus, resonanz-landschaft, grenzfeste, moeglichkeits-garten, mosaik-herz, multiplizitaet, oblivion, silas, and the entries q3, q5.
