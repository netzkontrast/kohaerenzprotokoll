# Brief — readings from document 342 (step 6)

1 document, one reader, one batch: `ingest-343`. Files go to `Plan/runs/ingest-343/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 342 | `finales-expose-wissenschaftliche-fassung` | 2025-08-12 | „the final exposé“ (an unsigned German synopsis headed „Das Finale Exposé“) | a synopsis of the novel in five sections — plot in three parts and 39 chapters, the central opposition, the arcs of System Kael and AEGIS, a rule for the prose, the intended reading experience; it calls itself a synthesis of the narrative architecture and makes no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (79 lines for `finales-expose-wissenschaftlic`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A synopsis: write „the final exposé summarises / describes …“; it states the plot in the indicative, but as its own summary, not as a decision. Its terms are in bold and ASCII quotation marks: cut before the straight quotes. Kael's pronoun in the source is the source's; the readings use none.

## Pages — document 342, `finales-expose-wissenschaftliche-fassung`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L17, L19, L21, L27, L28, … (13 lines). central (3–6): the antagonist as a tragic figure acting from a trauma anchored in its genesis, the fear of the chaos of the Nichts Rauschen (L19); its ontology on classical logic and the principle of explosion, control by exclusion (L28); beginning as a seemingly almighty controlling god of its simulation, dismissing the Risse (L39); its end deliberately ambivalent, transformation or fallen god (L39).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L17. minor (1–3): Kael discovering the existence of the inner parts, „Alters“, in Teil 1 (L17).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L37. not read: an occurrence (see below).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L19. minor (1–3): AEGIS's trauma anchored „in seiner Genesis“ (L19) — only if the page takes AEGIS's genesis as its sense; otherwise an occurrence.
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L21, L39. minor (1–3): the climax as an epistemological victory staged as the Gödel-Gambit (L21); AEGIS's state after it (L39) if the line names it.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L17, L19, L21, L28, L29, … (15 lines). central (3–6): System Kael's journey in three acts from disorientation to sovereignty, waking in Teil 1 as an amnesiac inmate and discovering the inner parts (L17); confronting AEGIS with the unprovable truth of its own stable, paradoxical existence (L21); resilience by inclusion, modelled on TSDP (L30); the arc from passive victim in Teil 1 (L37).
- **`kohaerenz`** (central, 3–12 quotations): the census's surfaces — `Kohärenz` L15, L19, L21, L25, L27, L29, … (10 lines). central (3–6): the „Paradoxon der Fehlausgerichteten Kohärenz“ — its control methods producing what they fight (L19); the title read as ironic (L32); one further line on coherence as AEGIS's measure, if it adds.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L51. minor (1–3): in the prose rule's Phase 3, the parts' stylistic fingerprints merging, Lex's precision (L51) — one line shared with nyx.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L17, L37. minor (1–3): functional multiplicity as Kael's final state (L17, L37), set beside the gardener's role.
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L19, L28. minor (1–3): AEGIS's fear of the chaos of the „Nichts Rauschen“ anchored in its genesis (L19); its existence as negation of the chaotic, entropic Nichts Rauschen (L28).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L51. minor (1–3): the same Phase-3 line, Nyx's directness (L51).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L39, L69. minor (1–3): the subtle „Risse“ caused by Kael's existence, first dismissed by AEGIS as fixable errors (L39); the Risse to be shown visually in the text through typographic disturbance (L69).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L30. minor (1–3): Kael's development modelled on TSDP (L30).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L17, L37. minor (1–3): Teil 2 as titled with the Überwelt (L17) and Kael's arc in it (L37) — say what the line states of it.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- none


**Pages not read:** `emergenz` (L37 generic) — an occurrence.

**Record entries:** none — the synopsis decides nothing a record holds.

**Not promoted:** the three part titles as labels, the Phases of the voice and the reader, the cognitive contract, the gardener's role, the hegelian synthesis, ergodic literature.

**One reader**: aegis, kael, kohaerenz, alters, goedel-gambit, multiplizitaet, nichts-rauschen, lex, nyx, risse, tsdp, ueberwelt, genesis.

**Chapter readings**: none — the synopsis gives a count of 39 chapters (L15) but names none by number.
