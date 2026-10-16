# Brief — readings from document 436 (step 6)

1 document, one reader, one batch: `ingest-437`. Files go to `Plan/runs/ingest-437/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 436 | `kohaerenz-protokoll-umfassendes-konzept` | 2025-04-27 | „the comprehensive concept“ (an unsigned German „Umfassendes Konzept“ in ten numbered sections) | logline, premise, three parts of 13 chapters, characters, setting, concepts, themes, style and a 39-chapter overview of one label per chapter; calls itself a detailed roadmap (L104), no claim of canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (105 lines for `kohaerenz-protokoll-umfassende`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plan: write „the comprehensive concept plans …“ or „the comprehensive concept's Kap 33 …“. Its world lines name mathematicians in parentheses (L29–L32): never write those names nor quote a span containing one — the codes and the Guardians' names may stand. Its trauma symbol (L88) is named only as the document's Kerntrauma symbol, no detail. Its chapter overview gives one label per chapter in three lines (L100 Kap 1–13, L101 Kap 14–25, L102 Kap 26–39), while the part headings put Kap 26 in Part 2 (L51) — recorded, not corrected. Quote the German as written; cut before straight quotes and bold markers. No gendered pronoun for Kael, Juna or AEGIS — use the names (quotations stay verbatim).

## Pages — document 436, `kohaerenz-protokoll-umfassendes-konzept`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L23, L24, L36, L37, L38, L47, … (16 lines). central (4–8): „Eine hochkomplexe, autopoietische KI“ in the unstable Potentialmeer, seeking self-preservation through control and analysis, defined by its function (L23 — the self-referring sentence carries straight quotes: cut before it); AEGIS manifests M as the human avatar Kael and fragments it into 20 simulated Kernwelten (L24); „Antagonistische Kraft, aber keine simple“ evil AI, driven to its limits by M/Kael and the K-J connection (L70 — describe the named limit); AEGIS's system with visible „Rissen“ (L79); Kap 20, 27, 33: „AEGIS-Sabotage“, „AEGIS-Abwehr“, „AEGIS-Kollaps“ (L101, L102).
- **`did`** (minor, 1–4): the census's surfaces — `DID` L24, L69, L85. minor (1–4): Kael experiences the fragmentation into Kernwelten as induced Dissoziative Identitätsstörung (L24); „Erlebt die Fragmentierung als DID“ (L69).
- **`emergenz`** (minor, 1–4): the census's surfaces — `Emergenz` L32, L38, L84. minor (1–4): the fourth world's theme: potentiality, „Emergenz“, creativity, intuition (L32 — quote only the theme words after the code, never the parenthesis).
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L37, L83. minor (1–4): the Potentialmeer as a meta-space of „hoher Entropie“ (L37) and an „entropischer“ meta-space of pure possibility (L77).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L36, L71, L102. minor (1–4): „Juna & K-J Verbindung“: a non-local, sub-protocol connection between Kael and Juna that defies AEGIS's logic and catalyses Kael's integration (L36); Juna as catalyst, source of intuition, anchor of hope, perhaps an aspect of M or an external force, the nature ambivalent (L71).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L24, L25, L36, L38, L46, L65, … (16 lines). central (4–8): Kael as the human avatar of M, fragmented across the Kernwelten and experiencing an induced DID (L24, L69); the journey toward awareness, integration of the parts and liberation from AEGIS (L69); Part 3: Kael takes up the fight, infiltration, final confrontation, transformation (L65); Kap 32 „Transformation Kael/M“ (L102).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L24, L25, L78. central (4–8): AEGIS fragments M/Kael into 20 simulated Kernwelten (L24); each a „Labor“ analysing one aspect and an incoherent „Cache“ of Kael's identity, four in focus (L25); the four worlds by code with theme and Guardian (L29–L32 — never quote the parenthesised names).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — named in the document's general sense.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L71. minor (1–4): Juna connected to Kael by the non-logical „Moonshine-Link“ — cut before the straight quote (L71); the K-J connection's metaphor „Monstrous Moonshine“ (L36).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L23, L37, L65, L77, L83, L87, … (8 lines). minor (1–4): „Ein Meta-Raum reiner Potentialität, hoher Entropie und ontologischer Instabilität“ that threatens AEGIS (L37); visually a fluctuating, iridescent mist of potentiality (L77); Kap 34 „Exodus ins Potentialmeer“ and the new order in it (L102).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). an occurrence: `Guardian` names the Kernwelt Guardians, not the Integrity Guardian.
- `cache-kohaerenz`: `Cache Kohärenz Metapher` (near `cachekoharenz`), `Cache Kohärenz Protokolle` (near `cachekoharenz`), `Cache` (near `cachekohaerenz`), `Cache` (near `cachekoharenz`). a reading, on cache-kohaerenz below.
- `garten-der-stillen-praesenz`: `Garten` (near `gartenderstillenpraesenz`), `Garten` (near `gartenderstillenprasenz`). an occurrence: `Garten` a symbol of Kael's inner world.
- `guardians`: `Kernwelt-Guardians` (near `guardians`), `Guardian` (near `guardians`). a reading, on guardians below.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Cache Kohärenz Metapher` (near `koharenz`), `Cache Kohärenz Protokolle` (near `koharenz`), `Finale Resonanz/Kohärenz` (near `koharenz`). occurrences: the title; `Cache Kohärenz Protokolle` read on cache-kohaerenz.
- `mnemosyne-server-architektur`: `Architekt` (near `mnemosyneserverarchitektur`). an occurrence: `Architekt` is the first world's Guardian.
- `moeglichkeits-garten`: `Garten` (near `moeglichkeitsgarten`), `Garten` (near `moglichkeitsgarten`). an occurrence: `Garten` a symbol of Kael's inner world.
- `mosaik-herz`: `Mosaik` (near `mosaikherz`). an occurrence: `Scherben/Mosaik` a symbol pair, not the Mosaik-Herz.
- `risse`: `Rissen` (near `risse`). a reading, on risse below.


**Pages beyond the draft:**
- **`guardians`** (minor, 1–4): „Kernwelt-Guardians: KI-Instanzen oder Manifestationen“ embodying each world's rules and challenging Kael — `Architekt`, `Netzweber`, `Chaos-Regulator`, `Möglichkeits-Weber` (L73); each paired to one of the four worlds (L29–L32 — give the pairings by code, never the parenthesised names).
- **`cache-kohaerenz`** (minor, 1–2): each Kernwelt an incoherent „Cache“ of Kael's identity — „(Cache Kohärenz Metapher)“ (L25).
- **`risse`** (minor, 1): AEGIS's system „mit sichtbaren“ Risse when unstable — cut before the straight quote (L79).

**Record entries** (one file each, formatted as earlier entries — `ls Plan/runs/ingest-43*/readings/q3-*`, `ls Plan/runs/ingest-42*/readings/q5-*`):
- **`q3-how-many-kern-welten-and-alters`**: the comprehensive concept: AEGIS fragments M/Kael into „20 simulierte“ Kernwelten (L24), four in focus (L25); no count of alters. Before and not against the author's answers of 2026-10-05, which stand.
- **`q5-guardians-and-kern-welten`**: four Guardians, one per focus world — `Architekt`, `Netzweber`, `Chaos-Regulator`, `Möglichkeits-Weber` (L29–L32, L73); four, not five.

**Chapter readings** (batch `ingest-437-kap`, one file per chapter, `Plan/runs/ingest-437-kap/readings/kap-NN--kohaerenz-protokoll-umfassendes-konzept.md`, Kap 1 to Kap 39, formatted as the files in `Plan/runs/ingest-422-kap/readings/`): the chapter's label from the overview (Kap 1–13 L100, Kap 14–25 L101, Kap 26–39 L102), quoted, one bullet; Kap 26 notes that the overview lists it in Part 3 while the part heading puts it in Part 2 (L51, L102). Kap 17 and 28 carry the Kerntrauma: quote only words that are not the symbol.

**Not promoted:** M (Die Entität), Kael/M, the world codes, the four Guardians' names, Kernwunde, Kerntrauma and its symbol, Bunker, Scherben/Mosaik, Garten, Jetzt-Raum, Wächterin/Selbst, Cache-Konflikte, the chapter labels, and the borrowed concepts.

**One reader**: every page above, the two record entries and the 39 chapter readings.
