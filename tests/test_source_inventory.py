"""Tests for scripts/source_inventory.py: D-W9 exclusion, stable slugs, export-state carry-over."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT))

import source_inventory as inv  # noqa: E402
from tools.kpwiki import wiki_schema  # noqa: E402

# The appendix comes FIRST here so that dropping it before disambiguation
# would change the surviving slug — the contract says it must not.
INDEX_TEXT = """## Anhang — nicht eindeutig zugeordnet

- [Alpha](https://drive.google.com/open?id=CCC1) · 2025-06-01

## Kernkonzept, Synthesen & Gesamtdokumente

- [Alpha](https://drive.google.com/open?id=AAA1) · 2025-05-04
- [Beta.docx](https://drive.google.com/open?id=BBB1) · 2025-05-03 · 2 Kopien
"""


def parsed() -> list[dict]:
    records = inv.parse_index(INDEX_TEXT)
    inv.disambiguate_slugs(records)
    return records


def test_t4_rows_dropped_by_default():
    records = inv.select_in_scope(parsed(), include_out_of_scope=False)
    assert [r["drive_id"] for r in records] == ["AAA1", "BBB1"]
    assert all(r["tier"] != inv.OUT_OF_SCOPE_TIER for r in records)


def test_t4_rows_kept_on_request():
    records = inv.select_in_scope(parsed(), include_out_of_scope=True)
    assert [r["drive_id"] for r in records] == ["CCC1", "AAA1", "BBB1"]


def test_surviving_slugs_do_not_change_when_appendix_is_dropped():
    full = {r["drive_id"]: r["slug"] for r in parsed()}
    kept = {r["drive_id"]: r["slug"] for r in inv.select_in_scope(parsed(), False)}
    assert full["CCC1"] == "alpha" and full["AAA1"] == "alpha-2"
    assert kept["AAA1"] == "alpha-2"


def test_record_has_new_fields_in_order():
    record = parsed()[1]
    keys = list(record)
    assert keys[-3:] == ["duplicate_of", "superseded_by", "truncated"]
    assert record["superseded_by"] == "" and record["truncated"] is False


def test_carry_over_keeps_export_fields_and_dedup_tier():
    records = inv.select_in_scope(parsed(), False)
    existing = [{"drive_id": "BBB1", "tier": "T0-duplicate", "export_path": "Sources/drive/beta.md",
                 "sha256": "ab" * 32, "exported_at": "2026-09-16", "duplicate_of": "alpha-2", "truncated": True}]
    inv.carry_over_export_state(records, existing)
    beta = next(r for r in records if r["drive_id"] == "BBB1")
    assert beta["tier"] == "T0-duplicate" and beta["duplicate_of"] == "alpha-2"
    assert beta["export_path"] == "Sources/drive/beta.md" and beta["truncated"] is True
    assert beta["superseded_by"] == ""


def test_carry_over_never_keeps_an_index_tier():
    records = inv.select_in_scope(parsed(), False)
    inv.carry_over_export_state(records, [{"drive_id": "AAA1", "tier": "T2-theory"}])
    assert next(r for r in records if r["drive_id"] == "AAA1")["tier"] == "T3-work"


def test_section_mapping_matches_schema_enums():
    inv.validate_mapping()
    assert inv.OUT_OF_SCOPE_TIER in wiki_schema.enum_values("tier")
    assert inv.DEDUP_TIERS == {"T0-duplicate", "T1-superseded"}


def test_real_manifest_is_the_680_in_scope_records():
    lines = (ROOT / "Sources/manifest.jsonl").read_text(encoding="utf-8").splitlines()
    records = [json.loads(line) for line in lines]
    assert len(records) == 680
    assert not any(r["tier"] == inv.OUT_OF_SCOPE_TIER for r in records)
    assert all("superseded_by" in r and r["truncated"] is False for r in records)
    assert len({r["slug"] for r in records}) == 680


def test_check_passes_on_real_repo(capsys):
    assert inv.main(["--check"]) == 0
    assert "manifest up to date" in capsys.readouterr().out


def test_stats_reports_dropped_rows(capsys):
    assert inv.main(["--stats"]) == 0
    out = capsys.readouterr().out
    assert "documents: 680" in out and "(D-W9): 13" in out
