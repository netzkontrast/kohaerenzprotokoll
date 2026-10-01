# novelgraph — Index-Layer: Chunks und Vektoren pro Source

**2026-10-01 · Ist-Analyse und Plan, vor dem Code geschrieben.** Auftrag: ein schneller, CPU-only, inkrementeller
Retrieval-Index über alle Sources (BM25, statische Embeddings, hybrid per RRF), der die Provenienz auf Zeilenebene hält.
Kein Modellaufruf, kein Graph, kein ANN, kein Server, kein Ersatz für qmd. Die Messtabelle (§5) wird eingetragen, sobald
gemessen ist; bis dahin steht dort nichts.

## 1. Ist-Analyse

**Ablage.** `Sources/manifest.jsonl` ist das Rückgrat: eine Zeile pro Dokument mit `drive_id`, `title`, `slug`,
`category`, `tier` und, sobald gelandet, `export_path` (`Sources/drive/<slug>.md`) und `sha256`. Gelandet sind alle Zeilen
bis auf `Coherence Protocol.mp3` (`python3 scripts/state.py --get sources.landed`). `Sources/ask/` hält gelandete
`ask`-Antworten (Entscheidung 017); sie sind ausdrücklich **nicht** Teil des Korpus und werden nicht indexiert.

**Slug-Konvention.** Kleinbuchstaben, ASCII, Bindestriche (`2-kohaerenz-protokoll-konzeptentwicklung`); der Slug ist der
Dateiname ohne `.md` und der Schlüssel jeder Zitierung `^[slug.md:Lnn]`.

**Zeilen.** Eine Zitierung nennt die **Dateizeile**, Frontmatter eingeschlossen. Wo das Frontmatter endet, weiß genau
eine Implementierung: `scripts/subject.py` (`Document.offset`). Der Index übernimmt diese Konvention: `line_start` und
`line_end` sind Dateizeilen, 1-basiert, inklusive. Damit ist jeder Treffer direkt mit `python3 scripts/read.py <slug>` und
`quotes.py` prüfbar.

**Was es schon gibt, und warum es nicht reicht.**

| Werkzeug | was es tut | Grenze |
|---|---|---|
| qmd (`.agents/skills/qmd`) | BM25 + Vektoren + Reranker über sieben Collections | Hybrid-Queries dauern auf der CPU Minuten (die Skill-Seite misst 0,22 s BM25 gegen 2 min 41 s reranked) — Modellinferenz zur Query-Zeit |
| `askdb.py` | FTS5 über jede nicht-leere Zeile jedes Dokuments, im GraphQLite-Store | Einheit ist die Zeile, keine Vektoren |
| `graphrag.py` | Seeds per `fold()`, PageRank über den Wiki-Graphen | liefert Wiki-Seiten und ihre Zitate, nie ungelesene Sources |
| `hx.split` | HyperExtracts 2048-Zeichen-Chunks | Zeichen-, nicht Zeilengrenzen; für Verträge, nicht Retrieval |

`docs/README.md` §2.2 plant `chunks` als Teil des Dokument-Schemas („by structure … never across a heading") — dieser
Auftrag baut genau das, außerhalb von `derive.py`, als eigenes Paket.

**Die Benches.**

- `graphrag.py bench` (`state.py`: `graphrag.cases`): Gold sind **Wiki-Seiten**. Ein Index über Source-Chunks gibt keine
  Wiki-Seiten zurück; die Bench ist hier nicht anwendbar.
- `ask.py bench` / `bench_cases()`: dieselben 24 Fälle (Konflikte C*, Fragen Q*), Gold sind die **Dateizeilen**
  `(slug, Lnn)`, die die Konflikt- und Frageseiten zitieren. Das ist die Bench für diesen Index: Recall@8 als
  *Dokument-Recall* (Anteil der Gold-Dokumente unter den Top-8-Chunks) und *Zeilen-Recall* (Anteil der Gold-Zeilen, die in
  einem Top-8-Chunk liegen). Die Fälle werden per Import gelesen, nicht kopiert, und nicht verändert.
  Vorbehalt aus `Plan/concept/evaluation-audit_2026-09-30.md`: das Gold ist zirkulär (92 % sind Zeilen, die auch Wiki-Seiten
  zitieren) und lexikalisch gefunden, BM25 ist also begünstigt; es ist eine Regressionsbench, kein Maß für Entdeckung.
  Zeilen-Recall begünstigt außerdem große Chunks — deshalb wird die mittlere Chunkgröße daneben berichtet.

## 2. Abhängigkeiten zur laufenden Script-Konsolidierung

Das Paket ändert kein bestehendes Script. Es importiert, an genau einer Stelle (`novelgraph/src/novelgraph/repo.py`):

| Helfer | aus | wofür |
|---|---|---|
| `subject.documents()`, `Document.offset`, `read_jsonl`, `write_jsonl` | `scripts/subject.py` | Manifest, Pfade, Frontmatter-Grenze, JSONL |
| `fold()` | `scripts/wiki_index.py` | Oberflächen im `lex/` |
| `bench_cases()` | `scripts/ask.py` | die 24 Bench-Fälle |

Wird einer davon bei der Konsolidierung umbenannt oder verschoben, ist `repo.py` die einzige Datei, die nachzieht.
Einen offenen Konsolidierungs-PR gab es bei Arbeitsbeginn nicht (offen: #136, #76).

## 3. Plan und Entscheidungen

**Layout** wie im Auftrag, unter `Index/` im Repository-Root. Committet: `methods.toml`, `manifest.jsonl`,
`sources/<slug>/source.json`, `chunks/`, `lex/`. Gitignored: `sources/*/vec/` und `_build/`.
*Spannung, offen gelassen:* `CLAUDE.md` sagt „There is no third layer"; `Index/` ist eine abgeleitete Schicht, die
committet wird. Sie wird von keinem Pipeline-Schritt gelesen und ist jederzeit neu baubar (P25) — sie ist ein Cache mit
prüfbaren IDs, keine Wahrheit. Ob sie committet bleiben soll, ist eine Frage an den Autor (§6).

**Tokens.** Gezählt mit einer festen Regex (`\w+|[^\w\s]`), unabhängig vom Embedder, damit ein Wechsel des Modells keine
Chunk-Grenze verschiebt. Die Regel steht versioniert in `methods.toml`.

**Kleinste Einheit ist die Zeile.** Chunk-Zeilen speichern keinen Text, nur einen Zeilenbereich; ein Satz innerhalb einer
Zeile ist deshalb nicht adressierbar. Drive-Exporte schreiben einen Absatz oft als eine Zeile — der Split
„Absätze → Sätze" endet bei Zeilen. Eine einzelne Zeile über `max` bleibt ein Chunk über `max`; wie viele, wird gezählt.

**Chunker v1.**

- `heading@v1`: Abschnitte an Markdown-Überschriften; darin Blöcke (Absatz = Zeilen bis zur Leerzeile; eine Tabelle =
  zusammenhängende `|`-Zeilen, nie geteilt); ein Block über dem Ziel wird zeilenweise geteilt. Packen auf 350–450, min 120,
  max 600; an einer Überschrift wird geschnitten, sobald der laufende Chunk `min` erreicht hat — ein zu kurzer Abschnitt
  wird mit dem nächsten verbunden. `heading_path` ist der Pfad des ersten Inhaltszeile, `prefix` = „Titel › H1 › H2".
- `section@v1`: ein Chunk pro Abschnitt der obersten vorkommenden Überschriftenebene (ein Vorspann vor der ersten
  Überschrift ist eigener Chunk); ohne Überschriften das ganze Dokument.
- `window400@v1`: Zeilenfenster mit ≥ 400 Tokens, Schritt so, dass ~15 % (60 Tokens) überlappen. Baseline.

**Lex.** Pro Chunk die `fold()`-Formen der großgeschriebenen Oberflächen (die Regel von `rules/surfaces.py`: großgeschriebenes
Token) und die Lemmata (simplemma, de+en, deterministisch, kein Modell) mit Häufigkeit. FTS5 bekommt eine Text- und eine
Lemma-Spalte (`unicode61 remove_diacritics 2`), die Anfrage wird ODER-verknüpft, beide Spalten werden gewichtet.

**Embedder.** `potion-m128` = `minishlab/potion-multilingual-128M` über `model2vec`, eingebettet wird
`prefix + "\n" + text`, L2-normiert, float16; die Dimension kommt aus dem Modell. Pro Source liegt eine Matrix in `vec/`,
dazu ein JSON mit `chunk_ids_hash`. Beim Neubau einer Source werden Zeilen unveränderter Chunk-IDs aus der alten Matrix
übernommen, nur neue IDs werden eingebettet.

**Inkrementell.** `Index/manifest.jsonl` hält pro Slug `sha256`; stimmt sie mit der Datei überein und ist der Methodenstand
derselbe, wird die Source übersprungen. `_build/` wird nur neu konkateniert, wenn sich der Stempel (Hash über alle
Chunk-ID-Hashes) geändert hat.

**Suche.** Brute-Force-Skalarprodukt über `np.memmap`; hybrid = Top-50 BM25 + Top-50 Vektor, RRF mit k = 60.

**Umgebung.** uv-Projekt `novelgraph/` mit eigenem `.venv` (gitignored), nie das System-Python.
`uv run --project novelgraph novelgraph …`.

## 4. Was gemessen wird

Die sechs Akzeptanzkriterien des Auftrags; Latenz mit geladenem Modell im Prozess (warm), P50/P95 über 50 Anfragen.

## 5. Messungen

*Noch nicht gemessen.*

## 6. Offene Fragen

*Werden nach der Messung eingetragen.*
