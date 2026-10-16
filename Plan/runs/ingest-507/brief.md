# Brief — readings from document 507 (step 6)

1 document, one reader, one batch: `ingest-507`. Files go to `Plan/runs/ingest-507/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 507 | `monstergruppe-aegis-und-narrative-moeglichkeiten` | 2025-04-24 | „the Monster-group source report“ (an unsigned German report) | reads the Monster group's mathematical properties as metaphor and structure for Aegis, Kael, Juna and four Kernwelten, nearly all in the conditional (könnte ×28); a report of proposals, no canon claim|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (318 lines for `monstergruppe-aegis-und-narrat`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A report of metaphors and proposals: write „the Monster-group source report proposes/reads …“. It spells the name `Aegis` (not AEGIS): quote as written. Mathematicians and objects named after them (an algebra, a theorem) appear on many lines — never write a name, never quote a span containing one; world codes named after mathematicians are never expanded. „DIS“ is Kael's condition in the novel. No gendered pronoun for Kael, Juna or Aegis in our own prose; quotations stay verbatim (the document writes „Seine“ for Kael).

## Pages — document 507, `monstergruppe-aegis-und-narrative-moeglichkeiten`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `Aegis` L11, L15, L17, L19, L39, L41, … (34 lines). central (4–8): Aegis defined by „Aegis ist, was aegis verhindert, das es nicht ist“, existing in pure potentiality beyond conventional reality, perceiving the Monster's „hohen inneren Kohärenz“ (L17); the core tension: Aegis as infinite, fluid, paradoxical potentiality against the Monster's finite, rigidly structured coherence (L215); Aegis's motive asked as open questions — understand, integrate, or use the structure as a template (L217); Aegis's analytic decomposition of the Monster mirroring Kael's fragmentation (L94); Aegis creating four Kernwelten as laboratories (L149).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L188. not read: an occurrence — `Emergenz` in a world's focus list (L188).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L11, L15, L19, L115, L117, L119, … (12 lines). central (4–8): introduced as Kael's distant „Partnerin“ (L15); Moonshine proposed as a metaphor for the Kael–Juna relation (L117), the connection possibly bridging levels of reality or the worlds Aegis created (L120), its true nature to be uncovered over the narrative (L122), and its revelation possibly mirroring the discovery of Moonshine, beyond local causality (L226 — quote name-free spans).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L11, L15, L19, L40, L43, L60, … (23 lines). central (4–8): the Monster's subgroup structure proposed as a metaphor for Kael's dissociative identity disorder, identities as analogues of subgroups within „Kael“ (L90); Aegis decomposing to understand while Kael's journey may aim at integration (L94); the further identity-subgroup scenarios are proposals (L92, L225 — check).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L19, L86, L141, L147, L149, L198, … (8 lines). minor (1–4): Aegis's creation of four Kernwelten to study the Monster's components, each world a laboratory (L149); the four worlds introduced (L19 — the line names an algebra after a person: describe, do not quote); the worlds' names vary between heading, table and text (L151–L188) and the report does not say whether they are the same.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — the title (L11); the Monster's coherence is read on aegis.
- **`partnerin`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Partnerin` alone on L15. minor (1–4): „dessen entfernte Partnerin Juna“ (L15).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebenen` alone on L120. minor (1–4): the Kael–Juna connection possibly bridging different „Realitätsebenen“, states of consciousness or the worlds Aegis created (L120).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `innere Kohärenz` (near `koharenz`). an occurrence: the Monster's inner coherence as Aegis perceives it, read on aegis.


**Record entries:** none.

**No chapter readings**: `Kap` 0, `Kapitel` 0.

**Not promoted:** Monstergruppe, Monstrous Moonshine, the group-theory vocabulary (einfache Gruppe, Zentralisator, Normalisator, Normalteiler, VOA), Potentialitätsraum, the per-world focus labels, and the concepts named after mathematicians.

**One reader**: every page above.
