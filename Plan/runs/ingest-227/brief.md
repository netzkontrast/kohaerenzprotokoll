# Brief — readings from document 227 (step 6)

1 document, one reader, one batch: `ingest-227`. Files go to `Plan/runs/ingest-227/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 227 | `kohaerenz-protokoll-analyse-und-synthese` | 2025-07-29 | „the definitive synthesis“ (an unsigned German analysis) | a German analytic essay in five parts on AEGIS, Kael, the world's physics and the novel's form, under the title „Eine definitive Synthese …“; in content a near version of document 223 (same tables, same Fragment 'O' scenarios, sharing 5 long lines): light pass — readings only where it adds to what 223 put on the page |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (422 lines for `kohaerenz-protokoll-analyse-un`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A near version of the detailed research report (223): read only what it adds — its Dramatica table assigning OS, MC, IC and SS (L45–L48), AEGIS's two paths at the Gödel-Gambit (L142–L143), the transformed Guardians (L151), its Kishōtenketsu application table (L335–L338). Write „the definitive synthesis assigns …“; borrowed theory is its lens. The glued footnote digit `1` is dropped by `--find` — quote around it.

## Pages — document 227, `kohaerenz-protokoll-analyse-und-synthese`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L30, L32, L40, L45, L54, L58, … (42 lines). central (2–4): AEGIS as the Objective Story throughline, „Situation (ein festgefahrener Zustand der Kontrolle)“ (L45); at the Gödel-Gambit two forms of self-erasure — Pfad A, collapse into the Nichts Rauschen (L142), Pfad B, transformation into a paraconsistent frame, keeping its existence by giving up its purpose (L143).
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `algorithmische Melancholie` L151. minor (1–2): the transformed AEGIS marked by ineffiziente Schönheit and algorithmische Melancholie, its Guardians now executing contradictory orders at once (L151).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L32. occurrence: `Emergenz` stands in the SS row's theme, „die Emergenz von Komplexität“ (L48), not AEGIS's emergence.
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L128, L132, L159. minor (1–2): the Gödel-Gambit as the OS climax, the direct confrontation of AEGIS with Kael's integrated state (L132); Juna/V as the catalyst who presents it (L136).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L151. minor (1–2): after AEGIS's transformation its Guardians, now on paraconsistent logic, executing contradictory orders at once (L151).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L40, L47, L48, L136, L160, L252, … (9 lines). minor (1–2): Juna/V as the Impact Character, the „Du“-perspective, „Manipulation/Psychology“ (L47); the relationship Kael ↔ Juna/V as the Subjective Story, „Activity“ (L48); Juna/V as catalyst of the Gödel-Gambit (L136).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L30, L32, L40, L46, L48, L70, … (41 lines). central (1–3): Kael as the Main Character, the „Ich“-perspective, „Fixed Attitude (eine fixierte innere Haltung des Traumas)“ (L46); the rest repeats 223's TSDP table and Gärtner — not read again.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L179, L212, L315. not read: light pass — the same table row as document 223 (L212).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. occurrence: the title (L13).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L102, L178, L191, L213, L315. not read: light pass — the same D2 example and table row as document 223 (L102, L213).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L136, L160, L248, L252. not read: light pass — the same account as document 223 — a non-local back door AEGIS is blind to (L252–L257).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L189, L269. not read: light pass — the same account as document 223 (L189).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L74, L142. minor (1–2): Pfad A: AEGIS dissolving into the „Nichts Rauschen“ it fought (L142).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L102, L179, L191, L211. not read: light pass — the same D2 example and table row as document 223 (L102, L211).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L214. not read: light pass — the same table row as document 223 (L214).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L176, L209. not read: light pass — the same TSDP account as document 223 (L176).

- **`kishotenketsu`** (minor, 1–2; the page is reviewed — readings.py appends under Since review): the table setting the three-act structure against the Kishōtenketsu structure and applying each part to the novel — Ten as the Juna/V connection becoming an active influence that breaks the system's rules (L334–L338).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `did`: `Fragment` (near `psychischefragmentierung`). occurrence: `Fragment` is Fragment 'O' (L226), not psychic fragmentation as a term.
- `kishotenketsu`: `Kishōtenketsu-Struktur` (near `kishotenketsu`). a reading — the application table, see the extra page below.


**Record entries** (one file each):

- **`q8-aegis-after-the-vortex`**: two paths — collapse into the Nichts Rauschen or transformation into a paraconsistent frame (L142–L143); the transformed Guardians executing contradictory orders (L151).

**Not promoted:** as for document 223 — Specification Gaming, Fixes That Fail, LFI and D2, IIT and Φ, the rhizomatic identity, the Gärtner-Axiom, Fragment 'O', the triple helix, the reader's protocol.

**One reader** (light pass): aegis, kael, juna, goedel-gambit, algorithmische-melancholie, guardians, nichts-rauschen, kishotenketsu, and the record q8.

**Chapter readings**: none — the synthesis names parts and acts, not chapters.
