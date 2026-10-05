# Brief — readings from document 68 (step 6)

1 document, one reader, one batch: `ingest-68`. Files go to `Plan/runs/ingest-68/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 68 | `uberarbeitete-optimierte-plotline-genesis-der-existenz` | 2025-04-29 | „the plotline's Version 2“ | a German revision outline of the Genesis narrative, Version 2, in ten scenes and three parts, with goals, numbered beats and notes (`Annotation`, `Anmerkungen`, `Balanceakt`); it „integriert die neuen Plot-Elemente bezüglich der externen Entität, des Erwachens des Ichs und des spezifischen internen Konflikts“ (L13) and claims no canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (195 lines for `uberarbeitete-optimierte-plotl`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** **A plan for a narrative, revised.** Write „Version 2 plans …“ / „in Version 2's scene N …“. Its notes are reasons, not story. It revises the plotline read as document 67 (`optimierte-plotline-genesis-der-existenz`) and the narrative of document 65: you may name the one change each page's subject undergoes, citing the earlier document's line once, and compare nothing else. **What is new in Version 2**: the external entity's signature resonates with the latent signature of Komponente 734, „dem Echo der Unvollständigkeit“ (L119); the Ich in 734 wakes and wants connection with the entity (L138); the entity is indivisible, with multiple contradictory symmetries (L139); AEGIS isolates 734 as the internal source of a corruption that strives toward the threat (L145, L152); Kael is born longing for the entity (L177, L191). The outline never names the entity: never call it Juna or M — say „the external entity“.

## Pages — document 68, `uberarbeitete-optimierte-plotline-genesis-der-existenz`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L57, L59, L61, L75, L83, L95, … (23 lines). central (3–6): AEGIS's misreading of the entity's resonance with 734 (L119), its registering of 734's change (L121), its closer analysis — the entity indivisible, with contradictory symmetries, against AEGIS's logic of minimal symmetry and negation (L139), the twofold threat, an external paradox and a corrupted inner component (L144, L145), the decision for the protocol newly reasoned (L152), the cuts from AEGIS's side (L170), coherence restored by its own definition (L173).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L139. not read: sweep occurrence (L139).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L11. central (3–5): Version 2's sequence — the fragment with the feeling of something missing (L29), AEGIS's birth (L61), Komponente 734 (scene 5, L73), the entity's arrival (L104), the Ich waking (L125, L138), the protocol (L152), Kael's birth (L177). Count no beats beyond its scenes.
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L175, L177, L182, L191, L194. central (2–4): scene 10 (L175), its goal: Kael born as a mosaic, „geprägt von Trauma *und* der fragmentierten Erinnerung/Sehnsucht nach der Entität“ (L177 — quote around the asterisks), the outlook: Kael differently motivated than AEGIS, seeking wholeness and connection (L182), the fragments waking in the Kernwelten (L190), their longing (L191). Differ line: Kael born longing for the external entity.
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L190, L193. minor (1–2): the fragments come to themselves in the Kernwelten (L190); the broken reality (L193).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — `Kohärenz` L27, L40, L68, L97, L119, L139, … (9 lines). minor (1–2): the entity as a paradox that threatens AEGIS's `Kohärenzprinzip` (L144); coherence restored „nach AEGIS' Definition“ (L173).
- **`komponente-734`** (minor, 1–4): the census's surfaces — `Komponente 734` L73, L119, L120, L121, L138, L145, … (7 lines). central (3–5): scene 5 (L73), a functional unit, e.g. „Grenzanalyse Delta“ (L80); the latent signature, the echo of incompleteness, resonating with the entity (L119); something deeper triggered in 734 (L120); the Ich in 734 waking into a will to connect with the entity (L138); 734 no longer latent but actively corrupted (L145); its elimination or isolation (L152).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L86; `Simulation` L88, L93, L95, L98. minor (1–2): the Überwelt scene as Version 2 plans it (find its lines; `Simulation` and `Echo in der Simulation` are its words).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `did`: `Entität` (near `diddissoziativeidentitatsstruktur`), `Entität` (near `dissoziativeidentitatsstruktur`), `Fragment` (near `psychischefragmentierung`). occurrence: `Entität` is the external entity; `Fragment` the story's.
- `entropie-resonanz`: `Resonanz` (near `entropieresonanz`), `Resonanz` (near `entropieresonanzentropieresonanzprotokolleerp`), `Resonanz` (near `entropieresonanzprotokolle`), `Protokoll` (near `entropieresonanzentropieresonanzprotokolleerp`), `Protokoll` (near `entropieresonanzprotokolle`). occurrence: `Resonanz` is the entity's resonance with 734 (J69).
- `mosaik-herz`: `Mosaik` (near `mosaikherz`). occurrence: `Mosaik` is how Kael is born (L177); named in kael's reading.
- `nichts-rauschen`: `Nichts Rauschens` (near `nichtsrauschen`), `Rauschen` (near `nichtsrauschen`). reading (1): the fragment awakening in the Rauschen (find the lines; quote around inner marks).
- `nullpunkt-protokoll`: `Protokoll` (near `nullpunktprotokoll`). occurrence (J69).
- `protokoll-v14`: `Protokoll` (near `protokollv14`). occurrence (J69).
- `resonanz-landschaft`: `Resonanz` (near `resonanzlandschaft`). occurrence (J69).
- `trennungsprotokoll`: `Protokoll` (near `trennungsprotokoll`). reading (1–3), J114: the decision for the protocol, newly reasoned (L152), the cuts from AEGIS's side and from the woken Ich's (L170, L171), isolation of the fragments carrying the memory of belonging to the entity and the trauma of separation (L172). The outline writes `Protokoll` once and never `Trennungsprotokoll` (count it).


**Pages the lookup did not list, added by the reconciler:**

- **`residual-echos`** (1–2): the echoes of the past and of absence — a lost order and a vague incompleteness, as if a part of one's own structure were missing (L29); the latent signature of 734, the echo of incompleteness (L119). The outline does not write `Residual-Echos` (count it).

**Record entries** (one file each in `Plan/runs/ingest-68/readings/`):

- **`c12-genesis-beats`**: Version 2's order — 734 (scene 5), the entity and the Ich's waking (scenes 7–8), the protocol, Kael (scene 10). The component precedes the protocol.
- **`c16-kael-origin`**: Kael born from the fragments of 734 inside AEGIS, carrying a longing for an external entity whose signature resonated with what 734 lacked (L119, L177, L191) — the inside origin with an outside pull. Say it in the record's terms.
- **`q7-what-734-names`**: 734 as a functional unit, „Grenzanalyse Delta“ (L80), with a latent signature (L119).
