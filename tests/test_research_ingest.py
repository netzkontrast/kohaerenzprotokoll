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

from tools.kpwiki import candidates, programs, wiki_lint_rules, wiki_pages, wiki_schema  # noqa: E402
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
        # Presence, not truthiness: chapter_start is legally 0.
        assert front.get(field) not in (None, ""), field


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


def ledger_body_for(run, concept_slug: str = "juna") -> str:
    """The concept-tree ledger page for one concept, as text."""
    store, _, _ = cli.record_contradictions({}, run, INGESTED, {})
    path = next(p for p in candidates.ledger_pages(store, INGESTED)
                if p.endswith(f"/contradictions/concept/{concept_slug}.md"))
    return wiki_pages.split_frontmatter(candidates.ledger_pages(store, INGESTED)[path])[1]


def test_a_pending_disagreement_names_both_sources_in_the_ledger():
    """It left the concept page; it must still say who claimed what."""
    open_items = wiki_pages.sections(ledger_body_for(fx.handmade_compiled()))["Open contradictions"]
    assert f"[[{fx.SLUG_A}]]" in open_items and f"[[{fx.SLUG_B}]]" in open_items
    assert "KW2" in open_items and "KW3" in open_items


def test_a_ledger_entry_leaves_out_what_the_draft_left_empty():
    run = fx.handmade_compiled()
    run.concepts[1].disagreements[0].positions = []
    entry = wiki_pages.sections(ledger_body_for(run))["Open contradictions"]
    assert " —  — " not in entry and "— \n" not in entry
    assert f"[[{fx.SLUG_B}]]" in entry


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
    page = repo / "Wiki/candidates/sources/kernkonzept" / f"{fx.SLUG_A}.md"
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


def test_the_write_path_reaches_batchcompile_with_the_chosen_merge_role(repo: Path, monkeypatch):
    """--write is never exercised offline, so its wiring needs its own test.

    A NameError between parsing the flags and the first LM call would survive
    every other test in this file: they all stop at the dry-run branch.
    """
    (repo / "Sources").mkdir(exist_ok=True)
    (repo / cli.MANIFEST_REL).write_text(
        "".join(json.dumps(r) + "\n" for r in MANIFEST.values()), encoding="utf-8")
    seen = {}

    class Recorder:
        def __init__(self, merge_role: str = "auto", **rest):
            seen["merge_role"] = merge_role
            seen.update(rest)

        def __call__(self, **kwargs):
            raise SystemExit(0)                      # stop before any LM call

    monkeypatch.setattr(cli, "BatchCompile", Recorder)
    monkeypatch.setattr(cli.lm, "configure", lambda role="task": None)
    with pytest.raises(SystemExit):
        cli.main(["--root", str(repo), "--category", "kernkonzept",
                  "--write", "--merge-role", "worker"])
    assert seen["merge_role"] == "worker"
    # The chunk loop must hand BatchCompile both carriers, or chunking loses history.
    assert callable(seen["prior_claims"]) and callable(seen["load_extraction"])


# --- basic ingest: sources only, no concept layer --------------------------------------


def stub_source_ingest(monkeypatch, calls: list[str]):
    """Replace SourceIngest with a recorder, so the path runs without an LM."""
    class Recorder:
        def __call__(self, *, source_file, title, category_hint, body, glossary_terms):
            calls.append(source_file)
            return dspy.Prediction(triage=fx.extractions()[0].triage,
                                   claims=list(fx.extractions()[0].claims))

    monkeypatch.setattr(cli, "SourceIngest", Recorder)
    monkeypatch.setattr(cli.lm, "configure", lambda role="task": None)


def basic_ingest(repo: Path, monkeypatch, calls: list[str]) -> int:
    (repo / cli.MANIFEST_REL).write_text(
        "".join(json.dumps(r) + "\n" for r in MANIFEST.values()), encoding="utf-8")
    stub_source_ingest(monkeypatch, calls)
    return cli.main(["--root", str(repo), "--category", "kernkonzept",
                     "--extract-only", "--write"])


def candidate_state(repo: Path) -> dict[str, str]:
    """Every candidate page and its text — the fixture pre-writes some, so diff."""
    root = repo / "Wiki/candidates"
    return {path.relative_to(root).as_posix(): path.read_text(encoding="utf-8")
            for path in root.rglob("*.md")}


def test_basic_ingest_writes_source_pages_and_touches_no_concept_page(repo: Path, monkeypatch,
                                                                      capsys):
    before = candidate_state(repo)
    calls: list[str] = []
    assert basic_ingest(repo, monkeypatch, calls) == 0
    capsys.readouterr()
    after = candidate_state(repo)
    changed = {path for path in after if before.get(path) != after[path]}
    assert changed, "the basic ingest wrote nothing"
    assert all(path.startswith("sources/") for path in changed), sorted(changed)
    assert len(calls) == 2                                   # one per source, nothing batch-wide


def test_basic_ingest_caches_claims_for_the_deferred_concept_layer(repo: Path, monkeypatch, capsys):
    basic_ingest(repo, monkeypatch, [])
    capsys.readouterr()
    cached = sorted((repo / cli.EXTRACTIONS_REL).glob("*.json"))
    assert [p.stem for p in cached] == sorted(MANIFEST)
    restored = cli.cached_extraction(repo, cached[0].stem)
    assert restored is not None and restored.claims


def test_a_second_basic_ingest_extracts_nothing_again(repo: Path, monkeypatch, capsys):
    """Extraction depends on the document alone, so it is paid once."""
    basic_ingest(repo, monkeypatch, [])
    capsys.readouterr()
    again: list[str] = []
    assert basic_ingest(repo, monkeypatch, again) == 0
    assert again == [], "a cached source was extracted a second time"
    assert "cached" in capsys.readouterr().out


# --- chunked ingest: the default, and the invariant that makes it safe ------------------


def test_chunking_splits_sources_and_defaults_to_the_schema_value():
    ns = cli.build_parser().parse_args([])
    assert ns.chunk == wiki_schema.conventions()["batches"]["chunk_size"]
    assert ns.merge_role == "auto"
    sizes = [len(g) for g in cli.chunks_of(list(range(7)), 3)]
    assert sizes == [3, 3, 1]


def test_merge_is_routed_by_whether_a_contradiction_is_possible():
    """43% of the pilot's merges were on concepts that cannot disagree."""
    one = [programs.ClaimRef(1, "src-a", 0, "x")]
    two = one + [programs.ClaimRef(2, "src-b", 0, "y")]
    assert programs.merge_role_for(two, "auto") == "task"
    assert programs.merge_role_for(one, "auto") == "worker"
    assert programs.merge_role_for(one, "task") == "task"      # an explicit choice still wins
    assert programs.merge_role_for(two, "worker") == "worker"


def test_prior_claims_join_this_chunk_without_duplicating_a_claim():
    here = [programs.ClaimRef(1, "src-a", 0, "x")]
    prior = [programs.ClaimRef(7, "src-a", 0, "x"), programs.ClaimRef(8, "src-b", 2, "z")]
    joined = programs.with_prior(here, prior)
    assert [(r.source, r.index) for r in joined] == [("src-a", 0), ("src-b", 2)]


def test_the_concept_index_round_trips_and_feeds_the_next_chunk(repo: Path):
    """The invariant chunking depends on: a concept keeps every claim it was given."""
    extraction = fx.extractions()[0]
    cli.cache_extraction(repo, extraction)
    index = {"system-kael": [f"{extraction.source}:0"]}
    cli.save_concept_index(repo, index)
    assert cli.load_concept_index(repo) == index
    resolved = cli.prior_claims_resolver(repo, index)("system-kael")
    assert [(r.source, r.index) for r in resolved] == [(extraction.source, 0)]
    assert cli.prior_claims_resolver(repo, index)("never-seen") == []


def test_a_later_chunk_inherits_the_claims_an_earlier_one_assigned(repo: Path):
    """Chunk 2 must merge chunk 1's claims too, or a cross-chunk clash is invisible."""
    for extraction in fx.extractions():
        cli.cache_extraction(repo, extraction)
    run = fx.handmade_compiled()
    index = cli.record_concept_claims({}, run, {})
    assert index, "no concept claimed anything"
    carried = cli.record_concept_claims(index, run, {})
    assert carried == index, "re-recording the same chunk duplicated claims"
    slug = next(iter(index))
    assert cli.prior_claims_resolver(repo, index)(slug), f"{slug} resolved to no prior claims"


# --- the contradiction ledger ----------------------------------------------------------


def contested_draft():
    return [c for c in fx.concepts() if c.disagreements][0]


def test_a_concept_page_states_no_contradiction():
    """The wiki asserts what the sources agree on; clashes live in the ledger."""
    body = candidates.concept_body(contested_draft(), INGESTED)
    assert "Where they disagree" not in body
    assert "Where they disagree" not in wiki_schema.kind("concept")["sections"]
    for position in contested_draft().disagreements[0].positions:
        assert f"— {position}" not in body, f"position {position!r} leaked onto the page"


def test_the_ledger_has_a_tree_per_concept_and_per_entity():
    draft = contested_draft()
    subjects = candidates.ledger_subjects(draft)
    assert ("concept", draft.slug, draft.slug) in subjects
    assert any(kind == "entity" for kind, _, _ in subjects), "no entity tree"
    store, added, _ = cli.record_contradictions({}, fx.handmade_compiled(), INGESTED, {})
    assert added
    paths = sorted(candidates.ledger_pages(store, INGESTED))
    assert any("/contradictions/concept/" in p for p in paths), paths
    assert any("/contradictions/entity/" in p for p in paths), paths


def test_the_ledger_never_forgets_a_recorded_contradiction():
    """Append-only: re-recording the same run adds nothing and removes nothing."""
    run = fx.handmade_compiled()
    store, added, _ = cli.record_contradictions({}, run, INGESTED, {})
    again, added_again, _ = cli.record_contradictions(store, run, "2026-10-01", {})
    assert added_again == 0
    assert again == store


def test_settling_a_contradiction_moves_it_but_keeps_it():
    run = fx.handmade_compiled()
    store, _, _ = cli.record_contradictions({}, run, INGESTED, {})
    settled = run.model_copy(deep=True)
    for draft in settled.concepts:
        for item in draft.disagreements:
            item.resolution = "both-valid"
    store, added, changed = cli.record_contradictions(store, settled, INGESTED, {})
    assert added == 0 and changed > 0
    page = next(t for p, t in candidates.ledger_pages(store, INGESTED).items()
                if "/concept/" in p)
    topic = contested_draft().disagreements[0].topic
    assert topic in page, "a settled contradiction vanished from its ledger"
    assert "all-resolved" in page


def test_every_open_contradiction_raises_a_question():
    """The ledger remembers; a question is what puts it on a worklist."""
    run = fx.handmade_compiled()
    slugs, pages = cli.open_questions_for(run, INGESTED)
    pending = [d for c in run.concepts for d in c.disagreements
               if d.resolution == candidates.PENDING]
    assert len(slugs) == len(pending) and len(pages) == len(pending)
    assert all("/questions/incorrectness/" in path for path in pages), sorted(pages)


def test_the_ledger_store_round_trips_through_disk(repo: Path):
    store, _, _ = cli.record_contradictions({}, fx.handmade_compiled(), INGESTED, {})
    cli.save_ledger(repo, store)
    assert cli.load_ledger(repo) == store


# --- what the first live probe exposed -------------------------------------------------


def test_a_verbatim_quote_survives_a_typographic_quotation_mark():
    """The export writes „…“ and the model writes "…"; the quote is the same.

    This was the largest defect class in the 2026-09-16 probe: 40 of its 46
    citation failures were the lint refusing a quote over its glyphs.
    """
    cited = ['Er nennt es (dem „Nichts-Rauschen“) und meint es so.']
    assert wiki_lint_rules.quote_is_cited('(dem „Nichts-Rauschen") und meint es so.', cited)
    assert wiki_lint_rules.quote_is_cited('(dem "Nichts-Rauschen") und meint es so.', cited)
    # A curly apostrophe is the same character as a straight one.
    assert wiki_lint_rules.quote_is_cited("Kael’s Kernwelt", ["about Kael's Kernwelt here"])
    # Enclosing marks are stripped before comparison, so the term matches
    # however it was quoted — what must still match is the wording itself.
    assert wiki_lint_rules.quote_is_cited("'Nichts-Rauschen'", cited)
    assert not wiki_lint_rules.quote_is_cited("Nichts-Rauschens", cited)


def test_a_quote_may_carry_the_sentence_s_own_punctuation():
    """A page writing "Moonshine-Link," quotes a source reading "Moonshine-Link"."""
    cited = ['her connection via the "Moonshine-Link" is positioned as a catalyst']
    assert wiki_lint_rules.quote_is_cited("Moonshine-Link,", cited)
    assert wiki_lint_rules.quote_is_cited("Moonshine-Link", cited)


def test_relaxing_the_quote_check_still_rejects_a_fabrication():
    """The point of the rule survives: invented wording never passes."""
    cited = ['her connection via the "Moonshine-Link" is positioned as a catalyst']
    assert not wiki_lint_rules.quote_is_cited("Moonshine-Bridge", cited)
    assert not wiki_lint_rules.quote_is_cited("positioned as a saviour", cited)
    assert not wiki_lint_rules.quote_is_cited("", cited)


def test_a_concept_whose_slug_is_a_codex_entry_links_to_it():
    """kiko, lex and nyx shared a codex slug and carried no codex_ref."""
    assert candidates.codex_ref("", frozenset({"kiko"}), "kiko") == "codex:kiko"
    assert candidates.codex_ref("juna", frozenset({"juna", "kiko"}), "kiko") == "codex:juna"
    assert candidates.codex_ref("", frozenset({"kiko"}), "unknown-slug") == ""
