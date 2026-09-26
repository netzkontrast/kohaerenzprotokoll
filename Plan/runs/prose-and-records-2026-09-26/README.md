# Narrative text among the unread, and the open records by vector — 2026-09-26

Asked for together, after the chapter run (`../qmd-chapters-2026-09-26/`) showed
its limit: no Kap 0 question found the narrative Kap 0 text.

**A search places a document to look at. It measures nothing.** Every number below
is a count of this run.

## 1 · Narrative text among the unread documents (`form.json`)

Every unread landed document was measured for form: German or not; personal
pronouns and plan vocabulary (Kapitel, Storyform, Akt, Beat, Konzept …) per
thousand words; the share of long plain paragraphs. The score, pronouns minus
three times plan vocabulary, was calibrated on the two known drafts — the unread
narrative Kap 0 text ranks sixth of 260 German unread documents, the read first
draft of Kap 40 and Kap 0 would rank above it, and the structured outline far
below. Candidates were then opened and read at their start; filenames with
*prosa*, *szene*, *kapitel*, *entwurf* were checked the same way.

**Holding narrative text, by what was read of each:**

| document | date | what, where it starts |
|---|---|---|
| `kp-kap25-2026-09-14-md` | 2026-09-14 | a chapter file: template, summary, outline and scene plan (L23–51), then *Kapitel 25 — Wegkreuzung* in the first person from L52; its session log, `2026-09-14-kap25-vertiefung-md`, says 1,137 → 2,688 words of prose |
| `koharenz-protokoll-kapitel-0-v2-md` | 2026-05-17 | Kap 0 (known from the morning scan) |
| `kohaerenz-protokoll-kapitel-39-das-mosaik-herz` | 2026-02-25 | *Kapitel 39: Das Mosaik-Herz*, from L13 |
| `kohaerenz-protokoll-szene-der-stillstand-der-welt` | 2026-02-25 | *Szene: Die Stasis-Lücke*, Kael in Sektor 04, from L13; no chapter named |
| `kohaerenz-protokoll` | 2025-04-27 | a *Vorwort*, *Genesis der Existenz*, then *Kapitel 1–12* and *14–23* as headings over narrative text (Kap 1 from L126) |
| `einleitung-genesis-der-existenz` | 2025-04-29 | *Vorwort* and Genesis |
| `genesis-prosa-ausformulierung-gesamt`, `genesis-finale-prosa-angepasste-ich-natur` | 2025-04-29 | Genesis in scenes, first person |
| `aegis-genesis-krise-prosa-auftrag`, `-3` | 2025-04-29 | AEGIS' Genesis crisis, a short narrative |
| `kapitel-eins-welterkundung-konstrukt-stadt` | — | a plan for Kap 1 with a narrative sketch at L107–186 |

**Not narrative, despite the name:** `aegis-genesis-krise-prosa-auftrag-2`,
`-formulieren`, `-formulieren-2`, `genesis-krise-aegis-prosa-auftrag`,
`genesis-ein-implementierungsleitfaden-prosa-version`,
`prosaversion-von-genesis-erstellen` — analyses and writing briefs.

**The author, on this list: „There is no prose there" — and then: „Those arent
Texts for the novel - only Research".** So every text above is research that
happens to be narrative, not text for the novel and not a draft of it. It is read
as any research document is, by `ingest`, and nothing from it is the novel's
prose. The search for narrative text stops here: it finds a form, and the form
says nothing about what a document is for.

`grep` over the list, orientation only: the 2025-04-27 document writes `Juna` 138
times and `Julia` never, and the Genesis text of 2025-04-29 writes `734` 32 times —
both earlier than the rename and numbering timeline the wiki holds, so worth
checking whenever these are read.

## 2 · The open records by vector (`records.tsv`, `records-vector.json`)

The morning scan (`../qmd-scan-2026-09-26/`) asked each open record in short BM25
queries. Here each of the same 35 records was written as one German question
(`vec:`) and one hypothetical answer passage (`hyde:`), asked of `sources` with
`--no-rerank`, the unread hits fused by rank, twelve kept per record — 70 queries.

- **Of the 420 placements, 234 are ones the BM25 scan did not make for that
  record** — but only three documents appear that it hit for no record at all:
  `dissoziative-identitaetsstoerung-unsichtbare-diagnose`, `genesis-aegis`,
  `manifest-der-handlungsfaehigkeit-nachhall`. The vectors mostly re-tie known
  documents to other records; they find almost nothing new.
- **47 of the 234 are English documents**, which a German BM25 query cannot reach.
- **Canon-era documents tied to a record for the first time:**
  `koharenz-protokoll-kapitel-0-v2-md` → A11 (the Abhandlung's Setzungen — the
  Wir voice, warmth in Kap 0, the shards at both ends);
  `dual-storyform-hintergruende-md` → A6, A11;
  `worldbuilding-konzept-kohaerenzprotokoll-md` → C1, C9;
  `systemic-architecture-specification-the-coherence-protocol-w` → C11;
  `the-architecture-of-fracture-a-compendium-of-the-kael-system` → A7, A13;
  `kohaerenz-protokoll-philosophischer-bericht-md` → A3 — a name, where a vector
  match says nothing (A3 is `Mira`; `grep -w` still finds it in one read document).
- **The document most often tied only by vectors** is
  `an-inquiry-into-the-unresolved-questions-and-thematic-tensio` (2025-10-15),
  for twelve records: a document about open questions answers open questions.
