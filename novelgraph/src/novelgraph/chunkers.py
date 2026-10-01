"""The chunkers of `Index/methods.toml`. Each returns line ranges, never text.

A chunk is a range of **file** lines (1-based, inclusive; frontmatter counted, the
convention every `^[slug.md:Lnn]` follows), so its text is always a slice of the
source and a chunk can never misquote it. The smallest unit is therefore a line:
a Drive export often writes a paragraph as one line, and a sentence inside it has
no address of its own. A single line longer than a chunker's maximum stays one
chunk, and `novelgraph stats` counts how many do.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass

TOKEN = re.compile(r"\w+|[^\w\s]")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")


def tokens(text: str) -> int:
    """The embedder-independent token count of `methods.toml` [tokens]."""
    return len(TOKEN.findall(text))


def clean_heading(title: str) -> str:
    title = re.sub(r"\\([!-/:-@\[-`{-~])", r"\1", title)  # CommonMark escapes from the Drive export: `2\.` is `2.`
    title = re.sub(r"[*_`]+", "", title).strip()
    return re.sub(r"\s+", " ", title)


@dataclass
class Line:
    n: int              # file line, 1-based
    text: str
    tokens: int
    heading: int        # heading level, 0 if not a heading
    path: tuple         # heading titles from the outermost, this line's section


def parse(file_lines: list[str], offset: int) -> list[Line]:
    """The body's lines with their section path; headings inside a code fence are not headings."""
    out, stack, fenced = [], [], False
    for i in range(offset - 1, len(file_lines)):
        text = file_lines[i]
        level = 0
        if FENCE.match(text):
            fenced = not fenced
        elif not fenced:
            m = HEADING.match(text)
            if m and clean_heading(m.group(2)):
                level = len(m.group(1))
                stack = [(lv, t) for lv, t in stack if lv < level] + [(level, clean_heading(m.group(2)))]
        out.append(Line(i + 1, text, tokens(text), level, tuple(t for _, t in stack)))
    return out


def heading_tree(lines: list[Line]) -> list[dict]:
    return [{"level": ln.heading, "title": ln.path[-1], "line": ln.n} for ln in lines if ln.heading]


# ── chunk assembly ─────────────────────────────────────────────────────────────

@dataclass
class Unit:
    first: int
    last: int
    tokens: int
    path: tuple
    starts_section: bool


def _span(lines: list[Line], path: tuple) -> dict:
    content = [ln for ln in lines if ln.text.strip()]
    return {"line_start": content[0].n, "line_end": content[-1].n,
            "heading_path": list(path), "tokens": sum(ln.tokens for ln in content)}


DELIMITER = re.compile(r"^\s*\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)*\|?\s*$")


def table_lines(lines: list[Line]) -> set[int]:
    """The file lines that belong to a table, by GFM's rule: a header row with a `|`, a delimiter row
    (`--- | :---:`, outer pipes optional), then every following non-blank row with a `|`. A run of lines
    starting with `|` counts too (the Drive export's tables). A table is never split."""
    out = set()
    i = 0
    while i < len(lines):
        ln = lines[i]
        if not ln.heading and ln.text.lstrip().startswith("|"):
            out.add(ln.n)
        elif (i + 1 < len(lines) and "|" in ln.text and not ln.heading
              and "|" in lines[i + 1].text and DELIMITER.match(lines[i + 1].text)):
            j = i
            while j < len(lines) and lines[j].text.strip() and "|" in lines[j].text and not lines[j].heading:
                out.add(lines[j].n)
                j += 1
            i = j
            continue
        i += 1
    return out


def _blocks(section: list[Line], tables: set[int]) -> list[list[Line]]:
    """Paragraphs (lines up to a blank line) and tables (runs of `|` lines), in order.
    A heading line is glued to the block after it, so no chunk ends on a bare heading."""
    blocks, cur, cur_table = [], [], None
    for ln in section:
        if not ln.text.strip():
            if cur:
                blocks.append(cur)
            cur, cur_table = [], None
            continue
        is_table = ln.n in tables
        if cur and cur_table is not None and is_table != cur_table and not cur[-1].heading:
            blocks.append(cur)
            cur = []
        cur.append(ln)
        cur_table = is_table
    if cur:
        blocks.append(cur)
    glued = []
    for b in blocks:
        if glued and all(ln.heading for ln in glued[-1]):
            glued[-1] = glued[-1] + b
        else:
            glued.append(b)
    return glued


def _is_table(block: list[Line], tables: set[int]) -> bool:
    return all(ln.n in tables for ln in block if not ln.heading)


def heading_v1(lines: list[Line], p: dict) -> list[dict]:
    lo, hi, mn, mx = p["target_min"], p["target_max"], p["min"], p["max"]  # noqa: E741
    tables = table_lines(lines)
    sections: list[list[Line]] = []
    for ln in lines:
        if ln.heading or not sections:
            sections.append([])
        sections[-1].append(ln)
    units: list[Unit] = []
    for sec in sections:
        first_in_section = True
        for block in _blocks(sec, tables):
            content = [ln for ln in block if ln.text.strip()]
            total = sum(ln.tokens for ln in content)
            if total <= hi or _is_table(block, tables):
                pieces = [content]
            else:  # a block over the target is cut between lines, a heading kept with what follows
                pieces, cur, n = [], [], 0
                for ln in content:
                    if cur and not cur[-1].heading and ((n + ln.tokens > hi and n >= lo) or n + ln.tokens > mx):
                        pieces.append(cur)
                        cur, n = [], 0
                    cur.append(ln)
                    n += ln.tokens
                if cur:
                    pieces.append(cur)
            for piece in pieces:
                units.append(Unit(piece[0].n, piece[-1].n, sum(ln.tokens for ln in piece),
                                  piece[0].path, first_in_section))
                first_in_section = False
    groups: list[list[Unit]] = []
    n = 0
    for u in units:
        if groups and groups[-1]:
            flush = ((u.starts_section and n >= mn)
                     or (n + u.tokens > hi and n >= mn)
                     or (n + u.tokens > mx))
            if flush:
                groups.append([])
                n = 0
        if not groups:
            groups.append([])
        groups[-1].append(u)
        n += u.tokens
    # a group under min joins its previous neighbour, else its next, when the pair stays within max
    size = lambda g: sum(u.tokens for u in g)  # noqa: E731
    i = 0
    while i < len(groups):
        if len(groups) > 1 and size(groups[i]) < mn:
            if i > 0 and size(groups[i - 1]) + size(groups[i]) <= mx:
                groups[i - 1].extend(groups.pop(i))
                continue
            if i + 1 < len(groups) and size(groups[i]) + size(groups[i + 1]) <= mx:
                groups[i].extend(groups.pop(i + 1))
                continue
        i += 1
    by_n = {ln.n: ln for ln in lines}
    out = []
    for g in groups:
        span = [by_n[k] for k in range(g[0].first, g[-1].last + 1)]
        out.append(_span(span, g[0].path))
    return out


def section_v1(lines: list[Line], p: dict) -> list[dict]:
    levels = [ln.heading for ln in lines if ln.heading]
    top = min(levels) if levels else 0
    parts: list[list[Line]] = [[]]
    for ln in lines:
        if top and ln.heading == top and any(x.text.strip() for x in parts[-1]):
            parts.append([])
        parts[-1].append(ln)
    out = []
    for part in parts:
        if any(ln.text.strip() for ln in part):
            first = next(ln for ln in part if ln.text.strip())
            path = first.path[:1] if top else ()
            out.append(_span(part, path))
    return out


def window_v1(lines: list[Line], p: dict) -> list[dict]:
    size, overlap = p["size"], int(round(p["size"] * p["overlap"]))
    content = [ln for ln in lines if ln.text.strip()]
    out, i = [], 0
    by_n = {ln.n: ln for ln in lines}
    while i < len(content):
        j, n = i, 0
        while j < len(content):
            n += content[j].tokens
            if n >= size:
                break
            j += 1
        j = min(j, len(content) - 1)
        span = [by_n[k] for k in range(content[i].n, content[j].n + 1)]
        out.append(_span(span, content[i].path))
        if j == len(content) - 1:
            break
        k, tail = j, 0
        while k > i and tail < overlap:
            tail += content[k].tokens
            k -= 1
        i = max(k + 1, i + 1)
    return out


KINDS = {"heading": heading_v1, "section": section_v1, "window": window_v1}


def content_sha(file_lines: list[str], start: int, end: int) -> str:
    return hashlib.sha1("\n".join(file_lines[start - 1:end]).encode("utf-8")).hexdigest()


def chunk_id(slug: str, method: str, start: int, end: int, sha: str) -> str:
    return hashlib.sha1(f"{slug}|{method}|{start}|{end}|{sha}".encode("utf-8")).hexdigest()[:12]


def prefix(title: str, path) -> str:
    return " › ".join([title, *path])


def chunk(slug: str, title: str, file_lines: list[str], offset: int, method: str, params: dict,
          parsed: list[Line] | None = None) -> list[dict]:
    """The chunk rows of one document under one method — exactly the fields `chunks/*.jsonl` holds."""
    lines = parsed if parsed is not None else parse(file_lines, offset)
    if not any(ln.text.strip() for ln in lines):
        return []
    rows = []
    for c in KINDS[params["kind"]](lines, params):
        sha = content_sha(file_lines, c["line_start"], c["line_end"])
        rows.append({"id": chunk_id(slug, method, c["line_start"], c["line_end"], sha),
                     "line_start": c["line_start"], "line_end": c["line_end"],
                     "heading_path": c["heading_path"], "sha": sha, "tokens": c["tokens"],
                     "prefix": prefix(title, c["heading_path"])})
    return rows
