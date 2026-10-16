---
source: Sources/drive/codex-optimierung-fuer-kohaerenz-protokoll.md
read: "2026-10-12, the whole document (L1 to L583) through read.py with line numbers; by a document-reader subagent (Sonnet)"
stance_markers: ["Fazit der Bewertung", "Hypothetisch gezogene Codex-Daten", "Erwarteter Output-Fokus", "Annahme", "Empfehlungen"]
stance_marker_count: 11
reads_as: "a research report that assesses a writing tool's codex, proposes field names and a master prompt, and demonstrates them on two hypothetical scene beats"
---

# Note — Codex-Optimierung für das Kohärenz Protokoll ^[L11]

What this document says about the terms that matter in it. Every quotation carries its file line on the same line of this note; a number about the whole document is a count mark that `quotes.py` checks. Where the note says **observed**, no quotation is possible (a structure, a gap) and the claim rests on the lines or counts it names. The document is a design report about tooling, and the novel's world appears in it as material for examples; the five stance labels together stand 11 times (`Fazit der Bewertung` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#1], `Hypothetisch gezogene Codex-Daten` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#2], `Erwarteter Output-Fokus` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#2], `Annahme` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#3], `Empfehlungen` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#3]).

## 1 · What kind of text this is, and how it marks itself

- The report names its task as a commission: „Dieser Bericht adressiert den Forschungsauftrag“ ^[L15].
- It judges the existing templates cautiously: „Die Vorlagen decken vermutlich viele der identifizierten Elemente ab“ ^[L76].
- Its closing verdict on that assessment is hedged too: „Fazit der Bewertung“ ^[L81] opens a sentence calling the templates a base that is probably not optimal.
- Its field names are offered as a proposal: „werden folgende spezifische Custom Details für die relevanten Codex-Eintragstypen vorgeschlagen“ ^[L123].
- The two scenes are declared invented: „anhand von zwei hypothetischen Szenen-Beats“ ^[L316].
- Codex values inside the scenes are labelled as hypothetical: „Hypothetisch gezogene Codex-Daten“ ^[L333].
- Each scene ends in a prediction, not a text: „Erwarteter Output-Fokus“ ^[L407].
- The final advice is addressed as recommendations: „Empfehlungen für die Codex-Optimierung“ ^[L531].
- An appendix is offered only on request: „Bei Bedarf“ ^[L559].
- **Observed:** the table rows hold sample values (the column is headed „Beschreibung & Beispiel“ ^[L131]); the values are examples of what an entry may contain. The document marks no passage as a lock or as canon.

## 2 · Kael and the Anteile

- The document introduces the novel's protagonist as a „Protagonisten mit dissoziativer Identitätsstruktur“ ^[L15], and the same sentence calls the structure „TSDP-basiert“ ^[L15].
- The character level is justified by the „subjektiven Wahrnehmung des Protagonisten Kael“ ^[L26].
- A point-of-view part is identified by „Name und spezifische Rolle im TSDP-System“ ^[L30], with the two roles spelled out in the same line as `Anscheinend Normale Persönlichkeit` and `Emotionale Persönlichkeit` ^[L30].
- The Codex is to hold a parent entry that „verweist auf alle individuellen Anteils-Einträge“ ^[L94]; the parent is named `Kael System` there.
- The field `Anteil_TSDP_Role` is described as „TSDP-Klassifikation und Kernfunktion“ ^[L132].
- Example scene one names a part: „Kael (Anteil 'Der Wächter', ANP) untersucht einen 'Riss' in Kernwelt Co₁“ ^[L318].
- Example scene two names another: „Kael (Anteil 'Das Kind', EP) interagiert mit AEGIS in Kernwelt B“ ^[L409].
- Both scenes sit under the hypothetical labels of section 1, so these part names are the examples' own.

## 3 · AEGIS

- The conceptual level lists „das KI-System AEGIS“ ^[L50] among the concepts a scene may have to show.
- For the case that the theme `Kontrolle` is explored, the document lists as a possibility „AEGIS' manipulative Eingriffe“ ^[L63].
- The presence of the system is said to shape the scene: „Die Präsenz von AEGIS“ ^[L62] is listed as influencing action and atmosphere.
- In the field tables, a sample value for a concept entry is „KI-System mit widersprüchlichen Kernregeln“ ^[L145], and a sample manifestation is „AEGIS gibt widersprüchliche Befehle“ ^[L147].
- In the second scene's hypothetical codex data, the entry reads „Antagonistische Kontroll-KI mit internem Widerspruch“ ^[L444].
- A sample relation value for a part toward the system is „AEGIS: Misstrauen, Furcht“ ^[L139].
- The predicted output of the second scene says the system's replies „könnten kryptisch sein“ ^[L515].

## 4 · Juna

- Juna is named once in running text, among the figures who influence a scene: „externe Figuren wie Juna“ ^[L38].
- A sample relation value reads „Juna: Hoffnung, Verwirrung“ ^[L139]; it is a sample entry of the field `Anteil_Beziehung_Andere`.
- **Observed:** `Juna` stands 3 times in the document (`Juna` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#3]): L38, L112 (a table cell naming Juna as a character entry) and L139. No passage describes Juna further.

## 5 · The worlds, Riss and Paradoxon X

- The world level asks for the current world by name, with four examples: „Name (z.B. Co₁, McL, B, Ly)“ ^[L43]. No world is described beyond the sample values.
- Sample world metaphors given for the field `Welt_Core_Concept` include „Logisches Kristallgefängnis“ ^[L140] and „Chaotischer Emotionsraum“ ^[L140].
- Example scene one gives a hypothetical aesthetic for `Co₁`: „Kristallin, Geometrisch, Kalt, Ordentlich“ ^[L352].
- Example scene two gives rules for `Kernwelt B`: „Instabil, von Emotionen beeinflusst“ ^[L455].
- Anomalies are raised as a question to ask of a world: „Gibt es Anomalien wie“ ^[L46] the `Risse`.
- A `Riss` is said to act on a character: „kann Angst triggern“ ^[L59].
- Its hypothetical codex definition reads „Instabilität in der simulierten Realität“ ^[L362].
- `Paradoxon X` is named next to the TSDP dynamics as a concept to be shown through events: „Abstrakte Konzepte wie Paradoxon X oder TSDP-Dynamiken“ ^[L62].
- The keywords the examples give it are hypothetical: „Widerspruch, Systemfehler, Unlösbare Aufgabe“ ^[L464].
- The count of the entry name is `Paradoxon X` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#21].

## 6 · The report's own principles

- The design is introduced as principles: „Die folgenden Prinzipien leiten den Entwurf“ ^[L85].
- The first principle is „Informationen werden so prägnant wie möglich erfasst“ ^[L87].
- A priority scheme is named in the document's own terms: „Minimal Sufficiency“ ^[L276].
- For continuity, „Nur ein kurzer Ausschnitt der direkt vorangehenden Szene“ ^[L272] is loaded optionally.
- The themes used in the two scenes are „Realität vs. Illusion“ ^[L327] and „Kontrolle vs. Freiheit“ ^[L418].

## 7 · Said two ways, or left open — recorded, not resolved

- The part names `Der Wächter` and `Das Kind` occur only in the two examples marked hypothetical; `Der Wächter` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#4], `Das Kind` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#6].
- The narrative level lists patterns without defining them: „Heldinnenreise, Zyklen, Heldenreise“ ^[L25].
- **Observed:** `Fundament` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#1], `Cache Kohärenz` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#1], `Switching` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#1] and `Co-Präsenz` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#1] each stand once, in the list of L50, and nothing explains them.
- **Observed:** the abbreviation `TSDP` is never expanded; the lines that name `TSDP-System` (L30), `TSDP-basiert` (L15), `TSDP-Dynamiken` (L50, L62) and `TSDP-Rolle` (L284) use it as known.
- **Observed:** `McL` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#1] and `Ly` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#1] stand only in the list of world names at L43.

## 8 · Absent, counted

- **Observed:** the document names no chapter by number; `Kap` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#0] alone stands 0 times, and `Kapitel` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#1] stands once, at L25, as a level of the story's structure in general.
- **Observed:** no passage of the report states what happens in the novel; every event the report writes stands in the two hypothetical examples (L318 to L407, L409 to L515).
