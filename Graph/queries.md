<!-- generated: graph_export -->
# Gezielt nachfragen

Vom Repository-Root aus, nachdem der Koordinator initialisiert hat:

```bash
.venv-graphqlite/bin/python scripts/kg.py context "AEGIS und Entropie" --max-bytes 12000
.venv-graphqlite/bin/python scripts/kg.py around term:aegis --hops 1 --limit 12
.venv-graphqlite/bin/python scripts/kg.py search "Juna" --limit 6
.venv-dspy/bin/python scripts/askdb.py touches <quellen-slug>
python3 scripts/read.py <quellen-slug> --from 120 --to 135
```

Kontext liefert überprüfte Belege, Konflikte und Fragen; keine neue Entscheidung.
Ein Quellenfenster wird erst für eine konkrete Frage geöffnet. Die Zeilen einer
verwendeten Aussage zitieren, nicht jede mögliche Fundstelle auf Vorrat.
Unabhängige Quellenleser verwenden den Atlas erst nach eingefrorener Extraktion.

Der Atlas ist zum Lesen und Verlinken. Es gibt keinen Import und kein Restore
für diese Markdown-Dateien. Ihre Bearbeitung verändert keine Graph-Aussage.
