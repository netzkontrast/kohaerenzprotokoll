"""Shared page model for the research wiki (``Wiki/``).

Frontmatter parsing, section splitting, wikilink and citation extraction,
readers for the edge index and the log. ``scripts/wiki_lint.py``,
``scripts/render_wiki_views.py`` and the DSPy programs all go through this
module so every tool sees the same page. Standard library plus PyYAML only,
so the lint runs without the DSPy virtualenv.

Page kinds, enums and the citation grammar come from ``wiki_schema``; nothing
here restates them.
"""
from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from . import wiki_schema

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", re.DOTALL)
WIKILINK_RE = re.compile(r"\[\[([^\[\]|#]+?)(?:#[^\[\]|]*)?(?:\|[^\[\]]*)?\]\]")
HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*$", re.MULTILINE)
FENCED_CODE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
QUOTE_FRAGMENT_RE = re.compile(r"„([^“]{3,})“|\"([^\"\n]{3,})\"")
LOG_LINE_RE = re.compile(r"^## \[(\d{4}-\d{2}-\d{2})\] (\S+) \| (.+)$")
TOKEN_RE = re.compile(r"\{\{(\w+)\}\}")

PAGE_DIRS = ("sources", "concepts", "questions", "syntheses")
CANDIDATES_DIR = "candidates"
RENDERED_FILES = ("index.md", "concept-table.md")
FIXED_FILES = ("SCHEMA.md", "log.md", "overview.md")


@dataclass
class Citation:
    """One ``^[file:start-end]`` reference; ``end == start`` for a single line."""

    file: str
    start: int
    end: int
    raw: str


@dataclass
class LogLine:
    """One ``## [date] op | title | k=v | k=v`` entry of ``Wiki/log.md``."""

    date: str
    op: str
    title: str
    fields: dict[str, str]
    raw: str
    lineno: int


@dataclass
class Page:
    """A wiki page: parsed frontmatter plus body, located relative to the wiki root."""

    path: Path
    rel: str
    kind: str | None
    slug: str
    front: dict[str, Any] = field(default_factory=dict)
    body: str = ""
    is_candidate: bool = False
    error: str | None = None

    @property
    def status(self) -> str | None:
        value = self.front.get("status")
        return str(value) if value is not None else None

    @property
    def title(self) -> str:
        return str(self.front.get("title") or self.slug)


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """Return ``(frontmatter, body)``; raise ``ValueError`` on malformed YAML."""
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        raise ValueError(f"frontmatter is not valid YAML: {exc}") from exc
    if data is None:
        data = {}
    if not isinstance(data, dict):
        raise ValueError("frontmatter must be a mapping")
    return data, text[match.end():]


def kind_of(rel: str, front: dict[str, Any]) -> str | None:
    """Kind by directory; candidates declare it in their ``kind`` field."""
    if rel.startswith(CANDIDATES_DIR + "/"):
        value = front.get("kind")
        return str(value) if value else None
    return wiki_schema.kind_for_path(f"Wiki/{rel}")


def load_page(path: Path, wiki_root: Path) -> Page:
    """Load one page; a frontmatter error is recorded on the page, not raised."""
    rel = path.resolve().relative_to(wiki_root.resolve()).as_posix()
    text = path.read_text(encoding="utf-8")
    error = None
    try:
        front, body = split_frontmatter(text)
    except ValueError as exc:
        front, body, error = {}, text, str(exc)
    slug = str(front.get("slug") or path.stem)
    return Page(path=path, rel=rel, kind=kind_of(rel, front), slug=slug,
                front=front, body=body, is_candidate=rel.startswith(CANDIDATES_DIR + "/"),
                error=error)


def iter_pages(wiki_root: Path, include_candidates: bool = True) -> list[Page]:
    """Every page under the kind directories (and candidates), sorted by path."""
    dirs = list(PAGE_DIRS) + ([CANDIDATES_DIR] if include_candidates else [])
    pages = []
    for name in dirs:
        folder = wiki_root / name
        if not folder.is_dir():
            continue
        for path in sorted(folder.rglob("*.md")):
            pages.append(load_page(path, wiki_root))
    return pages


def strip_code(text: str) -> str:
    """Drop fenced and inline code so links or markers inside code never count."""
    return INLINE_CODE_RE.sub("", FENCED_CODE_RE.sub("", text))


def sections(body: str) -> dict[str, str]:
    """Map every level-2 heading to the text up to the next level-1/2 heading."""
    result: dict[str, str] = {}
    matches = list(HEADING_RE.finditer(body))
    for index, match in enumerate(matches):
        if len(match.group(1)) != 2:
            continue
        end = len(body)
        for later in matches[index + 1:]:
            if len(later.group(1)) <= 2:
                end = later.start()
                break
        result[match.group(2).strip()] = body[match.end():end].strip()
    return result


def wikilinks(text: str) -> list[str]:
    """Slugs of every ``[[slug]]`` / ``[[slug|label]]`` / ``[[slug#anchor]]`` outside code."""
    return [m.group(1).strip() for m in WIKILINK_RE.finditer(strip_code(text))]


def citations(text: str) -> list[Citation]:
    """Every ``^[file:L-L]`` citation, per the grammar in ``entities.yaml``."""
    found = []
    for match in wiki_schema.citation_pattern().finditer(text):
        start = int(match.group("start"))
        end = int(match.group("end") or start)
        found.append(Citation(match.group("file"), start, end, match.group(0)))
    return found


def quoted_fragments(text: str) -> list[str]:
    """German „…“ and straight "…" fragments of at least three characters."""
    return [a or b for a, b in QUOTE_FRAGMENT_RE.findall(text)]


def read_edges(path: Path) -> list[dict[str, Any]]:
    """Records of ``Wiki/graph/edges.jsonl``; a bad line raises with its number."""
    if not path.exists():
        return []
    records = []
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{lineno}: not JSON ({exc.msg})") from exc
        if not isinstance(record, dict):
            raise ValueError(f"{path}:{lineno}: record must be an object")
        records.append(record)
    return records


def parse_log_line(line: str, lineno: int = 0) -> LogLine | None:
    """Parse one entry of the log grammar; ``None`` for any other line."""
    match = LOG_LINE_RE.match(line.rstrip())
    if not match:
        return None
    parts = [p.strip() for p in match.group(3).split(" | ")]
    fields: dict[str, str] = {}
    for part in parts[1:]:
        key, sep, value = part.partition("=")
        if sep:
            fields[key.strip()] = value.strip()
    return LogLine(match.group(1), match.group(2), parts[0], fields, line.rstrip(), lineno)


def read_log(path: Path) -> list[LogLine]:
    """Every parseable entry of ``Wiki/log.md`` in file order."""
    if not path.exists():
        return []
    entries = []
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        entry = parse_log_line(line, lineno)
        if entry:
            entries.append(entry)
    return entries


def template_tokens(text: str) -> list[str]:
    """Distinct ``{{token}}`` names of a ``Wiki/templates/*.md.tmpl`` file, in order."""
    seen: dict[str, None] = {}
    for match in TOKEN_RE.finditer(text):
        seen.setdefault(match.group(1), None)
    return list(seen)


def fill_template(text: str, values: dict[str, Any]) -> str:
    """Replace every ``{{token}}``; a token without a value raises ``KeyError``.

    Escaping for YAML (quotes in titles, list syntax) is the caller's job: the
    template puts scalar tokens inside quotes and list tokens inside brackets.
    """
    missing = [name for name in template_tokens(text) if name not in values]
    if missing:
        raise KeyError(f"template tokens without a value: {missing}")
    return TOKEN_RE.sub(lambda m: str(values[m.group(1)]), text)


def body_sha256(body: str) -> str:
    """Hash of a page body with normalised line endings and one trailing newline.

    This is the promotion pin recorded in the log (``conventions.yaml``): a
    reviewed body that changes afterwards produces a different hash.
    """
    normalised = body.replace("\r\n", "\n").rstrip() + "\n"
    return hashlib.sha256(normalised.encode("utf-8")).hexdigest()
