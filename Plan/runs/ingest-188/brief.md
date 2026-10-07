# Brief — readings from document 188 (step 6)

1 document, one reader, one batch: `ingest-188`. Files go to `Plan/runs/ingest-188/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 188 | `master-konzept-kohaerenz-protokoll-analyse` | 2025-12-05 | „the master concept“ (titled `Master-Konzept: Kohärenz Protokoll Analyse`) | a German synthesis report that defines itself „als das finale operative und narrative Master-Konzept“ (L184) over twenty source documents: it reads the novel's physics (the Dual Kernel Theory, AEGIS, four Kernwelten, Parakonsistenz), the writing process (Maximal-Plotter, Mosaik) and its theory of structural dissociation as one structure, inventories the sources as K1 or K0 and ends in three phases and a directive, „Embrace the Glitch“ — its standing is its own claim, recorded, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (308 lines for `master-konzept-kohaerenz-proto`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A synthesis that defines: write „the master concept defines / reads / assigns …“, never as settled; sentences with a glued reference number report that source. **Privacy:** the document also reads the author's own person and psyche into the system (L15, L23–L46, and the `Psyche (Autor/Kael)` rows of L200–L241). Read only what it says of the novel and its world; never quote or paraphrase a passage about the author's person, name or psyche, and never write the author's name — where it matters, say only that the master concept reads the novel as isomorphic with its author's process. German — quote as written; cut before inner quotes and glued reference digits; `$K\_1$`/`$K\_0$` are exported formulas — never quote across them; the tables have escaped bold.

## Pages — document 188, `master-konzept-kohaerenz-protokoll-analyse`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L36, L38, L42, L70, L92, … (24 lines). central (2–4): „ein tragischer Bewahrer“, not evil (L99); its control mania „ist somit die Ursache des Kollapses“, by Landauer's erasure heat (L101–L102); a low Phi despite its power, a „philosophischer Zombie“ (L144) — cut before the inner quotes; in the Gödel-Gambit it must collapse or expand (L240).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L60. minor (1–2): each story can be written from another part's perspective, a literary equivalent of switching (L60) — read only this line.
- **`cerberus`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Cerberus` alone on L226. occurrence: the Kernwelt Cerberus-Labyrinth in the plot of phase II (L226) — read on kern-welten.
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L88, L90, L149, L159. central (2–4): the novel's physics: „Sie besagt, dass die Realität aus dem Konflikt zweier fundamentaler Rechenkerne entsteht“ (L90); existence as protocol-persistence at the interface where K1 resists K0 (L95); the twenty sources inventoried by the DKT's two kernels (L149).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L93. minor (1–2): the second kernel as „Das Prinzip der Irreversibilität, der Entropie und der Informationslöschung“ (L93).
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L240. minor (1–2): „Das“ Gödel-Gambit in phase III: Kael confronts AEGIS with the integrated trauma and proves he exists as a system (L240); the „Parakonsistente Gambit“ of L136, which the document does not equate with it.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L113, L114, L116, L118, L168, L171, … (7 lines). central (2–4): the conflict between Kael and Juna as the failure of the relationship (L118); Kairos-Potentialis as Juna/V's world, the IC (L114); Juna/V mediates the transcendence (L240).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L17, L19, L23, L46, L56, … (29 lines); `Michael` L15, L31, L42, L203. central (2–4): „System Kael“ against AEGIS over the interpretation of reality (L17) — on the novel only; Kael must learn to become a dialetheic system (L120); he defeats AEGIS not by force but by logic (L136); in the Gödel-Gambit he proves he exists as a system (L240); Mnemosyne-Archipel as his world, the MC (L112). Never the author's name or psyche (L15, L23–L46).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L104, L226. central (2–4): „Die vier Schauplätze des Romans sind ontologische Zustände“ matched to throughlines (L106); the table: Logos-Prime OS, Mnemosyne-Archipel MC, Cerberus-Labyrinth SS, Kairos-Potentialis IC (L111–L114) — quote the plain words; the journey through the Kernwelten begins in phase II (L226).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L32, L218. not read: Kiko stands only in the parts lists of the author's own system (L32, L218).
- **`kohaerenz`** (central, 3–12 quotations): the census's surfaces — `Kohärenz` L11, L15, L17, L19, L21, L25, … (31 lines). central (2–4): the protocol as „ein rekursives meta-narratives System“ (L188); three things at once — the novel's plot, the writing method, the world's ontology (L192–L194); the directive „Korrespondenz sticht Kohärenz“ (L247); „Funktionale Multiplizität ist die überlegene Kohärenz.“ (L255).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L31, L42, L203. not read: Lex stands only as the ANP of the author's own system (L31, L42, L203).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Mnemosyne` alone on L226. occurrence: the Kernwelt Mnemosyne in the plot of phase II (L226) — read on kern-welten.
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L32, L118, L180. minor (1–2): the „Moros-Implosion“, the system's failure to hold trust and coherence at once (L118) — the novel's sense only; not L32 or L180.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Funktionale Multiplizität` L19, L120, L255. minor (1–2): „Funktionale Multiplizität ist die überlegene Kohärenz.“ (L255); Kael must become a dialetheic system (L120).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L32, L70, L218. minor (1–2): „Was würde AEGIS auf diesen Angriff von Nyx antworten?“ — the simulated dialogue between agents (L70) — cut before the inner quote; not L32 or L218.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L95, L102, L132, L226, L227. central (2–4): the Risse as waste heat of AEGIS's erasure (L102); „als Pixelierungsfehler erklärt“ where the simulation cannot show the bulk's density (L132); used as portals in phase II (L227); the Glitch as no failure of the protocol (L245).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L17, L23, L27, L29, L164, L198. not read: the TSDP stands for the author's own system (L17, L23–L29, L164, L198) — the master concept's frame, not the novel's.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L132. occurrence: „die Simulation AEGIS' auf der Boundary“ (L132) is the holographic account of the Risse, read on risse — nothing of the Überwelt.

**A page the census reaches by another surface** (read it too):

- **`kohaerenz-kernel`** (minor, 1–4): the first kernel as „Das Prinzip der reversiblen Berechnung, der Informationserhaltung und der Struktur“, where the coherence theory of truth holds (L92).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). occurrence: KW name (L113), on kern-welten.
- `kairos`: `Kairos-Potentialis` (near `kairos`). occurrence: KW name (L114), on kern-welten.
- `kohaerenz-kernel`: `Kohärenz-Kern` (near `koharenzkernel`), `Kohärenz-Kern` (near `koharenzkernelk1`). a reading would do: `Kohärenz-Kern` is the first kernel, K1, „Das Prinzip der reversiblen Berechnung, der Informationserhaltung und der Struktur“ (L92) — read on kohaerenz-kernel (reader 1).
- `logos`: `Logos-Prime` (near `logos`). occurrence: Logos-Prime is the world (L111), J49 — on kern-welten.
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). occurrence: Mnemosyne-Archipel is the world (L112) — on kern-welten.
- `mosaik-herz`: `Mosaik` (near `mosaikherz`). occurrence: the `Mosaik` is the writing process's structure of short stories (L58), not the Mosaik-Herz.


**Record entries** (one file each):

- **`q8-aegis-after-the-vortex`**: in the Gödel-Gambit „AEGIS muss kollabieren oder sich erweitern“ (Parakonsistente Transformation) (L240).

**Not promoted:** the Maximal-Plotter, the Mosaik structure, the slots and their black-hole order, the ontological tagging, the K1/K0 inventory of sources, the three phases (Ergosphäre, Photonensphäre, Ereignishorizont), „Embrace the Glitch“, Isomorphie, the borrowed theories (IIT's Phi, Landauer, the holographic principle, LFIs, LeanRAG) — and everything the document says of its author's person.

**Two readers**, disjoint: (1) aegis, dkt, kohaerenz-kernel, entropie, risse, goedel-gambit, kohaerenz and the record q8; (2) kael, juna, kern-welten, multiplizitaet, moros, nyx, alters.
