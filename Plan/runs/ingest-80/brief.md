# Brief — readings from document 80 (step 6)

1 document, one reader, one batch: `ingest-80`. Files go to `Plan/runs/ingest-80/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 80 | `roman-plot-entwicklung-mit-kohaerenzprotokoll` | 2026-02-23 | „the master blueprint“ (its title: `Narrative Architektur und Vollständiger Plot-Blueprint`) | a German plot blueprint of 2026-02-23 in an assistant's voice: an ontological analysis (AEGIS against Kael, the Parakonsistente Gambit), a research plan, the „Vier-Linsen“ method, then 39 chapters in three parts plus a coda `Kapitel 40/0`, each in five fields (Schauplatz, Charaktere/Linsen, Pacing & Atmosphäre, Plot-Beats, Quellen), and 30 references; it calls itself a „Master-Blueprint“ for later AI-assisted writing sessions; no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (426 lines for `roman-plot-entwicklung-mit-koh`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** **A plan for writing sessions, before the reset.** Write „the master blueprint plans …“. Glued reference digits after a word (`Normalität.10`) are its sources: cut before them. Its chapter content goes on the chapter pages, a later batch: on a term page give at most one or two chapter beats, by chapter number. Its analysis (L19–L49) is the blueprint's own reading. Lost symbols after `Monstergruppe` (L38) and `Ganzheit`: don't quote across them.

## Pages — document 80, `roman-plot-entwicklung-mit-kohaerenzprotokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L23, L25, L37, L44, L62, L72, … (57 lines). central (3–5): AEGIS spelled out as „Autonomous Entropic Gatekeeper for Integrity Systems“ (L23), operating by the coherence theory of truth (L23); the Parakonsistente Gambit, Kael as a living Gödel sentence (L25); AEGIS not evil but trapped in its programming (L37); the parser lens (L44).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `Zero-Trust` L37. minor (1–2): read by the census's surfaces: what the blueprint plans for it — 1–3 quotations, chapter numbers in prose.
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L102, L104, L209, L211. minor (1–2): read by the census's surfaces: what the blueprint plans for it — 1–3 quotations, chapter numbers in prose.
- **`alters`** (central, 3–12 quotations): the census's surfaces — `Alters` L36, L64, L144, L187, L219, L249, … (11 lines). minor (1–2): read by the census's surfaces: what the blueprint plans for it — 1–3 quotations, chapter numbers in prose.
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L101, L102, L104, L109, L110, L309, … (7 lines). minor (1–2): read by the census's surfaces: what the blueprint plans for it — 1–3 quotations, chapter numbers in prose.
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L397. minor (1–2): read by the census's surfaces: what the blueprint plans for it — 1–3 quotations, chapter numbers in prose.
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L21. minor (1): the „Dual Kernel Theory“ (DKT) as the architecture's frame (L21).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L136. minor (1–2): read by the census's surfaces: what the blueprint plans for it — 1–3 quotations, chapter numbers in prose.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L44. minor (1–2): read by the census's surfaces: what the blueprint plans for it — 1–3 quotations, chapter numbers in prose.
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L195. minor (1–2): read by the census's surfaces: what the blueprint plans for it — 1–3 quotations, chapter numbers in prose.
- **`guardians`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Guardians` alone on L417. minor (1–2): read by the census's surfaces: what the blueprint plans for it — 1–3 quotations, chapter numbers in prose.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L25, L38, L46, L62, L64, L110, … (25 lines). central (2–4): the social lens (L46); `Juna (Hologramm)` in Kap 1 (L62, L64); and how else the blueprint writes her (`Signatur`, `Juna/V (Echo)`, Kap 17's origin self) — record each as written.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L13, L23, L25, L38, L45, L61, … (89 lines). central (2–3): the human lens (L45); waking after a „Universal Reboot“ (L64); Kap 40/0, Kael generating Kap 1 by a retrieval over the memories of the future (L385).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L125, L133, L134, L136, L225, L227. minor (1–2): read by the census's surfaces: what the blueprint plans for it — 1–3 quotations, chapter numbers in prose.
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L23, L256, L279, L335, L340. minor (1–2): read by the census's surfaces: what the blueprint plans for it — 1–3 quotations, chapter numbers in prose.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L70, L72, L187, L209, L211, L341, … (8 lines). minor (1–2): read by the census's surfaces: what the blueprint plans for it — 1–3 quotations, chapter numbers in prose.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: title — occurrence (J9).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Konstrukt-Stadt` alone on L413. minor (1–2): read by the census's surfaces: what the blueprint plans for it — 1–3 quotations, chapter numbers in prose.
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L64, L70, L72, L78, L94, L96, … (12 lines). central (2): Lex (Analytiker) in Kap 2 (L70) and where else he acts.
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L78, L80, L158, L185, L225, L309, … (7 lines). minor (1–2): read by the census's surfaces: what the blueprint plans for it — 1–3 quotations, chapter numbers in prose.
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L85, L93, L94, L96, L176. minor (1–2): read by the census's surfaces: what the blueprint plans for it — 1–3 quotations, chapter numbers in prose.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L25, L38, L112. minor (1–2): the Moonshine-Link (Kael–Juna) anchored as hard SF, linking entanglement (ER=EPR) with symmetries (L38).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L285, L287. minor (1–2): read by the census's surfaces: what the blueprint plans for it — 1–3 quotations, chapter numbers in prose.
- **`mosaik-herz`** (minor, 1–4): the census's surfaces — `Mosaik-Herz` L144. minor (1–2): read by the census's surfaces: what the blueprint plans for it — 1–3 quotations, chapter numbers in prose.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Funktionale Multiplizität` L136. minor (1–2): read by the census's surfaces: what the blueprint plans for it — 1–3 quotations, chapter numbers in prose.
- **`nexus`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Nexus` alone on L195. minor (1–2): read by the census's surfaces: what the blueprint plans for it — 1–3 quotations, chapter numbers in prose.
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Das Nichts Rauschen` L277. minor (1–2): read by the census's surfaces: what the blueprint plans for it — 1–3 quotations, chapter numbers in prose.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L102, L104, L110, L112, L160, L309, … (8 lines). minor (1–2): read by the census's surfaces: what the blueprint plans for it — 1–3 quotations, chapter numbers in prose.
- **`oblivion`** (minor, 1–4): the census's surfaces — `Oblivion` L94, L96, L341, L343. minor (1–2): read by the census's surfaces: what the blueprint plans for it — 1–3 quotations, chapter numbers in prose.
- **`potentialmeer`** (central, 3–12 quotations): the census's surfaces — `Potentialmeer` L152, L203, L232, L235, L267, L274, … (11 lines). central (2–3): what the blueprint plans for the Potentialmeer — find its lines.
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L372. minor (1–2): read by the census's surfaces: what the blueprint plans for it — 1–3 quotations, chapter numbers in prose.
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L86, L88. minor (1–2): read by the census's surfaces: what the blueprint plans for it — 1–3 quotations, chapter numbers in prose.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L37, L57, L235. minor (1–2): read by the census's surfaces: what the blueprint plans for it — 1–3 quotations, chapter numbers in prose.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L193, L209, L211, L257, L259. minor (1–2): read by the census's surfaces: what the blueprint plans for it — 1–3 quotations, chapter numbers in prose.
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L201, L203, L290, L293, L295. minor (1–2): read by the census's surfaces: what the blueprint plans for it — 1–3 quotations, chapter numbers in prose.
- **`tsdp`** (central, 3–12 quotations): the census's surfaces — `TSDP` L13, L21, L36, L53, L57, L144, … (10 lines). central (2–3): the three parts as TSDP's treatment phases (L53, L57); the research table's TSDP row (L36).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L157, L184, L192. minor (1–2): read by the census's surfaces: what the blueprint plans for it — 1–3 quotations, chapter numbers in prose.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `entropie`: `Informationsentropie` (near `entropie`), `Shannon-Entropie` (near `entropie`). occurrence: `Informationsentropie`, `Shannon-Entropie` are lens terms (J12).
- `kishotenketsu`: `Kishōtenketsu-Prinzip` (near `kishotenketsu`). reading (1) on `kishotenketsu`: the Kishōtenketsu principle of Kap 40/0 (L385).
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Singuläre Punkt der Kohärenz` (near `koharenz`), `Sünde gegen die Kohärenz` (near `koharenz`), `Kohärenz-Test` (near `koharenz`), `Kohärenztheorie der Wahrheit` (near `koharenz`). occurrence (J12).


**Record entries:**

- **`q7-what-734-names`**: `Unit 734 (Guardian/Regel-Exekutor)` in Kap 2 (L70) and wherever else the blueprint names 734 — a sense beside Komponente and Kael; decide nothing.
- **`c7-juna-first-appearance`**: Juna as a hologram at the formal check-in in Kap 1 (L62, L64).
- **`c6-guardians-count-and-pairing`**: the guardians the blueprint names, and Sophia as `Guardian` in Kap 18 and `abtrünnig` in Kap 29 — find the lines.
- **`c13-externe-ebene-beyond-the-simulation`**: what the blueprint says of an external level, if it does (the page `externe-ebene` is in the list).

One reader writes all term pages and records.
