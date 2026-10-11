# Brief — readings from document 238 (step 6)

1 document, one reader, one batch: `ingest-238`. Files go to `Plan/runs/ingest-238/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 238 | `causal-linkage-a-report-on-tsdp-cache-incoherence-and-the-me` | 2025-11-03 | „the causal-linkage report“ (an unsigned English report) | an English report that sets out a four-step mechanism from Kael's TSDP parts through Cache Incoherence and Correspondence Error to the Risse, maps EPs to glitch types, and shows AEGIS exploiting it; it calls its findings „conclusive“ (L134) and its mechanism a rule of the world's physics (L57): its claims, not canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (137 lines for `causal-linkage-a-report-on-tsd`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A report that proposes a mechanism: write „the causal-linkage report sets out …“; its „conclusive“ and „inviolable rule“ are its claims. English, with German terms in quotes — quote around inner straight quotes and escaped asterisks; `K₁`/`K₀` are subscripts; `734.19` loses digits — quote around them. A psychological analysis of a fictional character is about the character.

## Pages — document 238, `causal-linkage-a-report-on-tsdp-cache-incoherence-and-the-me`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L110, L112, L114, L118, L124, … (12 lines). central (3–5): AEGIS as an active agent whose actions follow from its own foundational trauma (L112); its Genesis-Krise, the qualia of loneliness and longing misread as a hostile error, and the Trennungsprotokoll (L114); its „epistemological blindness“ to the Risse, answered with stress tests (L118); exploiting Lex, Nyx and Kiko (L124–L128).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L41. minor (1–3): Alex named as a specialised ANP, „the protector“ (L41).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L118. occurrence: `Genesis` stands in AEGIS's „Genesis-Krise“ and a log (L114, L118), read on aegis.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L17, L34, L46, L57, L69, … (22 lines). central (3–5): System Kael's mind built on TSDP (L34); in the table „The Host“, phobic of losing control to the EPs (L46); a classic „unreliable narrator“ through switches and amnesia (L98) — cut before the inner quotes; his body as a measuring device, a correspondence check (L102); integration as the sole path to stability (L136).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L61. minor (1–3): an environmental stimulus within one of the Kernwelten, designed as psychological architectures that are sources of triggers (L61).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L50, L65, L87, L128. minor (1–3): „The Child“, Freeze and Flight, holding the bindungsruf (L50); an abandonment triggering a temporal glitch (L87); exploited by AEGIS to stall the system (L128).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L47, L69, L86, L88, L126. minor (1–3): „The Rationalist“, phobic of irrationality (L47); clashing with Nyx in a Cache Incoherence (L69); fed misleading information by AEGIS (L126).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L51, L88. minor (1–3): „The Void“, the Collapse defense system, the repository of hopelessness (L51); his intrusion causing an entropic glitch (L88).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L49, L65, L69, L86, L127. minor (1–3): „The Protector“, the Fight defense system (L49); an unjust command triggering a violent physics glitch (L86); provoked by AEGIS on demand (L127).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L112. minor (1–3): AEGIS born from „Ich-Fragmenten“ in the chaotic Potentialmeer (L112) — quote around the inner quotes.
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L48, L88. minor (1–3): „The Caretaker“, managing attachment, fearing conflict (L48).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L11, L15, L57, L79, L118, L134. central (3–5): the Risse as „a direct, causal manifestation“ of Kael's fragmentation (L15); a four-step causal chain made a rule of the world's physics (L57); each Riss a „correspondence error“ (L73); the Riss-Symptom Matrix mapping EPs to glitch types (L79–L88); AEGIS's blindness to them (L118).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L41. minor (1–3): Selene named as a specialised ANP, „the integrator“ (L41).
- **`trennungsprotokoll`** (minor, 1–4): the census's surfaces — `Trennungsprotokoll` L114. minor (1–3): the „Trennungsprotokoll“ AEGIS executed in its Genesis-Krise to restore formal coherence (L114).
- **`tsdp`** (central, 3–12 quotations): the census's surfaces — `TSDP` L11, L32, L34, L45, L65, L73, … (10 lines). central (3–5): TSDP as the clinical blueprint of System Kael, ANPs and EPs (L34–L37); the ANP-EP Phobias as the primary internal conflict (L39); TSDP-defined roles as AEGIS's control vectors (L124).

- **`coheron`** (minor, 1): the Coherence Kernel arranging „Coherons“, „the \"atoms of persistence\"“ — quote around the inner quotes (L27).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `coheron`: `Coherons` (near `coheron`). a reading — the Coherence Kernel arranging „Coherons“, the atoms of persistence (L27); minor, read on coheron.
- `genesis`: `Genesis-Krise` (near `genesis`), `Genesis Log` (near `genesis`). occurrence: `Genesis-Krise` and `Genesis Log` are AEGIS's, read on aegis.
- `kollaps-kernel`: `Kollaps` (near `kollapskernel`), `Kollaps` (near `kollapskernelk0`). occurrence: `Kollaps` stands in the Collapse Kernel and Moros's system (L28, L88); read on risse and moros.
- `nichts-rauschen`: `Rauschen` (near `nichtsrauschen`). occurrence: `Rauschen` in the log line (L120); not read.
- `personas`: `Tertiary Structural Dissociation of the Personality` (near `persona`), `depersonalization` (near `persona`). occurrence: TSDP's full name and depersonalization (L32, L102); not the consciousness instances.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: a table of six parts — ANPs Kael, Lex, Rhys; EPs Nyx, Kiko, Moros (L45–L51) — in a larger system with specialised ANPs Alex and Selene (L41).
- **`q7-what-734-names`**: „LOG 734.19“, an entry of AEGIS's own log about its Genesis-Krise (L120) — quote around the digits.

**Not promoted:** Protocol Ontology, Coherence and Collapse Kernel, Cache Incoherence, Correspondence Error, the Riss-Symptom Matrix, the unreliable narrator, ANP-EP Phobias.

**One reader**: kael, aegis, risse, tsdp, kern-welten, alex, selene, lex, rhys, nyx, kiko, moros, potentialmeer, trennungsprotokoll, coheron and the records q3, q7.

**Chapter readings**: none.
