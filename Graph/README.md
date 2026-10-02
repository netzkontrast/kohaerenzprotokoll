# Graph — ein Atlas zum Lesen

[Zum Einstieg](index.md) · [Quellen](sources.md) · [Konflikte](conflicts.md) ·
[Fragen](questions.md) · [Entscheidungen](decisions.md) · [Gezielte Abfragen](queries.md)

Dieser Ordner macht den vorhandenen Graph für Menschen lesbar. Begriffseiten
zeigen Nachbarschaft, Quellenbezüge und offene Punkte. Sie enthalten keine neue
Synthese der Quellen und erklären keine Empfehlung zum Beschluss.

```bash
python3 scripts/knowledge.py init --profile reader
.venv-graphqlite/bin/python scripts/kg.py export
.venv-graphqlite/bin/python scripts/kg.py export --check   # schreibt nichts; scheitert, wenn Graph/ veraltet ist
```

Der Export ist bewusst **eine Dokumentation, kein Datenbank-Abbild**. Es gibt
keinen Import und kein Restore für diese Dateien. Er lässt Quelltexte,
Zeilen-/Absatzknoten, Evidenz-Payloads und vollständige Vorschlagskanten weg.
Die Datenbank entsteht immer aus `Sources/`, `Wiki/` und `Plan/`; `Graph/` wird
von keinem Builder eingelesen. Änderungen hier erzeugen keine Graph-Aussagen.

Quellen werden als Quellenbezüge verlinkt. Für eine konkrete Aussage erst das
benötigte Quellenfenster öffnen und dann die verwendeten Zeilen zitieren. Der
Atlas gibt keine Quellpassagen oder Zeilenlisten auf Vorrat aus. Enthaltene
Wiki-Lesungen, Zitatreferenzen, Konflikte und Empfehlungen bleiben unterscheidbar.

Die erzeugten Seiten tragen einen Generatorhinweis. Statt sie von Hand zu
ändern, die zugrunde liegende Wiki-Seite oder das Entscheidungsblatt korrigieren
und erneut exportieren. `README.md` erklärt die Bedienung; die übrigen Seiten
werden durch `scripts/graph_export.py` geschrieben.

Bei Sitzungsbeginn bereitet der Koordinator die Datenbank vor. Claude führt das
über den SessionStart-Hook aus; Codex folgt `AGENTS.md`. Delegierte Leser nutzen
nur die Check-Form und lesen den Atlas nicht vor eingefrorener unabhängiger
Extraktion. Der Export bleibt explizit, damit ein Sitzungsstart keine
versionierten Leseseiten unnötig umschreibt.

Die spätere Schemaarbeit ist im
[inhaltlichen Graph-Review](../Plan/concept/graph-schema-audit_2026-09-30.md)
priorisiert: Quellspannen statt massenhafter Textstruktur, quellengebundene
Aussagen und Geltungsbereiche, Fragen/Entscheidungsabhängigkeiten sowie
Template-/Prüflauf-Herkunft. Diese Vorschläge sind keine erfundenen Live-Daten.
