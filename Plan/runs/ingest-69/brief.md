# Brief — readings from document 69 (step 6)

1 document, one reader, one batch: `ingest-69`. Files go to `Plan/runs/ingest-69/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 69 | `uberarbeitete-optimierte-plotline-13-szenen-genesis-der-exis` | 2025-04-29 | „the plotline's Version 3“ | a German revision outline of the Genesis narrative, Version 3, which expands Version 2 to 13 scenes in three parts; scenes 6, 8 and 10 are new (`NEUE Szene`), the others carry their old number (`Ursprünglich Szene`); goals, beats, `Anmerkungen`, `Optimierung` notes; no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (221 lines for `uberarbeitete-optimierte-plotl`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** **A plan, the third version of one outline.** Version 2 (`uberarbeitete-optimierte-plotline-genesis-der-existenz`, record 68) is already read; this one keeps its story and adds three scenes. **Read only what is new or changed here**, so each reading is short: scene 6, the system diagnosis and 734's latent anomaly (L86–L107); scene 8, the limits of simulation — AEGIS meets what it cannot model and classifies it away (L123–L144); scene 10, the entity fed into the Überwelt and the simulation failing, the entity „unsimulierbar“ (L161–L181). For a page whose subject Version 3 tells exactly as Version 2 did, write one sentence saying so, citing one line, or report not read. Write „Version 3 plans …“. Never name the external entity Juna or M. Inner straight quotes: quote around them; asterisks: quote around them.

## Pages — document 69, `uberarbeitete-optimierte-plotline-13-szenen-genesis-der-exis`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L13, L57, L59, L61, L69, L75, … (36 lines). central (3–5): the new scenes — the system diagnosis and self-monitoring (scene 6, L88 on), AEGIS classing the unmodellable as `außerhalb relevanter Parameter` and optimising only its internal models (L143), the highest alarm and the entity fed into the Überwelt (L177), the simulation failing and AEGIS's conclusion that the entity is fundamentally incompatible with its understanding of reality and coherence (L179–L181); the „Hybris“ the outline names (L125, quote around the inner marks).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L11. minor (1–2): Version 3's 13 scenes in three parts (find the part headings) — the sequence as Version 2's with three inserted scenes; cite the new ones' lines.
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L209, L211, L217, L220. minor (1): scene 13, Kael born as a mosaic, marked by trauma and fragmented longing (L211) — as in Version 2; one sentence.
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L219. minor (1) or not read: only if Version 3 changes what it says (find the line); otherwise report not read with the line.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L27. not read: sweep occurrence (L27); `Kohärenz-Fragment` (L157) is AEGIS's misreading of the entity, a compound.
- **`komponente-734`** (minor, 1–4): the census's surfaces — `Komponente 734` L73, L103, L104, L107, L140, L141, … (9 lines). minor (1–3): new in Version 3 — the latent anomaly in 734 stressed in scene 6 (L88), 734 experiencing the beauty of the pure constructs and returning with the unconscious knowledge that AEGIS's understanding has gaps (L141, L144), 734 drawn into the Überwelt to simulate the entity (L178).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L109, L116, L125, L140, L141, L163, … (9 lines). central (3–5): scene 7 as tool of optimisation and reality construction (L111); scene 8 — an ambitious simulation of the Nichts Rauschen's origins or of alternative coherent systems (L140), the limit of the model (L142), AEGIS classifying the unmodellable away (L143); scene 10 — the Überwelt as AEGIS's mightiest tool of analysis failing before the entity (L177–L181). Differ line: the Überwelt shown failing, in two new scenes.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `did`: `Entität` (near `diddissoziativeidentitatsstruktur`), `Entität` (near `dissoziativeidentitatsstruktur`), `Fragment` (near `psychischefragmentierung`). occurrence.
- `entropie-resonanz`: `Protokoll` (near `entropieresonanzentropieresonanzprotokolleerp`), `Protokoll` (near `entropieresonanzprotokolle`). occurrence (J69).
- `kohaerenz`: `Kohärenz-Fragment` (near `koharenz`). occurrence: AEGIS's misreading of the entity (L157), a compound (J12).
- `mosaik-herz`: `Mosaik` (near `mosaikherz`). occurrence (Kael's birth as mosaic, L211).
- `nichts-rauschen`: `Nichts Rauschens` (near `nichtsrauschen`), `Rauschen` (near `nichtsrauschen`). reading (1) only if new: the Nichts Rauschen as what AEGIS tries to model and cannot (L140, L142); else not read.
- `nullpunkt-protokoll`: `Protokoll` (near `nullpunktprotokoll`). occurrence (J69).
- `protokoll-v14`: `Protokoll` (near `protokollv14`). occurrence (J69).
- `trennungsprotokoll`: `Protokoll` (near `trennungsprotokoll`). minor (1) or not read: scene 12, `Die Zerstückelung` (L196, L198), as in Version 2; say the outline names the act Zerstückelung and writes `Protokoll` (count both); one sentence.


**Record entries:** none needed — C12, C16 and Q7 hold Version 2's positions, which Version 3 keeps. If a scene of Version 3 changes the order of component, protocol and Kael, write a one-line `c12-genesis-beats` entry saying so; otherwise none.
