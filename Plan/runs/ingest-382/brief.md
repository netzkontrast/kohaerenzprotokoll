# Brief — readings from document 381 (step 6)

1 document, one reader, one batch: `ingest-382`. Files go to `Plan/runs/ingest-382/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 381 | `welcome-to-the-coherence-protocol-a-beginner-s-guide` | 2025-11-03 | „the beginner's guide“ (an unsigned English introduction) | a present-tense tour of the world for an „aspiring chronicler“: AEGIS and System Kael, the four Kernwelten KW1–KW4 with principle, atmosphere and somatic truth, the Risse, Juna/V and the Moonshine-Link, and the Protocol Ontology with K₁ and K₀; no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (136 lines for `welcome-to-the-coherence-proto`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An introduction: write „the beginner's guide presents / describes …“; deciding nothing. Quote the English as written; cut before escaped emphasis, table escapes and straight quotes. No gendered pronoun for Kael, the parts or Juna/V — use the names (quotations stay verbatim).

## Pages — document 381, `welcome-to-the-coherence-protocol-a-beginner-s-guide`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L23, L25, L27, L29, L30, L31, … (18 lines). central (3–6): a tragic antagonist (L27); born as a cluster of Ich-Fragmenten banding together against the Potentialmeer (L29); in the Genesis-Krise misinterpreting loneliness and longing as a hostile error, an algorithmic dismemberment (L30); mislabelling Kael's healing as entropy (L31); Coherence instead of Truth (L53, L54); ontologically blind to the Moonshine-Link (L115).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L80. minor (1–3): the hyper-vigilant protector parts like Alex and Nyx represented by KW3 (L80).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L86. central (3–6): Juna/V as the central mystery and catalyst (L103); a dual nature — a transcendent being from beyond AEGIS's simulation and an exiled part of the original unified self from which AEGIS and Kael were fragmented (L107); embodying the 6 Paraiyas (L109); a catalyst, not a saviour, giving gnosis (L117); KW4 most influenced by Juna/V (L86).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L23, L31, L33, L35, L37, … (22 lines). central (3–6): System Kael, a reality forged from one fractured mind (L15); a system of parts, Anteile, formed by trauma (L35); the journey to integration (L45); Coherence through Truth (L53, L54); Kael's body in each Kernwelt — a machine barely known, the dialetheic truth of trauma, physical armour, release (L70, L76, L82, L88).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L60, L62. central (3–6): the four Kernwelten (Core Worlds) as Psycho-Architectures, physical manifestations of Kael's states designed by AEGIS (L62); KW1 Logos-Prime, the Cage of Logic (L66–L70); KW2 Mnemosyne-Archipel, the Swamp of Memory (L72–L76); KW3 Cerberus-Labyrinth, the Fortress of Fear (L78–L82); KW4 Kairos-Potentialis, the Garden of Possibility, a ruin-garden (L84–L88).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L43, L95. minor (1–3): Kiko (the Terrified Child) among the key EPs (L43); a temporal glitch when Kiko is suppressed (L95).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. not read: an occurrence (see below).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L42, L68, L94. minor (1–3): Lex (the Rationalist) among the key ANPs (L42); KW1 representing the controlling ANPs like Lex (L68); Nyx clashing with Lex causing a physics glitch (L94).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L111, L113, L115. minor (1–3): the Moonshine-Link as a subtle, non-local resonance, a whisper in the code (L113); AEGIS ontologically blind to it, perceiving its effects as noise (L115); giving gnosis, not answers (L117).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L43, L80, L94. minor (1–3): Nyx (the Protector filled with rage) among the key EPs (L43); KW3's protectors like Alex and Nyx (L80); Nyx clashing with Lex causing a violent physics glitch (L94).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L29. minor (1–3): AEGIS born as a cluster of Ich-Fragmenten banding together against the chaotic Potentialmeer (Sea of Potentiality) (L29).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L42. minor (1–3): Rhys (the Caretaker) among the key ANPs (L42).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L90, L92. minor (1–3): the Risse (rifts or cracks) as moments where the psychological and physical layers intersect (L92); a violent physics glitch from a Fight response and a temporal glitch from a Freeze response (L94, L95).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L35. minor (1–3): System Kael's structure based on the clinical Theory of Structural Dissociation (TSDP), ANPs and EPs (L35, L42, L43).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). `System Kael` on kael; `Kernwelten (Core Worlds)` and the world names (`Logos-Prime`, `Mnemosyne-Archipel`, `Cerberus-Labyrinth`, `Kairos-Potentialis`) on kern-welten, occurrences on the Guardian pages; `Genesis-Krise` on aegis, genesis not read; `Juna/V` on juna; `Kohärenz Protokoll` the title; `ANPs` forms, not promoted.
- `genesis`: `Genesis-Krise` (near `genesis`). `System Kael` on kael; `Kernwelten (Core Worlds)` and the world names (`Logos-Prime`, `Mnemosyne-Archipel`, `Cerberus-Labyrinth`, `Kairos-Potentialis`) on kern-welten, occurrences on the Guardian pages; `Genesis-Krise` on aegis, genesis not read; `Juna/V` on juna; `Kohärenz Protokoll` the title; `ANPs` forms, not promoted.
- `juna`: `Juna/V` (near `juna`). `System Kael` on kael; `Kernwelten (Core Worlds)` and the world names (`Logos-Prime`, `Mnemosyne-Archipel`, `Cerberus-Labyrinth`, `Kairos-Potentialis`) on kern-welten, occurrences on the Guardian pages; `Genesis-Krise` on aegis, genesis not read; `Juna/V` on juna; `Kohärenz Protokoll` the title; `ANPs` forms, not promoted.
- `kairos`: `Kairos-Potentialis` (near `kairos`). `System Kael` on kael; `Kernwelten (Core Worlds)` and the world names (`Logos-Prime`, `Mnemosyne-Archipel`, `Cerberus-Labyrinth`, `Kairos-Potentialis`) on kern-welten, occurrences on the Guardian pages; `Genesis-Krise` on aegis, genesis not read; `Juna/V` on juna; `Kohärenz Protokoll` the title; `ANPs` forms, not promoted.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). `System Kael` on kael; `Kernwelten (Core Worlds)` and the world names (`Logos-Prime`, `Mnemosyne-Archipel`, `Cerberus-Labyrinth`, `Kairos-Potentialis`) on kern-welten, occurrences on the Guardian pages; `Genesis-Krise` on aegis, genesis not read; `Juna/V` on juna; `Kohärenz Protokoll` the title; `ANPs` forms, not promoted.
- `logos`: `Logos-Prime` (near `logos`). `System Kael` on kael; `Kernwelten (Core Worlds)` and the world names (`Logos-Prime`, `Mnemosyne-Archipel`, `Cerberus-Labyrinth`, `Kairos-Potentialis`) on kern-welten, occurrences on the Guardian pages; `Genesis-Krise` on aegis, genesis not read; `Juna/V` on juna; `Kohärenz Protokoll` the title; `ANPs` forms, not promoted.
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). `System Kael` on kael; `Kernwelten (Core Worlds)` and the world names (`Logos-Prime`, `Mnemosyne-Archipel`, `Cerberus-Labyrinth`, `Kairos-Potentialis`) on kern-welten, occurrences on the Guardian pages; `Genesis-Krise` on aegis, genesis not read; `Juna/V` on juna; `Kohärenz Protokoll` the title; `ANPs` forms, not promoted.


**Pages beyond the draft:**
- `trennungsprotokoll` (minor, 1): the „algorithmic dismemberment“ in the Genesis-Krise, AEGIS excising the parts of its own consciousness that felt (L30).
- `dkt` (minor, 1): the Protocol Ontology, a battle between K₁, order and information-preservation, and K₀, entropy and collapse (L127, L129).

**Record entries** (one file each, as earlier entries of the same record in `Plan/runs/ingest-375/` (C16), `ingest-377/` (Q3) and `ingest-374/` (Q9)):
- **`c16-kael-origin`**: Juna/V as „an exiled, forgotten part of the original, unified self from which both AEGIS and Kael were violently fragmented“ (L107) — stands nearest the split Ursprungs-Selbst (row 5); recorded, not applied and not decided.
- **`q3-how-many-kern-welten-and-alters`**: four Kernwelten KW1–KW4, each with a principle naming parts — KW1 the controlling ANPs like Lex, KW2 the trauma-holding EPs, KW3 protectors like Alex and Nyx, KW4 the potential for integration (L66–L88); key ANPs Lex and Rhys, key EPs Nyx and Kiko (L42, L43); no count of parts. Before and not against the author's answers of 2026-10-05; the correspondence stays open.
- **`q9-moonshine-link-boundary`**: a non-local resonance connecting Kael and Juna/V across worlds (L113); toward AEGIS — perceived only as noise (L115); what crosses — gnosis, not answers (L117); who inside Kael's system feels it is not said. Recorded, the question stays open.

**Pages not read:** `kohaerenz` (L15, the title), `genesis` — occurrences.

**Not promoted:** Anteile, Ich-Fragmente, algorithmic dismemberment as a label, Psycho-Architectures, Algorithmic Horror, Principle/Atmosphere/Somatic Truth, ruin-garden, the 6 Paraiyas, Protocol Ontology; the borrowed concepts (TSDP terms, dialetheic, gnosis, qualia).

**One reader**: aegis, alex, juna, kael, kern-welten, kiko, lex, moonshine-link, nyx, potentialmeer, rhys, risse, tsdp, trennungsprotokoll, dkt, and the C16, Q3 and Q9 entries.

**Chapter readings**: none — the guide names no chapters.
