# Brief — readings from document 444 (step 6)

1 document, one reader, one batch: `ingest-445`. Files go to `Plan/runs/ingest-445/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 444 | `canonical-narrative-architecture-for-kohaerenz-protokoll` | 2025-11-03 | „the canonical-architecture report“ (an unsigned English report, „Report on the Canonical Narrative Architecture“) | declares resolutions of four contradictions — the protagonist's identity, AEGIS's fate, the nature of the climax, the Guardians — and a three-act summary; calls itself canonical and definitive (L15, L27, L55, L103), a claim recorded and never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (140 lines for `canonical-narrative-architectu`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A report that declares: write „the canonical-architecture report declares …“ — its „canonical resolution“ is its own claim, recorded, never applied; nothing it declares is the author's decision. Quote the English as written; cut before straight quotes, bold and italics markers and glued footnote digits. No gendered pronoun for Kael, AEGIS or any part — use the names (quotations stay verbatim, including the document's own „male“ and „his“). Never write a real person's name nor a term carrying one (a cited story title names a thinker, L109), nor quote a span containing one.

## Pages — document 444, `canonical-narrative-architecture-for-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L36, L42, L48, L55, L61, L62, … (16 lines). central (4–8): the declared resolution: AEGIS is not destroyed but forced into a permanent, pathological state of „algorithmic melancholy“ (L55 — cut before the straight quote), against a system crash (L50); the climax as an internal, psycho-ontological confrontation that forces AEGIS's transformation from within (L79); Act III: the systemic transformation (L127).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L33. minor (1–4): named among Kael's key alters (L33).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L91, L93, L99, L103, L126, L127, … (7 lines). minor (1–4): the declared resolution: „the Guardians are not a monolith“ — the „Guardian's Dilemma“ as canonical element, with possible rebel Guardians (L103 — cut before the straight quotes); the contradiction stated: monolithic enforcers or a Wächter-Zwiespalt (L99); rebel Guardians aiding Kael in Act III (L127).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L87. minor (1–4): the „Juna/V connection“ as narratively crucial because it gives Kael gnosis — external elements are catalysts, not saviours (L87).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L25, L27, L33, L34, L35, L36, … (24 lines). central (4–8): the declared resolution: „The protagonist is a male entity named“ Kael, host personality of a complex internal system — „System Kael“ (L27 — cut before the straight quotes); its evidence: the name and male pronouns used for the protagonist and key alters across cited documents (L33); the core conflict, the ANP-EP phobia (L34); Kael's arc from fragmentation to functional multiplicity as the plot's engine (L85); Kael's final state as a „living Gödel-Satz“ (L62 — describe, the term carries a name); Act I–III (L125–L127).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — the novel's title (L11).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L33. minor (1–4): named among Kael's key alters in the evidence for the name and pronouns (L33).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L33. minor (1–4): named among Kael's key alters (L33).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L33. minor (1–4): named among Kael's key alters (L33).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L33. minor (1–4): named among Kael's key alters (L33).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L126. minor (1–4): Act II: System Kael begins to perceive and test the rules of AEGIS's simulated reality, the Risse (L126 — find the span).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L27, L33, L34, L40, L136. minor (1–4): System Kael modelled on the clinical framework of tertiary structural dissociation (L27); TSDP as the architectural diagnosis of Kael's fragmentation (L40); the ANP-EP phobia (L34).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Krise` (near `genesis`). an occurrence: named in the document's general sense.
- `juna`: `Juna/V connection` (near `juna`). an occurrence: named in the document's general sense.
- `personas`: `Tertiary Structural Dissociation of the Personality` (near `persona`). an occurrence: named in the document's general sense.


**Record entries** (one file each, formatted as earlier entries — `ls Plan/runs/ingest-*/readings/c17-*`, `ls Plan/runs/ingest-4*/readings/q1-*`, `ls Plan/runs/ingest-44*/readings/q8-*`):
- **`c17-kael-gender`**: the canonical-architecture report states the contradiction over the protagonist's name and gender (L23) and declares „a male entity named“ Kael, host of System Kael (L27), on the evidence of male pronouns in cited documents (L33) — its claim, recorded, not applied and not decided.
- **`q8-aegis-after-the-vortex`**: it declares that AEGIS is not destroyed but forced into „algorithmic melancholy“ (L55), against a system crash (L50) — recorded, not applied.
- **`q1-guardians-and-aegis`**: it declares the Guardian's Dilemma canonical, the Guardians not a monolith, rebel Guardians possible (L99, L103) — recorded, not applied.

**Not promoted:** System Kael, ANP-EP Phobia, functional multiplicity (the English form), algorithmic melancholy, living Gödel-Satz, psycho-ontological confrontation, Guardian's Dilemma, Wächter-Zwiespalt, Rebel Guardian, Juna/V connection, The Foundation, Stories 22, 25 and 29, and the borrowed concepts.

**One reader**: every page above and the three record entries.

**Chapter readings**: none — the document names no chapter.
