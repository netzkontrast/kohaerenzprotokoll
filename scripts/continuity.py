"""The continuity register: what holds at the start of each chapter, in four tables, and a draft checked against it.

Decision 030 (2026-10-26): continuity is kept per chapter in four tables — **wissen** (who knows what: Kael, AEGIS,
the reader), **zeit** (day, clock, deadline), **zahlen** (the heat quantities and the book's numbers) and **dinge**
(objects, places, figures and names, each with the chapter it enters) — and every draft is checked against them.
The four hand tables of 2026-10-06 (`Plan/runs/storyform-2026-10-06/`) are the seed, with their provenance.

    Manuscript/kontinuitaet/kap-NN.json      {"kapitel": N, "status": "proposal"|"approved", "provenance": …,
                                              "wissen": [{"wer": "Kael"|"AEGIS"|"Leser", "fakt": …, "seit": N, "marker": [...], "quelle": …, "status": …}],
                                              "zeit": [{"was": …, "wert": …, "quelle": …, "status": …}],
                                              "zahlen": [{"name": …, "wert": …, "einheit": …, "quelle": …, "status": …}],
                                              "dinge": [{"name": …, "art": "figur"|"anteil"|"ort"|"gegenstand"|"welt", "seit": N, "quelle": …, "status": …}]}

**A draft changes nothing in the register until it is approved** (`manuscript.py approve` adds what an approved scene
establishes, as `status: approved` rows). `seed` writes the proposal rows from what is structured enough to read by
code: the canon ledger (C7, Kernwelten, Q7, W12), `weave.json` (the world of each chapter), `anteile.json` (which parts
appear, how, and that none is named before Kap 13), `clock-b.json` (AEGIS' reserve per chapter), `development.json`
(`timing`, `knowledge`, `reader`), the treatment (the chapter a figure is first named in) and the hand knowledge table
(its five columns per chapter). Every seed row is `status: proposal` and says where it came from.

`check <draft>` holds the draft to the register of its chapter — **the state at the start of the chapter**, i.e. the
rows of chapters below it, plus the rows of its own chapter marked as entering there:

| check | finds |
|---|---|
| a number | a `zahlen` row whose name stands in the draft near a different value |
| a thing too early | a `dinge` row (figure, part, place, object) named in the draft before its `seit` chapter |
| knowledge too early | a `wissen` row whose `marker` words stand in the draft before its `seit` chapter |

Every finding is a **query** (gewollter Riss oder Versehen?), never a failure: which version holds is the author's,
as the `continuity-editor` skill says. A row with `status: approved` makes the query say so.

Usage:
    python3 scripts/continuity.py seed [--force]         # write the proposal rows for Kap 0–40 (keeps approved rows)
    python3 scripts/continuity.py show kap-NN            # the state at the start of a chapter, by table
    python3 scripts/continuity.py check <draft.md> [--kap N] [--json]
    python3 scripts/continuity.py register               # every file well formed (CI)
    python3 scripts/continuity.py selftest
"""

from __future__ import annotations

import json
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
FOLDER = ROOT / "Manuscript" / "kontinuitaet"
KANON = ROOT / "Manuscript" / "kanon.md"
STORYFORM = ROOT / "Plan" / "storyform"
TREATMENT = ROOT / "Manuscript" / "plot" / "treatment.md"
TABLE = ROOT / "Plan" / "runs" / "storyform-2026-10-06" / "wissenstabelle.md"
FIGUREN = ROOT / "Manuscript" / "figuren"
TABLES = ("wissen", "zeit", "zahlen", "dinge")
NUMBER = re.compile(r"\d+(?:[,.]\d+)?(?:\s?[×x]\s?10[⁰¹²³⁴⁵⁶⁷⁸⁹]+)?\s?(?:%|°C|Bit|J\b|Joule|Grad)?")


def path_of(n: int, folder: Path | None = None) -> Path:
    return (folder or FOLDER) / f"kap-{n:02d}.json"


def load(n: int, folder: Path | None = None) -> dict:
    p = path_of(n, folder)
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return {"kapitel": n, "status": "proposal", "provenance": "", **{t: [] for t in TABLES}}


def save(reg: dict, folder: Path | None = None) -> None:
    p = path_of(reg["kapitel"], folder)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


# --- the state at the start of a chapter ----------------------------------------------

def state_at(n: int, folder: Path | None = None) -> dict[str, list[dict]]:
    """Every row of chapters 0..n-1, and the rows of chapter n that say `seit` ≤ n or carry no `seit`:
    what a writer of chapter n may rely on. Later rows (seit > n) are kept apart as `later`."""
    out: dict[str, list[dict]] = {t: [] for t in TABLES}
    later: list[dict] = []
    top = max([n] + [int(m.group(1)) for p in (folder or FOLDER).glob("kap-*.json") for m in [re.search(r"kap-(\d+)", p.name)] if m])
    for k in range(0, top + 1):
        reg = load(k, folder)
        for t in TABLES:
            for row in reg.get(t, []):
                r = {**row, "kapitel": k}
                seit = r.get("seit", k)
                r["seit"] = seit
                if seit <= n and k <= n:
                    out[t].append(r)
                elif t in ("dinge", "wissen") and seit > n:
                    later.append({**r, "tabelle": t})
    # one row per thing or fact still to come, at its earliest chapter
    first: dict[tuple, dict] = {}
    for r in later:
        key = (r["tabelle"], r.get("name") or r.get("fakt"))
        if key not in first or r["seit"] < first[key]["seit"]:
            first[key] = r
    out["later"] = sorted(first.values(), key=lambda r: (r["seit"], r["tabelle"], str(r.get("name") or r.get("fakt"))))
    return out


def chapter_of(path: Path) -> int | None:
    m = re.search(r"kap-(\d+)", str(path))
    return int(m.group(1)) if m else None


def check(path: Path, kap: int | None = None, folder: Path | None = None) -> list[dict]:
    import prose_rules as rules
    text = rules.prose_of(path.read_text(encoding="utf-8"))
    kap = kap if kap is not None else chapter_of(path)
    if kap is None:
        raise SystemExit(f"{path}: which chapter? name it kap-NN or pass --kap")
    st = state_at(kap, folder)
    out = []
    paras = rules.paragraphs(text)

    def word(w: str) -> re.Pattern:
        return re.compile(r"(?<![\wÄÖÜäöüß])" + re.escape(w) + r"(?![\wÄÖÜäöüß])")

    # numbers: a named quantity near a different value
    for row in st["zahlen"]:
        pat = re.compile(word(row["name"]).pattern + r"[^.\n]{0,60}?(" + NUMBER.pattern + ")")
        for no, para in paras:
            for m in pat.finditer(para):
                found = m.group(1).replace(" ", "")
                want = str(row["wert"]).replace(" ", "")
                if found and want and found.rstrip(".") != want.rstrip(".") and not want.startswith(found.rstrip(".")):
                    out.append({"tabelle": "zahlen", "absatz": no, "name": row["name"], "register": f"{row['wert']} ({row.get('quelle', '?')}, Kap {row['kapitel']}, {row.get('status', '?')})",
                                "entwurf": m.group(1).strip(), "frage": f"„{row['name']}“ steht im Register bei {row['wert']}, im Entwurf bei {m.group(1).strip()}"})
    # things and knowledge before their chapter
    for row in st["later"]:
        words = row.get("marker") or [row.get("name")]
        for w in [x for x in words if x]:
            pat = word(w)
            for no, para in paras:
                if pat.search(para):
                    out.append({"tabelle": row["tabelle"], "absatz": no, "name": w, "register": f"ab Kap {row['seit']} ({row.get('quelle', '?')}, {row.get('status', '?')})",
                                "entwurf": para[max(0, pat.search(para).start() - 40):pat.search(para).end() + 40],
                                "frage": (f"„{w}“ tritt laut Register erst in Kap {row['seit']} ein" if row["tabelle"] == "dinge"
                                          else f"{row.get('wer', '?')} weiß „{row.get('fakt', w)[:60]}“ laut Register erst ab Kap {row['seit']}") + " — gewollter Riss oder Versehen?"})
                    break
    return out


# --- the seed ----------------------------------------------------------------------------

def _kanon_rows() -> list[dict]:
    import weiche
    return weiche.kanon_rows()


def _first_named(treatment: str) -> dict[str, int]:
    names = {}
    for p in sorted(FIGUREN.glob("*.md")):
        m = re.search(r"^match: \[(.*)\]$", p.read_text(encoding="utf-8"), re.M)
        if m:
            for x in m.group(1).split(","):
                names[x.strip().strip('"')] = p.stem
    first: dict[str, int] = {}
    cur = None
    for line in treatment.split("\n"):
        m = re.match(r"^### Kap (\d+)", line)
        if m:
            cur = int(m.group(1))
            continue
        if cur is None:
            continue
        for n in names:
            if n not in first and re.search(r"(?<![\wÄÖÜäöüß])" + re.escape(n) + r"(?![\wÄÖÜäöüß])", line):
                first[n] = cur
    return first


def _knowledge_table() -> dict[int, dict[str, str]]:
    """The hand table's five columns per chapter: (a) 734, (b) Genesis, (c) Juna, (d) Anschluss/Kanal, (e) zehn Jahre."""
    if not TABLE.exists():
        return {}
    cols = ["734 / Cluster", "Genesis", "Juna", "Anschluss / Kanal", "zehn Jahre"]
    out: dict[int, dict[str, str]] = {}
    on = False
    for line in TABLE.read_text(encoding="utf-8").split("\n"):
        if line.startswith("## Die Tabelle"):
            on = True
            continue
        if on and line.startswith("## "):
            break
        m = re.match(r"^\| (\d+) \|(.*)\|$", line) if on else None
        if m:
            cells = [c.strip() for c in m.group(2).split("|")]
            out[int(m.group(1))] = {c: v for c, v in zip(cols, cells) if v and v != "—"}
    return out


def seed(folder: Path | None = None, force: bool = False, today: str = "2026-10-26") -> int:
    folder = folder or FOLDER
    weave = json.loads((STORYFORM / "weave.json").read_text(encoding="utf-8"))
    anteile = json.loads((STORYFORM / "anteile.json").read_text(encoding="utf-8"))
    clock = json.loads((STORYFORM / "clock-b.json").read_text(encoding="utf-8"))
    dev = json.loads((STORYFORM / "development.json").read_text(encoding="utf-8"))["chapters"]
    treatment = TREATMENT.read_text(encoding="utf-8") if TREATMENT.exists() else ""
    first = _first_named(treatment)
    table = _knowledge_table()
    kanon = {r["id"]: r for r in _kanon_rows()}
    P = "proposal"
    n_rows = 0
    for n in range(0, 41):
        reg = load(n, folder)
        kept = {t: [r for r in reg.get(t, []) if r.get("status") == "approved"] for t in TABLES}
        if not force and any(r.get("status") != "approved" for t in TABLES for r in reg.get(t, [])) and path_of(n, folder).exists():
            continue
        new = {t: [] for t in TABLES}
        # the world (canon: Kernwelten) and the route
        w = next((x for x in weave.get("worlds", []) if x["chapters"][0] <= n <= x["chapters"][1]), None)
        if w:
            new["dinge"].append({"name": w["world"], "art": "welt", "seit": w["chapters"][0], "quelle": "Plan/storyform/weave.json (Kanonzeile Kernwelten)", "status": P})
        # AEGIS' reserve
        if str(n) in clock.get("readings", {}):
            new["zahlen"].append({"name": "Abwärmebudget", "wert": f"{clock['readings'][str(n)]} %", "einheit": clock.get("unit", "%"), "quelle": "Plan/storyform/clock-b.json (Schritt 48, Werte Vorschlag)", "status": P})
        # the parts that appear here, and that none is named before unnamed_until
        for app in anteile.get("appearances", []):
            if n in app.get("chapters", []):
                for part in app["parts"]:
                    new["dinge"].append({"name": part, "art": "anteil", "seit": anteile.get("unnamed_until", 13) if n < anteile.get("unnamed_until", 13) else n,
                                         "kanal": app.get("channel"), "wie": app.get("how", "")[:160], "quelle": "Plan/storyform/anteile.json", "status": P,
                                         "hinweis": "zeigt sich hier über " + str(app.get("channel")) + "; der Name fällt nicht vor Kap " + str(anteile.get("unnamed_until", 13))})
        if n == 0:
            for part in anteile.get("parts", []):
                if part != "Kael":
                    new["dinge"].append({"name": part, "art": "anteil", "seit": anteile.get("unnamed_until", 13), "quelle": "Plan/storyform/anteile.json unnamed_until", "status": P})
        # figures: the chapter the treatment first names them in
        for name, k in first.items():
            if k == n and name not in anteile.get("parts", []):
                new["dinge"].append({"name": name, "art": "figur", "seit": k, "quelle": "Manuscript/plot/treatment.md, erste Nennung (Vorschlag)", "status": P})
        # Juna's chapters (canon C7)
        if n == 0 and "C7" in kanon:
            new["dinge"].append({"name": "Juna", "art": "figur", "seit": 4, "quelle": "Manuscript/kanon.md C7: Kap 4, 11 erinnert; 17, 25 Spuren; 32 Gegenwart", "status": "kanon"})
            new["wissen"].append({"wer": "Kael", "fakt": "Junas Name (W7 empfiehlt Kap 11)", "seit": 11, "marker": ["Juna"], "quelle": "Plan/weichen/w7-schleier.md (Empfehlung)", "status": P})
            new["wissen"].append({"wer": "Kael", "fakt": "dass er das aus 734 herausgetrennte Cluster ist (W30 empfiehlt: am Vortex)", "seit": 35, "marker": ["734"], "quelle": "Plan/weichen/w30-734-auf-kaels-seite.md (Empfehlung B)", "status": P})
            new["wissen"].append({"wer": "Kael", "fakt": "die Zahl der gelöschten Jahre, zehn", "seit": 12, "marker": ["zehn Jahre"], "quelle": "Plan/runs/storyform-2026-10-06/wissenstabelle.md Kap 12", "status": P})
        # development.json: timing, knowledge, reader
        row = dev.get(str(n), {})
        if row.get("timing"):
            new["zeit"].append({"was": "Lage", "wert": row["timing"], "quelle": "Plan/storyform/development.json timing", "status": P})
        if row.get("knowledge"):
            new["wissen"].append({"wer": "Stand", "fakt": row["knowledge"], "seit": n, "quelle": "Plan/storyform/development.json knowledge (was gilt, nicht was Kael weiß)", "status": P})
        if row.get("reader"):
            new["wissen"].append({"wer": "Leser", "fakt": row["reader"], "seit": n, "quelle": "Plan/storyform/development.json reader", "status": P})
        # the hand knowledge table
        for col, cell in table.get(n, {}).items():
            wer = "AEGIS" if cell.startswith("AE") else "Leser" if cell.startswith("L:") else "Kael"
            new["wissen"].append({"wer": wer, "fakt": f"[{col}] {cell}", "seit": n, "quelle": "Plan/runs/storyform-2026-10-06/wissenstabelle.md", "status": P})
        reg = {"kapitel": n, "status": "proposal", "provenance": f"seeded {today} by continuity.py seed from kanon.md, weave.json, anteile.json, clock-b.json, development.json, the treatment and the 2026-10-06 tables; approved rows survive a reseed",
               **{t: kept[t] + new[t] for t in TABLES}}
        save(reg, folder)
        n_rows += sum(len(new[t]) for t in TABLES)
    return n_rows


def show(n: int, folder: Path | None = None) -> str:
    st = state_at(n, folder)
    out = [f"# Kontinuität zu Beginn von Kap {n}", ""]
    for t in TABLES:
        out.append(f"## {t} · {len(st[t])}")
        for r in st[t]:
            if t == "wissen":
                out.append(f"- [{r.get('status', '?')}] {r.get('wer')}: {r.get('fakt')} (seit Kap {r.get('seit', r['kapitel'])}; {r.get('quelle', '')})")
            elif t == "zeit":
                out.append(f"- [{r.get('status', '?')}] Kap {r['kapitel']} {r.get('was')}: {r.get('wert')} ({r.get('quelle', '')})")
            elif t == "zahlen":
                out.append(f"- [{r.get('status', '?')}] {r.get('name')} = {r.get('wert')} (Kap {r['kapitel']}; {r.get('quelle', '')})")
            else:
                out.append(f"- [{r.get('status', '?')}] {r.get('name')} ({r.get('art')}, seit Kap {r.get('seit', r['kapitel'])}; {r.get('quelle', '')})" + (f" — {r['hinweis']}" if r.get("hinweis") else ""))
        out.append("")
    out.append(f"## noch nicht eingetreten · {len(st['later'])}")
    for r in st["later"]:
        out.append(f"- {r.get('name') or r.get('fakt')} (ab Kap {r['seit']}, {r['tabelle']})")
    return "\n".join(out)


def register_problems(folder: Path | None = None) -> list[str]:
    out = []
    for p in sorted((folder or FOLDER).glob("kap-*.json")):
        try:
            reg = json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            out.append(f"{p.name}: not JSON ({e})")
            continue
        if set(TABLES) - set(reg):
            out.append(f"{p.name}: lacks {', '.join(sorted(set(TABLES) - set(reg)))}")
            continue
        if reg.get("kapitel") != int(p.stem.split("-")[1]):
            out.append(f"{p.name}: kapitel {reg.get('kapitel')} is not the file's")
        for t in TABLES:
            for i, r in enumerate(reg[t]):
                if r.get("status") not in ("proposal", "kanon", "approved"):
                    out.append(f"{p.name} {t}[{i}]: status {r.get('status')!r}")
                if not r.get("quelle"):
                    out.append(f"{p.name} {t}[{i}]: no quelle")
                if t == "dinge" and not r.get("name") or t == "zahlen" and not (r.get("name") and "wert" in r) or t == "wissen" and not (r.get("wer") and r.get("fakt")):
                    out.append(f"{p.name} {t}[{i}]: incomplete row")
    return out


# --- selftest -------------------------------------------------------------------------------

def selftest() -> int:
    results = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        folder = root / "kontinuitaet"
        folder.mkdir()
        save({"kapitel": 0, "status": "proposal", "provenance": "t", "wissen": [
            {"wer": "Kael", "fakt": "Junas Name", "seit": 11, "marker": ["Juna"], "quelle": "W7", "status": "proposal"}],
            "zeit": [], "zahlen": [{"name": "Abwärmebudget", "wert": "71 %", "einheit": "%", "quelle": "clock-b", "status": "proposal"}],
            "dinge": [{"name": "Mara", "art": "figur", "seit": 7, "quelle": "T", "status": "proposal"},
                      {"name": "KW1", "art": "welt", "seit": 1, "quelle": "weave", "status": "kanon"}]}, folder)
        save({"kapitel": 1, "status": "proposal", "provenance": "t", "wissen": [], "zeit": [{"was": "Lage", "wert": "Ein Arbeitstag", "quelle": "dev", "status": "proposal"}],
              "zahlen": [{"name": "Zuweisung", "wert": "37", "einheit": "", "quelle": "T", "status": "approved"}], "dinge": []}, folder)
        st = state_at(1, folder)
        results.append(("the state at Kap 1 holds KW1, the reserve and the day, and keeps Mara and Juna for later",
                        [r["name"] for r in st["dinge"]] == ["KW1"] and len(st["zahlen"]) == 2 and len(st["zeit"]) == 1
                        and sorted(r.get("name") or r.get("fakt") for r in st["later"]) == ["Junas Name", "Mara"]))
        st7 = state_at(7, folder)
        results.append(("at Kap 7 Mara has entered", any(r["name"] == "Mara" for r in st7["dinge"]) and not any(r.get("name") == "Mara" for r in st7["later"])))
        (root / "kap-01").mkdir()
        d = root / "kap-01" / "szene-1.md"
        d.write_text("# x\n\n---\n\nDie Zuweisung steht bei 37. Das Abwärmebudget liegt bei 71 %.\n", encoding="utf-8")
        results.append(("a draft matching the register has no query", check(d, None, folder) == []))
        d.write_text("---\n\nDie Zuweisung steht bei 41.\n", encoding="utf-8")
        f = check(d, None, folder)
        results.append(("a different value for a named number is a query naming both", any(x["tabelle"] == "zahlen" and x["name"] == "Zuweisung" and "41" in x["entwurf"] and "37" in x["register"] for x in f)))
        d.write_text("---\n\nMara sitzt auf der Bank. Juna ruft an.\n", encoding="utf-8")
        f = check(d, None, folder)
        results.append(("a figure before its chapter is a query", any(x["tabelle"] == "dinge" and x["name"] == "Mara" and "Kap 7" in x["register"] for x in f)))
        results.append(("knowledge before its chapter is a query", any(x["tabelle"] == "wissen" and x["name"] == "Juna" and "Kap 11" in x["register"] for x in f)))
        f = check(d, 12, folder)
        results.append(("the same draft as Kap 12 raises neither", f == []))
        results.append(("the register check accepts the fixture", register_problems(folder) == []))
        (folder / "kap-02.json").write_text('{"kapitel": 3, "wissen": [{"wer": "Kael"}], "zeit": [], "zahlen": [], "dinge": [{"name": "x", "quelle": "q", "status": "maybe"}]}', encoding="utf-8")
        probs = register_problems(folder)
        results.append(("the register check names a wrong chapter, an incomplete row, a bad status", any("not the file's" in x for x in probs) and any("incomplete" in x for x in probs) and any("status 'maybe'" in x for x in probs)))
        results.append(("show prints every table and what is still to come", "## zahlen · 2" in show(1, folder) and "Mara (ab Kap 7" in show(1, folder)))
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
    if verb == "seed":
        n = seed(force="--force" in rest)
        print(f"seeded {n} proposal row(s) into {FOLDER.relative_to(ROOT)}/")
        return 0
    if verb == "show" and rest:
        print(show(int(re.sub(r"\D", "", rest[0]))))
        return 0
    if verb == "check" and rest:
        findings = check(Path(rest[0]), int(opt("--kap")) if opt("--kap") else None)
        if "--json" in rest:
            print(json.dumps(findings, ensure_ascii=False, indent=1))
        else:
            for f in findings:
                print(f"query {f['tabelle']:7} Absatz {f['absatz']:>3}  {f['frage']}")
            print(f"{len(findings)} query(ies); none is a failure — which version holds is the author's")
        return 0
    if verb == "register":
        probs = register_problems()
        for p in probs:
            print("FAIL  " + p)
        files = sorted(FOLDER.glob("kap-*.json"))
        rows_n = sum(len(json.loads(p.read_text(encoding="utf-8")).get(t, [])) for p in files for t in TABLES if p.exists())
        print(f"{len(files)} chapter file(s), {rows_n} row(s), {len(probs)} problem(s)")
        return 1 if probs else 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
