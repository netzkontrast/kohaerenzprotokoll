# Brief — readings from document 551 (step 6)

1 document, one reader, one batch: `ingest-551`. Files go to `Plan/runs/ingest-551/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 551 | `digitale-uberwelt` | 2025-04-17 | „the Überwelt concept“ | a concept draft for a purely informational „Digitale Überwelt“ regulated by AEGIS and inhabited by the five Guardians, with research, a self-review and a refined final draft; it calls its inputs an unchangeable rule set (L17) and its result a coherent foundation (L110) — claims recorded, not applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (195 lines for `digitale-uberwelt`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A concept draft: write „the Überwelt concept proposes …“; never canon. **Never cite L53 or L106** (an earlier name) **nor L122 or L144** (real names); L49 is one export-joined line of about 36,000 characters that also names real persons — quote only short name-free spans from it. Claims tagged „[Kontext 1]“ report the AEGIS protocol; say so.

## Pages — document 551, `digitale-uberwelt`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L17, L25, L29, L36, L40, … (25 lines). central: has no place, is the operating system and kernel (L49); reacts mechanistically and protocol-driven (L49); the Consensus Enforcer routes control impulses without debate (L45); reacts to novel cracks by its core function of coherence (L104); bounds Kairos's emergence (L105).
- **`aegis-teilfunktionen`** (central, 3–12 quotations): the census's surfaces — `Zero-Trust` L25, L29, L40, L45, L49, L77, … (9 lines); `Integrity Guardian` L44, L49, L62, L105; `Cognitive Firewall` L49, L62, L104, L105; `SIS` L49, L71, L104, L107. minor: the Cognitive Firewall and the Integrity Guardian as signals of invalidity (L49); generic defence and isolation mechanisms „(Cognitive Firewall, SIS)“ (L104).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L17, L29, L34, L49, L103. minor: one of the five Guardians with its domain (L17).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L62. a reading — see below.
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L49, L72, L108. minor: defined by contrast to the Überwelt (L72); emotion, connection, transcendence against pure information (L49); a space of continuous fields and resonance (L108).
- **`guardians`** (central, 3–12 quotations): the census's surfaces — `Guardians` L15, L17, L21, L29, L30, L36, … (21 lines). minor: the five with their domains as the unchangeable rule set (L17); communication by Encrypted Intent Channels, intent not speech (L30); consensus without trust or negotiation (L40).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L17, L36, L45, L49, L62, L99, … (7 lines). minor: Kairos's domain (L17); its coexistence with AEGIS in bounded „Potenzialfeldern“ (L105).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kern-Welten` L49. minor: the four simulated Kern-Welten run on the Überwelt like virtual machines (L49).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L44. not read: an occurrence — system coherence as AEGIS's metric (L44) (J9).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L17, L29, L30, L34, L36, L45, … (8 lines). minor: one of the five Guardians with its domain (L17).
- **`mnemosyne`** (central, 3–12 quotations): the census's surfaces — `Mnemosyne` L17, L30, L35, L49, L54, L63, … (11 lines). minor: one of the five Guardians with its domain (L17).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L49, L53, L104, L106. minor: „Risse“ as violations or failures of the AEGIS protocol (L49); AEGIS's reaction to novel cracks (L104).
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L17, L35, L49, L98. minor: one of the five Guardians with its domain (L17).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L11, L15, L21, L49, L72, L101, … (9 lines). central: not geographic but functionally structured (L49); the hypervisor layer under the Kern-Welten (L49); pure information, logic, protocol against the external level (L49); the concept's closing claim (L110).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Systemkohärenz` (near `koharenz`). an occurrence.


**Reading by the sentence beyond the lookup:**
- **`emergenz`** (minor): Kairos's domain includes „Emergenz“ (L62); Kairos-fostered emergence crossing thresholds triggers AEGIS's controls (L105).

**Record entries:** none.

**Not promoted:** Encrypted Intent Channels, Consensus Enforcer, ZTEM, RTSV, BPoF, Potenzialfelder, the functional zones, the Kontext tags.

**One reader**: every page above.
