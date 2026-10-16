# Brief — readings from document 480 (step 6)

1 document, one reader, one batch: `ingest-480`. Files go to `Plan/runs/ingest-480/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 480 | `operationalizing-the-coherence-protocol-a-narrative-stress-t` | 2025-11-03 | „the stress-test guide“ (an unsigned English planning guide, „Operationalizing the 'Coherence Protocol'“) | turns critiques into twelve „How can we…?“ prompts on the Risse, the trauma cycle, metafiction and the climax; it asks and sets objectives, it decides nothing|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (82 lines for `operationalizing-the-coherence`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** Questions and objectives: write „the stress-test guide asks how …“ or „sets the objective that …“; every e.g. is an example in a prompt, never a fact of the story. L76 carries a figure named after a logician — never quote a span containing that name. Quote the English as written; cut before bold and inner quotes. No gendered pronoun for Kael, Juna, AEGIS or any alter — use the names (quotations verbatim).

## Pages — document 480, `operationalizing-the-coherence-protocol-a-narrative-stress-t`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L28, L50, L62, L64, L66, L67, … (9 lines). minor (1–4): AEGIS's Ursprungs-Ich experienced loneliness and longing and misread them as hostile data corruption (L62); the Genesis-Krise as a proposed memory flashback (L66); AEGIS's manipulation of System Kael as a compulsive reenactment of its original trauma response (L67); AEGIS ontologically blind to the Moonshine-Link (L71).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L64. minor (1–4): the Genesis-Krise as AEGIS's misinterpretation of loneliness and longing, staged as a memory flashback (L66; L64 is the heading).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L50. minor (1–4): the Juna/V connection as a source of a Gnostic Injection (L50); demystifying the Juna/V connection is an objective of the climax (L62); the synchronized emotional exchange between Kael and Juna/V (L71).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L23, L28, L44, L50, L62, L67, … (10 lines). central (4–8): a Riss as the causal manifestation of an EP intrusion within System Kael, the world's instability reflecting Kael's fragmentation (L28); Kael's ANPs suppressing an EP to win, triggering a worse intrusion (L44); a Gnostic Injection through the Juna/V connection offering Kael a feeling of a deeper reality (L50); the climax as Kael becoming the Foundation's embodiment by achieving functional multiplicity (L76 — never quote the name); early acts of integration rewarded by subtle symmetries (L77).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L45. minor (1–4): the Kernwelten (Core Worlds) as arenas for the trauma cycle, a conquered logical KW1 (Lex's domain) destabilizing a trauma-laden KW2 (the EPs' domain) (L45).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L28, L44. minor (1–4): Kiko as the trauma-holder EP breaking through dissociative barriers (L28) and the Child-EP holding freeze trauma, suppressed by an ANP (L44) — examples in prompts.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L44, L45, L67, L72, L77. minor (1–4): Lex as the Rationalist ANP suppressing an EP (L44); KW1 as Lex's domain (L45); AEGIS reinforcing Lex's control (L67); Lex analysing the link and declaring it illogical (L72).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L71. minor (1–4): the Moonshine-Link operating on a non-local, sub-protocol level to which AEGIS is ontologically blind, shown through sensor logs of uncorrelated noise (L71).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L44. minor (1–4): Moros as the collapse-EP, an example of a later, more severe intrusion (L44).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L44. minor (1–4): Nyx as the protector-EP, an example of a later, more severe intrusion (L44).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L49, L67, L72, L77. minor (1–4): Rhys given a reframing line at a metafictional break (L49); AEGIS suppressing Rhys's empathy (L67); Rhys experiencing the link as intuitive prehension (L72); Kael choosing to listen to Rhys over Lex (L77).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L19, L23. minor (1–4): the objective to turn the Risse from passive metaphor into a causal threat; a Riss as the visible scar of the battle between K₀'s collapse and K₁'s Corrective Wavelet (L23); a Riss staged as a K₀ intrusion (L27) and as an EP intrusion (L28).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Krise` (near `genesis`). a reading: `Genesis-Krise` L66, read on genesis.
- `juna`: `Juna/V` (near `juna`). a reading: `Juna/V` read on juna.
- `personas`: `Emotional Personality` (near `persona`). an occurrence: the EP's expansion, the borrowed theory's term.


**Pages beyond the draft:**
- **`kohaerenz-kernel`** (minor, 1–2): the K₁ structure firing the Corrective Wavelet to maintain reality (L23, L27 — describe around the bold).
- **`kollaps-kernel`** (minor, 1–2): K₀ as the principle of universal decoherence, its entropic collapse; a K₀ intrusion as a decoherence event (L23, L27).

**Record entries:** none.

**No chapter readings**: the guide names no chapter.

**Not promoted:** Corrective Wavelet, Gnostic Injection, The Foundation, Ursprungs-Ich, Einsamkeit, Sehnsucht, functional multiplicity, high-Φ, prehension, subtle symmetries, the EP labels, and the borrowed concepts (one carries a person's name).

**One reader**: every page above.
