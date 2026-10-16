# Brief — readings from document 496 (step 6)

1 document, one reader, one batch: `ingest-496`. Files go to `Plan/runs/ingest-496/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 496 | `monstergruppe-babymonstergruppe-fragmentierung-erzaehlung` | 2025-04-23 | „the coset-space report“ (an unsigned German report in ten sections) | analyses the Monster group M and the Baby Monster group B and maps the conceptual removal of B's double cover from M onto Juna's loss and Kael's fragmentation as a coset space; a metaphorical toolkit, no canon claim|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (254 lines for `monstergruppe-babymonstergrupp`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analogy report: write „the coset-space report maps …“; Kael = M and Juna = B are its metaphor, never story facts. M, B, H and 2⋅B stay as codes; many lines name mathematicians (e.g. L50) — never quote a span containing a person's name. Quote verbatim; cut before formulas, bold and inner quotes. No gendered pronoun for Kael or Juna in our own prose.

## Pages — document 496, `monstergruppe-babymonstergruppe-fragmentierung-erzaehlung`

- **`did`** (central, 3–12 quotations): the census's surfaces — `DID` L15, L105, L116, L117, L123, L125, … (16 lines). central (4–8): the coset space as the set of fragments or alternative states (L115); cosets symbolising alter states (L142); the missing group operation as the loss of a single coherent operative self, a core feature of DID (L143); the structural change as an analogy for trauma (L145).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L15, L50, L73, L105, L123, L125, … (16 lines). central (4–8): Juna as B via its double cover: Juna's importance represented by B's structural weight inside M, a central figure (L132); the removal of the subgroup corresponds directly to the loss of Juna (L137); Juna's structural importance, tied to Kael's core stability (L194).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L26, L50, L73, L105, L123, … (29 lines). central (4–8): Kael as M: immense order and complexity, a unique closed entity, read as Kael's identity before fragmentation (L131); Kael's original wholeness and indivisibility (L192); the core metaphor Kael = M, complex and originally unified (L174); the loss does not simplify Kael but disorganises (L195).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — `Kohärenz` L11, L15, L16, L105, L107, L122, … (8 lines). minor (1–4): the report's aim: the effect of a conceptual removal of B on the coherence of M's structure (L15); fragmentation as the loss of group coherence (L174); the loss of coherence (L143).
- **`partnerin`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Partnerin` alone on L15. minor (1–4): Juna named as Kael's Partnerin (L15).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `alters`: `Alter` (near `alters`). an occurrence.


**Record entries:** none.

**No chapter readings**: the report names no chapter (`Kap` 0).

**Not promoted:** Monstergruppe, Babymonstergruppe, Nebenklassenraum, Zentralisator and the other group-theory terms, Kaels Innenwelt, Verlust von Juna, and the person-named groups.

**One reader**: every page above.
