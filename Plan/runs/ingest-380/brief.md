# Brief — readings from document 379 (step 6)

1 document, one reader, one batch: `ingest-380`. Files go to `Plan/runs/ingest-380/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 379 | `untersuche-in-wie-fern-juna-bzw-das-fundament-du` | 2025-11-03 | „das Briefing“ (an unsigned German briefing to an external AI instance) | claims that `Juna/V` and `Das Fundament` resolve four named contradictions (AEGIS's logic as physics, the Genesis-Krise paradox, artificial trauma, Deus ex Machina) and then prepares a plot twist: Juna/V as the exiled other primary part of the Ursprungs-Ich; it calls itself a briefing and a tactical plan, no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (181 lines for `untersuche-in-wie-fern-juna-bz`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A briefing: write „das Briefing schlägt vor / definiert …“ — its solutions and its plot twist are proposals, deciding nothing. Quote the German as written; cut before glued footnote digits, straight quotes and LaTeX ($K\_₀$). No gendered pronoun for Kael or Juna/V — use the names. Note in the readings where the briefing's two accounts differ (L114 vs L154, L47/L120 vs L154–L161).

## Pages — document 379, `untersuche-in-wie-fern-juna-bzw-das-fundament-du`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L25, L29, L38, L47, L62, L90, … (19 lines). central (3–6): AEGIS' logic as a perversion of the true physics, Das Fundament (L29); the Genesis-Krise as a category error — AEGIS' Ursprungs-Ich met a transcendent entity linked to Juna/V and classed Gnosis as entropy (L38, L114); its axiom „Aegis ist, was Aegis verhindert, dass es nicht ist“ and operational closure (L107); not faulty because false but incomplete and isolated, a cancer (L109); the Kernwelten as Skinner boxes (L120).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L90. not read: an occurrence (see below).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L38. minor (1–3): the entity of the Genesis-Krise not (only) entropy; AEGIS classed Gnosis wrongly as Entropie, system noise (L38).
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L161. minor (1–3): Juna/V as a transcendent entity from an „Externen Ebene“ (L92); in the twist Juna/V banished into an Externe Ebene, the Transcendent Exile (L161).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L11. central (3–6): Juna/V as a transcendent entity from an Externe Ebene, a catalyst, not a saviour, giving Gnosis, not Episteme (L64, L92, L135); the entity of the Genesis-Krise as first contact with Juna/V (L113, L114); the twist: Juna/V as the other primary part of the Ursprungs-Ich, exiled in the Genesis-Krise, carrying the whole traumatic load (L148, L161); Juna/V's unreliability as that of an exiled, trauma-holding part (L172).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L29, L47, L64, L92, L94, L117, … (17 lines). central (3–6): Kael's trauma authentic, Kael a primary sentient fragment of AEGIS' Ursprungs-Ich severed in a Zerstückelung (L47, L120); Kael's integration as alignment with Das Fundament (L64, L135); in the twist Kael as the Host part (ANP) that stayed in the system, amnesiac (L159); the finale as bringing Juna/V home (L175).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L120. minor (1–3): AEGIS' later actions, the Kernwelten as Skinner boxes (L120).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L174. minor (1–3): Kael's system (Lex, Nyx, Kiko etc.) as the secondary fragments the Host created to live with the hole Juna/V's exile left (L174).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L73. not read: an occurrence (see below).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L174, L175. minor (1–3): Lex among the secondary fragments (L174); the Host integrating inner parts (Lex, Nyx) before the last integration (L175).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L56, L93, L166. central (3–6): the Moonshine-Link not a Deus ex Machina: an ER=EPR basis (L60), invisible to AEGIS as non-local and sub-protocollar (L62); Kael and Juna/V as maximally entangled quantum information systems joined by an Einstein-Rosen bridge (L94); in the twist maximally entangled because they come from the same substance (L166).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L174, L175. minor (1–3): Nyx among the secondary fragments (L174) and the inner parts integrated before the last integration (L175).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L47, L117, L120, L174, L180. minor (1–3): the TSDP structure as the real wound of the Genesis-Krise (L47); the TSDP structure with ANPs and EPs as the direct wound of the fragmentation (L120).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L47. not read: an occurrence (see below).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Krise` (near `genesis`), `Genesis-Krise-Paradoxon` (near `genesis`). `Genesis-Krise` and `Genesis-Krise-Paradoxon` read on aegis, kael and juna, genesis not read; `Juna/V` and `Juna Album` (a document title, L172) on juna; `Kohärenz Protokoll` the title or the protocol (L73, L120); `Simulation` (L47, „keine Simulation von Trauma“) not the Überwelt; `Emergenz` (L90) the general sense; `Entropie` (L38) AEGIS's misclassification, read on entropie.
- `juna`: `Juna/V` (near `juna`), `Juna Album` (near `juna`). `Genesis-Krise` and `Genesis-Krise-Paradoxon` read on aegis, kael and juna, genesis not read; `Juna/V` and `Juna Album` (a document title, L172) on juna; `Kohärenz Protokoll` the title or the protocol (L73, L120); `Simulation` (L47, „keine Simulation von Trauma“) not the Überwelt; `Emergenz` (L90) the general sense; `Entropie` (L38) AEGIS's misclassification, read on entropie.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). `Genesis-Krise` and `Genesis-Krise-Paradoxon` read on aegis, kael and juna, genesis not read; `Juna/V` and `Juna Album` (a document title, L172) on juna; `Kohärenz Protokoll` the title or the protocol (L73, L120); `Simulation` (L47, „keine Simulation von Trauma“) not the Überwelt; `Emergenz` (L90) the general sense; `Entropie` (L38) AEGIS's misclassification, read on entropie.


**Record entries** (one file each, as `Plan/runs/ingest-375/readings/c16-kael-origin--*.md` and `Plan/runs/ingest-374/readings/q9-moonshine-link-boundary--*.md`):
- **`c16-kael-origin`**: Kael as „ein primäres, sentientes Fragment des Ursprungs-Ichs“ of AEGIS (L47; also L120); in the prepared twist the Ursprungs-Ich as Kael+Juna, split in a Bifurkation, Kael the Host in the system and Juna/V the exile (L154–L161). The briefing holds both accounts and, on the entity, says first Juna/V (L113) and later „eine wahre K₀-Kraft oder etwas anderes“ (L154). Stands nearest the split Ursprungs-Selbst (row 5); recorded, not applied and not decided.
- **`q9-moonshine-link-boundary`**: whose it is — Kael and Juna/V as maximally entangled systems joined by an Einstein-Rosen bridge (L94), in the twist because they come from the same substance (L166); what crosses — Gnosis, not Episteme (L64, L135); toward AEGIS — invisible as non-local and sub-protocollar (L62). Who inside Kael's system feels it is not said. Recorded, the question stays open.

**Pages not read:** `genesis`, `kohaerenz`, `ueberwelt`, `emergenz` — occurrences.

**Internal tension (for the record):** the briefing gives Kael's origin and the Genesis-Krise entity two ways — L47/L113/L120 against the twist of L148–L161 — and calls the second a redefinition; recorded in the C16 entry, no new record.

**Not promoted:** Das Fundament, Exilant, Zerstückelung, Bifurkation, Host/Manager, Ruf zur Ganzheit, Katalysator, the four contradictions as labels; the borrowed concepts (seltsamer Attraktor, ER=EPR, Einstein-Rosen-Brücke, Frame Problem, IFS, Deus ex Machina, Gnosis/Episteme).

**One reader**: aegis, juna, kael, kern-welten, kiko, lex, moonshine-link, nyx, tsdp, externe-ebene, entropie, and the C16 and Q9 entries.

**Chapter readings**: none — the briefing names no chapters.
