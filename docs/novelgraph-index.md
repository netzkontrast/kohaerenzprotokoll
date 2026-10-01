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

## Übernommene Hinweise aus dem parallelen PR #138

Das uv-Projekt bleibt in `novelgraph/`; sein einziges venv liegt jetzt im
Repository-Root, damit `qmd_coverage.py` installierte Paket-READMEs wie die
anderen venvs ausschließt. Installation:

```sh
UV_PROJECT_ENVIRONMENT=$PWD/.venv-novelgraph uv sync --project novelgraph
.venv-novelgraph/bin/novelgraph build --method heading@v1
.venv-novelgraph/bin/novelgraph build --method section@v1
.venv-novelgraph/bin/novelgraph build --method window400@v1
.venv-novelgraph/bin/novelgraph verify
.venv-novelgraph/bin/novelgraph measure
```

FTS5 wird mit `content=''` gebaut: keine zweite Ablage des Source-Texts, keine
Payload-Kopie in der FTS-Tabelle. `rowid - 1` adressiert dieselbe Zeile der
Vektormatrix und `rows.jsonl`; Treffer-Metadaten werden aus den Source-Chunks
bezogen. `verify` leitet die erwarteten Postings unabhängig neu ab und vergleicht
ihren SHA256 sowie die vollständige Zeilenordnung. Ein negativer Test ersetzt
sämtliche Postings durch andere Begriffe bei gleicher Zeilenzahl und muss scheitern.
Die vorhandenen Provenienz-, Coverage-, Matrixwert- und Freshness-Gates bleiben.

Lex-Oberflächen und echte simplemma-Lemmata sind sortierte, eindeutige,
leerzeichengetrennte Zeichenketten statt großer JSON-Arrays. Das ändert nicht die
bisherige Termfrequenz-Semantik (ein Vorkommen pro Term in dieser Zusatzspalte).
Der Registry-Stand ist `lex.version=3`; bestehende Vektoren werden anhand ihrer
Chunk-ID und des vollständigen Eingabetext-Hashes wiederverwendet.
`lex/` bleibt entsprechend dem Auftrag committed; die Ignore-Entscheidung in
#138 ist keine Änderung des hier erteilten Auftrags.

Die Bench meldet zusätzlich die theoretische Dokument-Recall-Obergrenze bei
acht Treffern, pro Fall `min(8, gold_documents) / gold_documents`, sowie die
mittlere Zahl Source-Zeilen pro Treffer. Diese Obergrenze gilt für Dokument-,
nicht Zeilen-Recall. Große `section`-Chunks haben mehr Kontext und dürfen daher
nicht allein anhand höherer Zeilen-Recall als bessere Retrieval-Methode gelten.
Bench-Fragen und Gold bleiben unverändert. Die bekannten lexikalischen/circularen
Labels messen Regression, nicht unabhängig geprüfte Entdeckung.
