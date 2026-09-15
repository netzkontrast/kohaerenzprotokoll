#!/usr/bin/env python3
"""Decidable prose lints for Kohärenz Protokoll chapter files.

Encodes the hard rules that can be checked mechanically — the R-rules from
`Canon/kohaerenz-protokoll_welt-sensorik-drafting_2026-06-10.md` §10.1, the
Act-I fences from `Plan/drafting/drafting-brief.md` §3, and the chapter file
format from §4. Everything semantic (R-1 tragic irony, R-2 telling, R-6 one
concept per scene, voice register) stays with the scene-bridge-auditor and
the human reviewer; this script only reports what a grep can prove.

    python3 scripts/lint_chapter.py                 # all chapters
    python3 scripts/lint_chapter.py path/to/07-*.md # one or more files
    python3 scripts/lint_chapter.py --hook FILE     # hook mode: warn, exit 0
    python3 scripts/lint_chapter.py --json          # machine-readable

Exit status is 1 when any VIOLATION was found (0 in --hook mode, which is
what `.claude/hooks/post-tool-use.sh` relies on so a lint never blocks a
write). Calibrated 2026-09-15 against chapters 0–40: zero findings.

Levels:
  VIOLATION — a locked rule is broken; fix before the chapter counts as drafted
  WARN      — likely violation that needs a human eye (homonyms, register)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS = ROOT / (
    "Manuscript/works/the-agency-system/works/"
    "hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/chapters"
)

STATUS_ENUM = ("outlined", "drafted", "revised", "final")
ACT_I = range(1, 14)          # Kap 1–13 — Multiplizitäts-Schleier intact
BEFORE_NAME = range(1, 9)     # D-05: "Kael" first appears in Kap 9
VORTEX_1 = (35, 36)           # R-5 canonical exception: Vortex 1 Beat 4

# Kap 1–40 open their prose with `# Kapitel N — Titel`; Kap 0 keeps its own
# framing title (`# Kohärenz Protokoll — Kapitel 0 …`).
BODY_RE = re.compile(r"^# (?:Kapitel |Kohärenz Protokoll — Kapitel )", re.M)
SCENE_BREAK = re.compile(r"^---\s*$", re.M)
FENCE = re.compile(r"^```.*?^```", re.M | re.S)

# --- rule tables --------------------------------------------------------
# (code, level, chapters, regex, message). `None` for chapters = all.
DKT_TERMS = r"\b(Coheron\w*|Erason\w*|Landauer\w*|Kohärenzfeld\w*|Dual-Kernel\w*|DKT)\b"
R3_TERMS = r"\b(Fragment\w*|ANPs?|EPs?|TSDP|DID|Anteile?|Multiplizität\w*|Dissoziation\w*)\b"
VOICE_NAMES = (
    "Kael|Lex|Alex|Rhys|Selene|Nyx|Kiko|Lia|Isabelle|Moros|Argus|Silas|Oblivion|"
    "AEGIS|Mnemosyne|Juna"
)

BODY_RULES = [
    ("ACT1-AEGIS", "VIOLATION", ACT_I, r"\bAEGIS\b",
     "Drafting-Brief §3: der Name AEGIS erscheint in Akt I nie im leserseitigen Text"),
    ("ACT1-DKT", "VIOLATION", ACT_I, DKT_TERMS,
     "Drafting-Brief §3 / Begriffe §14: keine DKT-Fachbegriffe in Akt I"),
    ("ACT1-R3", "WARN", ACT_I, R3_TERMS,
     "R-3: Multiplizitäts-Schleier — Alter/Fragment/ANP/EP/TSDP/DID/Anteil fallen nicht in Akt I"),
    ("ACT1-JUNA", "VIOLATION", ACT_I, r"\bJunas?\b",
     "R-10 / Drafting-Brief §3: Juna nie als Name in Akt I"),
    ("NAME-KAEL", "VIOLATION", BEFORE_NAME, r"\bKaels?\b",
     "D-05: der Name Kael erscheint erstmals in Kap 9"),
    ("MEMORY-TELL", "VIOLATION", None, r"ich erinnere mich nicht",
     "Drafting-Brief §2: nie „ich erinnere mich nicht“"),
    ("R9-QUOTE", "VIOLATION", range(1, 41), r"AEGIS ist, was AEGIS verhindert",
     "R-9: Genesis-Stil-Marker werden nie wörtlich wiederholt"),
    ("DEFERRAL", "VIOLATION", None, r"\b(TODO|FIXME|TBD|XXX)\b",
     "Deferral marker in a chapter file — write it or ask"),
]

# A voice label at the start of a line inside prose: "**Lex:**", "Lex:", "LEX —".
VOICE_LABEL = re.compile(
    rf"^\s*(?:\*\*)?(?:{VOICE_NAMES})(?:\*\*)?\s*[:：]\s", re.M)


@dataclass
class Finding:
    file: str
    line: int
    level: str
    code: str
    message: str
    excerpt: str = ""

    def render(self) -> str:
        ex = f"  ← {self.excerpt}" if self.excerpt else ""
        return f"{self.file}:{self.line}: {self.level} {self.code} — {self.message}{ex}"


def _frontmatter(text: str) -> tuple[dict, int]:
    """Return (fields, end_line). Minimal YAML: `key: value` lines only."""
    if not text.startswith("---"):
        return {}, 0
    end = text.find("\n---", 3)
    if end == -1:
        return {}, 0
    block = text[3:end]
    fields = {}
    for ln in block.splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", ln)
        if m:
            fields[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return fields, text[:end].count("\n") + 2


def _line_of(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def _excerpt(text: str, pos: int, width: int = 70) -> str:
    start = text.rfind("\n", 0, pos) + 1
    end = text.find("\n", pos)
    line = text[start:end if end != -1 else None].strip()
    return line if len(line) <= width else line[: width - 1] + "…"


def lint_file(path: Path) -> list[Finding]:
    rel = str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)
    text = path.read_text(encoding="utf-8")
    out: list[Finding] = []
    fm, fm_end = _frontmatter(text)

    # --- file format (Drafting-Brief §4) ---
    if not fm:
        out.append(Finding(rel, 1, "VIOLATION", "FRONTMATTER",
                           "chapter file must start with YAML frontmatter"))
    else:
        if fm.get("type") != "novel.chapter":
            out.append(Finding(rel, 1, "VIOLATION", "FRONTMATTER",
                               "frontmatter `type` must be novel.chapter"))
        st = fm.get("status")
        if st not in STATUS_ENUM:
            out.append(Finding(rel, 1, "VIOLATION", "STATUS",
                               f"status {st!r} not in {STATUS_ENUM}"))
        m = re.match(r"(\d{2})-", path.name)
        if m and fm.get("chapter_number") not in (None, str(int(m.group(1)))):
            out.append(Finding(rel, 1, "VIOLATION", "NUMBER",
                               f"chapter_number {fm.get('chapter_number')!r} ≠ filename {m.group(1)}"))

    m = re.match(r"(\d{2})-", path.name)
    number = int(m.group(1)) if m else int(fm.get("chapter_number", -1) or -1)

    bm = BODY_RE.search(text)
    if not bm:
        if fm.get("status") in ("drafted", "revised", "final"):
            out.append(Finding(rel, fm_end or 1, "VIOLATION", "BODY",
                               "status is drafted+ but no `# Kapitel N` prose body found"))
        return out
    body_start = bm.start()
    body = text[body_start:]

    # --- word-level fences ---
    for code, level, chapters, pattern, message in BODY_RULES:
        if chapters is not None and number not in chapters:
            continue
        for hit in re.finditer(pattern, body):
            pos = body_start + hit.start()
            out.append(Finding(rel, _line_of(text, pos), level, code, message,
                               _excerpt(text, pos)))

    # --- voices are never labeled (Anteile §8.1, Drafting-Brief R-3) ---
    for hit in VOICE_LABEL.finditer(body):
        pos = body_start + hit.start()
        out.append(Finding(rel, _line_of(text, pos), "VIOLATION", "VOICE-LABEL",
                           "Stimmen werden nie gelabelt — kein Sprecher-Tag, kein Header",
                           _excerpt(text, pos)))

    # --- R-8 / §12.7: AEGIS logs never say "Ich" (checked inside code fences) ---
    for fence in FENCE.finditer(body):
        for hit in re.finditer(r"\bIch\b", fence.group(0)):
            pos = body_start + fence.start() + hit.start()
            out.append(Finding(rel, _line_of(text, pos), "WARN", "AEGIS-ICH",
                               "§12.7: AEGIS verwendet nie das Wort „Ich“ (Log-Block)",
                               _excerpt(text, pos)))

    # --- R-5 heat polarity per scene ---
    if number not in VORTEX_1:
        offset = 0
        for scene in SCENE_BREAK.split(body):
            has_ozon = re.search(r"\bOzon", scene)
            has_warm = re.search(r"\b(Wärme|hautwarm|warm\w*)\b", scene)
            if has_ozon and has_warm:
                pos = body_start + offset + has_warm.start()
                out.append(Finding(rel, _line_of(text, pos), "WARN", "R5-HEAT",
                                   "R-5: kaltes Ozon (AEGIS) und Wärme (Juna) in derselben Szene",
                                   _excerpt(text, pos)))
            offset += len(scene) + 4  # "---\n"
    return out


def target_files(args: list[str]) -> list[Path]:
    if args:
        return [Path(a).resolve() for a in args]
    return sorted(p for p in CHAPTERS.glob("[0-9][0-9]-*.md"))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("files", nargs="*", help="chapter files (default: all)")
    ap.add_argument("--hook", action="store_true",
                    help="hook mode: print findings, always exit 0")
    ap.add_argument("--json", action="store_true", help="JSON output")
    ns = ap.parse_args(argv)

    findings: list[Finding] = []
    for f in target_files(ns.files):
        if not f.is_file():
            print(f"{f}: not a file", file=sys.stderr)
            continue
        findings.extend(lint_file(f))

    if ns.json:
        print(json.dumps([asdict(x) for x in findings], ensure_ascii=False, indent=1))
    else:
        for x in findings:
            print(x.render())
        if findings:
            v = sum(1 for x in findings if x.level == "VIOLATION")
            w = len(findings) - v
            print(f"\n{v} violation(s), {w} warning(s)")
        elif not ns.hook:
            print("lint_chapter: clean")

    if ns.hook:
        return 0
    return 1 if any(x.level == "VIOLATION" for x in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
