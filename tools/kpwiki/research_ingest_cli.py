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
reviewed candidate into the canonical partition below ``Wiki/sources/`` or
``Wiki/concepts/``.

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
from .programs import BatchCompile, ClaimRef, SourceIngest, SourceInput, index_claims
from .schema import Compiled, Extraction, PageState

ROOT = Path(__file__).resolve().parents[2]
MANIFEST_REL = "Sources/manifest.jsonl"
CODEX_REL = "Graph/nodes/codex_entry.jsonl"
EXTRACTIONS_REL = "Wiki/candidates/_extractions"
CONCEPT_INDEX_REL = "Wiki/candidates/_extractions/_concepts.json"
LEDGER_REL = "Wiki/candidates/_extractions/_contradictions.json"
EDGES_REL = "Wiki/graph/edges.jsonl"
LOG_REL = "Wiki/log.md"
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


def existing_pages(root: Path, include_candidates: bool = False) -> dict[str, PageState]:
    """Every promoted page as a PageState, so a merge lands on the page that exists.

    `include_candidates` adds the drafts this command wrote earlier, which is
    what keeps a concept's slug stable across chunks: without it chunk 2 cannot
    see chunk 1's draft and invents a second page for the same concept.
    """
    wiki_root = root / "Wiki"
    if not wiki_root.is_dir():
        return {}
    pages = {}
    for page in wiki_pages.iter_pages(wiki_root, include_candidates=include_candidates):
        if page.error is None:
            pages[page.slug] = PageState(slug=page.slug, kind=page.kind or "", status=page.status or "",
                                         body=page.body)
    return pages


def glossary_terms(root: Path) -> list[str]:
    """Codex slugs the extraction and the clustering step should recognise.

    Read from the record rather than scraped out of a rendered view: `Codex/`
    is a navigation tree whose root files deliberately carry no entries, and a
    matcher that depends on the shape of a rendering breaks whenever the
    rendering changes.
    """
    path = root / CODEX_REL
    if not path.is_file():
        return []
    slugs = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            slug = json.loads(line).get("slug")
            if slug:
                slugs.append(slug)
    return list(dict.fromkeys(slugs))[:MAX_GLOSSARY_TERMS]


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


def extraction_path(root: Path, slug: str) -> Path:
    """Where one source's claims are cached, beside the pages of the same run."""
    return root / EXTRACTIONS_REL / f"{slug}.json"


def cached_extraction(root: Path, slug: str) -> Extraction | None:
    """A previous run's claims for this source, or None.

    Extraction is the expensive half of a source — the pilot's three slowest
    calls were all extractions — and it depends on the document alone, never on
    the batch it arrives in. So it is paid once and reused, which is what makes
    the concept layer re-runnable without re-reading every body.
    """
    path = extraction_path(root, slug)
    if not path.is_file():
        return None
    return Extraction.model_validate_json(path.read_text(encoding="utf-8"))


def cache_extraction(root: Path, extraction: Extraction) -> Path:
    path = extraction_path(root, extraction.source)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(extraction.model_dump_json(indent=1), encoding="utf-8")
    return path


def extract_sources(root: Path, inputs: list[SourceInput],
                    terms: list[str]) -> tuple[list[Extraction], list[str], int]:
    """Triage and extract each source, reusing whatever is already cached.

    Per source and independent of every other, so an interrupted run resumes
    where it stopped instead of starting over.
    """
    program = SourceIngest()
    glossary = ", ".join(terms)
    extractions, skipped, fresh = [], [], 0
    for source in inputs:
        if source.truncated or not source.body.strip():
            skipped.append(source.slug)
            print(f"  skip {source.slug}: truncated or empty")
            continue
        found = cached_extraction(root, source.slug)
        if found is not None:
            print(f"  cached {source.slug}: {len(found.claims)} claim(s)")
            extractions.append(found)
            continue
        result = program(source_file=source.source_file, title=source.title,
                         category_hint=source.category_hint, body=source.body,
                         glossary_terms=glossary)
        found = Extraction(source=source.slug, title=source.title,
                           triage=result.triage, claims=list(result.claims or []))
        cache_extraction(root, found)
        fresh += 1
        print(f"  extracted {source.slug}: {len(found.claims)} claim(s)")
        extractions.append(found)
    return extractions, skipped, fresh


def load_concept_index(root: Path) -> dict[str, list[str]]:
    """Which claims each concept already owns, as `{slug: ["source:index", …]}`.

    This is what makes chunking safe. Without it a later chunk merges a concept
    from its own claims alone, so a document in chunk 5 contradicting one from
    chunk 1 produces two agreeable pages and no disagreement — a clean-looking
    wiki that has quietly stopped doing its job.
    """
    path = root / CONCEPT_INDEX_REL
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def save_concept_index(root: Path, index: dict[str, list[str]]) -> None:
    path = root / CONCEPT_INDEX_REL
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(index, indent=1, sort_keys=True), encoding="utf-8")


def prior_claims_resolver(root: Path, index: dict[str, list[str]]):
    """`slug -> [ClaimRef]`, rebuilt from the per-source extraction cache."""
    def resolve(slug: str) -> list[ClaimRef]:
        refs = []
        for claim_id in index.get(slug, []):
            source, _, position = claim_id.rpartition(":")
            extraction = cached_extraction(root, source)
            if extraction is None or not position.isdigit():
                continue
            at = int(position)
            if at < len(extraction.claims):
                refs.append(ClaimRef(0, source, at, extraction.claims[at]))
        return refs
    return resolve


def record_concept_claims(index: dict[str, list[str]], run: Compiled,
                          pages: dict[str, PageState]) -> dict[str, list[str]]:
    """Fold this chunk's plans into the concept index, keeping earlier claims."""
    by_id = {ref.global_id: ref for ref in index_claims(run.extractions)}
    updated = {slug: list(ids) for slug, ids in index.items()}
    for plan in run.plans:
        slug = plan.existing_slug if plan.existing_slug in pages else plan.slug
        owned = updated.setdefault(slug, [])
        for claim_id in plan.claim_ids:
            ref = by_id.get(claim_id)
            if ref is not None and f"{ref.source}:{ref.index}" not in owned:
                owned.append(f"{ref.source}:{ref.index}")
    return updated


def load_ledger(root: Path) -> dict[str, list[dict[str, Any]]]:
    """Every contradiction ever recorded, keyed `"<subject_kind>/<slug>"`.

    Append-only and the source of truth; the Markdown ledgers under
    `Wiki/candidates/contradictions/` are its rendering, so regenerating a page
    can never drop a clash. That permanence is the point: a document arriving
    much later is checked against disagreements found long before it, which a
    list of currently-open questions could not do.
    """
    path = root / LEDGER_REL
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def save_ledger(root: Path, store: dict[str, list[dict[str, Any]]]) -> None:
    path = root / LEDGER_REL
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(store, indent=1, sort_keys=True, ensure_ascii=False),
                    encoding="utf-8")


def record_contradictions(store: dict[str, list[dict[str, Any]]], run: Compiled, seen: str,
                          questions: dict[str, str]) -> tuple[dict, int, int]:
    """Fold this run's disagreements in. Nothing is ever removed or rewritten.

    A clash already recorded for a subject updates only its resolution, so a
    settled argument moves from Open to Resolved and stays on the page rather
    than disappearing from it.
    """
    updated = {key: list(records) for key, records in store.items()}
    added = resolved = 0
    for draft in run.concepts:
        for item in draft.disagreements:
            record = candidates.contradiction_record(draft, item, seen,
                                                     questions.get(item.topic, ""))
            for subject_kind, slug, subject in candidates.ledger_subjects(draft):
                bucket = updated.setdefault(f"{subject_kind}/{slug}", [])
                known = next((r for r in bucket if r["topic"] == record["topic"]
                              and r["concept"] == record["concept"]), None)
                if known is None:
                    bucket.append({**record, "subject": subject})
                    added += 1
                elif known.get("resolution") != record["resolution"]:
                    known["resolution"] = record["resolution"]
                    resolved += 1
    return updated, added, resolved


def open_questions_for(run: Compiled, seen: str) -> tuple[dict[str, str], dict[str, str]]:
    """A question page per pending disagreement: `({topic: slug}, {path: text})`.

    The ledger is memory; a question is the worklist. An unresolved clash needs
    both, or it is remembered and never acted on.
    """
    slugs, pages = {}, {}
    for draft in run.concepts:
        for item in draft.disagreements:
            if item.resolution != candidates.PENDING:
                continue
            slug = f"widerspruch-{draft.slug}-{candidates.entity_slug(item.topic)}"[:60].rstrip("-")
            slugs[item.topic] = slug
            front, body = candidates.question_for_disagreement(draft, item, slug, seen)
            pages[candidates.candidate_path("question", slug, front)] = candidates.page_text(
                front, [body])
    return slugs, pages


def chunks_of(inputs: list[SourceInput], size: int) -> list[list[SourceInput]]:
    return [inputs[at:at + size] for at in range(0, len(inputs), max(size, 1))]


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
    ap.add_argument("--extract-only", action="store_true",
                    help="basic ingest: triage and extract each source, write its source page "
                         "and cache its claims; skip the concept layer entirely")
    ap.add_argument("--merge-role", choices=["auto", "task", "worker"], default="auto",
                    help="LM for the per-concept merge. 'auto' (default) routes: a concept "
                         "drawing on several sources can hold a contradiction and gets the "
                         "task model, one drawing on a single source cannot and gets worker. "
                         "'task' or 'worker' force one model for every merge")
    ap.add_argument("--chunk", type=int,
                    default=wiki_schema.conventions()["batches"]["chunk_size"],
                    help="sources per chunk; each chunk merges and writes on its own, so a "
                         "run resumes at chunk boundaries instead of restarting")
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
    if ns.extract_only:
        print("\nbasic ingest — sources only, no concept layer")
        extractions, skipped, fresh = extract_sources(root, inputs, terms)
        run = Compiled(extractions=extractions, skipped=skipped)
        print(f"  {len(extractions)} source(s), {fresh} newly extracted, "
              f"{sum(len(e.claims) for e in extractions)} claim(s) total")
        written = write_run(root, run, manifest, terms)
        print(f"claims cached under {EXTRACTIONS_REL}/ — the concept layer can run later "
              "over these without re-reading a single body")
        if ns.out:
            write_artifact(ns.out, run)
        return report_lint(root, written)

    written, last = ingest_chunks(root, ns, inputs, manifest, terms)
    if ns.out and last is not None:
        write_artifact(ns.out, last)
    return report_lint(root, written)


def write_artifact(path: Path, run: Compiled) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(run.model_dump_json(indent=1), encoding="utf-8")
    print(f"compiled result: {path}")


def write_run(root: Path, run: Compiled, manifest: dict[str, dict[str, Any]],
              terms: list[str], extra: dict[str, str] | None = None) -> list[str]:
    """Render, write and log one chunk's output. Each chunk lands on its own."""
    rendered = candidates.render_pages(run, manifest, codex_slugs=frozenset(terms))
    rendered.update(extra or {})
    written = write_pages(root, rendered)
    edges = append_edges(root, candidates.edge_records(run))
    logged = append_log(root, candidates.log_entries(run, rendered))
    print(f"  wrote {len(written)} candidate page(s), {edges} edge(s), {logged} log line(s)")
    return written


def ingest_chunks(root: Path, ns: argparse.Namespace, inputs: list[SourceInput],
                  manifest: dict[str, dict[str, Any]],
                  terms: list[str]) -> tuple[list[str], Compiled | None]:
    """Ingest in chunks, carrying each concept's claim history across them.

    A chunk is one merge cycle and one write, so an interrupted run resumes at
    a chunk boundary. Correctness across boundaries comes from the concept
    index: every concept is merged from all the claims it has ever been given,
    not only the ones in the chunk at hand, so a contradiction between two
    documents is found whether or not they arrived together.
    """
    groups = chunks_of(inputs, ns.chunk)
    concept_index = load_concept_index(root)
    ledger = load_ledger(root)
    written: list[str] = []
    last: Compiled | None = None
    for number, group in enumerate(groups, start=1):
        print(f"\nchunk {number}/{len(groups)} — {len(group)} source(s): "
              f"{', '.join(s.slug for s in group)}")
        pages = existing_pages(root, include_candidates=True)
        run = BatchCompile(merge_role=ns.merge_role,
                           prior_claims=prior_claims_resolver(root, concept_index),
                           load_extraction=lambda slug: cached_extraction(root, slug))(
            sources=group, pages=pages, known_entities=terms).compiled
        for extraction in run.extractions:
            cache_extraction(root, extraction)
        print("  knowledge diff")
        for line in candidates.knowledge_diff_report(run, manifest):
            print(f"    {line}")
        verdict = score(run, group, pages, terms)
        print(f"  compile_metric: score={verdict.score:.3f}")

        stamp = candidates.today()
        question_slugs, question_pages = open_questions_for(run, stamp)
        ledger, added, settled = record_contradictions(ledger, run, stamp, question_slugs)
        save_ledger(root, ledger)
        extra = {**question_pages, **candidates.ledger_pages(ledger, stamp)}
        if added or settled:
            print(f"  contradictions: {added} newly recorded, {settled} resolution(s) updated, "
                  f"{len(question_pages)} question(s) raised")
        written += write_run(root, run, manifest, terms, extra)
        concept_index = record_concept_claims(concept_index, run, pages)
        save_concept_index(root, concept_index)
        last = run
    open_now = sum(1 for records in ledger.values()
                   for r in records if r.get("resolution", candidates.PENDING) == candidates.PENDING)
    print(f"\n{len(groups)} chunk(s), {len(concept_index)} concept(s) in {CONCEPT_INDEX_REL}")
    print(f"ledger: {len(ledger)} subject(s), {open_now} open contradiction(s) in {LEDGER_REL}")
    return written, last


def report_lint(root: Path, written: list[str]) -> int:
    findings = lint_written(root, written)
    print("\nlint on the written candidates:")
    for finding in findings:
        print(f"  {finding}")
    print(f"  {len(findings)} finding(s); a candidate with findings is never promoted")
    return 0


if __name__ == "__main__":
    sys.exit(main())
