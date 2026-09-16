"""Offline tests for the /research-ingest projection and its selection.

The rendering is deterministic, so the decisive test writes the fixture batch
into a temporary repository and runs the candidate subset of the wiki lint
over the pages: what BatchCompile drafts must be lintable before anyone is
asked to review it. No LM is called anywhere in this file.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import pytest

dspy = pytest.importorskip("dspy")

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import wiki_lint  # noqa: E402

from tools.kpwiki import candidates, wiki_pages, wiki_schema  # noqa: E402
from tools.kpwiki import compile_fixture as fx  # noqa: E402
from tools.kpwiki import research_ingest_cli as cli  # noqa: E402
from tools.kpwiki.wiki_lint_rules import build_context  # noqa: E402

INGESTED = "2026-09-16"
MANIFEST = {
    fx.SLUG_A: {"slug": fx.SLUG_A, "title": "Notiz A zum System Kael", "drive_id": "1aaa", "tier": "T3-work",
                "category": "kernkonzept", "index_date": fx.DATE_A, "sha256": "a" * 64,
                "export_path": fx.FILE_A, "truncated": False},
    fx.SLUG_B: {"slug": fx.SLUG_B, "title": "Notiz B zum System Kael", "drive_id": "1bbb", "tier": "T3-work",
                "category": "kernkonzept", "index_date": fx.DATE_B, "sha256": "b" * 64,
                "export_path": fx.FILE_B, "truncated": False},
}


def rendered() -> dict[str, str]:
    return candidates.render_pages(fx.handmade_compiled(), MANIFEST, INGESTED)


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    """A temporary repository with the two exports and the rendered candidates."""
    (tmp_path / "Sources/drive").mkdir(parents=True)
    (tmp_path / fx.FILE_A).write_text(fx.BODY_A, encoding="utf-8")
    (tmp_path / fx.FILE_B).write_text(fx.BODY_B, encoding="utf-8")
    for rel, text in rendered().items():
        target = tmp_path / "Wiki" / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
    return tmp_path


def front_of(text: str) -> dict:
    return wiki_pages.split_frontmatter(text)[0]


# --- the pages ----------------------------------------------------------------------


def test_every_extraction_and_concept_becomes_a_candidate():
    paths = set(rendered())
    assert paths == {
        f"candidates/sources/kernkonzept/{fx.SLUG_A}.md",
        f"candidates/sources/kernkonzept/{fx.SLUG_B}.md",
        "candidates/concepts/concept/system-kael.md",
        "candidates/concepts/character/juna.md",
        "candidates/concepts/rule/schleier.md",
    }


def test_source_frontmatter_takes_the_deterministic_fields_from_the_manifest():
    front = front_of(rendered()[f"candidates/sources/kernkonzept/{fx.SLUG_A}.md"])
    assert front["kind"] == "source" and front["status"] == "draft"
    assert front["drive_id"] == "1aaa" and front["sha256"] == "a" * 64
    assert front["tier"] == "T3-work" and front["category"] == "kernkonzept"
    assert front["language"] == "de" and front["ingested"] == INGESTED
    for field in wiki_schema.required_fields("source"):
        assert front.get(field), field


def test_concept_frontmatter_carries_the_contract_fields():
    front = front_of(rendered()["candidates/concepts/character/juna.md"])
    assert front["kind"] == "concept" and front["status"] == "draft"
    assert front["canon_status"] == "unverified" and front["table_status"] == "contradicted"
    assert front["sources"] == [fx.SLUG_A, fx.SLUG_B]
    assert front["disagreements"] == ["Juna's Kernwelt"]
    for field in wiki_schema.required_fields("concept"):
        assert front.get(field), field


def test_pages_carry_every_section_the_schema_declares():
    pages = rendered()
    source_sections = wiki_pages.sections(wiki_pages.split_frontmatter(pages[f"candidates/sources/kernkonzept/{fx.SLUG_A}.md"])[1])
    concept_sections = wiki_pages.sections(wiki_pages.split_frontmatter(pages["candidates/concepts/character/juna.md"])[1])
    assert list(source_sections) == wiki_schema.kind("source")["sections"]
    assert list(concept_sections) == wiki_schema.kind("concept")["sections"]


def test_a_source_links_the_concepts_that_list_it():
    body = wiki_pages.split_frontmatter(rendered()[f"candidates/sources/kernkonzept/{fx.SLUG_A}.md"])[1]
    entities = wiki_pages.sections(body)["Entities"]
    assert sorted(wiki_pages.wikilinks(entities)) == ["juna", "schleier", "system-kael"]


def test_key_claims_quote_the_cited_lines():
    body = wiki_pages.split_frontmatter(rendered()[f"candidates/sources/kernkonzept/{fx.SLUG_A}.md"])[1]
    claims = wiki_pages.sections(body)["Key claims"]
    assert "„Juna lebt in KW2.“" in claims
    assert f"^[{fx.FILE_A}:3-3]" in claims


def test_a_pending_disagreement_names_both_sources_and_its_resolution():
    body = wiki_pages.split_frontmatter(rendered()["candidates/concepts/character/juna.md"])[1]
    disagree = wiki_pages.sections(body)["Where they disagree"]
    assert f"[[{fx.SLUG_A}]] vs [[{fx.SLUG_B}]]" in disagree and "resolution: pending" in disagree


def test_a_disagreement_line_leaves_out_what_the_draft_left_empty():
    run = fx.handmade_compiled()
    run.concepts[1].disagreements[0].positions = []
    body = wiki_pages.split_frontmatter(
        candidates.render_pages(run, MANIFEST, INGESTED)["candidates/concepts/character/juna.md"])[1]
    line = wiki_pages.sections(body)["Where they disagree"].strip()
    assert " —  — " not in line and line.count("—") == 2
    assert line.endswith("^[Sources/drive/notiz-kael-b.md:3-3]")


def test_a_codex_reference_is_prefixed_when_the_glossary_knows_it_and_dropped_otherwise():
    known = frozenset({"juna", "kael"})
    assert candidates.codex_ref("juna", known) == "codex:juna"
    assert candidates.codex_ref("codex:juna", known) == "codex:juna"
    assert candidates.codex_ref("erfundener-begriff", known) == ""
    assert candidates.codex_ref("", known) == ""


def test_the_rendered_concept_carries_only_a_known_codex_reference():
    run = fx.handmade_compiled()
    run.concepts[1].codex_ref = "juna"
    run.concepts[2].codex_ref = "kein-eintrag"
    pages = candidates.render_pages(run, MANIFEST, INGESTED, codex_slugs=frozenset({"juna"}))
    assert front_of(pages["candidates/concepts/character/juna.md"])["codex_ref"] == "codex:juna"
    assert "codex_ref" not in front_of(pages["candidates/concepts/rule/schleier.md"])


def test_no_candidate_emits_the_canon_marker():
    assert all("[K]" not in text for text in rendered().values())


# --- the decisive check: the drafts lint ---------------------------------------------


def test_the_rendered_candidates_pass_the_candidate_lint(repo: Path):
    ctx = build_context(repo / "Wiki", repo)
    findings = [f.render() for rel in rendered() for f in wiki_lint.hook_findings(ctx, repo / "Wiki" / rel)]
    assert findings == []


def test_a_quote_outside_the_cited_lines_is_caught(repo: Path):
    page = repo / "Wiki/candidates" / f"{fx.SLUG_A}.md"
    page.write_text(page.read_text(encoding="utf-8").replace("„Juna lebt in KW2.“", "„Juna wohnt in KW9.“"),
                    encoding="utf-8")
    ctx = build_context(repo / "Wiki", repo)
    findings = [f.render() for f in wiki_lint.hook_findings(ctx, page)]
    assert any("is not inside the cited lines" in f for f in findings)


# --- edges, log, report ---------------------------------------------------------------


def test_one_supports_edge_per_cited_source_and_concept():
    records = candidates.edge_records(fx.handmade_compiled(), INGESTED)
    pairs = {(r["from"], r["to"]) for r in records}
    assert ("notiz-kael-a", "juna") in pairs and ("notiz-kael-b", "juna") in pairs
    assert len(records) == len(pairs)
    for record in records:
        assert record["type"] == "supports" and record["written_by"] == candidates.WRITER
        assert record["at"] == INGESTED and record["evidence"].startswith("^[Sources/drive/")
        assert record["confidence"] in wiki_schema.enum_values("confidence")


def test_edges_satisfy_the_edge_schema(repo: Path):
    path = repo / "Wiki/graph/edges.jsonl"
    cli.append_edges(repo, candidates.edge_records(fx.handmade_compiled(), INGESTED))
    ctx = build_context(repo / "Wiki", repo)
    problems = [p for record in ctx.edges for p in __import__(
        "tools.kpwiki.wiki_lint_rules", fromlist=["edge_problems"]).edge_problems(ctx, record)]
    assert path.is_file() and ctx.edges
    assert problems == []


def test_log_lines_follow_the_grammar_and_a_declared_writer():
    lines = candidates.log_entries(fx.handmade_compiled(), rendered(), INGESTED)
    ops, writers = wiki_schema.conventions()["log"]["ops"], wiki_schema.writers()["writers"]
    assert sum(line.count("] ingest |") for line in lines) == 5     # one per written page
    assert sum(line.count("] claim |") for line in lines) == 2      # reinforced + challenged
    for line in lines:
        match = wiki_pages.LOG_LINE_RE.match(line)
        assert match, line
        parsed = wiki_pages.parse_log_line(line, 1)
        assert parsed.op in ops and parsed.fields["skill"] in writers


def test_a_knowledge_diff_event_becomes_a_claim_line():
    lines = candidates.log_entries(fx.handmade_compiled(), {}, INGESTED)
    assert any(line.startswith(f"## [{INGESTED}] claim | juna reinforced:") for line in lines)
    assert any("juna challenged:" in line for line in lines)


def test_the_report_names_every_decision_and_the_contradiction():
    report = "\n".join(candidates.knowledge_diff_report(fx.handmade_compiled(), MANIFEST))
    assert "create system-kael" in report.replace("  ", " ")
    assert "flag   juna" in report and "conflicts:" in report
    assert "contradicted (a disagreement is pending): juna" in report


def test_a_triage_that_disagrees_with_the_manifest_is_reported_not_applied():
    run = fx.handmade_compiled()
    run.extractions[0].triage = run.extractions[0].triage.model_copy(update={"tier": "T2-theory"})
    notes = candidates.triage_disagreements(run, MANIFEST)
    assert notes == [f"{fx.SLUG_A}: triage says tier=T2-theory, manifest says T3-work"]
    front = front_of(candidates.render_pages(run, MANIFEST, INGESTED)[f"candidates/sources/kernkonzept/{fx.SLUG_A}.md"])
    assert front["tier"] == "T3-work"


# --- selection ------------------------------------------------------------------------


def options(**kwargs) -> argparse.Namespace:
    base = {"slug": [], "category": None, "tier": None, "batch": 25}
    base.update(kwargs)
    return argparse.Namespace(**base)


def manifest_with(**extra) -> dict[str, dict]:
    records = {slug: dict(record) for slug, record in MANIFEST.items()}
    records.update(extra)
    return records


def test_selection_filters_by_category_and_orders_by_index_date():
    kept, notes = cli.select(manifest_with(), options(category="kernkonzept"))
    assert [r["slug"] for r in kept] == [fx.SLUG_A, fx.SLUG_B] and notes == []
    assert cli.select(manifest_with(), options(category="audit"))[0] == []


def test_unexported_truncated_and_excluded_tiers_are_dropped_with_a_reason():
    extra = {
        "nix": {"slug": "nix", "title": "N", "export_path": "", "tier": "T3-work", "category": "kernkonzept"},
        "cut": {"slug": "cut", "title": "C", "export_path": "Sources/drive/cut.md", "truncated": True,
                "tier": "T3-work", "category": "kernkonzept"},
        "dup": {"slug": "dup", "title": "D", "export_path": "Sources/drive/dup.md", "tier": "T0-duplicate",
                "category": "kernkonzept"},
    }
    kept, notes = cli.select(manifest_with(**extra), options())
    assert {r["slug"] for r in kept} == {fx.SLUG_A, fx.SLUG_B}
    assert "nix: not exported yet" in notes
    assert "cut: export is truncated, never ingested" in notes
    assert "dup: tier T0-duplicate is not ingested" in notes


def test_the_batch_limit_leaves_the_rest_for_a_later_run():
    kept, notes = cli.select(manifest_with(), options(batch=1))
    assert [r["slug"] for r in kept] == [fx.SLUG_A]
    assert any("1 record(s) left for a later run" in n for n in notes)


def test_an_unknown_slug_is_named():
    kept, notes = cli.select(manifest_with(), options(slug=["kein-slug", fx.SLUG_B]))
    assert [r["slug"] for r in kept] == [fx.SLUG_B] and "unknown slug: kein-slug" in notes


def test_excluded_tiers_come_from_the_schema():
    assert cli.excluded_tiers() == {"T0-duplicate", "T1-superseded", "T4-out-of-scope"}


def test_dry_run_writes_nothing_and_an_empty_selection_exits_one(repo: Path, capsys):
    (repo / "Sources").mkdir(exist_ok=True)
    (repo / cli.MANIFEST_REL).write_text("".join(json.dumps(r) + "\n" for r in MANIFEST.values()), encoding="utf-8")
    before = sorted(p.name for p in (repo / "Wiki/candidates").iterdir())
    assert cli.main(["--root", str(repo), "--category", "kernkonzept"]) == 0
    assert "dry run: no LM call" in capsys.readouterr().out
    assert sorted(p.name for p in (repo / "Wiki/candidates").iterdir()) == before
    assert cli.main(["--root", str(repo), "--category", "audit"]) == 1
