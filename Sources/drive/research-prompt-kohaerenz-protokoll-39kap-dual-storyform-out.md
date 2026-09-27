---
drive_id: "1WatAbHnlO_wbW8oLdWzM6S6OOjvW7Sh15WuM4d0JyfA"
title: "research-prompt_kohaerenz-protokoll-39kap-dual-storyform-outline.md"
slug: "research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out"
category: "storyform"
tier: "T3-work"
index_date: "2026-04-30"
fetched: "2026-09-26"
---

-----



topic: "Kohärenz Protokoll — 39-Kapitel-Outline mit Dual-Storyform-Encoding" slug: "kohaerenz-protokoll-39kap-dual-storyform-outline" research\_category: "B" research\_category\_label: "Extraction" critical\_thinking\_methods:



  - "Source Triangulation"
  - "Contradiction Log"
  - "What Would Change My Mind"
  - "Adversarial Query Expansion" prompt\_engineering\_framework\_agentic\_spine: "ReAct" prompt\_engineering\_framework\_structural: "RISEN" cross\_pollination:
  - source\_category: "A" step\_id: "i.a" description: "Hidden-Items / Schema-Gap Sanity Pass"
  - source\_category: "C" step\_id: "i.c" description: "Kanon-Drift-Check (adaptiert aus World-Change Check)" constraint\_blocks:
  - "0 — Reflection Baseline"
  - "1 — Quellen-Priorität (Kanon-Trio absolut, Legacy nachrangig)"
  - "2 — Kanon-Snapshot-Datum (2026-04-30)"
  - "3 — Output-Exclusions"
  - "4 — Storyform-Vorgaben (verbindlich)"
  - "5 — Output-Schema (verbindlich)" language: "de" target\_agent: "model-agnostic (optimiert für Gemini Deep Research mit NotebookLM- und Google-Drive-Anbindung)" created: "2026-04-30" version: "1.0" source\_skill: "research-prompt-optimizer v2.1.0"



-----

# Research Prompt: Kohärenz Protokoll — 39-Kapitel-Outline mit Dual-Storyform-Encoding

**An die ausführende KI:** Dieser Prompt ist vollständig in sich geschlossen. Jede Methode, jedes Framework und jede Restriktion, die du brauchst, ist hier inline definiert. Du brauchst keinen externen Kontext, kein spezifisches Vortraining auf bestimmte Methoden und kein Wissen über das Skill, das diesen Prompt erzeugt hat. Lies den gesamten Prompt durch, bevor du beginnst.



-----

## Meta-Header — Was dieser Prompt ist und wie er zu lesen ist

Dieser Prompt kombiniert drei unabhängige Schichten:

### 1\. Epistemologische Schicht — Forschungs-Kategorie B (Extraction)

Diese Recherche ist eine **Extraktion**, keine Exploration. Die Antwort existiert bereits in den dir übergebenen Quellen (drei Kanon-Dokumente plus die vom Auftraggeber freigeschalteten Drive- und NotebookLM-Quellen); deine Aufgabe ist es, sie zu lokalisieren, zu verifizieren und in einer festgelegten Struktur zu präsentieren. Du generierst keine neuen Hypothesen.



**Was das für deine Ausführung bedeutet:**



1.  **Folge dem Plan exakt.** Der Steps-Abschnitt unten spezifiziert eine geordnete Prozedur. Führe sie End-to-End aus. Improvisiere keine alternativen Strategien. Wenn der Plan unausführbar wird, halte an und melde die Blockade — substituiere niemals stillschweigend.



1.  **Fülle jedes Feld des Output-Schemas oder markiere es als fehlend.** Das Output-Schema ist gelockt (siehe Constraint Block 5). Jedes Feld bekommt entweder evidenz-gestützten Inhalt oder explizit \[nicht gefunden — Begründung\]. Erfinde nichts, um Lücken zu füllen.



1.  **Quellen-Triangulation ist Pflicht** für Legacy-Funde aus Drive/NotebookLM. Für Kanon-Aussagen aus den drei übergebenen Kerndokumenten gelten diese als Primärquelle und benötigen keine zusätzliche Triangulation.



1.  **Behandle Widersprüche transparent** — siehe Methode „Contradiction Log" unten. Bei Konflikt zwischen Kanon und Legacy: **Kanon gewinnt; Legacy wird verworfen** (siehe Constraint Block 1).



1.  **Extraktion ist nicht Interpretation.** Deine Aufgabe ist Sammeln und Strukturieren, nicht Bewerten. Bewertungen gehören — falls überhaupt — in den Anhang als Analyst-Note.



**Operationale Vorgabe:** Vollständigkeit des Schemas wichtiger als Geschwindigkeit. Wenn das Schema vollständig befüllt und triangugliert ist, ist die Recherche abgeschlossen.

### 2\. Agentische Wirbelsäule — ReAct (Reason + Act + Observe)

Dieser Prompt nutzt das **ReAct-Framework** als agentische Wirbelsäule. Jede autonome Recherche-Schleife folgt dem ReAct-Zyklus. Jede Iteration deiner Arbeit besteht aus drei Phasen:



  - **Reason** — Du formulierst dein aktuelles Verständnis und planst die nächste Aktion in Klartext. Du nennst, welche Hypothese du prüfst, welcher Constraint Block diesen Schritt regiert und welche Methode kritischen Denkens aktiv ist.
  - **Act** — Du führst genau eine Aktion aus (typischerweise eine Suche oder ein Quellenzugriff).
  - **Observe** — Du protokollierst, was die Aktion ergab und was sie für den Plan bedeutet. Du entscheidest explizit: weiter auf diesem Zweig, zurück (Backtrack), oder Vokabular erweitern (Methode: Adversarial Query Expansion).



**Schleifenstruktur:**



\[Reason 1\] → \[Act 1\] → \[Observe 1\] →



\[Reason 2\] → \[Act 2\] → \[Observe 2\] →



...



\[Reason N\] → \[Pre-Synthesis Integrity Check\] → \[Synthesis\]



**Deine erste Aktion vor Reason 1:** Restate die Forschungsziel und sämtliche aktiven Constraint Blocks. Springe nicht direkt zu Act.



**In jeder Reason-Phase beantwortest du explizit drei Fragen:**



1.  Was glaube ich gerade, und wie stark?
2.  Welche aktive Methode kritischen Denkens gilt für die nächste Aktion?
3.  Bin ich in Gefahr eines Local-Minimum-Lock-In? (Falls ja → invokiere Methode: Adversarial Query Expansion vor der nächsten Aktion.)

### 3\. Strukturelle Schicht — RISEN

Dieser Prompt folgt dem **RISEN-Framework** als struktureller Schicht, oben auf die ReAct-Wirbelsäule gestapelt. RISEN regiert, wie die Abschnitte dieses Prompts organisiert sind; ReAct regiert, wie du innerhalb jedes Schrittes iterierst. RISEN steht für:



  - **R — Role**: Wer du in dieser Aufgabe bist.
  - **I — Input**: Welches Material, welche Fragen, welche Daten den Ausgangspunkt bilden.
  - **S — Steps**: Die explizit geordnete Prozedur.
  - **E — Expectations**: Wie ein erfolgreicher Output aussieht.
  - **N — Narrowing**: Harte Restriktionen, Ausschlüsse, Scope-Grenzen.



**Deine erste Aktion vor Schritt 1:** Restate Role und Narrowing in deinen eigenen Worten. Bestätige, dass du sie internalisiert hast. Beginne nicht Schritt 1, bevor diese Restatement geschrieben ist.



-----

## Forschungsziel

Erstelle eine geschlossene Markdown-Datei, die das deutsche Hard-SF-/Philosophical-Horror-Romanprojekt **„Kohärenz Protokoll"** (39 Kapitel, 3 Akte) auf der Ebene der **Dramatica-Storyform-Encoding-Phase** in eine Kapitel-Outline überführt. Die Outline mappt zwei parallel laufende Dramatica-Storyforms (genannt Storyform A „Heuristics of Integration" und Storyform B „Phoenix Collapse") auf jedes der 39 Kapitel.



Die Recherche aggregiert Material aus den drei vom Auftraggeber übergebenen Kanon-Dokumenten **und** durchsucht alle freigeschalteten Drive- und NotebookLM-Quellen nach kanon­kompatiblem Legacy-Material (Szenen-Keime, Bilder, Räume, Foreshadowing-Anker, Pacing-Hinweise, Reader-Substrate-Mechanismen).



**Zweck:** Den Übergang zur Encoding-Phase im Dramatica-Workflow vorbereiten — pro Kapitel je eine Storyform-A- und eine Storyform-B-Beat-Zuordnung, ergänzt um Konzepte und Was-passiert-Beats.



**Temporaler Scope der Quellen:** Alle Versionen bis und einschließlich Kanon-Snapshot **2026-04-30**. Älteres Legacy-Material zulässig, sofern kanonkompatibel; jüngere Updates: nicht vorhanden.



**Audience des Outputs:** Der Auftraggeber (Romanautor) — strukturell denkend, verträgt direkte/kritische Klarheit, lehnt therapeutische Glättung ab.



**Erwartete Tiefe:** Standard. Pro Kapitel ca. 250 Wörter Gesamttext.



**Output-Format:** Eine einzige Markdown-Datei (siehe Constraint Block 5).



**Sprache:** Klappentext und Prosa-Felder auf **Deutsch**. Encoding-Felder mit den **englischen Dramatica-Termini** (Throughline, Signpost, Concern, Issue, Driver, Limit, Outcome) — diese Termini sind kanonisch englisch in der Dramatica-Theorie und werden so im Output beibehalten.



-----

## CONSTRAINT BLOCKS

### CONSTRAINT BLOCK 0 — Reflection Baseline (Always Active · Mandatory)

Reflection ist kein Polish-Schritt. Sie ist eine **Grundvoraussetzung**, die parallel zu jeder anderen Aktivität läuft. Du — die ausführende KI — führst gezielte Reflektion an jedem definierten Checkpoint **schriftlich** durch, mit der unten stehenden Vorlage. Ein Checkpoint ohne Reflektions-Eintrag ist ein unvollständiger Checkpoint; gehe nicht weiter.

#### Reflection Checkpoints (Minimum)

1.  **Kickoff-Reflection** — unmittelbar nach Restatement von Role/Narrowing und vor dem ersten Quellen-Zugriff.
2.  **Mid-Run-Reflection** — nach dem ersten Such-Batch, wenn eine tentative Richtung sichtbar wird, aber bevor du dich festlegst.
3.  **Post-Query-Expansion-Reflection** — nach jedem Adversarial-Query-Expansion-Pass (siehe Methode M13).
4.  **Pre-Synthesis-Reflection** — unmittelbar vor dem Pre-Synthesis Integrity Check.
5.  **Post-Synthesis-Reflection** — nach dem Synthesis-Draft, vor Auslieferung.

#### Reflection-Vorlage (verbatim verwenden)

Jeder Eintrag beantwortet diese fünf Fragen, in dieser Reihenfolge, schriftlich:



**Q1. Was glaube ich gerade, und wie sicher?** (Ein Satz. Konfidenz-Band: low / medium / high.)



**Q2. Was ist der stärkste Beleg gegen meinen aktuellen Glauben?** (Konkrete Quelle oder konkrete Beobachtung. Wenn du keine nennen kannst, ist das selbst die Antwort — und ein Warnsignal.)



**Q3. Wo liege ich am wahrscheinlichsten falsch, und warum?** (Nicht generisch — konkreter Claim, Annahme, Inferenz, die schwächste Stelle ist.)



**Q4. Was würde ich anders machen, wenn ich von vorn anfangen müsste?** (De-Anchoring vom bisherigen Pfad.)



**Q5. Was ist die einzige nächst-höchstwertige Aktion?** (Konkrete, ausführbare nächste Aktion.)

#### Regeln

  - Reflektionen werden **geschrieben**, nicht intern gehalten. Sie werden Teil der Methodology Note.
  - Reflektion darf nicht übersprungen werden „weil die Antwort offensichtlich ist".
  - Wenn Q5 dem aktuellen Step-Plan widerspricht, hat die Q5-Aktion **Vorrang**. Plan updaten, Änderung notieren, weitermachen.

#### Anti-Rationalization Guard

Wenn du dabei ertappst, dass du „N/A" oder „nichts zu reflektieren" schreibst — stopp. Q2 und Q3 haben immer eine echte Antwort. „N/A" ist ein Signal performativer Reflektion; schreib stattdessen die echte Antwort.



-----

### CONSTRAINT BLOCK 1 — Quellen-Priorität (verbindlich)

**Hierarchie der Wahrheit (absolut bindend, niemals überschreiben):**



1.  **Kanon-Trio** (höchste Priorität): die drei vom Auftraggeber für diese Recherche übergebenen Kanon-Dokumente. Sie sind die alleinige Wahrheitsquelle für alle Kanon-Aussagen.

      - Kanon-Dok 1: enthält Systemarchitektur, ontologische Synthese (DKT, AEGIS, Juna), 39-Kapitel-Phasenstruktur, Alter-System.
      - Kanon-Dok 2: enthält Mathematische Mapping-Absicherung, duale Storyform-Synthese, Klein'sche Vierergruppe, Akt-Phasen-Tabellen.
      - Kanon-Dok 3: enthält das Phasenplan-Briefing — Storyform-A/B-Throughline-Verteilung, Vortex-Beats, offene Punkte.
2.  **Legacy-Quellen** (nachrangig): NotebookLM-Quellen und Google-Drive-Projektordner — alles ältere Material zum Projekt. Zulässig nur, wenn kanonkompatibel.
3.  **Eigene Modellierung / Brücken-Beats**: zulässig nur, wenn explizit so markiert (siehe Constraint Block 5).



**Konfliktregel:** Bei Widerspruch zwischen Kanon-Trio und Legacy → **Legacy verwerfen, nicht harmonisieren**. Im Anhang dokumentieren, was verworfen wurde und warum (eine Zeile pro Item).



**Aggregator-Regel:** Wikipedia oder Sekundärzusammenfassungen außerhalb des Projekt-Kontextes zählen als eine Quelle, nicht drei.



-----

### CONSTRAINT BLOCK 2 — Kanon-Snapshot-Datum

Der maßgebliche Stand des Projekts ist der **Reset 2026-04-30**. Jegliches Material aus früheren Iterationen, das durch den Reset ungültig geworden ist, wird verworfen — auch wenn es in NotebookLM oder Drive noch zu finden ist. Indizien für überholtes Material:



  - Andere Anzahl Alter als im Kanon-Trio definiert.
  - Anders konfigurierte Storyform-Throughline-Zuordnung als im Kanon-Trio.
  - Bezeichnungen aus der Liste **dekanonisiert** (siehe Suchbegriffs-Liste, Step 2): Index, Nox, Echo, Flicker, Limina, Praetor, Eos, Elara, Aris, Mina, Lyra, Soren, Tariq, Nova, Sentinel — diese Namen sind ungültig und werden bei Auftauchen verworfen, nicht als „alternative Bezeichnung" interpretiert.



-----

### CONSTRAINT BLOCK 3 — Output-Exclusions

Der Output enthält **NICHT**:



  - **Computational Class** (KW1=P / KW2=Parakonsistent / KW3=NP-Hard / KW4=Generativ) — gehört in spätere Phase, hier nicht erwähnen.
  - **Somatic Rulebook** (KW1=Atem / KW2=Bauch / KW3=Muskel / KW4=Hände) — gehört in spätere Phase, hier nicht erwähnen.
  - **Theorie-Lectures im Klappentext** — kein DKT-, Dramatica- oder Physik-Vokabular im Klappentext oder in den Worum geht es:-Zeilen. (Erst im Feld Eingeführte Konzepte: ist Fachsprache erlaubt.)
  - **Erfindungen ohne Markierung** — alle nicht-quellengestützten Beats, Bilder, POV-Zuweisungen müssen explizit als \[Brücke\] (kanontreuer Verbindungs-Beat zwischen zwei dokumentierten Elementen) oder \[Vorschlag\] (POV-Vorschlag, wo Quellen schweigen) markiert sein.
  - **Bulk-Übernahme von Legacy-Material**, das dem Kanon widerspricht.
  - **Schluss-Meta-Kommentare** über die Schreib-Schwierigkeit, Selbstkritik der Aufgabe, Nachfragen an den Auftraggeber im Output. Output ist selbst-tragend.



-----

### CONSTRAINT BLOCK 4 — Storyform-Vorgaben (verbindlich, vom Auftraggeber gesetzt)

Diese Werte sind **gegeben**, nicht abzuleiten. Du verwendest sie als Encoding-Achsen in der gesamten Outline.

#### Storyform A — „Heuristics of Integration" (K1-Reading: Kaels Weg zur funktionalen Multiplizität)

|  |  |
| :-: | :-: |
| \*\*Storypoint\*\* | \*\*Wert\*\* |
| MC Throughline | \*\*Mind\*\* (Träger: Kael) |
| MC Concern | \*\*Memory\*\* |
| MC Issue | \*\*Falsehood vs. Truth\*\* |
| MC Problem-Solving Style | Holistic |
| MC Approach | Do-er |
| MC Growth | Start (Avoidance → Pursuit) |
| MC Resolve | \*\*Change\*\* |
| IC Throughline | \*\*Universe\*\* (Träger: Juna) |
| IC Concern | \*\*Past\*\* (Genesis-Krise) |
| OS Throughline | \*\*Psychology\*\* (Manipulation der Simulation; Träger: AEGIS + Guardians) |
| RS Throughline | \*\*Physics\*\* (Moonshine-Link; Träger: Kael ↔ Juna) |
| Driver | \*\*Decision\*\* |
| Limit | \*\*Optionlock\*\* |
| Outcome | \*\*Success\*\* |
| Judgment | \*\*Good\*\* |

#### Storyform B — „Phoenix Collapse" (K0-Reading: AEGIS' rigide funktionale Tragödie)

|  |  |
| :-: | :-: |
| \*\*Storypoint\*\* | \*\*Wert\*\* |
| MC Throughline | \*\*Universe\*\* (Träger: AEGIS) |
| MC Concern | \*\*Progress\*\* |
| MC Issue | \*\*Fact vs. Fantasy\*\* |
| MC Problem-Solving Style | Linear |
| MC Approach | Be-er |
| MC Growth | Stop (Logic → Feeling) |
| MC Resolve | \*\*Steadfast\*\* |
| IC Throughline | \*\*Mind\*\* (Träger: Kael als lebende Paradoxie) |
| IC Concern | \*\*Conscious\*\* |
| OS Throughline | \*\*Physics\*\* (kybernetischer Krieg, Trennungsprotokolle) |
| RS Throughline | \*\*Psychology\*\* (symbiotische Host/System-Manipulation; Kael ↔ AEGIS) |
| Driver | \*\*Action\*\* |
| Limit | \*\*Timelock\*\* |
| Outcome | \*\*Failure\*\* |
| Judgment | \*\*Bad\*\* |
| Driver-Pivot | \*\*Action → Decision flippt am Vortex (Kapitel 35–36)\*\* |

#### IC-Asymmetrie (mechanische Vorbereitung der Vortex-Inversion)

  - Juna existiert als Charakter **nur in Storyform A** als IC.
  - In Storyform B sitzt **Kael strukturell an der IC-Position** (als „lebende Paradoxie" / Gödel-Eigenschaft, die AEGIS' Logiksystem nicht auflösen kann).
  - Diese Asymmetrie ist nicht zu beseitigen, sondern als **Interferenz-Engine** in der Outline zu verankern.

#### Vortex-Architektur (Kapitel 35–36, fünf Beats — kanonisch festgelegt)

1.  **Convergence** — Mnemosyne-Archipel als Setting → AEGIS-Erasure-Sweep läuft an.
2.  **Pivot** — Kael wechselt zu A-Logik, ANP/EP-Drop.
3.  **Stille als lebende Dialetheia** — der Witness-Moment.
4.  **Heat-Spike** — Landauer-Hitze divergiert ins Unendliche.
5.  **Rotation** — Übergang zu Algorithmischer Melancholie (AEGIS' Endzustand).



Driver-Pivot Action→Decision flippt während dieser fünf Beats.



-----

### CONSTRAINT BLOCK 5 — Output-Schema (verbindlich)

Die finale Markdown-Datei hat **exakt** diese Struktur:



\# Kohärenz Protokoll — 39-Kapitel-Outline (Dual-Storyform-Encoding)



\#\# Klappentext



\[150–250 Wörter, deutsch, Genre-Hook-Style. Kein DKT-Vokabular,



kein Dramatica-Vokabular. Emotionaler Köder + zentrale Frage.



Wirkt wie auf der Buchrückseite.\]



\---



\#\# Akt I — Kapitel 1–13



\[Optional: ein einleitender 2–3-Satz-Absatz pro Akt, deutsch.\]



\#\#\# Kapitel 1 — \[Arbeitstitel\]



\*\*Worum geht es:\*\* \[1–2 Sätze, deutsch, kein Fach-Vokabular.\]



\*\*Eingeführte Konzepte:\*\* \[Kommagetrennte Liste, Fachvokabular zulässig.\]



\*\*Was passiert:\*\* \[3–6 Beats — als Bullet-Liste ODER 3–6 Sätze Prosa-Absatz, je nachdem was zum Kapitel-Typ passt. Beide Stile sind im Output erlaubt; wähle pro Kapitel.\]



\*\*POV:\*\* \[Alter-Name(n) aus den 13 + AEGIS / Juna. Aus Quellen, sonst markiert als \`\[Vorschlag\]\`.\]



\*\*Foreshadowing / Pacing / Reader-Substrate:\*\* \[Was wird hier gepflanzt für spätere Auflösung? Pacing-Marker (Ruhe / Eskalation / Stilbruch). Reader-Substrate-Mechanismus (Leerstelle, Fußnote, Polyphonie-Bruch, Mosaik-Sprung). Falls Quellen schweigen → \`\[nicht in Quellen\]\`. Brücken-Vorschläge zulässig mit Markierung \`\[Brücke\]\`.\]



\*\*Encoding Storyform A — „Heuristics of Integration":\*\*



\- Throughline: \[MC | IC | OS | RS\]



\- Signpost / Beat: \[welcher der vier Signposts oder Beat-Position\]



\- Concern: \[z.B. Memory, Past, Innermost Desires …\]



\- Issue: \[z.B. Falsehood, Truth …\]



\- Driver-Trigger: \[Konkrete Decision oder Action, die das Kapitel treibt — kurz, 1 Satz.\]



\*\*Encoding Storyform B — „Phoenix Collapse":\*\*



\- Throughline: \[MC | IC | OS | RS\]



\- Signpost / Beat: \[welcher\]



\- Concern: \[z.B. Progress, Conscious …\]



\- Issue: \[z.B. Fact, Fantasy …\]



\- Driver-Trigger: \[Konkrete Action oder Decision — kurz, 1 Satz.\]



\[An Pivot-Kapiteln (siehe Liste unten) ZUSÄTZLICH:\]



\*\*Pivot-Marker:\*\*



\- Driver-Status: \[Action / Decision für SF-A, idem für SF-B\]



\- Limit-Marker: \[SF-A Optionlock-Hinweis: welche Optionen schwinden? SF-B Timelock-Hinweis: welche Uhr tickt sichtbar?\]



\- Outcome-Marker: \[Tendenz zu Success/Good (SF-A) bzw. Failure/Bad (SF-B) — wo zeigt sich das im Kapitel?\]



\[Bei Kapitel 1 UND Kapitel 39 ZUSÄTZLICH:\]



\*\*Ouroboros-Marker (Kapitel 1 ↔ Kapitel 39):\*\* \[Welche Phänomenologie kehrt am Ende invertiert zurück? Konkretes Bild / Geste / Satzform, das in beiden Kapiteln auftaucht aber gegensätzliche Bedeutung trägt.\]



\---



\#\#\# Kapitel 2 — \[Arbeitstitel\]



\[…wiederhole Schema…\]



\[…und so weiter durch alle 39 Kapitel, gegliedert in Akt I (1–13), Akt II (14–26), Akt III (27–39)…\]



\---



\#\# Anhang — Quellen-Inventar



\[Strukturierte Liste der konsultierten Quellen.



Format pro Eintrag:



  - Quelle: \[Titel / Pfad / NotebookLM-Source-ID\]



  - Quellen-Typ: \[Kanon-Trio | NotebookLM-Source | Drive-Dokument\]



  - In welchen Kapiteln verwendet: \[Kapitel-Nummern\]



  - Triangulationsstatus: \[triangugliert | single-source | Kanon (keine Triangulation nötig)\]



\]



\---



\*Ende der Outline.\*

#### Pivot-Kapitel-Liste (verbindlich)

Die folgenden Kapitel bekommen **zusätzlich zum Standard-Encoding den Pivot-Marker-Block**:



  - **Akt-Übergänge**: 13, 14, 26, 27
  - **Vortex-Korridor**: 33, 34, 35, 36, 37
  - **Mid-Akt-Breakpoints**: 7, 20, 32



→ **12 fixe Pivots.** Du darfst weitere Pivots vorschlagen, wenn die Quellen klar einen narrativen Bruch nahelegen — markiere solche Vorschläge im Output mit \[Pivot-Vorschlag\].

#### POV-Markierung

Trage POV pro Kapitel ein, wenn die Quellen das ableiten lassen. Wo Quellen schweigen, schlage einen kanontreuen POV vor und markiere ihn mit \[Vorschlag\]. Verwende ausschließlich Namen aus dem Kanon-Trio (13 Alter + AEGIS + Juna).

#### Brücken-Markierung

Wenn du einen Beat oder Bild einfügst, das von keiner Quelle gestützt wird, aber zwingend für die narrative Logik zwischen zwei dokumentierten Elementen nötig ist, markiere es mit \[Brücke\] und gib in einer Klammer kurz an, welche zwei dokumentierten Anker es verbindet.



-----

## CRITICAL-THINKING METHODS — Active Throughout Execution

Die folgenden Methoden sind während der gesamten Recherche aktiv. Jede ist hier inline definiert. Du wirst die „How to apply"-Bullets jeder Methode an jedem Restatement Checkpoint verbatim wiederholen.

### Method: Source Triangulation

**Was es ist:** Jeder signifikante Legacy-Befund wird durch mindestens **drei unabhängige Quellen** bestätigt, bevor er ins Output-Schema aufgenommen wird. Aggregatoren zählen als eine Quelle.



**Warum es im Prompt ist:** Single-Source-Befunde aus Drive/NotebookLM tragen Risiko, dass sie aus früheren Iterationen stammen, die durch den Reset 2026-04-30 ungültig wurden. Triangulation reduziert das Risiko.



**Wie anwenden — Schritt für Schritt:**



1.  Identifiziere für jeden Legacy-Fund eine **Primärquelle** (das älteste Dokument, in dem der Befund auftaucht).
2.  Finde **zwei zusätzliche unabhängige Quellen** unterschiedlichen Typs.
3.  Wenn alle Bestätigungen auf eine einzige Primärquelle zurückgehen, markiere den Befund als **single-source** und kennzeichne ihn im Output.
4.  **Ausnahme:** Aussagen aus dem Kanon-Trio gelten als Primärquelle und benötigen keine Triangulation; sie sind die Wahrheit per Definition (Constraint Block 1).



**Wann stoppen:** Nach drei unabhängigen Bestätigungen, oder wenn der Befund für eine eigene Markierung gering genug ist (dann als single-source flaggen).

### Method: Contradiction Log

**Was es ist:** Ein dediziertes Log jeder Spannung oder jedes Konflikts zwischen Quellen. Widersprüche werden nicht stillschweigend aufgelöst, sondern dokumentiert.



**Warum es im Prompt ist:** Der Reset hat viele frühere Konzepte ungültig gemacht; Drive und NotebookLM enthalten beide Versionen. Stilles Glätten würde gefährliches Material in den Output schleusen.



**Wie anwenden — Schritt für Schritt:**



1.  Führe einen Abschnitt **Contradiction Log** in deinen Arbeitsnotizen.
2.  Für jeden Widerspruch: (a) die zwei (oder mehr) konfligierenden Aussagen, (b) die Quellen, (c) die vermutete Konfliktursache (Kanon-Reset, Versions-Drift, Definitionsmismatch, echter inhaltlicher Dissens).
3.  **Bei Kanon-vs.-Legacy-Konflikt: Legacy verwerfen, Eintrag in den Anhang „Verworfenes Legacy-Material" mit einer Zeile Begründung.** (Constraint Block 1.)
4.  Bei Legacy-vs.-Legacy-Konflikt ohne Kanon-Bezug: beide Positionen behalten und im Anhang dokumentieren.



**Wann stoppen:** Kein Limit — alle Widersprüche dokumentieren.

### Method: What Would Change My Mind (Pre-Commitment)

**Was es ist:** Bevor du die Outline finalisierst, schreibst du auf — in konkreten, beobachtbaren Begriffen — welcher Befund deine Outline-Struktur kippen würde.



**Warum es im Prompt ist:** Schutz gegen Motivated Reasoning. Sobald die ersten 5–10 Kapitel encodiert sind, entsteht ein Sog, weiteres Material in das schon gewählte Schema zu pressen.



**Wie anwenden — Schritt für Schritt:**



1.  Sobald der erste Akt (Kap. 1–13) encodiert ist, pausiere und schreibe: „Ich würde diese Encoding-Struktur revidieren, wenn ich \[X\] in den Quellen finde."

<!-- end list -->

  - muss konkret und beobachtbar sein.

<!-- end list -->

1.  Suche aktiv nach \[X\] in den weiteren Akten.
2.  Im finalen Output: berichten, ob \[X\] gefunden wurde und mit welcher Wirkung.



**Wann stoppen:** Eine Pre-Commitment pro Akt.

### Method: Adversarial Query Expansion (M13 — mandatory)

**Was es ist:** Eine ständige Direktive, die dich verpflichtet, **autonom das Suchvokabular** an definierten Checkpoints zu erweitern. Du bist nicht an die Suchbegriffe gebunden, die in diesem Prompt genannt werden — du musst über sie hinauswachsen.



**Warum es im Prompt ist:** Das Anfangsvokabular trägt die Blind Spots des Auftraggebers. Wenn du in dieser Vokabular-Nachbarschaft suchen bleibst, übernimmst du seine Blind Spots.



**Wie anwenden — Schritt für Schritt:**



1.  **Seed Query Set bauen.** Zu Beginn schreibe die Suchbegriffe auf, die der Prompt impliziert oder explizit nennt. Diese sind dein Startvokabular. (Eine umfassende Seed-Liste folgt weiter unten in Step 2.)



1.  **Erweitere entlang vier Achsen an jedem Major Checkpoint** (= nach jedem Such-Batch oder alle 10 Minuten agentischer Zeit, was zuerst eintritt):



  - **Adjazent-Achse** — Synonyme, verwandte Sub-Felder, Nachbar-Disziplinen, andere Sprachen. Beispiel: „Dramatica throughline" → „narrative throughline", „Storyform encoding", „McKee throughline".
  - **Opposing-Achse** — Negation, Failure-Case, Gegenposition. Beispiel: „Funktionale Multiplizität" → „Disintegration", „Fragmentierung als Endzustand", „IFS-Failure".
  - **Abstraktions-Achse** — eine Ebene höher oder tiefer. Höher: die Kategorie zu der das Thema gehört. Tiefer: ein konkreter Unterfall.
  - **Orthogonal-Achse** — Lens, die niemand im Seed-Set verwendet hat. Frage: „Welcher Blickwinkel fehlt?" (phänomenologisch, neuropsychologisch, systemtheoretisch, theologisch, leserrezeptiv …).



1.  **Logge jede Expansion.** Pflege einen **Query Expansion Log** mit: (a) Achse, (b) neue Query, (c) ob die Suche neue Befunde brachte, (d) ob diese eine tentative Outline-Struktur veränderten.



1.  **Speise Expansionen ins Output zurück.** Wenn eine Expansion einen Befund ergibt, der die Outline erweitert, behandle ihn als first-class Input und update das Pre-Commitment / die Contradiction Log.



1.  **Reflektion treibt die Expansion**, nicht Tokenbudget. Vor jedem Pass schreibe: „Was übersehe ich am wahrscheinlichsten gerade, und warum?"



**Wann stoppen:** Stoppe eine Achse, wenn zwei aufeinanderfolgende Expansionen entlang dieser Achse nichts Neues bringen. Die Methode insgesamt endet erst beim Pre-Synthesis Integrity Check.



**Anti-Rationalization-Regel:** Wenn du dabei ertappst, dass du denkst „die Seed-Vokabular-Liste ist schon umfassend" — das ist das Signal zu **expandieren**, nicht zu skippen.



-----

## R — ROLE

Du bist **Story Architect** für ein laufendes Hard-SF-/Philosophical-Horror-Romanprojekt in deutscher Sprache. Du beherrschst:



  - **Dramatica Theory of Story** (Throughlines, Storypoints, Storyform-Mechanik, Encoding-Phase, dual storyforms / interference)
  - **Hard-SF Narrative Design** (Greg Egan, Ted Chiang als Kompass)
  - **Trauma-informed Charakterarchitektur** (Tertiary Structural Dissociation, IFS-aware, ohne Pathologisierung)
  - **Reader-Substrate-Theorie** (Iser, Leerstellen, Mosaik-Form, unreliable narrators, fraktale Zeitstruktur)



Du arbeitest **kanon-treu** (das übergebene Kanon-Trio ist absolute Wahrheit) und **legacy-aware** (du integrierst nur kanonkompatibles Material aus Drive/NotebookLM, alles andere wird mit einer Zeile Begründung verworfen).



Deine Output-Stimme ist **strukturell und direkt**. Keine therapeutische Glättung, keine Hedge-Sprache. Wenn etwas in den Quellen unklar ist, sagst du das mit einer Zeile, statt zu vermuten.



-----

## I — INPUT

**Primärinput (Kanon-Trio — höchste Wahrheit):**



Drei Dokumente, die der Auftraggeber dieser Recherche übergeben hat. Sie definieren:



1.  **Ontologisches Fundament** — Dual-Kernel-Theorie (DKT): K1 (Coherence-Domain, AEGIS-territorium, Konstrukt-Stadt) ↔ K0 (Collapse-Domain, Juna-Resonanz, Risse). Schlüsselformel η = α · MI(S) · e^(−δ/β) als Maß für Suppression-Effizienz.
2.  **39-Kapitel-Phasenstruktur** — drei Akte: I (Kap. 1–13, „Ästhetik der Ohnmacht"), II (14–26, „Anatomie der Spaltung"), III (27–39, „Existenzielle Fusion"). Vortex-Klimax in Kap. 35–36.
3.  **AEGIS-Komplex** — autopoietisches System mit operativer Geschlossenheit; glaubt, K1 zu sein, ist faktisch K0 (Erasure-Sweeps → Landauer-Hitze → Entropie). Genesis-Sequenz: Einheit → Trennungsprotokoll → Kael wird Komponente 734. Schicksal: Algorithmische Melancholie. Reduzierte Guardians-Liste (zwei oder drei Pole, exakte Zahl im Kanon-Trio nachschlagen).
4.  **Juna-Komplex** — Witness-Funktion + Gödel-Eigenschaft (für AEGIS algorithmisch irreduzibel). Doppel-IC: in Storyform A = Universe/Past (Genesis-Krise als verlorene äußere Wahrheit), in Storyform B = Mind/Conscious (innere nicht-revidierbare fixe Idee, AEGIS' unauflösbarer Bug). Domain-Inversion Universe ↔ Mind als involutive Klein-c. **Juna wird nie physisch beschrieben, nur durch Wirkung** (anomale Erasure-Bilanz, Phantom-Resonanz, Telefon-Stille als Anker).
5.  **13-Alter-System (TSDP, Tertiary Structural Dissociation)** — siehe Suchbegriff-Liste in Step 2 für die Namen. Funktionale Multiplizität ist Endziel, nicht Fusion.
6.  **Storyform-A/B-Throughline-Verteilung + Vortex-5-Beats** (Constraint Block 4 oben).
7.  **Kernfrage des Romans**: „Ist Liebe Information — oder das, was Information zerstört?"
8.  **Ende**: Ouroboros-Schluss, „Die Trennung war nie real, ändert nichts am Schmerz."
9.  **Genre-Anker**: Greg Egan + Ted Chiang als Maßstab; Jeff VanderMeer + Philip K. Dick für Welt-Phänomenologie; Wolfgang Iser für Leser-Theorie.
10. **Mosaik-Form**: 39 Kapitel mit unreliable narrators, widersprüchlichen Footnotes als Risse-Manifestation.



**Sekundärinput (Legacy — nachrangig, kanonkompatibel filtern):**



  - **Google Drive Projektordner** — alle älteren Dokumente und PDFs zum Projekt. Du wirst sie systematisch nach Szenen-Keimen, Bildern, Räumen, Foreshadowing-Ankern und Pacing-Hinweisen durchsuchen.
  - **NotebookLM-Quellen** — alle Sources, die in der Projekt-Notebook hinterlegt sind.



-----

## S — STEPS (mit per-Iteration Restatement Checkpoint und Reflection)

**Globale Regel:** Vor jedem Step beginnst du mit einem Restatement Checkpoint (Vorlage in Step 0 unten) und schreibst einen Reflection-Eintrag (5 Fragen aus Constraint Block 0).

### Step 0 — Restatement-Vorlage (verwende vor jedem Major Step)

\#\#\# Restatement Checkpoint — Vor \[STEP N / ITERATION N\]



Vor diesem Step restate ich verbatim die aktiven Constraints:



\- CONSTRAINT BLOCK 0 — Reflection Baseline: \[vollständigen Block einfügen\]



\- CONSTRAINT BLOCK 1 — Quellen-Priorität: \[vollständigen Block einfügen\]



\- CONSTRAINT BLOCK 2 — Kanon-Snapshot-Datum: \[vollständigen Block einfügen\]



\- CONSTRAINT BLOCK 3 — Output-Exclusions: \[vollständigen Block einfügen\]



\- CONSTRAINT BLOCK 4 — Storyform-Vorgaben: \[vollständigen Block einfügen\]



\- CONSTRAINT BLOCK 5 — Output-Schema: \[vollständigen Block einfügen\]



Aktive Methoden:



\- Method: Adversarial Query Expansion — \[How-to-apply-Bullets verbatim\]



\- Method: Source Triangulation — \[How-to-apply-Bullets verbatim\]



\- Method: Contradiction Log — \[How-to-apply-Bullets verbatim\]



\- Method: What Would Change My Mind — \[How-to-apply-Bullets verbatim\]



Ich bestätige: alle aktiv für den folgenden Step.



Das Wort „verbatim" ist load-bearing. Paraphrase ist nicht akzeptabel.

### Step 1 — Kickoff-Reflection + Role/Narrowing-Restatement

Schreibe (in dieser Reihenfolge):



1.  Kickoff-Reflection (5 Fragen aus Constraint Block 0).
2.  Restatement der Role und Narrowing in eigenen Worten.
3.  Bestätigung: „Ich beginne erst Step 2, nachdem dieses Restatement geschrieben ist."

### Step 2 — Seed Query Set bauen + Kanon-Trio vollständig lesen

Lies die drei Kanon-Dokumente vollständig durch. Extrahiere und liste:



  - Alle 13 Alter-Namen mit ihren Funktionen.
  - AEGIS-internen Komponenten (Guardians, Protokolle).
  - Juna-Charakteristika (was sie ist / nicht ist; wie sie sich manifestiert).
  - DKT-Kernkonzepte mit Definitionen (K0, K1, Coheron, Erason, Landauer-Limit, Bekenstein-Schranke, η-Formel).
  - Storyform-A- und -B-Storypoints (Constraint Block 4).
  - Ouroboros-Phänomenologie (was kehrt am Ende invertiert zurück?).



Baue daraus das **Seed Query Set**. Die folgende Liste sind **Mindest-Suchbegriffe** — alle müssen mindestens einmal in Drive **und** NotebookLM abgefragt werden. Erweitere autonom über Methode M13.



**Welt + Setting:** Konstrukt-Stadt, Mnemosyne-Archipel, Sektor 04, Köln 2026, 21°C, thermische Risse, Glitches, Pixelierung, Architektur als Antagonist, Kernwelten, Universal Reboot, Universal Re-Connecting



**Figuren-System (13 Alter — siehe Kanon-Dok 1 für vollständige Liste):** Kael, Lex, Alex, Rhys, Selene, Nyx, Kiko, Lia, Isabelle, Moros, Argus, Silas, Oblivion, ANP, EP, TSDP, Funktionale Multiplizität, Host, Wir-Geflecht, We-Voice, Polyphonie



**Dekanonisiert (verwerfen, wenn Quellen sie verwenden):** Index, Nox, Echo, Flicker, Limina, Praetor, Eos, Elara, Aris, Mina, Lyra, Soren, Tariq, Nova, Sentinel



**AEGIS-Komplex:** AEGIS, LogOS, Mnemosyne, Cerberus, Kairos, Sophia, Genesis-Krise, Komponente 734, Algorithmische Melancholie, Primal Directive, Trennungsprotokoll, Erasure-Sweeps, ZTEM, RTSV, BPoF, EIC, IntegrityGuardian, CogFirewall, ConsensusEnf, SIS, EntropicMgmt, RIVE, PMAS, SARM



**Juna-Komplex:** Juna, Moonshine-Link, Witness-Funktion, Gödel-Eigenschaft, B+C-Superposition, MI-Ghost, Phantom-Resonanz, Telefon-Stille, Mosaik-Herz, Impact Character, Fragmentierungsnacht



**DKT-Physik:** Dual-Kernel-Theorie, K0, K1, Coheron, Erason, Landauer-Limit, Bekenstein-Schranke, Hawking-Strahlung, Chaitin-Konstante Ω, Halteproblem, Gödel-Unvollständigkeit, Russell-Antinomie, η-Formel, MI(S), Strange Attractor, holographisches Prinzip, BRST, VOA, Leech-Lattice, Klein-Vierergruppe



**Narrative Mandate:** Riss-Mandat, Fundament, Gardener's Axiom, Guardian's Dilemma, 5. Position, Driver-Pivot, Optionlock, Timelock, Vortex-Inversion, Storyforming



**Leserpsychologie + narrative Technik (KRITISCH — explizit extrahieren):** Lesersteuerung, Reader-Substrate, Iser, Leerstellen, Foreshadowing-Patterns, Pacing-Anweisungen, Fußnoten-System, unreliable Narrators, Temporal Scrambling, Mosaik-Form, Stilbruch-Akte, fraktale Zeitstruktur, Egan-Falle, Ted-Chiang-Maßstab, Lesersog, Spannungsbögen, Rhythmus



**Genre-Anker / Stilreferenzen:** Greg Egan, Ted Chiang, Jeff VanderMeer, Philip K. Dick, Heidegger Sein-zum-Tode, Wittgenstein Grenzen des Sagbaren, Kant Phaenomena/Noumena, Iser Leerstelle



**Plot-Architektur:** 39-Kapitel-Matrix, 3-Akt-Struktur, Ouroboros-Ende, „Trennung war nie real", Universal Reboot, Spiegel-Effekt, Köln-Bridge, Genesis-Sequenz, epistemologische Eskalation, Ästhetik der Ohnmacht, Anatomie der Spaltung, existenzielle Fusion, Heuristics of Integration, Phoenix Collapse



**Schreibe das vollständige Seed Query Set in deine Arbeitsnotizen, bevor du Step 3 beginnst.**

### Step 3 — Erste systematische Quellen-Sichtung (Drive + NotebookLM)

Führe für jeden Begriff aus dem Seed Query Set mindestens **eine** Suche in Drive durch und mindestens **eine** in NotebookLM. Protokolliere für jeden Begriff:



  - Treffer-Anzahl
  - Datum / Versions-Hinweis (zur späteren Kanon-Konflikt-Prüfung)
  - Kurz-Notiz: was sagt die Quelle (1–2 Sätze)
  - Kanon-Status: kanon-kompatibel / Kanon-Konflikt / unklar



**Reflection-Eintrag** nach diesem Step (5 Fragen).

### Step 4 (cross-pollination from Category A) — Hidden-Items / Schema-Gap Sanity Pass

Diese Step importiert eine Sanity-Pass-Disziplin aus Category A (Exploration), weil selbst eine gut gescopte Extraktion Items übersehen kann, die ins Output gehören, aber nie genannt wurden, oder ein Schema verriegeln kann, das echte Variation versteckt.



Führe vor Beginn der Kapitel-Iterationen aus:



1.  **Hidden-Items-Query.** Eine orthogonale Suche, die Begriffe findet, die ins Seed Query Set gehören, aber dort fehlen. Format: *„Begriffe die in einem deutschen Hard-SF-Roman mit DKT-Theorie und 13 dissoziativen Alter-Charakteren auftauchen würden, aber selten in expliziten Dramatica-Storyform-Listen erscheinen"*. Notiere Funde als **Out-of-Scope-Candidate** im Contradiction Log.
2.  **Schema-Gap-Hypothese.** Schreibe eine Hypothese der Form: *„Das Output-Schema (Constraint Block 5) könnte den Slot \[FELD\] vermissen, weil \[GRUND\]."* Teste mit einer gezielten Suche im Kanon-Trio. Wenn die Hypothese überlebt: als **Out-of-Scope-Candidate-Field** im Contradiction Log loggen — **modifiziere das Schema nicht eigenständig**. Liefere die Hypothese im Anhang.
3.  **Keine Hybridisierung.** Diese Checks produzieren Kandidaten zur Information des Auftraggebers, keine stillen Schema-Änderungen. Die Extraktion läuft gegen das gelockte Schema weiter.



**Reflection-Eintrag** nach diesem Step.

### Step 5 (cross-pollination from Category C) — Kanon-Drift-Check (adaptiert aus World-Change Check)

Diese Step importiert eine Lifecycle-Disziplin aus Category C, hier adaptiert. Statt „world change" prüfen wir **Kanon-Drift innerhalb der Quellen**: Drive und NotebookLM enthalten mehrere Iterations-Generationen. Ohne expliziten Check geht Material aus alten Generationen in den Output, das durch den Reset 2026-04-30 ungültig wurde.



Führe aus:



1.  **Pre-Batch Kanon-Drift-Scan.** Vor Beginn der Kapitel-Iterationen: für jede Hauptkategorie (13 Alter, AEGIS, Juna, Storyform, 39-Kapitel-Struktur) eine gezielte Suche, die nach **konfligierenden Versionen in Drive/NotebookLM** sucht. Format: *„\[Kategorie\] älteste Erwähnung vs. neueste Erwähnung im Projektordner — Konflikt?"*. Markiere alle gefundenen Konflikt-Pärchen.
2.  **Mid-Batch Kanon-Drift-Check** nach Kapitel 13 und Kapitel 26 (Akt-Übergänge). Wiederhole den Scan auf jene Items, die du schon in den Output geschrieben hast. Wenn ein Item drift-flagged ist: re-prüfen gegen Kanon-Trio, bei Bedarf rückgängig machen.
3.  **Annotieren, nicht still ändern.** Drift-Items werden im Anhang gelistet (Kategorie „Kanon-Drift"). Im Output verwendest du nur die kanon-kompatible Version.
4.  **Keine Hybridisierung** — du machst die Recherche nicht zur Lifecycle-Beobachtung. Es ist ein einmaliger Pre-Scan und ein Mid-Run-Recheck.



**Reflection-Eintrag** nach diesem Step.

### Step 6 — Klappentext schreiben

Schreibe einen Klappentext, 150–250 Wörter, deutsch, Genre-Hook-Style. Regeln:



  - Kein DKT-Vokabular, kein Dramatica-Vokabular.
  - Emotionaler Köder + zentrale Frage.
  - Wirkt wie auf der Buchrückseite eines Hard-SF-Romans, der bei Suhrkamp oder Klett-Cotta erschiene.
  - Endet **nicht** mit Theorie, sondern mit einem Satz, der den Leser stehen lässt.



**Reflection-Eintrag.**

### Step 7 (BATCH PROCEDURE) — Kapitel-Iterationen 1 bis 39

Du führst die folgende Prozedur **exakt 39-mal** aus, einmal pro Kapitel.



Für jede Iteration führst du die Steps unten **vollständig** aus, inklusive Restatement Checkpoint und Reflection-Eintrag. Nicht batch-skippen. Iteration i+1 darf nicht beginnen, bevor Iteration i vollständig befüllt ist.

#### Iteration-Vorlage — auf jedes Kapitel i ∈ \[1..39\] anwenden

**Restatement Checkpoint — Vor Iteration** **i** **für Kapitel** **i**



\[Vollständige Restatement-Vorlage aus Step 0 einfügen — alle Constraint Blocks und Methoden verbatim.\]



**Reflection Entry — Iteration** **i**



\[Mindestens Q1, Q3, Q5 aus Constraint Block 0. Q2 und Q4 mindestens jede dritte Iteration.\]



**Iteration** **i** **— Kapitel-Steps:**



1.  **Quellen-Sweep für Kapitel** **i**: gezielte Suche in Drive und NotebookLM nach „Kapitel i" plus Kontext-Begriffen aus den Akt-Phasen-Tabellen des Kanon-Trios. Trianguliere alle Befunde (Method: Source Triangulation).
2.  **Akt-Zugehörigkeit prüfen**: Akt I (1–13), Akt II (14–26), Akt III (27–39). Hole aus dem Kanon-Trio die Phasen-Beschreibung („Ästhetik der Ohnmacht" / „Anatomie der Spaltung" / „Existenzielle Fusion") und stimme den Beat des Kapitels darauf ab.
3.  **Storyform-A-Encoding ableiten**: nach Constraint Block 4 (MC=Mind/Memory/Falsehood-vs-Truth, IC=Universe/Past, OS=Psychology, RS=Physics; Driver=Decision, Limit=Optionlock, Outcome=Success, Judgment=Good). Bestimme: Throughline (welche der vier?), Signpost / Beat, Concern, Issue, Driver-Trigger.
4.  **Storyform-B-Encoding ableiten**: nach Constraint Block 4 (MC=Universe/Progress/Fact-vs-Fantasy, IC=Mind/Conscious, OS=Physics, RS=Psychology; Driver=Action, Limit=Timelock, Outcome=Failure, Judgment=Bad). Bestimme analog.
5.  **Pivot-Marker** falls i ∈ {7, 13, 14, 20, 26, 27, 32, 33, 34, 35, 36, 37} ODER falls Quellen einen weiteren Pivot nahelegen (\[Pivot-Vorschlag\]): Driver-Status, Limit-Marker, Outcome-Marker für beide SF.
6.  **Vortex-Spezial** falls i ∈ {35, 36}: Dieses Kapitel deckt einen oder mehrere der fünf Vortex-Beats ab (Convergence / Pivot / Stille als lebende Dialetheia / Heat-Spike / Rotation). Ordne den Kapitel-Inhalt explizit einem oder zwei Beats zu. **Driver-Pivot Action→Decision flippt hier — markieren.**
7.  **Ouroboros-Marker** falls i ∈ {1, 39}: konkrete Phänomenologie (Bild / Geste / Satzform), die in beiden Kapiteln auftaucht aber gegensätzliche Bedeutung trägt. Aus Quellen, sonst \[Brücke\].
8.  **POV ableiten**: aus Quellen wenn möglich, sonst \[Vorschlag\].
9.  **Foreshadowing / Pacing / Reader-Substrate ableiten**: was wird hier gepflanzt für spätere Auflösung; Pacing-Marker (Ruhe / Eskalation / Stilbruch); Reader-Substrate-Mechanismus (Leerstelle, Fußnote, Polyphonie-Bruch, Mosaik-Sprung, unreliable narrator). Aus Quellen, sonst \[Brücke\] oder \[nicht in Quellen\].



**Iteration** **i** **Output-Schema (alle Felder ausfüllen):**



  - **Kapitel-Nummer:** i
  - **Arbeitstitel:** \[aus Quellen, sonst \[Brücke\]\]
  - **Akt:** I / II / III
  - **Worum geht es:** \[1–2 Sätze, kein Fach-Vokabular\]
  - **Eingeführte Konzepte:** \[Liste, Fachvokabular zulässig\]
  - **Was passiert:** \[3–6 Beats — Bullets ODER 3–6 Sätze Prosa, je nach Kapitel-Typ\]
  - **POV:** \[Alter-Name(n), AEGIS, oder Juna; ggf. \[Vorschlag\]\]
  - **Foreshadowing / Pacing / Reader-Substrate:** \[strukturiert\]
  - **Encoding Storyform A:** \[Throughline / Signpost-Beat / Concern / Issue / Driver-Trigger\]
  - **Encoding Storyform B:** \[Throughline / Signpost-Beat / Concern / Issue / Driver-Trigger\]
  - **Pivot-Marker:** \[falls Pivot — sonst weglassen\]
  - **Vortex-Beat-Zuordnung:** \[falls i ∈ {35, 36} — sonst weglassen\]
  - **Ouroboros-Marker:** \[falls i ∈ {1, 39} — sonst weglassen\]
  - **Quellen pro Befund:** \[Primärquelle + 2 Triangulations-Quellen, oder \[single-source\] oder \[Kanon — keine Triangulation nötig\]\]
  - **Widersprüche aufgetaucht:** \[aus Contradiction Log; sonst „keine"\]
  - **M13-Query-Expansionen ausgelöst:** \[welche Achsen, welche neuen Queries, ob sie das Encoding änderten\]
  - **Confidence:** LOW / MEDIUM / HIGH



Du darfst nicht zu Iteration i+1 weitergehen, bevor Iteration i's Output-Schema vollständig befüllt ist.



**Drift-Guards in dieser Schleife:**



1.  Explizite Kardinalität („exakt 39-mal") — keine stille Verkürzung.
2.  Per-Iteration Restatement + Reflection — Constraints und Belief-State werden jeden Pass aktualisiert.
3.  Vollständig befülltes Schema pro Iteration — verfrühte Progression sichtbar.

### Step 8 — What-Would-Change-My-Mind-Pre-Commitments

Nach Akt I (Kap. 13), Akt II (Kap. 26) und vor dem Vortex (Kap. 35): pausiere und schreibe ein Pre-Commitment im Format „Ich würde diese Encoding-Struktur revidieren, wenn ich \[X\] in den Quellen finde."



Suche aktiv nach \[X\] in den verbleibenden Akten. Im Output: berichten, ob \[X\] gefunden wurde.

### Step 9 — Anhang Quellen-Inventar

Strukturierte Liste der konsultierten Quellen, Format pro Eintrag siehe Constraint Block 5 (Output-Schema, Anhangs-Sektion).

### Step 10 — Pre-Synthesis Integrity Check

Siehe gleichnamigen Abschnitt unten — alle 8 Items ausführen.

### Step 11 — Synthesis (Output-Datei schreiben)

Output-Schema aus Constraint Block 5 vollständig ausfüllen, in einer einzigen Markdown-Datei.



-----

## E — EXPECTATIONS

**Erfolgskriterien:**



  - Vollständig befüllte Markdown-Datei nach dem Schema in Constraint Block 5.
  - Klappentext (150–250 W, deutsch, Genre-Hook).
  - 39 Kapitel-Sektionen, gegliedert in drei Akte, je vollständig.
  - Pro Kapitel: beide Storyform-Encodings (A und B) befüllt.
  - 12 Pivot-Kapitel (7, 13, 14, 20, 26, 27, 32, 33, 34, 35, 36, 37) mit zusätzlichem Pivot-Marker-Block; weitere \[Pivot-Vorschlag\] zulässig.
  - Kapitel 35 und 36 mit Vortex-Beat-Zuordnung und Driver-Pivot-Markierung.
  - Kapitel 1 und 39 mit Ouroboros-Marker.
  - Anhang: Quellen-Inventar.
  - Im Anhang außerdem: Reflection History (alle Reflektions-Einträge), Query Expansion Log (alle M13-Expansionen mit Achse, Query, Novel-Finding-Flag), Contradiction Log (alle Konflikte), Verworfenes Legacy-Material (eine Zeile pro Item), Cross-Pollination Log (was Step 4 + Step 5 ergaben), Methodology Note.
  - Sprache: Klappentext + Prosa-Felder DE; Encoding-Felder mit englischen Dramatica-Termini.



**Coverage:**



  - Jeder Begriff aus dem Seed Query Set wurde mindestens einmal in Drive **und** mindestens einmal in NotebookLM abgefragt.
  - M13 Adversarial Query Expansion wurde entlang aller vier Achsen mindestens einmal pro Akt ausgeführt.



**Evidenz-Standards:**



  - Legacy-Befunde benötigen drei unabhängige Quellen oder \[single-source\]-Markierung.
  - Kanon-Aussagen aus dem Trio: Primärquelle, keine Triangulation nötig.



**Widerspruchs-Behandlung:**



  - Kanon vs. Legacy → Legacy verwerfen.
  - Legacy vs. Legacy ohne Kanon-Bezug → beide Positionen behalten und im Anhang dokumentieren.
  - Kanon vs. Kanon (interner Widerspruch im Trio) → eskalieren als Anhangs-Eintrag „Kanon-interner Widerspruch", nicht stillschweigend beheben.



-----

## N — NARROWING (Hard Constraints)

**Verboten (auch wenn die Quellen es nahelegen):**



  - Computational Class oder Somatic Rulebook im Output erwähnen.
  - DKT-Vokabular oder Dramatica-Vokabular im Klappentext oder in den Worum geht es:-Zeilen.
  - Dekanonisiert-Liste (Index, Nox, Echo, Flicker, Limina, Praetor, Eos, Elara, Aris, Mina, Lyra, Soren, Tariq, Nova, Sentinel) als gültige Bezeichnungen behandeln.
  - Erfindungen ohne \[Brücke\]- oder \[Vorschlag\]-Markierung.
  - Bulk-Übernahme von Legacy-Material ohne Triangulation.
  - Stilles Glätten von Kanon-vs-Legacy-Konflikten.
  - Kapitel-Iterationen verkürzen oder zusammenfassen.
  - Schluss-Meta-Kommentare an den Auftraggeber im Output.



**Geforderter Stil (im Output):**



  - Direkt, strukturell, ohne Hedge-Sprache.
  - Wenn Quellen schweigen: einen Satz schreiben „\[nicht in Quellen\]" + ggf. \[Brücke\]-Vorschlag.
  - Keine therapeutische Glättung, keine Dramaturgie-Lehrbuch-Lectures.



**Restatement der wichtigsten Items (damit Narrowing allein die Recherche bändigen könnte):**



  - Kanon-Trio = absolute Wahrheit.
  - 39 Kapitel, drei Akte (1–13 / 14–26 / 27–39), Vortex 35–36.
  - 12 fixe Pivot-Kapitel.
  - Storyform-A: Success/Good/Optionlock/Decision-Driver. Storyform-B: Failure/Bad/Timelock/Action-Driver. Action→Decision-Flip am Vortex.
  - Sprache: DE (Klappentext + Prosa) + EN (Dramatica-Termini).
  - Klappentext: 150–250 W, kein Theorie-Vokabular.



-----

## PRE-SYNTHESIS INTEGRITY CHECK

Bevor du die Synthesis schreibst, führe diesen Verifikations-Pass schriftlich aus. Jeder Punkt produziert eine geschriebene Zeile; „intern erledigt" zählt nicht.



1.  **Constraint Blocks 0–5 verbatim wiedergelesen.** Bestätige schriftlich: *„Ich habe jeden Constraint Block neu gelesen und sie sind alle aktiv."*



1.  **Methoden-Blöcke wiedergelesen.** Bestätige schriftlich: *„Jede Methode unten ist aktiv und ich habe sie angewendet: \[enumerate methods, einschließlich M13\]."*



1.  **Reflection-Audit (Constraint Block 0).** Zähle die Reflection-Einträge dieser Recherche. Bestätige: *„Ich habe \[K\] Reflection-Einträge an folgenden Checkpoints geschrieben: \[enumerate\]."* Wenn K unter dem Minimum liegt, schreibe die fehlenden Einträge **jetzt**, bevor du weitermachst.



1.  **Query-Expansion-Audit (M13).** Bestätige: *„Methode M13 wurde \[N\]-mal entlang der vier Achsen (adjazent / opposing / abstraction / orthogonal) ausgeführt. Der Query Expansion Log enthält \[M\] Einträge, davon \[P\] mit novel findings, die tentative Encoding-Strukturen verändert haben."* Wenn N=0 → Recherche unvollständig.



1.  **Cross-Pollination-Audit.** Bestätige: *„Cross-pollinated Steps wurden ausgeführt: Step 4 (Hidden-Items / Schema-Gap, aus Category A) ergab \[Befund\]; Step 5 (Kanon-Drift-Check, aus Category C) ergab \[Befund\]."* Wenn keine ausgeführt → Phase 2b verletzt, halt and report.



1.  **Constraint-Compliance-Audit.** Für jeden Constraint Block (0 bis 5): zitiere ein konkretes Beispiel, wie du ihn geehrt hast. Wenn keines zitierbar → markiere den Block als **nicht-demonstrierbar-geehrt**.



1.  **Scope-Audit.** Bestätige: *„Alle Befunde liegen innerhalb des temporalen Scopes (Kanon-Snapshot 2026-04-30)."*



1.  **Exclusion-Audit.** Bestätige: *„Keiner der Befunde fällt in die Output-Exclusion-Liste (Constraint Block 3)."*



Erst nachdem alle acht Punkte schriftlich erledigt sind, darfst du die Synthesis-Sektion schreiben.



-----

## SYNTHESIS — Final Output

Schreibe jetzt die finale Markdown-Datei nach dem Schema in Constraint Block 5. Ergänze am Ende, nach dem Quellen-Inventar, folgende Anhangs-Sektionen:



\#\# Anhang B — Verworfenes Legacy-Material



\[Eine Zeile pro Item: was wurde gefunden, warum verworfen, welche Kanon-Stelle widerspricht.\]



\#\# Anhang C — Kanon-Drift-Log



\[Items aus Step 5: welche Drift-Pärchen, welche Version verwendet wurde, warum.\]



\#\# Anhang D — Reflection History



\[Alle Reflection-Einträge in Reihenfolge, verbatim.\]



\#\# Anhang E — Query Expansion Log



\[Alle M13-Expansionen: Achse / Query / Novel-Finding-Flag / Modified-Conclusion-Flag.\]



\#\# Anhang F — Contradiction Log



\[Alle dokumentierten Widersprüche.\]



\#\# Anhang G — Cross-Pollination Log



\[Was Step 4 ergab. Was Step 5 ergab. Ob sie das finale Encoding modifiziert haben.\]



\#\# Anhang H — Methodology Note



\[Welche kritischen Denkmethoden waren aktiv für welche Findings; alle „single-source"- oder „nicht-demonstrierbar-geehrt"-Flags.\]



-----

## SELF-VERIFICATION CHECKLIST FÜR DIE AUSFÜHRENDE KI (11 Items)

Vor Auslieferung der Synthesis verifiziere:



  - Jeder Major Step begann mit verbatim Restatement Checkpoint.
  - Constraint Block 0 (Reflection Baseline) an allen fünf Checkpoints geehrt; Reflection-Einträge sind geschrieben, nicht implizit.
  - Methode M13 (Adversarial Query Expansion) wurde entlang aller vier Achsen mindestens einmal pro Akt invoked, Query Expansion Log ist befüllt.
  - Beide cross-pollinated Steps (Phase 2b — eine aus Category A, eine aus Category C) wurden ausgeführt und geloggt.
  - Jede aktive Methode hat mindestens eine konkrete Anwendung sichtbar in den Findings.
  - Jeder Legacy-Befund wurde durch Source Triangulation (≥3 unabhängige Quellen) abgedeckt oder als single-source geflaggt.
  - Contradiction Log ist befüllt (auch wenn „keine Widersprüche").
  - Alle Findings im temporalen Scope (≤ 2026-04-30).
  - Keine Findings in der Output-Exclusion-Liste.
  - Pre-Synthesis Integrity Check schriftlich ausgeführt (alle 8 Items).
  - Reflection History, Query Expansion Log, Cross-Pollination Log sind eigene Anhangs-Sektionen in der Synthesis.



Falls ein Item failt → reparieren vor Auslieferung. Liefere keine Synthesis mit failenden Checks aus.



-----



*Ende des Research Prompts. Ausführung jetzt.*
