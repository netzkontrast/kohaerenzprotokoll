"""Command-line front for /research-ingest: sources → BatchCompile → candidates.

    python -m tools.kpwiki.research_ingest_cli --category audit --dry-run
    python -m tools.kpwiki.research_ingest_cli --slug a --slug b [--write]
    python -m tools.kpwiki.research_ingest_cli --category kernkonzept --batch 25 --write

Selection is deterministic and comes from ``Sources/manifest.jsonl``:
``--slug`` (repeatable), ``--category``, ``--tier`` and ``--batch N`` (the
batch size of ``conventions.yaml`` by default). A record without an export, a
record marked ``truncated`` and every tier the contract excludes from ingest
(``T0-duplicate``, ``T1-superseded``, ``T4-out-of-scope``) are dropped, with a
line saying so.

``--dry-run`` (the default) assembles the batch, prints what would be sent and
stops before the first LM call. ``--write`` is a user-owned flag: a session
never sets it on its own (``writers.yaml → user_flags``). With it the run
calls the LM, prints the knowledge diff, writes ``Wiki/candidates/**``,
appends to ``Wiki/graph/edges.jsonl`` and ``Wiki/log.md``, and finishes by
linting every page it wrote. Nothing is promoted: ``/wiki-promote`` moves a
reviewed candidate into ``Wiki/sources/`` or ``Wiki/concepts/``.

Exit status: 0 when the run finished (lint findings are reported, not fatal),
1 when the selection is empty, 2 when a selected export is missing from disk.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from . import candidates, lm, wiki_pages, wiki_schema
from .compile_metric import compile_metric
from .programs import BatchCompile, SourceInput
from .schema import Compiled, PageState

ROOT = Path(__file__).resolve().parents[2]
MANIFEST_REL = "Sources/manifest.jsonl"
GLOSSARY_REL = "Codex/GLOSSARY.md"
EDGES_REL = "Wiki/graph/edges.jsonl"
LOG_REL = "Wiki/log.md"
CODEX_SLUG_RE = "`([a-z0-9-]+)`"
MAX_GLOSSARY_TERMS = 400


# --- selection ----------------------------------------------------------------------


def excluded_tiers() -> set[str]:
    """Tiers the contract never ingests: duplicates, superseded drafts, out of scope."""
    tiers = wiki_schema.enum_values("tier")
    return {t for t in tiers if t.startswith(("T0-", "T1-", "T4-"))}


def load_manifest(root: Path) -> dict[str, dict[str, Any]]:
    records = {}
    for line in (root / MANIFEST_REL).read_text(encoding="utf-8").splitlines():
        if line.strip():
            record = json.loads(line)
            records[record["slug"]] = record
    return records


def select(manifest: dict[str, dict[str, Any]], ns: argparse.Namespace) -> tuple[list[dict], list[str]]:
    """The records to ingest, plus one note per record that was dropped and why."""
    wanted = list(manifest.values())
    notes = []
    if ns.slug:
        missing = [s for s in ns.slug if s not in manifest]
        notes += [f"unknown slug: {s}" for s in missing]
        wanted = [manifest[s] for s in ns.slug if s in manifest]
    if ns.category:
        wanted = [r for r in wanted if r.get("category") == ns.category]
    if ns.tier:
        wanted = [r for r in wanted if r.get("tier") == ns.tier]
    kept, excluded = [], excluded_tiers()
    for record in wanted:
        if not record.get("export_path"):
            notes.append(f"{record['slug']}: not exported yet")
        elif record.get("truncated"):
            notes.append(f"{record['slug']}: export is truncated, never ingested")
        elif record.get("tier") in excluded:
            notes.append(f"{record['slug']}: tier {record['tier']} is not ingested")
        else:
            kept.append(record)
    kept.sort(key=lambda r: (r.get("index_date", ""), r["slug"]))
    if ns.batch and len(kept) > ns.batch:
        notes.append(f"batch limit {ns.batch}: {len(kept) - ns.batch} record(s) left for a later run")
        kept = kept[: ns.batch]
    return kept, notes


def to_inputs(records: list[dict], root: Path) -> list[SourceInput]:
    inputs = []
    for record in records:
        path = root / record["export_path"]
        if not path.is_file():
            raise FileNotFoundError(record["export_path"])
        inputs.append(SourceInput(slug=record["slug"], title=record.get("title", record["slug"]),
                                  category_hint=record.get("category", ""), index_date=record.get("index_date", ""),
                                  source_file=record["export_path"], body=path.read_text(encoding="utf-8"),
                                  truncated=bool(record.get("truncated"))))
    return inputs


# --- wiki state ---------------------------------------------------------------------


def existing_pages(root: Path) -> dict[str, PageState]:
    """Every promoted page as a PageState, so a merge lands on the page that exists."""
    wiki_root = root / "Wiki"
    if not wiki_root.is_dir():
        return {}
    pages = {}
    for page in wiki_pages.iter_pages(wiki_root, include_candidates=False):
        if page.error is None:
            pages[page.slug] = PageState(slug=page.slug, kind=page.kind or "", status=page.status or "",
                                         body=page.body)
    return pages


def glossary_terms(root: Path) -> list[str]:
    """Codex slugs the extraction and the clustering step should recognise."""
    import re

    path = root / GLOSSARY_REL
    if not path.is_file():
        return []
    slugs = dict.fromkeys(re.findall(CODEX_SLUG_RE, path.read_text(encoding="utf-8")))
    return list(slugs)[:MAX_GLOSSARY_TERMS]


# --- writing ------------------------------------------------------------------------


def write_pages(root: Path, pages: dict[str, str]) -> list[str]:
    written = []
    for rel, text in sorted(pages.items()):
        target = root / "Wiki" / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        written.append(f"Wiki/{rel}")
    return written


def append_lines(path: Path, lines: list[str], separator: str = "\n") -> None:
    if not lines:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    previous = path.read_text(encoding="utf-8") if path.is_file() else ""
    prefix = "" if not previous or previous.endswith("\n") else "\n"
    path.write_text(previous + prefix + separator.join(lines) + "\n", encoding="utf-8")


def append_edges(root: Path, records: list[dict[str, Any]]) -> int:
    append_lines(root / EDGES_REL, [json.dumps(r, ensure_ascii=False, sort_keys=True) for r in records])
    return len(records)


def append_log(root: Path, lines: list[str]) -> int:
    append_lines(root / LOG_REL, lines, separator="\n\n")
    return len(lines)


def lint_written(root: Path, written: list[str]) -> list[str]:
    """Run the candidate subset of the wiki lint over every page this run wrote."""
    sys.path.insert(0, str(root / "scripts"))
    import wiki_lint  # noqa: E402  (a script, imported for its hook mode)

    from .wiki_lint_rules import build_context

    ctx = build_context(root / "Wiki", root)
    findings = []
    for rel in written:
        findings.extend(f.render() for f in wiki_lint.hook_findings(ctx, root / rel))
    return findings


# --- run ----------------------------------------------------------------------------


def describe_batch(inputs: list[SourceInput], pages: dict[str, PageState], terms: list[str]) -> list[str]:
    total = sum(len(s.body.splitlines()) for s in inputs)
    return [f"batch: {len(inputs)} source(s), {total} lines, {sum(len(s.body) for s in inputs)} chars",
            f"existing pages: {len(pages)} · glossary terms: {len(terms)}",
            *(f"  {s.slug} ({s.index_date}, {len(s.body.splitlines())} lines) — {s.title}" for s in inputs)]


def score(run: Compiled, inputs: list[SourceInput], pages: dict[str, PageState], terms: list[str]) -> Any:
    import dspy

    gold = dspy.Example(sources={s.source_file: s.body for s in inputs}, pages=pages, known_entities=terms)
    return compile_metric(gold, dspy.Prediction(compiled=run))


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--slug", action="append", default=[], help="manifest slug; repeatable")
    ap.add_argument("--category", help="manifest category, e.g. audit or kernkonzept")
    ap.add_argument("--tier", help="manifest tier, e.g. T3-work")
    ap.add_argument("--batch", type=int, default=wiki_schema.conventions()["batches"]["ingest_size"],
                    help="how many sources at most in one run")
    ap.add_argument("--write", action="store_true",
                    help="call the LM and write candidates, edges and log lines (user-owned flag)")
    ap.add_argument("--dry-run", action="store_true", help="assemble and print the batch, call no LM (default)")
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--out", type=Path, help="write the Compiled result as JSON as well")
    return ap


def main(argv: list[str] | None = None) -> int:
    ns = build_parser().parse_args(argv)
    root = ns.root.resolve()
    manifest = load_manifest(root)
    records, notes = select(manifest, ns)
    for note in notes:
        print(f"skip: {note}")
    if not records:
        print("nothing to ingest for this selection")
        return 1
    try:
        inputs = to_inputs(records, root)
    except FileNotFoundError as exc:
        print(f"export missing on disk: {exc}", file=sys.stderr)
        return 2
    pages, terms = existing_pages(root), glossary_terms(root)
    for line in describe_batch(inputs, pages, terms):
        print(line)
    if not ns.write:
        print("dry run: no LM call, nothing written; re-run with --write to ingest")
        return 0

    lm.configure("task")
    run = BatchCompile()(sources=inputs, pages=pages, known_entities=terms).compiled
    print("\nknowledge diff")
    for line in candidates.knowledge_diff_report(run, manifest):
        print(f"  {line}")
    verdict = score(run, inputs, pages, terms)
    print(f"\ncompile_metric: score={verdict.score:.3f}\n  {verdict.feedback}")

    rendered = candidates.render_pages(run, manifest, codex_slugs=frozenset(terms))
    written = write_pages(root, rendered)
    edges = append_edges(root, candidates.edge_records(run))
    logged = append_log(root, candidates.log_entries(run, rendered))
    print(f"\nwrote {len(written)} candidate page(s), {edges} edge(s), {logged} log line(s)")
    if ns.out:
        ns.out.parent.mkdir(parents=True, exist_ok=True)
        ns.out.write_text(run.model_dump_json(indent=1), encoding="utf-8")
        print(f"compiled result: {ns.out}")
    findings = lint_written(root, written)
    print("\nlint on the written candidates:")
    for finding in findings:
        print(f"  {finding}")
    print(f"  {len(findings)} finding(s); a candidate with findings is never promoted")
    return 0


if __name__ == "__main__":
    sys.exit(main())
