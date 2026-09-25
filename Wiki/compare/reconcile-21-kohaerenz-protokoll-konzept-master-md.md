---
document: kohaerenz-protokoll-konzept-master-md
against: 93 pages, 15 conflicts
ran: "2026-09-25"
candidates: 478
decisions: 554
by_lookup: 290
judgements: 264
new_pages: 1
new_readings: 47
---

# Reconciliation 21 — `kohaerenz-protokoll-konzept-master-md` against the wiki

`python3 scripts/reconcile.py kohaerenz-protokoll-konzept-master-md`

478 candidates, 554 decisions — **290 by lookup, 264 to judgement**, and one sweep hit.
Document 20, „KOHÄRENZ PROTOKOLL — Konzeptioneller Master-Report" ^[kohaerenz-protokoll-konzept-master-md.md:L11] of 2026-05-08: the
theory of the novel in seventeen parts — its physics, the truth theories, the thirteen
Alters, AEGIS, Juna, the Kern-Welten, two storyforms, the reader, open points and
rules for the prose. „Er ist nicht erzählerisch, sondern operativ" ^[kohaerenz-protokoll-konzept-master-md.md:L29].

It ranks its sources (L21), calls every earlier document a quarry and itself the
foundation (L29), and replaces earlier conceptual PDFs as the canon reference (L1119).
**Recorded, not applied** (decision 006).

## The fourth source of one date

It is dated 2026-05-08, like the character bible, the konsolidiertes Konzept and the
Genesis iteration. Where those disagree it does not side with one of them as a block:
the character bible's three Genesis beats (C12), the other two's Do-er for AEGIS (C8),
the konsolidiertes Konzept's Lia and Isabelle for Flight, marked implicit (C15), and
for Juna neither Kap 33 nor Kap 38 — a revelation in Akt II (C7). **No date orders four sources
of one day**, and none of the four says which of the others it follows.

## One new page, by the document's own rule

`truth-rotation`. The document calls its §II, the Dual-Kernel-Theorie, „literales
Naturgesetz der Romanwelt — keine Metapher" ^[kohaerenz-protokoll-konzept-master-md.md:L37]. Five of the six subsections of §II
define something the wiki already had a page for: the kernels and the DKT, Coheron and
Erason, the Persistenzgleichung, the Landauer heat, Atemporalität. The sixth, „Die
Truth-Rotation — Warum AEGIS = K₀ und Kael = K₁" ^[kohaerenz-protokoll-konzept-master-md.md:L212], had none.

The page opened with this document's reading and gathered the seven read documents
that name it, each commit naming its document. The term stood in all seven of their
censuses, and no reconciliation had made it a page. Here it came to judgement as a
near match (`Truth-Rotation` / `Rotation`), not as a new term: all 248 terms the
lookup called new are listed in `reconcile.json` under `not_promoted`, each with
where its content went.

## Readings — 47 pages

40 the lookup reached, 7 by recorded rules: `genesis` (J78), `erason` (J24),
`atemporalitaet` (J85), and `hitze-polaritaetsregel`, `landauer-signatur`,
`blinder-fleck` and `did`, placed by what the passage states (J62). `ueberwelt` was
looked up and not read: `Simulation` is the city here (L55), and J39 keeps the two
apart. The sweep's one hit, `Genesis` at L998, is a reading, already quoted on the
genesis page.

## What moved

- **C2** — AEGIS as the entropy, in the table the character bible and the
  konsolidiertes Konzept also have, and K₀ as „die Bedingung für Ereignisse überhaupt" ^[kohaerenz-protokoll-konzept-master-md.md:L107],
  the glossary's fourth sense, a month before the glossary.
- **C3** — an origin inside the Genesis with the direction reversed: Kael is left
  over from the separation AEGIS initiates (L464–L465).
- **C7** — „Revelation-Timing: KW2/KW3 (Akt II), nicht früher." ^[kohaerenz-protokoll-konzept-master-md.md:L571] No Kap 33, no
  Kap 38; her other modes of appearance an open point (L994).
- **C11** — heat and ozone as two marks of one displacement: „Somatischer Filter:
  Landauer wird zu Hitze und Ozon, nicht zu Gleichungen." ^[kohaerenz-protokoll-konzept-master-md.md:L1024] Nothing is locked.
- **C12** — three beats, called canonical, a fourth asked and answered no (L469) and
  still open for verification (L998).
- **C8, C14, C15** — Do-er (L809); AEGIS in the third person (L404, L877); Flight
  „implizit Lia/Isabelle" ^[kohaerenz-protokoll-konzept-master-md.md:L1049].
- **C4, C5, C6, C9, C10** — AEGIS' ontological blindness, none for a Guardian (L477);
  KW4 the Möglichkeits-Garten (L661); five Guardians in earlier drafts, two now
  (L504); KW1 the Konstrukt-Stadt, as decided (L658); the knuckles in the premise, in
  no chapter (L51).
- **Q1–Q5** — the Guardians as K₀ sub-operators (L961); twelve protocols once, three
  now (L517); exactly thirteen Alters and four worlds as act markers (L383, L665);
  `Hüterin` for AEGIS and `Wächter` for Mnemosyne (L55, L508); the old Guardians
  absorbed in both, no world for any (L513, L665).

Read and unchanged: C1 (AEGIS is never expanded) and C13 (Köln, Basisrealität and
Externe Ebene do not occur).

## Two names for KW2

It names KW2 `Resonanz-Landschaft` (L331, L659) and gives the `Mnemosyne-Archipel` to
the Vortex, Kap 35–36 (L508). Every other read canon-era source that names KW2 names it
the Archipel; the konsolidiertes Konzept and the drafting manual give it both names and
the climax — „KW2 — Mnemosyne-Archipel (Resonanzlandschaft, Klimax-Setting)" ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L483].
Not a conflict — no source denies what another states — and a question for the author
in `NOW.md`.

## Judgements

J89: a symbol and the name a parenthesis gives it are one term in either order —
`K₁ (Kohärenz-Kernel)` here, `Kohärenz-Kernel (K₁)` on the page. J90 and J91: a
clipped word names what its full form names — `Komp 734` for Komponente 734 (L998,
L465), `Erason-Op` for Oblivion's `Erason-Operator` (L186, L400). Every other near
match was decided by a recorded rule, named in `reconcile.json`.

## The benchmark moved

`graphrag.py bench`: recall@8 with PageRank 0.659 → 0.672, seeds unchanged at 0.466.
Two cases rose, on labels this reading did not change: C4 from 0.556 to 0.667, Q5 from
0.286 to 0.429. No case fell.
