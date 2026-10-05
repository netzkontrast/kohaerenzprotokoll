"""HyperExtract's extraction, ported (`hx.py`), and source-checked candidate staging.

    python3 scripts/reading_extract.py selftest
    python3 scripts/reading_extract.py native-selftest
    python3 scripts/reading_extract.py smoke TEMPLATE --text FILE --response JSON
    python3 scripts/reading_extract.py stage SLUG TEMPLATE EXPORT --run NAME

smoke runs the template's real prompt, schema, chunks and merge with a canned reply: no credentials or network.
extract() requires a caller-supplied model (`he_claude.Claude`); the caller owns decision 011's consent and the usage
record. stage consumes extract()'s envelope, never writes Sources/, Wiki/ or a database. Standard library only:
HyperExtract's engine is `hx.py`, the installed upstream package only checks it (`hx.py parity`).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path

import quotes
import read
from subject import Document, document
from subject import _split

ROOT = Path(__file__).resolve().parents[1]

# A contract's word for "the text gives no name" (`Utterances`: a line nobody tags). It stands in no
# document and is never looked for in one; it names no page either.
NO_NAME = {"unlabelled"}


def stands(doc: Document, name: str) -> bool:
    """Whether a name is in the document. A quotation of it is (`read.locate`); a name under four
    characters is not a quotation — `quotes.parts_of` drops fragments that short, so `Lex`, `Nyx`, `Lia`
    and `KW1` could never be found — and stands when it is a word on its own on some line. A name of
    four characters or more is judged as it always was, so no row a stage accepted changes."""
    if name in NO_NAME or read.locate(doc, name):
        return True
    clean = quotes.normalise(name).strip()
    if not clean or len(clean) >= 4:
        return False
    alone = re.compile(r"(?<![\w-])" + re.escape(clean) + r"(?![\w-])")
    return any(alone.search(quotes.normalise(line)) for line in doc.lines())


# A contract tagged `heading-scoped` (ChapterCards, 2026-10-05) may name the chapter in the heading above
# the quoted line rather than in the line itself: outlines write `### Chapter 8: …` and the fields beneath.
# The model is not believed about which heading that is: code walks up from the placed line to the
# nearest heading and asks whether it names the row's chapter, so a field cannot be moved to a neighbour.
HEADING = re.compile(r"^\s*(#{1,6}\s|\*\*[^*].*\*\*\s*$)")


def heading_scoped(template: Path) -> bool:
    try:
        text = template.read_text(encoding="utf-8")
    except OSError:
        return False
    return bool(re.search(r"^tags:.*\bheading-scoped\b", text, re.M))


def _plain(text: str) -> str:
    return " ".join(re.sub(r"[*#\\_`]", " ", text).lower().split())


def names_chapter(line: str, chapter: str) -> bool:
    want = _plain(chapter)
    return bool(want) and re.search(r"(?<!\w)" + re.escape(want) + r"(?![\w])", _plain(line)) is not None


def under_heading(doc: Document, line: int, chapter: str) -> bool:
    """Whether the placed line, or the nearest heading above it, names the chapter."""
    rows = doc.lines()
    index = line - doc.offset
    if not 0 <= index < len(rows):
        return False
    if names_chapter(rows[index], chapter):
        return True
    for above in range(index - 1, -1, -1):
        if HEADING.match(rows[above]):
            return names_chapter(rows[above], chapter)
    return False


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def native_extract(template: Path, text: str, ask, log: list | None = None) -> dict:
    """One document, one template, one chunk after another (`hx.extract`); a chunk whose reply failed is dropped.
    `log`, when given, receives one entry per chunk (its size, and whether its reply validated).
    Do not feed several documents into one run: each run is one document's record."""
    import hx
    data, chunks = hx.extract(hx.load(template), text, ask)
    if log is not None:
        log.extend(chunks)
    return data


def extract(template: Path, doc: Document, ask, extractor: str, text: str | None = None,
            log: list | None = None, keep: dict | None = None) -> dict:
    """Use from an approved, recorded provider adapter; never from auto-init.

    `text` is what the model is sent when it is less than the whole body (`hegraph.gate`: the paragraphs that hold a
    cue of the contract). Every quotation is still placed against the whole document, so a gated run cannot cite
    what the document does not hold."""
    source_hash, template_hash = digest(doc.path), digest(template)
    if _split(doc.path.read_text(encoding="utf-8")) != (doc.body, doc.offset):
        raise ValueError("cached document changed; resolve it again before extraction")
    data = native_extract(template, doc.body if text is None else text, ask, log)
    if keep is not None:      # the merged data, kept even when the check below refuses it
        keep["data"] = data
    candidates(data)  # a run whose every chunk failed merges to empty data
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
    scoped = heading_scoped(template)
    seen = set()
    output = []
    for item in rows:
        raw = item["raw"]
        quote = raw["quote"]
        lines = read.locate(doc, quote)
        surfaces = [raw["term"]] if item["kind"] == "reading" else [raw["source"], raw["target"]]
        absent = [s for s in surfaces if not stands(doc, s)]
        signature = json.dumps([doc.slug, source_hash, template_hash, extractor,
                                item["kind"], raw, lines], sort_keys=True, ensure_ascii=False)
        identifier = "claim:" + hashlib.sha256(signature.encode()).hexdigest()
        reason = ("joined or shortened quote" if re.search(r"\[.*?\]|…|\.\.\.", quote) else
                  "quote not placed" if not lines else "surface absent from document" if absent
                  else "ambiguous quote: choose its passage" if len(lines) > 1
                  else "chapter is neither on the quoted line nor the heading above it"
                  if scoped and item["kind"] == "relation_reading" and not under_heading(doc, lines[0], raw["source"])
                  else None)
        status = "refused" if reason else "duplicate" if identifier in seen else "candidate"
        seen.add(identifier)
        output.append({"id": identifier, **item, "document": doc.slug, "template": template.stem,
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
    """The template's real prompt, schema, chunks and merge, every chunk answered with `response`."""
    import hx
    return native_extract(template, text, hx.canned([response]))


def selftest() -> int:
    global ROOT
    checks = []
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp)
        source = p / "source.md"
        source.write_text("---\ntitle: Fixture\n---\nAlpha steuert Beta.\nVielleicht schützt Alpha Beta.\nLex hält Alpha.\n", encoding="utf-8")
        doc = Document("fixture", "fixture", "2026-09-30", "md", "", source,
                       "Alpha steuert Beta.\nVielleicht schützt Alpha Beta.\nLex hält Alpha.\n", 4)
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
        checks.append(("a row names the template it came from", report["rows"][0]["template"] == "template"))
        checks.append(("duplicate visible", verify(doc, template, env({"items": [row, row]}))["duplicates"] == 1))
        checks.append(("invented quote refused", verify(doc, template, env({"items": [{**row, "quote": "Alpha lenkt Beta."}]}))["refused"] == 1))
        checks.append(("invented surface refused", verify(doc, template, env({"items": [{**row, "term": "Gamma"}]}))["refused"] == 1))
        lex = {"term": "Lex", "quote": "Lex hält Alpha.", "stance": "asserts"}
        checks.append(("a name of three characters stands as a word", verify(doc, template, env({"items": [lex]}))["candidates"] == 1))
        checks.append(("an absent name of three characters is refused", verify(doc, template, env({"items": [{**lex, "term": "Zed"}]}))["refused"] == 1))
        checks.append(("the word for no name needs no line", verify(doc, template, env({"items": [
            {"source": "unlabelled", "target": "Alpha", "type": "speech", "quote": "Lex hält Alpha.", "stance": "asserts"}]}))["candidates"] == 1))
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
        outline = p / "outline.md"
        body = "### Kapitel 2: Die Flucht\n- Plot: Alpha flieht vor Beta.\n### Kapitel 3: Das Bleiben\n- Plot: Beta bleibt.\n"
        outline.write_text("---\ntitle: Outline\n---\n" + body, encoding="utf-8")
        odoc = Document("outline", "outline", "2026-10-05", "md", "", outline, body, 4)
        scoped = p / "scoped.yaml"
        scoped.write_text("tags: [chapters, heading-scoped]\n", encoding="utf-8")
        def oenv(data, t=scoped):
            return {"document": odoc.slug, "source_sha256": digest(outline), "template_sha256": digest(t),
                    "extractor": "offline-fixture", "data": data}
        card = {"source": "Kapitel 2", "target": "Alpha", "type": "who", "quote": "Alpha flieht vor Beta.", "stance": "asserts"}
        checks.append(("a field under its chapter's heading is placed", verify(odoc, scoped, oenv({"items": [card]}))["candidates"] == 1))
        checks.append(("a field moved to the next chapter is refused", verify(odoc, scoped, oenv({"items": [{**card, "source": "Kapitel 3"}]}))["refused"] == 1))
        checks.append(("Kapitel 2 does not match a heading for Kapitel 23", not names_chapter("### Kapitel 23: X", "Kapitel 2")))
        checks.append(("an unscoped contract keeps its old rule", verify(odoc, template, oenv({"items": [{**card, "source": "Kapitel 3"}]}, template))["candidates"] == 1))
        source.write_text(source.read_text() + "Alpha steuert Beta.\n", encoding="utf-8")
        doc = Document("fixture", "fixture", "2026-09-30", "md", "", source,
                       "Alpha steuert Beta.\nVielleicht schützt Alpha Beta.\nLex hält Alpha.\nAlpha steuert Beta.\n", 4)
        checks.append(("ambiguous passage refused", verify(doc, template, env({"items": [row]}))["refused"] == 1))
    for name, held in checks:
        print(("held " if held else "FAIL ") + name)
    print(f"reading_extract: {sum(v for _, v in checks)}/{len(checks)} checks held")
    return int(not all(v for _, v in checks))


def native_selftest() -> int:
    """Every template with a committed fixture: its reply, checked against the template's schema and merged, comes
    back as the fixture — the check that ran in HyperExtract's own interpreter until the port (`hx.py parity`)."""
    folder = ROOT / "Plan/hyperextract/fixtures"
    failed = 0
    names = sorted(f.stem for f in folder.glob("*.json") if not f.stem.startswith("upstream-"))
    text = (folder / "reading.txt").read_text(encoding="utf-8")
    for name in names:
        expected = json.loads((folder / (name + ".json")).read_text(encoding="utf-8"))
        try:
            data = smoke(ROOT / "Plan/hyperextract" / (name + ".yaml"), text, expected)
            candidates(data)
            held = data == expected if "items" in expected else (
                sorted(map(json.dumps, data["nodes"])) == sorted(map(json.dumps, expected["nodes"]))
                and sorted(map(json.dumps, data["edges"])) == sorted(map(json.dumps, expected["edges"])))
        except ValueError as exc:
            held = False
            print(exc)
        failed += not held
        print(f"{'held' if held else 'FAILED'} {name}: prompt/schema/chunks/merge")
    try:
        candidates(smoke(ROOT / "Plan/hyperextract/TermReadings.yaml", text,
                         {"items": [{"term": "Alpha", "quote": None, "stance": "asserts"}]}))
        held = False
    except ValueError:
        held = True
    failed += not held
    print(f"{'held' if held else 'FAILED'} malformed structured response refused")
    print(f"reading_extract native: {len(names) + 1 - failed}/{len(names) + 1} checks held; synthetic, no model quality measured")
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
