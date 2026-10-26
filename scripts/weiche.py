"""The switch board: the Weichen of the novel, what each frees, and the author's answer recorded in one act.

A Weiche is a decision sheet in `Plan/weichen/<id>-<slug>.md`: a question, its options, a recommendation, and —
only when the author has spoken — an answer. Answering one today means editing the sheet and adding a row to
`Manuscript/kanon.md` by hand. Decision 030 (2026-10-26) says the Weichen are answered **per chapter, when a
chapter's briefing needs them**, so this tool does the recording and says what an answer frees.

    python3 scripts/weiche.py list [--kap N] [--status offen]   # every sheet: status, kind, recommendation, chapters
    python3 scripts/weiche.py show <id>                         # question, options, recommendation, dependencies, what it frees
    python3 scripts/weiche.py answer <id> --words "…" [--option A] [--on YYYY-MM-DD]
    python3 scripts/weiche.py defer <id> --words "…"
    python3 scripts/weiche.py check                             # an answered sheet has its answer and a canon row (CI)
    python3 scripts/weiche.py selftest

`answer` writes three things and nothing else: `status: beantwortet` in the sheet's frontmatter, an `## Antwort`
section with the date, the option and **the author's words verbatim**, and a row in `Manuscript/kanon.md`
§ Entscheidungen with the same words and the sheet's path. It refuses without the words (P0). It never chooses an
option: `--option` names the one the author chose, and the words are the author's.

**What a Weiche frees** is derived, not stored: the chapters whose `development.json` row or treatment paragraph
names the Weiche (`chapters_of`). A sheet may also name chapters in prose; that is the writer's reading, and `show`
prints both apart.
"""

from __future__ import annotations

import datetime
import json
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WEICHEN = ROOT / "Plan" / "weichen"
KANON = ROOT / "Manuscript" / "kanon.md"
DEVELOPMENT = ROOT / "Plan" / "storyform" / "development.json"
TREATMENT = ROOT / "Manuscript" / "plot" / "treatment.md"
STATUSES = ("offen", "beantwortet", "vertagt", "ersetzt")
ID = re.compile(r"\b(W\d+|WP|SP)\b")
KAP = re.compile(r"\bKap\.? (\d+)\b")


# --- reading a sheet ---------------------------------------------------------------

def frontmatter(text: str) -> dict:
    """The sheet's own frontmatter: `key: value   # comment`, lists as `[a, b]`; keys may carry umlauts."""
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    out = {}
    for line in text[4:end].split("\n"):
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        value = re.sub(r"\s+#.*$", "", value).strip()
        if value.startswith("[") and value.endswith("]"):
            out[key.strip()] = [v.strip() for v in value[1:-1].split(",") if v.strip()]
        else:
            out[key.strip()] = value.strip('"')
    return out


def set_front(text: str, key: str, value: str) -> str:
    """The same frontmatter line with a new value, its trailing comment kept."""
    head, sep, body = text[4:].partition("\n---\n")
    lines = []
    for line in head.split("\n"):
        if line.startswith(key + ":"):
            comment = re.search(r"\s+#.*$", line)
            lines.append(f"{key}: {value}" + (comment.group(0) if comment else ""))
        else:
            lines.append(line)
    return "---\n" + "\n".join(lines) + sep + body


def sections(text: str) -> list[tuple[str, str]]:
    out: list[list] = []
    for line in text.split("\n"):
        if line.startswith("## "):
            out.append([line[3:].strip(), []])
        elif out:
            out[-1][1].append(line)
    return [(h, "\n".join(b).strip()) for h, b in out]


def section(text: str, *starts: str) -> str:
    for h, b in sections(text):
        if any(h.lower().startswith(s.lower()) for s in starts):
            return b
    return ""


def options_of(text: str) -> list[tuple[str, str]]:
    """(letter or label, title) for every `### X — …` or `- **X — …**` option under the options section."""
    body = section(text, "Optionen", "Die Optionen")
    out = []
    for m in re.finditer(r"^(?:### |- \*\*)([A-Z](?:\d)?)\s*[—–-]\s*([^*\n]+)", body, re.M):
        out.append((m.group(1), m.group(2).strip().rstrip("*").strip()))
    return out


def sheets(folder: Path | None = None) -> dict[str, Path]:
    out = {}
    for p in sorted((folder or WEICHEN).glob("*.md")):
        if p.stem == "README":
            continue
        meta = frontmatter(p.read_text(encoding="utf-8"))
        if meta.get("id"):
            out[meta["id"]] = p
    return out


# --- what a Weiche frees --------------------------------------------------------------

def chapters_of(wid: str, dev: dict | None = None, treatment: str | None = None,
                folder: dict[str, Path] | None = None) -> dict[str, list[int]]:
    """{'development': […], 'treatment': […], 'sheet': […]}: the chapters whose row or paragraph names the Weiche,
    and the chapters the sheet itself names."""
    dev = dev if dev is not None else (json.loads(DEVELOPMENT.read_text(encoding="utf-8"))["chapters"] if DEVELOPMENT.exists() else {})
    treatment = treatment if treatment is not None else (TREATMENT.read_text(encoding="utf-8") if TREATMENT.exists() else "")
    pat = re.compile(r"\b" + re.escape(wid) + r"\b")
    from_dev = sorted(int(k) for k, row in dev.items() if pat.search(json.dumps(row, ensure_ascii=False)))
    from_treat, current = [], None
    for line in treatment.split("\n"):
        m = re.match(r"^### Kap (\d+)", line)
        if m:
            current = int(m.group(1))
        elif current is not None and pat.search(line) and current not in from_treat:
            from_treat.append(current)
    sheet = sheets().get(wid) if folder is None else folder.get(wid)
    from_sheet = named_in_sheet(sheet.read_text(encoding="utf-8")) if sheet else []
    return {"development": from_dev, "treatment": from_treat, "sheet": from_sheet}


def named_in_sheet(text: str) -> list[int]:
    """The chapters a sheet's prose names — the writer's reading, looser than a row that names the Weiche."""
    return sorted({int(m.group(1)) for m in KAP.finditer(text)})


# --- the verbs ---------------------------------------------------------------------------

def kanon_rows(text: str | None = None) -> list[dict]:
    text = text if text is not None else (KANON.read_text(encoding="utf-8") if KANON.exists() else "")
    out = []
    for line in text.split("\n"):
        if line.startswith("| ") and not line.startswith("| id") and not line.startswith("|---"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 4:
                out.append({"id": cells[0].strip("` "), "date": cells[1], "what": cells[2], "where": cells[3]})
    return out


def add_kanon_row(wid: str, date: str, what: str, where: str, kanon: Path | None = None) -> None:
    path = kanon or KANON
    text = path.read_text(encoding="utf-8")
    rows = [ln for ln in text.split("\n")]
    # the last table row of § Entscheidungen
    in_section, last = False, None
    for i, line in enumerate(rows):
        if line.startswith("## "):
            in_section = line[3:].strip().startswith("Entscheidungen")
        elif in_section and line.startswith("| ") and not line.startswith("| id"):
            last = i
    if last is None:
        raise SystemExit("Manuscript/kanon.md: no table under ## Entscheidungen")
    what = what.replace("|", "¦").replace("\n", " ").strip()
    rows.insert(last + 1, f"| {wid} | {date} | {what} | `{where}` |")
    path.write_text("\n".join(rows), encoding="utf-8")


def answer(wid: str, words: str, option: str = "", today: str | None = None, by: str = "author",
           folder: Path | None = None, kanon: Path | None = None, status: str = "beantwortet") -> dict:
    if not words.strip():
        raise SystemExit("an answer records the author's words verbatim: --words is required (P0)")
    path = sheets(folder).get(wid)
    if not path:
        raise SystemExit(f"no Weiche {wid}")
    text = path.read_text(encoding="utf-8")
    meta = frontmatter(text)
    if meta.get("status") == "beantwortet" and status == "beantwortet":
        raise SystemExit(f"{wid} is already answered; a later answer is a correction — say so in the words and edit the sheet by hand")
    today = today or datetime.date.today().isoformat()
    head = f"**{'Beantwortet' if status == 'beantwortet' else 'Vertagt'} {today}" + (f": {option}" if option else "") + f".** {words.strip()}"
    block = f"\n\n## Antwort\n\n{head}\n" if "\n## Antwort" not in text else f"\n\n{head}\n"
    text = set_front(text, "status", status).rstrip("\n") + block
    path.write_text(text, encoding="utf-8")
    row = {"id": wid, "status": status, "on": today, "by": by, "option": option, "words": words.strip(),
           "sheet": path.relative_to(ROOT).as_posix() if path.is_relative_to(ROOT) else str(path)}
    if status == "beantwortet":
        add_kanon_row(wid, today, (f"{option}: " if option else "") + words.strip(), row["sheet"], kanon)
    return row


def problems(folder: Path | None = None, kanon_text: str | None = None) -> tuple[list[str], list[str]]:
    """(failures, notes): every sheet's status is known; an answered sheet carries its answer; and is in kanon.md (noted)."""
    fail, note = [], []
    rows = kanon_rows(kanon_text)
    named = " ".join(r["id"] + " " + r["what"] + " " + r["where"] for r in rows)
    for wid, path in sheets(folder).items():
        text = path.read_text(encoding="utf-8")
        meta = frontmatter(text)
        if meta.get("status") not in STATUSES:
            fail.append(f"{wid}: status {meta.get('status')!r} is not one of {', '.join(STATUSES)}")
        if meta.get("status") == "beantwortet":
            if not re.search(r"\*\*Beantwortet \d{4}-\d{2}-\d{2}", text):
                fail.append(f"{wid}: beantwortet, but the sheet has no „**Beantwortet <date>**“ answer")
            if not re.search(r"\b" + re.escape(wid) + r"\b", named):
                note.append(f"{wid}: answered, and Manuscript/kanon.md names it nowhere")
    return fail, note


def listing(kap: int | None = None, status: str | None = None) -> str:
    out = []
    dev = json.loads(DEVELOPMENT.read_text(encoding="utf-8"))["chapters"] if DEVELOPMENT.exists() else {}
    treat = TREATMENT.read_text(encoding="utf-8") if TREATMENT.exists() else ""
    for wid, path in sheets().items():
        meta = frontmatter(path.read_text(encoding="utf-8"))
        ch = chapters_of(wid, dev, treat)
        touched = sorted(set(ch["development"]) | set(ch["treatment"]) | set(ch["sheet"]))
        if kap is not None and kap not in touched:
            continue
        if status and meta.get("status") != status:
            continue
        kaps = ("Kap " + ", ".join(map(str, touched))) if touched else "—"
        out.append(f"{wid:5} {meta.get('status', '?'):12} {meta.get('frage_art', ''):9} empf. {str(meta.get('empfehlung', ''))[:22]:22} {kaps[:40]:40} {path.name}")
    return "\n".join(out) + f"\n{len(out)} Weiche(n)"


def show(wid: str) -> str:
    path = sheets().get(wid)
    if not path:
        return f"no Weiche {wid}"
    text = path.read_text(encoding="utf-8")
    meta = frontmatter(text)
    ch = chapters_of(wid)
    out = [f"# {wid} — {path.name}", f"status: {meta.get('status')} · art: {meta.get('frage_art')} · empfehlung: {meta.get('empfehlung')}",
           f"hängt ab von: {', '.join(meta.get('hängt_ab_von', [])) or '—'}", "",
           "## Frage", section(text, "Die Frage") or "(no section)", "", "## Optionen"]
    out += [f"- {k} — {t}" for k, t in options_of(text)] or ["(none parsed)"]
    out += ["", "## Empfehlung", section(text, "Empfehlung") or "(none)", "",
            f"## Was sie frei gibt (abgeleitet)", f"development.json: Kap {', '.join(map(str, ch['development'])) or '—'}",
            f"treatment: Kap {', '.join(map(str, ch['treatment'])) or '—'}", f"im Blatt genannt: Kap {', '.join(map(str, ch['sheet'])) or '—'}"]
    ans = section(text, "Antwort")
    if ans:
        out += ["", "## Antwort", ans]
    return "\n".join(out)


# --- selftest -----------------------------------------------------------------------------

SHEET = """---
id: W99
status: offen     # offen | beantwortet | vertagt | ersetzt — nur der Autor setzt beantwortet
hängt_ab_von: [W1, W2]
frage_art: schlüssel        # schlüssel | schalter | standard | vertagt
auslöser: "test"
empfehlung: "A"
---

# W99 — Eine Probe

## Die Frage

Trägt das Wir die Welt oder die Scherben? Kap 40 und Kap 1 hängen daran.

## Die Optionen

### A — Die Welt

Text.

### B — Die Scherben

Text.

## Empfehlung

A.
"""
KANON_FIXTURE = """# Kanon

## Entscheidungen

| id | Datum | Was gilt | Wo es steht |
|---|---|---|---|
| C6 | 2026-09-24 | Fünf Guardians. | `Wiki/conflicts/c6.md` |

## Freigegebene Kapitel

Keines.
"""


def selftest() -> int:
    results = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        folder, kanon = root / "weichen", root / "kanon.md"
        folder.mkdir()
        (folder / "w99-probe.md").write_text(SHEET, encoding="utf-8")
        kanon.write_text(KANON_FIXTURE, encoding="utf-8")
        meta = frontmatter(SHEET)
        results.append(("the frontmatter reads id, status, a list and a quoted value", meta["id"] == "W99" and meta["status"] == "offen"
                        and meta["hängt_ab_von"] == ["W1", "W2"] and meta["empfehlung"] == "A"))
        results.append(("the options are parsed", options_of(SHEET) == [("A", "Die Welt"), ("B", "Die Scherben")]))
        results.append(("the chapters a sheet names are listed", named_in_sheet(SHEET) == [1, 40]))
        dev = {"1": {"open": "siehe W99"}, "2": {"open": "nichts"}, "40": {"open": "W99 entscheidet"}}
        treat = "### Kap 2 — x\n- hängt an W99.\n### Kap 3 — y\n- nichts.\n"
        results.append(("what a Weiche frees comes from development.json and the treatment",
                        chapters_of("W99", dev, treat, {}) == {"development": [1, 40], "treatment": [2], "sheet": []}))
        results.append(("W9 does not match W99", chapters_of("W9", dev, treat, {}) == {"development": [], "treatment": [], "sheet": []}))
        f, n = problems(folder, kanon.read_text(encoding="utf-8"))
        results.append(("an open sheet passes", f == [] and n == []))
        try:
            answer("W99", "", "A", "2026-10-26", folder=folder, kanon=kanon)
            results.append(("an answer without words is refused", False))
        except SystemExit as e:
            results.append(("an answer without words is refused", "--words" in str(e)))
        row = answer("W99", "Die Scherben, als Mosaik, das die Welt hält.", "B", "2026-10-26", folder=folder, kanon=kanon)
        text = (folder / "w99-probe.md").read_text(encoding="utf-8")
        results.append(("answer sets the status and keeps the comment", "status: beantwortet     # offen |" in text))
        results.append(("answer writes the Antwort section with date, option and words",
                        "## Antwort" in text and "**Beantwortet 2026-10-26: B.** Die Scherben, als Mosaik, das die Welt hält." in text))
        krows = kanon_rows(kanon.read_text(encoding="utf-8"))
        results.append(("answer adds the canon row after the last one, with the words and the sheet",
                        krows[-1]["id"] == "W99" and "Die Scherben" in krows[-1]["what"] and "w99-probe.md" in krows[-1]["where"] and krows[0]["id"] == "C6"))
        results.append(("the canon section after the table is untouched", "## Freigegebene Kapitel\n\nKeines." in kanon.read_text(encoding="utf-8")))
        f, n = problems(folder, kanon.read_text(encoding="utf-8"))
        results.append(("an answered sheet with its row passes", f == [] and n == []))
        try:
            answer("W99", "noch einmal", "A", folder=folder, kanon=kanon)
            results.append(("a second answer is refused", False))
        except SystemExit as e:
            results.append(("a second answer is refused", "already answered" in str(e)))
        (folder / "w98-x.md").write_text(SHEET.replace("W99", "W98").replace("status: offen", "status: beantwortet"), encoding="utf-8")
        f, n = problems(folder, kanon.read_text(encoding="utf-8"))
        results.append(("beantwortet without an answer fails, and without a canon row is noted",
                        any("no „**Beantwortet" in x for x in f) and any("W98" in x for x in n)))
        (folder / "w97-x.md").write_text(SHEET.replace("W99", "W97").replace("status: offen", "status: irgendwas"), encoding="utf-8")
        f, _ = problems(folder, kanon.read_text(encoding="utf-8"))
        results.append(("an unknown status fails", any("W97" in x and "not one of" in x for x in f)))
        row = answer("W97", "später", "", "2026-10-26", folder=folder, kanon=kanon, status="vertagt")
        results.append(("defer sets vertagt without a canon row", row["status"] == "vertagt"
                        and "status: vertagt" in (folder / "w97-x.md").read_text(encoding="utf-8")
                        and not any(r["id"] == "W97" for r in kanon_rows(kanon.read_text(encoding="utf-8")))))
    for name, ok in results:
        print(("held  " if ok else "FAILED") + "  " + name)
    failed = sum(1 for _, ok in results if not ok)
    print(f"{len(results) - failed} of {len(results)} held")
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    verb, rest = argv[0], argv[1:]

    def opt(name: str, default: str = "") -> str:
        return rest[rest.index(name) + 1] if name in rest and rest.index(name) + 1 < len(rest) else default

    if verb == "selftest":
        return selftest()
    if verb == "list":
        print(listing(int(opt("--kap")) if opt("--kap") else None, opt("--status") or None))
        return 0
    if verb == "show" and rest:
        print(show(rest[0]))
        return 0
    if verb in ("answer", "defer") and rest:
        row = answer(rest[0], opt("--words"), opt("--option"), opt("--on") or None, opt("--by", "author"),
                     status="beantwortet" if verb == "answer" else "vertagt")
        print(json.dumps(row, ensure_ascii=False))
        return 0
    if verb == "check":
        fail, note = problems()
        for f in fail:
            print("FAIL  " + f)
        for n in note:
            print("note  " + n)
        n_all = len(sheets())
        print(f"{n_all} Weiche(n), {len(fail)} problem(s), {len(note)} note(s)")
        return 1 if fail else 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
