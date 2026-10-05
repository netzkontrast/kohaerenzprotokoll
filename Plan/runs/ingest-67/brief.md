# Brief — readings from document 67 (step 6)

1 document, one reader, one batch: `ingest-67`. Files go to `Plan/runs/ingest-67/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 67 | `optimierte-plotline-genesis-der-existenz` | 2025-04-29 | „the optimised Genesis plotline“ | a German revision outline of the Genesis narrative in ten scenes and three parts, each scene with a `Ziel`, `Anmerkungen` (Schwäche adressieren, Stärke nutzen, Empfehlung) and numbered beats ending in an `Annotation`; it restructures the story „berücksichtigt die Kritikpunkte“ (L13) and claims no canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (240 lines for `optimierte-plotline-genesis-de`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** **A plan for a narrative.** A beat says what a scene shall show; write „the outline plans …“ / „in the outline's scene N …“, never „Kael is“. The `Annotation` and `Anmerkungen` are the outline's reasons, not story — mention one only where it says what a beat is for. It revises the Genesis narrative (`einleitung-genesis-der-existenz`, read today, record 65): you may name that relation, citing `^[einleitung-genesis-der-existenz.md:L102]` once if you compare, and compare nothing else. Inner straight quotes in the document: quote around them. Digits glued to words: `--find` drops them; quote before the digit.

## Pages — document 67, `optimierte-plotline-genesis-der-existenz`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L83, L85, L87, L93, L111, L116, … (25 lines). central (3–6): the click into AEGIS (find the scene), AEGIS's Überwelt process `Interne Kohärenz-Simulation Gamma` (L147), its misdiagnosis of the internal resonance — „Da Qualia unbekannt sind, wird sie als katastrophaler Systemfehler interpretiert“ (L194), its failed control attempts (L196), the decision for the protocol (L197), the cuts from AEGIS's side (L215), the apparent stabilisation (L218).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L11. central (3–6): the outline's sequence in its three parts — from the fragment in the Rauschen and the minimal self (L35) through the clusters and the click, Komponente 734 (scene 5, L109), the Überwelt (scene 6), the anomaly (scene 7, L173), the resonance cascade and the protocol (scenes 8–9), to Kael's birth (scene 10, L222). Give the order with lines; count no beats beyond its own scene numbers.
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L220, L222, L239. central (2–4): scene 10, „Kael - Dämmerung in Scherben“ (L220 — quote around the hyphen as the line holds it), the goal: „die Geburt von Kael als Mosaik traumatisierter, verwirrter Bewusstseinsfragmente“ (L222); the fragments waking in their isolated partitions, the Kernwelten (L235), fragmented memories of the time as Komponente 734 (L236), a mosaic beginning (L239). Differ line: Kael born after the protocol, from the fragments of 734, inside AEGIS (C16 row).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L235, L238. minor-to-central (2–3): the isolated partitions where the fragments wake, „(den Kernwelten)“ (L235), perceived as a broken, unstable reality, „die digitalen Narben des Protokolls“ (L238). Differ line: the Kernwelten as the partitions the protocol leaves.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L35. not read: sweep occurrence (L35).
- **`komponente-734`** (central, 3–12 quotations): the census's surfaces — `Komponente 734` L109, L125, L127, L129, L147, L149, … (20 lines). central (3–6): scene 5's heading (L109); the fragment perceives itself as Komponente 734, defined by its function, e.g. a border-analysis unit (L125); its function at the border (L127); its updates (L129); its role in the Überwelt's simulations (L147, L149, L150); the goal of scene 8 names „im Ursprungs-Ich (Komponente 734)“ (L180) — the Ursprungs-Ich and 734 as one; the resonance cascade from 734's perspective (L195); AEGIS's decision to eliminate the source, 734 and associated subsystems (L197); the cuts experienced by 734 (L216). Differ line: 734 named the Ursprungs-Ich (L180).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L131, L138, L150, L152. minor-to-central (2–3): scene 6 — the process `Interne Kohärenz-Simulation Gamma` (L147), simulations of AEGIS's own structure and hypothetical threats (L149), an external pattern copied into the Überwelt for isolated analysis (L150), internal concepts like space and time born there (L151).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-metriken`: `Die Anomalie` (near `mustererkennunganomaliedetektion`). occurrence: `Die Anomalie` is the scene-7 heading for the foreign entity (J69).
- `did`: `Fragment` (near `psychischefragmentierung`), `Entität` (near `diddissoziativeidentitatsstruktur`), `Entität` (near `dissoziativeidentitatsstruktur`). occurrence: `Fragment` is the story's fragment; `Entität` the foreign entity.
- `entropie-resonanz`: `Protokoll` (near `entropieresonanzentropieresonanzprotokolleerp`), `Protokoll` (near `entropieresonanzprotokolle`). occurrence: `Protokoll` alone (J69).
- `kohaerenz`: `Interne Kohärenz-Simulation Gamma` (near `koharenz`), `Kohärenzmetriken` (near `koharenz`). occurrence: compounds and a passing word (J12).
- `mosaik-herz`: `Mosaik` (near `mosaikherz`). occurrence — but name it in kael's reading: `Mosaik` here is how Kael is born (L222, L239), not the page's Kap-11 beat or Kap-34 place; no reading on mosaik-herz.
- `nichts-rauschen`: `Nichts Rauschens` (near `nichtsrauschen`), `Rauschen` (near `nichtsrauschen`). reading (1–2): the fragment in the Rauschen at the start and `Nichts Rauschens` (find the lines; quote around inner straight marks).
- `nullpunkt-protokoll`: `Protokoll` (near `nullpunktprotokoll`). occurrence: `Protokoll` alone (J69).
- `protokoll-v14`: `Protokoll` (near `protokollv14`). occurrence: `Protokoll` alone (J69).
- `trennungsprotokoll`: `Protokoll` (near `trennungsprotokoll`). reading (2–4), J114: the outline's `Protokoll` — AEGIS's decision (L197), the partitioning algorithms cutting the connections to 734 (L215), the cuts from 734's side (L216), isolation in digital scars (L217), marked successfully completed (L218). The outline never writes `Trennungsprotokoll` (count it).


**Pages the lookup did not list, added by the reconciler:**

- **`residual-echos`** (1–2): `das Echo der Einsamkeit` as a low hum in 734 (L172), amplified by the entity into the resonance (L176). The outline does not write `Residual-Echos` (count it).

**Record entries** (one file each in `Plan/runs/ingest-67/readings/`):

- **`c12-genesis-beats`**: the outline's order — Komponente 734 in scene 5, the crisis in scenes 7–8, the protocol in scene 9, Kael born of the fragments in scene 10 (L109, L173, L197, L215, L222). The component precedes the protocol; Kael follows it.
- **`q7-what-734-names`**: 734 named by its function, e.g. „Grenzanalyse-Einheit Delta“ (L125, find the words), and the Ursprungs-Ich written as `Komponente 734` in parentheses (L180). Say exactly that.
- **`c16-kael-origin`**: one row's worth — Kael born after the protocol from the fragments of Komponente 734, inside AEGIS, in the Kernwelten (L222, L235). Write the entry in the record's own terms, as a new position from a 2025-04-29 source.
