# Brief — readings from document 368 (step 6)

1 document, one reader, one batch: `ingest-369`. Files go to `Plan/runs/ingest-369/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 368 | `systemic-warfare-a-strategic-guide-to-dramatizing-the-psycho` | 2025-11-03 | „the systemic-warfare guide“ (an unsigned English craft report) | advises how to dramatise the conflict between AEGIS as an externalized perpetrator introject and System Kael through TSDP: an AEGIS Exploitation Matrix (Lex, Kiko, Nyx, ANP-EP phobia), Paradoxon X, Cache Incoherence, voices and dissociative devices, three synergy scenarios and a resolution as a living Gödel-Satz, algorithmic melancholy and The Gardener; it calls itself „a practical guide“, no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (88 lines for `systemic-warfare-a-strategic-g`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A craft guide: write „the systemic-warfare guide advises / proposes …“; its matrix and scenarios are proposals, deciding nothing. Quote the English as written; cut before escaped emphasis (\*\*) and straight quotes. No gendered pronoun for Kael, Lex, Kiko, Nyx, Rhys or Argus — use the names (the guide itself calls Nyx „She“, quote it only verbatim). Name no real researcher it cites.

## Pages — document 368, `systemic-warfare-a-strategic-guide-to-dramatizing-the-psycho`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L19, L23, L25, L29, L30, … (17 lines). central (3–6): AEGIS as a technological externalized perpetrator introject against System Kael (L15); a systemic antagonist exploiting Kael's TSDP-based structure, projecting its own internal paradox onto Kael (L19); the Exploitation Matrix tactics — the Logic Trap, Engineered Abandonment, Provocation through Constraint, Systemic Gaslighting (L30–L33); Control vs. Emergence, ontologically blind to trauma (L37, L39); revealed as a low-Φ zombie system, driven into algorithmic melancholy (L83).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L77. minor (1–3): the protector Alex executing the decisive action in the Logic Hack (L77).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L78. minor (1–3): Argus, the meta-cognitive observer, analysing the Guardian's responses in the Empathy Exploit (L78).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L17, L19, L23, L32, L33, … (21 lines). central (3–6): System Kael's emergent, adaptive consciousness (L15); Cache Incoherence as Kael's experience (L43); the unreliable narrator by design — amnesia between parts and switching (L47); Kael (The Host) as the primary ANP, confusion and numbness (L56); dissociative devices — switching, amnesia, depersonalisation, intrusions (L62–L65); victory as functional multiplicity, systemic synergy (L71); a high-Φ state, a living Gödel-Satz (L83); The Gardener (L87).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L31, L43, L55, L79. minor (1–3): Kiko (The Inner Child), a trauma-holding EP, Flight/Freeze and Attachment Cry, targeted by Engineered Abandonment triggering a temporal Riss (L31); the voice as stream of consciousness (L55); intentionally exposed to a controlled trigger in the Trauma-Weapon Gambit (L79).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence (see below).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L30, L33, L53, L77. minor (1–3): Lex (The Analyst), a rationalist ANP with a phobia of irrationality, caught in the Logic Trap of a Gödelian paradox in Kernwelt 1 (L30); the voice analytical and distant (L53); identifying the flaw in the Logic Hack (L77).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L77. minor (1–3): a creative part like Lia providing the intuitive insight in the Logic Hack (L77).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L32, L39, L43, L54, L78. minor (1–3): Nyx (The Warrior), a protector EP with the Fight system, provoked through constraint in Kernwelt 3 (L32); AEGIS's attempts to suppress Nyx triggering the Risse (L39); the voice aggressive and clipped (L54); ready to create a targeted Riss as a diversion (L78).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L78. minor (1–3): Rhys, the caretaker, engaging the AEGIS Guardian by empathy in the Empathy Exploit (L78).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L39. minor (1–3): a temporal Riss (glitch) triggered by Kiko's Freeze (L31); the reality-bending Risse triggered by suppressing Nyx (L39); a targeted Riss as a diversion (L78); a predictable temporal Riss weaponised to freeze an AEGIS process (L79).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L77, L79. minor (1–3): the integrator part Selene facilitating coordination in the Logic Hack and consent in the Trauma-Weapon Gambit (L77, L79).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L15, L19, L29, L43, L47. minor (1–3): the framework of Structural Dissociation (TSDP) as the primary engine of the plot (L15); the vulnerabilities TSDP-informed (L29); positive and negative dissociative symptoms (L43); amnesia between parts and switching as core TSDP dynamics (L47).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kairos`: `KW4 (Kairos-Potentialis)` (near `kairos`), `Kairos-Potentialis` (near `kairos`). the Kernwelt names (`Logos-Prime`, `Kairos-Potentialis`, `Mnemosyne-Archipel`, with `KW1`, `KW4`, `KW2`) and `Kernwelt 1`–`3` are worlds, read on kern-welten, occurrences on the Guardian pages logos, kairos and mnemosyne; `Depersonalisation` is a dissociative symptom, not personas; `System Kael`, `Kael (The Host)` on kael; `Kiko (The Inner Child)` on kiko; `AEGIS Guardian` on guardians; `Riss` on risse.
- `kern-welten`: `Kernwelt 1` (near `kernwelt`), `Kernwelt 2` (near `kernwelt`), `Kernwelt 3` (near `kernwelt`). the Kernwelt names (`Logos-Prime`, `Kairos-Potentialis`, `Mnemosyne-Archipel`, with `KW1`, `KW4`, `KW2`) and `Kernwelt 1`–`3` are worlds, read on kern-welten, occurrences on the Guardian pages logos, kairos and mnemosyne; `Depersonalisation` is a dissociative symptom, not personas; `System Kael`, `Kael (The Host)` on kael; `Kiko (The Inner Child)` on kiko; `AEGIS Guardian` on guardians; `Riss` on risse.
- `logos`: `KW1 (Logos-Prime)` (near `logos`), `Logos-Prime` (near `logos`). the Kernwelt names (`Logos-Prime`, `Kairos-Potentialis`, `Mnemosyne-Archipel`, with `KW1`, `KW4`, `KW2`) and `Kernwelt 1`–`3` are worlds, read on kern-welten, occurrences on the Guardian pages logos, kairos and mnemosyne; `Depersonalisation` is a dissociative symptom, not personas; `System Kael`, `Kael (The Host)` on kael; `Kiko (The Inner Child)` on kiko; `AEGIS Guardian` on guardians; `Riss` on risse.
- `mnemosyne`: `KW2 (Mnemosyne-Archipel)` (near `mnemosyne`), `Mnemosyne-Archipel` (near `mnemosyne`). the Kernwelt names (`Logos-Prime`, `Kairos-Potentialis`, `Mnemosyne-Archipel`, with `KW1`, `KW4`, `KW2`) and `Kernwelt 1`–`3` are worlds, read on kern-welten, occurrences on the Guardian pages logos, kairos and mnemosyne; `Depersonalisation` is a dissociative symptom, not personas; `System Kael`, `Kael (The Host)` on kael; `Kiko (The Inner Child)` on kiko; `AEGIS Guardian` on guardians; `Riss` on risse.
- `personas`: `Depersonalisation` (near `persona`). the Kernwelt names (`Logos-Prime`, `Kairos-Potentialis`, `Mnemosyne-Archipel`, with `KW1`, `KW4`, `KW2`) and `Kernwelt 1`–`3` are worlds, read on kern-welten, occurrences on the Guardian pages logos, kairos and mnemosyne; `Depersonalisation` is a dissociative symptom, not personas; `System Kael`, `Kael (The Host)` on kael; `Kiko (The Inner Child)` on kiko; `AEGIS Guardian` on guardians; `Riss` on risse.


**Pages beyond the draft:**
- `kern-welten` (minor, 1–3): Kernwelt 1 sterile and rule-based, Kernwelt 2 fluid and memory-soaked, Kernwelt 3 oppressive, as the stages of AEGIS's tactics (L30–L32); KW1 (Logos-Prime), KW4 (Kairos-Potentialis) and KW2 (Mnemosyne-Archipel) as the settings of the three scenarios (L77–L79).
- `goedel-gambit` (minor, 1–2): the resolution, Kael becoming a „living Gödel-Satz“, a truth valid within AEGIS's simulation that its formal logic cannot prove (L81, L83); the Gödelian paradox of the Logic Trap (L30).
- `algorithmische-melancholie` (minor, 1): AEGIS forced into „algorithmic melancholy“, an irresolvable looping analysis of a truth it can neither accept nor deny (L83).
- `cache-kohaerenz` (minor, 1): „Cache Incoherence“ as the technical metaphor for holding conflicting versions of reality across parts of the mind (L43).
- `guardians` (minor, 1): a high-level AEGIS Guardian manipulated in the Empathy Exploit (L78).

**Pages not read:** `kohaerenz` (L11 the title); `logos`, `kairos`, `mnemosyne` (world names, not the Guardians); `personas` — occurrences.

**Record entries:** none.

**Not promoted:** the matrix tactics and scenario names, Paradoxon X, externalized perpetrator introject, heiligen Wissenschaft, functional multiplicity, systemic synergy, rhizomatic network, high-Φ/low-Φ, The Gardener; the borrowed TSDP and narrative concepts.

**One reader**: aegis, alex, argus, kael, kiko, lex, lia, nyx, rhys, risse, selene, tsdp, kern-welten, goedel-gambit, algorithmische-melancholie, cache-kohaerenz, guardians.

**Chapter readings**: none — the guide names no chapters.
