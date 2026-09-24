"""The whole project as one interactive app, derived into the files of a
claude.ai Design canvas.

Every screen shows what the repository already states, and nothing else: the
pages, conflicts and questions in `Wiki/`, the reconciliation records in
`Wiki/compare/`, the typed graph from `scripts/graph.py`, every number from
`scripts/state.py`, the manifest, `NOW.md`, `GOAL.md`, `PRINCIPLES.md`, the
decisions, and the loop and invariants of the `tools` skill. Nothing is inferred
and nothing is summarised: a page is rendered from its own markdown, a relation
is an edge `graph.py` derived, a count is a measurement, and a reading-log row is
the document's own `reconcile.json`.

What it writes is derived, so it goes where derived things go and is never
committed (`Plan/derived/`, git-ignored). One component, `project/Main.dc.html`,
holds the app and its data; six thin artboards open it on a different screen
each, so the canvas shows every screen at once and each one is playable.

    python3 scripts/ui.py                # derive, run the invariants, write Plan/derived/ui/canvas/
    python3 scripts/ui.py --no-checks    # the same, without running the invariants
    python3 scripts/ui.py --check        # write, then check what was written; exit 1 on a defect
    python3 scripts/ui.py selftest       # every check, proved able to fail

The app's source is `scripts/ui.html` (the markup, with the macros below) and
`scripts/ui.js` (the component). `@RUNS(path)@` expands to the renderer of one
run list — plain, bold, German quotation, italic, code, `[[link]]`, citation —
and `@RUNSFLAT(path)@` to the same without the link, for runs inside a button.

## Publishing

A script cannot publish a canvas; a Claude session does, with its Artifact tool,
`root` set to `Plan/derived/ui/canvas`. The canvas is
`https://claude.ai/artifact/1EyhQkX3MpiRTw3TxjTjYL`, private to the author. A
data refresh changes only `project/Main.dc.html`: publish that file alone, so
the author's own arrangement of the canvas survives. `canvas.json` and the
frames go only when the layout itself changes.

## What it deliberately does not do

It writes nothing outside `Plan/derived/ui/`, and it runs only checks that write
nothing — `judgements.py` rewrites `Plan/runs/judgements.md`, so its line comes
from the replay `state.py` already performs. It does not choose a reading,
merge readings, or show a relation `graph.py` does not hold.

## The checks

`--check` reads the files the way the canvas will: every non-void element closed;
nothing interactive inside a button or a link, because the HTML parser closes the
outer one; no `sc-for`/`sc-if` inside a table or a select, because the parser
moves it out; no block inside a `<p>`, which the parser closes; every `{{hole}}` a
dotted path or a literal, never an expression; no macro left unexpanded; each
root sized as its `$preview`; the `support.js` head line exact; `data-props`
valid JSON; every link, citation and relation in the data pointing at something
that exists; and the counts equal to the measurements. The component's syntax is
checked with `node --check` when `node` is present, and said to be unchecked when
it is not.
"""

from __future__ import annotations

import html
import json
import math
import random
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import graph  # noqa: E402
import state  # noqa: E402
import subject  # noqa: E402
import wiki_index  # noqa: E402

HERE = ROOT / "scripts"
TEMPLATE = HERE / "ui.html"
COMPONENT = HERE / "ui.js"
OUT = ROOT / "Plan" / "derived" / "ui"
PAGES = ROOT / "Wiki" / "candidates"
CONFLICTS = ROOT / "Wiki" / "conflicts"
QUESTIONS = ROOT / "Wiki" / "questions"
COMPARE = ROOT / "Wiki" / "compare"
RUNS_DIR = ROOT / "Plan" / "runs"
DECISIONS = ROOT / "Plan" / "decisions"
TOOLS = ROOT / ".agents" / "skills" / "tools" / "SKILL.md"
CANVAS_URL = "https://claude.ai/artifact/1EyhQkX3MpiRTw3TxjTjYL"

SCREENS = ["now", "wiki", "conflicts", "questions", "graph", "corpus", "process"]
FRAMES = [("Main.dc.html", "now", "Now — the app (entry)"), ("Wiki.dc.html", "wiki", "Wiki"),
          ("Conflicts.dc.html", "conflicts", "Conflicts"), ("Questions.dc.html", "questions", "Questions"),
          ("Graph.dc.html", "graph", "Knowledge graph"), ("Corpus.dc.html", "corpus", "Corpus"),
          ("Process.dc.html", "process", "Process")]
WIDTH, HEIGHT = 1440, 900
GRAPH_W, GRAPH_H = 852.0, 740.0


# ---------------------------------------------------------------- the reading order

REC = re.compile(r"^reconcile-(\d+)-(.+)$")


def reading_order() -> list[str]:
    """The reconciled documents, in the order they were reconciled.

    `Wiki/compare/reconcile-NN-<slug>.md` numbers each reconciliation; the first
    document has none, because there was nothing to reconcile it against. A
    document reconciled twice counts from its first record.
    """
    first: dict[str, int] = {}
    for path in COMPARE.glob("reconcile-*.md"):
        m = REC.match(path.stem)
        if m:
            first[m.group(2)] = min(first.get(m.group(2), 10 ** 6), int(m.group(1)))
    done = sorted(p.parent.name for p in RUNS_DIR.glob("*/reconcile.json"))
    return sorted(done, key=lambda slug: (first.get(slug, 0), slug))


# ---------------------------------------------------------------- markdown → runs and blocks
#
# A run list is what one paragraph says, typed: a plain string, or
# ['b'|'g'|'i'|'c', text] for bold, a German quotation, italic and code,
# ['l', label, page] for a [[link]], ['r', [[doc, lines], ...]] for a citation,
# where doc is a reading-order index or the slug of an unread document.
# A block is ['p'|'q'|'h', runs], ['ul'|'ol', [runs]], ['pre', text] or
# ['tb', head, rows, align, columns].

TOKEN = re.compile(
    r"(\[\[[^\]]+\]\])"                                          # 1 wiki link
    r"|(\^\[[^\]]+\])"                                           # 2 citation
    r"|(`[^`]+`)"                                                # 3 code
    r"|(\*\*.+?\*\*)"                                            # 4 bold
    r"|(\[[^\]]+\]\([^)]+\))"                                    # 5 markdown link
    r"|((?<![\w*])\*(?![\s*])[^*]+?(?<![\s*])\*(?![\w*]))"       # 6 italic
)
CITE = re.compile(r"([A-Za-z0-9][A-Za-z0-9\-]*)\.md:((?:L?\d+(?:\s*[–-]\s*L?\d+)?(?:,\s*)?)+)")
LIST_ITEM = re.compile(r"^(\s*)([-*]|\d+\.)\s+(.*)$")
DATE = re.compile(r"\b(20\d\d-\d\d-\d\d)\b")


class Renderer:
    """Markdown as this repository writes it, into the app's run and block lists."""

    def __init__(self, pages: list[str], read: list[str]):
        self.page = {slug: i for i, slug in enumerate(pages)}
        self.read = read

    def _doc(self, slug: str):
        return self.read.index(slug) if slug in self.read else slug

    def _cite(self, token: str, ctx: str | None) -> list:
        inner = token[2:-1]
        parts = CITE.findall(inner)
        if parts:
            return ["r", [[self._doc(slug), re.sub(r"\s+", " ", lines).strip().rstrip(",")] for slug, lines in parts]]
        return ["r", [[self._doc(ctx) if ctx else -1, re.sub(r"\s+", " ", inner).strip()]]]

    def _inline(self, text: str, bold: bool, ctx: str | None) -> list:
        runs, pos, plain = [], 0, "b" if bold else "t"
        for m in TOKEN.finditer(text):
            if m.start() > pos:
                runs.append([plain, text[pos:m.start()]])
            token = m.group(0)
            if m.group(1):
                target, _, label = token[2:-2].partition("|")
                runs.append(["l", (label or target).strip(), target.strip()])
            elif m.group(2):
                runs.append(self._cite(token, ctx))
            elif m.group(3):
                runs.append(["c", token[1:-1]])
            elif m.group(4):
                runs.extend(self._inline(token[2:-2], True, ctx))
            elif m.group(5):
                runs.append([plain, re.match(r"\[([^\]]+)\]", token).group(1)])
            else:
                runs.append(["i", token[1:-1]])
            pos = m.end()
        if pos < len(text):
            runs.append([plain, text[pos:]])
        return runs

    @staticmethod
    def _quotes(runs: list) -> list:
        """A German quotation („…") is the source's own words: its own run type."""
        out, inside = [], False
        for r in runs:
            if r[0] not in ("t", "b", "i"):
                out.append(r)
                continue
            buf = ""
            for ch in r[1]:
                if not inside and ch == "„":
                    if buf:
                        out.append([r[0], buf])
                    buf, inside = ch, True
                elif inside and ch in "\"“”":
                    out.append(["g", buf + ch])
                    buf, inside = "", False
                else:
                    buf += ch
            if buf:
                out.append(["g" if inside else r[0], buf])
        merged: list = []
        for r in out:
            if merged and r[0] == merged[-1][0] and r[0] in ("t", "b", "i", "g", "c"):
                merged[-1] = [r[0], merged[-1][1] + r[1]]
            else:
                merged.append(r)
        return merged

    def runs(self, text: str, ctx: str | None = None) -> list:
        text = re.sub(r"\s+", " ", re.sub(r"<!--.*?-->", "", text)).strip()
        out = []
        for r in self._quotes(self._inline(text, False, ctx)):
            if r[0] == "t":
                out.append(r[1])
            elif r[0] == "l":
                out.append(["l", r[1], self.page[r[2]]] if r[2] in self.page else r[1])
            else:
                out.append(r)
        return out

    @staticmethod
    def text(runs: list) -> str:
        return "".join(r if isinstance(r, str) else "" if r[0] == "r" else r[1] for r in runs)

    @staticmethod
    def _row(row: str) -> list[str]:
        """Split a table row on `|`, never inside `[[slug|label]]` or code."""
        s = row.strip()
        s = s[1:] if s.startswith("|") else s
        s = s[:-1] if s.endswith("|") and not s.endswith("\\|") else s
        cells, buf, depth, code, i = [], "", 0, False, 0
        while i < len(s):
            c = s[i]
            if c == "\\" and s[i + 1:i + 2] == "|":
                buf, i = buf + "|", i + 2
                continue
            if c == "`":
                code = not code
            if not code and s.startswith("[[", i):
                depth, buf, i = depth + 1, buf + "[[", i + 2
                continue
            if not code and depth and s.startswith("]]", i):
                depth, buf, i = depth - 1, buf + "]]", i + 2
                continue
            if c == "|" and not depth and not code:
                cells.append(buf.strip())
                buf, i = "", i + 1
                continue
            buf, i = buf + c, i + 1
        cells.append(buf.strip())
        return cells

    def table(self, rows: list[str], ctx: str | None) -> list:
        cells = [self._row(r) for r in rows]
        sep = len(cells) > 1 and all(re.fullmatch(r":?-+:?", c.replace(" ", "")) or not c for c in cells[1])
        n = max(len(r) for r in cells)
        pad = lambda r: r + [""] * (n - len(r))  # noqa: E731
        align = "".join("r" if sep and j < len(cells[1]) and cells[1][j].strip().endswith(":")
                        and not cells[1][j].strip().startswith(":") else "l" for j in range(n))
        head = [self.runs(c, ctx) for c in pad(cells[0])]
        body = [[self.runs(c, ctx) for c in pad(r)] for r in (cells[2:] if sep else cells[1:])]
        widths = []
        for j in range(n):
            lengths = sorted(len(self.text(row[j])) for row in [head] + body)
            widths.append(max(0.55, min(4.0, math.sqrt(max(lengths[len(lengths) // 2], lengths[-1] * 0.5, 1)) / 3.2)))
        return ["tb", head, body, align, " ".join(f"minmax(0, {w:.2f}fr)" for w in widths)]

    def blocks(self, md: str, ctx: str | None = None) -> list:
        lines, out, para, i = md.split("\n"), [], [], 0

        def flush() -> None:
            text = " ".join(x.strip() for x in para).strip()
            if text and text != "---":
                out.append(["p", self.runs(text, ctx)])
            para.clear()

        while i < len(lines):
            line = lines[i]
            s = line.strip()
            if s.startswith("```"):
                flush()
                j = i + 1
                while j < len(lines) and not lines[j].strip().startswith("```"):
                    j += 1
                out.append(["pre", "\n".join(lines[i + 1:j]).rstrip()])
                i = j + 1
                continue
            if not s or s == "---":
                flush()
                i += 1
                continue
            heading = re.match(r"^#{1,6}\s+(.*)$", s)
            if heading:
                flush()
                out.append(["h", self.runs(heading.group(1), ctx)])
                i += 1
                continue
            if s.startswith(">"):
                flush()
                quoted = []
                while i < len(lines) and lines[i].strip().startswith(">"):
                    quoted.append(lines[i].strip()[1:].strip())
                    i += 1
                chunk: list[str] = []
                for q in quoted + [""]:
                    if q:
                        chunk.append(q)
                    elif chunk:
                        if all(LIST_ITEM.match(x) for x in chunk):
                            chunk = [" · ".join(LIST_ITEM.match(x).group(3) for x in chunk)]
                        out.append(["q", self.runs(" ".join(chunk), ctx)])
                        chunk = []
                continue
            if s.startswith("|"):
                flush()
                rows = []
                while i < len(lines) and lines[i].strip().startswith("|"):
                    rows.append(lines[i].strip())
                    i += 1
                out.append(self.table(rows, ctx))
                continue
            item = LIST_ITEM.match(line)
            if item and len(item.group(1)) < 2:
                flush()
                kind, items = "ol" if item.group(2)[0].isdigit() else "ul", []
                while i < len(lines):
                    t = lines[i]
                    it = LIST_ITEM.match(t)
                    if it and len(it.group(1)) < 2:
                        items.append([it.group(3)])
                    elif t.strip() and items and t[:1] in (" ", "\t"):
                        items.append([it.group(3)]) if it else items[-1].append(t.strip())
                    else:
                        break
                    i += 1
                out.append([kind, [self.runs(" ".join(x), ctx) for x in items]])
                continue
            para.append(line)
            i += 1
        flush()
        return out

    def sections(self, body: str, ctx: str | None = None) -> tuple[str, list, list]:
        """(title, lede, sections); a section is [heading runs, document, date, blocks].

        A heading naming a read document carries it as the section's document,
        and the slug leaves the heading text: the app shows it as a siglum.
        """
        title = ""
        h1 = re.search(r"^# (.+)$", body, re.M)
        if h1:
            title = h1.group(1).strip()
            body = body[:h1.start()] + body[h1.end():]
        parts = re.split(r"^## (.+)$", body, flags=re.M)
        secs = []
        for j in range(1, len(parts), 2):
            head = parts[j].strip()
            doc = next((s for s in self.read if s in head), None)
            shown = head
            if doc:
                shown = re.sub(r"`" + re.escape(doc) + r"`\s*,?\s*", "", shown)
                shown = re.sub(r"—\s*—", "—", re.sub(r"\(\s*\)", "", shown)).strip(" ,—") or head
            date = DATE.search(shown) or DATE.search(head)
            secs.append([self.runs(shown), self.read.index(doc) if doc else -1,
                         date.group(1) if date else "", self.blocks(parts[j + 1], doc or ctx)])
        return title, self.blocks(parts[0], ctx), secs


# ---------------------------------------------------------------- the invariants, run now

INVARIANTS = ["scripts/account.py order", "scripts/state.py --prose", "scripts/judgements.py",
              "scripts/quotes.py", "scripts/duplicates.py", "scripts/qmd_coverage.py", "scripts/relations.py",
              "scripts/link.py", "scripts/sources.py check", "scripts/selftest.py"]


def run_invariants(measured: dict) -> list[list[str]]:
    """[command, held | red | not run, what it said]. Only commands that write nothing run."""
    out = []
    for cmd in INVARIANTS:
        if cmd == "scripts/judgements.py":
            total, agree, dis = (measured[k] for k in ("judgements.total", "judgements.mechanised", "judgements.disagree"))
            out.append([cmd, "held" if dis == 0 else "red",
                        f"{total} judgements: {agree} agree, {dis} DISAGREE, {total - agree - dis} still judgement "
                        "— the replay scripts/state.py performs, since running this rewrites Plan/runs/judgements.md"])
            continue
        proc = subprocess.run([sys.executable, *cmd.split()], cwd=ROOT, capture_output=True, text=True, timeout=600)
        lines = [ln.strip() for ln in (proc.stdout + proc.stderr).splitlines() if ln.strip()] or ["(no output)"]
        joined = " ".join(lines)
        if cmd == "scripts/qmd_coverage.py" and proc.returncode and "qmd" in joined and "No such file" in joined:
            out.append([cmd, "not run", "qmd is not installed in this container — scripts/setup_qmd.sh rebuilds it"])
            continue
        line = lines[-1]
        if cmd == "scripts/account.py order":
            line = ("holds — every document with a census has a note and a reconciliation, in order"
                    if '"holds": true' in joined else line)
        elif cmd == "scripts/quotes.py":
            k = next((n for n, ln in enumerate(lines) if "cited quotes checked" in ln), None)
            if k is not None:
                line = lines[k] + (" " + lines[k + 1] if k + 1 < len(lines) and not lines[k].endswith(".") else "")
        elif cmd == "scripts/relations.py":
            line = "; ".join(re.sub(r"\s+", " ", ln) for ln in lines
                             if re.match(r"^(relations|orphans|isolated|unmarked)\b", ln))
            line += "" if "BROKEN" in joined else "; no broken links"
        elif cmd in ("scripts/link.py", "scripts/duplicates.py"):
            line = next((ln for ln in lines if "would be marked" in ln or "distinct documents" in ln), line)
        out.append([cmd, "held" if proc.returncode == 0 else "red", line])
    return out


def run_selftests() -> list[list[str]]:
    proc = subprocess.run([sys.executable, "scripts/selftests.py"], cwd=ROOT, capture_output=True, text=True, timeout=1800)
    rows = []
    for line in proc.stdout.splitlines():
        m = re.match(r"^\s+(held|FAILED|not run)\s+(.+?)\s{2,}(.*)$", line)
        if m:
            rows.append([m.group(1), m.group(2).strip(), m.group(3).strip()])
    return rows


# ---------------------------------------------------------------- export

def _section(text: str, head: str) -> str:
    """The body under the heading that starts with `head`, to the next heading of its level or above."""
    m = re.search(r"^(#{2,3}) " + re.escape(head) + r".*?$\n", text, re.M)
    if not m:
        return ""
    end = re.compile(r"^#{1," + str(len(m.group(1))) + r"} ", re.M).search(text, m.end())
    return text[m.end():end.start() if end else len(text)]


def _layout(nodes: list[dict], edges: list[list[int]]) -> None:
    """Documents pinned on an ellipse in reading order; the rest by force, seeded."""
    cx, cy, rx, ry = GRAPH_W / 2, GRAPH_H / 2, 392.0, 336.0
    rng = random.Random(7)
    count = len(nodes)
    pinned, pos = set(), []
    docs = sum(1 for n in nodes if n["k"] == "doc") or 1
    for i, n in enumerate(nodes):
        if n["k"] == "doc":
            angle = -math.pi / 2 + 2 * math.pi * n["ref"] / docs
            pos.append([cx + rx * math.cos(angle), cy + ry * math.sin(angle)])
            pinned.add(i)
        else:
            pos.append([cx + rng.uniform(-200, 200), cy + rng.uniform(-160, 160)])
    weight = {0: 1.0, 1: 0.25, 2: 0.0, 3: 0.9, 4: 0.8, 5: 0.25, 6: 0.8}
    springs: dict[tuple[int, int], float] = defaultdict(float)
    for a, b, t in edges:
        if weight[t]:
            springs[(min(a, b), max(a, b))] += weight[t]
    k = math.sqrt(GRAPH_W * GRAPH_H / max(count, 1)) * 0.8
    temp = 60.0
    for _ in range(900):
        disp = [[0.0, 0.0] for _ in range(count)]
        for i in range(count):
            xi, yi = pos[i]
            for j in range(i + 1, count):
                dx, dy = xi - pos[j][0], yi - pos[j][1]
                f = k * k / (dx * dx + dy * dy + 0.01)
                disp[i][0] += dx * f
                disp[i][1] += dy * f
                disp[j][0] -= dx * f
                disp[j][1] -= dy * f
        for (a, b), w in springs.items():
            dx, dy = pos[a][0] - pos[b][0], pos[a][1] - pos[b][1]
            d = math.sqrt(dx * dx + dy * dy) + 0.01
            f = 0.5 * w * d / k
            disp[a][0] -= dx * f
            disp[a][1] -= dy * f
            disp[b][0] += dx * f
            disp[b][1] += dy * f
        for i in range(count):
            if i in pinned:
                continue
            disp[i][0] += (cx - pos[i][0]) * 0.01
            disp[i][1] += (cy - pos[i][1]) * 0.01
            dx, dy = disp[i]
            d = math.sqrt(dx * dx + dy * dy) + 0.01
            step = min(d, temp)
            pos[i][0] += dx / d * step
            pos[i][1] += dy / d * step
            ex, ey = (pos[i][0] - cx) / (rx - 46), (pos[i][1] - cy) / (ry - 40)
            r = math.sqrt(ex * ex + ey * ey)
            if r > 1:
                pos[i][0], pos[i][1] = cx + (pos[i][0] - cx) / r, cy + (pos[i][1] - cy) / r
        temp = max(1.5, temp * 0.992)
    for i, n in enumerate(nodes):
        n["x"], n["y"] = round(pos[i][0], 1), round(pos[i][1], 1)


def export(checks: bool = True) -> dict:
    """Everything the app shows, as one JSON-able dict."""
    read = reading_order()
    manifest = subject.rows()
    by_slug = {r["slug"]: r for r in manifest}
    slugs = sorted(p.stem for p in PAGES.glob("*.md"))
    pidx = {s: i for i, s in enumerate(slugs)}
    md = Renderer(slugs, read)
    g = graph.build()
    derived = state.derive()["measurements"]
    measured = {k: v["value"] for k, v in derived.items()}

    # pages
    pages = []
    for slug in slugs:
        text = (PAGES / f"{slug}.md").read_text(encoding="utf-8")
        meta = wiki_index.frontmatter(text)
        body, _ = subject._split(text)
        ingested = meta.get("ingested") or []
        title, lede, secs = md.sections(body, ingested[0] if len(ingested) == 1 else None)
        node = g["nodes"].get(f"term:{slug}", {})
        ev = Counter(e["status"] for e in g["evidence"].get(slug, []))
        num = lambda v: int(v) if str(v).isdigit() else 0  # noqa: E731
        pages.append({"s": slug, "t": meta.get("term") or title or slug, "st": meta.get("status", ""),
                      "src": num(meta.get("sources")), "rd": num(meta.get("readings")), "cf": meta.get("conflict", ""),
                      "g": meta.get("gathered", ""), "sf": [x for x in node.get("surfaces", []) if x != slug][:24],
                      "lede": lede, "sec": secs,
                      "ev": [ev.get("verified", 0), ev.get("unchecked", 0), ev.get("unresolved", 0)],
                      "ing": [], "out": [], "in": [], "cx": [], "qx": []})

    # conflicts and questions: text from the file, relations from the graph
    def number(path: Path) -> int:
        return int(re.match(r"[cq](\d+)", path.stem).group(1))

    conflicts, cidx = [], {}
    for path in sorted(CONFLICTS.glob("c*.md"), key=number):
        text = path.read_text(encoding="utf-8")
        meta = wiki_index.frontmatter(text)
        body, _ = subject._split(text)
        title, lede, secs = md.sections(body)
        key = f"conflict:{meta.get('id', path.stem.upper())}"
        node = g["nodes"].get(key, {})
        cidx[key] = len(conflicts)
        status = node.get("status") or ""
        conflicts.append({"id": key.split(":", 1)[1], "f": path.stem, "title": title, "subj": node.get("subject") or "",
                          "kind": node.get("kind") or "", "status": status, "decided": status.startswith("decided"),
                          "first": meta.get("first_seen", ""), "src": meta.get("sources", ""), "pages": [],
                          "lede": lede, "sec": secs, "np": None})
    questions, qidx = [], {}
    for path in sorted(QUESTIONS.glob("q*.md"), key=number):
        text = path.read_text(encoding="utf-8")
        meta = wiki_index.frontmatter(text)
        body, _ = subject._split(text)
        title, lede, secs = md.sections(body)
        key = f"question:{meta.get('id', path.stem.upper())}"
        node = g["nodes"].get(key, {})
        qidx[key] = len(questions)
        questions.append({"id": key.split(":", 1)[1], "f": path.stem, "title": title, "q": node.get("question") or "",
                          "status": node.get("status") or "", "first": meta.get("gathered", ""),
                          "raised": [], "docs": [], "conf": [], "lede": lede, "sec": secs})

    def term(node_id: str):
        return pidx.get(node_id.split(":", 1)[1]) if node_id.startswith("term:") else None

    def doc(node_id: str):
        slug = node_id.split(":", 1)[1]
        return read.index(slug) if node_id.startswith("doc:") and slug in read else None

    for e in g["edges"]:
        a, t, b = e["source"], e["type"], e["target"]
        if t == "links" and term(a) is not None and term(b) is not None:
            pages[term(a)]["out"].append(term(b))
            pages[term(b)]["in"].append(term(a))
        elif t == "reads" and term(a) is not None and doc(b) is not None:
            pages[term(a)]["ing"].append(doc(b))
        elif t == "contests" and a in cidx and term(b) is not None:
            conflicts[cidx[a]]["pages"].append(term(b))
            pages[term(b)]["cx"].append(cidx[a])
        elif t == "raised_by" and a in qidx and term(b) is not None:
            questions[qidx[a]]["raised"].append(term(b))
            pages[term(b)]["qx"].append(qidx[a])
        elif t == "asks" and a in qidx and doc(b) is not None:
            questions[qidx[a]]["docs"].append(doc(b))
        elif t == "concerns" and a in qidx and b in cidx:
            questions[qidx[a]]["conf"].append(cidx[b])
    for p in pages:
        for k in ("ing", "out", "in", "cx", "qx"):
            p[k] = sorted(set(p[k]))

    # the author's agenda, NOW.md
    now_text = (ROOT / "NOW.md").read_text(encoding="utf-8")
    for row in _section(now_text, "The novel — where the sources disagree").splitlines():
        if row.startswith("| **C"):
            cells = Renderer._row(row)
            key = "conflict:" + cells[0].strip("* ")
            if key in cidx:
                conflicts[cidx[key]]["np"] = {"q": md.runs(cells[1]), "pos": md.runs(cells[2])}

    def listed(head: str) -> list:
        return [item for b in md.blocks(_section(now_text, head)) if b[0] in ("ul", "ol") for item in b[1]]

    intro = [b[1] for b in md.blocks(_section(now_text, "Questions for the author")) if b[0] == "p"]
    decided = re.search(r"\*\*Decided so far:\*\*(.*?)\n\n", now_text, re.S)
    agenda = {"intro": intro[0] if intro else [], "decided": md.runs("**Decided so far:**" + decided.group(1)) if decided else [],
              "unsettled": listed("The novel — what no source settles"), "process": listed("The process — the author"),
              "handover": listed("Handover — the next session starts here")}
    _, now_lede, now_secs = md.sections(now_text)
    goal_title, goal_lede, goal_secs = md.sections((ROOT / "GOAL.md").read_text(encoding="utf-8"))

    # the reconciliation records, and the reading log they and reconcile.json keep
    compare, latest = [], {}
    for path in sorted(COMPARE.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        body, _ = subject._split(text)
        m = REC.match(path.stem)
        slug = m.group(2) if m else None
        title, lede, secs = md.sections(body, slug)
        compare.append({"k": f"R{int(m.group(1)):02d}" if m else path.stem[:3], "f": path.stem, "title": title,
                        "d": read.index(slug) if slug in read else -1, "lede": lede, "sec": secs})
        if slug in read:
            latest[slug] = len(compare) - 1
    docs = []
    for i, slug in enumerate(read):
        rec = json.loads((RUNS_DIR / slug / "reconcile.json").read_text(encoding="utf-8"))
        row = by_slug.get(slug, {})
        before, after = rec.get("state_before", {}), rec.get("state_after", {})
        ci = latest.get(slug, -1)
        note = []
        if ci >= 0:
            note = [b[1] for b in compare[ci]["lede"] if b[0] == "p" and any(isinstance(r, str) and r.strip() for r in b[1])][:2]
        date = row.get("index_date", "")
        docs.append({"slug": slug, "sig": f"D{i + 1}", "title": row.get("title", slug), "cat": row.get("category", ""),
                     "date": date, "canon": date >= "2026-05-01", "fmt": row.get("format", ""),
                     "terms": len(rec.get("new_terms") or []), "readings": len(rec.get("new_readings") or []),
                     "conflicts": after.get("conflicts", 0) - before.get("conflicts", 0),
                     "pages": [], "note": note, "rec": ci})
    for i, p in enumerate(pages):
        for d in p["ing"]:
            docs[d]["pages"].append(i)

    # decisions, principles, the tools skill
    decisions = []
    for path in sorted(DECISIONS.glob("[0-9]*.md")):
        text = path.read_text(encoding="utf-8")
        title, lede, secs = md.sections(text)
        field = lambda k: (re.search(r"\*\*" + k + r":\*\*\s*([^·\n]+)", text) or [None, ""])[1].strip()  # noqa: E731
        lede = [b for b in lede if not (b[0] == "p" and md.text(b[1]).startswith("Date:"))]
        decisions.append({"id": path.stem[:3], "f": path.stem, "title": re.sub(r"^\d+ — ", "", title),
                          "date": field("Date"), "by": field("Decided by"), "status": field("Status"),
                          "lede": lede, "sec": secs})
    prin_text = (ROOT / "PRINCIPLES.md").read_text(encoding="utf-8")
    principles = []
    for chunk in re.split(r"^## ", prin_text, flags=re.M)[1:]:
        group, _, rest = chunk.partition("\n")
        for item in re.split(r"^(?=\*\*P\d+ — )", rest, flags=re.M):
            m = re.match(r"^\*\*(P\d+) — (.+?)\*\*\s*(.*)$", item, re.S)
            if m:
                principles.append({"id": m.group(1), "t": m.group(2).rstrip("."), "grp": group.strip(),
                                   "b": md.blocks(m.group(3))})
    principles.sort(key=lambda p: int(p["id"][1:]))
    catalogue = md.blocks(_section(prin_text, "The catalogue"))

    tools = TOOLS.read_text(encoding="utf-8")

    def table_after(marker: str) -> list:
        rows, seen = [], False
        for line in tools[tools.index(marker):].splitlines()[1:]:
            if line.startswith("|"):
                rows.append(line)
                seen = True
            elif seen:
                break
        return md.table(rows, None)

    phases = []
    for m in re.finditer(r"^## (\d) · (.+?)$\n(.*?)(?=^## |\Z)", tools, re.M | re.S):
        paras = [b for b in md.blocks(m.group(3)) if b[0] == "p"]
        code = next((b[1] for b in md.blocks(m.group(3)) if b[0] == "pre"), "")
        cmds = [re.sub(r"\s+#.*$", "", ln).strip() for ln in code.splitlines()
                if ln.strip() and not ln.strip().startswith("#") and not re.match(r"^[│┌└▲▼\s─]", ln)]
        said = md.text(paras[0][1]) if paras else ""
        cut = [m2.end() for m2 in re.finditer(r"[.:](\s|$)", said) if m2.end() >= 120]
        phases.append({"n": m.group(1), "t": m.group(2).split(" — ")[0].strip(),
                       "d": said[:cut[0]].strip() if cut and cut[0] < len(said) - 1 else said, "cmd": "\n".join(cmds[:3])})
    missing = md.blocks(_section(tools, "What is missing, stated plainly"))

    # graph nodes and edges, laid out
    gnodes, gid = [], {}
    for nid, n in g["nodes"].items():
        kind = n["type"]
        if kind == "term":
            ref, label = pidx[n["slug"]], pages[pidx[n["slug"]]]["t"]
        elif kind == "doc":
            if n["slug"] not in read:
                continue
            ref, label = read.index(n["slug"]), f"D{read.index(n['slug']) + 1}"
        elif kind == "conflict":
            ref, label = cidx[nid], nid.split(":", 1)[1]
        else:
            ref, label = qidx[nid], nid.split(":", 1)[1]
        gid[nid] = len(gnodes)
        gnodes.append({"k": kind, "ref": ref, "label": label})
    types = ["links", "reads", "cites", "contests", "raised_by", "asks", "concerns"]
    seen_edges: set[tuple[int, int, int]] = set()
    gedges = []
    for e in g["edges"]:
        a, b = gid.get(e["source"]), gid.get(e["target"])
        if a is None or b is None or a == b or e["type"] not in types:
            continue
        key = (a, b, types.index(e["type"]))
        if key not in seen_edges:
            seen_edges.add(key)
            gedges.append(list(key))
    _layout(gnodes, gedges)
    degree = Counter()
    for a, b, t in gedges:
        if t == 0:
            degree[a] += 1
            degree[b] += 1
    for i, n in enumerate(gnodes):
        n["deg"] = degree[i]

    cats = sorted({r["category"] for r in manifest})
    tiers = sorted({r.get("tier", "") for r in manifest})
    fmts = sorted({r.get("format", "") for r in manifest})
    sections = sorted({r.get("index_section", "") for r in manifest})
    rows = [[r["title"], r["slug"], cats.index(r["category"]), tiers.index(r.get("tier", "")),
             fmts.index(r.get("format", "")), r.get("index_date", ""), 1 if r.get("export_path") else 0,
             read.index(r["slug"]) if r["slug"] in read else -1, sections.index(r.get("index_section", ""))]
            for r in manifest]
    folded = sum(1 for line in (ROOT / "Sources" / "duplicates.jsonl").read_text(encoding="utf-8").splitlines() if line.strip())

    head = subprocess.run(["git", "log", "-1", "--format=%h %cs"], cwd=ROOT, capture_output=True, text=True).stdout.split()
    return {
        "meta": {"commit": head[0] if head else "", "date": head[1] if len(head) > 1 else ""},
        "state": {k: [v["value"], v["how"]] for k, v in derived.items()},
        "docs": docs, "pages": pages, "conflicts": conflicts, "questions": questions, "compare": compare,
        "agenda": agenda, "now": {"lede": now_lede, "sec": now_secs},
        "goal": {"title": goal_title, "lede": goal_lede, "sec": goal_secs},
        "decisions": decisions, "principles": principles, "catalogue": catalogue,
        "invariants": table_after("## 0 · Invariants"), "commands": table_after("## The commands, as combinations"),
        "phases": phases, "missing": missing,
        "checks": run_invariants(measured) if checks else [], "selftests": run_selftests() if checks else [],
        "graph": {"nodes": gnodes, "edges": gedges, "types": types, "w": GRAPH_W, "h": GRAPH_H},
        "catdesc": {r["category"]: r.get("index_section", "") for r in manifest},
        "corpus": {"cats": cats, "tiers": tiers, "fmts": fmts, "sections": sections, "rows": rows, "folded": folded},
    }


# ---------------------------------------------------------------- assemble

RUNS = (
    '<sc-for list="{{%s}}" as="r" hint-placeholder-count="1">'
    '<sc-if value="{{r.isT}}" hint-placeholder-val="{{ true }}"><span>{{r.x}}</span></sc-if>'
    '<sc-if value="{{r.isB}}" hint-placeholder-val="{{ false }}"><strong style="font-weight: 600;">{{r.x}}</strong></sc-if>'
    '<sc-if value="{{r.isG}}" hint-placeholder-val="{{ false }}"><span style="font-family: \'Newsreader\', Georgia, serif; font-size: 1.06em; color: #2A2823;">{{r.x}}</span></sc-if>'
    '<sc-if value="{{r.isI}}" hint-placeholder-val="{{ false }}"><em>{{r.x}}</em></sc-if>'
    '<sc-if value="{{r.isC}}" hint-placeholder-val="{{ false }}"><code style="font-family: \'IBM Plex Mono\', ui-monospace, monospace; font-size: 0.84em; padding: 1px 4px; border-radius: 3px; background: #EFEBE1; color: #3A3730; overflow-wrap: anywhere;">{{r.x}}</code></sc-if>'
    '<sc-if value="{{r.isL}}" hint-placeholder-val="{{ false }}"><button type="button" onClick="{{r.go}}" class="kp-link" style="display: inline; margin: 0; padding: 0; border: 0; background: none; font: inherit; line-height: inherit; text-align: inherit; color: #2B4C8C; text-decoration: underline; text-decoration-color: #A9B6D0; text-underline-offset: 3px; cursor: pointer;">{{r.x}}</button></sc-if>'
    '<sc-if value="{{r.isR}}" hint-placeholder-val="{{ false }}"><span title="{{r.title}}" style="display: inline-block; margin: 0 1px; padding: 0 4px; border-radius: 3px; background: #E4E9F2; color: #2B4C8C; font-family: \'IBM Plex Mono\', ui-monospace, monospace; font-size: 10.5px; line-height: 1.6; vertical-align: 1px; white-space: nowrap; cursor: help;">{{r.x}}</span></sc-if>'
    '</sc-for>'
)
_LINK_BRANCH = RUNS[RUNS.index('<sc-if value="{{r.isL}}"'):RUNS.index('<sc-if value="{{r.isR}}"')]
RUNSFLAT = RUNS.replace(_LINK_BRANCH, "")

FRAME = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Kohärenz Protokoll — {title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<style>
body{{margin:0;background:#F3F0E8}}
</style>
</helmet>
<div style="width: {w}px; height: {h}px; overflow: hidden; background: #F3F0E8;">
<dc-import name="Main" screen="{screen}" hint-size="{w}px,{h}px"></dc-import>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
  renderVals() {{
    return {{}};
  }}
}}
</script>
</body>
</html>
'''


def data_script(data: dict, js: str | None = None) -> str:
    """The component with the data in its slot, safe inside a <script> element."""
    text = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    text = text.replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    js = js if js is not None else COMPONENT.read_text(encoding="utf-8")
    if js.count("__DATA__") != 1:
        raise SystemExit("scripts/ui.js must hold exactly one __DATA__ slot")
    return js.replace("__DATA__", text)


def main_artboard(data: dict, template: str | None = None) -> str:
    props = {"screen": {"editor": "enum", "options": SCREENS, "default": "now", "section": "Start"},
             "$preview": {"width": WIDTH, "height": HEIGHT}}
    attr = json.dumps(props, separators=(",", ":")).replace("&", "&amp;").replace("'", "&#39;")
    markup = template if template is not None else TEMPLATE.read_text(encoding="utf-8")
    markup = re.sub(r"@RUNSFLAT\(([^)@]+)\)@", lambda m: RUNSFLAT % m.group(1), markup)
    markup = re.sub(r"@RUNS\(([^)@]+)\)@", lambda m: RUNS % m.group(1), markup)
    markup = markup.replace("@TITLE@", "Kohärenz Protokoll — Now").replace("@PROPS@", attr)
    return markup.replace("@JS@", data_script(data))


def canvas_index() -> dict:
    gap, row2 = 80, HEIGHT + 420
    place = [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1)]
    boards = {}
    for (name, _, title), (col, row) in zip(FRAMES, place):
        boards[name] = {"x": col * (WIDTH + gap), "y": row * row2, "w": WIDTH, "h": HEIGHT,
                        "title": title, "is_interactive": True}
    return {
        "v": 3, "createdOnFiles": {"v": 1, "at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")},
        "title": "Kohärenz Protokoll UI", "launch": {"view": "canvas"}, "pages": [], "boards": boards,
        "order": [name for name, _, _ in FRAMES],
        "notes": {
            "row1": {"x": 0, "y": -300, "kind": "title1", "maxW": 4 * WIDTH + 3 * gap,
                     "text": "Kohärenz Protokoll — the whole project as one app: what the sources say, and what waits on the author"},
            "row2": {"x": 0, "y": row2 - 300, "kind": "title1", "maxW": 3 * WIDTH + 2 * gap,
                     "text": "The graph, the corpus, and the process that keeps the wiki honest"},
            "howto": {"x": -560, "y": 0, "w": 440, "size": "m", "fill": "blue",
                      "text": "Every frame is the same app, opened on a different screen. Press Play on any frame to use it: "
                              "the left rail switches screens, the search box covers the whole project, and every page, "
                              "conflict, question, document and graph node links to the others.\n\n"
                              "Derived by scripts/ui.py from the repository; the snapshot's commit is on the app's rail."},
        },
        "designSystems": [],
    }


def build(out: Path = OUT, checks: bool = True) -> dict:
    data = export(checks)
    project = out / "canvas" / "project"
    if project.exists():
        shutil.rmtree(project)
    project.mkdir(parents=True)
    (project / "Main.dc.html").write_text(main_artboard(data), encoding="utf-8")
    for name, screen, title in FRAMES[1:]:
        (project / name).write_text(FRAME.format(title=title, screen=screen, w=WIDTH, h=HEIGHT), encoding="utf-8")
    (project / "canvas.json").write_text(json.dumps(canvas_index(), ensure_ascii=False, indent=1), encoding="utf-8")
    (out / "data.json").write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    return data


# ---------------------------------------------------------------- checks

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
INTERACTIVE = {"button", "a", "input", "select", "textarea"}
TABLE = {"table", "thead", "tbody", "tfoot", "tr", "select"}
BLOCK = {"address", "article", "aside", "blockquote", "div", "dl", "fieldset", "figure", "footer", "form", "h1", "h2",
         "h3", "h4", "h5", "h6", "header", "hr", "main", "nav", "ol", "p", "pre", "section", "table", "ul"}
HOLE = re.compile(r"\{\{(.*?)\}\}")
PATH = re.compile(r"^\s*(\$?[A-Za-z_][\w$]*(\.[\w$]+)*|true|false|null|-?\d+(\.\d+)?|'[^']*'|\"[^\"]*\")\s*$")


class _Lint(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[str] = []
        self.problems: list[str] = []

    def _where(self) -> str:
        return f"line {self.getpos()[0]}"

    def handle_starttag(self, tag, attrs):
        if tag in INTERACTIVE and any(t in ("button", "a") for t in self.stack):
            outer = next(t for t in reversed(self.stack) if t in ("button", "a"))
            self.problems.append(f"{self._where()}: <{tag}> inside <{outer}> — the parser closes the outer one")
        if tag in ("sc-for", "sc-if", "dc-import") and self.stack and self.stack[-1] in TABLE:
            self.problems.append(f"{self._where()}: <{tag}> inside <{self.stack[-1]}> — the parser moves it out")
        if tag in BLOCK and "p" in self.stack:
            self.problems.append(f"{self._where()}: <{tag}> inside <p> — the parser closes the <p>")
        if tag not in VOID:
            self.stack.append(tag)

    def handle_startendtag(self, tag, attrs):
        if tag not in VOID and tag not in ("path", "circle", "rect", "line", "ellipse", "polyline", "polygon"):
            self.problems.append(f"{self._where()}: <{tag}/> self-closed — close it explicitly")

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.problems.append(f"{self._where()}: </{tag}> closes nothing")
        elif self.stack[-1] != tag:
            self.problems.append(f"{self._where()}: </{tag}> closes <{self.stack[-1]}>")
            if tag in self.stack:
                while self.stack and self.stack.pop() != tag:
                    pass
        else:
            self.stack.pop()


def lint(markup: str, name: str) -> list[str]:
    """What the canvas would silently get wrong in one artboard's source."""
    problems = []
    head, _, rest = markup.partition('<script type="text/x-dc" data-dc-script')
    if '<script src="./support.js"></script>' not in head.split("</head>")[0]:
        problems.append(f"{name}: the support.js head line is missing or changed")
    leftover = re.findall(r"@[A-Z][A-Z_]*(?:\(|@)", head)
    if leftover:
        problems.append(f"{name}: macro left unexpanded — {', '.join(sorted(set(leftover)))}")
    for m in HOLE.finditer(head):
        if not PATH.match(m.group(1)):
            problems.append(f"{name}: hole {{{{{m.group(1)}}}}} is not a dotted path or a literal")
    parser = _Lint()
    parser.feed(head)
    problems += [f"{name}: {p}" for p in parser.problems]
    unclosed = [t for t in parser.stack if t not in ("html", "body", "x-dc")]
    if unclosed:
        problems.append(f"{name}: unclosed at the end — {' > '.join(unclosed)}")
    props = re.search(r"data-props='([^']*)'", rest)
    if not props:
        problems.append(f"{name}: no data-props")
    else:
        try:
            preview = json.loads(html.unescape(props.group(1))).get("$preview", {})
        except ValueError as exc:
            problems.append(f"{name}: data-props is not JSON — {exc}")
            preview = {}
        root = re.search(r"</helmet>\s*<div[^>]*style=\"([^\"]*)\"", head)
        size = dict(re.findall(r"(width|height):\s*(\d+)px", root.group(1))) if root else {}
        if preview and (int(size.get("width", -1)) != preview.get("width") or int(size.get("height", -1)) != preview.get("height")):
            problems.append(f"{name}: root is {size.get('width')}×{size.get('height')}, $preview "
                            f"{preview.get('width')}×{preview.get('height')}")
    script = rest.split(">", 1)[1].rsplit("</script>", 1)[0] if ">" in rest else ""
    if "class Component extends DCLogic" not in script:
        problems.append(f"{name}: no `class Component extends DCLogic`")
    if "</script" in script.lower():
        problems.append(f"{name}: `</script` inside the component ends it early")
    return problems


def check_data(data: dict) -> list[str]:
    """Every reference in the data points at something that exists; counts are measurements."""
    problems = []
    n_pages, n_docs = len(data["pages"]), len(data["docs"])

    def walk(runs, where):
        for r in runs:
            if isinstance(r, list) and r and r[0] == "l" and not (isinstance(r[2], int) and 0 <= r[2] < n_pages):
                problems.append(f"{where}: link to no page ({r[2]!r})")
            if isinstance(r, list) and r and r[0] == "r":
                for doc, _ in r[1]:
                    if isinstance(doc, int) and not -1 <= doc < n_docs:
                        problems.append(f"{where}: citation of no document ({doc})")

    def blocks(bs, where):
        for b in bs:
            if b[0] in ("p", "q", "h"):
                walk(b[1], where)
            elif b[0] in ("ul", "ol"):
                for item in b[1]:
                    walk(item, where)
            elif b[0] == "tb":
                for cell in b[1] + [c for row in b[2] for c in row]:
                    walk(cell, where)

    records = [(f"page {p['s']}", p) for p in data["pages"]] + [(f"conflict {c['id']}", c) for c in data["conflicts"]] + \
              [(f"question {q['id']}", q) for q in data["questions"]] + [(f"record {c['f']}", c) for c in data["compare"]] + \
              [(f"decision {d['id']}", d) for d in data["decisions"]] + [("NOW.md", data["now"]), ("GOAL.md", data["goal"])]
    for where, rec in records:
        blocks(rec["lede"], where)
        for sec in rec["sec"]:
            walk(sec[0], where)
            blocks(sec[3], where)
            if not -1 <= sec[1] < n_docs:
                problems.append(f"{where}: section of no document ({sec[1]})")
    for p in data["pages"]:
        for key, limit in (("out", n_pages), ("in", n_pages), ("ing", n_docs), ("cx", len(data["conflicts"])),
                           ("qx", len(data["questions"]))):
            bad = [i for i in p[key] if not 0 <= i < limit]
            if bad:
                problems.append(f"page {p['s']}: {key} points at nothing — {bad}")
    measured = {k: v[0] for k, v in data["state"].items()}
    for key, have in (("wiki.pages", n_pages), ("wiki.conflicts", len(data["conflicts"])),
                      ("wiki.questions", len(data["questions"])), ("documents.reconciled", n_docs),
                      ("sources.total", len(data["corpus"]["rows"])),
                      ("sources.landed", sum(r[6] for r in data["corpus"]["rows"])),
                      ("sources.folded", data["corpus"]["folded"]), ("graph.nodes", len(data["graph"]["nodes"])),
                      ("graph.edges", len(data["graph"]["edges"]))):
        if measured.get(key) != have:
            problems.append(f"{key}: the app holds {have}, scripts/state.py measures {measured.get(key)}")
    links = sum(len(p["out"]) for p in data["pages"])
    if measured.get("wiki.relations") != links:
        problems.append(f"wiki.relations: the app holds {links} links, scripts/state.py measures {measured.get('wiki.relations')}")
    return problems


def check_script(data: dict, js: str | None = None) -> tuple[list[str], str]:
    """(problems, what was checked). `node --check` when node is present — never a silent pass."""
    node = shutil.which("node")
    if not node:
        return [], "the component's syntax was NOT checked: node is not installed"
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "component.js"
        path.write_text("class DCLogic {}\n" + data_script(data, js), encoding="utf-8")
        proc = subprocess.run([node, "--check", str(path)], capture_output=True, text=True)
    if proc.returncode:
        return [f"component: {(proc.stderr.strip().splitlines() or ['syntax error'])[-1]}"], "node --check"
    return [], "the component's syntax checked with node --check"


def check(out: Path = OUT, data: dict | None = None) -> tuple[list[str], list[str]]:
    """(problems, notes) for what `build` wrote."""
    project = out / "canvas" / "project"
    problems = []
    for path in sorted(project.glob("*.dc.html")):
        problems += lint(path.read_text(encoding="utf-8"), path.name)
    index = json.loads((project / "canvas.json").read_text(encoding="utf-8"))
    for name in index["order"]:
        if not (project / name).exists():
            problems.append(f"canvas.json: {name} has no file")
    data = data if data is not None else json.loads((out / "data.json").read_text(encoding="utf-8"))
    problems += check_data(data)
    script_problems, note = check_script(data)
    return problems + script_problems, [note]


# ---------------------------------------------------------------- selftest

def selftest() -> list[str]:
    """Each check, handed the defect it exists to name. A case that passes for the
    wrong reason fails: the problem must be reported, and in the right words."""
    failures = []
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp)
        data = build(out, checks=False)
        problems, notes = check(out, data)
        if problems:
            failures.append("the clean build is not clean: " + "; ".join(problems[:5]))
        template = TEMPLATE.read_text(encoding="utf-8")
        anchor = '<div style="flex-grow: 1;"></div>'
        if anchor not in template:
            return failures + ["the selftest's anchor is gone from scripts/ui.html"]
        markup_cases = [
            ("button in button", anchor.replace("</div>", '<button type="button"><button type="button">x</button></button></div>'),
             "inside <button>"),
            ("unclosed div", anchor.replace("</div>", "<div>"), ("unclosed at the end", "closes <div>")),
            ("expression hole", anchor.replace("</div>", "{{ a + b }}</div>"), "is not a dotted path"),
            ("sc-for in table", anchor.replace("</div>", '<table><sc-for list="{{x}}" as="y"></sc-for></table></div>'),
             "inside <table>"),
            ("block in p", anchor.replace("</div>", "<p><div>x</div></p></div>"), "inside <p>"),
            ("macro left", anchor.replace("</div>", "@RAIL_H@</div>"), "unexpanded"),
        ]
        for label, replacement, words in markup_cases:
            found = lint(main_artboard(data, template.replace(anchor, replacement, 1)), "Main.dc.html")
            words = (words,) if isinstance(words, str) else words
            if not any(w in p for p in found for w in words):
                failures.append(f"{label}: not reported as {words!r} — got {found[:2]}")
        broken = json.loads(json.dumps(data))
        broken["pages"][0]["lede"] = [["p", [["l", "nowhere", 10 ** 6]]]]
        if not any("link to no page" in p for p in check_data(broken)):
            failures.append("a link to no page: not reported")
        broken = json.loads(json.dumps(data))
        broken["pages"].pop()
        if not any("wiki.pages" in p for p in check_data(broken)):
            failures.append("a page missing from the app: not reported against wiki.pages")
        if shutil.which("node"):
            broken_js = COMPONENT.read_text(encoding="utf-8").replace("renderVals() {", "renderVals() {{", 1)
            syntax, _ = check_script(data, broken_js)
            if not syntax:
                failures.append("a syntax error in the component: not reported by node --check")
        else:
            notes.append("node absent: the syntax case did not run")
    return failures


# ---------------------------------------------------------------- main

def main(argv: list[str]) -> int:
    if argv[:1] == ["selftest"]:
        failures = selftest()
        for f in failures:
            print(f"  FAILED  {f}")
        print(f"ui: {'every check reported its defect' if not failures else str(len(failures)) + ' case(s) failed'} "
              "(clean build, 6 markup, 2 data, 1 syntax)")
        return 1 if failures else 0
    data = build(OUT, checks="--no-checks" not in argv)
    project = OUT / "canvas" / "project"
    size = (project / "Main.dc.html").stat().st_size
    print(f"wrote {project.relative_to(ROOT)}/ — {len(FRAMES)} artboards and canvas.json; "
          f"Main.dc.html {size / 1024:.0f} KB")
    print(f"  {len(data['pages'])} pages · {len(data['conflicts'])} conflicts · {len(data['questions'])} questions · "
          f"{len(data['compare'])} records · {len(data['docs'])} documents read · {len(data['corpus']['rows'])} manifest rows · "
          f"{len(data['graph']['nodes'])} graph nodes")
    if "--check" in argv:
        problems, notes = check(OUT, data)
        for p in problems:
            print(f"  DEFECT  {p}")
        for n in notes:
            print(f"  {n}")
        print(f"{len(problems)} defects in what was written")
        if problems:
            return 1
    print(f"publish from a Claude session: Artifact url {CANVAS_URL}, root {OUT.relative_to(ROOT)}/canvas, "
          "file project/Main.dc.html")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
