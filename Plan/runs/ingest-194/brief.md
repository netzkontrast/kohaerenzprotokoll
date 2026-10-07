# Brief — readings from document 194 (step 6)

1 document, one reader, one batch: `ingest-194`. Files go to `Plan/runs/ingest-194/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 194 | `kishotenketsu-fuer-meinen-roman-bitte-plane-ein` | 2025-08-15 | „the Kishōtenketsu plan“ (an assistant reply, „Absolut. Basierend auf …“) | a German chat reply that condenses a 39-chapter draft (a file it names „Absolut.md“) into a 30-chapter outline in four Kishōtenketsu acts — Ki, Shō, Ten, Ketsu (L23–L26); each chapter has `Fokus`, `Handlung`, `AEGIS' Perspektive` and `Konzept & Recherche`; worlds are W1–W4, the Guardians are `Wächter`, and the alters go by epithets („Die Ruhige“, „Die Mutige“, „Die Präzise“); it makes no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (383 lines for `kishotenketsu-fuer-meinen-roma`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plan in a chat reply: write „the Kishōtenketsu plan proposes / has …“; its chapter numbers count a 30-chapter book (the session wrote the chapter readings, `ingest-194-kap`). German — quote as written; cut before inner straight quotes (the alters' epithets and many terms stand in them); `--find` drops digits glued to words (W1 shows as W) — quote around them.

## Pages — document 194, `kishotenketsu-fuer-meinen-roman-bitte-plane-ein`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L23, L24, L25, L26, L47, L48, … (49 lines). central (2–4): its perspective in every chapter: an anomalous latency „der“ unit Kael (L47) — read L47; it recognises in the Ten that Kael is no system fault (L25); confronted with a truth its axioms define as impossible, forced into an unsolvable loop that breaks its core programming (L370) — cut before the inner quotes; still and transformed at the end (L380).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L23, L57, L139. minor (1–2): the first inner alters in the Ki (L23); the alters as epithets — read L57 („Die Mutige“) and L139 (the Schatten's Drall) — quote around the inner quotes.
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L69. minor (1–2): „Cerberus (Wächter W“ — read L69 and quote around the digit: he logs a phase transition from panic to coherent performance.
- **`emergenz`** (minor, 1–4): the census's surfaces — `Emergenz` L174. minor (1–2): „Kaels“ unity as an emergent property of his parts' interaction, which AEGIS's top-down control cannot grasp (L174) — cut before inner quotes.
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L26, L364. central (2–4): Kael defeats AEGIS „nicht durch Gewalt“ but by the Gödel-Gambit (L26) — cut before the inner quotes; chapter 29, „Das Gödel-Gambit (Climax)“ (L364); he sends out his Sinnbild, the truth that coherence comes from integrating contradictions (L369); AEGIS's unsolvable loop (L370).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L23, L46, L79, L81, L254, L278. minor (1–2): in the gap of the Gegentakt Kael feels „Junas direkte Präsenz“ (L79) — read the line; Juna exists in Kairos, qualitative time (L81); Juna-sharpened intuition sees through the artificial warmth (L254).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L21, L23, L24, L25, L26, L46, … (72 lines). central (2–4): „Wir lernen Kael als fragmentierten Insassen“ in a world AEGIS controls (L23); he begins to explore and train his inner multiplicity (L24); his irrevocable decision to live by his own rhythm (L25); he becomes „Gärtner“, not fighter (L380) — quote around the inner quotes.
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L80, L81. minor (1–2): „Kairos/Sophia (Wächter W“ — read L80, quote around the digit: they read Kael's listening as a failure; Chronos against Kairos, Juna in Kairos (L81).
- **`kishotenketsu`** (minor, 1–4): the census's surfaces — `Kishōtenketsu` L11, L17. minor (1–2): the reply follows „der japanischen Erzählstruktur des“ Kishōtenketsu (L11); the four acts Ki, Shō, Ten, Ketsu (L23–L26).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L17. occurrence: „Die Architektur der Kohärenz“ is a section heading (L17).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L91. minor (1–2): LogOS as Wächter of W1 classifies Kael's act as a deliberate protocol violation (L91) — quote around the digit.
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L58, L102. minor (1–2): Mnemosyne as Wächter of W2 registers a stochastic variance (L58) and is unsettled by Kael's cold reaction (L102).
- **`moeglichkeits-garten`** (minor, 1–4): the census's surfaces — `Möglichkeits-Garten` L79, L128. minor (1–2): W4 as the Möglichkeits-Garten, where Kael listens to the pauses of the system's beat (L79) and leaves a painful belief behind (L128) — quote around W4.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Multiplizität` L24, L171, L182, L185, L324. minor (1–2): Kael trains his inner multiplicity (L24); „Die fundamentale Selbsterkenntnis und Akzeptanz der eigenen Multiplizität“ (L182); masterly functional multiplicity (L324).
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Resonanz-Landschaft` alone on L57. minor (1–2): „In der organischen Resonanz-Landschaft“ W2 (L57) — quote before the digit.
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Glitch` alone on L216. minor (1–2): the `Glitch` in a time jump AEGIS causes, where „die Präzise“ reads the simulation's version numbers (L216) — quote around the inner quotes; a Glitch, not the word Risse — say so.
- **`sophia`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Sophia` alone on L80. minor (1–2): joined with Kairos as Wächter of W4 (L80).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L216. occurrence: the simulation in the Glitch (L216) and the simulation theory and The Matrix (L218) are concepts of the plan, nothing of the Überwelt.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `sophia`: `Kairos/Sophia` (near `sophia`). a reading — on sophia above.
- `ueberwelt`: `Die Simulationstheorie` (near `simulation`). occurrence: `Die Simulationstheorie` is a borrowed concept (L218).


**Record entries** (one file each):

- **`q5-guardians-and-kern-welten`**: Wächter per world — LogOS W1, Mnemosyne W2, Cerberus W3, Kairos/Sophia W4 (L58, L69, L80, L91).
- **`q8-aegis-after-the-vortex`**: AEGIS's core programming broken by the Gödel-Satz; at the end „still, transformiert“ (L370, L380).

**Chapters:** 30 chapter readings, written by the session (`Plan/runs/ingest-194-kap/brief.md`).

**Not promoted:** the four act names and the chapter fields, W1–W4, the alters' epithets (Die Ruhige, Die Mutige, Die Präzise, the Schatten), Gegentakt, Drall, Sinnbild, and the borrowed concepts (Epoché, Chronos/Kairos, Wu Wei, DBT, Śūnyatā).

**Two readers**, disjoint: (1) kael, juna, alters, multiplizitaet, emergenz, goedel-gambit, kishotenketsu and the record q8; (2) aegis, logos, mnemosyne, cerberus, kairos, sophia, moeglichkeits-garten, resonanz-landschaft, risse and the record q5.
