"""The wiki as plain HTML pages, one per record, beside the app on the website.

The app (`ui.py`) is one large component that needs its runtime and JavaScript to show anything. A person on a slow
phone, a search inside the browser, or an agent fetching one page wants the record itself. This script renders each
record's markdown — term pages, conflicts, questions, chapter pages, reconciliation records, decisions — into a small
standalone HTML file under `Plan/derived/web/static/`, with an index per kind and one over all of them.

It renders, it does not interpret: headings, paragraphs, lists, tables, code, emphasis, `[[links]]` to the page they
name, and citations as small marks. Every page names its repository path and the commit. A line with a figure's
earlier name or the trauma symbol is withheld, as the MCP server withholds it (`rag.WITHHELD_LINE`, decision 029).

**Incremental**: a page is written only when its bytes changed, so a local rebuild after one ingest touches the
handful of pages that ingest changed, and the count of pages written says so.

    python3 scripts/static_pages.py            # write Plan/derived/web/static/
    python3 scripts/static_pages.py selftest
"""

from __future__ import annotations

import html
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from rag import WITHHELD_LINE, WITHHELD_TEXT  # noqa: E402

OUT = ROOT / "Plan" / "derived" / "web" / "static"
KINDS = [  # (folder on the website, title, source folder, glob, id from the file stem)
    ("wiki", "Term pages", "Wiki/candidates", "*.md", lambda s: s),
    ("conflicts", "Conflicts", "Wiki/conflicts", "c*.md", lambda s: s.split("-", 1)[0].upper()),
    ("questions", "Questions", "Wiki/questions", "q*.md", lambda s: s.split("-", 1)[0].upper()),
    ("chapters", "Chapter pages", "Wiki/chapters", "kap-*.md", lambda s: s),
    ("records", "Reconciliation records", "Wiki/compare", "reconcile-*.md", lambda s: s),
    ("decisions", "Decisions", "Plan/decisions", "[0-9]*.md", lambda s: s[:3]),
]
STYLE = """body{margin:0;background:#F3F0E8;color:#2A2823;font:16px/1.55 Georgia,serif}
main{max-width:760px;margin:0 auto;padding:16px}
a{color:#2B4C8C}code,pre{font-family:ui-monospace,monospace;font-size:.86em;background:#EFEBE1;border-radius:3px}
code{padding:1px 4px}pre{padding:8px;overflow-x:auto}table{border-collapse:collapse;display:block;overflow-x:auto}
td,th{border:1px solid #D8D2C4;padding:4px 6px;vertical-align:top;font-size:.9em}
sup.cite{font-family:ui-monospace,monospace;font-size:.7em;color:#2B4C8C}.meta{color:#6B665C;font-size:.85em}
blockquote{margin:0 0 0 12px;padding-left:10px;border-left:3px solid #D8D2C4}
@media (prefers-color-scheme:dark){body{background:#1E1D1A;color:#E8E4DA}code,pre{background:#2C2A25}
td,th{border-color:#44403A}a,sup.cite{color:#9DB4E0}}"""


def inline(text: str, slugs: set[str]) -> str:
    """Escape, then mark up code, links, citations and emphasis — in that order, so code stays literal."""
    parts = re.split(r"(`[^`]*`)", text)
    out = []
    for part in parts:
        if part.startswith("`") and part.endswith("`") and len(part) > 1:
            out.append(f"<code>{html.escape(part[1:-1])}</code>")
            continue
        s = html.escape(part, quote=False)

        def link(m: re.Match) -> str:
            slug, label = m.group(1), m.group(2) or m.group(1)
            return f'<a href="../wiki/{slug}.html">{label}</a>' if slug in slugs else label
        s = re.sub(r"\[\[([a-z0-9-]+)(?:\|([^\]]+))?\]\]", link, s)
        s = re.sub(r"\^\[([^\]]+)\]", lambda m: f'<sup class="cite" title="{m.group(1)}">[{m.group(1)}]</sup>', s)
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
        out.append(s)
    return "".join(out)


def render(markdown: str, slugs: set[str]) -> str:
    """Markdown as this repository writes it, to HTML. Frontmatter is dropped; an unknown construct is a paragraph."""
    lines = markdown.split("\n")
    if lines and lines[0].strip() == "---":
        end = next((i for i, ln in enumerate(lines[1:], 1) if ln.strip() == "---"), 0)
        lines = lines[end + 1:]
    lines = [WITHHELD_TEXT if WITHHELD_LINE.search(ln) else ln for ln in lines]
    out, para, i = [], [], 0

    def flush() -> None:
        if para:
            out.append(f"<p>{inline(' '.join(para), slugs)}</p>")
            para.clear()
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("```"):
            flush()
            j = i + 1
            while j < len(lines) and not lines[j].startswith("```"):
                j += 1
            out.append(f"<pre>{html.escape(chr(10).join(lines[i + 1:j]))}</pre>")
            i = j + 1
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", ln)
        if m:
            flush()
            n = len(m.group(1))
            out.append(f"<h{n}>{inline(m.group(2), slugs)}</h{n}>")
        elif ln.startswith("|"):
            flush()
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                    rows.append(cells)
                i += 1
            body = "".join("<tr>" + "".join(f"<{'th' if r is rows[0] else 'td'}>{inline(c, slugs)}</{'th' if r is rows[0] else 'td'}>"
                                            for c in r) + "</tr>" for r in rows)
            out.append(f"<table>{body}</table>")
            continue
        elif re.match(r"^\s*([-*]|\d+\.)\s+", ln):
            flush()
            ordered = bool(re.match(r"^\s*\d+\.", ln))
            items = []
            while i < len(lines) and re.match(r"^\s*([-*]|\d+\.)\s+", lines[i]):
                item = re.sub(r"^\s*([-*]|\d+\.)\s+", "", lines[i])
                i += 1
                while i < len(lines) and lines[i].startswith("  ") and not re.match(r"^\s*([-*]|\d+\.)\s+", lines[i]):
                    item += " " + lines[i].strip()
                    i += 1
                items.append(f"<li>{inline(item, slugs)}</li>")
            tag = "ol" if ordered else "ul"
            out.append(f"<{tag}>{''.join(items)}</{tag}>")
            continue
        elif ln.startswith(">"):
            flush()
            out.append(f"<blockquote>{inline(ln.lstrip('> '), slugs)}</blockquote>")
        elif not ln.strip() or ln.strip().startswith("<!--"):
            flush()
        else:
            para.append(ln.strip())
        i += 1
    flush()
    return "\n".join(out)


def page(title: str, body: str, path: str, commit: str, up: str) -> str:
    return (f"<!doctype html><html lang=\"de\"><head><meta charset=\"utf-8\">"
            f"<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
            f"<meta name=\"robots\" content=\"noindex,nofollow\"><title>{html.escape(title)}</title>"
            f"<style>{STYLE}</style></head><body><main>"
            f"<p class=\"meta\"><a href=\"{up}\">↑ index</a> · <code>{html.escape(path)}</code>"
            f"{' · commit ' + html.escape(commit) if commit else ''}</p>\n{body}\n</main></body></html>\n")


def write_if_changed(path: Path, text: str) -> bool:
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return True


def commit_of(root: Path) -> str:
    out = subprocess.run(["git", "log", "-1", "--format=%h"], cwd=root, capture_output=True, text=True).stdout.strip()
    return out or os.environ.get("VERCEL_GIT_COMMIT_SHA", "")[:7]


def build(root: Path = ROOT, out: Path = OUT) -> dict:
    """Write every page and index; return how many were written and how many kept. A page whose record is gone
    is removed, so the folder holds exactly the records there are."""
    commit = commit_of(root)
    slugs = {p.stem for p in (root / "Wiki" / "candidates").glob("*.md") if not WITHHELD_LINE.search(p.stem)}
    written = kept = 0
    expected: set[Path] = set()
    top = []
    for folder, title, src, pattern, ident in KINDS:
        rows = []
        for p in sorted((root / src).glob(pattern)):
            if WITHHELD_LINE.search(p.stem):
                continue  # a record whose very name is withheld has no page
            text = p.read_text(encoding="utf-8")
            head = next((ln[2:].strip() for ln in text.split("\n") if ln.startswith("# ")), p.stem)
            head = WITHHELD_TEXT if WITHHELD_LINE.search(head) else head
            name = f"{p.stem}.html"
            target = out / folder / name
            expected.add(target)
            changed = write_if_changed(target, page(head, render(text, slugs), p.relative_to(root).as_posix(), commit,
                                                     "index.html"))
            written, kept = written + changed, kept + (not changed)
            rows.append(f'<li><a href="{name}">{html.escape(ident(p.stem))}</a> — {inline(head, set())}</li>')
        index = out / folder / "index.html"
        expected.add(index)
        if write_if_changed(index, page(title, f"<h1>{title}</h1><ul>{''.join(rows)}</ul>", src + "/", commit, "../index.html")):
            written += 1
        top.append(f'<li><a href="{folder}/index.html">{title}</a> ({len(rows)})</li>')
    root_index = out / "index.html"
    expected.add(root_index)
    body = ("<h1>Kohärenz Protokoll — the records as pages</h1><p>Each record of the wiki, rendered from its markdown; "
            "the app is at <a href=\"../Main.dc.html\">Main.dc.html</a>.</p><ul>" + "".join(top) + "</ul>")
    if write_if_changed(root_index, page("Kohärenz Protokoll — records", body, "Wiki/", commit, "index.html")):
        written += 1
    removed = 0
    for p in out.rglob("*.html") if out.exists() else []:
        if p not in expected:
            p.unlink()
            removed += 1
    return {"written": written, "kept": kept, "removed": removed}


def selftest() -> list[str]:
    bad = []
    slugs = {"juna"}
    h = render("---\nterm: X\n---\n# Juna\n\nSiehe [[juna|die Seite]] und [[nobody]] „Zitat“ ^[doc.md:L3].\n\n"
               "| a | b |\n|---|---|\n| `x<y` | **fett** |\n\n- eins\n- zwei\n", slugs)
    for want, why in (('<a href="../wiki/juna.html">die Seite</a>', "a link to an existing page"),
                      ("nobody", "an unknown link left as text"), ('<sup class="cite"', "a citation mark"),
                      ("<code>x&lt;y</code>", "code escaped"), ("<strong>fett</strong>", "bold"),
                      ("<ul><li>eins</li><li>zwei</li></ul>", "a list"), ("<th>a</th>", "a table head")):
        if want not in h:
            bad.append(f"render: {why}")
    if "term: X" in h:
        bad.append("render: frontmatter shown")
    early = "Jul" "ia"
    if early in render(f"{early} sagt etwas.", slugs) or WITHHELD_TEXT not in render(f"{early} sagt.", slugs):
        bad.append("render: an earlier name's line not withheld")
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "Wiki" / "candidates").mkdir(parents=True)
        (root / "Wiki" / "candidates" / "juna.md").write_text("# Juna\nText\n")
        out = root / "out"
        first = build(root, out)
        second = build(root, out)
        (root / "Wiki" / "candidates" / "juna.md").write_text("# Juna\nAnderer Text\n")
        third = build(root, out)
        if second["written"] != 0:
            bad.append("incremental: an unchanged rebuild wrote pages")
        if third["written"] != 1:
            bad.append(f"incremental: one changed page wrote {third['written']}")
        if first["written"] < 3:
            bad.append("build: the first run wrote too little")
    return bad


def main(argv: list[str]) -> int:
    if argv[:1] == ["selftest"]:
        bad = selftest()
        print(f"static pages: {'held' if not bad else 'FAILED'} — " + ("every case holds" if not bad else "; ".join(bad)))
        return 1 if bad else 0
    r = build()
    print(f"static pages: {r['written']} written, {r['kept']} unchanged, {r['removed']} removed — {OUT.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
