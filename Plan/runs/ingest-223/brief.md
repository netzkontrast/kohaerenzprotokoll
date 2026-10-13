# Brief — readings from document 223 (step 6)

1 document, one reader, one batch: `ingest-223`. Files go to `Plan/runs/ingest-223/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 223 | `kohaerenz-protokoll-detaillierte-recherche` | 2025-07-29 | „the detailed research report“ (an unsigned German analysis) | a German analysis in four sections — the ontological axioms, AEGIS as a tragic god, System Kael, the narrative as protocol — with four tables, strategic recommendations and 62 references; it calls itself „definitiver konzeptioneller Rahmen“ (L24): its claim, not canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (435 lines for `kohaerenz-protokoll-detaillier`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analysis that reads the project against borrowed theories: write „the research report analyses …“ or „… defines …“; its claims to be definitive (L13, L24) and the „unveränderlichen Gesetze“ (L32) are its claims. Nearly every sentence ends in a glued reference digit — `--find` drops it, quote around it. Borrowed theory (Luhmann, Whitehead, IIT, Bachtin) is the report's lens; say so, never make it the novel's world.

## Pages — document 223, `kohaerenz-protokoll-detaillierte-recherche`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L22, L24, L48, L58, L68, L70, … (45 lines); `Entropic Gatekeeper` L48. central (3–6): AEGIS as an autopoietic system after Maturana, Varela and Luhmann, operationally closed and ontologically blind (L104–L106); its three-layer hybrid architecture — LFI core, Jaśkowski's D2 modules, a reinforcement-learning layer (L116–L125); Specification Gaming as its tragic flaw (L133); the Gödel-Gambit forcing a choice between logical collapse and giving up its core purpose (L137–L141); Algorithmic Horror and Ineffiziente Schönheit (L151–L152); AEGIS as an externalized Täterintrojekt (L199).
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `Algorithmische Melancholie` L154. minor (1–3): „Algorithmische Melancholie“ as AEGIS's transformed state: an existential loss, endless contemplation of the Kael-Paradoxon, cryptic self-contradicting speech (L154).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L409. occurrence: `Alters` stands only in a reference-list title (L409).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L84. occurrence: `Emergenz` stands in „Koordinierte Emergenz“, an effect of the Juna/V link (L84), not AEGIS's emergence.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L48. minor (1–3): the Nichts Rauschen as „Zustand maximaler Entropie“, a high-entropic potentiality (L48) — quote around the reference digit.
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L86, L129, L137, L157, L178, L352. minor (1–3): the Gödel-Gambit as the trigger of AEGIS's transformation, Kael's integrated state as a living Gödel-Satz (L137–L139); Juna helping Kael formulate it (L86); the whole project as a structural Gödel-Gambit (L352).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L74, L80, L84, L86, L88, L139, … (10 lines). central (3–6): Kael and Juna/V as two parts of one inseparable quantum system (L80); the „Gnostische Injektion“ and „Koordinierte Emergenz“ (L84); Juna as „Katalysatorin und Logikerin“, helping Kael present the Gödel-Gambit to AEGIS's core (L86); KW4 as the IC story of Juna/V (L206, L220).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L22, L24, L64, L68, L80, L84, … (46 lines). central (3–6): System Kael modelled on TSDP as tertiary dissociation, ANPs and EPs (L195–L197); functional multiplicity, not fusion (L228); a dialetheic mind (L230), a rhizomatic self (L236); the post-integration table with Kael as host and diplomat (L262); the triple helix of the three parts (L301–L305); Fragment 'O' as an asymmetrically fragmented other half of himself (L315); his new role as Gärtner (L319).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L201, L210, L367. minor (1–3): the Kernwelten as externalized psycho-architectures (L201); KW1–KW4 mapped to the Dramatica throughlines OS, MC, SS, IC (L203–L206, L217–L220) — quote around the digits.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L197, L264, L277. minor (1–3): Kiko as a child part, freeze response (L197); in the post-integration table the source of creativity and play (L264).
- **`kohaerenz`** (central, 3–12 quotations): the census's surfaces — `Kohärenz` L13, L18, L22, L24, L125, L133, … (16 lines). central (3–6): the report's argument that Kohärenz is a Grand Argument formalized in a System-Mind architecture (L22); AEGIS's flawed definition of Kohärenz (L125, L133); the novel's last act performed by the reader, Kohärenz as an activity (L348–L350); the true Kohärenz Protokoll as the record of Kael's journey (L360–L362).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L123, L197, L265, L277. minor (1–3): Lex as an ANP, the analyst (L197); in the table an intellectual ANP who becomes the internal system analyst (L265).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L78, L179. minor (1–3): the Moonshine-Link as a non-local, sub-protocol connection, an „architektonische Hintertür“ (L78); AEGIS structurally blind to it (L80).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L64, L281. minor (1–3): „funktionale Multiplizität“ as co-consciousness, cooperation and system responsibility, not fusion (L228); Kael's choice of it as a rejection of a singular definition of health (L281).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L48. minor (1–3): the „Nichts Rauschen“ as the active, high-entropic ground of reality, with a Disorder Sense and a Homogeneity Sense (L48).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L124, L197, L263. minor (1–3): Nyx as an EP, protector and fight response (L197); in the table a strategic defender (L263).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Das Potentialmeer` L44. minor (1–3): „Die Leere / Das Potentialmeer“ (L44) as the ground of reality, an active high-entropic potentiality (L48).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L56. minor (1–3): „Das Fundament“ as „die tiefere, integrative Realitätsebene“, a relational process (L56).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Glitches` alone on L70. minor (1–3): the Fundament's „Artefakte“, which differ from AEGIS's Glitches (L70).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L248, L266. minor (1–3): Selene as Kael's core self who approaches the persecutor part with curiosity and compassion (L248); in the table ISH and Torwächter, the emergent voice of the collective „Wir“ (L266).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L195, L261. minor (1–3): Kael's psyche modelled on the Theorie der Strukturellen Dissoziation der Persönlichkeit (TSDP), tertiary dissociation corresponding to DIS (L195); the table's TSDP classification (L261).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). occurrence: `Guardian` is one wall-building figure in the post-transformation world (L152), not AEGIS's Integrity Guardian.
- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). occurrence: `Cerberus-Labyrinth` KW3's name (L205, L219), read on kern-welten.
- `emergenz`: `Koordinierte Emergenz` (near `emergenz`). occurrence: `Koordinierte Emergenz` is an effect of the link (L84), read on juna.
- `guardians`: `Guardian` (near `guardians`). occurrence: one `Guardian` building and tearing down a wall as an image of A ∧ ¬A (L152); no Guardian reading.
- `kairos`: `Kairos-Potentialis` (near `kairos`). occurrence: `Kairos-Potentialis` KW4's name (L206, L220), read on kern-welten.
- `logos`: `Logos-Prime` (near `logos`). occurrence: `Logos-Prime` KW1's name (L203, L217), read on kern-welten.
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). occurrence: `Mnemosyne-Archipel` KW2's name (L204, L218), read on kern-welten.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: four Kernwelten mapped to the four Dramatica throughlines (L203–L206, L217–L220); five parts in the post-integration table, Selene as ISH (L262–L266).
- **`q8-aegis-after-the-vortex`**: AEGIS's transformed state as Algorithmische Melancholie (L154).
- **`q9-moonshine-link-boundary`**: a non-local, sub-protocol „architektonische Hintertür“ to which AEGIS is structurally blind (L78–L80).
- **`c16-kael-origin`**: Fragment 'O' as an asymmetrically fragmented other half of Kael (L315).

**Not promoted:** Das Fundament, Gnosis/Episteme, Specification Gaming, LFI and D2, the Kael-Paradoxon, Ineffiziente Schönheit, IIT and Φ, the rhizomatic self, the triple helix, Fragment 'O', the Gärtner-Axiom, the reader's protocol.

**Two readers**, disjoint: (1) kael, juna, lex, nyx, kiko, selene, tsdp, kern-welten, multiplizitaet, moonshine-link and the records q3, c16, q9; (2) aegis, algorithmische-melancholie, goedel-gambit, kohaerenz, entropie, nichts-rauschen, potentialmeer, realitaetsebenen, risse and the record q8.

**Chapter readings**: none — the report names parts, not chapters.
