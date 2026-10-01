# novelgraph Index-Layer

## Ist-Analyse und Plan (vor Implementierung)

Basis: `b6ec5236` auf main. Gelesen: README, GOAL, CLAUDE, NOW,
PRINCIPLES und scripts/README; die Source-/Manifest-Helfer in subject und
sources, fold in wiki_index, graph/graphrag, ask/askdb/askextract,
qmd/qmd_coverage/setup_qmd und die Bench-/Evaluationsschnittstellen.

Die Quellen liegen in `Sources/drive/<slug>.md`; Slugs und Pfade werden aus
`Sources/manifest.jsonl` übernommen, niemals neu gebildet. Der Katalog hat
587 Einträge, davon 586 gelandet (gemessen mit `sources.py check`).
`Coherence Protocol.mp3` besitzt noch keinen Export. Coverage wird daher sowohl
gegen gelandete Quellen als auch gegen den gesamten Katalog ausgewiesen; der
fehlende Export wird explizit gemeldet und niemals als indexiert gezählt.

`subject.read_jsonl`, `subject.rows`, `subject._split` und `wiki_index.fold`
werden importiert. Die private Frontmatter-Schnittstelle `_split` ist eine
Abhängigkeit zur laufenden Konsolidierung; ein Integrationstest schützt ihre
Dateizeilen-Semantik. Vorhandene Scripts bleiben unverändert. Der Graph-Index
`Plan/derived/ask.db` und qmd bleiben eigenständige, unveränderte Werkzeuge.

Implementiert wird ein uv-Projekt in `novelgraph/`, mit eigener CLI und Tests.
`Index/` enthält die verlangten source-, chunk- und lex-Dateien; Vektoren und
aggregierte FTS-/mmap-Artefakte werden durch `Index/.gitignore` ausgeschlossen.
Das Projekt-venv wird lokal ausgeschlossen. Alle Quelltexte bleiben unverändert.
Die Tokenzählung nutzt den Tokenizer des Embedder-Modells; Tabellen sowie einzelne
überlange Source-Zeilen bleiben ungeteilt, weil das vorgegebene Chunk-Schema keine
Zeichenoffsets trägt. Solche Größenüberschreitungen werden gemessen, nicht versteckt.
Keine synthetischen Lemmata: ohne einen tatsächlich geladenen Lemmatizer bleibt
die Lemma-Liste leer; fold-Oberflächen bilden eine separate FTS-Spalte.

Reihenfolge: Registry und Paket; Chunker/Provenienz; inkrementeller Vektor-Cache;
FTS5/mmap/RRF; Verify mit negativen Fixtures; volle Builds aller drei Methoden;
Rebuild- und Einzelquellen-Test in einer temporären Kopie; Latenzen und unveränderte
Bench-Fragen; Messbericht und PR. Keine LLM-Calls oder neue Source-Lesungen.

Bench: `ask.bench_cases()` liefert die bestehenden Fragen samt Source-Zeilen-Gold.
Recall@8 bedeutet hier Anteil der Gold-Zeilen innerhalb der acht gefundenen Chunks;
zusätzlich wird Dokument-Recall berichtet. `graphrag.bench` misst Wiki-Seiten, daher
ist sein Page-Recall nicht direkt mit Chunk-Recall vergleichbar. Fälle werden nicht
geändert, die bekannte Leakage aus dem Evaluation-Audit wird im Bericht genannt.

## Messungen

Noch nicht ausgeführt. Ziele sind keine Ergebnisse. Netzwerk-/Modellverfügbarkeit
und die fehlende MP3-Quelle werden getrennt von Implementierungsfehlern ausgewiesen.
