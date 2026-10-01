# Review PR #136

Geprüfter Head: `160f8265` (2026-10-01). Empfehlung: **mergen als Testdaten-PR**.
Der erste geprüfte Stand `5bc80c21` war unvollständig; der neue Head enthält alle
Runs, die fehlende README und den im Review gefundenen Stance-Verlust.

## Nachweise

- A: 32 Runs, 96 Calls, $1.7742322, 642.26 Sekunden.
- B: 32 Runs, 256 Calls, $5.0904062, 1954.04 Sekunden.
- Gesamt: 64 Runs, 352 Calls, $6.8646384; keine fehlgeschlagenen Calls/Chunks.
- Geprüfte Source- und Template-Hashes der gestagten Reports passen zu Dateien.
- `results.py` reproduziert die Markdown-/JSONL-Ergebnisse ohne Diff.
- Alle 52 Standardbibliotheks-Suites bestehen; 15 Venv-Suites sind ausgelassen,
  nicht bestanden. Der PR verändert keinen Extraktions- oder Kanon-Code.

## Konsistenz und Aussagekraft

Die Verträge überlappen absichtlich, sind aber keine voneinander unabhängigen
Bestätigungen. A ist ein Meta-Konzepttext, B ein Drafting-/Review-Protokoll, kein
neutraler Kanon-Datensatz. Technische Session-Aussagen (`ncp.json`, agency-CLI,
fehlende Provenienz) tauchen deshalb neben Figuren-/Welt-Aussagen auf. Ein Treffer
belegt zunächst, was diese Quelle berichtet; er bestätigt weder Kanon noch Handlung.

Staging akzeptiert insgesamt 476 Kandidaten; 68 Rows werden verweigert und eine
dedupliziert. Die Quote-Verifikation misst Texttreue, keine semantische Präzision.
`TermCensus` und `LocationRegistry` liefern Formen, die das Staging nicht übernimmt;
fehlende Rows werden in der Tabelle als nicht gestaged ausgewiesen. Leere Runs
sind je nach Vertrag erwartbar, aber ohne gelabelte Gold-Negative kein gemessener
Beleg für richtige Abstention. Gleiche Fundzeilen von Haiku/Sonnet beweisen ebenfalls
keine Relationsgleichheit. Es fehlen unabhängige Labels und Wiederholungen.

Konkreter Cross-Contract-Befund: `AliasPairs` liest an B:L39 aus ausdrücklich
„dekanonisierte Guardians … nicht übernommen“ vier `role_of/asserts`-Rows, während
`EntityFacts` die Dekanonisierung bewahrt. Der README-Befund 6 hält das jetzt fest.
Ebenso kann `same_as` bei Motiv/Bedeutung (Wegkreuzung/interner Wahlpunkt) keine
Entity-Fusion begründen. `CausalLinks` extrahiert technische fehlende Provenienz
aus B:L51; das ist keine kausale Romanrelation. Die Rows bleiben unreviewte
Vorschläge, wie der PR korrekt erklärt.

## Konkrete Kommentare / Folgearbeit

1. **Nicht blockierend, run.sh:** Ein vorhandenes Run-Verzeichnis reicht als
   Resume-Kriterium. Ein abgebrochener Run wird dauerhaft übersprungen; die
   Pipeline ohne `pipefail` kann Python-Fehler maskieren. Prüft auf vollständige
   `usage.json`/`raw.json` und eine terminale Staging-Diagnose; ergänzt eine
   Offline-Abbruchfixture. Im aktuellen vollständigen Head ist kein solcher
   Ausfall nachgewiesen.
2. **Nicht blockierend, README Befund 3:** Repariert `stands` separat, mit
   positiven *und* negativen Zahlen-/Markup-Fixtures, und re-staged die
   eingefrorenen Raw-Dateien ohne neue Modellkosten. Lasst historische Ergebnisse
   dabei vergleichbar und kennzeichnet die neue Gate-Version.
3. **Vor produktiver Nutzung:** Labelt pro Vertrag Attribution/Stance,
   Endpoint-Bedeutung und Anwendbarkeit; unterscheidet Meta-Protokoll, Vorschlag,
   Quellenbehauptung und akzeptierten Kanon. Keine Alias-Promotion aus Admission.
4. **Kostenvergleich:** „etwa doppelt Haiku“ ist eine grobe, keine kontrollierte
   Aussage. Vergleicht gleiche Quelle, Contract-/Prompt-Version und Chunking,
   und berichtet Tokenmengen neben USD. Kein Qualitätsranking aus Fundzeilen.

Kein Merge und keine Kanon-Promotion wurden vorgenommen.
