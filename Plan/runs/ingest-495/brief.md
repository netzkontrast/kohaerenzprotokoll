# Brief — readings from document 495 (step 6)

1 document, one reader, one batch: `ingest-495`. Files go to `Plan/runs/ingest-495/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 495 | `monstergruppe-babygruppe-und-kael` | 2025-04-23 | „the Monster-group analogy report“ (an unsigned German report) | maps the Monster group M onto Kael and the Baby Monster group B onto Juna, each mathematical fact followed by an analogy, and reads Juna's loss as the fragmentation of Kael's coherence; an analogy, no canon claim|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (267 lines for `monstergruppe-babygruppe-und-k`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analogy report: write „the Monster-group analogy report maps …“ or „reads …“; what it says of Kael and Juna is analogy, never a story fact. M and B stay as codes; the report names mathematicians and person-named groups and algebras — never quote a span containing a person's name. Quote verbatim; cut before bold, italics and inner quotes. No gendered pronoun for Kael or Juna in our own prose (the report uses them; quotations verbatim).

## Pages — document 495, `monstergruppe-babygruppe-und-kael`

- **`did`** (minor, 1–4): the census's surfaces — `DID` L15, L151, L159, L177. minor (1–4): Kael's fragmentation compared with a dissociative identity disorder (L15, L151, L159); advice to show DID as fragmentation of one system rather than separate personalities (L177).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L15, L17, L45, L47, L51, L55, … (49 lines). central (4–8): Juna paired with B (L15, L47); not external to Kael (L55), with an own complexity, inner world and agency (L63); the doubled B as the centraliser of the 2A involutions read as Juna stabilising a central aspect of Kael, and the loss destabilising exactly that (L83–L87 — describe the codes); the loss as the triggering event (L158, L172).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L17, L21, L23, L25, L29, … (61 lines). central (4–8): Kael paired with M, the gigantic group (L15, L27); size and indivisibility read as a possibly indivisible core (L33) and an identity that fits no common scheme (L37); after Juna's loss Kael exists on as a basic individual, what suffers is coherence, intelligibility and functioning (L105); the collapse not random (L123); advice to show DID as fragmentation of one system (L177).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — `Kohärenz` L105, L107, L125, L158, L174, L177. minor (1–4): what suffers after Juna's loss is the coherence of Kael's inner structure (L105, L107); coherence in the analogy's table (L174) and in the advice (L177).
- **`partnerin`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Partnerin` alone on L15. minor (1–4): Juna named as Kael's Partnerin, paired with B (L15).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L109. not read: an occurrence — L109 is a section heading using „Risse“ as a figure for what becomes unclear, not the novel's Risse.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- none


**Record entries:** none.

**No chapter readings**: the report names no chapter (`Kap`, `Kapitel`, `Chapter` each 0).

**Not promoted:** Monstergruppe, Baby-Monstergruppe, Kael-Juna-Struktur, Kaels Welt, the group-theory terms (Involution, Zentralisator, maximale Untergruppe, sporadische Gruppe and the rest), and the person-named algebras and groups.

**One reader**: every page above.
