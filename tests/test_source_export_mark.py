"""Tests for scripts/source_export_mark.py against a temporary Sources/ tree."""
from __future__ import annotations

import base64
import hashlib
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import source_export_mark as mark  # noqa: E402

LONG_BODY = "# Titel\r\n\r\n" + "\r\n".join(f"Zeile {i} mit etwas Text.   " for i in range(40)) + "\r\n"


@pytest.fixture
def tree(tmp_path, monkeypatch):
    manifest = tmp_path / "Sources" / "manifest.jsonl"
    manifest.parent.mkdir(parents=True)
    records = [{"drive_id": "id-a", "slug": "alpha", "title": "A", "tier": "T3-work", "export_path": "",
                "sha256": "", "exported_at": "", "truncated": False},
               {"drive_id": "id-b", "slug": "beta", "title": "B", "tier": "T2-theory", "export_path": "",
                "sha256": "", "exported_at": "", "truncated": False}]
    manifest.write_text("".join(json.dumps(r) + "\n" for r in records), encoding="utf-8")
    monkeypatch.setattr(mark, "ROOT", tmp_path)
    monkeypatch.setattr(mark, "MANIFEST", manifest)
    monkeypatch.setattr(mark, "DRIVE_DIR", tmp_path / "Sources" / "drive")
    return tmp_path


def records(tree: Path) -> dict[str, dict]:
    return {json.loads(l)["slug"]: json.loads(l) for l in (tree / "Sources/manifest.jsonl").read_text().splitlines()}


def test_json_result_is_normalised_written_and_marked(tree, capsys):
    saved = tree / "result.txt"
    saved.write_text(json.dumps({"fileContent": LONG_BODY}), encoding="utf-8")
    assert mark.main(["--slug", "alpha", "--from-json", str(saved), "--date", "2026-09-16"]) == 0
    exported = tree / "Sources/drive/alpha.md"
    body = exported.read_bytes()
    assert b"\r" not in body and body.endswith(b"Text.\n") and b"Text.   " not in body
    rec = records(tree)["alpha"]
    assert rec["export_path"] == "Sources/drive/alpha.md"
    assert rec["sha256"] == hashlib.sha256(body).hexdigest()
    assert rec["exported_at"] == "2026-09-16" and rec["truncated"] is False
    assert records(tree)["beta"]["export_path"] == ""
    assert "alpha:" in capsys.readouterr().out


def test_other_lines_are_kept_byte_for_byte(tree):
    before = (tree / "Sources/manifest.jsonl").read_text().splitlines()
    text = tree / "body.md"
    text.write_text(LONG_BODY, encoding="utf-8")
    mark.main(["--slug", "beta", "--from-text", str(text)])
    after = (tree / "Sources/manifest.jsonl").read_text().splitlines()
    assert after[0] == before[0] and len(after) == 2


def test_short_body_is_refused_unless_flagged(tree, capsys):
    text = tree / "short.md"
    text.write_text("kurz\n", encoding="utf-8")
    assert mark.main(["--slug", "alpha", "--from-text", str(text)]) == 3
    assert "under 200 bytes" in capsys.readouterr().err
    assert not (tree / "Sources/drive/alpha.md").exists()
    assert mark.main(["--slug", "alpha", "--from-text", str(text), "--truncated"]) == 0
    assert records(tree)["alpha"]["truncated"] is True


def test_truncation_notice_is_detected(tree):
    text = tree / "cut.md"
    text.write_text(LONG_BODY + "\n[Content truncated]\n", encoding="utf-8")
    assert mark.main(["--slug", "alpha", "--from-text", str(text)]) == 3


def test_remark_existing_export_and_unknown_slug(tree):
    text = tree / "body.md"
    text.write_text(LONG_BODY, encoding="utf-8")
    mark.main(["--slug", "alpha", "--from-text", str(text)])
    assert mark.main(["--slug", "alpha", "--truncated"]) == 0
    assert records(tree)["alpha"]["truncated"] is True
    assert mark.main(["--slug", "gamma", "--from-text", str(text)]) == 2
    assert mark.main(["--slug", "beta"]) == 2


PLAIN_TAIL = "\ufeffTitel\r\nZeile 1 mit etwas Text.\r\n         10. Roman: Kohärenz Protokoll, https://drive.google.com/open?id=1-qJDwKciE7L-RJzqALCUQDLTbwZdld1nAIsBzeUmGc4\r\n"


def test_tail_from_completes_a_cut_last_line(tree, capsys):
    cut = LONG_BODY + "10. Roman: Kohärenz Protokoll, <https://drive.google.com/open?id=1-qJDwKciE7L-RJzqALCUQDLTbwZdld1nAIs"
    saved = tree / "result.txt"
    saved.write_text(json.dumps({"fileContent": cut}), encoding="utf-8")
    plain = tree / "plain.txt"
    plain.write_text(PLAIN_TAIL, encoding="utf-8")
    assert mark.main(["--slug", "alpha", "--from-json", str(saved), "--tail-from", str(plain)]) == 0
    body = (tree / "Sources/drive/alpha.md").read_text(encoding="utf-8")
    assert body.endswith("<https://drive.google.com/open?id=1-qJDwKciE7L-RJzqALCUQDLTbwZdld1nAIsBzeUmGc4>\n")
    assert "completed with 'BzeUmGc4>'" in capsys.readouterr().out
    assert records(tree)["alpha"]["truncated"] is False


def test_tail_from_refuses_when_no_unique_match(tree, capsys):
    cut = LONG_BODY + "10. Roman: Kohärenz Protokoll, <https://drive.google.com/open?id=1-qJDwKciE7L-RJzqALCUQDLTbwZdld1nAIs"
    saved = tree / "result.txt"
    saved.write_text(json.dumps({"fileContent": cut}), encoding="utf-8")
    plain = tree / "plain.txt"
    plain.write_text("ganz anderer Text\n", encoding="utf-8")
    assert mark.main(["--slug", "alpha", "--from-json", str(saved), "--tail-from", str(plain)]) == 4
    assert "expected 1" in capsys.readouterr().err
    assert not (tree / "Sources/drive/alpha.md").exists()


def test_complete_tail_leaves_a_complete_line_alone():
    body = "# T\n\nEin vollständiger Satz mit mehr als zwanzig Zeichen.\n"
    assert mark.complete_tail(body, "Ein vollständiger Satz mit mehr als zwanzig Zeichen.\n") == (body, "")


def test_download_result_is_decoded_from_base64(tree):
    raw = ("\ufeff" + LONG_BODY).encode("utf-8")
    saved = tree / "download.txt"
    saved.write_text(json.dumps({"content": base64.b64encode(raw).decode("ascii"), "id": "id-a",
                                 "mimeType": "text/x-markdown", "title": "A.md"}), encoding="utf-8")
    assert mark.main(["--slug", "alpha", "--from-json", str(saved)]) == 0
    body = (tree / "Sources/drive/alpha.md").read_text(encoding="utf-8")
    assert body.startswith("# Titel\n") and "\ufeff" not in body
