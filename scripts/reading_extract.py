"""HyperExtract's local-template bridge and source-checked candidate staging.

    python3 scripts/reading_extract.py selftest
    <he-python> scripts/reading_extract.py smoke TEMPLATE --text FILE --response JSON
    python3 scripts/reading_extract.py stage SLUG TEMPLATE EXPORT --run NAME

smoke runs the real factory and feed_text with a canned structured model and fake
embeddings: no credentials or network. extract() requires caller-supplied clients;
the caller owns the existing route.py/decision 011 consent and usage recording.
stage consumes extract()'s envelope, never writes Sources/, Wiki/ or a database.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path

import read
from subject import Document, document
from subject import _split

ROOT = Path(__file__).resolve().parents[1]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def native_extract(template: Path, text: str, source_id: str, llm, embedder) -> dict:
    """Explicit clients avoid global defaults; the API accepts local YAML at 0.10.3.

    One document, one instance, bounded concurrency; no search-index construction.
    Do not feed several documents into one KA: its merge loses passage variants.
    """
    from hyperextract.utils.template_engine import Template
    ka = Template.create(str(template.resolve()), "en", llm_client=llm,
                         embedder=embedder, max_workers=1)
    ka.feed_text(text, source_id=source_id)
    return ka.data.model_dump()


def extract(template: Path, doc: Document, llm, embedder, extractor: str) -> dict:
    """Use from an approved, recorded provider adapter; never from auto-init."""
    source_hash, template_hash = digest(doc.path), digest(template)
    if _split(doc.path.read_text(encoding="utf-8")) != (doc.body, doc.offset):
        raise ValueError("cached document changed; resolve it again before extraction")
    data = native_extract(template, doc.body, doc.slug, llm, embedder)
    candidates(data)  # HyperExtract can swallow a chunk schema error into empty data
    if digest(doc.path) != source_hash or digest(template) != template_hash:
        raise ValueError("source or template changed during extraction")
    return {"document": doc.slug, "source_sha256": source_hash,
            "template_sha256": template_hash, "extractor": extractor, "data": data}


def candidates(data: dict) -> list[dict]:
    if not isinstance(data, dict):
        raise ValueError("data must be an object")
    if set(data) == {"items"}:
        rows = data["items"]
        kind = "relation_reading" if rows and isinstance(rows, list) and isinstance(rows[0], dict) and "source" in rows[0] else "reading"
    elif set(data) == {"nodes", "edges"}:
        if not isinstance(data["nodes"], list) or any(
                not isinstance(n, dict) or not isinstance(n.get("name"), str)
                or not n["name"].strip() for n in data["nodes"]):
            raise ValueError("graph nodes must carry names")
        names = {n["name"] for n in data["nodes"]}
        rows = data["edges"]
        kind = "relation"
    else:
        raise ValueError("supported exports: TermReadings items or StatedRelations nodes/edges")
    if not isinstance(rows, list) or not rows:
        raise ValueError("empty or invalid candidate list: not a successful extraction")
    result = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("candidate must be an object")
        required = (("term", "quote", "stance") if kind == "reading" else
                    ("source", "target", "type", "quote", "stance") if kind == "relation_reading" else
                    ("source", "target", "type", "quote"))
        if any(not isinstance(row.get(k), str) or not row[k].strip() for k in required):
            raise ValueError("candidate lacks nonempty string fields: " + ", ".join(required))
        if kind in {"reading", "relation_reading"} and row["stance"] not in {"asserts", "denies", "hedges", "asks", "cites"}:
            raise ValueError("unknown stance")
        if kind == "relation" and (row["source"] not in names or row["target"] not in names):
            raise ValueError("relation endpoint absent from exported nodes")
        result.append({"kind": kind, "raw": row})
    return result


def verify(doc: Document, template: Path, envelope: dict) -> dict:
    if not isinstance(envelope, dict):
        raise ValueError("export must be an object")
    source_hash, template_hash = digest(doc.path), digest(template)
    if _split(doc.path.read_text(encoding="utf-8")) != (doc.body, doc.offset):
        raise ValueError("cached document changed; resolve it again before staging")
    for key, expected in (("document", doc.slug), ("source_sha256", source_hash),
                          ("template_sha256", template_hash)):
        if envelope.get(key) != expected:
            raise ValueError(f"missing or stale {key}; re-extract from current inputs")
    extractor = envelope.get("extractor")
    if not isinstance(extractor, str) or not extractor.strip():
        raise ValueError("extractor/model identifier required")
    rows = candidates(envelope.get("data"))
    seen = set()
    output = []
    for item in rows:
        raw = item["raw"]
        quote = raw["quote"]
        lines = read.locate(doc, quote)
        surfaces = [raw["term"]] if item["kind"] == "reading" else [raw["source"], raw["target"]]
        absent = [s for s in surfaces if not read.locate(doc, s)]
        signature = json.dumps([doc.slug, source_hash, template_hash, extractor,
                                item["kind"], raw, lines], sort_keys=True, ensure_ascii=False)
        identifier = "claim:" + hashlib.sha256(signature.encode()).hexdigest()
        reason = ("joined or shortened quote" if re.search(r"\[.*?\]|…|\.\.\.", quote) else
                  "quote not placed" if not lines else "surface absent from document" if absent
                  else "ambiguous quote: choose its passage" if len(lines) > 1 else None)
        status = "refused" if reason else "duplicate" if identifier in seen else "candidate"
        seen.add(identifier)
        output.append({"id": identifier, **item, "document": doc.slug,
                       "source_sha256": source_hash, "template_sha256": template_hash,
                       "extractor": extractor, "quote_status": "placed" if lines else "unplaced",
                       "lines": lines, "review_status": "unreviewed", "status": status,
                       "reason": reason, "absent_surfaces": absent})
    return {"source_sha256": source_hash, "template_sha256": template_hash,
            "input_rows": len(rows), "candidates": sum(r["status"] == "candidate" for r in output),
            "refused": sum(r["status"] == "refused" for r in output),
            "duplicates": sum(r["status"] == "duplicate" for r in output), "rows": output}


def stage(doc: Document, template: Path, export: Path, run: str) -> int:
    if not re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9_-]{0,79}", run):
        raise ValueError("run must be a simple new name, at most 80 characters")
    raw = export.read_text(encoding="utf-8")
    report = verify(doc, template, json.loads(raw))
    target = ROOT / "Plan/runs" / doc.slug / "hyperextract" / run
    target.mkdir(parents=True, exist_ok=False)  # prior attempts are immutable
    (target / "export.json").write_text(raw, encoding="utf-8")
    (target / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (target / "candidates.jsonl").write_text("".join(
        json.dumps(r, ensure_ascii=False) + "\n" for r in report["rows"]
        if r["status"] == "candidate"), encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "rows"}, ensure_ascii=False))
    print(target.relative_to(ROOT))
    return 1 if report["refused"] or not report["candidates"] else 0


def smoke(template: Path, text: str, response: dict) -> dict:
    """Exercise actual local-file factory, structured schema, extraction and merge."""
    from langchain_core.language_models.chat_models import BaseChatModel
    from langchain_core.embeddings import FakeEmbeddings
    from langchain_core.runnables import RunnableLambda

    class FixtureChat(BaseChatModel):
        @property
        def _llm_type(self):
            return "offline-hyperextract-fixture"

        def _generate(self, *args, **kwargs):
            raise AssertionError("unstructured model call forbidden in smoke test")

        def with_structured_output(self, schema, **kwargs):
            return RunnableLambda(lambda _: schema.model_validate(response))

    return native_extract(template, text, "synthetic-smoke", FixtureChat(), FakeEmbeddings(size=8))


def selftest() -> int:
    global ROOT
    checks = []
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp)
        source = p / "source.md"
        source.write_text("---\ntitle: Fixture\n---\nAlpha steuert Beta.\nVielleicht schützt Alpha Beta.\n", encoding="utf-8")
        doc = Document("fixture", "fixture", "2026-09-30", "md", "", source,
                       "Alpha steuert Beta.\nVielleicht schützt Alpha Beta.\n", 4)
        template = p / "template.yaml"
        template.write_text("synthetic template", encoding="utf-8")
        row = {"term": "Alpha", "quote": "Alpha steuert Beta.", "stance": "asserts"}
        def env(data):
            return {"document": doc.slug, "source_sha256": digest(source),
                    "template_sha256": digest(template), "extractor": "offline-fixture", "data": data}
        good = env({"items": [row]})
        report = verify(doc, template, good)
        checks.append(("real file lines placed", report["rows"][0]["lines"] == [4]))
        checks.append(("placement never promotes meaning", report["rows"][0]["review_status"] == "unreviewed"))
        checks.append(("repeat IDs stable", report == verify(doc, template, good)))
        checks.append(("duplicate visible", verify(doc, template, env({"items": [row, row]}))["duplicates"] == 1))
        checks.append(("invented quote refused", verify(doc, template, env({"items": [{**row, "quote": "Alpha lenkt Beta."}]}))["refused"] == 1))
        checks.append(("invented surface refused", verify(doc, template, env({"items": [{**row, "term": "Gamma"}]}))["refused"] == 1))
        checks.append(("hedge retained", verify(doc, template, env({"items": [{**row, "quote": "Vielleicht schützt Alpha Beta.", "stance": "hedges"}]}))["candidates"] == 1))
        checks.append(("joined quote refused", verify(doc, template, env({"items": [{**row, "quote": "Alpha […] Beta."}]}))["refused"] == 1))
        edge = {"source": "Alpha", "target": "Beta", "type": "controls", "quote": row["quote"]}
        graph = {"nodes": [{"name": "Alpha"}, {"name": "Beta"}], "edges": [edge]}
        checks.append(("native graph shape", verify(doc, template, env(graph))["candidates"] == 1))
        checks.append(("relation stance preserved", verify(doc, template, env({"items": [{**edge, "stance": "denies"}]}))["rows"][0]["raw"]["stance"] == "denies"))
        defects = {"empty": {"items": []}, "bad stance": {"items": [{**row, "stance": "true"}]},
                   "malformed": {"items": [None]}, "dangling edge": {**graph, "nodes": [{"name": "Alpha"}]}}
        for name, data in defects.items():
            try:
                verify(doc, template, env(data))
                checks.append((name + " refused", False))
            except ValueError:
                checks.append((name + " refused", True))
        for key in ("document", "source_sha256", "template_sha256"):
            try:
                verify(doc, template, {**good, key: "stale"})
                checks.append((key + " drift refused", False))
            except ValueError:
                checks.append((key + " drift refused", True))
        export = p / "export.json"
        export.write_text(json.dumps(good), encoding="utf-8")
        original_root = ROOT
        try:
            ROOT = p
            checks.append(("stage writes only trial candidates", stage(doc, template, export, "trial") == 0
                           and (p / "Plan/runs/fixture/hyperextract/trial/candidates.jsonl").is_file()))
            try:
                stage(doc, template, export, "trial")
                checks.append(("prior run cannot be overwritten", False))
            except FileExistsError:
                checks.append(("prior run cannot be overwritten", True))
            try:
                stage(doc, template, export, "../outside")
                checks.append(("run path escape refused", False))
            except ValueError:
                checks.append(("run path escape refused", True))
        finally:
            ROOT = original_root
        source.write_text(source.read_text() + "Alpha steuert Beta.\n", encoding="utf-8")
        doc = Document("fixture", "fixture", "2026-09-30", "md", "", source,
                       "Alpha steuert Beta.\nVielleicht schützt Alpha Beta.\nAlpha steuert Beta.\n", 4)
        checks.append(("ambiguous passage refused", verify(doc, template, env({"items": [row]}))["refused"] == 1))
    for name, held in checks:
        print(("held " if held else "FAIL ") + name)
    print(f"reading_extract: {sum(v for _, v in checks)}/{len(checks)} checks held")
    return int(not all(v for _, v in checks))


def native_selftest() -> int:
    import subprocess
    from templates import he_python
    py = he_python()
    if py is None:
        print("not reached: scripts/install.sh hyperextract", file=sys.stderr)
        return 2
    folder = ROOT / "Plan/hyperextract/fixtures"
    failed = 0
    for name in ("TermReadings", "StatedRelations", "RelationReadings"):
        response = folder / (name + ".json")
        done = subprocess.run([str(py), str(Path(__file__).resolve()), "smoke",
                               str(ROOT / "Plan/hyperextract" / (name + ".yaml")),
                               "--text", str(folder / "reading.txt"), "--response", str(response)],
                              capture_output=True, text=True, timeout=60)
        expected = json.loads(response.read_text())
        # HyperExtract writes logs before the JSON; the last complete output is
        # checked by its exact pretty-printed native structure, not only exit 0.
        held = done.returncode == 0 and done.stdout.rstrip().endswith(
            json.dumps(expected, ensure_ascii=False, indent=2))
        failed += not held
        print(f"{'held' if held else 'FAILED'} {name}: native factory/feed/schema/merge")
        if not held:
            print((done.stdout + done.stderr)[-2000:])
    with tempfile.TemporaryDirectory() as tmp:
        bad = Path(tmp) / "bad.json"
        bad.write_text('{"items":[{"term":"Alpha","quote":null,"stance":"asserts"}]}')
        done = subprocess.run([str(py), str(Path(__file__).resolve()), "smoke",
                               str(ROOT / "Plan/hyperextract/TermReadings.yaml"),
                               "--text", str(folder / "reading.txt"), "--response", str(bad)],
                              capture_output=True, text=True, timeout=60)
        held = done.returncode != 0
        failed += not held
        print(f"{'held' if held else 'FAILED'} malformed structured response refused")
    print(f"reading_extract native: {4 - failed}/4 checks held; synthetic, no model quality measured")
    return int(failed > 0)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("selftest")
    sub.add_parser("native-selftest")
    trial = sub.add_parser("smoke")
    trial.add_argument("template", type=Path)
    trial.add_argument("--text", type=Path, required=True)
    trial.add_argument("--response", type=Path, required=True)
    ingest = sub.add_parser("stage")
    ingest.add_argument("slug")
    ingest.add_argument("template", type=Path)
    ingest.add_argument("export", type=Path)
    ingest.add_argument("--run", required=True)
    args = parser.parse_args()
    try:
        if args.command == "selftest":
            return selftest()
        if args.command == "native-selftest":
            return native_selftest()
        if args.command == "smoke":
            data = smoke(args.template, args.text.read_text(encoding="utf-8"),
                         json.loads(args.response.read_text(encoding="utf-8")))
            candidates(data)  # empty/malformed payload cannot claim success
            print(json.dumps(data, ensure_ascii=False, indent=2))
            return 0
        return stage(document(args.slug), args.template, args.export, args.run)
    except (ValueError, OSError, KeyError) as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
