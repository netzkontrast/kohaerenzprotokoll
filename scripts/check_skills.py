"""Validate the project's skills against the agent-skills spec, and against each other.

`dspy_skills.SkillManager` builds the `<available_skills>` block a ReAct agent
is given from the `description` field and nothing else, and Claude Code does
the same. So a skill whose frontmatter is malformed, over-long or misnamed is
not a skill with a typo — it is a skill no agent will ever choose, and nothing
says so. This is the check that says so.

Ported from `netzkontrast/dspy-agent-skills` `tests/test_skill_metadata.py`
(the rules), rewritten standard-library because every check here is decidable
and none needs pytest.

Two rules are this project's own:

- **One encoding per skill (P6).** A project skill lives in `.agents/skills/`
  and `.claude/skills/<name>` is a symlink to it. A real folder with the same
  name is a second copy, and two copies drift on the first edit.
- **Vendored skills are checked, never rewritten.** Four collections are copied
  unchanged from upstream, each pinned in `CLAUDE.md`: the `jev*` folders from
  `wuyoscar/jev-skill` v0.2.0; the four Notion skills from
  `netzkontrast/notion-skills`; `knowledge-graph-extract`; `graphify`; and the
  `hyper-extract` / `hyperextract-*` folders from `netzkontrast/Hyper-Extract`.
  Their findings are reported under their own heading and do not fail the run:
  fixing them here would make them no longer the vendored thing.

    python3 scripts/check_skills.py            # exit 1 on a project-skill defect
    python3 scripts/check_skills.py --json
    python3 scripts/check_skills.py --selftest
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / ".agents" / "skills"
CLAUDE = ROOT / ".claude" / "skills"
VENDORED = re.compile(r"^(jev(-|$)|knowledge-capture$|meeting-intelligence$|research-documentation$|"
                      r"spec-to-implementation$|knowledge-graph-extract$|graphify$|hyper-?extract(-|$))")

SUPPORTED = {"name", "description", "when_to_use", "argument-hint",
             "disable-model-invocation", "user-invocable", "allowed-tools", "model",
             "effort", "context", "agent", "hooks", "paths", "shell",
             # the spec's own optional fields, used by the vendored skills
             "license", "metadata", "compatibility"}
FORBIDDEN = {"triggers", "version", "dspy-compatibility", "dspy-version"}
NAME = re.compile(r"^[a-z][a-z0-9-]{0,63}$")
LIMIT = 1536
KEY = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*)\s*:\s*(.*)$")


def frontmatter(text: str) -> dict[str, str] | str:
    """The top-level keys of a SKILL.md frontmatter, or why there are none."""
    if not text.startswith("---\n"):
        return "does not start with a '---' frontmatter block"
    end = text.find("\n---", 4)
    if end == -1:
        return "frontmatter is never closed"
    out: dict[str, str] = {}
    key = None
    for line in text[4:end].splitlines():
        match = KEY.match(line)
        if match and not line.startswith((" ", "\t")):
            key = match.group(1)
            out[key] = match.group(2).strip()
        elif key is not None:
            out[key] = (out[key] + " " + line.strip()).strip()
    return out


def check(folder: Path) -> list[str]:
    """Every defect in one skill folder, each naming what is wrong."""
    problems = []
    files = [p.name for p in folder.iterdir() if p.is_file()]
    if "SKILL.md" not in files:
        wrong = [f for f in files if f.lower() == "skill.md"]
        return [f"no SKILL.md{f' (found {wrong[0]!r} — the case is enforced)' if wrong else ''}"]
    meta = frontmatter((folder / "SKILL.md").read_text(encoding="utf-8"))
    if isinstance(meta, str):
        return [meta]
    name = meta.get("name", "").strip("\"'")
    if not name:
        problems.append("no name")
    elif not NAME.match(name):
        problems.append(f"name {name!r} is not kebab-case of at most 64 characters")
    elif name != folder.name:
        problems.append(f"name {name!r} is not the folder name {folder.name!r}")
    description = meta.get("description", "")
    if not description:
        problems.append("no description — no agent can choose this skill")
    size = len(description) + len(meta.get("when_to_use", ""))
    if size > LIMIT:
        problems.append(f"description + when_to_use is {size} characters, limit {LIMIT}")
    for field in sorted(set(meta) & FORBIDDEN):
        problems.append(f"forbidden field {field!r} — ignored by the harness")
    for field in sorted(set(meta) - SUPPORTED - FORBIDDEN):
        problems.append(f"unknown field {field!r}")
    return problems


def links() -> list[str]:
    """P6: each project skill is reachable from .claude/skills as a symlink, once."""
    problems = []
    for folder in sorted(PROJECT.iterdir()):
        if not folder.is_dir():
            continue
        mirror = CLAUDE / folder.name
        if not mirror.exists() and not mirror.is_symlink():
            problems.append(f"{folder.name}: no .claude/skills/{folder.name} — Claude Code cannot see it")
        elif not mirror.is_symlink():
            problems.append(f"{folder.name}: .claude/skills/{folder.name} is a copy, not a symlink")
        elif mirror.resolve() != folder.resolve():
            problems.append(f"{folder.name}: .claude/skills/{folder.name} points at {mirror.resolve()}")
    return problems


def run() -> dict:
    project = {f.name: check(f) for f in sorted(PROJECT.iterdir()) if f.is_dir()}
    vendored = {f.name: check(f) for f in sorted(CLAUDE.iterdir())
                if f.is_dir() and not f.is_symlink() and VENDORED.match(f.name)}
    stray = sorted(f.name for f in CLAUDE.iterdir()
                   if f.is_dir() and not f.is_symlink() and not VENDORED.match(f.name))
    return {"project": project, "vendored": vendored, "links": links(),
            "stray": [f"{s}: a real folder in .claude/skills that is neither vendored "
                      f"nor a link into .agents/skills" for s in stray]}


def selftest() -> list[str]:
    """Each rule fails on a skill built to break it."""
    import tempfile
    cases = {
        "lower": ("skill.md", "---\nname: lower\ndescription: x\n---\n", "case is enforced"),
        "misnamed": ("SKILL.md", "---\nname: other\ndescription: x\n---\n", "not the folder name"),
        "nodesc": ("SKILL.md", "---\nname: nodesc\n---\n", "no description"),
        "long": ("SKILL.md", "---\nname: long\ndescription: " + "x" * 1600 + "\n---\n", "limit"),
        "legacy": ("SKILL.md", "---\nname: legacy\ndescription: x\nversion: 1\n---\n", "forbidden"),
        "good": ("SKILL.md", "---\nname: good\ndescription: x\n---\n", None),
    }
    failures = []
    with tempfile.TemporaryDirectory() as tmp:
        for name, (filename, body, needle) in cases.items():
            folder = Path(tmp) / name
            folder.mkdir()
            (folder / filename).write_text(body, encoding="utf-8")
            problems = check(folder)
            if needle is None and problems:
                failures.append(f"{name}: clean skill reported {problems}")
            elif needle and not any(needle in p for p in problems):
                failures.append(f"{name}: expected a problem naming {needle!r}, got {problems}")
    return failures


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        problems = selftest()
        for p in problems:
            print(f"  FAIL  {p}")
        print(f"check_skills: {6 - len(problems)} of 6 cases hold")
        return 1 if problems else 0
    result = run()
    if "--json" in argv:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        for heading, key in (("project skills", "project"), ("vendored — reported, not failed", "vendored")):
            rows = result[key]
            bad = {k: v for k, v in rows.items() if v}
            print(f"{heading}: {len(rows) - len(bad)} of {len(rows)} clean")
            for skill, problems in bad.items():
                for p in problems:
                    print(f"  {skill}: {p}")
        for p in result["links"] + result["stray"]:
            print(f"  {p}")
    failed = any(result["project"].values()) or result["links"] or result["stray"]
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
