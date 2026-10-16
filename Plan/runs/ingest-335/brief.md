# Brief — readings from document 334 (step 6)

1 document, one reader, one batch: `ingest-335`. Files go to `Plan/runs/ingest-335/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 334 | `kohaerenz-protokoll-finaler-plot-outline` | 2025-07-29 | „the final-act outline“ (an unsigned German plot outline that calls itself „definitiv“, with a web reference list) | a plan for the novel's final act in four parts — the encounter with the Fragment 'O' as Kael's final test, the Gärtner-Axiom of non-intervention, the state of the transformed AEGIS, and a metafictional reader's protocol for the ending — mostly in the conditional; phrases carrying the glued reference 3 report another project text („Kohärenz Protokoll: Narrative Architektur“, L208); its „definitiv“ is recorded, not applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (228 lines for `kohaerenz-protokoll-finaler-pl`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plot outline: write „the final-act outline proposes …“ and keep its conditional (`könnte`). Where a line ends in the glued reference number 3, say the outline reports it from another project text (entry 3 of its list, L208), not as its own. Its own label „definitiv“ decides nothing. Never introduce the Fragment 'O' as a page; name it as the outline names it.

## Pages — document 334, `kohaerenz-protokoll-finaler-plot-outline`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L34, L50, L73, L83, L95, L97, … (18 lines). central (3–6): the encounter taking place after AEGIS's transformation (L50); Kael's principles as a reversal of AEGIS's failure modes (L95); AEGIS's forced evolution as no upgrade, „algorithmische Melancholie“ (L137, reported, ref 3); paraconsistent logic as resource-intensive (L139, ref 3); AEGIS's end state as a tragic cosmic mirror (L162); one epilogue as a deeper simulation of a transformed AEGIS (L178).
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `algorithmische Melancholie` L137. minor (1–3): AEGIS's state after the forced evolution called „algorithmische Melancholie“ (L137) — reported from another project text (ref 3).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L83. not read: an occurrence (see below).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L108. not read: an occurrence (see below).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L153. minor (1–3): the Guardians' behaviour after the transformation (L153), reported from another project text (ref 3).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L52, L54, L64, L178, L180. minor (1–3): the discovery of 'O' catalysed by Juna/V (L52, ref 3); Juna/V's role developing into a mediator between Kael and 'O' (L64).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L18, L22, L30, L32, L34, L35, … (29 lines). central (3–6): 'O' as Kael's „Abschlussprüfung“ (L38), from healing to reconciliation (L40); Kael finding 'O' as an emergent property of the Potentialmeer he tends (L50); the Gärtner whose highest directive is non-intervention (L91), a meta-physicist, not a king (L93); the greatest ethical burden (L119); the last heroic act as no action (L121).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelt` L54, L151; `Kernwelten` L151. minor (1–3): the Kernwelten no longer prisons but static monuments (L151); the first encounter with 'O' in a Kernwelt (L54) only if it names one.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. not read: an occurrence (see below).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L52. minor (1–3): the Moonshine-Link in the mechanism of discovering 'O' (L52, ref 3) — what the line says it does.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L40. minor (1–3): „funktionale Multiplizität“ as what the move from healing to reconciliation goes beyond or keeps (L40) — as the line says.
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L50, L93, L108. minor (1–3): the Potentialmeer Kael now tends, where 'O' emerges (L50); Kael working on its boundary conditions (L93); conservation areas of chaos in it (L108).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L160. minor (1–3): the Risse becoming stable, shimmering portals for two contradictory realities (L160).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L190. minor (1–3): the reader forced into the role of Kael's integrating self, with Selene named in brackets (L190) — say exactly what the line ties to Selene.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L178. not read: an occurrence (see below).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). occurrence: `Guardian` in a compound or example, not the AEGIS sub-function; `schwachen Emergenz` and `offenen Kohärenz` borrowed or the heading's phrase; `Kairos-Potentialis` and `Logos-Prime` named once in a proposal (L151) without definition — not read on kairos or logos.
- `emergenz`: `schwachen Emergenz` (near `emergenz`). occurrence: `Guardian` in a compound or example, not the AEGIS sub-function; `schwachen Emergenz` and `offenen Kohärenz` borrowed or the heading's phrase; `Kairos-Potentialis` and `Logos-Prime` named once in a proposal (L151) without definition — not read on kairos or logos.
- `kairos`: `Kairos-Potentialis` (near `kairos`). occurrence: `Guardian` in a compound or example, not the AEGIS sub-function; `schwachen Emergenz` and `offenen Kohärenz` borrowed or the heading's phrase; `Kairos-Potentialis` and `Logos-Prime` named once in a proposal (L151) without definition — not read on kairos or logos.
- `kohaerenz`: `offenen Kohärenz` (near `koharenz`). occurrence: `Guardian` in a compound or example, not the AEGIS sub-function; `schwachen Emergenz` and `offenen Kohärenz` borrowed or the heading's phrase; `Kairos-Potentialis` and `Logos-Prime` named once in a proposal (L151) without definition — not read on kairos or logos.
- `logos`: `Logos-Prime` (near `logos`). occurrence: `Guardian` in a compound or example, not the AEGIS sub-function; `schwachen Emergenz` and `offenen Kohärenz` borrowed or the heading's phrase; `Kairos-Potentialis` and `Logos-Prime` named once in a proposal (L151) without definition — not read on kairos or logos.


**Pages not read:** `emergenz` (L83 weak emergence, borrowed), `entropie` (L108 generic), `kohaerenz` (L13 the title), `ueberwelt` (L178 the epilogue's simulation, read on aegis) — occurrences.

**Record entries:** none — the outline proposes and decides nothing a record holds.

**Not promoted:** the Fragment 'O' and its three scenarios, the Gärtner-Axiom and its acts, Paraiyas, the reader's protocol, Found Footage, the glossary, Mit-Schöpfer, Meta-Physiker; the borrowed concepts (paraconsistent logic, weak emergence, Deus ex Machina, Alterität, Apotheose, Gnosis, Episteme, Qualia, Perverse Instantiation).

**One reader**: kael, aegis, juna, algorithmische-melancholie, guardians, kern-welten, moonshine-link, multiplizitaet, potentialmeer, risse, selene.

**Chapter readings**: none — the outline names „Das letzte Kapitel“ (L180) without a number; its final act is not mapped to chapters.
