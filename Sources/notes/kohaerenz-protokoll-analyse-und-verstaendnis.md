---
source: Sources/drive/kohaerenz-protokoll-analyse-und-verstaendnis.md
read: "2026-10-12, the whole document (L1 to L301) through read.py with line numbers; by a document-reader subagent (Sonnet)"
stance_markers: ["Vor- und Nachteile", "Mechanismus", "Referenzen"]
stance_marker_count: 6
reads_as: "an analytical report in numbered sections on cache coherence protocols in computer systems, with a reference list; it describes itself as a „Bericht“ with an aim and a conclusion"
---

# Note — Kohärenz Protokoll: Analyse und Verständnis

What this document says about the terms that matter in it. Every quotation carries its file line on the same line of this note; a number about the whole document is a count mark that `quotes.py` checks. Where the note says **observed**, no quotation is possible (a structure, a gap) and the claim rests on the lines or counts it names. The document speaks as an explanatory technical report throughout; it names no figure, place or event of a novel world, and the words below are the report's technical vocabulary.

Stance markers counted: `Vor- und Nachteile` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#2], `Mechanismus` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#3], `Referenzen` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#1].

## 1 · What kind of text this is, and how it marks itself

- The report states its aim in its own words: „Das Ziel dieses Berichts ist es, eine umfassende technische Analyse von Cache-Kohärenzprotokollen zu liefern“ ^[L29]
- It limits its scope to one meaning of the word among several disciplines: „konzentriert sich dieser Bericht auf seine spezifische und kritische Anwendung in Computersystemen“ ^[L25]
- **Observed:** the sections are numbered 1 to 8 with decimal sub-sections (L13 to L244), bullets carry bold labels that repeat under each mechanism (`Mechanismus` and `Vor- und Nachteile`, L77 to L85), and a numbered reference list closes it (L246 to L301). Reference numbers are glued to many sentences by the export.
- It reports its result at the end: „Die Analyse hat gezeigt, dass der Begriff“ ^[L236] `Kohärenz Protokoll` is equivalent to `Cache Coherence Protocol` in computer-science usage.

## 2 · Kohärenz Protokoll

- The report reads the term as a computer-architecture term: it „wird im Deutschen primär im Kontext der Computerarchitektur verwendet“ ^[L17]
- **Observed:** the term is written `Kohärenz Protokoll` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#3] times (L13, L17, L236), always as a quoted name; elsewhere the report writes the compounds `Cache-Kohärenzprotokolle` and `Kohärenzprotokolle`.
- The report defines a protocol in the technical sense: „Ein Protokoll im technischen Sinne ist eine formale Sammlung von Regeln, Prozeduren und Datenformaten“ ^[L57]

## 3 · Cache-Kohärenz and its problem

- The problem named is data inconsistency, with a heading of its own: „Das fundamentale Problem“ ^[L19]
- The report gives it a role: „sondern eine grundlegende Technologie“ ^[L29]
- It limits what coherence guarantees: „Cache-Kohärenz ist eine notwendige, aber nicht hinreichende Bedingung für Speicherkonsistenz“ ^[L184]
- It names the importance for real-time systems: `Echtzeitsystemen` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#1] appears once, in section 2.3 (L51).

## 4 · Other disciplines' senses of Kohärenz

- Signal processing: „ein statistisches Maß, das die lineare Korrelation“ ^[L41] between two signals is quantified.
- Physics: the report distinguishes „Man unterscheidet zwischen zeitlicher Kohärenz“ ^[L35] and spatial coherence.
- Quantum mechanics: „Quantenkohärenz ist jedoch fragil“ ^[L37]; loss of it is called `Dekohärenz`.
- **Observed:** the report brings these senses in only to separate them from its subject (L25).

## 5 · The two mechanisms

- Snooping: „überwacht („snoopt“) jeder Cache-Controller“ ^[L77] the bus.
- Directory: protocols use „eine zentrale oder verteilte Datenstruktur“ ^[L83]
- Snooping's drawback in its words: „Ihr Hauptnachteil ist die begrenzte Skalierbarkeit“ ^[L79]
- Directory's advantage and drawback: „Der Hauptvorteil ist die Skalierbarkeit“ ^[L85] and „Ein potenzieller Nachteil ist die höhere Latenz“ ^[L85]
- Mixed forms: „Die strikte Trennung zwischen Snooping und Directory weicht in modernen Systemen zunehmend auf“ ^[L87]

## 6 · The MESI family and named protocols

- MESI is introduced as „Das MESI-Protokoll (Modified, Exclusive, Shared, Invalid) ist ein fundamentales“ ^[L99] state-based invalidation protocol.
- The four states are bold labels `Modified (M)`, `Exclusive (E)`, `Shared (S)`, `Invalid (I)` (L104 to L107).
- Variants: MSI is „Eine vereinfachte Version ohne den Exclusive-Zustand“ ^[L156]
- A transition table is announced at L120: „Die folgende Tabelle fasst die wichtigsten Zustandsübergänge im MESI-Protokoll zusammen“ ^[L120]
- Named protocols: `Token Coherence` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#3] is described as „Entkoppelt Korrektheitsmechanismen“ ^[L165] from performance optimisations; `RCP` is described as „Erweitert bestehende Kohärenzprotokolle“ ^[L172] with speculative states.
- The general view of the list: „Die Vielfalt der Kohärenzprotokolle geht weit über die MESI-Familie hinaus“ ^[L163]

## 7 · Relations to other concepts

- Synchronisation depends on coherence: „Synchronisationsprimitive sind auf die zugrundeliegende Cache-Kohärenz angewiesen“ ^[L190]
- Trend in optimisation: „Der Trend geht zu Protokollen“ ^[L208] specialised for access patterns.
- Security reaction: „Als Reaktion darauf werden neue Kohärenzprotokolle wie RCP“ ^[L219] developed.

## 8 · Said two ways, or left open — recorded, not resolved

- The report's closing remarks call coherence a continuing central technology: „Cache-Kohärenz bleibt eine zentrale und kritische Technologie“ ^[L244]
- It says no single solution exists: „Cache-Kohärenz kein abgeschlossenes Problem mit einer einzigen Universallösung ist“ ^[L176]
- **Observed:** section 5.2 calls MESI a `fundamentales` protocol (L99) and section 5.3 lists MSI as inefficient for some data (L156); these are sections' statements, not a conflict.

## 9 · Absent, counted

- **Observed:** the document names no chapter, figure or story element of a novel: `Roman` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#0], `Figur` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#0], `Kap` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#0]. `Kapitel` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#1] stands once, in the title of a reference (L289).
- **Observed:** the report makes no claim of canon or authority for itself; its own standing is an analysis with an aim (L29) and a result (L236).
