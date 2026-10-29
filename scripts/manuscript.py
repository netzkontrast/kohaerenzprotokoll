"""The manuscript: scenes with their status, the checks before approval, approval by the author's words, the book as one file.

Decision 030 (2026-10-26): a session writes a scene on beats the author approved; the author marks it per paragraph
in the app and edits it; approval is the author's words, recorded in `Manuscript/kanon.md`. A chapter in the pilot
is 3,000–5,000 words (W16), so a chapter is a sequence of scenes.

A scene is `Manuscript/kap-NN/szene-N-<slug>.md`:

    ---
    kapitel: 1
    szene: 1
    titel: Das Licht
    status: beats | entwurf | redigiert | freigegeben
    beats_on: 2026-10-26          # the date the author approved the beats
    beats_words: "…"              # the author's words on the beats
    briefing: <inputs_hash>       # the briefing the scene was written on
    geprueft: 2026-10-27 regeln 0 Fehler 3 Rückfragen · kontinuität 1 Rückfrage   # the last check, on this prose
    geprueft_hash: <sha256 of the prose at the check>
    freigegeben: 2026-10-28       # only with freigabe_words
    freigabe_words: "…"
    ---
    > Beats (freigegeben 2026-10-26): …the approved beats, verbatim…

    ---

    The prose.

Everything above the second `---` is the scene's head; `prose_rules.prose_of` strips it, so the checks run on
the prose alone. The beats are the only text the session writes before the scene, and they are the author's once
approved.

Usage:
    python3 scripts/manuscript.py status                          # the grid Kap 0–40: briefing, scenes, words, approvals
    python3 scripts/manuscript.py beats kap-NN N --words "…" --beats "…" [--titel "…"]   # a new scene on approved beats; refuses without a current briefing
    python3 scripts/manuscript.py check kap-NN N                  # prose_rules and continuity over the prose; recorded in the head
    python3 scripts/manuscript.py approve kap-NN N --words "…"    # refuses: briefing behind, checks unrun or stale, a rule failure
    python3 scripts/manuscript.py build [--with-drafts]           # Plan/derived/buch.md: the approved scenes in order
    python3 scripts/manuscript.py findings kap-NN                 # the writing skills' findings on the chapter
    python3 scripts/manuscript.py verify                          # every scene file well formed; kanon's approved chapters exist (CI)
    python3 scripts/manuscript.py selftest

What `approve` writes: the scene's head, and — when every scene of the chapter is approved — a line under
`## Freigegebene Kapitel` in `Manuscript/kanon.md` with the files, the words and the author's words. It never writes
prose, and it does not add to the continuity register: what an approved scene establishes is a judgement, written
into `Manuscript/kontinuitaet/kap-NN.json` as `status: approved` rows by the session that approved it, with the
scene as `quelle`.
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
sys.path.insert(0, str(ROOT / "scripts"))
MANUSCRIPT = ROOT / "Manuscript"
KANON = MANUSCRIPT / "kanon.md"
WRITING = ROOT / "Plan" / "runs" / "writing"
BOOK = ROOT / "Plan" / "derived" / "buch.md"
STATUSES = ("beats", "entwurf", "redigiert", "freigegeben")
WORDS = (3000, 5000)  # W16, the pilot


def folder_of(n: int, base: Path | None = None) -> Path:
    return (base or MANUSCRIPT) / f"kap-{n:02d}"


def slug(text: str) -> str:
    t = text.lower().translate(str.maketrans("äöüß", "aous")).replace("ae", "ae")
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t[:40] or "szene"


def read_scene(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    head, body = {}, text
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        for line in text[4:end].split("\n"):
            if ":" in line:
                k, _, v = line.partition(":")
                head[k.strip()] = re.sub(r"\s+#.*$", "", v).strip().strip('"')
        body = text[end + 5:]
    import prose_rules
    prose = prose_rules.prose_of(text)
    m = re.search(r"^> Beats \([^)]*\):\s*(.*?)(?=\n\n---|\Z)", body, re.S | re.M)
    return {"path": path, "head": head, "body": body, "prose": prose, "beats": (m.group(1).strip() if m else ""),
            "words": len(re.findall(r"\w+", prose)), "prose_hash": hashlib.sha256(prose.encode("utf-8")).hexdigest()}


def write_scene(path: Path, head: dict, body: str) -> None:
    lines = ["---"] + [f"{k}: {v}" for k, v in head.items() if v not in (None, "")] + ["---"]
    path.write_text("\n".join(lines) + "\n" + body.lstrip("\n"), encoding="utf-8")


def scenes(n: int, base: Path | None = None) -> list[dict]:
    return [read_scene(p) for p in sorted(folder_of(n, base).glob("szene-*.md"))]


# --- the verbs -------------------------------------------------------------------------

def beats(n: int, k: int, words: str, beats_text: str, titel: str = "", today: str | None = None,
          base: Path | None = None, briefing_status=None) -> Path:
    if not words.strip():
        raise SystemExit("the beats are approved by the author's words: --words is required (P0)")
    if not beats_text.strip():
        raise SystemExit("--beats: the beats the author approved, verbatim")
    import brief
    st, why = (briefing_status or brief.status)(n)
    if st != "current":
        raise SystemExit(f"refused: the briefing of Kap {n} is {st} ({why}) — a scene is written only on a current briefing")
    folder = folder_of(n, base)
    folder.mkdir(parents=True, exist_ok=True)
    if any(read_scene(p)["head"].get("szene") == str(k) for p in folder.glob("szene-*.md")):
        raise SystemExit(f"refused: Kap {n} already has a scene {k}")
    today = today or datetime.date.today().isoformat()
    bh = re.search(r"^inputs_hash: (\w+)$", (folder / "briefing.md").read_text(encoding="utf-8"), re.M)
    path = folder / f"szene-{k}-{slug(titel or beats_text[:40])}.md"
    head = {"kapitel": n, "szene": k, "titel": titel or f"Szene {k}", "status": "beats", "beats_on": today,
            "beats_words": '"' + words.strip().replace('"', "'") + '"', "briefing": bh.group(1) if bh else ""}
    body = f"> Beats (freigegeben {today}): {beats_text.strip()}\n\n---\n\n"
    write_scene(path, head, body)
    return path


def scene_path(n: int, k: int, base: Path | None = None) -> Path:
    for p in sorted(folder_of(n, base).glob("szene-*.md")):
        if read_scene(p)["head"].get("szene") == str(k):
            return p
    raise SystemExit(f"no scene {k} in Kap {n}")


def check(n: int, k: int, today: str | None = None, base: Path | None = None, duties_fn=None) -> dict:
    import continuity
    import prose_rules
    if duties_fn is None:
        import brief
        duties_fn = brief.duties_of
    path = scene_path(n, k, base)
    sc = read_scene(path)
    if not sc["prose"].strip():
        raise SystemExit(f"{path.name}: no prose yet")
    rf = prose_rules.check(path, n)
    cf = continuity.check(path, n)
    # a decided sentence naming this scene is never judged answered by code: it is read beside the prose (F10, F11)
    du = duties_fn(n, k)
    fails = sum(1 for f in rf if f["severity"] == "fail")
    today = today or datetime.date.today().isoformat()
    sc["head"]["geprueft"] = f"{today} regeln {fails} Fehler {len(rf) - fails} Rückfragen · kontinuität {len(cf)} Rückfragen · pflichten {len(du)} zu lesen"
    sc["head"]["geprueft_hash"] = sc["prose_hash"]
    if sc["head"].get("status") == "beats":
        sc["head"]["status"] = "entwurf"
    write_scene(path, sc["head"], sc["body"])
    return {"rules": rf, "continuity": cf, "duties": du, "fails": fails, "words": sc["words"]}


def approve(n: int, k: int, words: str, today: str | None = None, base: Path | None = None, kanon: Path | None = None,
            briefing_status=None) -> dict:
    if not words.strip():
        raise SystemExit("an approval records the author's words verbatim: --words is required (P0)")
    import brief
    path = scene_path(n, k, base)
    sc = read_scene(path)
    st, why = (briefing_status or brief.status)(n)
    if st != "current":
        raise SystemExit(f"refused: the briefing of Kap {n} is {st} ({why})")
    if sc["head"].get("geprueft_hash") != sc["prose_hash"]:
        raise SystemExit(f"refused: the prose changed since the last check — run manuscript.py check kap-{n:02d} {k}")
    m = re.search(r"regeln (\d+) Fehler", sc["head"].get("geprueft", ""))
    if not m or int(m.group(1)):
        raise SystemExit("refused: a confirmed rule fails, or the check was not run")
    today = today or datetime.date.today().isoformat()
    sc["head"].update(status="freigegeben", freigegeben=today, freigabe_words='"' + words.strip().replace('"', "'") + '"')
    write_scene(path, sc["head"], sc["body"])
    all_scenes = scenes(n, base)
    chapter_done = all(s["head"].get("status") == "freigegeben" for s in all_scenes)
    if chapter_done:
        total = sum(s["words"] for s in all_scenes)
        line = (f"- Kap {n}: " + ", ".join(f"`{s['path'].relative_to(ROOT).as_posix() if s['path'].is_relative_to(ROOT) else s['path'].name}`" for s in all_scenes)
                + f" — {total} Wörter, freigegeben {today}: „{words.strip()}“")
        kp = kanon or KANON
        text = kp.read_text(encoding="utf-8")
        text = re.sub(r"(## Freigegebene Kapitel\n\n)(Keines\.[^\n]*\n)?", lambda mm: mm.group(1), text, count=1)
        text = text.replace("## Freigegebene Kapitel\n\n", "## Freigegebene Kapitel\n\n" + line + "\n", 1) if line not in text else text
        kp.write_text(text, encoding="utf-8")
    return {"kapitel": n, "szene": k, "status": "freigegeben", "on": today, "words": words.strip(), "chapter_done": chapter_done}


def build(with_drafts: bool = False, base: Path | None = None, out: Path | None = None) -> Path:
    import brief
    parts = ["# Kohärenz Protokoll — das Buch, Stand " + datetime.date.today().isoformat(), "",
             "Abgeleitet von `manuscript.py build`: die freigegebenen Szenen in Reihenfolge" + (", dazu die Entwürfe, so markiert" if with_drafts else "") + ". Keine Autorität; die Dateien in `Manuscript/kap-NN/` sind es.", ""]
    total = 0
    for n in range(0, 41):
        sc = scenes(n, base)
        shown = [s for s in sc if s["head"].get("status") == "freigegeben" or (with_drafts and s["prose"].strip())]
        if not shown:
            continue
        title, _ = brief.treatment_paragraph(n)
        parts += [f"## Kap {n}" + (f" — {title}" if title else ""), ""]
        for s in shown:
            if s["head"].get("status") != "freigegeben":
                parts += [f"*[Entwurf, Szene {s['head'].get('szene')}, {s['head'].get('status')}]*", ""]
            parts += [s["prose"].strip(), ""]
            total += s["words"]
    parts += [f"---", f"{total} Wörter."]
    out = out or BOOK
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(parts) + "\n", encoding="utf-8")
    return out


def findings(n: int) -> list[Path]:
    return sorted(p for p in WRITING.rglob("*.md") if p.parent.name == f"kap-{n:02d}" or re.search(rf"\bkap-?0?{n}\b", p.stem))


def status_grid(base: Path | None = None) -> str:
    import brief
    out = ["Kap  Titel                          Briefing  Szenen (beats/entwurf/redigiert/frei)  Wörter   Weichen offen"]
    import weiche
    open_by: dict[int, int] = {}
    for wid, p in weiche.sheets().items():
        if weiche.frontmatter(p.read_text(encoding="utf-8")).get("status") == "beantwortet":
            continue
        ch = weiche.chapters_of(wid)
        for c in set(ch["development"]) | set(ch["treatment"]) | set(ch["sheet"]):
            open_by[c] = open_by.get(c, 0) + 1
    for n in range(0, 41):
        title, _ = brief.treatment_paragraph(n)
        st, _ = brief.status(n) if (folder_of(n, base) / "briefing.md").exists() else ("none", "")
        sc = scenes(n, base)
        counts = [sum(1 for s in sc if s["head"].get("status") == x) for x in STATUSES]
        words = sum(s["words"] for s in sc)
        flag = "" if not sc else (" ✓" if WORDS[0] <= words <= WORDS[1] else " (W16: 3000–5000)")
        out.append(f"{n:>3}  {title[:30]:30} {st:9} {'/'.join(map(str, counts)):36} {words:>6}{flag:18} {open_by.get(n, 0)}")
    return "\n".join(out)


def verify(base: Path | None = None, kanon: Path | None = None) -> list[str]:
    out = []
    for n in range(0, 41):
        for s in scenes(n, base):
            h, name = s["head"], s["path"].name
            for key in ("kapitel", "szene", "titel", "status", "beats_on", "beats_words", "briefing"):
                if not h.get(key):
                    out.append(f"{name}: lacks {key}")
            if h.get("status") not in STATUSES:
                out.append(f"{name}: status {h.get('status')!r}")
            if h.get("kapitel") != str(n):
                out.append(f"{name}: kapitel {h.get('kapitel')} is not the folder's")
            if not s["beats"]:
                out.append(f"{name}: no beats block")
            if h.get("status") == "freigegeben" and not (h.get("freigegeben") and h.get("freigabe_words")):
                out.append(f"{name}: freigegeben without date or words")
            if h.get("status") in ("redigiert", "freigegeben") and h.get("geprueft_hash") != s["prose_hash"]:
                out.append(f"{name}: {h.get('status')}, and the prose changed since its check")
    kp = kanon or KANON
    if kp.exists():
        sect = re.search(r"## Freigegebene Kapitel\n(.*?)(?=^## |\Z)", kp.read_text(encoding="utf-8"), re.S | re.M)
        for f in re.findall(r"`(Manuscript/kap-\d+/szene-[^`]+\.md)`", sect.group(1) if sect else ""):
            if not (ROOT / f).exists():
                out.append(f"kanon.md approves {f}, which does not exist")
    return out


# --- selftest --------------------------------------------------------------------------------

def selftest() -> int:
    results = []
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        kanon = base / "kanon.md"
        kanon.write_text("# Kanon\n\n## Entscheidungen\n\n| id | Datum | Was gilt | Wo es steht |\n|---|---|---|---|\n\n## Freigegebene Kapitel\n\nKeines. Ein Kapitel kommt hierher, wenn du eine Fassung freigibst.\n\n## Weiter\n", encoding="utf-8")
        folder_of(1, base).mkdir(parents=True)
        (folder_of(1, base) / "briefing.md").write_text("---\ninputs_hash: abc123\n---\n", encoding="utf-8")
        current = lambda n: ("current", "current")  # noqa: E731
        behind = lambda n: ("behind", "an input changed")  # noqa: E731
        try:
            beats(1, 1, "", "x", base=base, briefing_status=current)
            results.append(("beats without the author's words are refused", False))
        except SystemExit as e:
            results.append(("beats without the author's words are refused", "--words" in str(e)))
        try:
            beats(1, 1, "ja", "x", base=base, briefing_status=behind)
            results.append(("beats on a stale briefing are refused", False))
        except SystemExit as e:
            results.append(("beats on a stale briefing are refused", "behind" in str(e)))
        p = beats(1, 1, "ja, so", "Kael erwacht; die Hand hält die andere; 07:02.", "Das Licht", "2026-10-26", base, current)
        sc = read_scene(p)
        results.append(("a scene file is created with beats, status and the briefing hash",
                        p.name == "szene-1-das-licht.md" and sc["head"]["status"] == "beats" and sc["beats"].startswith("Kael erwacht")
                        and sc["head"]["briefing"] == "abc123" and sc["prose"] == "" and sc["head"]["beats_words"] == 'ja, so'))
        try:
            beats(1, 1, "ja", "y", base=base, briefing_status=current)
            results.append(("a second scene 1 is refused", False))
        except SystemExit as e:
            results.append(("a second scene 1 is refused", "already" in str(e)))
        try:
            approve(1, 1, "frei", base=base, kanon=kanon, briefing_status=current)
            results.append(("approval before a check is refused", False))
        except SystemExit as e:
            results.append(("approval before a check is refused", "check" in str(e)))
        # prose, then check (the live rules and register: the fixture prose is clean)
        text = p.read_text(encoding="utf-8")
        p.write_text(text + "Das Licht ist schon da, als ich erwache. Ich ziehe die linke Hand weg.\n", encoding="utf-8")
        duty = lambda n, k: [{"scene": 1, "id": "W99", "sentence": "In Szene 1 steht der Abschnitt auf der Liste.", "context": ""}] if k == 1 else []  # noqa: E731
        r = check(1, 1, "2026-10-27", base, duties_fn=duty)
        sc = read_scene(p)
        results.append(("check records the run on the prose and moves beats to entwurf", r["fails"] == 0 and sc["head"]["status"] == "entwurf"
                        and sc["head"]["geprueft_hash"] == sc["prose_hash"] and "regeln 0 Fehler" in sc["head"]["geprueft"]))
        results.append(("a decided sentence naming the scene comes back as a duty to read, on clean prose too (F10, F11)",
                        [d["id"] for d in r["duties"]] == ["W99"] and "pflichten 1 zu lesen" in sc["head"]["geprueft"]))
        p.write_text(p.read_text(encoding="utf-8") + "\nNoch ein Satz.\n", encoding="utf-8")
        try:
            approve(1, 1, "frei", base=base, kanon=kanon, briefing_status=current)
            results.append(("approval after an edit without a new check is refused", False))
        except SystemExit as e:
            results.append(("approval after an edit without a new check is refused", "changed since" in str(e)))
        check(1, 1, "2026-10-27", base, duties_fn=duty)
        try:
            approve(1, 1, "", base=base, kanon=kanon, briefing_status=current)
            results.append(("approval without words is refused", False))
        except SystemExit as e:
            results.append(("approval without words is refused", "--words" in str(e)))
        row = approve(1, 1, "Freigegeben, so bleibt es.", "2026-10-28", base, kanon, current)
        sc = read_scene(p)
        results.append(("approval writes status, date and words, and the chapter line into kanon", row["chapter_done"] and sc["head"]["status"] == "freigegeben"
                        and "Freigegeben, so bleibt es." in kanon.read_text(encoding="utf-8") and "Keines." not in kanon.read_text(encoding="utf-8")
                        and "## Weiter" in kanon.read_text(encoding="utf-8")))
        results.append(("verify accepts the fixture", verify(base, kanon) == [] or [x for x in verify(base, kanon) if "does not exist" not in x] == []))
        p.write_text(p.read_text(encoding="utf-8").replace("status: freigegeben", "status: fertig"), encoding="utf-8")
        results.append(("verify names an unknown status", any("status 'fertig'" in x for x in verify(base, kanon))))
        p.write_text(p.read_text(encoding="utf-8").replace("status: fertig", "status: freigegeben") + "\nGeändert.\n", encoding="utf-8")
        results.append(("verify names an approved scene whose prose moved", any("changed since its check" in x for x in verify(base, kanon))))
        out = build(False, base, base / "buch.md")
        results.append(("build writes the approved scenes with the chapter heading and the count", "## Kap 1" in out.read_text(encoding="utf-8") and "Das Licht ist schon da" in out.read_text(encoding="utf-8")))
        results.append(("the slug is ascii and bounded", slug("Über die Kälte, 07:02 — ein Anfang") == "uber-die-kalte-07-02-ein-anfang"))
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

    def kap(x: str) -> int:
        return int(re.sub(r"\D", "", x))

    if verb == "selftest":
        return selftest()
    if verb == "status":
        print(status_grid())
        return 0
    if verb == "beats" and len(rest) >= 2:
        p = beats(kap(rest[0]), int(rest[1]), opt("--words"), opt("--beats"), opt("--titel"))
        print(f"wrote {p.relative_to(ROOT)} — status beats; the session writes the prose after the second ---")
        return 0
    if verb == "check" and len(rest) >= 2:
        r = check(kap(rest[0]), int(rest[1]))
        for f in r["rules"]:
            print(f"{f['severity']:5} {f['rule']:5} Absatz {f['absatz']:>3}  {f['wort']!s:28} {f['stelle']}")
        for f in r["continuity"]:
            print(f"query {f['tabelle']:7} Absatz {f['absatz']:>3}  {f['frage']}")
        for d in r["duties"]:
            print(f"duty  {d['id']:7} Szene {d['scene']}: {d['sentence']} — welche Zeile antwortet? (der Autor liest)")
        print(f"{r['words']} Wörter; {r['fails']} Fehler, {len(r['rules']) - r['fails']} Regel-Rückfragen, {len(r['continuity'])} Kontinuitäts-Rückfragen, {len(r['duties'])} Pflichten zu lesen")
        return 1 if r["fails"] else 0
    if verb == "approve" and len(rest) >= 2:
        print(json.dumps(approve(kap(rest[0]), int(rest[1]), opt("--words")), ensure_ascii=False))
        return 0
    if verb == "build":
        print(f"wrote {build('--with-drafts' in rest).relative_to(ROOT)}")
        return 0
    if verb == "findings" and rest:
        for p in findings(kap(rest[0])):
            print(p.relative_to(ROOT))
        return 0
    if verb == "verify":
        probs = verify()
        for x in probs:
            print("FAIL  " + x)
        n = sum(len(scenes(k)) for k in range(0, 41))
        print(f"{n} scene(s), {len(probs)} problem(s)")
        return 1 if probs else 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
