# novelgraph — Index-Layer: Chunks und Vektoren pro Source

**2026-10-01 · §1–§4 vor dem Code geschrieben (Commit `bb07a10`), §3a, §5 und §6 nach der Messung.** Auftrag: ein schneller,
CPU-only, inkrementeller Retrieval-Index über alle Sources (BM25, statische Embeddings, hybrid per RRF), der die Provenienz
auf Zeilenebene hält. Kein Modellaufruf, kein Graph, kein ANN, kein Server, kein Ersatz für qmd.

```bash
UV_PROJECT_ENVIRONMENT=$PWD/.venv-novelgraph uv sync --project novelgraph   # einmal: das venv aus novelgraph/uv.lock
.venv-novelgraph/bin/novelgraph build                 # inkrementell; --source SLUG, --method heading@v1, --force
.venv-novelgraph/bin/novelgraph search "Wie hängen die Guardians mit AEGIS zusammen?" [-k 8] [--mode bm25|vec|hybrid]
.venv-novelgraph/bin/novelgraph verify                # Coverage-Gate, IDs, Bereiche, Matrixzeilen
.venv-novelgraph/bin/novelgraph bench --record DIR    # Recall@k, Latenz, Größen
.venv-novelgraph/bin/novelgraph selftest
```

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

**Umgebung.** uv-Projekt `novelgraph/` (`pyproject.toml`, `uv.lock`) mit einem venv, nie das System-Python. *Abweichung nach dem
Bauen:* das venv liegt als `.venv-novelgraph/` im Repository-Root, nicht in `novelgraph/.venv` — wie jedes venv hier (`.venv-dspy`,
`.venv-graphqlite`), und weil `qmd_coverage.py` nur `.venv*` an der Wurzel als Abhängigkeit kennt: im Paketordner färbte es
den CI-Selbsttest mit den Markdown-Dateien der installierten Pakete rot.

## 3a. Was beim Bauen anders entschieden wurde — und warum

| Entscheidung | Grund |
|---|---|
| **Embedding-Cache-Schlüssel = Chunk-ID + sha1(prefix)[:8]** (`build.vec_key`); die ID-Formel selbst bleibt wie spezifiziert | Die ID deckt Text und Zeilenbereich ab, nicht den `prefix` — eingebettet wird aber `prefix + "\n" + text`. Eine umbenannte Überschrift hätte einen veralteten Vektor behalten. Gemessen: die Bereinigung der Überschriften (unten) änderte 59 Präfixe, und genau 59 Chunks wurden neu eingebettet, 91 übernommen. |
| **`[headings]` in `methods.toml`** und im Methodenstempel | Code, der eine Überschrift anders liest, ändert `heading_path` und `prefix`. Der erste Versuch, Drive-Escapes (`2\.`, `F\&E`, `-\>`, `\~27`) zu entfernen, wurde vom Build nicht bemerkt — der Stempel kam nur aus der Registry. Jetzt ist die Regel dort benannt; eine Änderung an ihr ist eine neue Version. |
| **`lex/` als Zeichenketten** (`"surfaces": "a b c"`, `"lemmata": "x y:3"`) statt JSON-Objekt | Die Objektform machte `lex/` 104 MB für drei Chunker, viermal das Korpus. Die Zeichenkette: 72 MB roh, ~19 MB gzip. |
| **FTS5 contentless** (`content=''`, rowid = Matrixzeile + 1) | Mit gespeichertem Text war `_build/` 260 MB; der Text ist ohnehin ein Slice der Source. Jetzt 82 MB. |
| **Modell gepinnt** auf Revision `73908c3` und lokal zuerst geladen | Ein Modellwechsel unter demselben Namen würde stumm andere Vektoren erzeugen. |
| **Der Zeilenschnitt prüft auch `max`** | Ein langer Absatz wurde zwischen Zeilen geschnitten, aber erst ab 350 Tokens gegen das Ziel 450 geprüft, nie gegen 600 — fünf Chunks lagen über `max`, obwohl sie teilbar waren (z. B. 279 + 312 + 110 …). Gefunden beim Prüfen der eigenen Größentabelle; jetzt ein Selbsttest. |
| **Sources werden für den Inkrement-Test nicht verändert** | `Sources/drive/` ist unveränderlich; der Test lief auf einer Kopie des Repositorys im Scratchpad (Kriterium 3). |

**Sprache.** `de` bei einer deutschen Stoppwort-Mehrheit von mehr als 2 : 1, `en` umgekehrt, sonst `mixed` — die Reihenfolge der
Lemmatisierer-Sprachen, nichts weiter.

## 4. Was gemessen wird

Die sechs Akzeptanzkriterien des Auftrags; Latenz mit geladenem Modell im Prozess (warm), P50/P95 über 50 Anfragen
(die 24 Bench-Fragen, dann Namen von Termseiten in Dateireihenfolge — fest, damit ein zweiter Lauf dasselbe fragt).
Die Rohdaten: `Plan/runs/novelgraph-index-2026-10-01/bench.json` (k = 8) und `bench-k50.json`.

## 5. Messungen

Gemessen am 2026-10-01 in einem Cloud-Container (4 CPUs, 15 GB), auf dem Korpus von `main` bei `b6ec523`.

| # | Kriterium | Ziel | gemessen | |
|---|---|---|---|---|
| 1 | voller Build, `verify` grün, Coverage | fehlerfrei, 100 % | voller Build mit `--force` 2 min 39 s (586 Sources, 31 366 Chunks eingebettet), `verify` ok, **586/586 = 100 %** | ✓ |
| 2 | Rebuild ohne Änderung | < 10 s, 0 Chunks eingebettet | **1,0–1,2 s**, 0 eingebettet, 1758 von 1758 Source×Methode übersprungen | ✓ |
| 3 | eine Source geändert | nur sie neu eingebettet | auf einer Kopie, eine Zeile von `2-kohaerenz-protokoll-konzeptentwicklung` verlängert: 1 Source neu gechunkt, **3 Chunks eingebettet** (einer pro Methode), 92 Vektoren übernommen, 1755 übersprungen; 25 s gesamt, fast ganz Modellladen und der Neuaufbau von `_build/` (alle drei Methoden) | ✓ |
| 4 | Latenz `search` hybrid, warm, 50 Anfragen | P50/P95 < 100 ms | `heading@v1` **P50 4,7 ms, P95 28,5 ms** (max 43); `section@v1` 1,9 / 9,9; `window400@v1` 6,3 / 47,4 | ✓ |
| 5 | Recall@8 je Modus und Chunker | berichten | Tabelle unten | — |
| 6 | Größen | berichten | Tabelle unten | — |

**Kalt ist nicht warm.** Ein einzelner CLI-Aufruf `novelgraph search` dauert ~15 s, fast ganz das Laden des Modells
(0,5 GB safetensors). Das 100-ms-Ziel gilt im laufenden Prozess; ein Server ist ausdrücklich Nicht-Ziel (§6, Frage 2).

### Recall@8 auf den 24 Fällen von `ask.py bench_cases()`

*Dokument* = Anteil der Gold-Dokumente unter den Top-8; *Decke* = was 8 Treffer höchstens erreichen können (ein Fall hat
im Median 24,5 Gold-Dokumente, 8 Chunks treffen höchstens 8); *Zeile* = Anteil der Gold-Zeilen innerhalb eines Top-8-Chunks;
*Zeilen/Treffer* = mittlere Größe eines zurückgegebenen Chunks, ohne die *Zeile* nicht lesbar ist.

| Chunker | Modus | Dokument @8 | Decke @8 | Zeile @8 | Zeilen/Treffer | Dokument @50 | Zeile @50 |
|---|---|---|---|---|---|---|---|
| `heading@v1` | bm25 | 0,066 | 0,427 | 0,034 | 13,7 | 0,233 | 0,115 |
| `heading@v1` | vec | 0,067 | 0,427 | 0,022 | 11,9 | 0,173 | 0,052 |
| `heading@v1` | hybrid | **0,068** | 0,427 | 0,032 | 13,4 | 0,229 | 0,104 |
| `section@v1` | bm25 | 0,064 | 0,427 | 0,067 | 368,7 | 0,245 | 0,219 |
| `section@v1` | vec | 0,032 | 0,427 | 0,035 | 206,6 | 0,168 | 0,149 |
| `section@v1` | hybrid | 0,047 | 0,427 | 0,050 | 327,2 | 0,209 | 0,185 |
| `window400@v1` | bm25 | 0,049 | 0,427 | 0,021 | 18,9 | 0,191 | 0,079 |
| `window400@v1` | vec | 0,046 | 0,427 | 0,014 | 16,0 | 0,144 | 0,042 |
| `window400@v1` | hybrid | 0,056 | 0,427 | 0,018 | 18,1 | 0,192 | 0,074 |

Gelesen, ohne mehr hineinzulegen:

- **Bei k = 8 liegen alle drei Modi von `heading@v1` innerhalb von 0,002**; über 24 Fälle ist das kein Unterschied (die
  Evaluations-Revision schätzt die kleinste nachweisbare Differenz auf dieser Bench auf etwa 0,027).
- **Bei k = 50 trennt es sich:** BM25 und hybrid ~0,23, Vektoren allein 0,17. Hybrid hebt BM25 auf dieser Bench nicht.
  Das Gold ist lexikalisch gefunden (Evaluations-Revision §2) — die Bench begünstigt BM25, sie sagt nicht, dass Vektoren
  nichts finden, was ein Leser brauchen würde.
- **`heading@v1` schlägt die Fenster-Baseline** in jedem Modus bei k = 8 (Dokument 0,068 gegen 0,056 hybrid), bei gleicher
  Treffergröße (13 gegen 18 Zeilen).
- **`section@v1` gewinnt Zeilen-Recall nur durch Größe**: ein Treffer ist im Mittel 300+ Zeilen und ~6 500 Tokens — als
  Kontext für einen Leser unbrauchbar, als Vektor ein Mittelwert über ein halbes Dokument (vec fällt dort am stärksten ab).
- **Gegen `ask.py bench` nicht vergleichbar**: dessen Pakete halten bis zu 60 000 Zeichen aus fünf Findern, hier sind es 8 Chunks.

### Größen

| | `heading@v1` | `section@v1` | `window400@v1` |
|---|---|---|---|
| Chunks | 15 339 | 795 | 15 232 |
| Tokens, Mittel / Median | 337 / 345 | 6 505 / 5 143 | 439 / 425 |
| über `max` (600) | 193: 156 Tabellen (nie geteilt), 37 eine einzelne Zeile (32 davon mit ihrer Überschrift) | — | — |
| unter `min` (120) | 16: 2 ganze Dokumente, die kürzer sind; 14 zwischen zwei Nachbarn, mit denen zusammen sie `max` überschritten hätten (meist Tabellen) | — | — |

| Ort | MB | in Git |
|---|---|---|
| `Index/sources/*/chunks/` | 16,4 (gzip ~2) | ja |
| `Index/sources/*/lex/` | 71,7 (gzip ~19) | ja |
| `Index/sources/*/source.json` | 1,3 | ja |
| `Index/sources/*/vec/` | 17,6 (Dimension 256, float16) | nein |
| `Index/_build/` | 81,8 (davon FTS5 62, Matrizen 16) | nein |
| Modell im HF-Cache | ~500 | nein |

## 6. Offene Fragen

1. **Soll `lex/` committet bleiben?** Es ist eine reine Funktion von Source, `fold()` und simplemma und in ~60 s neu gebaut;
   in Git kostet es ~19 MB komprimiert — `.git` ist heute 55 MB — und jede Versionsänderung der Lex-Regel noch einmal so viel.
   Committet, weil der Auftrag es so sagt. Die Alternative: nur `chunks/` und `source.json` committen (IDs prüfbar, ~2 MB).
2. **Kaltstart.** Ein CLI-Aufruf lädt 0,5 GB Modell (~15 s). Ein residenter Prozess wäre ein Server (Nicht-Ziel); ein kleineres
   Modell (`potion-base-8M`, englisch) ist schneller, aber nicht mehrsprachig. Offen, bis klar ist, wer `search` aufruft.
3. **`CLAUDE.md` sagt „There is no third layer".** `Index/` ist eine abgeleitete, teils committete Schicht. Sie wird von keinem
   Pipeline-Schritt gelesen; ob sie so bleiben darf, entscheidet der Autor.
4. **Eine unabhängige Bench.** Die 24 Fälle sind zirkulär und lexikalisch (Evaluations-Revision §0); ob Vektoren etwas finden,
   was BM25 nicht findet, kann diese Bench nicht zeigen. Der Weg dorthin steht in der Revision §3 (Pooling, Urteile des Autors).
5. **Tabellen und lange Zeilen sind nicht teilbar.** 193 `heading@v1`-Chunks liegen über 600 Tokens — 156 Tabellen, die der Auftrag
   nie zu teilen verlangt, und 37 Zeilen, weil ein Drive-Absatz eine Zeile ist und ein Satz darin keine Adresse hat.
   Zeichen-Offsets im Chunk würden das lösen und die Regel „ein Treffer ist ein Zeilenbereich" aufweichen.
6. **Zusammenführung mit `docs/README.md` §2.2** — dort sind strukturelle Chunks als Teil des Dokument-Schemas in `derive.py`
   geplant. Ob `heading@v1` diese Regel wird oder daneben bleibt, hängt an der Script-Konsolidierung (§2).
