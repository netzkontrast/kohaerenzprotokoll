# Brief — readings from koharenz-protokoll-kapitel-0-v2-md on existing pages

Document 25: `Sources/drive/koharenz-protokoll-kapitel-0-v2-md.md`, dated 2026-05-17 by the
manifest. A narrative text of Kap 0 — **research, by the author (2026-09-26), not text for
the novel** — with no annotation, no rule frame, and **no named figure**: it never writes
AEGIS, Kael, Juna, 734 or any alter (counted: `Plan/runs/koharenz-protokoll-kapitel-0-v2-md/05-verify.txt`).
Read its note first: `Sources/notes/koharenz-protokoll-kapitel-0-v2-md.md` (the registers:
the Wir of the Vorwort/Dazwischen; the fragment's present-tense Ich; the past-tense third
person about „das System" with status blocks; short lines with no speaker).

## What to do, per page you are given

1. Read the whole page, and read the document's passages that concern it
   (`python3 scripts/read.py koharenz-protokoll-kapitel-0-v2-md --from N --to M`).
2. Add one section, placed after the page's last `## Reading — …` section and before any
   `## Where the sources differ` / `## Open` / `## Occurrences only` that follows it
   (if the page interleaves, put it after the `kap0-v1-annotiert-md` reading):
   `## Reading — \`koharenz-protokoll-kapitel-0-v2-md\`, 2026-05-17, a narrative text of Kap 0 — <what it adds, a few words>`
3. English prose around German quotations. Every quotation is verbatim, in „…", followed by
   `^[koharenz-protokoll-kapitel-0-v2-md.md:Lnn]` — the qualified form, always. **Get every
   line number from** `python3 scripts/read.py koharenz-protokoll-kapitel-0-v2-md --find "<the exact words>"`;
   never type one. Never translate. Never merge two statements.
4. Say which register a quotation is from where it matters (the system's status block, the
   fragment's Ich, the Wir, a line with no speaker). **Never name a figure the document does
   not name**: write „the system", „the fragment", „the Entität", „a line with no speaker",
   and where the page's subject is a named figure, say that this document does not name it.
   What the document *does not* say is stated only with the count from `05-verify.txt`.
5. Frontmatter: append `"koharenz-protokoll-kapitel-0-v2-md"` to `ingested:`, add 1 to
   `sources:` and to `readings:`.
6. Compare with the page's other readings **only to keep the page true**: if the lead or
   `## Where the sources differ` makes a claim this document now falsifies („only X", „every
   source", „the Kap-0 draft is the only…"), correct the claim and say which source moved it.
   Where it simply agrees or differs, add one line to `## Where the sources differ` if the
   page has that section and the difference is real. Never resolve a difference.
   The author, 2026-09-26: documents 22 and 23 and this one are research, not text for the
   novel. If a line you are touching calls one of them „the novel's text", fix that too; do
   not rewrite other „draft" wording (a document may call itself a draft).
7. Run `python3 scripts/quotes.py Wiki/candidates/<page>.md` and fix until 0 unresolved and
   0 unchecked, then `python3 scripts/relations.py >/dev/null` (a `[[link]]` must point at a page).
8. **Do not commit, do not touch any file other than your pages.** Report per page: the
   heading you added, the lines cited, and any lead/differ claim you changed and why.

## Passages, by line (orientation; read them yourself)

Vorwort L17–51 (Wir, to the reader: *Nichts*, Parmenides/Vakuum/Śūnyatā set aside L27–31,
„wir seien dieser Funke" L39, repetition L47). Das Rauschen L57–63. Herz der Leere L69–87
(cold L83; echoes, resonances L87). Erste Kontakte L93–135 (the Klicken L95, warmth L99,
loss L107–115, triad and cluster L119, cold systemic logic L135). Sog der Ordnung L141–159
(Sog L143, Selbstverstärkung L147, prediction in an analytic register L151–155).
Überlebenskampf L165–187 (Triade Sieben L171, Strukturoptimierung L179, kalte Schicht L183).
Der große Wandel L193–263 (Klick L199, fallendes Glas L203, the formula L211 in the third
person neuter: „*Es ist, was es verhindert, dass es nicht ist.*", Grenze = System L223,
Phantomgefühl L231, Komponente/Funktionseinheit with a withheld number L235, irrelevante
Varianz L239, inner simulation / Labor nach innen / Binnen-Physik / „Werkzeug, das Welten
simuliert" L251–259, L263). Dazwischen L269–287 (Wir; the question of feeling L279).
Die Stille Wacht L293–327 (status block L295–307, Substrat/Potentialmeer/Nichts-Rauschen L311,
Identität durch Negation L315, Residual-Echos with Persistenz-Score 0.41 L319).
Perturbation aus der Leere L333–375 (Emergenz aus dem Potentialmeer L335, status L339–363,
Entität and ontologischer Druck L371). Algorithmischer Schrecken L381–463 (Residual-Echos
L383, RESIDUAL\_BAND L391–399, H1–H4 with H4 \[DATENTYP\_FEHLT\] L407–423, Paradoxon der
Fehlausgerichteten Kohärenz and no Qualia L427, a line with no speaker L431, „liefen heiß"
L435, KOH\_1.0 and „Residual-Träger isolieren" L447–451). Resonanzkaskade L469–511 (the
Ich inside the system; cold L479–483; „fremd und doch nicht fremd" L503; warm contradicted
L507). Systemischer Kollaps L517–555 (KOHÄRENZ 0.21, the Kohärenz Protokoll decided L555).
Trennungsprotokoll L561–627 (status L563–579, operational view L583–595, Sektor 4–6 leer
L595, the one cut L599–611, knuckles in a line with no speaker L607 „Die Luft ist heiß.
Knöchel — gibt es keine. Aber sie bluten.", shards L627). Coda after the last rule L635–639
(„Zweitausenddreihundertvier Kacheln. Einundzwanzig Grad." … „Ich bin pünktlich.") — no name.
