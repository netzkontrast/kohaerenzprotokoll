"""The figure and world cards in `Manuscript/figuren/` and `Manuscript/welt/`: does every reference they make resolve,
and does a text lean on a world card that rests?

Taken from `netzkontrast/worldbuilder` (its per-kind schema and cross-reference check over entity frontmatter), with
its auto-fix left behind: worldbuilder writes the missing inverse link, and here a link is never inferred. This only
reads and names.

    python3 scripts/cards.py check          every card: kind matches its folder, `kanon:` ids are rows of kanon.md,
                                            `wiki:` names a page, every [[slug]] resolves, no `match` surface on two
                                            cards, a resting card names the decision it rests by
    python3 scripts/cards.py lint <file>…   every line of a text that names a resting world card — a query, never a
                                            failure: the text may mean the word, or bring the old world back
    python3 scripts/cards.py selftest

**Premises and resting cards (decision 033).** A world card of `kind: voraussetzung` is a premise of the world: the
author's decision makes it one (`kanon:` names that row). A card with `status: ruht` and `ruht_seit: <id>` no longer
holds: a later decision took away what it described. It is not deleted — its ideas stay readable — and the tools
read it as history: `brief.py` does not present it as decided, and `lint` names every line of a text that leans on
it. A surface that a holding card also claims (a premise's word, say) is the holding card's and is not named.

Exit 1 on any finding of `check`. A finding is a broken reference, never a judgement of the card's content.
"""

from __future__ import annotations

import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from wiki_index import frontmatter  # noqa: E402  the frontmatter boundary, one implementation

FOLDERS = {"figuren": ("figur",), "welt": ("welt", "voraussetzung")}
STATUSES = (None, "ruht")
WIKI_DIRS = ("candidates", "terms", "conflicts", "questions", "chapters")
LINK = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
WORD = lambda w: re.compile(r"(?<![\wÄÖÜäöüß])" + re.escape(w) + r"(?![\wÄÖÜäöüß])")  # noqa: E731


def wiki_slugs(wiki: Path) -> set[str]:
    return {p.stem for d in WIKI_DIRS for p in (wiki / d).glob("*.md")}


def kanon_ids(kanon: Path) -> set[str]:
    return {m.group(1).strip() for m in re.finditer(r"^\| ([^|]+?) \| \d{4}-\d{2}-\d{2} \|", kanon.read_text(encoding="utf-8"), re.M)}


def load(manuscript: Path | None = None) -> list[dict]:
    """Every card as {rel, folder, path, fm, text}; a file without frontmatter has fm {}."""
    manuscript = manuscript or ROOT / "Manuscript"
    out = []
    for folder in FOLDERS:
        for p in sorted((manuscript / folder).glob("*.md")):
            if p.name == "README.md":
                continue
            text = p.read_text(encoding="utf-8")
            out.append({"rel": f"{folder}/{p.name}", "folder": folder, "path": p, "fm": frontmatter(text) or {}, "text": text})
    return out


def rests(card: dict) -> bool:
    return card["fm"].get("status") == "ruht"


def premises(manuscript: Path | None = None) -> list[dict]:
    """The world's premises: holding cards of `kind: voraussetzung`."""
    return [c for c in load(manuscript) if c["fm"].get("kind") == "voraussetzung" and not rests(c)]


def check(manuscript: Path | None = None, wiki: Path | None = None, kanon: Path | None = None) -> list[str]:
    manuscript = manuscript or ROOT / "Manuscript"
    wiki = wiki or ROOT / "Wiki"
    ids = kanon_ids(kanon or manuscript / "kanon.md")
    slugs = wiki_slugs(wiki)
    out, surfaces = [], {}
    for c in load(manuscript):
        rel, fm, text = c["rel"], c["fm"], c["text"]
        if not fm:
            out.append(f"{rel}: no frontmatter")
            continue
        for key in ("name", "kind"):
            if not fm.get(key):
                out.append(f"{rel}: lacks {key}")
        if fm.get("kind") and fm["kind"] not in FOLDERS[c["folder"]]:
            out.append(f"{rel}: kind {fm['kind']!r} in {c['folder']}/ (expected {' or '.join(map(repr, FOLDERS[c['folder']]))})")
        for i in fm.get("kanon") or []:
            if i not in ids:
                out.append(f"{rel}: kanon {i!r} is no row of kanon.md")
        if fm.get("status") not in STATUSES:
            out.append(f"{rel}: status {fm.get('status')!r} (a card holds, or rests: status ruht)")
        if rests(c) and fm.get("ruht_seit") not in ids:
            out.append(f"{rel}: rests without the decision it rests by (ruht_seit {fm.get('ruht_seit')!r} is no row of kanon.md)")
        if fm.get("kind") == "voraussetzung" and not fm.get("kanon"):
            out.append(f"{rel}: a premise names the author's decision that makes it one (kanon:)")
        if fm.get("wiki") and fm["wiki"] not in slugs:
            out.append(f"{rel}: wiki {fm['wiki']!r} names no page")
        for n, line in enumerate(text.split("\n"), 1):
            for s in LINK.findall(line):
                if s.strip() not in slugs:
                    out.append(f"{rel}:L{n}: [[{s.strip()}]] points at no page")
        for m in [] if rests(c) else fm.get("match") or []:  # a resting card's surfaces compete with nothing
            surfaces.setdefault(m.lower(), []).append(rel)
    for m, cards in sorted(surfaces.items()):
        if len(cards) > 1:
            out.append(f"match {m!r} is on {len(cards)} cards: {', '.join(cards)} — brief.py would pick the first")
    return out


def lint(text: str, manuscript: Path | None = None) -> list[dict]:
    """Every line naming a surface of a resting world card that no holding card claims: {line, surface, card, since}."""
    cards = load(manuscript)
    held = {m.lower() for c in cards if not rests(c) for m in c["fm"].get("match") or []}
    watch = [(m, c) for c in cards if rests(c) and c["folder"] == "welt" for m in c["fm"].get("match") or [] if m.lower() not in held]
    out = []
    for n, line in enumerate(text.split("\n"), 1):
        for m, c in watch:
            if WORD(m).search(line):
                out.append({"line": n, "surface": m, "card": c["rel"], "since": c["fm"].get("ruht_seit")})
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
        (ms / "kanon.md").write_text("| id | Datum | Was | Wo |\n|---|---|---|---|\n| W10-A | 2026-10-05 | x | y |\n"
                                     "| 033 | 2026-10-28 | zwei Voraussetzungen | z |\n", encoding="utf-8")
        good = '---\nname: Juna\nkind: figur\nkanon: [W10-A]\nmatch: ["Juna"]\nwiki: juna\n---\n\nSiehe [[juna]].\n'
        (ms / "figuren" / "juna.md").write_text(good, encoding="utf-8")
        results.append(("a card whose references all resolve has no finding", check(ms, wk) == []))
        (ms / "figuren" / "x.md").write_text('---\nname: X\nkind: welt\nkanon: [W99]\nmatch: ["juna"]\nwiki: nope\n---\n\n[[fehlt|Text]]\n', encoding="utf-8")
        f = check(ms, wk)
        results.append(("a wrong kind, an unknown kanon id, a missing wiki page and a dead link are each named",
                        any("kind 'welt'" in x for x in f) and any("'W99'" in x for x in f)
                        and any("wiki 'nope'" in x for x in f) and any("x.md:L9: [[fehlt]]" in x for x in f)))
        results.append(("a match surface on two cards is named, case-insensitively", any("match 'juna' is on 2 cards" in x for x in f)))
        (ms / "figuren" / "x.md").unlink()
        (ms / "welt" / "y.md").write_text("kein Kopf\n", encoding="utf-8")
        results.append(("a card without frontmatter is named, not skipped", any("welt/y.md: no frontmatter" in x for x in check(ms, wk))))
        (ms / "welt" / "y.md").unlink()
        (ms / "welt" / "dkt.md").write_text('---\nname: DKT\nkind: voraussetzung\nkanon: ["033"]\nmatch: ["Landauer", "Kollaps-Kernel"]\n---\n', encoding="utf-8")
        (ms / "welt" / "stadt.md").write_text('---\nname: Stadt\nkind: welt\nkanon: []\nstatus: ruht\nruht_seit: "033"\n'
                                              'match: ["Konstrukt-Stadt", "Landauer", "Kernwelt"]\n---\n', encoding="utf-8")
        results.append(("a premise and a card resting by a decision are well formed; a resting card's surface competes with nothing",
                        check(ms, wk) == []))
        (ms / "welt" / "alt.md").write_text('---\nname: Alt\nkind: welt\nstatus: ruht\nmatch: ["Grauzone"]\n---\n', encoding="utf-8")
        (ms / "welt" / "nackt.md").write_text('---\nname: Nackt\nkind: voraussetzung\nmatch: ["Nichts"]\n---\n', encoding="utf-8")
        (ms / "welt" / "halb.md").write_text('---\nname: Halb\nkind: welt\nstatus: halb\nmatch: ["Halb"]\n---\n', encoding="utf-8")
        f = check(ms, wk)
        results.append(("a card resting by no decision, a premise without its decision and an unknown status are each named",
                        any("alt.md: rests without the decision" in x for x in f) and any("nackt.md: a premise names" in x for x in f)
                        and any("halb.md: status 'halb'" in x for x in f)))
        results.append(("the premises are the holding cards of kind voraussetzung", [c["rel"] for c in premises(ms)] == ["welt/dkt.md", "welt/nackt.md"]))
        hits = lint("Kapitel 1.\nDie Konstrukt-Stadt schläft.\nLandauer zahlt die Wärme.\nKernwelten, Kernwelt.\nGrauzonen", ms)
        results.append(("lint names each line that leans on a resting world card, not a word a premise also claims, not inside a longer word",
                        [(h["line"], h["surface"]) for h in hits] == [(2, "Konstrukt-Stadt"), (4, "Kernwelt")]
                        and hits[0]["since"] == "033"))
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
    if argv and argv[0] == "lint" and len(argv) > 1:
        total = 0
        for name in argv[1:]:
            p = Path(name)
            for h in lint(p.read_text(encoding="utf-8")):
                print(f"query {name}:L{h['line']}  „{h['surface']}“ — {h['card']} ruht seit {h['since']}: gemeint, oder kommt die alte Welt zurück?")
                total += 1
        print(f"{total} line(s) name a resting world card")
        return 0
    print(__doc__)
    return 0 if argv and argv[0] in ("-h", "--help") else 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
