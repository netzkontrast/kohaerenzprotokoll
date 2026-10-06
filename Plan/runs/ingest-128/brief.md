# Brief — readings from document 128 (step 6)

1 document, one reader, one batch: `ingest-128`. Files go to `Plan/runs/ingest-128/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 128 | `roman-refactoring-kohaerenz-und-charakterentwicklung` | 2026-02-26 | „the refactoring plan“ (titled `Systemischer Refaktorierungsplan: Das Kohärenz Protokoll`, L11) | a German plan of 2026-02-26 by an AI „Novel Writing Assistent“ speaking to the author („Sie“, L13): the repository, the Dual-Kernel-Theorie and truth, an eleven-part matrix mapping Kael's parts onto physics and maths (L51–L62), then Akt I–III with chapter numbers, recommendations and questions back to the author; it promises the plan „garantiert eine unvergleichliche inhaltliche Kohärenz“ (L132) — recorded, not applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (166 lines for `roman-refactoring-kohaerenz-un`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plan by an assistant to the author: write „the refactoring plan recommends / maps …“; its physics metaphors per part are its proposals, not the world's physics; ideas carrying a footnote digit are its report of a reference (Davidson, Landauer, Jaspers, Heidegger, Page-Wootters) — say so. Glued footnote digits (`.2`, `.17`) are cut off quotations. Kael is male. Chapter pages are done by the session.

## Pages — document 128, `roman-refactoring-kohaerenz-und-charakterentwicklung`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L27, L29, L31, L33, L37, L39, … (24 lines). central (2–4): „der Autonomous Entropic Gatekeeper for Integrity Systems“ as „der algorithmische Wächter der Kohärenz-Domäne“ (L29); standing for the correspondence theory (L31); trying to compress the region to a singularity (L104); losing control of time (L114); its definition of coherence rejected (L126).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L61. minor (1–2): „(Sekundärer ANP)“, crisis manager and protector (L61).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L62, L92. minor (1–2): „(Emergierender ANP/EP)“, meta-cognition (L62).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `dissoziative Identitätsstruktur` alone on L15. minor (1–2): „dissoziative Identitätsstruktur“ (L15, L37) — what the lines say.
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L27. The sweep found `Dual-Kernel-Theorie (DKT)` alone on L27. minor (1–2): the Dual-Kernel-Theorie defining the narrative as a simulation constituted by the two kernels' conflict (L27).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L112. minor (1–2): time as emergent, the Page-Wootters mechanism (L112, L116) — say it is the plan's report of a theory.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L31. minor (1–2): the Kollaps-Kernel marks „den notwendigen Einbruch der Entropie“ (L31); the Nichts-Rauschen as entropy (L120).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L88. minor (1–2): „personifizierte, engstirnige Algorithmen“ (L88).
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L59. minor (1–2): „(EP Sexualisiert)“ (L59).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L27, L31, L33, L80, L84, L100, … (9 lines). central (2–4): „die Anomalie Juna“ as representative of the Kollaps-Kernel (L31); Kael meets Juna in Kapitel 3 (L84); protected in Kapitel 26 (L104); entangled with Kael (L106).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L21, L29, L33, L35, L37, … (30 lines). central (2–4): „(Primärer ANP)“, the host (L52); a system of eleven parts (L41); his trauma rooted „in der Genesis-Krise von AEGIS“ (L39); healing not as „Final Fusion“ (L66); his Sein zum Tode (L122).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L57, L76, L98, L116, L126. minor (1–2): „(EP Freeze/Angst)“ (L57).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the title and the protocol's name (J9).
- **`kohaerenz-kernel`** (minor, 1–4): the census's surfaces — `Kohärenz-Kernel` L27. minor (1–2): the conflict between Kohärenz-Kernel and Kollaps-Kernel (L27).
- **`kollaps-kernel`** (minor, 1–4): the census's surfaces — `Kollaps-Kernel` L27, L31. minor (1–2): L27; Juna as the Kollaps-Kernel's representative (L31).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L21, L54, L60, L72, L110, L138. minor (1–2): Akt I's Konstrukt-Stadt as a hostile, incomprehensible environment (L72).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L55, L68, L76, L126, L136. minor (1–2): „(Rationaler ANP)“, analyst and strategist, the Gödel incompleteness metaphor (L55).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L58, L98. minor (1–2): „(EP Ambivalenz)“ (L58).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L90, L92, L94. minor (1–2): Kapitel 14, LogOS the guardian of logic, the correspondence theory (L92); the slingshot argument against it (L94).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L96, L98, L100. minor (1–2): Kapitel 18, Mnemosyne confronting Kael with the illusion of his singular ego (L98).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L56, L60, L116, L136. minor (1–2): „(EP Kollaps)“, deepest hopelessness (L56).
- **`mosaik-herz`** (minor, 1–4): the census's surfaces — `Mosaik-Herz` L108, L124, L126. minor (1–2): Akt III's title (L108); „Stattdessen manifestiert sich das“ — cut before the straight quotes; the parts stay distinct (L126).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Funktionale Multiplizität` L64. minor (1–2): „Funktionale Multiplizität durch polyphone Narration“ (L64); healing not as fusion (L66).
- **`nexus`** (minor, 1–4): the census's surfaces — `Nexus` L88. minor (1–2): the same line: „die Überwelt (den Nexus)“ (L88).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts-Rauschen` L78, L80, L120. minor (1–2): the Nichts-Rauschen in the empty zones explained by the Landauer principle (L80); accepted as part of reality in Akt III (L120).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L54, L68, L126. minor (1–2): „(EP Kampf-Reaktion)“, rage and defence (L54).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L60, L100, L126. minor (1–2): „(Sekundärer ANP)“, harmoniser (L60) — an ANP here.
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L60. occurrence unless L60 says something of the Risse — then minor (1).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L53, L92, L106. minor (1–2): „(Integratorin / ISH)“ (L53); recognises that Kael and Juna are entangled (L106).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L39, L51, L132. minor (1–2): the matrix's column „(TSDP-Typ)“ (L51); the trauma as a Tertiäre Strukturelle Dissoziation (L39).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L86, L88, L100, L110. minor (1–2): „Der Übergang in die Überwelt (den Nexus)“ (L88) — the plan equates the two.
- **`verschraenkungs-insel`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Verschränkungs-Insel` alone on L106. minor (1–2): Selene establishing an entanglement island for Kael and Juna (L106).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Krise` (near `genesis`). a reading on genesis, minor (1): Kael's trauma rooted „in der Genesis-Krise von AEGIS“ (L39) — by Reader 1.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Cache-Inkohärenz` (near `koharenz`), `Kohärenztheorie` (near `koharenz`). occurrence (J9); Cache-Inkohärenz and Kohärenztheorie the plan's own and borrowed terms.
- `verschraenkungs-insel`: `Verschränkungs-Inseln` (near `verschrankungsinsel`). `Verschränkungs-Inseln` — on the page above.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: eleven parts (L41), the matrix's rows Kael, Selene, Nyx, Lex, Moros, Kiko, Lia, Isabelle, Rhys, Alex, Argus (L52–L62) — with their types.
- **`c7-juna-first-appearance`**: „Wenn Kael auf Juna trifft (Kapitel 3)“ (L84) — dated 2026-02-26, before the author's decision of 2026-10-05.
- **`q6-nexus-ueberraum-ueberwelt`**: „die Überwelt (den Nexus)“ (L88) — the plan equates the Überwelt and the Nexus.

**Not promoted:** the repository and knowledge-graph talk (L19–L23, the assistant's account of a code base), Slingshot-Argument, Korrespondenz- and Kohärenztheorie, Grenzsituation, Russellsche Trümmer, the physics metaphors per part, polyphone Narration, Page-Wootters, Ayin, Sein zum Tode, External Awakening, Cache-Inkohärenz (twice, undefined).

**Split into two readers, at the same time on disjoint pages:**
- Reader 1: aegis, juna, dkt, kohaerenz-kernel, kollaps-kernel, entropie, nichts-rauschen, konstrukt-stadt, ueberwelt, nexus, guardians, logos, mnemosyne, mosaik-herz, verschraenkungs-insel, emergenz, genesis, risse (if read), and the entries c7, q6.
- Reader 2: kael, lex, selene, nyx, moros, kiko, lia, isabelle, rhys, alex, argus, tsdp, multiplizitaet, did, and the entry q3.
