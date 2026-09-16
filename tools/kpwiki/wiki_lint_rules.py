"""Rule functions, shared context and fix plan for ``scripts/wiki_lint.py``.

Every rule is a function ``rule(ctx) -> list[Finding]`` registered in
:data:`RULES` under its rule id (concept §4 F, integration plan §3). The rules
read enums, required fields, transitions, edge types, cross-reference rules,
log ops and writers from ``tools/kpwiki/wiki_schema`` (``Wiki/schema/*.yaml``)
and load pages through ``tools/kpwiki/wiki_pages``; nothing here restates
either. Standard library plus PyYAML only, so the lint runs with the system
``python3``.

Severities: ``error`` fails the lint, ``warn`` and ``info`` never do. The
``--fix`` plan (reverse cross-references per ``xref.yaml`` plus schema
defaults) is computed here as :class:`FixAction` records and applied by the
script.
"""
from __future__ import annotations

import contextlib
import datetime as dt
import hashlib
import json
import re
import subprocess
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Iterator

import yaml

from . import wiki_pages, wiki_schema
from .. import kpgraph
from .wiki_pages import LogLine, Page

SEVERITIES = ("error", "warn", "info")
SPARSE_MIN_WORDS = 60
MISSING_ENTITY_MIN_PAGES = 3
SHINGLE_WORDS = 12
GRAPH_VALUE_MIN_CHARS = 200
SHINGLE_OVERLAP_THRESHOLD = 0.5
CANDIDATE_STAMP_FIELDS = ("ingested", "filed")
MANIFEST_REL = "Sources/manifest.jsonl"
SOURCES_DRIVE_REL = "Sources/drive"
COVERAGE_REL = "graph/coverage.json"

CODEX_REF_RE = re.compile(r"\bcodex:([a-z0-9-]+)")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
# Hex digest length of SHA-256 — a property of the hash, not of the schema.
SHA256_HEX_RE = re.compile(r"^[0-9a-f]{64}$")
GERMAN_QUOTE_RE = re.compile(r"„[^“]*“")
WORD_RE = re.compile(r"\w+")
WHERE_RE = re.compile(r'^(?:(body)|frontmatter\.(\S+)|section "([^"]+)"|edges\.(\S+))$')
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
NAV_DOCS = ("index.md", "overview.md", "concept-table.md", "context-map.md",
            "GLOSSARY.md", "SCHEMA.md", "log.md")


@dataclass
class Finding:
    """One lint result; ``line`` is a 1-based file line or ``None``."""

    rule: str
    severity: str
    path: str
    line: int | None
    message: str

    def render(self) -> str:
        where = f"{self.path}:{self.line}" if self.line else self.path
        return f"{self.severity} {self.rule} {where} — {self.message}"


@dataclass
class FixAction:
    """One reverse cross-reference or schema default that ``--fix`` writes."""

    page: Page
    action: str          # append_slug | append_link | set_slug | set_default
    target: str          # frontmatter field or section heading
    value: Any
    rule_id: str

    def describe(self, path: str) -> str:
        if self.action == "append_slug":
            return f"{path}: append {self.value!r} to frontmatter {self.target} ({self.rule_id})"
        if self.action == "append_link":
            return f'{path}: append [[{self.value}]] to section "{self.target}" ({self.rule_id})'
        if self.action == "set_slug":
            return f"{path}: set frontmatter {self.target} = {self.value!r} ({self.rule_id})"
        return f"{path}: set default {self.target} = {self.value!r} ({self.rule_id})"


@dataclass
class LintContext:
    """Everything the rules read: pages, edge index, log, manifest, caches."""

    wiki_root: Path
    repo_root: Path
    pages: list[Page]
    by_slug: dict[str, Page]
    candidates_by_slug: dict[str, Page]
    edges: list[dict[str, Any]]
    edge_lines: list[int]
    edges_error: str | None
    log: list[LogLine]
    manifest: dict[str, dict[str, Any]]
    manifest_total: int
    body_offsets: dict[str, int]
    file_cache: dict[str, list[str] | None] = field(default_factory=dict)

    @property
    def main_pages(self) -> list[Page]:
        return [p for p in self.pages if not p.is_candidate]

    @property
    def candidates(self) -> list[Page]:
        return [p for p in self.pages if p.is_candidate]

    def display(self, path: Path) -> str:
        try:
            return path.resolve().relative_to(self.repo_root.resolve()).as_posix()
        except ValueError:
            return path.as_posix()

    def page_path(self, page: Page) -> str:
        return self.display(page.path)

    def body_line(self, page: Page, index: int) -> int:
        """File line of the ``index``-th (1-based) body line."""
        return self.body_offsets.get(page.rel, 0) + index

    def file_lines(self, rel: str) -> list[str] | None:
        if rel not in self.file_cache:
            path = self.repo_root / rel
            self.file_cache[rel] = (path.read_text(encoding="utf-8", errors="replace").splitlines()
                                    if path.is_file() else None)
        return self.file_cache[rel]

    def wiki_file(self, repo_rel: str) -> Path:
        """Resolve a ``Wiki/...`` location named in the schema against the wiki root."""
        parts = Path(repo_rel).parts
        if parts and parts[0] == "Wiki":
            return self.wiki_root.joinpath(*parts[1:])
        return self.repo_root / repo_rel

    def resolves(self, slug: str) -> Page | None:
        return self.by_slug.get(slug) or self.candidates_by_slug.get(slug)


# --- context construction ---------------------------------------------------

def build_context(wiki_root: Path, repo_root: Path) -> LintContext:
    pages = wiki_pages.iter_pages(wiki_root) if wiki_root.is_dir() else []
    by_slug: dict[str, Page] = {}
    candidates: dict[str, Page] = {}
    for page in pages:
        (candidates if page.is_candidate else by_slug).setdefault(page.slug, page)
    ctx = LintContext(wiki_root=wiki_root, repo_root=repo_root, pages=pages, by_slug=by_slug,
                      candidates_by_slug=candidates, edges=[], edge_lines=[], edges_error=None,
                      log=[], manifest={}, manifest_total=0,
                      body_offsets={p.rel: body_offset(p) for p in pages})
    conventions = wiki_schema.conventions()
    ctx.edges, ctx.edge_lines, ctx.edges_error = load_edges(
        ctx.wiki_file(conventions["graph"]["wiki_relation_index"]))
    ctx.log = wiki_pages.read_log(ctx.wiki_file(conventions["log"]["file"]))
    ctx.manifest, ctx.manifest_total = load_manifest(repo_root / MANIFEST_REL)
    return ctx


def body_offset(page: Page) -> int:
    """Number of file lines before the body (the frontmatter block)."""
    text = page.path.read_text(encoding="utf-8")
    return text.count("\n") - page.body.count("\n")


def load_edges(path: Path) -> tuple[list[dict[str, Any]], list[int], str | None]:
    try:
        records = wiki_pages.read_edges(path)
    except ValueError as exc:
        return [], [], str(exc)
    lines: list[int] = []
    if path.exists():
        lines = [n for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1)
                 if line.strip()]
    return records, lines, None


def load_manifest(path: Path) -> tuple[dict[str, dict[str, Any]], int]:
    if not path.is_file():
        return {}, 0
    records: dict[str, dict[str, Any]] = {}
    total = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(record, dict):
            total += 1
            if record.get("slug"):
                records.setdefault(str(record["slug"]), record)
    return records, total


# --- schema helpers (everything derived from the YAML) -------------------------

def known_kind(page: Page) -> bool:
    return page.error is None and page.kind in wiki_schema.kinds()


def kind_fields(kind: str) -> dict[str, dict[str, Any]]:
    return wiki_schema.kind(kind).get("fields", {}) or {}


def uses_lifecycle(kind: str) -> bool:
    status_field = wiki_schema.lifecycle()["field"]
    return bool(kind_fields(kind).get(status_field, {}).get("lifecycle"))


def terminal_states() -> list[str]:
    """Lifecycle states with no outgoing transition (the archive)."""
    transitions = wiki_schema.lifecycle()["transitions"]
    return [s for s in wiki_schema.lifecycle()["states"] if not transitions.get(s)]


def contested_state() -> str:
    """The dispute state: named in the ``contradicts`` effect, else the state
    a protected page can enter and leave again."""
    effect = str(wiki_schema.edge_types().get("contradicts", {}).get("effect", ""))
    match = re.search(r"status (\w+)", effect)
    if match:
        return match.group(1)
    transitions = wiki_schema.lifecycle()["transitions"]
    for state in wiki_schema.protected_statuses():
        for target in transitions.get(state, []):
            if state in transitions.get(target, []):
                return target
    return ""


def open_question_state() -> str:
    """The enum lists the initial (open) state of a question first."""
    return wiki_schema.enum_values("question_status")[0]


def terminal_prefixes() -> tuple[str, ...]:
    return tuple(str(t["prefix"]) for t in wiki_schema.xref().get("terminal", []))


def leaf_kinds() -> set[str]:
    """Kinds whose xref rule has no reverse: nothing points back at them."""
    return {r["forward"]["kind"] for r in wiki_schema.xref()["rules"]
            if r.get("reverse") in (None, "none")}


def ref_fields(page: Page) -> list[tuple[str, list[str]]]:
    """``(field, slugs)`` for every ``ref`` / ``list_of_ref`` field the page sets."""
    if not known_kind(page):
        return []
    found = []
    for name, spec in kind_fields(page.kind).items():
        if "list_of_ref" not in spec and "ref" not in spec:
            continue
        value = page.front.get(name)
        if isinstance(value, list):
            found.append((name, [str(v) for v in value]))
        elif isinstance(value, str):
            found.append((name, [value]))
    return found


def sha256_kinds() -> set[str]:
    """Kinds that pin a raw file hash (the source kind)."""
    return {k for k in wiki_schema.kinds() if "sha256" in kind_fields(k)}


# --- small utilities -------------------------------------------------------------

def is_empty(value: Any) -> bool:
    return value is None or (isinstance(value, (str, list, dict)) and not value)


def is_slug(value: Any) -> bool:
    return isinstance(value, str) and bool(wiki_schema.slug_pattern().match(value))


def is_iso_date(value: Any) -> bool:
    if isinstance(value, dt.date):
        return True
    if not isinstance(value, str) or not DATE_RE.match(value):
        return False
    try:
        dt.date.fromisoformat(value)
    except ValueError:
        return False
    return True


def as_date(value: Any) -> dt.date | None:
    if isinstance(value, dt.datetime):
        return value.date()
    if isinstance(value, dt.date):
        return value
    if isinstance(value, str) and is_iso_date(value):
        return dt.date.fromisoformat(value)
    return None


def normalise_ws(text: str) -> str:
    return " ".join(text.split())


def code_free_lines(body: str) -> list[str]:
    """Body lines with code removed and the line count preserved."""
    blanked = wiki_pages.FENCED_CODE_RE.sub(lambda m: "\n" * m.group(0).count("\n"), body)
    return wiki_pages.INLINE_CODE_RE.sub("", blanked).split("\n")


def iter_links(ctx: LintContext, page: Page) -> Iterator[tuple[int, str]]:
    """``(file line, slug)`` for every wikilink in the page body."""
    for index, line in enumerate(code_free_lines(page.body), 1):
        for slug in wiki_pages.wikilinks(line):
            yield ctx.body_line(page, index), slug


def shingles(text: str) -> set[tuple[str, ...]]:
    words = [w.lower() for w in WORD_RE.findall(text)]
    return {tuple(words[i:i + SHINGLE_WORDS]) for i in range(len(words) - SHINGLE_WORDS + 1)}


def git_output(cwd: Path, args: list[str]) -> str | None:
    try:
        proc = subprocess.run(["git", *args], cwd=cwd, capture_output=True, check=False)
    except OSError:
        return None
    if proc.returncode != 0:
        return None
    return proc.stdout.decode("utf-8", errors="replace")


# --- rule 1: required-field ----------------------------------------------------------

def rule_required_field(ctx: LintContext) -> list[Finding]:
    out: list[Finding] = []
    for page in ctx.pages:
        path = ctx.page_path(page)
        if page.error:
            out.append(Finding("required-field", "error", path, 1,
                               f"frontmatter did not parse: {page.error}"))
            continue
        if page.kind not in wiki_schema.kinds():
            out.append(Finding("required-field", "error", path, 1,
                               f"no recognisable page kind (kind={page.front.get('kind')!r}); "
                               f"known: {wiki_schema.kinds()}"))
            continue
        const = wiki_schema.field_enum(page.kind, "kind")
        if const and page.front.get("kind") != const[0]:
            out.append(Finding("required-field", "error", path, 1,
                               f"kind must be {const[0]!r} under "
                               f"{wiki_schema.kind(page.kind)['dir']}, got {page.front.get('kind')!r}"))
        missing = [f for f in wiki_schema.required_fields(page.kind) if is_empty(page.front.get(f))]
        if missing:
            out.append(Finding("required-field", "error", path, 1,
                               f"missing or empty required fields: {', '.join(missing)}"))
    return out


# --- rule 2: enum -----------------------------------------------------------------------

def field_problem(kind: str, name: str, spec: dict[str, Any], value: Any) -> str | None:
    allowed = wiki_schema.field_enum(kind, name)
    if allowed is not None:
        return None if value in allowed else f"{value!r} is not one of {allowed}"
    if "list_of_ref" in spec:
        if not isinstance(value, list):
            return f"{value!r} must be a list of slugs"
        bad = [v for v in value if not is_slug(v)]
        if bad:
            return f"{bad!r} are not slugs ({wiki_schema.slug_pattern().pattern})"
        if len(value) < int(spec.get("min", 0)):
            return f"needs at least {spec['min']} entries, has {len(value)}"
        return None
    if "ref" in spec:
        return None if is_slug(value) else f"{value!r} is not a slug"
    if "pattern" in spec:
        ok = isinstance(value, str) and re.fullmatch(spec["pattern"], value)
        return None if ok else f"{value!r} does not match {spec['pattern']}"
    if spec.get("format") == "date":
        return None if is_iso_date(value) else f"{value!r} is not an ISO date (YYYY-MM-DD)"
    if spec.get("type") == "bool":
        return None if isinstance(value, bool) else f"{value!r} is not a boolean"
    if spec.get("type") == "int":
        if isinstance(value, bool) or not isinstance(value, int):
            return f"{value!r} is not an integer"
        if "min" in spec and value < int(spec["min"]):
            return f"{value!r} is below {spec['min']}"
        if "max" in spec and value > int(spec["max"]):
            return f"{value!r} is above {spec['max']}"
        return None
    if spec.get("type") == "str":
        if not isinstance(value, str):
            return f"{value!r} is not a string"
        if "max_words" in spec and len(WORD_RE.findall(value)) > int(spec["max_words"]):
            return f"has more than {spec['max_words']} words"
        return None
    if "list_of" in spec:
        if not isinstance(value, list) or len(value) < int(spec.get("min", 0)):
            return f"must be a list with at least {spec.get('min', 0)} entries"
    return None


def rule_enum(ctx: LintContext) -> list[Finding]:
    out: list[Finding] = []
    for page in ctx.pages:
        if not known_kind(page):
            continue
        for name, spec in kind_fields(page.kind).items():
            # A null optional field (``supersedes:`` left empty by the template) is absent.
            if name == "kind" or page.front.get(name) is None:
                continue
            problem = field_problem(page.kind, name, spec, page.front[name])
            if problem:
                out.append(Finding("enum", "error", ctx.page_path(page), 1, f"{name}: {problem}"))
    return out


# --- rule 3: illegal-transition ------------------------------------------------------

def previous_frontmatters(ctx: LintContext) -> dict[str, dict[str, Any]]:
    """Frontmatter of every page as committed at HEAD; empty without git."""
    try:
        wiki_rel = ctx.wiki_root.resolve().relative_to(ctx.repo_root.resolve()).as_posix()
    except ValueError:
        return {}
    prefix = "" if wiki_rel == "." else wiki_rel + "/"
    listing = git_output(ctx.repo_root, ["ls-files", "-z", "--", wiki_rel])
    if listing is None:
        return {}
    tracked = set(listing.split("\0"))
    previous: dict[str, dict[str, Any]] = {}
    for page in ctx.pages:
        rel = prefix + page.rel
        if rel not in tracked:
            continue
        text = git_output(ctx.repo_root, ["show", f"HEAD:{rel}"])
        if text is None:
            continue
        try:
            previous[page.rel] = wiki_pages.split_frontmatter(text)[0]
        except ValueError:
            continue
    return previous


def rule_illegal_transition(ctx: LintContext) -> list[Finding]:
    out: list[Finding] = []
    previous = previous_frontmatters(ctx)
    initial = wiki_schema.lifecycle()["initial"]
    entry_states = sorted({initial, *wiki_schema.protected_statuses()})
    for page in ctx.pages:
        if not known_kind(page) or not uses_lifecycle(page.kind):
            continue
        path, status = ctx.page_path(page), page.status
        if page.is_candidate:
            if status != initial:
                out.append(Finding("illegal-transition", "error", path, 1,
                                   f"a candidate must have status {initial!r}, got {status!r}"))
            continue
        old = previous.get(page.rel, {}).get("status")
        if old is None:
            if status not in entry_states:
                out.append(Finding("illegal-transition", "error", path, 1,
                                   f"a new page enters with status in {entry_states}, got {status!r}"))
        elif status is not None and not wiki_schema.legal_transition(str(old), status):
            out.append(Finding("illegal-transition", "error", path, 1,
                               f"status {old!r} → {status!r} is not a legal transition; "
                               f"allowed: {wiki_schema.lifecycle()['transitions'].get(str(old), [])}"))
    return out


# --- rules 4 + 5: archived-link, broken-link ------------------------------------

def rule_archived_link(ctx: LintContext) -> list[Finding]:
    out: list[Finding] = []
    archived = set(terminal_states())
    for page in ctx.pages:
        for line, slug in iter_links(ctx, page):
            target = ctx.by_slug.get(slug)
            if target is not None and target.status in archived:
                out.append(Finding("archived-link", "warn", ctx.page_path(page), line,
                                   f"[[{slug}]] points to an archived page ({ctx.page_path(target)})"))
    return out


def rule_broken_link(ctx: LintContext) -> list[Finding]:
    out: list[Finding] = []
    for page in ctx.pages:
        for line, slug in iter_links(ctx, page):
            if slug in ctx.by_slug:
                continue
            candidate = ctx.candidates_by_slug.get(slug)
            if candidate is not None:
                out.append(Finding("broken-link", "info", ctx.page_path(page), line,
                                   f"[[{slug}]] resolves to a candidate ({ctx.page_path(candidate)})"))
            else:
                out.append(Finding("broken-link", "error", ctx.page_path(page), line,
                                   f"[[{slug}]] resolves to no wiki page"))
    return out


# --- rule 6: orphan ---------------------------------------------------------------------

def inbound_references(ctx: LintContext) -> tuple[set[str], set[str]]:
    """Slugs linked from another page's body, and slugs named in ref lists."""
    linked: set[str] = set()
    listed: set[str] = set()
    for page in ctx.pages:
        linked.update(slug for _, slug in iter_links(ctx, page) if slug != page.slug)
        for _, slugs in ref_fields(page):
            listed.update(s for s in slugs if s != page.slug)
    return linked, listed


def rule_orphan(ctx: LintContext) -> list[Finding]:
    out: list[Finding] = []
    linked, listed = inbound_references(ctx)
    exempt = leaf_kinds()
    for page in ctx.main_pages:
        if page.kind in exempt or page.slug in linked or page.slug in listed:
            continue
        out.append(Finding("orphan", "warn", ctx.page_path(page), None,
                           f"no other page links [[{page.slug}]] or lists it in sources/concepts"))
    return out


# --- rule 7: missing-entity --------------------------------------------------------

def codex_uses(ctx: LintContext) -> dict[str, list[Page]]:
    uses: dict[str, list[Page]] = defaultdict(list)
    for page in ctx.pages:
        for slug in sorted({m.group(1) for m in CODEX_REF_RE.finditer(wiki_pages.strip_code(page.body))}):
            uses[slug].append(page)
    return uses


def codex_carriers(ctx: LintContext) -> set[str]:
    carriers = set()
    for page in ctx.main_pages:
        if known_kind(page) and "codex_ref" in kind_fields(page.kind) and page.front.get("codex_ref"):
            carriers.add(str(page.front["codex_ref"]))
    return carriers


def rule_missing_entity(ctx: LintContext) -> list[Finding]:
    out: list[Finding] = []
    carriers = codex_carriers(ctx)
    for slug, pages in sorted(codex_uses(ctx).items()):
        if len(pages) < MISSING_ENTITY_MIN_PAGES or f"codex:{slug}" in carriers:
            continue
        names = ", ".join(ctx.page_path(p) for p in pages)
        out.append(Finding("missing-entity", "info", ctx.page_path(pages[0]), None,
                           f"codex:{slug} is used by {len(pages)} pages ({names}) "
                           f"and no concept page carries codex_ref: codex:{slug}"))
    return out


# --- rule 8: sparse-page ------------------------------------------------------------

def rule_sparse_page(ctx: LintContext) -> list[Finding]:
    out: list[Finding] = []
    for page in ctx.main_pages:
        if not known_kind(page):
            continue
        path = ctx.page_path(page)
        present = wiki_pages.sections(page.body)
        missing = [s for s in wiki_schema.kind(page.kind).get("sections", []) if s not in present]
        if missing:
            out.append(Finding("sparse-page", "warn", path, None,
                               f"missing sections: {', '.join(missing)}"))
        words = len(page.body.split())
        if words < SPARSE_MIN_WORDS:
            out.append(Finding("sparse-page", "warn", path, None,
                               f"body has {words} words (fewer than {SPARSE_MIN_WORDS})"))
    return out


def rule_page_size(ctx: LintContext) -> list[Finding]:
    """Keep pages focused; a hard maximum requires a semantic split."""
    out: list[Finding] = []
    for page in ctx.pages:
        if not known_kind(page):
            continue
        budget = wiki_schema.page_budget(page.kind)
        words = len(WORD_RE.findall(wiki_pages.strip_code(page.body)))
        if budget.get("max_words") and words > budget["max_words"]:
            out.append(Finding("page-size", "error", ctx.page_path(page), None,
                               f"body has {words} words; maximum is {budget['max_words']}; split by semantic entity"))
        elif budget.get("warn_words") and words > budget["warn_words"]:
            out.append(Finding("page-size", "warn", ctx.page_path(page), None,
                               f"body has {words} words; split is recommended above {budget['warn_words']}"))
    return out


def rule_page_location(ctx: LintContext) -> list[Finding]:
    """Every page lives exactly one partition below its kind directory."""
    out: list[Finding] = []
    for page in ctx.pages:
        if not known_kind(page):
            continue
        parts = Path(page.rel).parts
        expected = wiki_schema.partition_for(page.kind, page.front)
        root = Path(wiki_schema.kind(page.kind)["dir"]).name
        target = (f"candidates/{root}/{expected}/{page.slug}.md" if page.is_candidate
                  else f"{root}/{expected}/{page.slug}.md")
        if page.rel != target:
            out.append(Finding("page-location", "error", ctx.page_path(page), None,
                               f"must live at {target} (one canonical partition)"))
    return out


def rule_duplicate_slug(ctx: LintContext) -> list[Finding]:
    """Slugs are unique within promoted pages and within candidate pages."""
    out: list[Finding] = []
    for label, pages in (("promoted wiki", ctx.main_pages), ("candidates", ctx.candidates)):
        grouped: dict[str, list[Page]] = defaultdict(list)
        for page in pages:
            grouped[page.slug].append(page)
        for slug, matches in sorted(grouped.items()):
            if len(matches) < 2:
                continue
            paths = ", ".join(ctx.page_path(page) for page in matches)
            out.append(Finding("duplicate-slug", "error", ctx.page_path(matches[0]), None,
                               f"slug {slug!r} occurs {len(matches)} times in {label}: {paths}"))
    return out


def rule_navigation_link(ctx: LintContext) -> list[Finding]:
    """Internal links in the navigation surface must resolve on disk."""
    out: list[Finding] = []
    docs = [ctx.wiki_root / name for name in NAV_DOCS]
    docs.extend(sorted(ctx.wiki_root.glob("**/README.md")))
    for path in docs:
        if not path.is_file():
            continue
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for raw in MARKDOWN_LINK_RE.findall(line):
                target = raw.strip().split("#", 1)[0]
                if not target or "://" in target or target.startswith(("mailto:", "#")):
                    continue
                resolved = (path.parent / target).resolve()
                if not resolved.exists():
                    out.append(Finding("navigation-link", "error", ctx.display(path), lineno,
                                       f"internal link target does not exist: {raw}"))
    return out


def rule_context_window(ctx: LintContext) -> list[Finding]:
    """Retrieval metadata must describe a coherent chapter window."""
    out: list[Finding] = []
    for page in ctx.pages:
        if not known_kind(page) or "context_summary" not in kind_fields(page.kind):
            continue
        start, end = page.front.get("chapter_start"), page.front.get("chapter_end")
        if isinstance(start, int) and isinstance(end, int) and start > end:
            out.append(Finding("context-window", "error", ctx.page_path(page), 1,
                               f"chapter_start {start} is after chapter_end {end}"))
    return out


# --- rule 9: citation-resolves ----------------------------------------------------

def cited_text(ctx: LintContext, cit: wiki_pages.Citation) -> tuple[str | None, str | None]:
    """``(normalised text, problem)`` for one citation."""
    lines = ctx.file_lines(cit.file)
    if lines is None:
        return None, f"{cit.raw}: file {cit.file} not found under {ctx.display(ctx.repo_root)}"
    if not 1 <= cit.start <= cit.end <= len(lines):
        return None, f"{cit.raw}: lines {cit.start}-{cit.end} outside 1-{len(lines)}"
    return normalise_ws(" ".join(lines[cit.start - 1:cit.end])), None


def rule_citation_resolves(ctx: LintContext) -> list[Finding]:
    out: list[Finding] = []
    for page in ctx.pages:
        for index, line in enumerate(code_free_lines(page.body), 1):
            cits = wiki_pages.citations(line)
            if not cits:
                continue
            lineno, path = ctx.body_line(page, index), ctx.page_path(page)
            texts = []
            for cit in cits:
                text, problem = cited_text(ctx, cit)
                if problem:
                    out.append(Finding("citation-resolves", "error", path, lineno, problem))
                else:
                    texts.append(text)
            for fragment in wiki_pages.quoted_fragments(line):
                if texts and not any(normalise_ws(fragment) in t for t in texts):
                    out.append(Finding("citation-resolves", "error", path, lineno,
                                       f"quoted fragment „{fragment}“ is not inside the cited lines"))
    return out


# --- rule 10: stale-source ----------------------------------------------------------

def rule_stale_source(ctx: LintContext) -> list[Finding]:
    out: list[Finding] = []
    hashed = sha256_kinds()
    for page in ctx.pages:
        declared = page.front.get("sha256")
        if not known_kind(page) or page.kind not in hashed or not isinstance(declared, str):
            continue
        drive = ctx.repo_root / SOURCES_DRIVE_REL / f"{page.slug}.md"
        if drive.is_file():
            actual, origin = hashlib.sha256(drive.read_bytes()).hexdigest(), ctx.display(drive)
        else:
            actual, origin = str(ctx.manifest.get(page.slug, {}).get("sha256") or ""), MANIFEST_REL
        if actual and actual != declared:
            out.append(Finding("stale-source", "warn", ctx.page_path(page), 1,
                               f"sha256 {declared[:12]}… differs from {origin} ({actual[:12]}…)"))
    return out


# --- rule 11: xref-symmetry (fixable) ---------------------------------------------

def parse_where(where: str) -> tuple[str, str]:
    match = WHERE_RE.match(str(where))
    if not match:
        raise ValueError(f"xref.yaml: unknown where {where!r}")
    body, front, section, edge = match.groups()
    if body:
        return "body", ""
    if front:
        return "frontmatter", front
    if section:
        return "section", section
    return "edges", edge


def forward_pairs(ctx: LintContext, forward: dict[str, Any]) -> Iterator[tuple[Page, str]]:
    """``(from page, target slug)`` for every forward link of one xref rule."""
    zone, name = parse_where(forward["where"])
    for page in ctx.main_pages:
        if not known_kind(page) or page.kind != forward["kind"]:
            continue
        if zone == "body":
            for slug in sorted(set(wiki_pages.wikilinks(page.body))):
                yield page, slug
        elif zone == "frontmatter":
            value = page.front.get(name)
            for slug in (value if isinstance(value, list) else [value]):
                if isinstance(slug, str):
                    yield page, slug
        elif zone == "edges":
            for edge in ctx.edges:
                if edge.get("type") == name and edge.get("from") == page.slug and isinstance(edge.get("to"), str):
                    yield page, edge["to"]


def reverse_gap(target: Page, reverse: dict[str, Any], from_slug: str, rule_id: str) -> FixAction | None:
    zone, name = parse_where(reverse["where"])
    action = reverse.get("action")
    if zone == "frontmatter" and action == "append_slug":
        listed = target.front.get(name) or []
        if from_slug not in (listed if isinstance(listed, list) else [listed]):
            return FixAction(target, "append_slug", name, from_slug, rule_id)
    elif zone == "frontmatter" and action == "set_slug":
        if target.front.get(name) != from_slug:
            return FixAction(target, "set_slug", name, from_slug, rule_id)
    elif zone == "section" and action == "append_link":
        section = wiki_pages.sections(target.body).get(name, "")
        if from_slug not in wiki_pages.wikilinks(section):
            return FixAction(target, "append_link", name, from_slug, rule_id)
    return None


def xref_gaps(ctx: LintContext) -> list[FixAction]:
    """Every missing reverse link per ``xref.yaml``, as fix actions."""
    actions: list[FixAction] = []
    for rule in wiki_schema.xref()["rules"]:
        reverse = rule.get("reverse")
        if not isinstance(reverse, dict):
            continue
        for from_page, to_slug in forward_pairs(ctx, rule["forward"]):
            target = ctx.by_slug.get(to_slug)
            if target is None or target.kind != reverse["kind"] or target.error or target is from_page:
                continue
            gap = reverse_gap(target, reverse, from_page.slug, rule["id"])
            if gap:
                actions.append(gap)
    return actions


def rule_xref_symmetry(ctx: LintContext) -> list[Finding]:
    return [Finding("xref-symmetry", "warn", ctx.page_path(a.page), None,
                    f"missing reverse link — {a.describe(ctx.page_path(a.page))}")
            for a in xref_gaps(ctx)]


# --- rule 12: edge-evidence ---------------------------------------------------------

def base_edge_keys() -> list[str]:
    """Record keys every edge carries: the schema record minus per-type extras."""
    conditional = {k for spec in wiki_schema.edge_types().values() for k in spec.get("requires", [])}
    return [k for k in wiki_schema.edges()["record"] if k not in conditional]


def is_evidence(value: Any) -> bool:
    return isinstance(value, str) and bool(
        wiki_schema.citation_pattern().search(value) or wiki_pages.WIKILINK_RE.search(value))


def edge_problems(ctx: LintContext, record: dict[str, Any]) -> list[str]:
    problems = [f"missing {k}" for k in base_edge_keys() if is_empty(record.get(k))]
    types = wiki_schema.edge_types()
    kind = record.get("type")
    if kind not in types:
        problems.append(f"type {kind!r} is not one of {sorted(types)}")
    else:
        problems.extend(f"type {kind} requires {k}" for k in types[kind].get("requires", [])
                        if is_empty(record.get(k)))
    confidence = record.get("confidence")
    if confidence is not None and confidence not in wiki_schema.enum_values("confidence"):
        problems.append(f"confidence {confidence!r} is not one of {wiki_schema.enum_values('confidence')}")
    if record.get("evidence") is not None and not is_evidence(record["evidence"]):
        problems.append("evidence must be a ^[file:L-L] citation or a [[slug]]")
    src, dst = record.get("from"), record.get("to")
    if isinstance(src, str) and src and ctx.resolves(src) is None:
        problems.append(f"from {src!r} resolves to no wiki page")
    if isinstance(dst, str) and dst and ctx.resolves(dst) is None and not dst.startswith(terminal_prefixes()):
        problems.append(f"to {dst!r} resolves to no wiki page and is not a {'/'.join(terminal_prefixes())} target")
    writer = record.get("written_by")
    if writer is not None and writer not in wiki_schema.writers()["writers"]:
        problems.append(f"written_by {writer!r} is not a writer in writers.yaml")
    return problems


def rule_edge_evidence(ctx: LintContext) -> list[Finding]:
    path = ctx.display(ctx.wiki_file(wiki_schema.conventions()["graph"]["wiki_relation_index"]))
    if ctx.edges_error:
        return [Finding("edge-evidence", "error", path, None, ctx.edges_error)]
    out: list[Finding] = []
    contested = contested_state()
    for record, lineno in zip(ctx.edges, ctx.edge_lines):
        out.extend(Finding("edge-evidence", "error", path, lineno, p) for p in edge_problems(ctx, record))
        if record.get("type") != "contradicts":
            continue
        for end in (record.get("from"), record.get("to")):
            page = ctx.resolves(end) if isinstance(end, str) else None
            if page is not None and page.status != contested:
                out.append(Finding("edge-evidence", "warn", path, lineno,
                                   f"contradicts endpoint {end} has status {page.status!r}, not {contested!r}"))
    return out


# --- rule 13: writer-policy ---------------------------------------------------------

def rule_writer_policy(ctx: LintContext) -> list[Finding]:
    out: list[Finding] = []
    path = ctx.display(ctx.wiki_file(wiki_schema.conventions()["log"]["file"]))
    ops = wiki_schema.conventions()["log"]["ops"]
    writers = wiki_schema.writers()
    log_field = writers["log_field"]
    for entry in ctx.log:
        if entry.op not in ops:
            out.append(Finding("writer-policy", "error", path, entry.lineno,
                               f"op {entry.op!r} is not one of {ops}"))
        skill = entry.fields.get(log_field)
        if not skill:
            out.append(Finding("writer-policy", "error", path, entry.lineno,
                               f"missing {log_field}= field"))
        elif skill not in writers["writers"]:
            out.append(Finding("writer-policy", "error", path, entry.lineno,
                               f"{log_field}={skill} is not a writer in writers.yaml"))
        digest = entry.fields.get("sha256")
        if digest is not None and not SHA256_HEX_RE.match(digest):
            out.append(Finding("writer-policy", "error", path, entry.lineno,
                               f"sha256={digest!r} is not a 64-hex digest"))
    return out


# --- rule 14: no-k-marker-outside-canon -------------------------------------------

def rule_no_k_marker(ctx: LintContext) -> list[Finding]:
    out: list[Finding] = []
    markers = wiki_schema.entities()["markers"]["forbidden_outside_canon"]
    for page in ctx.pages:
        for index, line in enumerate(code_free_lines(page.body), 1):
            if line.lstrip().startswith(">"):
                continue
            unquoted = GERMAN_QUOTE_RE.sub("", line)
            for marker in markers:
                if marker in unquoted:
                    out.append(Finding("no-k-marker-outside-canon", "error", ctx.page_path(page),
                                       ctx.body_line(page, index),
                                       f"{marker} emitted outside a blockquote or „…“ quotation; "
                                       f"research pages never mark canon"))
    return out


# --- rule 15: no-reverse-into-canon ---------------------------------------------

def rule_no_reverse_into_canon(ctx: LintContext) -> list[Finding]:
    out: list[Finding] = []
    prefixes = terminal_prefixes()
    edges_path = ctx.display(ctx.wiki_file(wiki_schema.conventions()["graph"]["wiki_relation_index"]))
    for record, lineno in zip(ctx.edges, ctx.edge_lines):
        src = record.get("from")
        if isinstance(src, str) and src.startswith(prefixes):
            out.append(Finding("no-reverse-into-canon", "error", edges_path, lineno,
                               f"edge from {src!r}: terminal targets never write back"))
    for page in ctx.pages:
        for name, slugs in ref_fields(page):
            for slug in slugs:
                if slug.startswith(prefixes):
                    out.append(Finding("no-reverse-into-canon", "error", ctx.page_path(page), 1,
                                       f"{name} lists {slug!r}: terminal targets are never reverse-linked"))
    return out


# --- rule 16: no-auto-canon-page --------------------------------------------------

def canon_identities(ctx: LintContext) -> tuple[dict[str, str], dict[str, str]]:
    """File stems and first ``# `` headings of the terminal directories."""
    stems: dict[str, str] = {}
    headings: dict[str, str] = {}
    for folder in wiki_schema.conventions()["ownership"]["terminal"]:
        root = ctx.repo_root / folder
        if not root.is_dir():
            continue
        for path in sorted(root.rglob("*.md")):
            stems.setdefault(path.stem, ctx.display(path))
            for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
                if line.startswith("# "):
                    headings.setdefault(line[2:].strip(), ctx.display(path))
                    break
    return stems, headings


def rule_no_auto_canon_page(ctx: LintContext) -> list[Finding]:
    out: list[Finding] = []
    stems, headings = canon_identities(ctx)
    for page in ctx.pages:
        path = ctx.page_path(page)
        if page.slug in stems:
            out.append(Finding("no-auto-canon-page", "error", path, 1,
                               f"slug {page.slug!r} mirrors {stems[page.slug]}; "
                               f"pages about Canon are concept pages with canon_ref"))
        title = page.title.strip()
        if title in headings:
            out.append(Finding("no-auto-canon-page", "error", path, 1,
                               f"title {title!r} equals the heading of {headings[title]}; "
                               f"pages about Canon are concept pages with canon_ref"))
    return out


# --- rule 17: index-sync ----------------------------------------------------------------

def rule_index_sync(ctx: LintContext) -> list[Finding]:
    # A wiki that does not exist has nothing to render: demanding its indexes
    # would make --health on an absent Wiki/ report errors for every view.
    if not ctx.wiki_root.is_dir():
        return []
    try:
        from . import wiki_views
    except ImportError as exc:
        return [Finding("index-sync", "info", ctx.display(ctx.wiki_root), None,
                        f"tools/kpwiki/wiki_views unavailable ({exc}); rule skipped")]
    out: list[Finding] = []
    try:
        expected_views = wiki_views.views(ctx.wiki_root, ctx.repo_root)
    except Exception as exc:
        return [Finding("index-sync", "warn", ctx.display(ctx.wiki_root), None,
                        f"could not render views: {exc}")]
    for name, expected in expected_views.items():
        target = ctx.wiki_root / name
        path = ctx.display(target)
        if not target.exists():
            out.append(Finding("index-sync", "error", path, None,
                               "rendered navigation is missing; run scripts/render_wiki_views.py"))
            continue
        if target.read_text(encoding="utf-8").rstrip() != str(expected).rstrip():
            out.append(Finding("index-sync", "error", path, None,
                               "differs from the rendered view; run scripts/render_wiki_views.py"))
    expected_readmes = {name for name in expected_views if name.endswith("/README.md")}
    managed_roots = [Path(wiki_schema.kind(kind)["dir"]).name for kind in wiki_schema.kinds()]
    managed_roots.append(wiki_pages.CANDIDATES_DIR)
    for root in managed_roots:
        folder = ctx.wiki_root / root
        if not folder.is_dir():
            continue
        for readme in folder.rglob("README.md"):
            rel = readme.relative_to(ctx.wiki_root).as_posix()
            if rel not in expected_readmes:
                out.append(Finding("index-sync", "error", ctx.display(readme), None,
                                   "stale rendered navigation; remove it and re-render"))
    return out


# --- rule 18: log-coverage ------------------------------------------------------------

def rule_log_coverage(ctx: LintContext) -> list[Finding]:
    out: list[Finding] = []
    for page in ctx.main_pages:
        covered = any(page.slug in e.title or e.title == page.title for e in ctx.log)
        if not covered:
            out.append(Finding("log-coverage", "warn", ctx.page_path(page), None,
                               f"no {wiki_schema.conventions()['log']['file']} entry names "
                               f"{page.slug!r} or {page.title!r}"))
    return out


# --- rule 19: candidate-age --------------------------------------------------------

def candidate_stamp(page: Page) -> dt.date:
    for name in CANDIDATE_STAMP_FIELDS:
        stamp = as_date(page.front.get(name))
        if stamp:
            return stamp
    return dt.date.fromtimestamp(page.path.stat().st_mtime)


def rule_candidate_age(ctx: LintContext) -> list[Finding]:
    out: list[Finding] = []
    max_days = int(wiki_schema.conventions()["batches"]["candidate_max_age_days"])
    today = dt.date.today()
    for page in ctx.candidates:
        age = (today - candidate_stamp(page)).days
        if age > max_days:
            out.append(Finding("candidate-age", "warn", ctx.page_path(page), None,
                               f"candidate is {age} days old (limit {max_days}); promote or drop it"))
    return out


# --- rule 20: no-page-body-in-graph -------------------------------------------------

def graph_values(graph_dir: Path) -> Iterator[tuple[Any, str]]:
    """``(node id, text)`` for every long string a Graph/ record carries."""
    for path in sorted((graph_dir / "nodes").glob("*.jsonl")):
        for record in kpgraph.read_jsonl(path):
            for key, value in record.items():
                if isinstance(value, str) and len(value) >= GRAPH_VALUE_MIN_CHARS:
                    yield record.get("_nid", record.get("id", key)), value


def rule_no_page_body_in_graph(ctx: LintContext) -> list[Finding]:
    page_shingles = [(p, shingles(p.body)) for p in ctx.main_pages]
    page_shingles = [(p, s) for p, s in page_shingles if s]
    if not page_shingles:
        return []
    db = ctx.repo_root / wiki_schema.conventions()["graph"]["provenance"]
    if not db.is_dir():
        return [Finding("no-page-body-in-graph", "info", ctx.display(db), None,
                        "provenance graph not present; rule skipped")]
    out: list[Finding] = []
    try:
        for node_id, value in graph_values(db):
            node_shingles = shingles(value)
            if not node_shingles:
                continue
            for page, own in page_shingles:
                overlap = len(node_shingles & own) / min(len(node_shingles), len(own))
                if overlap >= SHINGLE_OVERLAP_THRESHOLD:
                    out.append(Finding("no-page-body-in-graph", "error", ctx.page_path(page), None,
                                       f"body overlaps node {node_id} of {ctx.display(db)} "
                                       f"({overlap:.0%} shared {SHINGLE_WORDS}-word shingles); "
                                       f"page bodies never enter the provenance graph (D-W2)"))
    except (OSError, ValueError) as exc:
        return [Finding("no-page-body-in-graph", "info", ctx.display(db), None,
                        f"could not read the provenance graph ({exc}); rule skipped")]
    return out


# --- rule 21: cascade-risk ----------------------------------------------------------

def rule_cascade_risk(ctx: LintContext) -> list[Finding]:
    out: list[Finding] = []
    config = wiki_schema.edges()["cascade_risk"]
    over, minimum = set(config["over"]), int(config["min_dependents"])
    inbound = Counter(e.get("to") for e in ctx.edges if e.get("type") in over)
    contested = contested_state()
    for page in ctx.main_pages:
        count = inbound.get(page.slug, 0)
        if page.status == contested and count >= minimum:
            out.append(Finding("cascade-risk", "info", ctx.page_path(page), None,
                               f"{count} pages depend on this contested page via {sorted(over)} "
                               f"edges (threshold {minimum})"))
    return out


# --- fix plan: defaults + applying actions -------------------------------------------

def default_gaps(ctx: LintContext) -> list[FixAction]:
    """Schema defaults (``default`` / ``initial``) missing from a page's frontmatter."""
    actions: list[FixAction] = []
    for page in ctx.pages:
        if not known_kind(page):
            continue
        for name, spec in kind_fields(page.kind).items():
            if name in page.front:
                continue
            if "default" in spec:
                actions.append(FixAction(page, "set_default", name, spec["default"], "defaults"))
            elif "initial" in spec:
                actions.append(FixAction(page, "set_default", name, spec["initial"], "defaults"))
    return actions


def fix_plan(ctx: LintContext) -> list[FixAction]:
    return xref_gaps(ctx) + default_gaps(ctx)


def append_link_to_section(body: str, section: str, slug: str) -> str:
    """Append ``- [[slug]]`` to a level-2 section, creating the section at the end if absent."""
    line = f"- [[{slug}]]"
    matches = list(wiki_pages.HEADING_RE.finditer(body))
    for index, match in enumerate(matches):
        if len(match.group(1)) != 2 or match.group(2).strip() != section:
            continue
        end = len(body)
        for following in matches[index + 1:]:
            if len(following.group(1)) <= 2:
                end = following.start()
                break
        head, chunk, tail = body[:match.end()], body[match.end():end].rstrip(), body[end:]
        return f"{head}{chunk}\n{line}\n" + (f"\n{tail}" if tail else "")
    return body.rstrip("\n") + f"\n\n## {section}\n{line}\n"


def apply_action(front: dict[str, Any], body: str, action: FixAction) -> tuple[dict[str, Any], str]:
    if action.action == "append_slug":
        listed = front.get(action.target) or []
        values = list(listed) if isinstance(listed, list) else [listed]
        if action.value not in values:
            values.append(action.value)
        front[action.target] = values
    elif action.action in ("set_slug", "set_default"):
        front[action.target] = action.value
    elif action.action == "append_link":
        body = append_link_to_section(body, action.target, action.value)
    return front, body


def render_page(front: dict[str, Any], body: str) -> str:
    dumped = yaml.safe_dump(front, sort_keys=False, allow_unicode=True)
    return f"---\n{dumped}---\n{body}"


RULES: dict[str, Callable[[LintContext], list[Finding]]] = {
    "required-field": rule_required_field,
    "enum": rule_enum,
    "illegal-transition": rule_illegal_transition,
    "archived-link": rule_archived_link,
    "broken-link": rule_broken_link,
    "orphan": rule_orphan,
    "missing-entity": rule_missing_entity,
    "sparse-page": rule_sparse_page,
    "page-size": rule_page_size,
    "page-location": rule_page_location,
    "duplicate-slug": rule_duplicate_slug,
    "navigation-link": rule_navigation_link,
    "context-window": rule_context_window,
    "citation-resolves": rule_citation_resolves,
    "stale-source": rule_stale_source,
    "xref-symmetry": rule_xref_symmetry,
    "edge-evidence": rule_edge_evidence,
    "writer-policy": rule_writer_policy,
    "no-k-marker-outside-canon": rule_no_k_marker,
    "no-reverse-into-canon": rule_no_reverse_into_canon,
    "no-auto-canon-page": rule_no_auto_canon_page,
    "index-sync": rule_index_sync,
    "log-coverage": rule_log_coverage,
    "candidate-age": rule_candidate_age,
    "no-page-body-in-graph": rule_no_page_body_in_graph,
    "cascade-risk": rule_cascade_risk,
}
