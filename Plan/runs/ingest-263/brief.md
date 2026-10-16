# Brief — readings from document 263 (step 6)

1 document, one reader, one batch: `ingest-263`. Files go to `Plan/runs/ingest-263/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 263 | `the-coherence-protocol-a-narrative-mosaic` | 2025-11-03 | „the narrative mosaic brief“ (an unsigned English brief) | a brief for 39 short stories forming „a narrative mosaic“ of the novel, each with one core concept, one assigned point of view and a „Dramatize the Concept“ paragraph, with a roster of the host, ten alters, AEGIS and its Guardians and Juna/V; no story text; it claims the finished collection will prove the novel's foundation sound (L306), its claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (307 lines for `the-coherence-protocol-a-narra`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A brief: write „the narrative mosaic brief assigns / describes …“; its roster (L21–L50) characterises the points of view, its story entries are instructions for stories not written. Its 39 stories are not chapters. Cut quotations before inner quotes and emphasis marks; digits glued to words drop out (`KW1`, „Component 734“), so quote around them.

## Pages — document 263, `the-coherence-protocol-a-narrative-mosaic`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L36, L38, L39, L40, L41, … (35 lines). central (3–6): the AEGIS Core Logic, „Component 734“, the traumatised Ursprungs-Ich after its fragmentation, defined by the prime directive „Aegis is what Aegis prevents itself from not being“ (L38); the AEGIS System-Wide Log (L39); a monolithic Guardian enforcing its will and a rebel Guardian questioning its logic (L40–L41); the component maintaining the Überwelt simulation (L146).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L27, L73, L74, L98. minor (1–3): „The protector ANP“, defending vulnerable parts in crisis (L27).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L24. minor (1–3): „The Internal Parts (Alters)“, to be written in close third person (L24); ten listed (L26–L35).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L35, L127, L128. minor (1–3): „The meta-cognitive observer/critic“, prone to cynical analysis-paralysis (L35).
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L32, L97, L98. minor (1–3): „The sexualized EP“, using sexualisation to reclaim power and control (L32).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L49. minor (1–3): „Juna/V (The Exile)“: the exiled part of Kael's Ursprungs-Ich, representing gnosis, quantum entanglement and the Paraiyas AEGIS rejects (L49).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L23, L40, L41, L49, L56, … (37 lines). central (3–6): „Kael (The „I“)“, the primary host, keeping a facade of normalcy amid amnesia, depersonalisation and incoherence (L23); System Kael as the collection's model (L306); the exiled part of his Ursprungs-Ich (L49).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelt` L42, L43, L44, L45, L68, L146, … (10 lines); `Kernwelten` L146. central (3–6): four Kernwelten, each with its Guardian: KW1 sterile, logical order (L42), KW2 emotion, memory and connection (L43), KW3 paranoia and zero-trust defence, bunker-like (L44), KW4 emergence, potential and creativity (L45).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L30, L79, L80, L218, L236. minor (1–3): „The child EP“, flight/freeze, profound fear, a search for safety (L30).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. not read: occurrence — the title (L15).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L26, L67, L68, L80, L86, L98, … (9 lines). minor (1–3): „The rationalist ANP“, phobic of chaos and emotion, a system Manager (L26).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L31, L109, L110. minor (1–3): „The child EP“ of ambivalence, play, and desire for and fear of closeness (L31).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L46, L92, L110, L199, L200. minor (1–3): a Guardian monitoring the Moonshine-Link anomaly as an example POV (L46); the story entries L92, L110, L199–L200 only if they characterise the link.
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L33, L103, L104. minor (1–3): „The „Collapse“ EP“, the bearer of the system's deepest hopelessness (L33).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L204, L206, L266. minor (1–3): the Nichts Rauschen with the Potentialmeer as cosmic horror (L204); a Guardian at the absolute boundary between AEGIS's reality and the Nichts Rauschen (L266).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L29, L86, L121, L122, L128, L218. minor (1–3): „The „Fight“ EP“, aggression, contempt for weakness and a traumatised need to protect (L29).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L204, L206, L212, L218, L265, L266. minor (1–3): with the Nichts Rauschen as cosmic horror (L204); L206, L212 only if they add.
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L28, L85, L86, L110, L122, L128, … (8 lines). minor (1–3): „The caretaker ANP“, empathy, connection and internal harmony (L28).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L205. minor (1–3): a Guardian monitoring the Risse as an assigned POV (L205).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L34, L115, L116. minor (1–3): „The integrator/buffer ANP“, blocking destabilising trauma intrusions (L34).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L60, L62, L78, L96, L102, L114, … (8 lines). minor (1–3): the alters' ANP/EP classes (L26–L35); TSDP at L60, L62 only if a line characterises it.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L146, L277. minor (1–3): the Überwelt simulation maintained by the AEGIS component (L146); the „Überwelt“ Simulation Core as an assigned POV (L277).

- **`guardians`** (minor, 1–3): a monolithic Guardian (Enforcer) and a rebel Guardian in the „Wächter-Zwiespalt“ who becomes Kael's secret ally (L40–L41); the Architect, the Network-Weaver, the Chaos-Regulator and the Possibility-Weaver as Guardians of KW1–KW4 (L42–L45).
- **`komponente-734`** (minor, 1): the AEGIS Core Logic, „Component 734“, the traumatised Ursprungs-Ich after its fragmentation (L38).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). occurrence: `Guardian` is the Guardians' singular, read on guardians.
- `guardians`: `Guardian's Dilemma` (near `guardians`), `Guardian` (near `guardians`). reading: the monolithic Guardian (Enforcer) and the rebel Guardian experiencing the „Wächter-Zwiespalt“ (L40–L41); the four Guardians of KW1–KW4 (L42–L45).
- `juna`: `Juna/V` (near `juna`). `Juna/V` read on juna (J34).
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the title.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: a host and ten alters in the roster (L23–L35); four Kernwelten (L42–L45).
- **`q5-guardians-and-kern-welten`**: one Guardian per Kernwelt — the Architect (KW1), the Network-Weaver (KW2), the Chaos-Regulator (KW3), the Possibility-Weaver (KW4) (L42–L45).
- **`q1-guardians-and-aegis`**: a monolithic Guardian enforcing AEGIS's will and a rebel Guardian, post-schism, questioning its logic and becoming Kael's ally (L40–L41).
- **`q7-what-734-names`**: „AEGIS Core Logic („Component 734“)“, the traumatised Ursprungs-Ich after its fragmentation (L38).
- **`c16-kael-origin`**: Juna/V as the exiled part of Kael's Ursprungs-Ich (L49), beside the AEGIS core as the Ursprungs-Ich after fragmentation (L38).

**Not promoted:** the 39 stories and their concepts, the points of view as such, the Authorial Narrator, the Architect, the Network-Weaver, the Chaos-Regulator, the Possibility-Weaver, the Wächter-Zwiespalt.

**One reader**: aegis, kael, juna, alters, lex, alex, rhys, nyx, kiko, lia, isabelle, moros, selene, argus, tsdp, kern-welten, guardians, komponente-734, ueberwelt, moonshine-link, potentialmeer, nichts-rauschen, risse and the records q3, q5, q1, q7, c16.

**Chapter readings**: none — its 39 stories are not chapters.
