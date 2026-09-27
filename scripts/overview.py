"""Every landed document, listed with its most important names — `Sources/README.md`.

A reader deciding which document to open next has had two ways to ask: `qmd`,
which ranks and does not enumerate, and `corpus.py`, which counts one term at a
time. Neither lists the corpus. This does, by writing a generated section at the
end of `Sources/README.md`: every file in `Sources/drive/`, by category, with the
names that matter most in it.

## Whose names

**The wiki's.** A name is counted under the page it belongs to, and printed as
the name the wiki uses for that page — so `Kern-Welt`, `Kernwelt` and `Kern-Welten`
are one entry, `Kern-Welten`. Three sources decide what belongs to a page, and
each is a decision somebody else already made:

1. **The page's own surfaces** (`Wiki/index.json`), plus the two forms its title
   writes beside the name: the part before ` — ` (`ARS` for „ARS — Autopoietische
   Reentry-Segmentierung") and a parenthesis (`DKT`, `K₀`). The slug is left out:
   `did` is a page slug and an English verb.
2. **Translation pairs** from `Plan/entities/bilingual.jsonl`, relation
   `translation` at p ≥ 0.8, where one side is a page's own surface, the pair
   switches language (`de` ↔ `en`) and the other side is judged an entity:
   `Core Worlds` is counted under `Kern-Welten`. One hop only, never from a
   surface a pair added, and a surface two pages claim goes to neither. The file
   also labels German-to-German pairs `translation` — `Kollaps` for `Oblivion` —
   which is why the language must switch. **A pair is a proposal** (the file says so), so
   every entry that a pair contributed to is marked `†` and the pair is listed
   at the end of the section. Nothing is merged anywhere else.
3. Nothing else. `fold()` equality is the lookup every reconciliation uses.

**Names that have no page** come second and are marked as such: the verified
rows of the entity lists (`Plan/entities/<slug>.md`, lists that pass `verify` as
a reading) and the entities of `bilingual.jsonl` judged at `entity_p` ≥ 0.8.
They are printed as written — with no page to normalise to, a translation hop
only moved `Guardian`, a term the corpus uses as its own, under `Wächter`.

## What „most important" means here

Not the most frequent — `AEGIS` is in most documents, and a list that says
`AEGIS, Kael, Kohärenz` for every row says nothing. The weight is tf-idf:
`(1 + ln n) · ln(N / df)`, n the occurrences in this document, df the documents
holding the name, N the documents landed. The printed number is n, a count, and
never the weight. A name must occur at least twice to be listed.

## How a name is found

Each line is split into word and punctuation tokens (`entities.TOKEN`). At each
position the longest run of tokens whose fold is a known name wins, so
`Kohärenz-Kernel` is one hit for its page and none for `Kohärenz`. A run may
cross `-`, `/`, `'`, `.` and whitespace, and stops at any other punctuation.
A single token of four characters or fewer must match case and all: `Lex` the
figure, not `lex`; `DID` the diagnosis, not `did`.

## The qmd first scan

`scan` asks qmd (BM25, `-c sources`) for each page's name and keeps the ranked
documents in `Plan/runs/qmd-scan/pages.json`. The README prints, per page, the
top unread documents — **a place to look first, never a count** (CLAUDE.md,
*Searching the corpus*). It runs before `write` and is optional: without the
file the section is left out and says so.

Usage:
    python3 scripts/overview.py scan        # qmd first scan -> Plan/runs/qmd-scan/pages.json
    python3 scripts/overview.py             # write the section of Sources/README.md
    python3 scripts/overview.py --check     # fail if the section is stale
    python3 scripts/overview.py doc <slug>  # one document's names, weights shown
    python3 scripts/overview.py selftest
"""

from __future__ import annotations

import json
import math
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from functools import lru_cache
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import subject  # noqa: E402
import wiki_index  # noqa: E402
from subject import ROOT  # noqa: E402

README = ROOT / "Sources" / "README.md"
BILINGUAL = ROOT / "Plan" / "entities" / "bilingual.jsonl"
SCAN = ROOT / "Plan" / "runs" / "qmd-scan" / "pages.json"
TERMS = ROOT / "Sources" / "terms"
HAIKU = ROOT / "Plan" / "runs" / "haiku-scan-2026-09-25"
BEGIN = "<!-- overview:begin — written by scripts/overview.py, do not edit by hand -->"
END = "<!-- overview:end -->"

TOKEN = re.compile(r"\w+|[^\w\s]")
JOIN = {"-", "/", "'", "’", ".", "‑", "–"}
PAIR_P = 0.8
ENTITY_P = 0.8
MAX_RUN = 12
SHORT = 4
TOP_PAGES = 8
TOP_OTHER = 5
MIN_N = 2
SCAN_TOP = 6


# ── the vocabulary ────────────────────────────────────────────────────────────

def display(title: str) -> str:
    """The wiki's name for a page, without the gloss its title carries."""
    name = title.split(" — ")[0].strip()
    return re.sub(r"\s*\([^)]*\)\s*$", "", name).strip() or title


def title_forms(title: str) -> list[str]:
    """The forms a title writes beside its name: `ARS` of `ARS — …`, `DKT` of `(DKT)`."""
    forms = [display(title)]
    if " — " in title:
        forms.append(title.split(" — ")[0].strip())
    forms += re.findall(r"\(([^)]+)\)", title)
    return forms


def words(surface: str) -> list[str]:
    return [t for t in TOKEN.findall(surface) if re.match(r"\w", t)]


class Vocabulary:
    """Surface -> canonical name, in three tables by how strictly a token must match."""

    def __init__(self) -> None:
        self.exact: dict[str, str] = {}      # a short single token, case kept
        self.folded: dict[str, str] = {}     # everything else, by fold()
        self.kind: dict[str, str] = {}       # canonical -> "page" | "entity"
        self.page_slug: dict[str, str] = {}  # canonical -> page slug
        self.via_pair: dict[str, list[str]] = defaultdict(list)  # canonical -> surfaces a pair added
        self.pair_keys: set[tuple[str, str]] = set()             # the keys those surfaces hold
        self.ambiguous: set[str] = set()

    def key(self, surface: str) -> tuple[str, str] | None:
        """Which table a surface belongs in, and its key there."""
        toks = words(surface)
        if not toks:
            return None
        if len(toks) == 1 and len(surface) <= SHORT:
            return ("exact", surface.strip())
        folded = wiki_index.fold(surface)
        return ("folded", folded) if len(folded) >= 3 else None

    def owner(self, surface: str) -> str | None:
        k = self.key(surface)
        if not k:
            return None
        return (self.exact if k[0] == "exact" else self.folded).get(k[1])

    def add(self, surface: str, canonical: str, kind: str, *, strong: bool) -> bool:
        """Claim `surface` for `canonical`. A strong claim (a page's own surface)
        makes a surface two pages claim ambiguous; a weak one never overrides."""
        k = self.key(surface)
        if not k or k[1] in self.ambiguous:
            return False
        table = self.exact if k[0] == "exact" else self.folded
        held = table.get(k[1])
        if held is None:
            table[k[1]] = canonical
            self.kind.setdefault(canonical, kind)
            return True
        if held != canonical and strong and self.kind.get(held) == "page":
            del table[k[1]]
            self.ambiguous.add(k[1])
        return False


@lru_cache(maxsize=1)
def vocabulary() -> Vocabulary:
    import entities as E

    vocab = Vocabulary()
    index = wiki_index.build()
    page_surfaces: dict[str, list[str]] = {}
    for slug, row in index["terms"].items():
        name = display(row["title"])
        vocab.page_slug[name] = slug
        surfaces = [s for s in row.get("surfaces", []) if s != slug] + title_forms(row["title"])
        page_surfaces[name] = list(dict.fromkeys(surfaces))
        for surface in page_surfaces[name]:
            vocab.add(surface, name, "page", strong=True)

    rows = [json.loads(l) for l in BILINGUAL.read_text(encoding="utf-8").splitlines() if l.strip()] \
        if BILINGUAL.exists() else []
    by_surface = {r["surface"]: r for r in rows}

    # 2. translation pairs touching a page's own surface: one hop, and only a pair
    #    that switches language. `bilingual.jsonl` also labels German-to-German
    #    pairs `translation` (`Kollaps` for `Oblivion`, `Logik` for `LogOS`), and
    #    a hop taken from a surface a pair added chains (`Teile ← Parts ← Alters`).
    #    The added surface must itself be judged an entity, which drops `ages`.
    def lang(surface: str) -> str | None:
        return (by_surface.get(surface) or {}).get("lang")

    def entity(surface: str) -> bool:
        return ((by_surface.get(surface) or {}).get("entity_p") or 0) >= ENTITY_P

    own = {surface: name for name, surfaces in page_surfaces.items() for surface in surfaces
           if vocab.owner(surface) == name}
    for r in rows:
        for other in r.get("same_as", []):
            if other.get("relation") != "translation" or other.get("p", 0) < PAIR_P:
                continue
            for a, b in ((r["surface"], other["surface"]), (other["surface"], r["surface"])):
                page = own.get(a)
                if not page or vocab.owner(b) or not entity(b):
                    continue
                if {lang(a), lang(b)} != {"de", "en"}:
                    continue
                if vocab.add(b, page, "page", strong=False):
                    vocab.via_pair[page].append(f"{b} ← {a}")
                    vocab.pair_keys.add(vocab.key(b))

    # names with no page: the verified entity lists, then bilingual's entities
    listed: list[str] = []
    for entry in E.lists():
        E.verify(entry)
        if entry["reading"]:
            listed += [row["term"] for row in entry["rows"] if row["verified"]]
    judged = [r["surface"] for r in rows
              if (r.get("entity_p") or 0) >= ENTITY_P and r.get("lang") != "other"]
    # Printed as written. A translation hop here counted `Guardian`, a term the
    # corpus uses as its own, as `Wächter`, and `Alignment Problem` as
    # `Fehlausgerichtete Kohärenz`; with no page to normalise to, the surface stays.
    for surface in dict.fromkeys(listed + judged):
        if not vocab.owner(surface):
            vocab.add(surface, surface, "entity", strong=False)
    return vocab


# ── counting ──────────────────────────────────────────────────────────────────

@lru_cache(maxsize=200_000)
def _fold(token: str) -> str:
    return wiki_index.fold(token) if re.match(r"\w", token) else ""


def names_in(text: str, vocab: Vocabulary, paired: set | None = None) -> Counter:
    """Every known name in `text`, longest match first, counted per canonical name.

    `paired`, when given, collects the names at least one hit reached through a
    surface a translation pair added -- the names the README marks with †."""
    found: Counter = Counter()
    for line in text.split("\n"):
        toks = TOKEN.findall(line)
        i = 0
        while i < len(toks):
            tok = toks[i]
            if not re.match(r"\w", tok):
                i += 1
                continue
            best, best_end, best_key = None, i, None
            key = ""
            for j in range(i, min(len(toks), i + MAX_RUN)):
                t = toks[j]
                if j > i and not re.match(r"\w", t) and t not in JOIN:
                    break
                key += _fold(t)
                if not re.match(r"\w", t):
                    continue
                if j == i and len(tok) <= SHORT:
                    table_key = ("exact", tok)
                    hit = vocab.exact.get(tok)
                else:
                    table_key = ("folded", key)
                    hit = vocab.folded.get(key) if len(key) >= 3 else None
                if hit:
                    best, best_end, best_key = hit, j, table_key
            if best:
                found[best] += 1
                if paired is not None and best_key in vocab.pair_keys:
                    paired.add(best)
                i = best_end + 1
            else:
                i += 1
    return found


def measure() -> dict:
    """Per document: counts per canonical name, and the tf-idf ranking over the corpus."""
    vocab = vocabulary()
    docs = subject.documents()
    paired: dict[str, set] = {d.slug: set() for d in docs}
    counts = {d.slug: names_in(d.body, vocab, paired[d.slug]) for d in docs}
    df = Counter(name for c in counts.values() for name in c)
    total = len(docs)

    def ranked(c: Counter, kind: str) -> list[tuple[str, int, float]]:
        rows = [(name, n, (1 + math.log(n)) * math.log(total / df[name]))
                for name, n in c.items() if n >= MIN_N and vocab.kind.get(name) == kind]
        return sorted(rows, key=lambda r: (-r[2], -r[1], r[0]))

    return {"vocab": vocab, "counts": counts, "df": df, "total": total, "paired": paired,
            "pages": {s: ranked(c, "page") for s, c in counts.items()},
            "other": {s: ranked(c, "entity") for s, c in counts.items()}}


# ── the qmd first scan ────────────────────────────────────────────────────────

def cmd_scan(n: int = 10) -> int:
    """Ask qmd for each page's name, in sources; keep the ranked slugs. Ranks, not counts."""
    import qmd

    index = wiki_index.build()
    out = {"ran": date.today().isoformat(), "command": f"qmd search <name> -c sources -n {n}",
           "note": "ranked places to look; never a count", "pages": {}}
    for slug, row in sorted(index["terms"].items()):
        name = display(row["title"])
        hits = qmd.search(name, collection="sources", n=n)
        out["pages"][slug] = {"query": name, "hits": [
            {"slug": h.slug, "score": round(h.score, 3), "line": h.line} for h in hits
            if h.slug]}
    SCAN.parent.mkdir(parents=True, exist_ok=True)
    SCAN.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    empty = sum(1 for p in out["pages"].values() if not p["hits"])
    print(f"{len(out['pages'])} pages asked, {empty} with no hit -> {SCAN.relative_to(ROOT)}")
    return 0


# ── the README section ────────────────────────────────────────────────────────

def status_of() -> dict[str, str]:
    read = {p.stem for p in TERMS.glob("*.md")}
    scanned = {p.stem for p in HAIKU.glob("*.md")} if HAIKU.exists() else set()
    return {**{s: "scanned" for s in scanned}, **{s: "**read**" for s in read}}


def cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def render(m: dict) -> str:
    vocab: Vocabulary = m["vocab"]
    rows = {r["slug"]: r for r in subject.rows()}
    status = status_of()
    docs = sorted(subject.documents(), key=lambda d: (d.category, d.date, d.slug))
    by_cat: dict[str, list] = defaultdict(list)
    for d in docs:
        by_cat[d.category].append(d)
    marked = {name for name, pairs in vocab.via_pair.items() if pairs}

    def fmt(entries, slug: str) -> str:
        return ", ".join(f"{name}{'†' if name in m['paired'][slug] else ''} {n}"
                         for name, n, _ in entries) or "—"

    out = [BEGIN, "", "## Every document, and the names that matter in it", "",
           f"**{len(docs)} documents in `drive/`**, by category, oldest first. Generated by "
           "`python3 scripts/overview.py` from the files, the wiki index, the entity lists "
           "and the translation pairs; `--check` fails when it is stale. **Every number is "
           "a count** — how often the name occurs in that document — and the order is "
           "tf-idf, so a name every document uses sinks. The script's docstring has the "
           "rules.", "",
           "- **Wiki names** are the wiki's pages, printed as the page names them; every "
           "surface the page lists counts for it.",
           "- **Other names** have no page: entity-list rows and names `bilingual.py` judged "
           "to be entities. A proposal, not a census.",
           "- **†** marks a name whose count in that document includes a surface a "
           "translation pair added (the pairs are listed at the end). A pair is a "
           "proposal; it merges nothing outside this list.",
           "- **status**: **read** has a census, note and reconciliation; *scanned* had "
           "the 2026-09-25 triage scan only.", ""]
    missing = [r for r in rows.values() if not r.get("export_path")]
    counts = Counter(d.category for d in docs)
    out += ["| category | documents |", "|---|--:|"]
    out += [f"| [{c}](#{c}) | {counts[c]} |" for c in sorted(by_cat)]
    out += [""]
    if missing:
        out += [f"Not landed: {', '.join(cell(r.get('title', r['slug'])) + ' (`' + r.get('format', '?') + '`)' for r in missing)}.", ""]

    for cat in sorted(by_cat):
        out += [f"### {cat}", "",
                "| document | date | words | status | wiki names | other names |",
                "|---|---|--:|---|---|---|"]
        for d in by_cat[cat]:
            title = cell(rows.get(d.slug, {}).get("title") or d.slug)
            words_n = len(d.body.split())
            out.append(f"| [{title}](drive/{d.slug}.md) | {d.date} | {words_n:,} | "
                       f"{status.get(d.slug, '')} | {cell(fmt(m['pages'][d.slug][:TOP_PAGES], d.slug))} | "
                       f"{cell(fmt(m['other'][d.slug][:TOP_OTHER], d.slug))} |")
        out.append("")

    if SCAN.exists():
        scan = json.loads(SCAN.read_text(encoding="utf-8"))
        read = {s for s, v in status.items() if v == "**read**"}
        out += ["### Where to look first, by wiki page", "",
                f"The qmd first scan of {scan['ran']}: `{scan['command']}` for each page's "
                "name, the top unread documents in rank order. **A rank, not a count** — "
                "BM25 favours short, early chunks, and a document missing here may still "
                "hold the line you want.", "",
                "| page | first unread documents qmd ranks |", "|---|---|"]
        for slug, entry in sorted(scan["pages"].items()):
            seen, picks = set(), []
            for h in entry["hits"]:
                if h["slug"] in read or h["slug"] in seen:
                    continue
                seen.add(h["slug"])
                picks.append(f"[{h['slug']}](drive/{h['slug']}.md)")
            out.append(f"| [{cell(entry['query'])}](../Wiki/candidates/{slug}.md) | "
                       f"{', '.join(picks[:SCAN_TOP]) or '—'} |")
        out.append("")
    else:
        out += ["*No qmd first scan on record — `python3 scripts/overview.py scan` writes one.*", ""]

    if marked:
        out += ["### The translation pairs used", "",
                f"From `Plan/entities/bilingual.jsonl`, relation `translation`, p ≥ {PAIR_P}. "
                "`A ← B`: surface A counted under the name, because the pair links it to B.", "",
                "| name | surfaces a pair added |", "|---|---|"]
        for name in sorted(marked):
            out.append(f"| {cell(name)} | {cell(', '.join(vocab.via_pair[name]))} |")
        out.append("")
    if vocab.ambiguous:
        out += [f"{len(vocab.ambiguous)} surfaces are claimed by two pages and counted for "
                f"neither: {', '.join(sorted(vocab.ambiguous))}.", ""]
    out.append(END)
    return "\n".join(out) + "\n"


def splice(text: str, section: str) -> str:
    if BEGIN in text:
        head = text[:text.index(BEGIN)]
        tail = text[text.index(END) + len(END):].lstrip("\n") if END in text else ""
        return head + section + (("\n" + tail) if tail else "")
    return text.rstrip("\n") + "\n\n" + section


def cmd_write(check: bool) -> int:
    section = render(measure())
    current = README.read_text(encoding="utf-8")
    new = splice(current, section)
    if check:
        if new != current:
            print(f"{README.relative_to(ROOT)}: the overview is stale — run scripts/overview.py")
            return 1
        print("overview current")
        return 0
    README.write_text(new, encoding="utf-8")
    print(f"wrote {README.relative_to(ROOT)}: {section.count(chr(10))} lines in the section")
    return 0


def cmd_doc(slug: str) -> int:
    m = measure()
    for kind in ("pages", "other"):
        print(f"# {kind}")
        for name, n, w in m[kind][slug][:20]:
            print(f"  {name:40s} n={n:<4d} df={m['df'][name]:<4d} w={w:.2f}")
    return 0


# ── self-test ─────────────────────────────────────────────────────────────────

def cmd_selftest() -> int:
    v = Vocabulary()
    for s in ("Kern-Welt", "Kern-Welten"):
        v.add(s, "Kern-Welten", "page", strong=True)
    for s in ("Kohärenz", "Kohärenz-Kernel", "Lex", "DID", "AEGIS"):
        v.add(s, s, "page", strong=True)
    v.add("Core Worlds", "Kern-Welten", "page", strong=False)
    v.pair_keys.add(v.key("Core Worlds"))
    v.add("Nyx", "A", "page", strong=True)
    v.add("Nyx", "B", "page", strong=True)
    cases = [
        ("Die Kernwelt und die Kern-Welten", {"Kern-Welten": 2}),
        ("Der Kohärenz-Kernel hält", {"Kohärenz-Kernel": 1}),
        ("Kohärenz, dann Kohärenz-Kernel", {"Kohärenz": 1, "Kohärenz-Kernel": 1}),
        ("what did Lex say about lex", {"Lex": 1}),
        ("DID and did", {"DID": 1}),
        ("the Core Worlds hold", {"Kern-Welten": 1}),
        ("Aegis und AEGIS", {"AEGIS": 2}),
        ("Kern (Welt)", {}),
        ("Nyx spricht", {}),
    ]
    failed = 0
    for text, want in cases:
        got = dict(names_in(text, v))
        ok = got == want
        failed += not ok
        print(f"  {'ok ' if ok else 'FAIL'} {text!r}: {got}" + ("" if ok else f" want {want}"))
    for text, want in (("the Core Worlds hold", {"Kern-Welten"}), ("die Kernwelt", set())):
        paired: set = set()
        names_in(text, v, paired)
        ok = paired == want
        failed += not ok
        print(f"  {'ok ' if ok else 'FAIL'} † {text!r}: {paired}" + ("" if ok else f" want {want}"))
    assert display("ANI — Äußere Nicht-Identifikation") == "ANI"
    assert display("Dual-Kernel-Theorie (DKT)") == "Dual-Kernel-Theorie"
    assert title_forms("Kollaps-Kernel (K₀)") == ["Kollaps-Kernel", "K₀"]
    print("selftest", "held" if not failed else f"FAILED ({failed})")
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    if argv[:1] == ["scan"]:
        return cmd_scan()
    if argv[:1] == ["selftest"]:
        return cmd_selftest()
    if argv[:1] == ["doc"] and len(argv) > 1:
        return cmd_doc(argv[1])
    return cmd_write(check="--check" in argv)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
