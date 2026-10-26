# Brief — readings from document 554 (step 6)

1 document, one reader, one batch: `ingest-554`. Files go to `Plan/runs/ingest-554/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 554 | `ki-gestuetzter-roman-assistent-projektplanung` | 2026-02-27 | „the novel-console specification“ | a build specification for an agent-driven web console around the novel, with an API table, an instruction text, a JSON sketch of the world („Story.ncp.json“) and a deployment plan; it calls itself a definitive blueprint (L13), a claim recorded, not applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (296 lines for `ki-gestuetzter-roman-assistent`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A software specification: write „the novel-console specification's world sketch …“; never canon. Read only the world sketch L167–L243 and L42–L43. **Never cite L72–L82, L138, L142, L220, L222, L224, L283, L287** (early names, the trauma symbol, a person's name, a person-named concept). Never quote the colour table.

## Pages — document 554, `ki-gestuetzter-roman-assistent-projektplanung`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L156, L221, L225, L232, L233. central: name and expansion (L232); core axiom „Existenz durch Negation“ (L233); symbolic core LFI (L235); treats Kael's alters as separate speakers (L236); Perverse Learning Loop (L237); Paradoxon X (L239); Algorithmic Horror (L240); misreads the moonshine link as noise (L225).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L236. minor: AEGIS treats Kael's alters as debating single speakers (L236).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L199. minor: K0 manifests as Nichts Rauschen, entropy, cracks (L199); Paradoxon X reads integration as rising entropy (L239).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L142, L220. not read: named only on a barred line (L142).
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L43, L156, L226, L236, L265, L272. minor: 13 entities of the System Kael (L43); the moonshine link triggers gnosis and resonance in Kael (L226); AEGIS treats Kael's alters as separate speakers (L236).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelt` L42, L156; `Kernwelten` L156. minor: rendering the current landscape „(Kernwelt 1-4)“ or the Überwelt (L42).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L56, L76, L139, L158. not read: only an example of the agent's rule check (L158), not a reading.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L168. not read: the project title (L168) (J9).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L31. not read: only an API example.
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L62, L76. not read: on a barred or UI line.
- **`moros`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Moros` alone on L138. not read: on a barred line (L138).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L199. minor: K0's manifestation „Das 'Nichts Rauschen', Entropie, Risse (Fissures)“ (L199); the triad's nothingness noise, alias „Die Leere / The Void“ (L205), an active high-entropy Potentialmeer (L206).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L56, L82, L140. not read: UI lines only.
- **`potentialmeer`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Potentialmeer` alone on L206. minor: the void as „Aktives, hochentropisches Potentialmeer aus unkomprimiertem informationellem Lärm.“ (L206).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L44, L56, L199. minor: „Risse (Fissures)“ as K0's manifestation (L199).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L43, L80. not read: on a barred line.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L15, L158. minor: entity profiles carry a TSDP type (L43).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Überwelt` alone on L42. minor: the „Digitalen Überwelt“ as a visualised world (L42).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz-Protokoll` (near `koharenz`), `Kohärenz-Protokolls` (near `koharenz`), `Kohärenz-Konsole` (near `koharenz`). occurrences (J9).
- `mnemosyne`: `Mnemosyne-Archipels` (near `mnemosyne`). an occurrence.
- `moonshine-link`: `Moonshine-Links` (near `moonshinelink`), `invokeMoonshineLink` (near `moonshinelink`). a reading: the moonshine link as transcendent, non-local connection outside AEGIS's control (L221), misread as noise (L225), a catalyst for Kael (L226).
- `ueberwelt`: `Digitalen Überwelt` (near `uberwelt`). a reading — above.


**Readings by the sentence beyond the lookup:**
- **`moonshine-link`** (minor): L221, L225, L226.
- **`dkt`** (minor): the dual kernel theory as cosmological backbone (L187).
- **`kohaerenz-kernel`** (minor): K1 „Coherence Kernel / Order“, ANP, exclusionary order (L190, L191, L193).
- **`kollaps-kernel`** (minor): K0 „Collapse Kernel / Chaos“, EP, Nichts Rauschen (L196, L197, L199).

**Record entries:** none.

**Not promoted:** the API functions, A2UI, Story.ncp.json, the triad, Das Fundament, LFI, Perverse Learning Loop, Paradoxon X, Algorithmic Horror, the deployment plan.

**One reader**: every page above.
