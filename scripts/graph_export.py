"""Human graph atlas: Markdown reading views, deliberately no import/round-trip.

kg.py export writes bounded-topic pages, not a serialized database. Source text,
line/paragraph nodes, evidence payloads and proposal edges are not dumped. The
underlying graph always derives from Sources/Wiki/Plan; Graph/ is output only.
"""
from __future__ import annotations

from collections import Counter, defaultdict
import os
from pathlib import Path
import re
import tempfile

import askdb

ROOT = askdb.ROOT
DIRECTORY = ROOT / "Graph"
MARKER = "<!-- generated: graph_export -->\n"


def text(value):
    return str(value if value is not None else "nicht angegeben").replace("\n", " ").replace("|", "\\|")


def relative(path, depth=0):
    return "../" * (depth + 1) + path


def title(node):
    return text(node.get("term") or node.get("subject") or node.get("question") or node.get("title") or node.get("slug") or node["id"])


def link(node, depth=0):
    if node["type"] == "term":
        return f"[{title(node)}]({'../' if depth else ''}terms/{node['slug']}.md)"
    path = node.get("path")
    if path:
        return f"[{title(node)}]({relative(path, depth)})"
    if node["type"] == "doc":
        return f"[{title(node)}]({relative('Sources/drive/' + node['slug'] + '.md', depth)})"
    return title(node)


def render(core, heads=None, ledger=None, stats=None):
    """A lossy, reading-oriented projection; no machine manifest or hidden dump."""
    nodes, edges = core["nodes"], core["edges"]
    heads, ledger, stats = heads or {}, ledger or [], stats or {}
    terms = sorted((n for n in nodes.values() if n["type"] == "term"), key=lambda n: title(n).casefold())
    docs = sorted((n for n in nodes.values() if n["type"] == "doc"), key=lambda n: title(n).casefold())
    by_source, by_target = defaultdict(list), defaultdict(list)
    for edge in edges:
        by_source[edge["source"]].append(edge)
        by_target[edge["target"]].append(edge)
    pages = {}
    intro = ["# Graph lesen", "", "Dieser Atlas zeigt Beziehungen im vorhandenen Wiki und Plan.",
             "Er entscheidet keine Quellenposition und ersetzt keine unabhängige Quellenlektüre.",
             "Quellpassagen werden erst für eine konkrete Frage geöffnet und gegebenenfalls zitiert.", "",
             "## Einstieg", "", "- [Begriffe](#begriffe): Nachbarschaft, Quellenbezug und offene Punkte je Begriff.",
             "- [Quellenbezüge](sources.md): Welche Wiki-Seiten welche Quellen lesen oder zitieren.",
             "- [Konflikte](conflicts.md): Dokumentierte Unterschiede, ohne sie aufzulösen.",
             "- [Fragen und ihr Status](questions.md): Frage, Status und betroffene Begriffe.",
             "- [Entscheidungen und Abhängigkeiten](decisions.md): Offene Weichen getrennt von Entscheidungsakten.",
             "- [Entdeckungshinweise](discovery.md): Was statistische Muster leisten und was nicht.",
             "- [Gezielt nachfragen](queries.md): Kleine CLI-Abfragen statt des gesamten Graphen.", "",
             "## Begriffe", "", "| Begriff | Wiki-Status | Referenzierte Quellen | Konflikt-/Fragenbezüge |", "|---|---|---|---|"]
    for n in terms:
        outgoing = by_source[n["id"]]
        sources = {e["target"] for e in outgoing if e["type"] in ("reads", "cites")}
        open_nodes = {e["source"] for e in by_target[n["id"]] if e["type"] in ("contests", "raised_by")}
        intro.append(f"| {link(n)} | {text(n.get('status'))} | {len(sources)} | {len(open_nodes)} |")
        body = [f"# {title(n)}", "", f"[Wiki-Seite lesen]({relative(n['path'], 1)}) · [Alle Begriffe](../index.md)",
                "", f"**Wiki-Status:** {text(n.get('status'))}.",
                "", "**Schreibweisen im Index:** " + ", ".join(text(x) for x in n.get("surfaces", [])) + ".", "",
                "## Verknüpfte Begriffe", "", "Wiki-Verlinkungen zeigen eine Verbindung zwischen Seiten; sie behaupten keine Gleichheit oder Kausalität.", ""]
        nearby = {e["target"] for e in outgoing if e["type"] == "links"}
        nearby |= {e["source"] for e in by_target[n["id"]] if e["type"] == "links"}
        body += [f"- {link(nodes[key], 1)}" for key in sorted(nearby) if key in nodes]
        if not nearby:
            body.append("Keine Wiki-Verlinkung im Graph erfasst.")
        body += ["", "## Konflikte und Fragen", ""]
        body += [f"- {link(nodes[key], 1)} — {text(nodes[key].get('status'))}." for key in sorted(open_nodes) if key in nodes]
        if not open_nodes:
            body.append("Keine Konflikt- oder Fragenbeziehung erfasst; das ist keine Vollständigkeitsprüfung des Begriffs.")
        body += ["", "## Quellenbezug", "", "Eine enthaltene Lesung und eine Zitatreferenz sind unterschiedliche Beziehungen.",
                 "Keine dieser Markierungen erklärt die Quellenposition zur verbindlichen Aussage.", "",
                 "| Quelle | Datum | Lesung im Wiki enthalten | Im Wiki zitiert |", "|---|---|---|---|"]
        for source in sorted(sources):
            if source not in nodes:
                continue
            kinds = {e["type"] for e in outgoing if e["target"] == source}
            body.append(f"| {link(nodes[source], 1)} | {text(nodes[source].get('date'))} | {'ja' if 'reads' in kinds else '—'} | {'ja' if 'cites' in kinds else '—'} |")
        if not sources:
            body.append("\nKeine Quellenbeziehung im Graph erfasst.")
        pages[f"terms/{n['slug']}.md"] = "\n".join(body) + "\n"
    pages["index.md"] = "\n".join(intro) + "\n"

    source_page = ["# Quellenbezüge", "", "Hier stehen ausschließlich im Wiki referenzierte Quellen, nicht der gesamte gelandete Korpus.",
                   "Lesen und Zitieren sind getrennt aufgeführt. Die Tabelle misst keine Reconciliation oder Freigabe.", "",
                   "| Quelle | Datum | Enthaltene Wiki-Lesungen | Zitatbezüge |", "|---|---|---|---|"]
    for doc in docs:
        incoming = by_target[doc["id"]]
        read = sorted({e["source"] for e in incoming if e["type"] == "reads"})
        cited = sorted({e["source"] for e in incoming if e["type"] == "cites"})
        names = lambda keys: ", ".join(link(nodes[key]) for key in keys if key in nodes)
        source_page.append(f"| {link(doc)} | {text(doc.get('date'))} | {names(read) or '—'} | {names(cited) or '—'} |")
    pages["sources.md"] = "\n".join(source_page) + "\n"
    for kind, filename, heading, relationship in (("conflict", "conflicts.md", "Dokumentierte Konflikte", "contests"),
                                                  ("question", "questions.md", "Fragen und ihr Status", "raised_by")):
        rows = [f"# {heading}", "", "Der Status stammt aus dem jeweiligen Wiki-Record. Die Darstellung trifft keine Entscheidung.", ""]
        for n in sorted((n for n in nodes.values() if n["type"] == kind), key=lambda n: n["id"]):
            related = [e["target"] for e in by_source[n["id"]] if e["type"] == relationship]
            rows += [f"## {title(n)}", "", f"**Status:** {text(n.get('status'))}. [Record lesen]({relative(n['path'])}).", "",
                     "**Betroffene Begriffe:** " + (", ".join(link(nodes[x]) for x in sorted(set(related)) if x in nodes) or "nicht erfasst") + ".", ""]
            if kind == "question":
                records = [nodes[e["target"]] for e in by_source[n["id"]] if e["type"] == "concerns" and e["target"] in nodes]
                sources = [nodes[e["target"]] for e in by_source[n["id"]] if e["type"] == "asks" and e["target"] in nodes]
                rows += ["**Benannte Konflikte:** " + (", ".join(link(x) for x in records) or "keine") + ".",
                         "", "**Benannte Quellen:** " + (", ".join(link(x) for x in sources) or "keine") + ".", ""]
        pages[filename] = "\n".join(rows) + "\n"

    decision = ["# Entscheidungen und Abhängigkeiten", "", "## Entscheidungsblätter und Status", "",
                "Empfehlungen sind Vorschläge. Nur der dokumentierte Status des Blatts sagt, ob es beantwortet ist.", "",
                "| Blatt | Status | Hängt ab von | Empfehlung, nicht Beschluss |", "|---|---|---|---|"]
    for key, h in sorted(heads.items()):
        decision.append(f"| [{text(key)}]({relative(h['file'])}) | {text(h.get('status'))} | {', '.join(text(x) for x in h.get('deps', [])) or '—'} | {text(h.get('empfehlung'))} |")
    decision += ["", "## Entscheidungsakten", "", "Die verlinkten Akten enthalten das Urteil und seine Reichweite; ein Dateiname ist keine Freigabe für andere Aussagen.", ""]
    decision += [f"- [{text(label)}]({relative(path)})" for path, label in ledger]
    pages["decisions.md"] = "\n".join(decision) + "\n"
    labels, types = stats.get("labels", {}), stats.get("types", {})
    pages["discovery.md"] = f"""# Entdeckungshinweise

Statistische Muster helfen, eine Stelle zum Lesen zu finden. Sie entscheiden
keine Beziehung zwischen Figuren oder Begriffen und erklären keine Position
zum Kanon. Diese Seite bildet keine einzeln gezählten Quellzeilen ab.

| Muster im Index | Erfasste Größe | Was es aussagt |
|---|---|---|
| Benannte Oberflächen | {labels.get('Entity', 'nicht gemessen')} Entity-Knoten | Namen aus geprüften Kandidatenlisten; noch keine Identitätsentscheidung |
| Namensvorkommen | {types.get('P_NAMES', 'nicht gemessen')} Fundbeziehungen | Die Oberfläche steht in einer Quelle; Bedeutung bleibt zu lesen |
| Statistische Gruppen | {labels.get('Hyperedge', 'nicht gemessen')} Hyperedge-Knoten | Gemeinsames Vorkommen oder geteilte Textsegmente als Suchhinweis |

`cooccur` misst gemeinsames Vorkommen; `parallel` gruppiert geteilte Textsegmente.
Beides ist berechnet, nicht durch ein Modell als Tatsache gelernt. Ein Muster
kann eine Recherche priorisieren, aber keine offene Frage automatisch beantworten.
Für konkrete Fundstellen die Quellenfenster gezielt öffnen; nicht die gesamten
Zeilen- und Absatzbeziehungen als vermeintliches Wissen lesen.
"""
    pages["queries.md"] = """# Gezielt nachfragen

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
"""
    return {path: MARKER + body for path, body in pages.items()}


def pages_for(db=askdb.DB):
    """The atlas as it should read now: refuses a stale store or a store whose graph differs from the files."""
    import graph, kg
    hashes = askdb.inputs()
    kg.freshness(db)
    core = kg.read_graph(db)
    if core != graph.build():
        raise ValueError("core graph differs from authoritative files: rebuild before export")
    ledger = []
    for path in sorted((ROOT / "Plan/decisions").glob("*.md")):
        heading = next((line[2:] for line in path.read_text(encoding="utf-8").splitlines() if line.startswith("# ")), path.stem)
        ledger.append((str(path.relative_to(ROOT)), heading))
    pages = render(core, askdb.sheet_heads(), ledger, askdb.stats(db))
    if askdb.inputs() != hashes:
        raise ValueError("inputs changed during export")
    return core, pages


def drift(pages, directory=DIRECTORY):
    """What the committed atlas lacks, has wrong, or keeps that the renderer would remove (pages it owns only)."""
    problems = []
    for path, content in sorted(pages.items()):
        target = directory / path
        if not target.exists():
            problems.append(f"missing: {path}")
        elif target.read_text(encoding="utf-8") != content:
            problems.append(f"stale: {path}")
    for target in sorted((directory / "terms").glob("*.md")):
        rel = str(target.relative_to(directory))
        if rel not in pages and target.read_text(encoding="utf-8").startswith(MARKER):
            problems.append(f"orphaned: {rel}")
    return problems


def check(db=askdb.DB, directory=DIRECTORY):
    """`kg.py export --check`: fail when Graph/ is not what an export would write now (SPEC.md step 3)."""
    _, pages = pages_for(db)
    problems = drift(pages, directory)
    return {"status": "current" if not problems else "stale", "pages": len(pages), "problems": problems}


def export(db=askdb.DB, directory=DIRECTORY):
    import kg
    core, pages = pages_for(db)
    directory.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".graph-export-", dir=directory.parent) as staged:
        staging = Path(staged)
        for path, content in pages.items():
            target = staging / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
        kg.freshness(db)
        for path in [p for p in pages if p != "index.md"] + ["index.md"]:
            target = directory / path
            target.parent.mkdir(parents=True, exist_ok=True)
            os.replace(staging / path, target)
    # Only remove stale pages demonstrably owned by this renderer.
    for path in (directory / "terms").glob("*.md"):
        if str(path.relative_to(directory)) not in pages and path.read_text(encoding="utf-8").startswith(MARKER):
            path.unlink()
    return {"status": "exported", "kind": "human-markdown", "pages": len(pages), "importable": False,
            "terms": sum(n['type'] == 'term' for n in core['nodes'].values()),
            "bytes": sum(len(s.encode()) for s in pages.values())}
