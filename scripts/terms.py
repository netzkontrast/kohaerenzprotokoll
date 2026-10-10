"""Term pages: the author's workbench page for one term, written from a reviewed candidate page.

A candidate page (`Wiki/candidates/<slug>.md`) is the research ledger: every source's
reading, attributed and unmerged, in English work prose. A **term page**
(`Wiki/terms/<slug>.md`) is what the author works with: German, short, every point
tagged with its status (`GOAL.md` §1.2) and its evidence, and it says separately
what the project has decided and what the sources only say. It exists only for a
candidate the author reviewed (decision 026), and it names the reviewed state it was
written from. `Plan/concept/wiki-terms_2026-10-08.md` has the reasons; the first
instance, `kishotenketsu`, was written by hand before this script (P3).

    kind: term page          # provisional — one instance, written by hand 2026-10-08
                             # may not: decide a reading, enter canon, stand in for the candidate page
                             # retire when: five term pages exist and the author has used none of them

**The shape**, as the first page has it: frontmatter `term`, `status` (`draft` |
`approved`), `kind`, `candidate`, `candidate_hash`, `written`, `by`; then the
sections of `SECTIONS`, in order. Every line of a section is a bullet opening with a
tag, or a line continuing one:

| tag | means | must carry |
|---|---|---|
| `[K]` | the author decided it | a link to `Plan/decisions/`, an answered sheet in `Plan/weichen/`, `Manuscript/kanon.md` or a decided `Wiki/conflicts/` record |
| `[V]` | a proposal | a source citation `^[slug.md:Lnn]` or a link into `Plan/` |
| `[S]` | a source says it — research, never canon (decision 006) | a source citation `^[slug.md:Lnn]` |
| `[L]` | a gap: nothing settles it | nothing |
| `[D]` | derived by whoever wrote the page | a link, or a command or path in backticks, naming what it is derived from |

`[M]` (memory only, `GOAL.md`) is refused: nothing on a term page may rest on it.
`## Autor-Notizen` holds `<!-- autor:anfang -->` … `<!-- autor:ende -->`, the author's own
block: no tag rule applies inside it, no tool writes it, and it is outside the pin.
Every quotation is checked by `quotes.py` like every other wiki file.

**Approval** is the author's (P0): `approve <slug> --words "…"` sets `status: approved`
and appends a row to `Plan/runs/promotions.jsonl` (`layer: terms`) with the sha256 of the
page outside the author's block; `check` fails when an approved page changed since.
A term page whose candidate was re-reviewed since, or has readings waiting under
`## Since review`, is **behind** — noted, not failed: it is still true of the state it names.

Usage:
    python3 scripts/terms.py finds <slug>          # where the project itself names the term — for the writer
    python3 scripts/terms.py scaffold <slug>       # a new page: frontmatter, sections, the measured lines; refuses an unreviewed candidate
    python3 scripts/terms.py check                 # every term page against the rules above
    python3 scripts/terms.py approve <slug> --words "<the author's words>"
    python3 scripts/terms.py selftest
"""

from __future__ import annotations

import datetime
import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TERMS = ROOT / "Wiki" / "terms"
CANDIDATES = ROOT / "Wiki" / "candidates"
LEDGER = ROOT / "Plan" / "runs" / "promotions.jsonl"
SECTIONS = ["Kurz", "Was das Projekt entschieden hat", "Was die Quellen sagen", "Wo die Quellen auseinandergehen",
            "In der Prosa", "Offen", "Autor-Notizen", "Herkunft"]
TAGS = "KVSLD"
AUTHOR_OPEN, AUTHOR_CLOSE = "<!-- autor:anfang -->", "<!-- autor:ende -->"
BULLET = re.compile(r"^- \[(?P<tag>[A-Z])\] ")
CITE = re.compile(r"\^\[([a-z0-9][a-z0-9-]*)\.md:L\d+(?:[–-]L?\d+)?\]")
MDLINK = re.compile(r"\]\(([^)\s]+)\)")
TICKED = re.compile(r"`[^`]+`")
GERMAN = re.compile(r"\b(der|die|das|und|ist|nicht|ein|eine|von|mit|für|auf|den|dem|sie|wie|oder|keine|steht)\b", re.I)
ENGLISH = re.compile(r"\b(the|and|is|of|to|that|with|for|on|which|are|not|it|this)\b", re.I)
QUOTED = re.compile(r"„[^“\"]*[“\"]")
FINDS_IN = ["Plan/decisions", "Plan/weichen", "Manuscript/kanon.md", "Manuscript/figuren", "Manuscript/welt",
            "Plan/storyform", "Wiki/conflicts", "Wiki/questions"]

sys.path.insert(0, str(ROOT / "scripts"))


# --- reading a page --------------------------------------------------------

def frontmatter(text: str) -> dict:
    from wiki_index import frontmatter as fm
    return fm(text)


def body_of(text: str) -> str:
    from promote import split
    return split(text)[1]


def sections(text: str) -> list[tuple[str, list[tuple[int, str]]]]:
    """(heading, [(file line, line)]) for every `## ` section, in order."""
    out: list[tuple[str, list[tuple[int, str]]]] = []
    for no, line in enumerate(text.split("\n"), 1):
        if line.startswith("## "):
            out.append((line[3:].strip(), []))
        elif out:
            out[-1][1].append((no, line))
    return out


def outside_author(text: str) -> str:
    """The page without the author's block — what an approval pins."""
    a, b = text.find(AUTHOR_OPEN), text.find(AUTHOR_CLOSE)
    return text if a < 0 or b < a else text[:a] + text[b:]


def digest(text: str) -> str:
    return hashlib.sha256(outside_author(text).encode("utf-8")).hexdigest()


def bullets(lines: list[tuple[int, str]]) -> list[tuple[int, str, str]]:
    """(line, tag, text with its continuation lines) per bullet; a stray line is tag '?'."""
    out: list[list] = []
    for no, line in lines:
        if not line.strip() or line.strip().startswith("<!--"):
            continue
        m = BULLET.match(line)
        if m:
            out.append([no, m.group("tag"), line])
        elif line.startswith("  ") and out:
            out[-1][2] += "\n" + line
        else:
            out.append([no, "?", line])
    return [tuple(b) for b in out]


def resolve_link(page: Path, target: str) -> Path:
    return (page.parent / target.split("#")[0]).resolve()


def decided(path: Path) -> str | None:
    """Why a link target counts as the author's decision, or None."""
    rel = path.relative_to(ROOT).as_posix() if path.is_relative_to(ROOT) else str(path)
    if not path.exists():
        return None
    if rel.startswith("Plan/decisions/") and rel.endswith(".md") and not rel.endswith("README.md"):
        return "a decision file"
    if rel == "Manuscript/kanon.md":
        return "the canon ledger"
    meta = frontmatter(path.read_text(encoding="utf-8"))
    status = meta.get("status", "")
    if rel.startswith("Plan/weichen/") and status.startswith("beantwortet"):
        return "an answered Weiche"
    if rel.startswith("Wiki/conflicts/") and status.startswith("decided"):
        return "a decided conflict"
    return None


def landed() -> set[str]:
    return {p.stem for p in (ROOT / "Sources" / "drive").glob("*.md")}


# --- the rules ---------------------------------------------------------------

def problems_of(path: Path, ledger_rows: list[dict] | None = None, docs: set[str] | None = None,
                candidates: Path | None = None) -> tuple[list[str], list[str]]:
    """(failures, notes) for one term page."""
    import promote
    text = path.read_text(encoding="utf-8")
    meta = frontmatter(text)
    slug = path.stem
    docs = docs if docs is not None else landed()
    candidates = candidates or CANDIDATES
    rows = ledger_rows if ledger_rows is not None else promote.ledger(LEDGER)
    fail, note = [], []

    for key in ("term", "status", "kind", "candidate", "candidate_hash", "written", "by"):
        if not meta.get(key):
            fail.append(f"frontmatter lacks {key}")
    if meta.get("status") not in ("draft", "approved"):
        fail.append(f"status {meta.get('status')!r} is neither draft nor approved")

    cand = candidates / f"{meta.get('candidate', slug)}.md"
    reviews = [r for r in rows if r.get("page") == meta.get("candidate", slug) and r.get("layer", "candidates") == "candidates"]
    if not cand.exists():
        fail.append(f"no candidate page {cand.name}")
    else:
        ctext = cand.read_text(encoding="utf-8")
        if not promote.is_reviewed(ctext) or not reviews or reviews[-1].get("action") != "promote":
            fail.append("its candidate page is not reviewed — a term page is written from a reviewed candidate only (decision 026)")
        else:
            if not any(r.get("sha256") == meta.get("candidate_hash") for r in reviews if r.get("action") == "promote"):
                fail.append("candidate_hash names no review of its candidate in the ledger")
            elif reviews[-1]["sha256"] != meta.get("candidate_hash"):
                note.append(f"behind: its candidate was re-reviewed on {reviews[-1]['on']}")
            waiting = promote.since_readings(ctext)
            if waiting:
                note.append(f"behind: {len(waiting)} reading(s) wait under Since review on the candidate: {', '.join(waiting)}")

    found = sections(body_of(text))
    names = [n for n, _ in found]
    if names != SECTIONS:
        fail.append(f"sections are {names}, not {SECTIONS}")
    prose = []
    for name, lines in found:
        if name == "Autor-Notizen":
            joined = "\n".join(l for _, l in lines)
            if joined.count(AUTHOR_OPEN) != 1 or joined.count(AUTHOR_CLOSE) != 1:
                fail.append("## Autor-Notizen holds the author's block exactly once")
            continue
        items = bullets(lines)
        if not items and name in SECTIONS:
            fail.append(f"## {name} is empty — write `- [L] …` when nothing is known")
        for no, tag, item in items:
            where = f"L{no} (## {name})"
            if tag == "?":
                fail.append(f"{where}: not a tagged bullet: {item[:60]!r}")
                continue
            if tag not in TAGS:
                fail.append(f"{where}: tag [{tag}] is not one of [{'] ['.join(TAGS)}]")
                continue
            cites = CITE.findall(item)
            for c in cites:
                if c not in docs:
                    fail.append(f"{where}: cites {c}.md, which is no landed document")
            links = [resolve_link(path, t) for t in MDLINK.findall(item) if not t.startswith("http")]
            for target in links:
                if not target.exists():
                    fail.append(f"{where}: links to {target.name}, which does not exist")
            if tag == "S" and not cites:
                fail.append(f"{where}: [S] without a source citation ^[slug.md:Lnn]")
            if tag == "V" and not cites and not any("/Plan/" in str(t) for t in links):
                fail.append(f"{where}: [V] without a source citation or a link into Plan/")
            if tag == "K" and not any(decided(t) for t in links):
                fail.append(f"{where}: [K] links no decision of the author's (a decision file, an answered Weiche, "
                            f"kanon.md or a decided conflict)")
            if tag == "D" and not links and not TICKED.search(item):
                fail.append(f"{where}: [D] does not name what it is derived from (a link, or a path or command in backticks)")
            prose.append(QUOTED.sub(" ", CITE.sub(" ", TICKED.sub(" ", item))))

    words = " ".join(prose)
    de, en = len(GERMAN.findall(words)), len(ENGLISH.findall(words))
    if de <= en:
        fail.append(f"the page reads as English ({de} German, {en} English function words) — a term page is German (GOAL.md)")

    if meta.get("status") == "approved":
        mine = [r for r in rows if r.get("page") == slug and r.get("layer") == "terms"]
        if not mine or mine[-1].get("action") != "approve":
            fail.append("status approved, but no approval in the ledger stands for it")
        elif mine[-1]["sha256"] != digest(text):
            fail.append(f"changed since the author approved it on {mine[-1]['on']} — revert, or the author approves again")
    return fail, note


def check(terms: Path | None = None) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    terms = terms or TERMS
    fails, notes = {}, {}
    docs = landed()
    import promote
    rows = promote.ledger(LEDGER)
    for path in sorted(terms.glob("*.md")):
        if path.stem == "README":
            continue
        f, n = problems_of(path, rows, docs)
        fails[path.stem], notes[path.stem] = f, n
    return fails, notes


# --- the verbs ---------------------------------------------------------------

def finds(slug: str) -> list[str]:
    """Every line of the project's own records that writes one of the term's surfaces."""
    import promote
    pats = sorted({promote.fold(s) for s in promote.surfaces(slug)}, key=len, reverse=True)
    if not pats:
        return []
    pat = re.compile(r"(?<!\w)(?:" + "|".join(map(re.escape, pats)) + r")(?!\w)")
    out = []
    for place in FINDS_IN:
        base = ROOT / place
        files = [base] if base.is_file() else sorted(base.rglob("*.md")) + sorted(base.rglob("*.json"))
        for f in files:
            status = frontmatter(f.read_text(encoding="utf-8")).get("status", "") if f.suffix == ".md" else ""
            for no, line in enumerate(f.read_text(encoding="utf-8").split("\n"), 1):
                # A document's slug in backticks or a citation names a document, not the term.
                if pat.search(promote.fold(CITE.sub(" ", TICKED.sub(" ", line)))):
                    out.append(f"{f.relative_to(ROOT)}:{no}" + (f" [{status.split('#')[0].strip()}]" if status else "")
                               + "  " + line.strip()[:140])
    return out


def scaffold(slug: str, today: str | None = None) -> Path:
    import promote
    cand = CANDIDATES / f"{slug}.md"
    if not cand.exists():
        raise SystemExit(f"no candidate page Wiki/candidates/{slug}.md")
    ctext = cand.read_text(encoding="utf-8")
    reviews = [r for r in promote.ledger(LEDGER) if r.get("page") == slug and r.get("layer", "candidates") == "candidates"]
    if not promote.is_reviewed(ctext) or not reviews or reviews[-1].get("action") != "promote":
        raise SystemExit(f"refused: Wiki/candidates/{slug}.md is not reviewed — the author promotes it first (promote.py sheet {slug})")
    target = TERMS / f"{slug}.md"
    if target.exists():
        raise SystemExit(f"refused: {target.relative_to(ROOT)} exists; a scaffold never overwrites a page")
    today = today or datetime.date.today().isoformat()
    meta = frontmatter(ctext)
    cov = promote.coverage(slug, meta.get("ingested", []))
    found = finds(slug)
    hint = "\n".join(["<!-- Fundstellen im Projekt (`terms.py finds " + slug + "`), für den Schreibenden; nur eine Entscheidung trägt [K]:"]
                     + [f.replace("--", "—") for f in found[:40]] + ["-->"])
    title = meta.get("term") or slug
    page = f"""---
term: {title}
status: draft
kind: konzept
candidate: {slug}
candidate_hash: {reviews[-1]['sha256']}
written: {today}
by: session
---

# {title}

## Kurz

- [L] Noch nicht geschrieben.

## Was das Projekt entschieden hat

{hint}

- [L] Noch nicht geschrieben.

## Was die Quellen sagen

- [D] Jede Lesart mit Datum und Stellung steht auf der [Kandidatenseite](../candidates/{slug}.md).

## Wo die Quellen auseinandergehen

- [L] Noch nicht geschrieben.

## In der Prosa

- [L] Noch nicht geschrieben.

## Offen

- [D] {cov['naming']} gelandete Dokumente nennen den Begriff, {cov['on_page']} mit einer Lesart auf der Kandidatenseite, {len(cov['unread'])} ungelesen (`python3 scripts/promote.py sheet {slug}`, {today}).

## Autor-Notizen

{AUTHOR_OPEN}
{AUTHOR_CLOSE}

## Herkunft

- [D] Gerüst vom {today} aus der geprüften Kandidatenseite (Prüfung vom {reviews[-1]['on']}, `Plan/runs/promotions.jsonl`). Ein Entwurf: bestätigt ist die Seite erst mit dem Wort des Autors.
"""
    TERMS.mkdir(exist_ok=True)
    target.write_text(page, encoding="utf-8")
    return target


def approve(slug: str, words: str, by: str = "author", today: str | None = None) -> dict:
    if not words.strip():
        raise SystemExit("an approval records the author's words verbatim: --words is required (P0)")
    path = TERMS / f"{slug}.md"
    fail, _ = problems_of(path)
    if fail:
        raise SystemExit("refused — " + "; ".join(fail))
    import promote
    text = promote.set_fields(path.read_text(encoding="utf-8"), {"status": "approved"})
    path.write_text(text, encoding="utf-8")
    row = {"page": slug, "layer": "terms", "action": "approve", "on": today or datetime.date.today().isoformat(),
           "by": by, "words": words, "sha256": digest(text)}
    with LEDGER.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    return row


# --- selftest ----------------------------------------------------------------

GOOD = """---
term: T
status: draft
kind: konzept
candidate: t
candidate_hash: {sha}
written: 2026-10-08
by: session
---

# T

## Kurz

- [S] Die Quelle sagt es so: „x" ^[doc.md:L1]

## Was das Projekt entschieden hat

- [K] Der Autor hat es entschieden ([Entscheidung](../../Plan/decisions/001-x.md)).

## Was die Quellen sagen

- [D] Die Lesarten stehen auf der [Kandidatenseite](../candidates/t.md).

## Wo die Quellen auseinandergehen

- [L] Nichts ist bekannt, und keine Quelle sagt es.

## In der Prosa

- [L] Keine Form ist festgelegt.

## Offen

- [D] Eine Zahl, gezählt mit `promote.py sheet t`.

## Autor-Notizen

<!-- autor:anfang -->
Was immer der Autor schreibt, the and is of to.
<!-- autor:ende -->

## Herkunft

- [D] Geschrieben aus der [Kandidatenseite](../candidates/t.md).
"""


def selftest() -> int:
    import promote
    results: list[tuple[str, bool]] = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        terms, cands, decs = root / "Wiki" / "terms", root / "Wiki" / "candidates", root / "Plan" / "decisions"
        for d in (terms, cands, decs):
            d.mkdir(parents=True)
        (decs / "001-x.md").write_text("# 001\n", encoding="utf-8")
        cand = "---\nterm: T\nstatus: reviewed\nreviewed: 2026-10-08\n---\n\n# T\n\nLead.\n"
        (cands / "t.md").write_text(cand, encoding="utf-8")
        sha = promote.digest(cand)
        rows = [{"page": "t", "action": "promote", "on": "2026-10-08", "sha256": sha}]
        page = terms / "t.md"

        global ROOT
        saved = ROOT
        ROOT = root  # decided() reads decision files relative to ROOT
        try:
            def run(text: str, ledger: list[dict] | None = None) -> tuple[list[str], list[str]]:
                page.write_text(text, encoding="utf-8")
                return problems_of(page, rows if ledger is None else ledger, {"doc"}, cands)

            good = GOOD.format(sha=sha)
            f, n = run(good)
            results.append(("the first page's shape passes", f == [] and n == []))
            f, _ = run(good.replace("- [S] Die Quelle sagt es so: „x\" ^[doc.md:L1]", "- [S] Die Quelle sagt es so."))
            results.append(("[S] without a citation fails", any("[S] without" in x for x in f)))
            f, _ = run(good.replace("^[doc.md:L1]", "^[nirgends.md:L1]"))
            results.append(("a citation of no landed document fails", any("no landed document" in x for x in f)))
            f, _ = run(good.replace("([Entscheidung](../../Plan/decisions/001-x.md))", "(so heißt es)"))
            results.append(("[K] with no decision linked fails", any("[K] links no decision" in x for x in f)))
            f, _ = run(good.replace("- [D] Eine Zahl, gezählt mit `promote.py sheet t`.", "- [D] Eine Zahl, einfach so."))
            results.append(("[D] naming nothing fails", any("[D] does not name" in x for x in f)))
            f, _ = run(good.replace("- [L] Keine Form ist festgelegt.", "Keine Form ist festgelegt."))
            results.append(("an untagged line fails", any("not a tagged bullet" in x for x in f)))
            f, _ = run(good.replace("- [L] Keine Form", "- [M] Keine Form"))
            results.append(("[M] is refused", any("tag [M]" in x for x in f)))
            f, _ = run(good.replace("## In der Prosa", "## Sprache"))
            results.append(("a missing section fails", any("sections are" in x for x in f)))
            english = good
            for de, en in [("Die Quelle sagt es so", "The source says it so"), ("Der Autor hat es entschieden", "The author decided it"),
                           ("Die Lesarten stehen auf der", "The readings are on the"), ("Nichts ist bekannt, und keine Quelle sagt es", "Nothing is known and it is not said"),
                           ("Keine Form ist festgelegt", "It is not fixed"), ("Eine Zahl, gezählt mit", "A number, counted with"),
                           ("Geschrieben aus der", "Written from the")]:
                english = english.replace(de, en)
            f, _ = run(english)
            results.append(("a page in English fails", any("reads as English" in x for x in f)))
            f, _ = run(good.replace(f"candidate_hash: {sha}", "candidate_hash: 0000"))
            results.append(("a candidate hash no review recorded fails", any("names no review" in x for x in f)))
            f, _ = run(good, [])
            results.append(("an unreviewed candidate fails", any("not reviewed" in x for x in f)))
            later = rows + [{"page": "t", "action": "promote", "on": "2026-11-01", "sha256": "1111"}]
            f, n = run(good, later)
            results.append(("a re-reviewed candidate makes the page behind, not failed", f == [] and any("re-reviewed" in x for x in n)))
            approved = good.replace("status: draft", "status: approved")
            f, _ = run(approved)
            results.append(("approved without a ledger row fails", any("no approval" in x for x in f)))
            row = {"page": "t", "layer": "terms", "action": "approve", "on": "2026-10-09", "sha256": digest(approved)}
            f, _ = run(approved, rows + [row])
            results.append(("an approved page with its row passes", f == []))
            f, _ = run(approved.replace("Was immer der Autor schreibt", "Der Autor schreibt Neues"), rows + [row])
            results.append(("the author's block is outside the pin", f == []))
            f, _ = run(approved.replace("Keine Form ist festgelegt.", "Eine Form ist festgelegt."), rows + [row])
            results.append(("an edit after approval fails", any("changed since" in x for x in f)))
            f, _ = run(good.replace(AUTHOR_CLOSE, ""))
            results.append(("a broken author block fails", any("author's block" in x for x in f)))
        finally:
            ROOT = saved
    try:
        approve("t", "")
        results.append(("approve refuses without the author's words", False))
    except SystemExit as e:
        results.append(("approve refuses without the author's words", "--words" in str(e)))
    for name, ok in results:
        print(("held  " if ok else "FAILED") + "  " + name)
    failed = sum(1 for _, ok in results if not ok)
    print(f"{len(results) - failed} of {len(results)} held")
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    verb, rest = argv[0], argv[1:]

    def opt(name: str, default: str = "") -> str:
        return rest[rest.index(name) + 1] if name in rest and rest.index(name) + 1 < len(rest) else default

    if verb == "selftest":
        return selftest()
    if verb == "check":
        fails, notes = check()
        for slug in fails:
            for f in fails[slug]:
                print(f"FAIL  {slug}: {f}")
            for n in notes[slug]:
                print(f"note  {slug}: {n}")
        total = sum(len(v) for v in fails.values())
        approved = sum(1 for p in TERMS.glob("*.md") if p.stem != "README"
                       and frontmatter(p.read_text(encoding="utf-8")).get("status") == "approved")
        print(f"{len(fails)} term page(s), {approved} approved, {total} problem(s)")
        return 1 if total else 0
    if verb == "finds" and rest:
        print("\n".join(finds(rest[0])) or "nothing in the project's own records names it")
        return 0
    if verb == "scaffold" and rest:
        print(f"wrote {scaffold(rest[0]).relative_to(ROOT)}")
        return 0
    if verb == "approve" and rest:
        print(json.dumps(approve(rest[0], opt("--words"), opt("--by", "author")), ensure_ascii=False))
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
