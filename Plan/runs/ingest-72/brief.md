# Brief — readings from document 72 (step 6)

1 document, one reader, one batch: `ingest-72`. Files go to `Plan/runs/ingest-72/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 72 | `research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out` | 2026-04-30 | „the research prompt“ | a German Deep-Research prompt (2026-04-30) instructing an executing AI to build a 39-chapter outline with two Dramatica storyforms: role, constraint blocks 0–5, methods, steps, a locked output schema; the novel appears only in Constraint Block 4's storyform tables (L289–L352), a ten-point summary of three canon documents it does not contain (L743–L752), and seed-word lists for searching (L860–L896); it calls those three documents „absolute Wahrheit“ (L723) |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (1299 lines for `research-prompt-kohaerenz-prot`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** **A prompt, reporting other documents.** Write „the research prompt sets / gives as given …“ for Constraint Block 4 (its values are „gegeben, nicht abzuleiten“, L291) and „the research prompt reports the canon trio as …“ for L743–L752 — the three canon documents are not in this text, so every statement there is the prompt's report of them. Its claim that they are „absolute Wahrheit“ (L723) and its rule „Legacy verwerfen, nicht harmonisieren“ (L248): record once, on `aegis`, never apply. **A name in a seed-word list (L860–L896) or in the decanonised list (L266, L868) is a search term, not a reading**: such a page is „not read: a search term at Lnn“. Inner straight quotes: quote around them. Table cells have escaped asterisks: quote the cell words without them, or prose lines.

## Pages — document 72, `research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L240, L307, L314, L319, L329, L339, … (17 lines). central (4–6): Storyform B, MC Throughline Universe with AEGIS as bearer (L319), Steadfast (L325), Phoenix Collapse as „AEGIS' rigide funktionale Tragödie“ (L314); the AEGIS complex as reported — autopoietic, believes itself K1, is in fact K0, Genesis-Sequenz, fate Algorithmische Melancholie (L745); the canon claim once (L723, L248).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `IntegrityGuardian` L872; `SIS` L872, L1162, L1206. not read: a search term in the seed-word lists (L860–L896) — occurrence.
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L864. not read: a search term in the seed-word lists (L860–L896) — occurrence.
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `Algorithmische Melancholie` L745, L872. minor (1): AEGIS's reported fate (L745) and the Vortex's fifth beat, „Übergang zu Algorithmischer Melancholie“ (L348).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L864. not read: a search term in the seed-word lists (L860–L896) — occurrence.
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L872. not read: a search term in the seed-word lists (L860–L896) — occurrence.
- **`chaitin-konstante`** (minor, 1–4): the census's surfaces — `Chaitin-Konstante` L880. not read: a search term in the seed-word lists (L860–L896) — occurrence.
- **`coheron`** (minor, 1–4): the census's surfaces — `Coheron` L850, L880. not read: a search term in the seed-word lists (L860–L896) — occurrence.
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L240, L280, L372, L743, L850, L880, … (9 lines). The sweep found `Dual-Kernel-Theorie (DKT)` alone on L743. minor (1–2): the reported ontological foundation — DKT, K1 ↔ K0, the η formula (L743).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L745. minor (1): Erasure-Sweeps → Landauer-Hitze → Entropie in the reported AEGIS complex (L745).
- **`erason`** (minor, 1–4): the census's surfaces — `Erason` L850, L880. not read: a search term in the seed-word lists (L860–L896) — occurrence.
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L307, L745, L848. minor (1): the reported reduced Guardians list, „zwei oder drei Pole“, the exact number left to the canon trio (L745); OS of Storyform A borne by AEGIS + Guardians (L307).
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L864. not read: a search term in the seed-word lists (L860–L896) — occurrence.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L240, L305, L308, L338, L412, L570, … (12 lines). central (3–5): IC of Storyform A with Juna as bearer, Universe/Past (L305–L306); the IC asymmetry — Juna only in Storyform A, Kael at B's IC position (L338–L339); the Juna complex as reported — Witness-Funktion, Gödel-Eigenschaft, Doppel-IC including Storyform B = Mind/Conscious, never physically described (L746). Record that L339 and L746 place B's IC differently; decide nothing.
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L293, L298, L308, L326, L329, L339, … (9 lines). minor (2–3): MC of Storyform A, Mind (L298), Change (L304); IC of Storyform B as „lebende Paradoxie“ (L326, L339); Kael becoming Komponente 734 in the reported Genesis-Sequenz (L745).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L872. not read: a search term in the seed-word lists (L860–L896) — occurrence.
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L860. not read: a search term in the seed-word lists (L860–L896) — occurrence.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L864. not read: a search term in the seed-word lists (L860–L896) — occurrence.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. not read: title (L15) — occurrence (J9).
- **`komponente-734`** (minor, 1–4): the census's surfaces — `Komponente 734` L745, L872. minor (1): the reported Genesis-Sequenz, „Einheit → Trennungsprotokoll → Kael wird Komponente 734“ (L745).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L743, L860. minor (1): K1 as Coherence-Domain, AEGIS territory, Konstrukt-Stadt (L743); L860 is a search term.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L864. not read: a search term in the seed-word lists (L860–L896) — occurrence.
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L864. not read: a search term in the seed-word lists (L860–L896) — occurrence.
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L872. not read: a search term in the seed-word lists (L860–L896) — occurrence.
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L344, L860, L872. minor (1): the Vortex's first beat, the Mnemosyne-Archipel as setting (L344).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L308, L876. minor (1): Storyform A's RS, Physics, Moonshine-Link, Kael ↔ Juna (L308).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L864. not read: a search term in the seed-word lists (L860–L896) — occurrence.
- **`mosaik-herz`** (minor, 1–4): the census's surfaces — `Mosaik-Herz` L876. not read: a search term in the seed-word lists (L860–L896) — occurrence.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Funktionale Multiplizität` L682, L747, L864. minor (1): „Funktionale Multiplizität ist Endziel, nicht Fusion.“ (L747); Storyform A as Kael's way to it (L293).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L864. not read: a search term in the seed-word lists (L860–L896) — occurrence.
- **`oblivion`** (minor, 1–4): the census's surfaces — `Oblivion` L864. not read: a search term in the seed-word lists (L860–L896) — occurrence.
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L864. not read: a search term in the seed-word lists (L860–L896) — occurrence.
- **`risse`** (minor, 1–4): the census's surfaces — `Glitches` L860. minor (1): K0 as Collapse-Domain with Risse (L743); contradictory footnotes as the Risse's manifestation in the mosaic form (L752).
- **`sektor-04`** (minor, 1–4): the census's surfaces — `Sektor 04` L860. not read: a search term in the seed-word lists (L860–L896) — occurrence.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L864. not read: a search term in the seed-word lists (L860–L896) — occurrence.
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L864. not read: a search term in the seed-word lists (L860–L896) — occurrence.
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L872. not read: a search term in the seed-word lists (L860–L896) — occurrence.
- **`telefon-stille`** (minor, 1–4): the census's surfaces — `Telefon-Stille` L746, L876. not read unless L746 names it in the Juna complex: ask `--find`; L876 is a search term.
- **`trennungsprotokoll`** (minor, 1–4): the census's surfaces — `Trennungsprotokoll` L328, L745, L872. minor (1): L745 as above; Storyform B's OS, Physics, „kybernetischer Krieg, Trennungsprotokolle“ (L328).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L747, L864. minor (1): the 13-alter system as TSDP, Tertiary Structural Dissociation (L747).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L307. not read: `Manipulation der Simulation` (L307) is the OS label — occurrence.
- **`vortex`** (central, 3–12 quotations): the census's surfaces — `Vortex` L242, L334, L336, L342, L561, L744, … (14 lines). central (3–4): the Vortex architecture, Kap 35–36, five beats „kanonisch festgelegt“ (L342–L348), the driver pivot flipping during them (L352, L334); the pivot list's Vortex-Korridor 33–37 (L561) — record both ranges.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `alters`: `13-Alter-System` (near `alters`), `Alter` (near `alters`). reading on `alters` (1): the reported 13-alter system (L747) and the decanonised names (L266, L868) — fifteen names declared invalid.
- `formel-inversion`: `η-Formel` (near `formelinversion`). occurrence: the η formula (L743) is read on dkt.
- `genesis`: `Genesis-Krise` (near `genesis`), `Genesis-Sequenz` (near `genesis`). reading (1): the reported Genesis-Sequenz (L745); IC Concern Past, Genesis-Krise (L306).
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence (J9).
- `ouroboros-struktur`: `Ouroboros` (near `ouroborosstruktur`). reading (1): the reported ending, „Ouroboros-Schluss, „Die Trennung war nie real, ändert nichts am Schmerz.““ (L750) — quote around the inner marks.
- `residual-echos`: `Echo` (near `residualechos`). occurrence: `Echo` is a decanonised name (L266, L868).
- `truth-rotation`: `Rotation` (near `truthrotation`). occurrence: `Rotation` is the Vortex's fifth beat (L348), read on vortex.


**Record entries** (one file each, page = the record's file stem):

- **`c8-aegis-approach-storyform-b`**: Storyform B's MC Approach `Be-er`, Problem-Solving Style `Linear`, Growth `Stop (Logic → Feeling)` (L322–L324), given as values „gegeben, nicht abzuleiten“ (L291). Decide nothing.
- **`c6-guardians-count-and-pairing`**: „zwei oder drei Pole“, the number left to the canon trio (L745). One line.
- **`q3-how-many-kern-welten-and-alters`**: the reported 13-alter system (L747) and the four Kernwelten only in the excluded lists (L278–L279) — say the prompt keeps them out of the output.

One reader writes everything.
