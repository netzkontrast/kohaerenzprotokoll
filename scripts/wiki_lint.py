#!/usr/bin/env python3
"""Deterministic lint for the research wiki (``Wiki/``) — free, zero LLM calls.

Runs the 21 rules of ``tools/kpwiki/wiki_lint_rules.py`` (concept §4 F,
integration plan §3): required fields, enums, lifecycle transitions, links,
citations, cross-reference symmetry, edge evidence, writer policy, the
``[K]`` marker fence, terminal-target discipline, rendered-view sync, log
coverage, candidate age, page bodies leaking into the provenance graph and
cascade risk. Every enum, required field, transition, edge type, xref rule,
log op and writer comes from ``Wiki/schema/*.yaml`` via ``wiki_schema``.

    python3 scripts/wiki_lint.py                    # all rules, all pages
    python3 scripts/wiki_lint.py --health           # summary + coverage numbers
    python3 scripts/wiki_lint.py --json             # findings + summary as JSON
    python3 scripts/wiki_lint.py --fix [--dry-run]  # reverse links, defaults, coverage.json
    python3 scripts/wiki_lint.py --suggest          # fix plan + non-automatable hints
    python3 scripts/wiki_lint.py --hook FILE        # one file, warn-only, exit 0
    python3 scripts/wiki_lint.py --rules enum,orphan --wiki-root DIR --repo-root DIR

Output lines read ``<severity> <rule> <path>[:<line>] — <message>``, sorted by
severity then path, followed by ``N errors, N warnings, N info``. Exit status
is 1 when any ``error`` was found (0 in ``--hook`` mode, which the PostToolUse
hook relies on). An empty or missing wiki lints clean.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from tools.kpwiki import wiki_lint_rules as rules  # noqa: E402
from tools.kpwiki import wiki_schema  # noqa: E402
from tools.kpwiki.wiki_lint_rules import Finding, FixAction, LintContext  # noqa: E402

# Rules a freshly written candidate must already satisfy; the rest apply at promotion.
CANDIDATE_HOOK_RULES = ("required-field", "enum", "citation-resolves", "no-k-marker-outside-canon")
SEVERITY_ORDER = {name: index for index, name in enumerate(rules.SEVERITIES)}


# --- running rules ------------------------------------------------------------------

def run_rules(ctx: LintContext, selected: list[str] | None = None) -> list[Finding]:
    findings: list[Finding] = []
    for rule_id, rule in rules.RULES.items():
        if selected is None or rule_id in selected:
            findings.extend(rule(ctx))
    return sort_findings(findings)


def sort_findings(findings: list[Finding]) -> list[Finding]:
    return sorted(findings, key=lambda f: (SEVERITY_ORDER.get(f.severity, len(SEVERITY_ORDER)),
                                           f.path, f.line or 0, f.rule, f.message))


def summary(findings: list[Finding]) -> dict[str, int]:
    counts = Counter(f.severity for f in findings)
    return {"errors": counts.get("error", 0), "warnings": counts.get("warn", 0),
            "info": counts.get("info", 0)}


def summary_line(findings: list[Finding]) -> str:
    counts = summary(findings)
    return f"{counts['errors']} errors, {counts['warnings']} warnings, {counts['info']} info"


def parse_rule_selection(value: str | None) -> list[str] | None:
    if not value:
        return None
    selected = [name.strip() for name in value.split(",") if name.strip()]
    unknown = [name for name in selected if name not in rules.RULES]
    if unknown:
        raise SystemExit(f"unknown rules: {', '.join(unknown)}; known: {', '.join(rules.RULES)}")
    return selected


# --- health -----------------------------------------------------------------------------------

def counts_by(pages, key: str) -> str:
    counter = Counter(str(p.front.get(key)) for p in pages if p.front.get(key) is not None)
    return " ".join(f"{name}={count}" for name, count in sorted(counter.items())) or "none"


def health_lines(ctx: LintContext) -> list[str]:
    promoted = ctx.main_pages
    open_state = rules.open_question_state()
    open_questions = [p for p in promoted if p.kind == "question" and p.status == open_state]
    contested = [p for p in promoted if p.status == rules.contested_state()]
    sources = [p for p in promoted if p.kind in rules.sha256_kinds()]
    manifest = f"{ctx.manifest_total}" if ctx.manifest_total else "no manifest"
    return [
        f"pages by kind: {counts_by(promoted, 'kind') if promoted else 'none'}",
        f"pages by status: {counts_by(promoted, 'status')}",
        f"candidates: {len(ctx.candidates)}",
        f"open questions by axis: {counts_by(open_questions, 'axis')}",
        f"contested pages: {len(contested)}" + (f" ({', '.join(p.slug for p in contested)})" if contested else ""),
        f"sources ingested: {len(sources)} / manifest {manifest}",
        f"edges: {len(ctx.edges)}",
    ]


# --- fix / suggest ------------------------------------------------------------------------

def apply_fixes(ctx: LintContext, actions: list[FixAction]) -> list[str]:
    """Write every action grouped per page; returns the paths written."""
    grouped: dict[str, list[FixAction]] = {}
    for action in actions:
        grouped.setdefault(action.page.rel, []).append(action)
    written = []
    for _, page_actions in sorted(grouped.items()):
        page = page_actions[0].page
        front, body = dict(page.front), page.body
        for action in page_actions:
            front, body = rules.apply_action(front, body, action)
        page.path.write_text(rules.render_page(front, body), encoding="utf-8")
        written.append(ctx.page_path(page))
    return written


def write_coverage(ctx: LintContext, dry_run: bool) -> str | None:
    """``Wiki/graph/coverage.json`` via ``wiki_views.coverage`` when that function exists."""
    try:
        from tools.kpwiki import wiki_views
    except ImportError:
        return None
    if not hasattr(wiki_views, "coverage"):
        return None
    target = ctx.wiki_root / rules.COVERAGE_REL
    if dry_run:
        return f"would write {ctx.display(target)}"
    data = wiki_views.coverage(ctx.pages, ctx.edges, ctx.repo_root / rules.MANIFEST_REL)
    if hasattr(wiki_views, "render_coverage"):
        text = wiki_views.render_coverage(data)
    else:
        text = json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    return f"wrote {ctx.display(target)}"


def run_fix(ctx: LintContext, dry_run: bool) -> None:
    actions = rules.fix_plan(ctx)
    verb = "would" if dry_run else "will"
    for action in actions:
        print(f"fix: {verb} {action.describe(ctx.page_path(action.page))}")
    if not dry_run and actions:
        for path in apply_fixes(ctx, actions):
            print(f"fix: wrote {path}")
    note = write_coverage(ctx, dry_run)
    if note:
        print(f"fix: {note}")
    if not actions:
        print("fix: nothing to complete")


def mentions_in_plain_text(ctx: LintContext, slug: str) -> list[str]:
    hits = []
    for page in ctx.pages:
        if page.slug != slug and slug in rules.wiki_pages.strip_code(page.body):
            hits.append(ctx.page_path(page))
    return hits


def suggestions(ctx: LintContext, findings: list[Finding]) -> list[str]:
    lines = [f"would {a.describe(ctx.page_path(a.page))}" for a in rules.fix_plan(ctx)]
    for finding in findings:
        if finding.rule == "orphan":
            slug = Path(finding.path).stem
            hits = mentions_in_plain_text(ctx, slug)
            where = ", ".join(hits) if hits else "no page mentions it in plain text"
            lines.append(f"orphan {finding.path}: link [[{slug}]] from {where}")
        elif finding.rule == "missing-entity":
            lines.append(f"missing entity: {finding.message}; create the concept page with that codex_ref")
    return lines


# --- hook -------------------------------------------------------------------------------------

def hook_findings(ctx: LintContext, target: Path) -> list[Finding]:
    """Findings for one file; candidates get the write-time subset of rules."""
    try:
        rel = target.resolve().relative_to(ctx.wiki_root.resolve()).as_posix()
    except ValueError:
        return []
    selected = list(CANDIDATE_HOOK_RULES) if rel.startswith(rules.wiki_pages.CANDIDATES_DIR + "/") else None
    display = ctx.display(target)
    return [f for f in run_rules(ctx, selected) if f.path == display]


# --- entry point -----------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--wiki-root", type=Path, help="wiki directory (default: <repo-root>/Wiki)")
    ap.add_argument("--repo-root", type=Path, default=ROOT,
                    help="where Sources/, Canon/, Codex/ and Graph/ live")
    ap.add_argument("--health", action="store_true", help="summary plus coverage numbers")
    ap.add_argument("--json", action="store_true", help="findings and summary as JSON")
    ap.add_argument("--fix", action="store_true", help="complete reverse links, defaults, coverage.json")
    ap.add_argument("--dry-run", action="store_true", help="with --fix: print the plan, write nothing")
    ap.add_argument("--suggest", action="store_true", help="fix plan plus non-automatable suggestions")
    ap.add_argument("--hook", type=Path, metavar="FILE", help="lint one file, warn-only, exit 0")
    ap.add_argument("--rules", help="comma-separated rule ids to run (default: all)")
    return ap


def print_findings(findings: list[Finding]) -> None:
    for finding in findings:
        print(finding.render())
    print(summary_line(findings))


def main(argv: list[str] | None = None) -> int:
    ns = build_parser().parse_args(argv)
    repo_root = ns.repo_root.resolve()
    wiki_root = (ns.wiki_root or repo_root / "Wiki").resolve()
    selected = parse_rule_selection(ns.rules)
    ctx = rules.build_context(wiki_root, repo_root)

    if ns.hook:
        # Silent when clean: the PostToolUse hook only shows a block when there is output.
        found = hook_findings(ctx, ns.hook)
        if found:
            print_findings(found)
        return 0
    if ns.fix:
        run_fix(ctx, ns.dry_run)
        if ns.dry_run:
            return 0
        ctx = rules.build_context(wiki_root, repo_root)

    findings = run_rules(ctx, selected)
    if ns.json:
        print(json.dumps({"findings": [vars(f) for f in findings], "summary": summary(findings)},
                         ensure_ascii=False, indent=1))
    elif ns.health:
        print(summary_line(findings))
        for line in health_lines(ctx):
            print(line)
    else:
        print_findings(findings)
        if ns.suggest:
            print("\nSuggestions:")
            for line in suggestions(ctx, findings) or ["nothing to suggest"]:
                print(f"- {line}")
    return 1 if any(f.severity == "error" for f in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
