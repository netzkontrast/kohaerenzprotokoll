"""The figure and world cards in `Manuscript/figuren/` and `Manuscript/welt/`: does every reference they make resolve?

Taken from `netzkontrast/worldbuilder` (its per-kind schema and cross-reference check over entity frontmatter), with
its auto-fix left behind: worldbuilder writes the missing inverse link, and here a link is never inferred. This only
reads and names.

    python3 scripts/cards.py check      every card: kind matches its folder, `kanon:` ids are rows of kanon.md,
                                        `wiki:` names a page, every [[slug]] resolves, no `match` surface on two cards
    python3 scripts/cards.py selftest

Exit 1 on any finding. A finding is a broken reference, never a judgement of the card's content.
"""

from __future__ import annotations

import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from wiki_index import frontmatter  # noqa: E402  the frontmatter boundary, one implementation

FOLDERS = {"figuren": "figur", "welt": "welt"}
WIKI_DIRS = ("candidates", "terms", "conflicts", "questions", "chapters")
LINK = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")


def wiki_slugs(wiki: Path) -> set[str]:
    return {p.stem for d in WIKI_DIRS for p in (wiki / d).glob("*.md")}


def kanon_ids(kanon: Path) -> set[str]:
    return {m.group(1).strip() for m in re.finditer(r"^\| ([^|]+?) \| \d{4}-\d{2}-\d{2} \|", kanon.read_text(encoding="utf-8"), re.M)}


def check(manuscript: Path | None = None, wiki: Path | None = None, kanon: Path | None = None) -> list[str]:
    manuscript = manuscript or ROOT / "Manuscript"
    wiki = wiki or ROOT / "Wiki"
    ids = kanon_ids(kanon or manuscript / "kanon.md")
    slugs = wiki_slugs(wiki)
    out, surfaces = [], {}
    for folder, kind in FOLDERS.items():
        for p in sorted((manuscript / folder).glob("*.md")):
            if p.name == "README.md":
                continue
            rel = f"{folder}/{p.name}"
            text = p.read_text(encoding="utf-8")
            fm = frontmatter(text)
            if not fm:
                out.append(f"{rel}: no frontmatter")
                continue
            for key in ("name", "kind"):
                if not fm.get(key):
                    out.append(f"{rel}: lacks {key}")
            if fm.get("kind") and fm["kind"] != kind:
                out.append(f"{rel}: kind {fm['kind']!r} in {folder}/ (expected {kind!r})")
            for i in fm.get("kanon") or []:
                if i not in ids:
                    out.append(f"{rel}: kanon {i!r} is no row of kanon.md")
            if fm.get("wiki") and fm["wiki"] not in slugs:
                out.append(f"{rel}: wiki {fm['wiki']!r} names no page")
            for n, line in enumerate(text.split("\n"), 1):
                for s in LINK.findall(line):
                    if s.strip() not in slugs:
                        out.append(f"{rel}:L{n}: [[{s.strip()}]] points at no page")
            for m in fm.get("match") or []:
                surfaces.setdefault(m.lower(), []).append(rel)
    for m, cards in sorted(surfaces.items()):
        if len(cards) > 1:
            out.append(f"match {m!r} is on {len(cards)} cards: {', '.join(cards)} — brief.py would pick the first")
    return out


def selftest() -> int:
    results = []
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        ms, wk = base / "Manuscript", base / "Wiki"
        for d in ("figuren", "welt"):
            (ms / d).mkdir(parents=True)
        (wk / "candidates").mkdir(parents=True)
        (wk / "candidates" / "juna.md").write_text("---\n---\n", encoding="utf-8")
        (ms / "kanon.md").write_text("| id | Datum | Was | Wo |\n|---|---|---|---|\n| W10-A | 2026-10-05 | x | y |\n", encoding="utf-8")
        good = '---\nname: Juna\nkind: figur\nkanon: [W10-A]\nmatch: ["Juna"]\nwiki: juna\n---\n\nSiehe [[juna]].\n'
        (ms / "figuren" / "juna.md").write_text(good, encoding="utf-8")
        results.append(("a card whose references all resolve has no finding", check(ms, wk) == []))
        (ms / "figuren" / "x.md").write_text('---\nname: X\nkind: welt\nkanon: [W99]\nmatch: ["juna"]\nwiki: nope\n---\n\n[[fehlt|Text]]\n', encoding="utf-8")
        f = check(ms, wk)
        results.append(("a wrong kind, an unknown kanon id, a missing wiki page and a dead link are each named",
                        any("kind 'welt'" in x for x in f) and any("'W99'" in x for x in f)
                        and any("wiki 'nope'" in x for x in f) and any("x.md:L9: [[fehlt]]" in x for x in f)))
        results.append(("a match surface on two cards is named, case-insensitively", any("match 'juna' is on 2 cards" in x for x in f)))
        (ms / "welt" / "y.md").write_text("kein Kopf\n", encoding="utf-8")
        results.append(("a card without frontmatter is named, not skipped", any("welt/y.md: no frontmatter" in x for x in check(ms, wk))))
    for name, ok in results:
        print(f"{'held' if ok else 'FAILED':7} {name}")
    held = sum(ok for _, ok in results)
    print(f"{held} of {len(results)} held")
    return 0 if held == len(results) else 1


def main(argv: list[str]) -> int:
    if argv and argv[0] == "selftest":
        return selftest()
    if argv and argv[0] == "check":
        f = check()
        for x in f:
            print(x)
        print(f"{len(f)} finding(s) over the cards in Manuscript/figuren and Manuscript/welt")
        return 1 if f else 0
    print(__doc__)
    return 0 if argv and argv[0] in ("-h", "--help") else 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
