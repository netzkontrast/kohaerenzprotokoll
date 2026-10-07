# Brief — readings from document 184 (step 6)

1 document, one reader, one batch: `ingest-184`. Files go to `Plan/runs/ingest-184/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 184 | `roman-konzept-reduktion-und-kernfindung` | 2026-03-31 | „the reduction report“ (titled `Die Ontologische Reduktion: Strategischer Analysebericht zur Neuausrichtung des Projekts Kohärenz Protokoll`) | a German strategic report that surveys the corpus, reads the Dual Kernel Theorie as the novel's heart, proposes a core story, a pitch, four cuts (group-theory names, NovelOS, Nova Ardent's double role, transition algorithms), a three-layer model and a 39-chapter gradient; it advises the author and claims its survey of over 200 documents (L13) — recorded, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (212 lines for `roman-konzept-reduktion-und-ke`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A report that recommends: write „the reduction report proposes / reads / recommends …“, never as settled; where it reports other documents (the Finaler Bauplan, the March 2026 documents, NovelOS) the claim is that document's as the report gives it. German — quote as written. The kernel symbols were lost in the export (L48–L58 and the table's last column show empty brackets or gaps) — never quote across a gap; glued reference digits end many sentences (`…definiert.5`) — cut before the digit; the tables have escaped bold — quote the plain words.

## Pages — document 184, `roman-konzept-reduktion-und-kernfindung`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L40, L50, L52, L64, L65, L66, … (15 lines). central (2–4): the coherence kernel „personifiziert durch die KI AEGIS“ (L50); trauma fragments classed as „Rauschen“ and eliminated (L52); AEGIS's deletions heat the system, the Risse its thermal consequences (L64); its classic logic driven into collapse by Kael's integration (L65); in the corpus table, from simple antagonist to „einer komplexen, tragischen Gottheit“ (L40).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L70, L128. minor (1–2): the drafts differ on the number and role of the parts, and the report proposes a reduction to the most functional (L70); the group-theory naming of every alter as a cut (L128).
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L46, L184. minor (1–2): „Das Herzstück des Romans ist die Dual Kernel Theorie (DKT)“ (L46); the DKT made tangible through the Risse in Act II (L184).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L58. occurrence: „evolutionäre Emergenz“ (L58) is the general word, not the wiki's Emergenz.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L25. occurrence: „narrativer Entropie“ (L25) is the corpus's overstructuring, not the world's entropy; read entropy as world-law only on kollaps-kernel.
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L185. minor (1–2): „Das Gödel-Gambit“ in Act III, Kap. 27–39 (L185) — quote the plain words.
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L81. minor (1–2): Nyx's sphere in the table, „(Grenzfeste)“ (L81) — cut around the lost symbol.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L84, L106, L118, L189. central (2–4): „Juna (The Other)“, resonance partner and catalyst of transcendence (L84); „Juna ist ein Fragment der Wahrheit, die Kael vor Jahren zersplitterte“ (L118); a connection AEGIS's logic cannot grasp (L118); the love story as the reader's anchor (L106).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L50, L58, L64, L65, L68, L70, … (14 lines). central (2–4): not a figure with a disorder but „die Manifestation eines komplexen adaptiven Systems“ (L70); „Kael (Host)“ in Logos-Prime (L79); an unreliable narrator by his neurological architecture (L106); a living paradox for AEGIS, integrated into a „funktionalen Multiplizität“ (L65); the pitch: he lives in the perfect silence of Logos-Prime (L116).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelt` L50, L155. minor (1–2): KW1 Logos-Prime to KW4 Kairos-Potentialis and their somatic signs (L90); the transition rules between the Kernwelten as a cut (L155).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L82. minor (1–2): „Kiko (Exile)“, primary pain, bearer of the secret, hunted (L82).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the report's title and the project's name (L11).
- **`kohaerenz-kernel`** (minor, 1–4): the census's surfaces — `Kohärenz-Kernel` L48. minor (1–2): „Kohärenz-Kernel“ (L48): absolute internal consistency, the coherence theory of truth, reversible computation (L50); its „kristallinen Stagnation“ (L52).
- **`kollaps-kernel`** (minor, 1–4): the census's surfaces — `Kollaps-Kernel` L54. minor (1–2): „Kollaps-Kernel“ (L54): irreversible deletion, entropy and the correspondence theory of truth (L56); the EPs in Kael's matrix and the condition for real consciousness (L58).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L80. minor (1–2): „Lex (Analyst)“, system administrator allied with AEGIS (L80).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L82, L90. minor (1–2): Kiko's sphere „(Mnemosyne)“ (L82); KW2 Mnemosyne-Archipel with visceral gut feelings and sudden cold (L90).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L65. minor (1–2): Kael's integration „zu einer“ functional multiplicity that establishes a paraconsistent logic (L65).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L56, L116. minor (1–2): the collapse kernel is „das“ Nichts Rauschen, the Lacanian Real breaking in (L56) — cut around the lost symbol; through the Risse the Nichts Rauschen enters (L116).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L81. minor (1–2): „Nyx (Protector)“, rage and defence, fights AEGIS (L81).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L106. occurrence: „die plötzlichen Wechsel der Realitätsebene“ (L106) is the thriller's effect on the reader, not a claim about the levels.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L64, L116, L184. central (2–4): the Risse as „die direkten thermischen Konsequenzen einer psychologischen Lüge“ (L64); entropic heat burns the edges of reality and through the Risse the Nichts Rauschen enters (L116); the DKT experienced through the Risse in Act II (L184).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L37, L70. minor (1–2): the clinical theory that „diktiert die ontologischen Gesetze seiner Welt“ (L70); in the corpus table (L37).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L37. occurrence: „direkte Abbildung in der Simulation“ (L37) is a corpus table cell about psychology, nothing of the Überwelt.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). occurrence: KW3's name (L90), on kern-welten.
- `kairos`: `Kairos-Potentialis` (near `kairos`). occurrence: KW4's name (L90), on kern-welten.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz Protokoll: Finaler Bauplan` (near `koharenz`). occurrence: the Protokoll's name, and the title of a document the report cites, „Kohärenz Protokoll: Finaler Bauplan“ (L25).
- `logos`: `Logos-Prime` (near `logos`). occurrence: Logos-Prime is KW1, the world, not the Guardian (L79, L90, L116) — J49; on kern-welten and kael.
- `multiplizitaet`: `funktionalen Multiplizität` (near `multiplizitat`). a reading — on multiplizitaet above.
- `residual-echos`: `Echo` (near `residualechos`). occurrence: „das Echo einer grausamen Vergangenheit“ (L116) is a figure of speech in the pitch.


**Record entries** (one file each):

- **`c16-kael-origin`**: „Juna ist ein Fragment der Wahrheit, die Kael vor Jahren zersplitterte“ (L118).
- **`q3-how-many-kern-welten-and-alters`**: the drafts differ on the number of parts and the report proposes a reduction (L70); its table keeps Kael, Lex, Nyx, Kiko, Limina and Juna (L79–L84); four KW (L90).
- **`q9-moonshine-link-boundary`**: a connection „die AEGIS’ Logik nicht erfassen kann“ (L118).

**Chapters:** none — the 39-chapter gradient gives only act ranges (Kap. 1–13, 14–26, 27–39, L183–L185).

**Not promoted:** NovelOS and ARCHON, Nova Ardent and Flicker, Limina (no page; on Q3), the somatic rulebook, the three-layer model and the 39-chapter gradient, the borrowed theories (Lacan's Real, Landauer, Gödel, Bekenstein, Hawking radiation), the group-theory names (Lyons, Conway, McLaughlin).

**Two readers**, disjoint: (1) kael, juna, alters, lex, nyx, kiko, grenzfeste, mnemosyne, kern-welten, tsdp, multiplizitaet and the records c16, q3, q9; (2) aegis, dkt, kohaerenz-kernel, kollaps-kernel, nichts-rauschen, risse, goedel-gambit.
