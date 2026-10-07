# Brief — readings from document 180 (step 6)

1 document, one reader, one batch: `ingest-180`. Files go to `Plan/runs/ingest-180/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 180 | `refining-dramatica-storyform-for-kohaerenz-protokoll` | 2026-01-02 | „the storyform exegesis“ (titled `The Coherence Protocol: A Definitive Exegesis of Narrative Systemics, Dramatica Architecture, …`) | an English research report that chooses one Dramatica storyform, „Kohärenz-Prime“ (OS Physics, MC Kael in Mind, IC AEGIS/Juna in Universe, RS Psychology), sets the cosmology (K1/K0, the Risse, the Moonshine Link), resolves the names Kael, Michael and Julia, decides AEGIS's end and a Guardian's schism, and lays out a 39-step plot in three acts; it calls its settings „definitive“ (L68) — recorded, never applied; the author's own storyforms (decision 025) are not this document's |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (343 lines for `refining-dramatica-storyform-f`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A report that decides and calls its decisions canonical: write „the storyform exegesis decides / sets / proposes …“; never as settled — the author's storyforms in Plan/storyform/ are the author's. Its storyform values are its proposal, quoted as written. Its 39 steps lost their numbers in the export (every step reads „1.“, except „Step 23“ at L300) — never number a step. English with German names — quote as written; cut before inner straight quotes; kernel symbols are escaped (`$K\_1$`) — never quote across them; the settings table has escaped bold — quote the plain words.

## Pages — document 180, `refining-dramatica-storyform-for-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L25, L33, L50, L54, L61, L81, … (48 lines). central (2–4): Influence Character with Juna, Domain Universe, „The God of the Machine“ (L92); its Issue Preconception, „Ontological Blindness“ (L94); Problem Faith, Solution Disbelief (L95, L96); „a ‚Tragic System'“, coherence through negation (L137); the defeat mechanism — not explosion but „Paraconsistent Transformation“, algorithmic melancholy (L139).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L50. minor (1–2): L50 — read the line; „Julia/Kiko/Nyx (The Alters)“ (L133).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L132. minor (1–2): Michael „shattered during the ‚Genesis Crisis'“ (L131) — quote around; L132 — read the line.
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel Gambit` L96, L256, L264, L296, L298. central (2–4): Kael forces AEGIS to doubt its completeness (L96); the climax, he uploads his functional multiplicity into AEGIS's logic core (L264); its mechanics, set up early (L296–L300).
- **`guardians`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Guardians` alone on L140. minor (1–2): „The ‚Wächter' (Guardians) are subsystems of AEGIS“ (L140) — quote around; the Guardian's Dilemma and Schism (L140, L233, L250).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L25, L54, L62, L85, L93, L120, … (11 lines); `Julia` L126, L128, L133. minor (1–2): Influence Character with AEGIS (L91–L92); Juna as „The Anomaly“ bypassing AEGIS's logic via the link (L120); „Julia“ to be deprecated as a name (L133).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L25, L35, L54, L62, L76, L78, … (58 lines); `Michael` L126, L128, L132, L209, L254. central (2–4): Main Character, Domain Mind, „trapped in ‚Trauma-Time'“ (L74) — quote around; Problem Control, Solution Uncontrolled (L77, L78); „System Kael“ the collective, „Kael (The Manager)“ the primary ANP with „male pronouns (He/Him) as the default interface“ (L129, L130); „Michael (The Ghost)“, the original host who shattered (L131).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L140, L233, L250. minor (1–2): the Guardian who resonates with Kael's emergent order (L140); hesitates in KW2 (L233); „LogOS (Loyal) vs. Kairos (Rebel)“ (L250).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L60. minor (1–2): K1 corresponds to the „City“ (KW1), K0 to the „Archipelago“ (KW2) (L113, L114); the „Überwelt“ named KW3 (L251).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L77, L133, L236. minor (1–2): an EP „subconscious“ manifestation (L75); „Kiko (The Child)“ (L133).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L17. occurrence: the project's name (L17) and the storyform's name „Kohärenz-Prime“.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L192, L232. minor (1–2): „Lex“ (Logic ANP) takes over to solve a cryptographic puzzle (L192); maps KW2 (L232).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L140, L160, L208, L250. minor (1–2): LogOS remains loyal to the old logic (L140); „LogOS (Loyal) vs. Kairos (Rebel)“ (L250).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Mnemosyne` alone on L230. minor (1–2): L230 — read the line; KW2 as „Mnemosyne Archipelago“.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine Link` L54, L118, L120, L176, L290, L330. central (2–4): the Relationship Story, „THE MOONSHINE LINK“, Domain Psychology (L98–L99); Issue Commitment, quantum entanglement (L101); „a ‚non-local, sub-protocol connection'“ AEGIS cannot see (L120) — quote around the inner quotes.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L77, L133, L231, L236. minor (1–2): an EP subconscious manifestation (L75); „Nyx (The Persecutor/Protector)“ (L133).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L33, L60, L81, L89, L110, L116. central (2–4): Kael's Unique Ability, investigating the Risse (L80); the OS Catalyst, interpreting them as messages (L89); „The Risse (Fissures)“, an intrusion of K0 into K1 when Kael's dissociation resonates (L115).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L17, L33, L144. minor (1–2): „Tertiary Structural Dissociation of the Personality“ — read where it stands; the ANP/EP hierarchy (L129–L133).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L251. minor (1–2): „the firewall of the ‚Überwelt' (KW3)—AEGIS's command center“ (L251) — quote around the inner quotes; the report places the Überwelt as KW3, say so.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis Crisis` (near `genesis`). a reading — on genesis above.
- `guardians`: `Guardian's Dilemma` (near `guardians`), `Guardian's Schism` (near `guardians`). a reading — on guardians above.
- `kohaerenz`: `Kohärenz-Prime` (near `koharenz`), `Kohärenz Protokoll` (near `koharenz`), `Kohärenz-Prime V2` (near `koharenz`). occurrence: the storyform's name and the title.
- `mnemosyne`: `Mnemosyne Archipelago` (near `mnemosyne`). a reading — on mnemosyne above.
- `personas`: `Tertiary Structural Dissociation of the Personality` (near `persona`). occurrence: the TSDP's full name.


**Record entries** (one file each):

- **`c16-kael-origin`**: „Michael (The Ghost)“, the original host who shattered during the Genesis Crisis (L131).
- **`c17-kael-gender`**: Kael the primary ANP with „male pronouns (He/Him) as the default interface“; Michael and Julia as host names the documents fluctuate between (L128–L133).
- **`q1-guardians-and-aegis`**: „subsystems of AEGIS“; the Guardian's Dilemma and Schism (L140, L250).
- **`q6-nexus-ueberraum-ueberwelt`**: the Überwelt as KW3, AEGIS's command center (L251).
- **`q8-aegis-after-the-vortex`**: not explosion but transformation, algorithmic melancholy (L139).
- **`q9-moonshine-link-boundary`**: non-local, sub-protocol, invisible to AEGIS (L120).

**Not promoted:** Kohärenz-Prime and its storyform values (Plan/storyform/ holds the author's), the Guardian's Dilemma and Schism, Michael (The Ghost) — on kael and C16, Story Mind, Dual Kernel Theory, the 39 steps, Dramatica vocabulary.

**No chapter readings:** the export numbered every step „1.“; mapping steps to chapters would be inference.

**Two readers**, disjoint: (1) kael, kiko, nyx, lex, tsdp, alters, juna, moonshine-link, genesis and the records c16, c17, q9; (2) aegis, guardians, logos, kairos, mnemosyne, kern-welten, ueberwelt, risse, goedel-gambit and the records q1, q6, q8.
