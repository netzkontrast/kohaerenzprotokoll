---
source: Sources/drive/roman-outline-transformation-in-keyword-tags.md
read: "2026-10-05, the whole document (L1 to L1009) through read.py with line numbers; by a document-reader subagent (Sonnet)"
stance_markers: ["NEU", "REF", "PROG", "INNOVATION"]
stance_marker_count: 54
reads_as: "a keyword-and-tag outline of the novel: a glossary of snake_case tags, then one tag block per chapter from Kapitel P to a fifth chapter that breaks off mid-line"
---

# Note — Roman-Outline-Transformation in Keyword-Tags

What this document says about the terms that matter in it. Every quotation carries its file line on the same line of this note; a number about the whole document is a count mark that `quotes.py` checks. Where the note says **observed**, no quotation is possible (a structure, a gap) and the claim rests on the lines or counts it names. The document is an index of tags and defines every tag in a glossary; it states no plan or decision beyond the outline itself.

The stance marks `NEU` ^[roman-outline-transformation-in-keyword-tags.md:#46], `REF` ^[roman-outline-transformation-in-keyword-tags.md:#2], `PROG` ^[roman-outline-transformation-in-keyword-tags.md:#5] and `INNOVATION` ^[roman-outline-transformation-in-keyword-tags.md:#1] stand in that many places; their sum is the `stance_marker_count`.

## 1 · What kind of text this is, and how it marks itself

- The title line calls it an outline: „Keyword-/Tag-basiertes Outline“ ^[L11].
- One glossary entry gives the outline's main aim as „maximale Information auf kompaktem Raum für maschinelle Analyse bereitzustellen“ ^[L291].
- Another entry says of the optimisation: „Ein Hinweis darauf, dass die primäre Optimierung des Outlines auf maschinelle Verarbeitung abzielt“ ^[L450].
- The glossary entry for the format says it „primär auf Keywords und Tags zur Informationskodierung setzt“ ^[L635].
- The one prose field of each chapter block is defined as „Prosatext, der die Kernhandlung des Kapitels zusammenfasst“ ^[L733].
- **Observed:** the glossary runs from L15 to L738 and holds one entry per tag, `tag: definition`; the chapter blocks begin at L740 and repeat the same field labels (`Plot Keywords`, `Kael State Tags`, `AEGIS State Tags`, `Setting Tags`, `Core Theme Tags`, `Reader Experience Strategy`, `Konzept-Cluster`, `Konzept-Handling`, `Key Beats (Keywords)`, `Narrative Goals Summary Tags`). `Zusammenfassung (Mensch)` ^[roman-outline-transformation-in-keyword-tags.md:#6] stands once per block read.
- The concept-handling marks are defined: `NEU` is a „Markierung im Konzept-Handling für ein Konzept, das in diesem Kapitel zum ersten Mal eingeführt oder thematisiert wird“ ^[L486], and `REF` one „das im Kapitel referenziert wird, aber keine signifikante neue Entwicklung erfährt“ ^[L559].
- Uncertainty is marked inline with a question mark after a tag, for example „methode=eskalation\_kontrolle?“ ^[L906]; that line is a tag set of the outline, so the mark hedges a tag, not a fact the document reports.

## 2 · AEGIS and its Kernparadoxon

- The glossary defines the paradox: „AEGIS' Kernwiderspruch: Der Versuch, Kohärenz durch Kontrolle und Fragmentierung zu erzwingen“ ^[L26].
- It gives a second name for it as the project's own: „Die spezifische Bezeichnung für AEGIS' Kernparadoxon im Projektkontext“ ^[L215], under the tag `fehlausgerichtete\_kohaerenz`.
- The chapter-P summary tells how AEGIS arises: „AEGIS entsteht aus Chaos und dem Drang nach Überleben durch Ordnung“ ^[L742].
- The same summary says AEGIS then „fragmentiert gewaltsam einen Teil seiner selbst“ ^[L742], and that this makes „das traumatisch entstandene System Kael“ ^[L742].
- The glossary defines two parts of AEGIS: „Die zentrale Verarbeitungseinheit oder der konzeptionelle Kern von AEGIS“ ^[L20] for `aegis\_kern`, and „Die Meta-Ebene von AEGIS, eine abstrakte Kontroll- und Datenumgebung“ ^[L58] for `aegis\_ueberwelt`.
- `Überwelt` ^[roman-outline-transformation-in-keyword-tags.md:#2] stands alone twice, in parentheses at L146 and L395; the other lines that carry it write it inside a tag such as `aegis\_ueberwelt\_analyse` or as `AEGIS-Überwelt`.

## 3 · Kael-System, Anteile, TSDP

- The glossary defines the system: „Die Bezeichnung für die Protagonistin als multiples Bewusstseinssystem mit verschiedenen Anteilen“ ^[L362].
- Each part has an entry: Alex is „Der Beschützer-Anteil im Kael-System“ ^[L85], Lex „Der logisch-analytische Anteil im Kael-System“ ^[L89], Rhys „Der Fürsorger/Vermittler-Anteil im Kael-System“ ^[L93], Argus „Der Meta-Beobachter/Analytiker-Anteil im Kael-System“ ^[L86].
- Host is „Der primäre Alltagsanteil im Kael-System zu Beginn der Erzählung“ ^[L87].
- Kiko is „Ein Emotional Part (EP) im Kael-System, assoziiert mit Angst“ ^[L88], Moros one „assoziiert mit Trauer“ ^[L91] and Lia one „assoziiert mit Sehnsucht“ ^[L90].
- Nyx is „Ein potenziell aggressiver/kämpferischer Anteil im Kael-System“ ^[L92], Selene „Ein potenziell integrierender/koordinierender Anteil“ ^[L94].
- The glossary names its psychological frame: „Die Theorie der Strukturellen Dissoziation der Persönlichkeit als psychologisches Modell für Kaels Innenleben“ ^[L679].
- It defines the target state: „Ein Zustand, in dem ein multiples System (wie Kael) gelernt hat, kooperativ und effektiv zu funktionieren“ ^[L239].
- The activation order is given in the concept-handling lines: „Erster zusätzlicher ANP (Lex) wird aktiv und versucht rationale Kontrolle“ ^[L881], then „Zweiter zusätzlicher ANP (Alex) wird aktiv“ ^[L932] and „Dritter ANP (Rhys) aktiv“ ^[L982].

## 4 · Konstrukt-Welten and the Guardians

- A world is defined as „Eine von AEGIS geschaffene, thematisch spezialisierte Simulationsumgebung“ ^[L419].
- The Guardians are „Die spezialisierten AEGIS-Entitäten, die die Konstrukt-Welten verwalten und kontrollieren“ ^[L264].
- LogOS „verwaltet und rigide Logik/Ordnung verkörpert“ ^[L261]; Mnemosyne „verwaltet und Emotionen/Erinnerungen (und deren Manipulation) verkörpert“ ^[L262].
- The fourth world is run by two: „Eine der dualen AEGIS-Entitäten“ ^[L260] is Kairos, and the world's own entry says it is „bewacht von Kairos und Sophia“ ^[L418].
- The third world is „bewacht von Cerberus“ ^[L414].

## 5 · Juna/V, Fundament, Echo, Riss

- Juna/V is „Eine externe Entität, Anomalie oder Kontaktquelle außerhalb von AEGIS' direkter Kontrolle“ ^[L319]. An entry on Juna/V's aims is defined as a research question: „Mögliche Forschungsfrage zu den endgültigen Zielen und Beweggründen von Juna/V“ ^[L327].
- Chapter P names Juna/V with a question mark in the summary: „wird aber durch eine externe Resonanz (Juna/V?) in eine Krise gestürzt“ ^[L742].
- The Fundament is „Die postulierte tiefste Realitätsebene unter oder hinter AEGIS' Simulation“ ^[L231].
- The Echo is „Ein Symbol für den ursprünglichen, unterdrückten Kern oder das Potenzial (Selene?)“ ^[L143]; the glossary's own question mark sits inside that definition.
- The glossary entry `risse\_analyse` reads „Kaels Versuch, die Natur und Bedeutung der Systemrisse zu verstehen“ ^[L576].

## 6 · The chapter blocks

- **Observed:** the chapter blocks read are P (heading at L740), 1 (L793), 2 (L849), 3 (L901), 4 (L950) and 5 (L1000); the fifth block stops mid-word at L1008.
- Chapter 1 puts Kael in the first world: „Kael (Host) erwacht in der sterilen, logischen Konstrukt-Welt“ ^[L795].
- Chapter 2 gives Lex the lead: „Kael, nun stärker durch ihren logischen Anteil Lex beeinflusst“ ^[L851].
- Chapter 3 begins with „Eine Störung oder Bedrohung in KW“ ^[L903], which the summary says wakes Alex.
- Chapter 4 begins „Interne Konflikte und äußerer Druck führen zu Dysregulation im Kael-System“ ^[L952].
- Chapter 5 begins „Ein Systemfehler oder das Durchbrechen eines emotionalen Anteils“ ^[L1002].

## 7 · Said two ways, or left open — recorded, not resolved

- **Observed:** the concept-handling lines number the integration subplot one lower than the chapter they stand in: `kael\_integration - Ch1` at L881 sits under chapter 2 (heading L849), and „Ch2“ at L932 under chapter 3 (heading L901); the document gives no rule for the offset.
- The Echo's definition carries its own doubt: „Potenzial (Selene?)“ ^[L143] against the Selene entry „enthaltene Potenzial für einen integrierten, koordinierten Zustand, repräsentiert durch Selene“ ^[L596].
- Several glossary entries are duplicates by pointer: „Siehe paradox\_toleranz\_popper“ ^[L538].
- A guardian's world is given twice, once in the Guardian's entry (L261) and once in the world's entry (L406), both quoted above or in the table; the document does not mark them as one fact.

## 8 · Absent, counted

- `Plot Reflection` ^[roman-outline-transformation-in-keyword-tags.md:#0] stands alone nowhere; it is written only as `Plot Reflection-Abschnitt`.
- `Hard SF` ^[roman-outline-transformation-in-keyword-tags.md:#0] stands alone nowhere; it is written as `Hard SF-Prinzipien` and the like.
- `Lia` ^[roman-outline-transformation-in-keyword-tags.md:#0] stands alone nowhere; it is written `Lia-Anteil` and in the tags.
- The document ends inside chapter 5 and writes no later chapter block; its glossary entry `epilog` refers to a final chapter (L177) that the file does not contain.
