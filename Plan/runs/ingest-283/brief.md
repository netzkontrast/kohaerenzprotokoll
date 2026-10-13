# Brief — readings from document 282 (step 6)

1 document, one reader, one batch: `ingest-283`. Files go to `Plan/runs/ingest-283/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 282 | `roman-konzeptentwicklung-kohaerenz-protokoll` | 2026-02-26 | „the master synthesis“ (an unsigned German research report) | a „Master-Synthese und Narrativer Blueprint“ (L11): the novel on four axes — psychological (Kael's ANP/EP split, cache coherence), systemic (AEGIS, LogOS, Mnemosyne), ontological (four Kernwelten), dramaturgical (Kishōtenketsu, Dramatica, three parts over 39 chapters) — with scene logics, sample prose, a self-check and an open question on chapter 1; its „Golden Sources“ and „System-Status: Online“ are its own framing |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (188 lines for `roman-konzeptentwicklung-kohae`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A synthesis and plan: write „the master synthesis describes / plans / places …“; its scene logics and `Narrativer Entwurf (Beispiel)` passages are proposals and samples, not canon. Quotations: cut before bold markers, glued reference digits and the lost formula symbols (L42, L46). Chapter numbers glued to words drop out of `--find` — quote around them.

## Pages — document 282, `roman-konzeptentwicklung-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L29, L40, L42, L44, L46, … (17 lines). central (3–6): „Autonomous Entropic Gatekeeper for Integrity Systems“ (L42); autopoietic, „operativ geschlossen“, reproducing its own elements (L44); unable to grasp Juna semantically, reading her as Nichts-Rauschen (L44); erasing her memory generating heat, suppression of trauma a thermodynamic crisis (L46); in Kapitel 3 ordering the deletion of the anomaly (L83); not destroyed but transformed into a semipermeable membrane (L116).
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — `Cache-Kohärenz` L31, L79, L144, L145, L151. minor (1–3): the ANP/EP separation mapped to cache coherence, a protocol fundamentally defect in Kael's psyche (L31); Part I's horror from its failure (L79); the self-check (L144–L145); the initial failure in chapter 1 as the open question (L151).
- **`chaitin-konstante`** (minor, 1–4): the census's surfaces — `Chaitin-Konstante` L110. minor (1–3): the Chaitin constant as the incompressible truth of Juna's existence that AEGIS's axioms cannot hold (L110).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L187. not read: occurrence — `DID` (L187) stands in a reference title.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L17. not read: occurrence — `Entropie` (L17) in a general sentence.
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L55. minor (1–3): only if L55 names the Externe Ebene with KW 4; else not read.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L29, L38, L44, L46, L55, L68, … (15 lines). central (3–6): an EP fragment, „die Trägerin der Trauma-Information“ (L29); outside AEGIS's axioms (L44); the personification of KW 4 (L55); first appearing at the edge of the field of view in Kapitel 3 (L83); unmasking herself near the end of Act II, Kapitel 26 (L102); the Chaitin constant of her existence (L110).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L25, L27, L31, L35, L36, … (26 lines). central (3–6): the System Mind and the isomorphy of Kael and AEGIS (L15); Kael as ANP host, the split literal (L25); the Manager as secondary ANP (L27); waking in his unit (L81); the Bekenstein bound and the SIS state in Kapitel 13 (L87); meeting Nox in Part III, not destroying him (L112).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L48, L50. central (3–6): the simulation divided into ontological spheres, Kernwelten, each with its own laws (L48–L50); KW 1 Konstrukt-Stadt (L52), KW 2 the Grenz-Zonen (L53), KW 3 Die Überwelt / Der Nexus (L54), KW 4 the Resonanz-Kontinuum (L55).
- **`kishotenketsu`** (minor, 1–4): the census's surfaces — `Kishōtenketsu` L57, L59, L61, L65, L131, L135, … (9 lines). minor (1–3): the Kishōtenketsu steps beside the Dramatica throughlines and the three parts (L57–L69).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrence — the title (L11).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L27, L44, L46, L52, L66, L78, … (7 lines). minor (1–3): KW 1, „Sie ist eine streng euklidische, deterministische Hyperstruktur“, the horror of predictability, a ban on metaphor (L52).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L37, L54, L83, L97, L99, L127. minor (1–3): a guardian program in the Überwelt (L54), confronting Kael in Part II (L97), „ein Gefangener der Turing-Mechanik“ sacrificing resolution (L99); and „die exekutive Instanz von AEGIS“ (L83) — the document does not reconcile the two.
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L54, L97, L100. minor (1–3): in Part II revealing to Kael the illusion of his own identity (L100).
- **`mosaik-herz`** (minor, 1–4): the census's surfaces — `Mosaik-Herz` L69, L116. minor (1–3): the dissonance integrated (L69); the finale in Kapitel 38-39 forming the Mosaik-Herz (L116).
- **`nexus`** (minor, 1–4): the census's surfaces — `Nexus` L54, L92, L95. minor (1–3): „Die Überwelt / Der Nexus“ as KW 3, the machine room behind the rendering (L54); „KW 3 (Der Nexus / Die Überwelt)“ in Part II (L92).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts-Rauschen` L44, L102. minor (1–3): AEGIS reading Juna's intrusion as Nichts-Rauschen (L44, L102).
- **`personas`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Persona` alone on L95. minor (1–3): the focal persona shifting in Part II so that the Manager takes the lead (L95).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L15. minor (1–3): only if L15 characterises a Realitätsebene; else not read.
- **`sektor-04`** (minor, 1–4): the census's surfaces — `Sektor 04` L85. minor (1–3): Sektor 04 in the sample prose of L85.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L25, L35, L83, L140. minor (1–3): Kael's psyche by the theory of structural dissociation (L25); the self-check friction TSDP-pathology vs cyberpunk aesthetics (L140).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L54, L87, L92, L114. minor (1–3): „Die Überwelt / Der Nexus“, KW 3, where the guardian programs reside (L54); L87, L114 only if they add.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz-Kernels` (near `koharenz`), `Zielkohärenz erreicht` (near `koharenz`). occurrence: the title; `Kohärenz-Kernels` and `Zielkohärenz erreicht` not read.
- `kohaerenz-kernel`: `Kohärenz-Kernels` (near `koharenzkernel`). occurrence: `Kohärenz-Kernels` with a lost symbol (L42), not characterised.
- `landauer-signatur`: `Landauer` (near `landauersignatur`). occurrence: `Landauer` the principle, not the signature.
- `thermodynamischer-phaenomenalismus`: `Phaenomena` (near `thermodynamischerphaenomenalismus`). occurrence: `Phaenomena` a reference title.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: four Kernwelten KW 1–KW 4 (L50–L55).
- **`q6-nexus-ueberraum-ueberwelt`**: „Die Überwelt / Der Nexus“ as one world, KW 3 (L54), reversed as „KW 3 (Der Nexus / Die Überwelt)“ (L92).
- **`c7-juna-first-appearance`**: Juna first at the edge of the field of view in Kapitel 3 (L83); unmasking herself in Kapitel 26 (L102).
- **`c11-landauer-warmth-or-cold-ozone`**: in the sample of L85, erasing Juna's memory makes the corridor's temperature shoot up, Kael is burnt, the smell is ozone and burnt matter (L85; L46 the principle).
- **`q8-aegis-after-the-vortex`**: AEGIS not destroyed but transformed into a semipermeable membrane (L116).

**Not promoted:** the System Mind, the four axes, the Grenz-Zonen and the Resonanz-Kontinuum as world names, Nox, the Manager, the SIS state, the Bekenstein bound, the self-check items, the Golden Sources.

**One reader**: every page above, the five records, and the chapter readings below.

**Chapter readings** (the same reader, into `Plan/runs/ingest-283-kap/readings/kap-NN--roman-konzeptentwicklung-kohaerenz-protokoll.md`, one per chapter, `## Reading — \`slug\`, 2026-02-26, the master synthesis — <topic>` with one bullet): Kap 1 (the open question on the initial cache-coherence failure, L149–L151), Kap 3 (Juna at the edge of view, the deletion order, L83, with the sample L85), Kap 13 (the ultimate collapse, L87), Kap 26 (Juna unmasks herself, L102), Kap 36 (the fourth wall, L114), Kap 38 and Kap 39 (the finale, the Mosaik-Herz, AEGIS transformed, L116).
