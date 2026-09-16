"""CLI modes of scripts/wiki_lint.py: --json, --health, --hook, --fix, --suggest.

Reuses the clean fixture from ``tests/test_wiki_lint.py``.

    python3 -m pytest tests/test_wiki_lint_modes.py -q -W error::RuntimeWarning
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from test_wiki_lint import (CONCEPT_FRONT, CONCEPT_BODY, append_body, lint, make_wiki,  # noqa: E402
                            set_front, wiki_lint, wiki_pages, write_page)


def run(repo: Path, *args: str) -> int:
    return wiki_lint.main([*args, "--repo-root", str(repo), "--wiki-root", str(repo / "Wiki")])


def remove_reverse_link(repo: Path) -> Path:
    page = repo / "Wiki/concepts/kohaerenz.md"
    page.write_text(page.read_text(encoding="utf-8").replace("- [[frage-eins]]\n", ""), encoding="utf-8")
    return page


def test_json_output(tmp_path, capsys):
    repo = make_wiki(tmp_path)
    append_body(repo, "Wiki/sources/quelle-eins.md", "\n[[nirgendwo]]\n")
    assert run(repo, "--json") == 1
    data = json.loads(capsys.readouterr().out)
    assert data["summary"]["errors"] == 1
    assert {"rule", "severity", "path", "line", "message"} <= set(data["findings"][0])


def test_health_output(tmp_path, capsys):
    repo = make_wiki(tmp_path)
    assert run(repo, "--health") == 0
    out = capsys.readouterr().out
    assert out.startswith("0 errors, 0 warnings,")
    assert "sources ingested: 1 / manifest 2" in out and "open questions by axis: incompleteness=1" in out
    assert "pages by kind: concept=1 question=1 source=1 synthesis=1" in out


def test_health_on_missing_wiki_is_clean(tmp_path, capsys):
    assert wiki_lint.main(["--health", "--repo-root", str(tmp_path), "--wiki-root", str(tmp_path / "nope")]) == 0
    assert capsys.readouterr().out.startswith("0 errors, 0 warnings, 0 info")


def test_hook_exits_zero_and_reports_only_that_file(tmp_path, capsys):
    repo = make_wiki(tmp_path)
    append_body(repo, "Wiki/concepts/kohaerenz.md", "\nDrift [K] emitted.\n")
    append_body(repo, "Wiki/sources/quelle-eins.md", "\n[[nirgendwo]]\n")
    assert run(repo, "--hook", str(repo / "Wiki/concepts/kohaerenz.md")) == 0
    out = capsys.readouterr().out
    assert "no-k-marker-outside-canon Wiki/concepts/kohaerenz.md" in out and "nirgendwo" not in out


def test_hook_on_candidate_runs_the_write_time_subset(tmp_path, capsys):
    repo = make_wiki(tmp_path)
    page = write_page(repo, "Wiki/candidates/kandidat.md",
                      {**CONCEPT_FRONT, "slug": "kandidat", "status": "draft", "kind_detail": "nope"},
                      CONCEPT_BODY + "\n[[nirgendwo]]\n")
    assert run(repo, "--hook", str(page)) == 0
    out = capsys.readouterr().out
    assert "enum Wiki/candidates/kandidat.md" in out and "broken-link" not in out


def test_fix_dry_run_writes_nothing(tmp_path, capsys):
    repo = make_wiki(tmp_path)
    page = remove_reverse_link(repo)
    before = page.read_text(encoding="utf-8")
    assert run(repo, "--fix", "--dry-run") == 0
    out = capsys.readouterr().out
    assert "would" in out and "[[frage-eins]]" in out
    assert page.read_text(encoding="utf-8") == before


def test_fix_writes_reverse_link_and_defaults(tmp_path, capsys):
    repo = make_wiki(tmp_path)
    page = remove_reverse_link(repo)
    set_front(repo, "Wiki/sources/quelle-eins.md", truncated=None)
    set_front(repo, "Wiki/concepts/kohaerenz.md", canon_status=None)
    run(repo, "--fix")
    front, body = wiki_pages.split_frontmatter(page.read_text(encoding="utf-8"))
    assert "[[frage-eins]]" in wiki_pages.sections(body)["Open questions"]
    assert front["canon_status"] == "unverified"
    assert wiki_pages.split_frontmatter((repo / "Wiki/sources/quelle-eins.md").read_text())[0]["truncated"] is False
    assert not [f for f in lint(repo) if f.rule in ("xref-symmetry", "required-field")]
    assert (repo / "Wiki/graph/coverage.json").is_file()


def test_suggest_lists_orphan_mentions(tmp_path, capsys):
    repo = make_wiki(tmp_path)
    write_page(repo, "Wiki/concepts/einsam.md", {**CONCEPT_FRONT, "slug": "einsam", "title": "Einsam"}, CONCEPT_BODY)
    append_body(repo, "Wiki/sources/quelle-eins.md", "\nThe einsam idea in plain text.\n")
    run(repo, "--suggest")
    out = capsys.readouterr().out
    assert "orphan Wiki/concepts/einsam.md: link [[einsam]] from Wiki/sources/quelle-eins.md" in out


def test_unknown_rule_selection_is_rejected(tmp_path):
    repo = make_wiki(tmp_path)
    try:
        run(repo, "--rules", "nope")
    except SystemExit as exc:
        assert "unknown rules: nope" in str(exc)
    else:
        raise AssertionError("an unknown rule id must be rejected")
