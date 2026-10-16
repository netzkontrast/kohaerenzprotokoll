# Brief — readings from document 237 (step 6)

1 document, one reader, one batch: `ingest-237`. Files go to `Plan/runs/ingest-237/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 237 | `kohaerenz-protokoll-finaler-bauplan` | 2025-07-29 | „the definitive framework“ (an unsigned German analytical plan) | a German plan in four parts, „Ein Definitives Narratives und Ontologisches Framework“ — AEGIS, Kael's parts, the Moonshine-Link and Das Fundament, the prose — of the same family as the detailed research report (223) and the final pillars report (236); it says the plot „folgt definitiv“ Szenario B (L136): its claim, not canon; light pass where it repeats them |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (264 lines for `kohaerenz-protokoll-finaler-ba`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plan that calls itself definitive: write „the definitive framework states …“; its „definitiv“ (L13, L136) is its claim. It belongs to a family of near versions (223, 227, 236): read only what it adds — Szenario B as the ending (L136), only Pfad B (L69), the transformed Guardians (L79), AEGIS's existential vacuum and ambivalent end (L81–L83), its own roster wording for Kael and Selene (L145, L149), the Gödel-Satz said of Kael himself (L195), the Moonshine-Link hedged as metaphorical or literal (L167). Glued footnote digit `1` — quote around it.

## Pages — document 237, `kohaerenz-protokoll-finaler-bauplan`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L19, L23, L31, L35, L43, L47, … (30 lines). central (2–4): Pfad B, „keine Niederlage, sondern eine erzwungene, radikale Evolution“ (L69); the loss of its directive plunging it „in ein existenzielles Vakuum“ (L81); its final aims and methods left „bewusst ambivalent und unklar“ (L83).
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `algorithmische Melancholie` L81. minor (1–3): „algorithmische Melancholie“ as a symptom of the transformed AEGIS, an existential vacuum after the loss of its directive (L81).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L136. occurrence: `Emergenz` in a general sense (L136); not AEGIS's emergence.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L63. occurrence: `Entropie` in „systemische Entropie“ of Kael's state (L63); not read.
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L59, L63, L91. minor (1–3): the climax set off by the Gödel-Gambit (L63); the Gödel-Satz said of Kael's state (L65) and of Kael himself, „Kael ist der Gödel-Satz für“ the system (L195).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L79. minor (1–3): after the transformation „Die Guardians, die nun auf parakonsistenter Logik operieren“ (L79).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L65, L92, L153, L165, L167, L193, … (8 lines). minor (1–3): Juna/V as catalyst of the Gödel-Gambit (L65); Kael and Juna/V „metaphorisch (oder im Rahmen der Weltphysik buchstäblich)“ entangled (L167).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L31, L35, L47, L49, L53, L55, … (36 lines). central (2–3): the plot „folgt definitiv“ Szenario B, Der Gärtner: Kael resists the temptation of direct control (L136); in the roster table „Primärer Diplomat und Schnittstelle zur Außenwelt“ (L145); „Kael ist der Gödel-Satz für“ the system (L195).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L112, L147, L213. not read: light pass — the same roster as the detailed research report (L147).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. occurrence: the title (L13).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L49, L110, L124, L148, L213. not read: light pass — the same D2 example and roster as the detailed research report (L49, L148).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L65, L92, L161, L165. minor (1–3): an exploit operating „auf einer für AEGIS unzugänglichen Ebene der Realität“ (L165); hedged as metaphorical or literal (L167); also „architektonische Hintertür“ (L92).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L118. occurrence: `Multiplizität` stands in a heading (L118); the same account as the detailed research report.
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L33. not read: light pass — the same account as the detailed research report (L33).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L51, L112, L124, L146. not read: light pass — the same D2 example and roster as the detailed research report (L51, L146).
- **`personas`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Persona` alone on L227. occurrence: `Persona` names the meta-narrator as a persona in the narrative system (L227), not the consciousness instances.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L149. minor (1–3): in the roster table „Das integrierte Selbst; bewusster Kern des Systems“ (L149).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L108, L144. not read: light pass — the same TSDP account as the detailed research report (L108).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Paradoxon der Fehlausgerichteten Kohärenz` (near `koharenz`), `wahre Kohärenz Protokoll` (near `koharenz`), `Kohärenz Protokoll` (near `koharenz`). occurrence: the title, `wahre Kohärenz Protokoll` and the Paradox of Misaligned Coherence, AEGIS's (not read again).
- `multiplizitaet`: `funktionalen Multiplizität` (near `multiplizitat`). occurrence: `funktionalen Multiplizität` stands in the account shared with 223.
- `potentialmeer`: `Potentialmeers` (near `potentialmeer`). occurrence: `Potentialmeers` in the shared account; not read again.


**Record entries** (one file each):

- **`q8-aegis-after-the-vortex`**: only Pfad B, a forced radical evolution (L69); an existential vacuum, its final aims left ambivalent (L81–L83).
- **`q1-guardians-and-aegis`**: after the transformation the Guardians operate on paraconsistent logic (L79).

**Not promoted:** as for the detailed research report — and Szenario B (Der Gärtner), Die Kosten der Gnosis, Host Kael, the Meta-Erzähler.

**One reader** (light pass): aegis, kael, juna, selene, guardians, goedel-gambit, moonshine-link, algorithmische-melancholie and the records q8, q1.

**Chapter readings**: none.
