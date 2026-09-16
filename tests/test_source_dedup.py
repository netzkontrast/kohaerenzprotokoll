"""Tests for scripts/source_dedup.py with temporary manifest + export trees."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT))

import source_dedup as dedup  # noqa: E402
from tools.kpwiki import wiki_schema  # noqa: E402

BASE_TEXT = " ".join(f"wort{i}" for i in range(60))


def record(slug: str, title: str, date: str, body: str | None, **extra) -> tuple[dict, str | None]:
    rec = {"drive_id": f"id-{slug}", "title": title, "slug": slug, "category": "kernkonzept",
           "tier": "T3-work", "index_date": date, "export_path": f"Sources/drive/{slug}.md" if body is not None else "",
           "sha256": "", "exported_at": "", "duplicate_of": "", "superseded_by": "", "truncated": False}
    rec.update(extra)
    return rec, body


def make_tree(tmp_path: Path, entries: list[tuple[dict, str | None]]) -> Path:
    (tmp_path / "Sources/drive").mkdir(parents=True)
    for rec, body in entries:
        if body is not None:
            (tmp_path / rec["export_path"]).write_text(body, encoding="utf-8")
    manifest = tmp_path / dedup.MANIFEST_RELATIVE
    manifest.write_text("".join(json.dumps(rec) + "\n" for rec, _ in entries), encoding="utf-8")
    return manifest


def read(manifest: Path) -> dict[str, dict]:
    return {json.loads(line)["slug"]: json.loads(line) for line in manifest.read_text().splitlines()}


def test_tier_names_come_from_schema():
    tiers = wiki_schema.enum_values("tier")
    assert dedup.DUPLICATE_TIER in tiers and dedup.SUPERSEDED_TIER in tiers
    assert dedup.DUPLICATE_TIER.startswith("T0-") and dedup.SUPERSEDED_TIER.startswith("T1-")


def test_byte_equal_marks_newer_record_as_duplicate(tmp_path):
    manifest = make_tree(tmp_path, [record("b-copy", "B", "2025-06-02", BASE_TEXT),
                                    record("a-orig", "B", "2025-06-01", BASE_TEXT)])
    assert dedup.main(["--root", str(tmp_path)]) == 0
    recs = read(manifest)
    assert recs["b-copy"]["tier"] == dedup.DUPLICATE_TIER and recs["b-copy"]["duplicate_of"] == "a-orig"
    assert recs["a-orig"]["tier"] == "T3-work" and recs["a-orig"]["duplicate_of"] == ""


def test_byte_equal_same_date_breaks_tie_by_slug(tmp_path):
    manifest = make_tree(tmp_path, [record("zeta", "Z", "2025-06-01", BASE_TEXT),
                                    record("alpha", "A", "2025-06-01", BASE_TEXT)])
    dedup.main(["--root", str(tmp_path)])
    recs = read(manifest)
    assert recs["zeta"]["duplicate_of"] == "alpha" and recs["alpha"]["tier"] == "T3-work"


def test_near_duplicate_supersedes_older_record(tmp_path):
    manifest = make_tree(tmp_path, [record("draft", "Entwurf", "2025-06-01", BASE_TEXT),
                                    record("final", "Fassung", "2025-06-05", BASE_TEXT + " neu ende")])
    dedup.main(["--root", str(tmp_path)])
    recs = read(manifest)
    assert recs["draft"]["tier"] == dedup.SUPERSEDED_TIER and recs["draft"]["superseded_by"] == "final"
    assert recs["final"]["tier"] == "T3-work" and recs["final"]["superseded_by"] == ""


def test_same_title_with_newer_date_supersedes(tmp_path):
    manifest = make_tree(tmp_path, [record("plan-2", "Plan  Köln", "2025-07-01", "ganz anderer text hier"),
                                    record("plan", "plan köln", "2025-05-01", "ein völlig verschiedener inhalt")])
    dedup.main(["--root", str(tmp_path)])
    recs = read(manifest)
    assert recs["plan"]["superseded_by"] == "plan-2" and recs["plan-2"]["tier"] == "T3-work"


def test_same_date_never_supersedes(tmp_path):
    manifest = make_tree(tmp_path, [record("x", "Same", "2025-06-01", BASE_TEXT),
                                    record("y", "Same", "2025-06-01", BASE_TEXT + " mehr")])
    dedup.main(["--root", str(tmp_path)])
    assert all(r["tier"] == "T3-work" for r in read(manifest).values())


def test_chain_points_to_nearest_newer(tmp_path):
    manifest = make_tree(tmp_path, [record("v1", "V", "2025-01-01", BASE_TEXT),
                                    record("v2", "V", "2025-02-01", BASE_TEXT + " a"),
                                    record("v3", "V", "2025-03-01", BASE_TEXT + " a b")])
    dedup.main(["--root", str(tmp_path)])
    recs = read(manifest)
    assert recs["v1"]["superseded_by"] == "v2" and recs["v2"]["superseded_by"] == "v3"
    assert recs["v3"]["tier"] == "T3-work"


def test_unrelated_texts_stay_untouched(tmp_path):
    manifest = make_tree(tmp_path, [record("p", "Physik", "2025-01-01", "eins zwei drei vier fünf sechs sieben acht neun"),
                                    record("q", "Psychologie", "2025-02-01", "zehn elf zwölf dreizehn vierzehn fünfzehn")])
    assert dedup.main(["--root", str(tmp_path)]) == 0
    assert all(r["tier"] == "T3-work" for r in read(manifest).values())


def test_truncated_missing_and_unexported_records_are_skipped(tmp_path, capsys):
    entries = [record("full", "T", "2025-01-01", BASE_TEXT),
               record("cut", "T", "2025-02-01", BASE_TEXT, truncated=True),
               record("gone", "T", "2025-03-01", None, export_path="Sources/drive/gone.md"),
               record("never", "T", "2025-04-01", None)]
    manifest = make_tree(tmp_path, entries)
    dedup.main(["--root", str(tmp_path)])
    assert "1 exported files hashed" in capsys.readouterr().out
    assert all(r["tier"] == "T3-work" for r in read(manifest).values())


def test_rerun_is_idempotent_and_check_reflects_state(tmp_path, capsys):
    make_tree(tmp_path, [record("b", "B", "2025-06-02", BASE_TEXT), record("a", "B", "2025-06-01", BASE_TEXT)])
    assert dedup.main(["--root", str(tmp_path), "--check"]) == 1
    assert dedup.main(["--root", str(tmp_path)]) == 0
    assert dedup.main(["--root", str(tmp_path), "--check"]) == 0
    assert dedup.main(["--root", str(tmp_path)]) == 0
    assert "0 record(s) would change" in capsys.readouterr().out


def test_dry_run_writes_nothing(tmp_path, capsys):
    manifest = make_tree(tmp_path, [record("b", "B", "2025-06-02", BASE_TEXT), record("a", "B", "2025-06-01", BASE_TEXT)])
    before = manifest.read_text()
    assert dedup.main(["--root", str(tmp_path), "--dry-run"]) == 0
    assert "b: T3-work -> T0-duplicate duplicate_of=a" in capsys.readouterr().out
    assert manifest.read_text() == before


def test_stats_reports_counts(tmp_path, capsys):
    make_tree(tmp_path, [record("b", "B", "2025-06-02", BASE_TEXT), record("a", "B", "2025-06-01", BASE_TEXT)])
    assert dedup.main(["--root", str(tmp_path), "--stats"]) == 0
    out = capsys.readouterr().out
    assert "exported files: 2" in out and f"{dedup.DUPLICATE_TIER}: 1" in out


def test_missing_manifest_exits_2(tmp_path):
    assert dedup.main(["--root", str(tmp_path)]) == 2


def test_shingles_and_jaccard():
    a = dedup.shingles(BASE_TEXT)
    assert len(a) == 60 - dedup.SHINGLE_WORDS + 1
    assert dedup.jaccard(a, a) == 1.0
    assert dedup.jaccard(a, dedup.shingles("x y z")) == 0.0
    assert dedup.jaccard(frozenset(), frozenset()) == 0.0
    assert dedup.shingles("") == frozenset() and dedup.shingles("kurz") == frozenset({("kurz",)})


def test_normalise_title_ignores_case_spacing_and_punctuation():
    assert dedup.normalise_title("Kohärenz  Protokoll: Plan!") == dedup.normalise_title("kohärenz protokoll plan")


def test_real_repo_has_no_exports_and_check_passes(capsys):
    assert dedup.main(["--check"]) == 0
    assert "0 exported files hashed" in capsys.readouterr().out
