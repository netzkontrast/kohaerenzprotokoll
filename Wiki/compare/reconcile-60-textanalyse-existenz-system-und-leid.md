---
document: textanalyse-existenz-system-und-leid
against: 106 pages, 15 conflicts
ran: "2026-10-05"
candidates: 232
decisions: 241
by_lookup: 136
judgements: 105
new_pages: 0
new_readings: 10
---

# Reconciliation 60 — `textanalyse-existenz-system-und-leid` against the wiki

`python3 scripts/reconcile.py textanalyse-existenz-system-und-leid`

232 candidates, 241 decisions — **136 by lookup, 105 to judgement**. Dated 2025-11-18 by the manifest: a commentary in German on a narrative it names „Genesis der Existenz“ ^[textanalyse-existenz-system-und-leid.md:L22], which it reads as „eine rigorose Allegorie der Systemwerdung“ ^[textanalyse-existenz-system-und-leid.md:L22] through systems theory and existential philosophy, with a synopsis table and 39 references. It quotes the narrative in short phrases each closed by a glued reference number 1, speaks once in the commentator's first person (L222) and claims no canon. It never names Kael, Juna or a chapter.

It is the first document read on the author's go of 2026-10-05 and one of step 6's sample. Its census and note were written by a Sonnet `document-reader` from the R5 setup (the card, `census.py draft`, `claims.py`, `quotes.py --strict`); the session's review corrected three claims, each of one kind — a name the narrative gives, quoted with its reference mark, written as the commentary's own (`Komponente 734` L162, „ontologische Anomalie“ ^[textanalyse-existenz-system-und-leid.md:L206]; `corrections.jsonl`). Its readings were written by one Sonnet `wiki-reader` from `Plan/runs/ingest-60/brief.md` and placed by `readings.py apply` with every check held; each page went in as its own commit naming the document.

## No new page

The document is a commentary through Luhmann, Lacan, Sartre, Heidegger, Baudrillard and Foucault: most of its candidates are borrowed concepts (operationale Geschlossenheit, Re-entry, Dasein, das Reale, Biopolitik) or the narrative's words for steps the wiki already pages (closure, Komponente 734, Überwelt, the protocol). The narrative's own new names — Der große Wandel, Resonanzkaskade, ontologische Anomalie, Sharding, Paradoxon der Fehlausgerichteten Kohärenz — stand in one commentary on one narrative; their readings went on genesis, komponente-734, aegis, kohaerenz and trennungsprotokoll, and none is opened as a page from a single quoted occurrence.

## Judgements

No new judgement. Every near match the lookup handed on was decided by an existing rule (`Plan/runs/judgements.md`): J5 (a negation prefix makes a new term: Kohärenz / Inkohärenz, Sein / Nicht-Sein, svabhava / asvabhava), J9 (a title containing a term: Strukturierte Synopse der Kernkonzepte; Genesis der Existenz), J12 and J16 (a compound is its own token: Rauschen / Umwelt-Rauschen, Resonanz / Resonanzkaskade, Cluster / Clusterbildung), J14 and J34 (a slash is an alias or a role: Das Nichts / Rauschen, Schmerz/Warnung, Kohärenz/Inkohärenz), J24 and J97 (a plural or case ending is no boundary: Fragment / Fragmente, binären Code / binäre Code, Ontologischen Reibung), J28 and J32 (a compound is placed by what it names: Paradoxon der Fehlausgerichteten Kohärenz, Herrschaft des Codes, Einsamkeit des Codes), J42 (a set is not its largest subset: Erhalte Kohärenz / Vermeide Nicht-Sein), J57 (a compound naming a protocol is not the property it is named for: Kohärenz Protokoll 1.0 / Kohärenz), J59 (a compound naming an entity is not the thing it contains: Kybernetisierung des Zeus-Schildes / Zeus; AEGIS Combat System / AEGIS), J69 (a match that exists only after folding: Nagarjuna / juna, Sein / evaluierungseinheit, Bewusstsein / personas), J72 (a parenthetical index is part of the label: Rauschen (Noise), Bewusstsein (psychisches System), Außenwelt (Leere)), J83 (a head used alone for the compound's content: Komponente / Komponente 734), J88 (a common noun for a page's referent is placed by the sentence: Fragment, Entität, Resonanz, Grenze), J114 (a protocol a source describes doing what a page's protocol does is placed on that page by the sentence: Kohärenz Protokoll 1.0 → trennungsprotokoll).

## Readings — 10 pages

`aegis`, `entropie`, `genesis`, `kohaerenz`, `komponente-734`, `negentropie`, `nichts-rauschen`, `residual-echos`, `trennungsprotokoll`, `ueberwelt`.

No chapter page.
`plot.md` cites it nowhere.
Conflicts with an entry from it: C12. Questions: none.

## Sweep

`Alex` L332 occurrence — Alex Reid, the author of a cited blog post in the reference list; not the novel's figure; `Emergenz` L22 occurrence — „der Emergenz von Ordnung“ ^[textanalyse-existenz-system-und-leid.md:L22] names one of the questions the commentary will ask, once, in its opening sentence; the document says nothing further under that word; `Genesis` L13 reading — the title names the narrative „Genesis der Existenz“ ^[textanalyse-existenz-system-und-leid.md:L13] the commentary retells — closure, Komponente 734, the Überwelt, the Entität, the Kohärenz Protokoll 1.0 — which is the page's subject, the ontological birth; read by the sentence, not by the title (J9).

## What the readers noticed and no record holds

The narrative's order fixes what C12 asks without counting beats: closure (L90–L92) makes the Ich-Fragment Komponente 734 (L162), and the protocol comes after the Entität and the Resonanzkaskade (L218–L244) — the component before the protocol, as in the record's four-beat order. The document names only the `Kohärenz Protokoll 1.0`, never the `Trennungsprotokoll`; other read sources say the Trennungsprotokoll initiates it, and its reading on `trennungsprotokoll` says so without equating them (J114).

The narrative itself is landed and unread: the commentary's first reference is „Einleitung: Genesis der Existenz“ ^[textanalyse-existenz-system-und-leid.md:L314], and the manifest holds `einleitung-genesis-der-existenz` and three plotlines of the same name. A question for the author goes to `Plan/questions-for-the-author.md`: whether that narrative, dated before the canon era, is an earlier Kap 0.

C2 (Entropie's senses): the document's entropy is the commentary's information-theoretic lens, with no position on the novel's sense — no entry. Q7 (what 734 names): the document says what the component is, never what the number labels — no entry.
