# Brief — readings from document 536 (step 6)

1 document, one reader, one batch: `ingest-536`. Files go to `Plan/runs/ingest-536/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 536 | `sf-roman-eroeffnung-fesselnde-techniken-analysiert` | 2026-03-31 | „the opening analysis“ | an analysis of how published hard-SF and horror novels open, a verdict on the novel's concept document, a proposed strategy for the first fifty pages and a drafted opening scene of about 500 words (L148–L192); a critique and a proposal, no canon claim|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (251 lines for `sf-roman-eroeffnung-fesselnde-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A critique and proposal: write „the opening analysis proposes …“; its drafted scene is a proposal, never canon. Where it reports the concept document (footnote „1“), say so. **Cite only L104–L146 and the scene L154–L192; never cite L140** (an earlier name) and never any line before L100 or after L193 (real persons and works). Never quote a span holding a person's name or a person-named principle (L102, L106 is fine only for the two kernel names, L108, L112, L132, L134, L138, L150 are not cited). No gendered pronoun for Kael, Juna, AEGIS or any part in our own prose; quotations stay verbatim, cut before pronouns where possible.

## Pages — document 536, `sf-roman-eroeffnung-fesselnde-techniken-analysiert`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L114, L120, L132, L142, L144, L146. central: dominates the first simulated Kernwelt (L114); with Lex proves Juna an anomaly (L120); not a classic villain but cosmic horror through absolute non-anthropomorphic order, an environmental condition (L144); „die Abwesenheit von Zufall und Ambiguität“, rates Kael's suffering as „Datenkorruption“ (L146, reported from the concept document).
- **`dkt`** (minor, 1–4): the census's surfaces — `Dual Kernel Theorie (DKT)` L13, L112; `DKT` L13, L112, L122, L124. minor: the reader must not be taught the Dual Kernel Theorie (L112 — not cited, a work title on it); „Die DKT-Physik bleibt absolut unsichtbar.“ (L124).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L132. not read: an occurrence — `Entropie` stands in a table row naming a person-named principle (L132).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L120, L132. minor: the absence that haunts Kael, a person who by the world's logic „niemals existiert hat“ (L120); AEGIS and Lex prove Juna a fictive anomaly (L120); in the scene only „Ein Bild von *ihr*.“ (L176) and a name on the tongue (L178).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L114, L116, L118, L120, L130, L131, … (16 lines). central: in the first simulated Kernwelt Logos-Prime, a somatic glitch breaks the order (L114); the problem is loss of control and loneliness (L118); haunted by Juna's absence (L120); loses time (L140 — not cited); the scene: the clock jumps (L160), raw knuckles (L166), the heat (L168, L170), the wound gone (L184, L186), „„Alles ist kohärent“, flüsterte er.“ (L190).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelt` L114. minor: Logos-Prime as „der ersten simulierten Kernwelt“ (L114).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L140. not read: named only on L140, which holds an earlier name.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. not read: an occurrence — the title (L13) (J9).
- **`kohaerenz-kernel`** (minor, 1–4): the census's surfaces — `Kohärenz-Kernel` L106. minor: the reader does not identify with „Kohärenz-Kernel“ (L106, reported from the concept document; the symbol lost in export); the `-Kernel` of reversible computation, total order (L114).
- **`kollaps-kernel`** (minor, 1–4): the census's surfaces — `Kollaps-Kernel` L106. minor: „Kollaps-Kernel“ (L106, reported; the symbol lost); the unerased trauma as the second `-Kernel` breaking in (L114).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L120, L140. minor: Kael's own rational part Lex, with AEGIS, proves Juna a fictive anomaly (L120).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L118. minor: Kael's problem on the first fifty pages must not be „Funktionalen Multiplizität“ (L118, reported from the concept document).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L140. not read: named only on L140, which holds an earlier name.
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Glitch` alone on L114. minor: the unexplained somatic „Glitch“ breaking into the order is the hook (L114).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L13, L136, L138, L150. minor: the dissociated parts (TSDP) as heading (L136); not to be introduced as a role-play menu, which would ruin the clinical TSDP (L138 — not cited; L136 only).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kaels-wohneinheit`: `Kaels` (near `kaelswohneinheit`), `Kaels` (near `kaelswohneinheit10`). an occurrence: the possessive `Kaels`.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Paradox der fehlausgerichteten Kohärenz` (near `koharenz`), `Kohärenztheorie der Wahrheit` (near `koharenz`). occurrences: the title, a paradox's and a theory's name (J9).
- `logos`: `Logos-Prime` (near `logos`). an occurrence: the world Logos-Prime, read on kern-welten.
- `multiplizitaet`: `Funktionalen Multiplizität` (near `multiplizitat`). a reading — read above.
- `sektor-04`: `Sektor` (near `sektor04`). an occurrence: „Sektor Logos-Prime“ (L156), not Sektor 04.


**Reading by the sentence beyond the lookup:**
- **`algorithmische-melancholie`** (minor): nor may the problem be the defence against „Algorithmischen Melancholie“ (L118, reported from the concept document).

**Chapter readings:** none — „Kapitel 1–5“ (L122) names a range for the physics' invisibility, not a chapter's content.

**Record entries:** none.

**Not promoted:** EP, ANPs, Sensory Rulebooks, Datenkorruption, fehlerhaften Gott, Sensorik-System, Reversible Berechnung, totale Ordnung, Informationslöschung, Abwärme, Kontrollverlust, somatisches Erzählen, Hook, Alles ist kohärent, the craft lenses, every person-named principle and theorem.

**One reader**: every page above.
