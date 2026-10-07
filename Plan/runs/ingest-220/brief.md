# Brief — readings from document 220 (step 6)

1 document, one reader, one batch: `ingest-220`. Files go to `Plan/runs/ingest-220/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 220 | `kohaerenz-protokoll-duale-dramatica-storyform-synthese` | 2026-04-28 | „the dual storyform synthesis“ (an unsigned German TRACE report) | a report in eight TRACE steps that builds two opposed Dramatica storyforms — A for AEGIS (Universe), B for Kael (Mind) — with Juna/V as Impact Character, a Kishōtenketsu progression for Kap 1–13 and a „5D-Lift“ synthesis; it calls its own audit passed and itself „ausführungsbereit“ — a claim, not canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (197 lines for `kohaerenz-protokoll-duale-dram`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A synthesis report that assigns storyform values: write „the dual storyform synthesis assigns …“ or „… constructs …“; its own verdicts („erfolgreich abgeschlossen“, „100%“) are recorded as its claims. Its storyform letters are its own (A = AEGIS, B = Kael) — say so, never map them onto the repository's storyforms. The sentence on L58 tied to footnote 2 („AEGIS ist, was AEGIS verhindert …“) is another text's directive the report cites — attribute it as cited. Empty symbols (`Kohärenz-Kernel ( / )`) and glued footnote digits: quote around them.

## Pages — document 220, `kohaerenz-protokoll-duale-dramatica-storyform-synthese`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L32, L50, L54, L56, L58, L62, … (22 lines). central (3–6): Storyform A: AEGIS in the class Universe, concern Understanding, issue Certainty vs. Potentiality (L64–L66); problem Order/Faith, solution Chaos/Disbelief, which AEGIS refuses (L71–L72); steelmanned as a tragic, logic-driven instance whose purpose is preventing total entropic collapse (L58); falsified by its own coherence enforcement, the Paradox of Misaligned Coherence (L76); in the synthesis not erased but disintegrating into an algorithmic melancholy, an emergent rule set inside the creative chaos (L178).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Zero-Trust` alone on L45. minor (1–3): the Zero-Trust Execution Model (ZTEM) as one of AEGIS's protocols, beside RIVE and RTSV (L65), in the order row of the isomorphy table (L45); its brilliance does not save AEGIS (L76).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L45. minor (1–3): „Zwangskontrolle durch funktionale Alters“ in the order row (L45); the TSDP-Alter table (L106–L112) — six alters with function, Dramatica role and world; in the synthesis they exist as independent orthogonal vectors, an Inner Council (L184).
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L20, L44. minor (1–3): the Dual Kernel Theory as the second „Werk-Anker“: the simulated world spanned between the ordering Kohärenz-Kernel and the chaotic-creative Entropie-Kernel (L20) — quote around the empty symbols; integrated in the audit (L156).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L72. occurrence: „der notwendigen Prämisse für Emergenz“ (L72) names emergence in general as what Chaos allows, not AEGIS's emergence.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L28. minor (1–3): „die Integration von Trauma (Entropie)“ as the epistemological centre (L28) — trauma as entropy; „traumatische Entropie“ AEGIS tries to erase (L50); Logos-Prime collapsing under the Entropie (L176). Bears on C2.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L120, L124, L125, L127, L142. minor (1–3): „Juna/V (Impact Character)“: Juna (or V) as the transformative catalyst who manipulates Kael out of his Mind prison (L120); class Psychology, concern Future, issue Choice (L122–L124); demonstrating the Moonshine Resonance vector (K-J Vector) (L125); the relationship throughline Kael ↔ Juna in Physics/Becoming/Commitment (L127–L133).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L50, L78, L80, L82, L88, L89, … (23 lines). central (3–6): Storyform B: Kael as protagonist and entropic counter-force (L80); not a classic hero but a fractal system „System Kael“ under TSDP, holding the correspondence theory of truth and Dialetheismus (L82); class Mind, concern Memories, issue Truth vs. Falsehood (L88–L90); problem Unproven, solution Proven (L95–L96); „Kael (Host / ANP)“ in the alter table (L107); Fragment Alpha in Logos-Prime (L140); Steadfast, refusing Order (L176); breaking up the concept of fusion in Kairos-Potentialis (L182).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L110, L184. minor (1–3): „Kiko (EP)“, bearer of emotional sensitivity, role Emotion, Mnemosyne-Archipel (KW2) (L110) — quote around the digit; Kiko (Sensibilität) in the synthesis (L184).
- **`kishotenketsu`** (minor, 1–4): the census's surfaces — `Kishōtenketsu` L30, L138, L159. minor (1–3): the Kishōtenketsu structure replacing linear hero's journeys and the three-act structure (L30, L138); its four parts mapped to Kap 1–13 (L140–L143); preferred in the audit (L159).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the title (L11).
- **`kohaerenz-kernel`** (minor, 1–4): the census's surfaces — `Kohärenz-Kernel` L20, L45, L178. minor (1–3): the ordering Kohärenz-Kernel of the DKT (L20); in the order row with ZTEM and information preservation (L45); the synthesis as the Aufhebung of the Kohärenz-Kernel (L178) — quote around the empty symbols.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L32, L108, L184. minor (1–3): „Lex (ANP)“, rationalist, strict problem avoidance, cognitive control, role Reason, Logos-Prime (L108); Lex (Analyse) in the synthesis (L184).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L112, L114, L184. minor (1–3): „Moros (EP)“, bearer of existential emptiness and collapse, role internal antagonist, Cerberus-Labyrinth (L112); activated by a trigger with Nyx (L114); Moros (Schmerz) in the synthesis (L184).
- **`mosaik-herz`** (minor, 1–4): the census's surfaces — `Mosaik-Herz` L180. minor (1–3): the heading „Das Mosaik-Herz: Die Etablierung der Funktionalen Multiplizität“ (L180) and the „Mosaic Heart“ integrated in Ketsu, Kap 9–13 (L143).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L96, L159. minor (1–3): functional multiplicity as resilient result of accepting true contradictions and integrating trauma (L28); reached through the element Proven (L96); the 5-dimensional architecture (Functional Multiplicity) (L172); prioritised in the audit (L159).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L109, L114, L184. minor (1–3): „Nyx (EP)“, fight response, hypervigilant protector computing NP-hard TSP problems, role Contagonist / Skeptic, Cerberus-Labyrinth (KW3) (L109); Nyx (Verteidigung) in the synthesis (L184).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L48. minor (1–3): „Risse im Gewebe der Raumzeit“ as symptom, digital waste heat from information erasure (L48); the physical Risse (Glitches) as the equivalent of Kael's flashbacks (L50); AEGIS's system showing Risse in Shō, Kap 4–5 (L141); closed by the gravity waves of the relationship (L134).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L111, L184. minor (1–3): „Selene (ANP)“, creative intelligence, integrator, role Guardian, Kairos-Potentialis (KW4) (L111) — quote around the digit; Selene (Integration) in the synthesis (L184).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L21, L44, L82, L98, L100, L106, … (8 lines). minor (1–3): TSDP as the third „Werk-Anker“, the clinical basis of the character architecture, ANP and EP (L21); demanding a split of the Dramatica functions inside the MC throughline (L100); the TSDP-Alter table (L106).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L141. occurrence: „In der sozialen Simulation zeigen sich Echos“ (L141) — the simulation's social layer, not the Überwelt.

- **`kern-welten`** (minor, 1–3): the alter table's worlds — Logos-Prime (KW1) for Kael and Lex, Mnemosyne-Archipel (KW2) for Kiko, Cerberus-Labyrinth (KW3) for Nyx and Moros, Kairos-Potentialis (KW4) for Selene (L107–L112); Kael's fight between Logos-Prime and Mnemosyne-Archipel (L89); Kael entering KW4 in Ketsu (L143) — quote around the digits.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Zero-Trust Execution Model` (near `zerotrust`). a reading — ZTEM, on the page above (L45, L65).
- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). occurrence: `Cerberus-Labyrinth` KW3's name (L109, L112), read on kern-welten.
- `entropie`: `Entropie-Kernel` (near `entropie`). occurrence: `Entropie-Kernel` is the DKT's kernel (L20, L46), read on dkt.
- `kairos`: `Kairos-Potentialis` (near `kairos`). occurrence: `Kairos-Potentialis` KW4's name (L111, L143, L182), read on kern-welten.
- `kohaerenz`: `Kohärenz-Protokoll` (near `koharenz`), `Kohärenztheorie` (near `koharenz`). occurrences: the Protokoll's name; `Kohärenztheorie` is the coherence theory of truth AEGIS represents (L66), read on aegis.
- `logos`: `Logos-Prime` (near `logos`). occurrence: `Logos-Prime` KW1's name (L89, L107, L140), read on kern-welten.
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). occurrence: `Mnemosyne-Archipel` KW2's name (L89, L110), read on kern-welten.
- `truth-rotation`: `Truth` (near `truthrotation`). occurrence: `Truth` is the Dramatica issue Truth vs. Falsehood (L48, L90), not the rotation.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: six alters, each assigned one of four worlds KW1–KW4, two to KW1 and two to KW3 (L107–L112).
- **`q8-aegis-after-the-vortex`**: AEGIS not erased but disintegrating into an algorithmic melancholy, an emergent rule set inside the creative chaos (L178).
- **`c16-kael-origin`**: „Kael (Host / ANP)“ (L107) and Kael as Fragment Alpha in Logos-Prime (L140).
- **`c2-entropie-sense`**: Entropie as trauma — „die Integration von Trauma (Entropie)“ (L28), „traumatische Entropie“ (L50).

**Not promoted:** NCP, ANP/EP, Z-Fighting, ZTEM's siblings RIVE/RTSV/BPoF, the Paradox of Misaligned Coherence, the Landauer-Prinzip, Moonshine Resonance and the K-J Vector, Inner Council, the 5D-Lift, Phönix-Kollaps, Vertex-Explosion, the Dramatica values.

**Two readers**, disjoint: (1) kael, juna, alters, lex, nyx, kiko, selene, moros, tsdp, kern-welten, multiplizitaet, mosaik-herz; (2) aegis, aegis-teilfunktionen, dkt, kohaerenz-kernel, entropie, risse, kishotenketsu and the records q3, q8, c16, c2.

**Chapter readings**: Kap 01–13 by the Kishōtenketsu ranges, by the session (`Plan/runs/ingest-220-kap/`).
