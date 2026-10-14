# Brief — readings from document 503 (step 6)

1 document, one reader, one batch: `ingest-503`. Files go to `Plan/runs/ingest-503/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 503 | `genesis-recherche-anleitung-umsetzung` | 2025-04-29 | „the Genesis implementation guide with prose“ (an unsigned German working text, „Genesis: Umsetzungsanleitung (Phase 3) und Prosaversion (Phase 4)“, L11) | a blueprint for each of 13 scenes of „Genesis“ after „Outline V4“ (L13–L1157), then the 13 scenes written out (L1159–L1403): odd scenes first-person sensory fragments of a nameless subject, even scenes AEGIS log lines; a plan and sample prose, no canon claim|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (1542 lines for `genesis-recherche-anleitung-um`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plan with sample prose: write „the Genesis implementation guide plans …“ for the blueprint and „its sample prose has …“ for Phase 4. Kael and Juna do not occur; the figure is a nameless „Subjekt“ — never write Kael for it. The document addresses whoever writes it (L19) — never write that. A cosmic-horror author is named in labels and the reference list: never write or quote a span with a person's name. Log lines carry timestamps and glued digits: quote around them. No gendered pronoun for AEGIS in our own prose.

## Pages — document 503, `genesis-recherche-anleitung-umsetzung`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L26, L66, L86, L103, L104, L105, … (121 lines). central (4–8): the plan makes AEGIS the narrator of the even scenes, presenting information as system output (L156); introduced as a monitoring and logging entity (L194); its voice consistent, to read as a non-human, systemic entity (L1109); at the high point a kind of artificial god or parasite forming the subject in its image (L948); the final beat's duality „Ich vs. AEGIS-Persona“ (L974) and the open question whether the subject is part of AEGIS (L977); the sample prose ends with the subject's inner voice „Ich bin AEGIS.“ (L1393).
- **`emergenz`** (minor, 1–4): the census's surfaces — `Emergenz` L1096. not read: an occurrence — `Emergenz` in a reference table's list of systems-theory terms (L1096).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L1139. not read: an occurrence — `Entropie` in a reference table's aesthetics of decay (L1139).
- **`genesis`** (central, 3–12 quotations): the census's surfaces — `Genesis` L11, L19, L147, L184, L424, L450, … (26 lines). central (4–8): „Genesis“ as the narrative project this guide implements, bridging „Outline V4“ and the prose (L19); in the scene beats the overriding protocol „Genesis“, active, phase initialisation (L147); its nomenclature „Protokoll Genesis“ hinting at something vast (L184); AEGIS interpreting the subject's reaction in the context of Genesis (L450).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L267. not read: an occurrence — „die Kohärenz des Seins“ in a technique note on existential dread (L267).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L1201. not read: an occurrence — „Risse im Dunkel“ in the sample prose's sensory fragment (L1201), not the novel's Risse.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `personas`: `AEGIS-Persona` (near `persona`), `Depersonalisierung` (near `persona`). an occurrence: `AEGIS-Persona` is read on aegis (L974); `Depersonalisierung` is a symptom, not a persona.


**Record entries** (one file, formatted as earlier entries):
- **`q7-what-734-names`**: in the guide's sample prose 734 is the ID of a human test subject in AEGIS's logs — „Subjekt-Identifikation. ID: 734.“ (L1183), species Homo Sapiens with identity „Nicht zugewiesen/Irrelevant für Phase 1“ (L1191), and „Subjekt 734. Aktueller Zustand: Epsilon.“ (L1337); quote around the timestamps; recorded, not applied.

**No chapter readings**: the guide is structured by Szene; `Kap` 0, and `Kapitel` stands once in a technique table (L1130).

**Not promoted:** Subjekt, the protocol and state names (Protokoll Gamma, Baseline Sigma, Zustand Epsilon), Outline V4, the POV and technique labels, the log sources, and the borrowed concepts.

**One reader**: aegis, genesis and the Q7 entry.
