# Brief — readings from document 470 (step 6)

1 document, one reader, one batch: `ingest-470`. Files go to `Plan/runs/ingest-470/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 470 | `juna` | 2025-07-30 | „the Fundament and Juna/V concept“ (an unsigned German concept text in two role-voiced passes, as „Konzept-Dramaturg“ L11 and „Narrativer Architekt“ L54) | defines Das Fundament and the Juna/V connection with their mechanics, roles and rules against a Deus ex Machina; the first pass breaks off at L52; it calls the two concepts the world's transcendent pillars (L11), a claim recorded, never applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (105 lines for `juna`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A concept text in role voices: write „the Fundament and Juna/V concept defines …“; the role voices are the document's, never a person. Two passes repeat one outline — cite the line that carries the wording. No gendered pronoun for Kael, Juna or AEGIS — use the names (quotations verbatim, including the document's „Sie“ and „Ihre“). Never write a real person's name; cut before inner „…“, bold and straight quotes.

## Pages — document 470, `juna`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L21, L25, L35, L37, L39, L41, … (24 lines). central (4–8): the Paraiyas as aspects of reality AEGIS rejects (L21); Das Fundament offers a deeper definition of coherence against AEGIS's (L25); AEGIS structurally blind to the connection (L91); AEGIS accidentally created M-inspired simulations (L91); AEGIS takes Juna/V as an anomaly, a non-quantifiable variable and a source of entropy and instability (L97).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L23. minor (1–4): Das Fundament as a strange attractor towards which the system tends (L23); weak emergence named (L23).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L97. minor (1–4): AEGIS perceives Juna/V as a critical source of entropy and instability (L97).
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L95. minor (1–4): in the finale Juna/V helps Kael present the Gödel-Gambit (L95); the first pass writes a Gödel-Satz at the same place (L43) — record both as the document writes them, never expand.
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L11. central (4–8): the Juna/V connection a disruptive vector (L35); Juna/V an external entity or anomaly whose exact nature stays mysterious (L37), the ambiguity a deliberate technique (L85); Juna/V embodies authentic connection and non-quantifiable emotion (L87); Juna/V as Impact Character, helping Kael in the finale (L95); AEGIS takes Juna/V as a dangerous anomaly and source of entropy (L97); the distance of Juna/V may be ambivalent, possibly after the reboots (L104); the mystery stays (L103).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L23, L25, L29, L30, L31, L39, … (23 lines). central (4–8): Das Fundament does not intervene to save Kael (L23) and gives Kael the right question, not the answer (L31); Kael's access to it earned through inner integration (L76), Kael's consciousness becoming isomorphic with it (L76); the link between Kael and Juna/V non-local and sub-systemic (L39); in the finale an epistemological victory, not a fight (L95).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L97. minor (1–4): the Kernwelten named once in the AEGIS perspective on Juna/V (L97).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — the title line and the protocol's name.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L39, L41, L89. minor (1–4): the link between Kael and Juna/V as the Moonshine-Link, non-local and sub-systemic (L39, L41, L89); read through Monstrous Moonshine (L91 — describe).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L76. not read: an occurrence — L76 names multiplicity in passing in the earned-insight rule.
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Glitch` alone on L91. minor (1–4): qualia that resist formal explanation are a fundamental Glitch for the Kohärenz Protokoll (L91 — describe around the inner quotes).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L87. not read: an occurrence — `Simulation` on L87 is the simulated reality, not the Überwelt.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `emergenz`: `schwache Emergenz` (near `emergenz`). `schwache Emergenz` read on emergenz.
- `juna`: `Juna/V-Verbindung` (near `juna`), `Juna/V` (near `juna`), `Kael-Juna (K-J) Verbindung` (near `juna`). `Juna/V`, `Juna/V-Verbindung` and `Kael-Juna (K-J) Verbindung` read on juna.
- `kohaerenz`: `alternatives Kohärenzprotokoll` (near `koharenz`), `Kohärenz Protokoll` (near `koharenz`). an occurrence: the protocol's name and an alternative protocol.
- `potentialmeer`: `Potentialmeers` (near `potentialmeer`). an occurrence: the genitive `Potentialmeers` in passing.


**Record entries:** none.

**No chapter readings**: the document names the finale and the final act, no chapter number.

**Not promoted:** Das Fundament, Paraiyas, Paradoxon X, the Deus-ex-Machina rules, Impact Character, Reboots, the role voices, and the borrowed concepts.

**One reader**: every page above.
