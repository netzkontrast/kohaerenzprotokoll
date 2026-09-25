"""Which markdown in this repository qmd can find, and which it cannot.

qmd indexes directories as named collections. A file in a directory no collection
covers is simply absent from every search, and **nothing says so** — the search
just returns fewer results and looks like it worked. A new directory is the risk:
`Wiki/questions/` happened to fall inside the existing `wiki` collection, but the
next one may not.

So coverage is checked rather than remembered.

## The known exclusions, stated rather than discovered

| path | why |
|---|---|
| `Legacy/` | a shelf, read by nothing. Indexing it would put the retired pipeline into every search for the live one — the exact thing decision 001 removed |
| `.lit-critic-src/`, `.venv*/`, `.tools-node/`, `node_modules/` | vendored clones and dependencies, git-ignored |
| `.agents/skills/`, `.claude/skills/`, `scripts/` | agent instructions and implementation notes, read from their paths when working on code; qmd searches the novel corpus and its process records |
| the four root files | `CLAUDE.md`, `NOW.md`, `PRINCIPLES.md`, `README.md`. **qmd's `--pattern` flag is ignored and every collection is `**/*.md`**, so a collection rooted at `.` pulls in Legacy and the vendored clones — 1,382 files. Tried, measured, removed. These four are loaded by an agent directly anyway; the loss is that a search cannot find them |
| `Sources/README.md` | the same shape one level down: the collections are `Sources/drive`, `Sources/notes` and `Sources/terms`, so a file at `Sources/` itself falls between them, and a collection rooted at `Sources/` would index all three twice |

Anything else uncovered is a gap and this prints it.

Usage:
    python3 scripts/qmd_coverage.py          # what is covered, what is not
    python3 scripts/qmd_coverage.py --paths  # the uncovered files themselves
"""

from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / ".qmd" / "index.yml"

SKIP = ("Legacy/", ".lit-critic-src/", ".venv", ".tools-node/", "node_modules/",
        ".qmd/", ".git/", ".cache/",
        ".agents/skills/", ".claude/skills/", "scripts/",
        # vendored: wuyoscar/jev-skill v0.2.0, third-party skill text, not corpus
        ".claude/skills/jev")
# Stated above, with the measurement that produced the decision.
KNOWN = {"CLAUDE.md", "NOW.md", "PRINCIPLES.md", "README.md", "Sources/README.md"}


def collections(config: Path = CONFIG) -> list[tuple[str, Path, list[str]]]:
    """Read the committed qmd collection paths and comma-separated glob patterns.

    This deliberately accepts only the simple mapping shape used by index.yml;
    an unrecognised collection fails closed instead of claiming full coverage.
    """
    result = []
    inside = False
    name = None
    fields: dict[str, str] = {}

    def finish():
        if name is not None:
            if not fields.get("path") or not fields.get("pattern"):
                raise ValueError(f"qmd collection {name!r} needs path and pattern")
            path = config.parent.parent / fields["path"]
            patterns = [p.strip() for p in fields["pattern"].split(",") if p.strip()]
            if not patterns:
                raise ValueError(f"qmd collection {name!r} has no patterns")
            result.append((name, path.resolve(), patterns))

    for line in config.read_text(encoding="utf-8").splitlines():
        if line == "collections:":
            inside = True
            continue
        if not inside or not line.strip() or line.lstrip().startswith("#"):
            continue
        if line and not line.startswith(" "):
            break
        if line.startswith("  ") and not line.startswith("    ") and line.strip().endswith(":"):
            finish()
            name, fields = line.strip()[:-1], {}
        elif name is not None and line.startswith("    ") and not line.startswith("      "):
            key, sep, value = line.strip().partition(":")
            if sep and key in {"path", "pattern"}:
                fields[key] = value.strip().strip('"\'')
    finish()
    if not result:
        raise ValueError(f"no qmd collections in {config}")
    return result


def repo_markdown(root: Path = ROOT) -> list[Path]:
    return [p for p in root.rglob("*.md")
            if not any(p.relative_to(root).as_posix().startswith(part) for part in SKIP)]


def coverage(root: Path = ROOT, config: Path = CONFIG) -> tuple[list[Path], list[Path], list[Path]]:
    files = repo_markdown(root)
    matched: set[Path] = set()
    for _, path, patterns in collections(config):
        for pattern in patterns:
            matched.update(p.resolve() for p in path.glob(pattern) if p.is_file())
    uncovered = [p for p in files if p.resolve() not in matched]
    surprising = [p for p in uncovered if p.relative_to(root).as_posix() not in KNOWN]
    return files, uncovered, surprising


def selftest() -> int:
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / ".qmd").mkdir()
        (root / "Wiki" / "questions").mkdir(parents=True)
        (root / "NewCorpus").mkdir()
        for name in ("Wiki/questions/answer.md", "NewCorpus/unindexed.md", "NOW.md"):
            (root / name).write_text("test", encoding="utf-8")
        config = root / ".qmd" / "index.yml"
        config.write_text('collections:\n  decisions:\n    path: .\n'
                          '    pattern: "Wiki/questions/**/*.md,Plan/decisions/**/*.md"\n', encoding="utf-8")
        _, uncovered, surprising = coverage(root, config)
        if {p.relative_to(root).as_posix() for p in surprising} != {"NewCorpus/unindexed.md"}:
            print(f"FAIL qmd pattern did not isolate the gap: {surprising}")
            return 1
        if len(uncovered) != 2:
            print(f"FAIL qmd known exclusion missing: {uncovered}")
            return 1
        config.write_text('collections:\n  all:\n    path: .\n'
                          '    pattern: "Wiki/**/*.md,NewCorpus/**/*.md,*.md"\n', encoding="utf-8")
        if coverage(root, config)[2]:
            print("FAIL qmd expanded pattern did not close the gap")
            return 1
    print("qmd coverage: constrained and expanded patterns hold")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--paths", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    if args.selftest:
        return selftest()

    configured = collections()
    files, uncovered, surprising = coverage()

    print(f"{len(files)} markdown files in the qmd coverage scope")
    print(f"{len(configured)} collections cover {len(files) - len(uncovered)} of them\n")
    for name, root, patterns in configured:
        try:
            print(f"  {name}: {root.relative_to(ROOT)} ({', '.join(patterns)})")
        except ValueError:
            print(f"  {name}: {root} ({', '.join(patterns)})")
    print(f"\n{len(uncovered)} uncovered, {len(surprising)} of them unexplained")
    if args.paths or surprising:
        for path in sorted(uncovered):
            name = path.relative_to(ROOT).as_posix()
            mark = "known" if name in KNOWN else "GAP  "
            print(f"  {mark}  {name}")
    if surprising:
        print("\nA GAP is a file no collection pattern covers. Add one:")
        print("  qmd collection add <dir> --name <name>")
        print("  qmd context add qmd://<name>/ \"what this holds\"")
    return 1 if surprising else 0


if __name__ == "__main__":
    raise SystemExit(main())
