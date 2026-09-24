"""Build graphify's graph and report from the extraction chunk, as run on 2026-09-24.

graphify's Step 4 for one document, with its own interpreter:
    /root/.local/share/uv/tools/graphifyy/bin/python Plan/runs/<slug>/second-readers/graphify/build_graph.py
Writes graph.json (derived, git-ignored by not being committed) and GRAPH_REPORT.md
beside the chunk. No model is called.
"""
import json
from pathlib import Path

from graphify.analyze import god_nodes, suggest_questions, surprising_connections
from graphify.build import build_from_json
from graphify.cluster import cluster, score_all
from graphify.export import to_json
from graphify.report import generate

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
SLUG = HERE.parents[1].name

extraction = json.loads((HERE / ".graphify_chunk_01.json").read_text(encoding="utf-8"))
G = build_from_json(extraction, root=str(ROOT), directed=False)
communities = cluster(G)
labels = {cid: f"Community {cid}" for cid in communities}
detection = {"total_files": 1, "total_words": 9317, "scan_root": str(ROOT),
             "files": {"document": [f"Sources/drive/{SLUG}.md"]}}
to_json(G, communities, str(HERE / "graph.json"))
report = generate(G, communities, score_all(G, communities), labels, god_nodes(G),
                  surprising_connections(G, communities), detection, {"input": 0, "output": 0},
                  str(ROOT), suggested_questions=suggest_questions(G, communities, labels))
(HERE / "GRAPH_REPORT.md").write_text(report, encoding="utf-8")
print(f"{G.number_of_nodes()} nodes, {G.number_of_edges()} edges, {len(communities)} communities")
