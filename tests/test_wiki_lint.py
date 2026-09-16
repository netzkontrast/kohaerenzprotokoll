"""Tests for scripts/wiki_lint.py — one fixture per rule (integration plan §3).

``make_wiki`` builds a minimal research wiki that lints clean (four promoted
pages, a raw source, a manifest, Canon and Codex stand-ins, a log and the
rendered views). Every test below breaks exactly one rule and asserts the
finding; the CLI modes live in ``tests/test_wiki_lint_modes.py``.

    python3 -m pytest tests/test_wiki_lint.py -q -W error::RuntimeWarning
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from tools.kpwiki import wiki_pages, wiki_views  # noqa: E402


def load_script():
    spec = importlib.util.spec_from_file_location("wiki_lint", ROOT / "scripts" / "wiki_lint.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


wiki_lint = load_script()
rules = wiki_lint.rules

DRIVE_TEXT = ("# Quelle Eins\n\nDie Kohärenz ist ein langsamer Drift über die vier Kernwelten.\n"
              "Jede Welt trägt ihren eigenen Rhythmus.\nEnde.\n")
FILLER = " ".join(["The fixture body carries enough plain English prose to clear the sparse-page",
                   "word floor, so every test breaks exactly one rule and nothing else."] * 3)
CANON_HEADING = "Kohärenz Canon Heading"

SOURCE_BODY = f"""
## Summary

{FILLER}

## Key claims

- „Kohärenz ist ein langsamer Drift“ — the drift claim ^[Sources/drive/quelle-eins.md:3-4]

## Entities

- [[kohaerenz]]

## Canon relation

consistent — canon:Canon/kohaerenz-canon.md#{CANON_HEADING}

## Open questions

## Log

- 2026-09-01 ingest by /research-ingest
"""
CONCEPT_BODY = f"""
## Definition

{FILLER} ^[Sources/drive/quelle-eins.md:3]

## What Canon says

> Die Kohärenz ist ein langsamer Drift. [K]

## Where sources agree

- [[quelle-eins]] carries the drift claim.

## Where they disagree

- none

## Timeline of the idea

- 2025-05-04 [[quelle-eins]]

## Open questions

- [[frage-eins]]
"""
QUESTION_BODY = f"""
## Question

Does the drift hold in every Kernwelt? {FILLER}

## Evidence

- „Jede Welt trägt ihren eigenen Rhythmus“ ^[Sources/drive/quelle-eins.md:4]

## What Canon says

> Canon schweigt.

## Candidate answers

- yes, per [[kohaerenz]]

## Resolution

open
"""
SYNTHESIS_BODY = f"""
## Question

What is the drift? {FILLER}

## Answer

The drift is described in [[kohaerenz]] from [[quelle-eins]]; [[frage-eins]] stays open.

## Sources

- [[quelle-eins]]
- [[kohaerenz]]
- [[frage-eins]]

## Gaps

- none
"""


def source_front(sha: str) -> dict:
    return {"title": "Quelle Eins", "kind": "source", "slug": "quelle-eins", "drive_id": "drive-1",
            "tier": "T3-work", "category": "kernkonzept", "language": "de", "status": "reviewed",
            "sha256": sha, "ingested": "2026-09-01", "truncated": False}


CONCEPT_FRONT = {"title": "Kohärenz", "kind": "concept", "slug": "kohaerenz", "kind_detail": "concept",
                 "status": "reviewed", "confidence": "medium", "sources": ["quelle-eins"],
                 "canon_status": "unverified", "codex_ref": "codex:kohaerenz"}
QUESTION_FRONT = {"title": "Frage Eins", "kind": "question", "slug": "frage-eins", "axis": "incompleteness",
                  "status": "open", "concepts": ["kohaerenz"],
                  "evidence": ["^[Sources/drive/quelle-eins.md:3-4] HIGH"], "owner": "author"}
SYNTHESIS_FRONT = {"title": "Synthese Eins", "kind": "synthesis", "slug": "synthese-eins",
                   "query": "what is the drift?", "sources": ["quelle-eins", "kohaerenz", "frage-eins"],
                   "status": "reviewed", "filed": "2026-09-10"}


def write_page(repo: Path, rel: str, front: dict, body: str) -> Path:
    path = repo / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(rules.render_page(front, body), encoding="utf-8")
    return path


def render_views(repo: Path) -> None:
    pages = wiki_pages.iter_pages(repo / "Wiki")
    (repo / "Wiki" / "index.md").write_text(wiki_views.render_index(pages), encoding="utf-8")
    (repo / "Wiki" / "concept-table.md").write_text(wiki_views.render_concept_table(pages), encoding="utf-8")


def add_log(repo: Path, title: str, op: str = "promote", skill: str = "/wiki-promote") -> None:
    with (repo / "Wiki" / "log.md").open("a", encoding="utf-8") as fh:
        fh.write(f"## [2026-09-16] {op} | {title} | skill={skill}\n")


def make_wiki(tmp_path: Path) -> Path:
    """A clean fixture wiki under ``tmp_path``; returns the repo root."""
    repo = tmp_path
    for folder in ("Wiki/sources", "Wiki/concepts", "Wiki/questions", "Wiki/syntheses",
                   "Wiki/candidates", "Wiki/graph", "Sources/drive", "Canon", "Codex"):
        (repo / folder).mkdir(parents=True, exist_ok=True)
    drive = repo / "Sources/drive/quelle-eins.md"
    drive.write_text(DRIVE_TEXT, encoding="utf-8")
    sha = hashlib.sha256(drive.read_bytes()).hexdigest()
    (repo / "Sources/manifest.jsonl").write_text(
        json.dumps({"slug": "quelle-eins", "sha256": sha, "tier": "T3-work"}) + "\n"
        + json.dumps({"slug": "quelle-zwei", "sha256": "", "tier": "T2-theory"}) + "\n", encoding="utf-8")
    (repo / "Canon/kohaerenz-canon.md").write_text(f"# {CANON_HEADING}\n\nDrift [K]\n", encoding="utf-8")
    (repo / "Codex/GLOSSARY.md").write_text("# Glossar\n", encoding="utf-8")
    (repo / "Wiki/graph/edges.jsonl").write_text("", encoding="utf-8")
    (repo / "Wiki/log.md").write_text("# Log\n\n", encoding="utf-8")
    write_page(repo, "Wiki/sources/quelle-eins.md", source_front(sha), SOURCE_BODY)
    write_page(repo, "Wiki/concepts/kohaerenz.md", CONCEPT_FRONT, CONCEPT_BODY)
    write_page(repo, "Wiki/questions/frage-eins.md", QUESTION_FRONT, QUESTION_BODY)
    write_page(repo, "Wiki/syntheses/synthese-eins.md", SYNTHESIS_FRONT, SYNTHESIS_BODY)
    for title in ("Quelle Eins", "Kohärenz", "Frage Eins", "Synthese Eins"):
        add_log(repo, title)
    render_views(repo)
    return repo


def lint(repo: Path, only: list[str] | None = None):
    ctx = rules.build_context(repo / "Wiki", repo)
    return wiki_lint.run_rules(ctx, only)


def hits(findings, rule: str):
    return [f for f in findings if f.rule == rule]


def set_front(repo: Path, rel: str, **changes) -> None:
    text = (repo / rel).read_text(encoding="utf-8")
    front, body = wiki_pages.split_frontmatter(text)
    for key, value in changes.items():
        if value is None:
            front.pop(key, None)
        else:
            front[key] = value
    (repo / rel).write_text(rules.render_page(front, body), encoding="utf-8")


def append_body(repo: Path, rel: str, text: str) -> None:
    with (repo / rel).open("a", encoding="utf-8") as fh:
        fh.write(text)


def write_edges(repo: Path, records: list[dict]) -> None:
    (repo / "Wiki/graph/edges.jsonl").write_text(
        "".join(json.dumps(r) + "\n" for r in records), encoding="utf-8")


def good_edge(**overrides) -> dict:
    record = {"from": "quelle-eins", "to": "kohaerenz", "type": "supports", "confidence": "high",
              "evidence": "^[Sources/drive/quelle-eins.md:3-4]", "written_by": "/research-ingest",
              "at": "2026-09-16"}
    record.update(overrides)
    return record


# --- the clean fixture --------------------------------------------------------------------

def test_clean_fixture_has_no_errors_or_warnings(tmp_path):
    findings = lint(make_wiki(tmp_path))
    assert [f.render() for f in findings if f.severity != "info"] == []
    assert {f.rule for f in findings} <= {"no-page-body-in-graph"}


def test_all_21_rules_are_registered():
    assert len(rules.RULES) == 21


# --- one test per rule -------------------------------------------------------------------

def test_required_field_missing(tmp_path):
    repo = make_wiki(tmp_path)
    set_front(repo, "Wiki/sources/quelle-eins.md", tier=None)
    found = hits(lint(repo, ["required-field"]), "required-field")
    assert found[0].severity == "error" and found[0].path == "Wiki/sources/quelle-eins.md"
    assert "tier" in found[0].message


def test_required_field_unparseable_frontmatter(tmp_path):
    repo = make_wiki(tmp_path)
    (repo / "Wiki/concepts/kohaerenz.md").write_text("---\ntitle: [unclosed\n---\nbody\n", encoding="utf-8")
    found = hits(lint(repo, ["required-field"]), "required-field")
    assert found[0].severity == "error" and "did not parse" in found[0].message


def test_enum_rejects_unknown_tier_and_bad_date(tmp_path):
    repo = make_wiki(tmp_path)
    set_front(repo, "Wiki/sources/quelle-eins.md", tier="T9-nope", ingested="2026-13-40")
    messages = [f.message for f in hits(lint(repo, ["enum"]), "enum")]
    assert any(m.startswith("tier:") for m in messages) and any(m.startswith("ingested:") for m in messages)


def test_illegal_transition_for_new_page(tmp_path):
    repo = make_wiki(tmp_path)
    set_front(repo, "Wiki/concepts/kohaerenz.md", status="superseded")
    found = hits(lint(repo, ["illegal-transition"]), "illegal-transition")
    assert found[0].severity == "error" and found[0].path == "Wiki/concepts/kohaerenz.md"


def test_illegal_transition_against_git_head(tmp_path):
    repo = make_wiki(tmp_path)
    for args in (("init", "-q"), ("add", "."), ("commit", "-q", "-m", "fixture")):
        subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@example.org", *args],
                       cwd=repo, check=True, capture_output=True)
    set_front(repo, "Wiki/concepts/kohaerenz.md", status="draft")
    found = hits(lint(repo, ["illegal-transition"]), "illegal-transition")
    assert found[0].severity == "error" and "'reviewed' → 'draft'" in found[0].message


def test_archived_link(tmp_path):
    repo = make_wiki(tmp_path)
    write_page(repo, "Wiki/concepts/alt.md", {**CONCEPT_FRONT, "slug": "alt", "title": "Alt",
                                              "status": "archived"}, CONCEPT_BODY)
    append_body(repo, "Wiki/sources/quelle-eins.md", "\nSee [[alt]].\n")
    found = hits(lint(repo, ["archived-link"]), "archived-link")
    assert found[0].severity == "warn" and found[0].path == "Wiki/sources/quelle-eins.md" and found[0].line


def test_broken_link_and_candidate_resolution(tmp_path):
    repo = make_wiki(tmp_path)
    write_page(repo, "Wiki/candidates/kandidat.md", {**CONCEPT_FRONT, "slug": "kandidat", "status": "draft"},
               CONCEPT_BODY)
    append_body(repo, "Wiki/sources/quelle-eins.md", "\n[[nirgendwo]] and [[kandidat]]\n")
    found = hits(lint(repo, ["broken-link"]), "broken-link")
    assert {(f.severity, f.message.split(" ")[0]) for f in found} == {("error", "[[nirgendwo]]"), ("info", "[[kandidat]]")}


def test_orphan(tmp_path):
    repo = make_wiki(tmp_path)
    write_page(repo, "Wiki/concepts/einsam.md", {**CONCEPT_FRONT, "slug": "einsam", "title": "Einsam"}, CONCEPT_BODY)
    found = hits(lint(repo, ["orphan"]), "orphan")
    assert [(f.severity, f.path) for f in found] == [("warn", "Wiki/concepts/einsam.md")]


def test_missing_entity(tmp_path):
    repo = make_wiki(tmp_path)
    for rel in ("Wiki/sources/quelle-eins.md", "Wiki/concepts/kohaerenz.md", "Wiki/questions/frage-eins.md"):
        append_body(repo, rel, "\nMentions codex:aegis here.\n")
    found = hits(lint(repo, ["missing-entity"]), "missing-entity")
    assert found[0].severity == "info" and "codex:aegis" in found[0].message and "3 pages" in found[0].message


def test_sparse_page_missing_section_and_short_body(tmp_path):
    repo = make_wiki(tmp_path)
    text = (repo / "Wiki/sources/quelle-eins.md").read_text(encoding="utf-8")
    (repo / "Wiki/sources/quelle-eins.md").write_text(text.split("## Log")[0], encoding="utf-8")
    write_page(repo, "Wiki/questions/frage-eins.md", QUESTION_FRONT, "\n## Question\n\nshort\n")
    found = hits(lint(repo, ["sparse-page"]), "sparse-page")
    assert all(f.severity == "warn" for f in found)
    messages = {f.path: " / ".join(g.message for g in found if g.path == f.path) for f in found}
    assert "missing sections: Log" in messages["Wiki/sources/quelle-eins.md"]
    assert "words" in messages["Wiki/questions/frage-eins.md"]


def test_citation_resolves(tmp_path):
    repo = make_wiki(tmp_path)
    append_body(repo, "Wiki/sources/quelle-eins.md",
                "\n- x ^[Sources/drive/quelle-eins.md:40-41]\n- y ^[Sources/drive/fehlt.md:1]\n"
                "- „Nicht vorhanden“ ^[Sources/drive/quelle-eins.md:3]\n")
    found = hits(lint(repo, ["citation-resolves"]), "citation-resolves")
    assert len(found) == 3 and {f.severity for f in found} == {"error"}
    assert any("outside" in f.message for f in found) and any("not found" in f.message for f in found)
    assert any("Nicht vorhanden" in f.message for f in found)


def test_stale_source_drive_file(tmp_path):
    repo = make_wiki(tmp_path)
    (repo / "Sources/drive/quelle-eins.md").write_text(DRIVE_TEXT + "Nachtrag.\n", encoding="utf-8")
    found = hits(lint(repo, ["stale-source"]), "stale-source")
    assert found[0].severity == "warn" and "Sources/drive/quelle-eins.md" in found[0].message


def test_stale_source_manifest(tmp_path):
    repo = make_wiki(tmp_path)
    (repo / "Sources/drive/quelle-eins.md").unlink()
    set_front(repo, "Wiki/sources/quelle-eins.md", sha256="0" * 64)
    found = hits(lint(repo, ["stale-source"]), "stale-source")
    assert found[0].severity == "warn" and "manifest" in found[0].message


def test_xref_symmetry(tmp_path):
    repo = make_wiki(tmp_path)
    text = (repo / "Wiki/concepts/kohaerenz.md").read_text(encoding="utf-8")
    (repo / "Wiki/concepts/kohaerenz.md").write_text(text.replace("- [[frage-eins]]\n", ""), encoding="utf-8")
    found = hits(lint(repo, ["xref-symmetry"]), "xref-symmetry")
    assert found[0].severity == "warn" and found[0].path == "Wiki/concepts/kohaerenz.md"
    assert "question-about-concept" in found[0].message and "[[frage-eins]]" in found[0].message


def test_edge_evidence(tmp_path):
    repo = make_wiki(tmp_path)
    write_edges(repo, [good_edge(), good_edge(type="bogus"), good_edge(evidence=None, written_by="/nope"),
                       good_edge(type="contradicts")])
    found = hits(lint(repo, ["edge-evidence"]), "edge-evidence")
    assert {f.line for f in found} == {2, 3, 4} and all(f.path == "Wiki/graph/edges.jsonl" for f in found)
    assert any("type 'bogus'" in f.message for f in found) and any("requires evidence" in f.message for f in found)
    assert [f.severity for f in found if f.line == 4] == ["warn", "warn"]


def test_writer_policy(tmp_path):
    repo = make_wiki(tmp_path)
    add_log(repo, "X", skill="/nope")
    add_log(repo, "Y", op="bogus")
    found = hits(lint(repo, ["writer-policy"]), "writer-policy")
    assert len(found) == 2 and all(f.severity == "error" and f.path == "Wiki/log.md" for f in found)


def test_no_k_marker_outside_canon(tmp_path):
    repo = make_wiki(tmp_path)
    append_body(repo, "Wiki/concepts/kohaerenz.md", "\nDrift [K] emitted.\n> quoted [K]\n„zitiert [K]“\n")
    found = hits(lint(repo, ["no-k-marker-outside-canon"]), "no-k-marker-outside-canon")
    assert len(found) == 1 and found[0].severity == "error" and found[0].path == "Wiki/concepts/kohaerenz.md"


def test_no_reverse_into_canon(tmp_path):
    repo = make_wiki(tmp_path)
    write_edges(repo, [good_edge(**{"from": "canon:Canon/kohaerenz-canon.md#x"})])
    set_front(repo, "Wiki/concepts/kohaerenz.md", sources=["quelle-eins", "codex:kohaerenz"])
    found = hits(lint(repo, ["no-reverse-into-canon"]), "no-reverse-into-canon")
    assert {f.path for f in found} == {"Wiki/graph/edges.jsonl", "Wiki/concepts/kohaerenz.md"}
    assert all(f.severity == "error" for f in found)


def test_no_auto_canon_page(tmp_path):
    repo = make_wiki(tmp_path)
    write_page(repo, "Wiki/concepts/kohaerenz-canon.md",
               {**CONCEPT_FRONT, "slug": "kohaerenz-canon", "title": CANON_HEADING}, CONCEPT_BODY)
    found = hits(lint(repo, ["no-auto-canon-page"]), "no-auto-canon-page")
    assert len(found) == 2 and all(f.severity == "error" for f in found)


def test_index_sync(tmp_path):
    repo = make_wiki(tmp_path)
    append_body(repo, "Wiki/index.md", "\n- stray line\n")
    found = hits(lint(repo, ["index-sync"]), "index-sync")
    assert [(f.severity, f.path) for f in found] == [("error", "Wiki/index.md")]
    assert "render_wiki_views.py" in found[0].message


def test_log_coverage(tmp_path):
    repo = make_wiki(tmp_path)
    log = repo / "Wiki/log.md"
    log.write_text(log.read_text(encoding="utf-8").replace("| Kohärenz |", "| Anders |"), encoding="utf-8")
    found = hits(lint(repo, ["log-coverage"]), "log-coverage")
    assert [(f.severity, f.path) for f in found] == [("warn", "Wiki/concepts/kohaerenz.md")]


def test_candidate_age(tmp_path):
    repo = make_wiki(tmp_path)
    write_page(repo, "Wiki/candidates/alt-kandidat.md",
               {**CONCEPT_FRONT, "slug": "alt-kandidat", "status": "draft", "ingested": "2020-01-01"}, CONCEPT_BODY)
    found = hits(lint(repo, ["candidate-age"]), "candidate-age")
    assert found[0].severity == "warn" and found[0].path == "Wiki/candidates/alt-kandidat.md"


def test_no_page_body_in_graph(tmp_path):
    repo = make_wiki(tmp_path)
    nodes = repo / "Graph" / "nodes"
    nodes.mkdir(parents=True)
    (nodes / "codex_entry.jsonl").write_text(
        json.dumps({"_nid": 7, "id": "codexentry:7", "body": CONCEPT_BODY},
                   ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    found = hits(lint(repo, ["no-page-body-in-graph"]), "no-page-body-in-graph")
    assert [(f.severity, f.path) for f in found] == [("error", "Wiki/concepts/kohaerenz.md")]
    assert "node 7" in found[0].message


def test_no_page_body_in_graph_without_the_graph_is_info(tmp_path):
    found = hits(lint(make_wiki(tmp_path), ["no-page-body-in-graph"]), "no-page-body-in-graph")
    assert [f.severity for f in found] == ["info"]


def test_cascade_risk(tmp_path):
    repo = make_wiki(tmp_path)
    write_edges(repo, [good_edge() for _ in range(5)])
    set_front(repo, "Wiki/concepts/kohaerenz.md", status="contested")
    found = hits(lint(repo, ["cascade-risk"]), "cascade-risk")
    assert [(f.severity, f.path) for f in found] == [("info", "Wiki/concepts/kohaerenz.md")]
    assert "5 pages" in found[0].message
