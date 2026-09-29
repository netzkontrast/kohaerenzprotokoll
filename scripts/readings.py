"""Readers write reading files; this writes the pages.

Until 2026-09-29 a reader wrote a reading straight onto a wiki page: it read the
whole page first, typed each line number it had asked `read.py --find` for, and
edited a file other readers might be editing. `Plan/concept/pipeline-optimization_2026-09-29.md`
(step 4, decision 015) moves the writing to code:

    Plan/runs/<batch>/readings/<page>--<document>.md     a reader writes this

    ---
    page: aegis                  # term, chapter, record or overview page
    document: <slug>
    date: 2025-10-15             # the document's date, for date order
    ---
    ## Reading — `<slug>`, 2025-10-15, the Inquiry file — what it adds

    Prose with each quotation „…" ^[?] — or ^[?L120] to prefer the hit nearest
    line 120 when the words stand on several lines.
    <!-- differ -->
    - One line for `## Where the sources differ`, if the document takes a side.

`apply` resolves every `^[?]` with `read.py`'s own comparison, so a line it
places cannot fail `quotes.py`; words it cannot place stop the file, with the
nearest lines named (P26: names in, lines by code). A reading goes before the
first reading with a later date on a term, chapter or overview page, and at the
end of a record, which is append-only. The page's `ingested:`, `sources:` and
`readings:` are re-derived afterwards (`wiki_index.py --fix-frontmatter`).
Nothing else on a page changes, and no page is created.

Usage:
    python3 scripts/readings.py check <batch>             # resolve everything, write nothing
    python3 scripts/readings.py apply <batch> [--root DIR] # write the pages (DIR: a worktree)
    python3 scripts/readings.py selftest
"""

from __future__ import annotations

import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import read  # noqa: E402
from digest import page_path  # noqa: E402
from subject import document  # noqa: E402

QUOTE_ASK = re.compile(r"„(?P<quote>[^„“]{1,400})[“\"](?P<gap>\s*)\^\[\?(?:L(?P<near>\d+))?\]")
FRONT = re.compile(r"\A---\n(.*?)\n---\n", re.S)
DATE_IN_HEAD = re.compile(r"^## Readings? — `[^`]+`, (\d{4}-\d{2}-\d{2})")
END_OF_READINGS = ("## Where the sources differ", "## Open", "## Occurrences only",
                   "## Questions for this chapter", "## Candidate sources", "## Raw qmd answers")


class Refused(Exception):
    pass


def parse(text: str) -> tuple[dict, str, list[str]]:
    m = FRONT.match(text)
    if not m:
        raise Refused("a reading file opens with frontmatter: page, document, date")
    meta = dict(line.split(":", 1) for line in m.group(1).splitlines() if ":" in line)
    meta = {k.strip(): v.split("#")[0].strip() for k, v in meta.items()}
    for key in ("page", "document", "date"):
        if not meta.get(key):
            raise Refused(f"frontmatter lacks {key}")
    body = text[m.end():]
    differ: list[str] = []
    if "<!-- differ -->" in body:
        body, tail = body.split("<!-- differ -->", 1)
        differ = [line for line in tail.strip().splitlines() if line.strip()]
    return meta, body.strip() + "\n", differ


def resolve(body: str, slug: str) -> str:
    doc = document(slug)
    problems = []

    def place(m: re.Match) -> str:
        hits = read.locate(doc, m.group("quote"))
        if not hits:
            near = ", ".join(f"L{line} ({share:.0%})" for share, line, _ in read.nearest(doc, m.group("quote")))
            problems.append(f"„{m.group('quote')[:60]}…“ not in {slug}: nearest {near}")
            return m.group(0)
        if m.group("near"):
            target = int(m.group("near"))
            hit = min(hits, key=lambda h: abs(h - target))
        else:
            hit = hits[0]  # the first copy, as the readers' brief always asked
        return f"„{m.group('quote')}“{m.group('gap')}^[{slug}.md:L{hit}]"

    out = QUOTE_ASK.sub(place, body)
    if problems:
        raise Refused("; ".join(problems))
    if "^[?" in out:
        raise Refused("a ^[?] stands where no quotation precedes it")
    return out


def insert(page: str, section: str, date: str, record: bool) -> str:
    lines = page.rstrip("\n").split("\n")
    if record:
        return "\n".join(lines) + "\n\n" + section.rstrip("\n") + "\n"
    at = None
    for i, line in enumerate(lines):
        m = DATE_IN_HEAD.match(line)
        if m and m.group(1) > date:
            at = i
            break
        if line.startswith(END_OF_READINGS):
            at = i
            break
    if at is None:
        return "\n".join(lines) + "\n\n" + section.rstrip("\n") + "\n"
    return "\n".join(lines[:at] + section.rstrip("\n").split("\n") + [""] + lines[at:]) + "\n"


def add_differ(page: str, differ: list[str]) -> str:
    if not differ:
        return page
    head = "## Where the sources differ"
    if head in page:
        start = page.index(head)
        nxt = page.find("\n## ", start + len(head))
        end = nxt if nxt != -1 else len(page)
        block = page[start:end].rstrip("\n") + "\n" + "\n".join(differ) + "\n"
        return page[:start] + block + ("\n" + page[end + 1:] if nxt != -1 else "")
    for stop in ("## Open", "## Occurrences only", "## Questions for this chapter"):
        if stop in page:
            i = page.index(stop)
            return page[:i] + head + "\n\n" + "\n".join(differ) + "\n\n" + page[i:]
    return page.rstrip("\n") + "\n\n" + head + "\n\n" + "\n".join(differ) + "\n"


def build(reading_file: Path, root: Path, staged: dict | None = None) -> tuple[Path, str]:
    meta, body, differ = parse(reading_file.read_text(encoding="utf-8"))
    if not body.startswith("## "):
        raise Refused("the body opens with its heading")
    target = page_path(meta["page"], root)
    record = "/conflicts/" in str(target) or "/questions/" in str(target)
    section = resolve(body, meta["document"])
    differ = resolve("\n".join(differ), meta["document"]).strip().split("\n") if differ else []
    page = (staged or {}).get(target) or target.read_text(encoding="utf-8")
    first = section.split("\n", 1)[0]
    if first in page:
        raise Refused(f"{target.name} already has this heading: {first}")
    return target, add_differ(insert(page, section, meta["date"], record), differ)


def wiki_dirty(root: Path) -> list[str]:
    """Readers write reading files, never pages: a changed page before apply means one did."""
    import subprocess
    out = subprocess.run(["git", "-C", str(root), "status", "--porcelain", "--", "Wiki"],
                         capture_output=True, text=True).stdout
    return [line for line in out.splitlines() if line.strip()]


def run(batch: str, write: bool, root: Path) -> int:
    folder = ROOT / "Plan" / "runs" / batch / "readings"
    dirty = wiki_dirty(root) if write else []
    if dirty:
        print("REFUSED: Wiki/ has uncommitted changes — a reader edited a page, or a run is half-applied:")
        print("\n".join("  " + d for d in dirty[:20]))
        return 1
    files = sorted(folder.glob("*.md"))
    if not files:
        print(f"no reading files in {folder}")
        return 1
    staged: dict[Path, str] = {}
    failed = 0
    for f in files:
        try:
            target, text = build(f, root, staged)  # several documents on one page: each on the last
            staged[target] = text
            print(f"ok       {f.name} → {target.relative_to(root)}")
        except Refused as e:
            failed += 1
            print(f"REFUSED  {f.name}: {e}")
    if failed:
        print(f"\n{failed} of {len(files)} files refused; nothing written.")
        return 1
    if write:
        for target, text in staged.items():
            target.write_text(text, encoding="utf-8")
        print(f"\n{len(staged)} pages written. Next: wiki_index.py --fix-frontmatter, "
              "quotes.py, link.py --apply, relations.py, lint_readings.py --doc <slug>")
    else:
        print(f"\n{len(staged)} pages would be written.")
    return 0


def selftest() -> int:
    slug = "entropie-aegis"
    doc = document(slug)
    line_no, line = next((doc.offset + i, l) for i, l in enumerate(doc.lines()) if len(l.split()) > 8)
    words = " ".join(line.split()[:5]).strip("*_#>- ")
    checks = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "Wiki/candidates").mkdir(parents=True)
        page = root / "Wiki/candidates/probe.md"
        page.write_text("---\ntitle: P\ningested: []\n---\n\n# P\n\nLead.\n\n"
                        "## Reading — `old`, 2025-01-01, old — a\n\nText.\n\n"
                        "## Reading — `new`, 2026-06-01, new — b\n\nText.\n\n"
                        "## Where the sources differ\n\n- old against new.\n", encoding="utf-8")
        good = f"---\npage: probe\ndocument: {slug}\ndate: 2025-04-17\n---\n## Reading — `{slug}`, 2025-04-17, E — c\n\nSays „{words}“ ^[?].\n<!-- differ -->\n- E takes a third side.\n"
        f = root / "good.md"
        f.write_text(good, encoding="utf-8")
        target, text = build(f, root)
        checks.append(("line placed by code", f"^[{slug}.md:L{line_no}]" in text or f"^[{slug}.md:L" in text))
        checks.append(("inserted in date order", text.index(f"`{slug}`") < text.index("`new`") and text.index("`old`") < text.index(f"`{slug}`")))
        checks.append(("differ line appended", "- E takes a third side." in text.split("## Where the sources differ")[1]))
        bad = good.replace(words, "Wörter die das Dokument nicht enthält und nie enthielt")
        f.write_text(bad, encoding="utf-8")
        try:
            build(f, root)
            checks.append(("words not in the document refused", False))
        except Refused as e:
            checks.append(("words not in the document refused", "nearest" in str(e)))
        f.write_text(good.replace("^[?]", "^[?]") + "\nStray ^[?] here.\n", encoding="utf-8")
        try:
            build(f, root)
            checks.append(("a ^[?] with no quotation refused", False))
        except Refused:
            checks.append(("a ^[?] with no quotation refused", True))
        page.write_text(text, encoding="utf-8")
        f.write_text(good, encoding="utf-8")
        try:
            build(f, root)
            checks.append(("a heading already on the page refused", False))
        except Refused:
            checks.append(("a heading already on the page refused", True))
        (root / "Wiki/conflicts").mkdir(parents=True)
        rec = root / "Wiki/conflicts/c99-probe.md"
        rec.write_text("---\ntitle: C99\n---\n\n# C99\n\n## 2026-09-01 — `x`, first\n\nEntry.\n", encoding="utf-8")
        f.write_text(good.replace("page: probe", "page: c99").replace("## Reading — ", "## 2026-09-29 — "), encoding="utf-8")
        _, text = build(f, root)
        checks.append(("a record entry is appended at the end", text.rstrip().endswith(".") and text.index("`x`") < text.index(f"`{slug}`")))
    failed = [n for n, ok in checks if not ok]
    print(f"readings: {len(checks) - len(failed)} of {len(checks)} cases hold" +
          (f" — FAILED: {', '.join(failed)}" if failed else ""))
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    if argv[:1] == ["selftest"]:
        return selftest()
    if len(argv) < 2 or argv[0] not in ("check", "apply"):
        print(__doc__)
        return 2
    root = Path(argv[argv.index("--root") + 1]).resolve() if "--root" in argv else ROOT
    return run(argv[1], argv[0] == "apply", root)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
