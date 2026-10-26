"""The prose-rule register: every rule the sources or the author set for the prose, with its status, and the checks.

The sources are full of rules for the prose — the first sentence of Kap 1, no AEGIS voice in Kap 1, no metaphors in
KW1, „die Amnesie wird nie erwähnt“, cold ozone, the ten ground rules of the Projekt-Anleitung. Decision 006 says
none of them binds until the author confirms it; decision 030 (2026-10-26) says they go into **a register with
status, each confirmed or rejected by the author's words**, and the confirmed, mechanically checkable ones are
checked by code. The standing rules of the author's instructions (early names never written, no gendered pronoun
for a figure, the trauma symbol never written) are in the register as confirmed from the start.

    Manuscript/regeln.jsonl   one row per rule:
      {"id": "R03", "text": "<German>", "source": "<^[slug.md:Lnn] | Plan/weichen/w7-schleier.md | the author, 2026-10-16>",
       "scope": {"kapitel": [1]} | {"kernwelt": "KW1"} | {"route": "hard-a"} | "alle",
       "status": "offen" | "bestätigt" | "verworfen" | "ersetzt", "words": "<the author's words>", "on": "<date>", "by": "author",
       "check": null | {"kind": "<CHECKS key>", ...params}, "added": "<date>, <who>"}

A violation of a `bestätigt` rule **fails**; of an `offen` one it is a **query**; a `verworfen` or `ersetzt` rule
is not checked. No check edits a draft, and no check decides a rule: `confirm` and `reject` take the author's words.

Checks (`CHECKS`), each over the prose of one draft (frontmatter and the session's head note stripped):

| kind | finds |
|---|---|
| `fruehe-namen` | an early name or a name the corpus gives after „ehem.“ (read, never written) |
| `kernwunde` | the trauma symbol's words (only „Kernwunde“ is written) |
| `pronomen-figuren` | a gendered pronoun within a few words after Kael, Juna, AEGIS or a part's name — a query, since German needs reading |
| `erstsatz` | the first sentence is not `line` |
| `wort-verbot` | one of `words` written (whole word, any case) |
| `wort-anzahl` | `word` written other than `n` times |
| `erzaehlform` | the narration drifts from first person present: more third-person past markers than first-person present ones |

Usage:
    python3 scripts/rules.py list [--kap N] [--status offen]      # the register, in scope of a chapter
    python3 scripts/rules.py show <id>
    python3 scripts/rules.py confirm <id> --words "<the author's words>" [--by author]
    python3 scripts/rules.py reject <id> --words "<the author's words>"
    python3 scripts/rules.py check <draft.md> [--kap N] [--json]  # the checks of every rule in scope; exit 1 on a failure
    python3 scripts/rules.py register                             # the register itself: ids, statuses, sources, checks (CI)
    python3 scripts/rules.py selftest
"""

from __future__ import annotations

import datetime
import json
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
REGISTER = ROOT / "Manuscript" / "regeln.jsonl"
WEAVE = ROOT / "Plan" / "storyform" / "weave.json"
ANTEILE = ROOT / "Plan" / "storyform" / "anteile.json"
STATUSES = ("offen", "bestätigt", "verworfen", "ersetzt")
FIGURES = ("Kael", "Juna", "AEGIS")
# Read, never written (decision 028 and the author's rules of 2026-10): split so a search for the names misses this file.
BARRED = re.compile("|".join(("Mich" "ael", "Jul" "ia", "Sha" "dow", "Lost " "One", "Isab" "ella", "Alex" "ander",
                              "Ste" "fan", r"\bDa" r"ta\b", "Wächt" "erin", "Der " "Kleine", "Beobachter/" "Kritiker")))
TRAUMA = re.compile("|".join(("Kis" "sen", r"\bGe" r"lb\b", r"\bge" r"lbe[nrs]?\b")), re.I)
PRONOUN = re.compile(r"\b(er|sie|ihn|ihm|ihr|ihre|ihren|ihrer|ihres|sein|seine|seinen|seiner|seines)\b")
FIRST_PRESENT = re.compile(r"\b(ich|mich|mir|mein|meine|meinen|meiner)\b", re.I)
THIRD_PAST = re.compile(r"\b(war|hatte|sagte|ging|kam|sah|wusste|dachte|stand|lag|nahm|blieb|wurde)\b")
SENTENCE_END = re.compile(r"(?<=[.!?…])\s+")


# --- the register ---------------------------------------------------------------

def rows(path: Path | None = None) -> list[dict]:
    path = path or REGISTER
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def save(items: list[dict], path: Path | None = None) -> None:
    (path or REGISTER).write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in items), encoding="utf-8")


def chapter_of(path: Path) -> int | None:
    m = re.search(r"kap-(\d+)", str(path))
    return int(m.group(1)) if m else None


def world_of(n: int, weave: dict | None = None) -> str | None:
    weave = weave if weave is not None else (json.loads(WEAVE.read_text(encoding="utf-8")) if WEAVE.exists() else {})
    for w in weave.get("worlds", []):
        if w["chapters"][0] <= n <= w["chapters"][1]:
            return w["world"]
    return None


def route_of(n: int, weave: dict | None = None) -> str | None:
    weave = weave if weave is not None else (json.loads(WEAVE.read_text(encoding="utf-8")) if WEAVE.exists() else {})
    return (weave.get("chapters", {}).get(str(n)) or {}).get("route")


def in_scope(rule: dict, kap: int | None, weave: dict | None = None) -> bool:
    scope = rule.get("scope", "alle")
    if scope == "alle":
        return True
    if kap is None:
        return False
    if "kapitel" in scope:
        return kap in scope["kapitel"]
    if "kernwelt" in scope:
        return world_of(kap, weave) == scope["kernwelt"]
    if "route" in scope:
        return route_of(kap, weave) == scope["route"]
    return False


def scope_text(scope) -> str:
    if scope == "alle":
        return "alle Kapitel"
    if "kapitel" in scope:
        ks = scope["kapitel"]
        return "Kap " + (f"{ks[0]}–{ks[-1]}" if len(ks) > 2 and ks == list(range(ks[0], ks[-1] + 1)) else ", ".join(map(str, ks)))
    if "kernwelt" in scope:
        return scope["kernwelt"]
    if "route" in scope:
        return {"hard-a": "Kaels Kapitel (hard-a)", "hard-b": "AEGIS' Kapitel (hard-b)", "bridge": "Brückenkapitel"}.get(scope["route"], scope["route"])
    return str(scope)


# --- the prose of a draft ---------------------------------------------------------

def prose_of(text: str) -> str:
    """A draft without its frontmatter and without the session's head note (heading and blockquote before the first rule)."""
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end > 0:
            text = text[end + 5:]
    lines = text.split("\n")
    i = 0
    while i < len(lines) and (not lines[i].strip() or lines[i].startswith("#") or lines[i].startswith(">")):
        i += 1
    if i < len(lines) and lines[i].strip() == "---":
        i += 1
    return "\n".join(lines[i:]).strip()


def paragraphs(prose: str) -> list[tuple[int, str]]:
    """(1-based paragraph number, text) for every non-blank paragraph."""
    out, n = [], 0
    for block in re.split(r"\n\s*\n", prose):
        if block.strip():
            n += 1
            out.append((n, block.strip()))
    return out


# --- the checks --------------------------------------------------------------------

def _find_words(prose: str, words: list[str]) -> list[dict]:
    pat = re.compile(r"(?<![\wÄÖÜäöüß])(?:" + "|".join(re.escape(w) for w in words) + r")(?![\wÄÖÜäöüß])", re.I)
    out = []
    for no, para in paragraphs(prose):
        for m in pat.finditer(para):
            out.append({"absatz": no, "wort": m.group(0), "stelle": para[max(0, m.start() - 40):m.end() + 40]})
    return out


def check_fruehe_namen(prose: str, rule: dict) -> list[dict]:
    out = []
    for no, para in paragraphs(prose):
        for m in BARRED.finditer(para):
            out.append({"absatz": no, "wort": "[ein früherer Name]", "stelle": para[max(0, m.start() - 40):m.start()] + "[…]"})
    return out


def check_kernwunde(prose: str, rule: dict) -> list[dict]:
    out = []
    for no, para in paragraphs(prose):
        for m in TRAUMA.finditer(para):
            out.append({"absatz": no, "wort": "[das Symbol]", "stelle": para[max(0, m.start() - 40):m.start()] + "[…]"})
    return out


def check_pronomen(prose: str, rule: dict) -> list[dict]:
    names = list(FIGURES) + rule.get("names", [])
    pat = re.compile(r"\b(" + "|".join(re.escape(n) for n in names) + r")\b((?:\W+\w+){0,8}?)\W+" + PRONOUN.pattern)
    out = []
    for no, para in paragraphs(prose):
        for m in pat.finditer(para):
            out.append({"absatz": no, "wort": m.group(m.lastindex), "figur": m.group(1),
                        "stelle": para[max(0, m.start() - 20):m.end() + 20]})
    return out


def check_erstsatz(prose: str, rule: dict) -> list[dict]:
    first = SENTENCE_END.split(prose.strip(), 1)[0].strip() if prose.strip() else ""
    want = rule["line"].strip()
    return [] if first.rstrip(".!?…").lower() == want.rstrip(".!?…").lower() else [{"absatz": 1, "wort": first[:80], "stelle": f"erwartet: {want}"}]


def check_wort_verbot(prose: str, rule: dict) -> list[dict]:
    return _find_words(prose, rule["words"])


def check_wort_anzahl(prose: str, rule: dict) -> list[dict]:
    hits = _find_words(prose, [rule["word"]])
    if len(hits) == rule["n"]:
        return []
    return [{"absatz": h["absatz"], "wort": h["wort"], "stelle": h["stelle"]} for h in hits] or [{"absatz": 0, "wort": rule["word"], "stelle": f"0 mal, erwartet {rule['n']}"}]


def check_erzaehlform(prose: str, rule: dict) -> list[dict]:
    fp, tp = len(FIRST_PRESENT.findall(prose)), len(THIRD_PAST.findall(prose))
    if fp >= tp:
        return []
    return [{"absatz": 0, "wort": f"{fp} Ich-Marker, {tp} Präteritum-Marker", "stelle": "die Erzählform liest sich nicht als Ich/Präsens"}]


QUERY_ONLY = {"pronomen-figuren", "erzaehlform"}  # heuristics: a person reads them
CHECKS = {"fruehe-namen": check_fruehe_namen, "kernwunde": check_kernwunde, "pronomen-figuren": check_pronomen,
          "erstsatz": check_erstsatz, "wort-verbot": check_wort_verbot, "wort-anzahl": check_wort_anzahl,
          "erzaehlform": check_erzaehlform}


def check(path: Path, kap: int | None = None, register: list[dict] | None = None, weave: dict | None = None) -> list[dict]:
    """Every finding of every rule in scope: {rule, status, severity: fail|query, absatz, wort, stelle}."""
    text = path.read_text(encoding="utf-8")
    prose = prose_of(text)
    kap = kap if kap is not None else chapter_of(path)
    out = []
    for rule in register if register is not None else rows():
        if rule.get("status") not in ("offen", "bestätigt") or not rule.get("check") or not in_scope(rule, kap, weave):
            continue
        fn = CHECKS.get(rule["check"]["kind"])
        if not fn:
            continue
        # A pronoun needs reading („sagt sie“ may be the colleague): always a query, never a failure.
        severity = "fail" if rule["status"] == "bestätigt" and rule["check"]["kind"] not in QUERY_ONLY else "query"
        for hit in fn(prose, rule["check"]):
            out.append({"rule": rule["id"], "status": rule["status"], "severity": severity, **hit})
    return out


# --- the verbs ------------------------------------------------------------------------

def set_status(rid: str, status: str, words: str, by: str = "author", today: str | None = None,
               path: Path | None = None) -> dict:
    if not words.strip():
        raise SystemExit("a rule's status is the author's: --words is required (P0, decision 030)")
    items = rows(path)
    for r in items:
        if r["id"] == rid:
            r.update(status=status, words=words, on=today or datetime.date.today().isoformat(), by=by)
            save(items, path)
            return r
    raise SystemExit(f"no rule {rid}")


def register_problems(items: list[dict] | None = None, landed: set[str] | None = None) -> list[str]:
    """What is wrong with the register itself."""
    import quotes
    items = items if items is not None else rows()
    out, seen = [], set()
    for r in items:
        rid = r.get("id", "?")
        if rid in seen:
            out.append(f"{rid}: id repeats")
        seen.add(rid)
        for key in ("id", "text", "source", "scope", "status", "added"):
            if key not in r:
                out.append(f"{rid}: lacks {key}")
        if r.get("status") not in STATUSES:
            out.append(f"{rid}: status {r.get('status')!r} is not one of {', '.join(STATUSES)}")
        if r.get("status") in ("bestätigt", "verworfen") and not (r.get("words") and r.get("on")):
            out.append(f"{rid}: {r.get('status')} without the author's words and date")
        if r.get("check") and r["check"].get("kind") not in CHECKS:
            out.append(f"{rid}: unknown check {r['check'].get('kind')!r}")
        m = re.match(r"\^\[([a-z0-9-]+)\.md:L(\d+)\]", str(r.get("source", "")))
        if m:
            if landed is not None:
                if m.group(1) not in landed:
                    out.append(f"{rid}: cites {m.group(1)}, no landed document")
            elif quotes.source_line(m.group(1), int(m.group(2))) is None:
                out.append(f"{rid}: cites {r['source']}, which is past the end of the document")
        scope = r.get("scope")
        if scope != "alle" and not (isinstance(scope, dict) and len(scope) == 1 and next(iter(scope)) in ("kapitel", "kernwelt", "route")):
            out.append(f"{rid}: scope {scope!r} is neither 'alle' nor one of kapitel, kernwelt, route")
    return out


def listing(kap: int | None = None, status: str | None = None) -> str:
    out = []
    for r in rows():
        if kap is not None and not in_scope(r, kap):
            continue
        if status and r["status"] != status:
            continue
        chk = r["check"]["kind"] if r.get("check") else "—"
        out.append(f"{r['id']:5} {r['status']:10} {scope_text(r['scope']):28} {chk:17} {r['text'][:90]}")
    return "\n".join(out) + (f"\n{len(out)} rule(s)" if out else "no rule")


# --- selftest ----------------------------------------------------------------------------

def selftest() -> int:
    results = []
    early = "Mich" "ael"
    good = ("---\nkapitel: 1\n---\n\n# Kap 1 — Szene 1\n\n> Entwurf einer Sitzung.\n\n---\n\n"
            "Das Licht ist schon da, als ich erwache, und meine linke Hand hält meine rechte.\n\n"
            "Ich ziehe die linke weg. Über der Tür zeigt die Wandfläche die Uhrzeit.\n")
    register = [
        {"id": "R01", "text": "x", "source": "the author", "scope": "alle", "status": "bestätigt", "words": "ja", "on": "2026-10-16", "added": "t",
         "check": {"kind": "fruehe-namen"}},
        {"id": "R02", "text": "x", "source": "the author", "scope": "alle", "status": "bestätigt", "words": "ja", "on": "2026-10-16", "added": "t",
         "check": {"kind": "kernwunde"}},
        {"id": "R03", "text": "x", "source": "the author", "scope": "alle", "status": "bestätigt", "words": "ja", "on": "2026-10-16", "added": "t",
         "check": {"kind": "pronomen-figuren", "names": ["Silas"]}},
        {"id": "L3", "text": "x", "source": "^[doc.md:L1]", "scope": {"kapitel": [1]}, "status": "offen", "added": "t",
         "check": {"kind": "erstsatz", "line": "Das Licht ist schon da, als ich erwache, und meine linke Hand hält meine rechte."}},
        {"id": "L6", "text": "x", "source": "^[doc.md:L1]", "scope": {"kapitel": [1]}, "status": "offen", "added": "t",
         "check": {"kind": "wort-verbot", "words": ["Wärme", "warm"]}},
        {"id": "L7", "text": "x", "source": "^[doc.md:L1]", "scope": {"kernwelt": "KW1"}, "status": "offen", "added": "t",
         "check": {"kind": "wort-verbot", "words": ["Knöchel"]}},
        {"id": "T", "text": "x", "source": "Plan/weichen/w7-schleier.md", "scope": {"route": "hard-a"}, "status": "offen", "added": "t",
         "check": {"kind": "wort-verbot", "words": ["Trennungsprotokoll"]}},
        {"id": "E", "text": "x", "source": "the author", "scope": "alle", "status": "offen", "added": "t",
         "check": {"kind": "erzaehlform"}},
        {"id": "V", "text": "x", "source": "the author", "scope": "alle", "status": "verworfen", "words": "nein", "on": "2026-10-16", "added": "t",
         "check": {"kind": "wort-verbot", "words": ["Licht"]}},
    ]
    weave = {"worlds": [{"world": "KW1", "chapters": [1, 13]}], "chapters": {"1": {"route": "hard-a"}, "6": {"route": "hard-b"}}}
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "kap-01").mkdir()
        p = root / "kap-01" / "szene-1.md"

        def run(text, kap=None):
            p.write_text(text, encoding="utf-8")
            return check(p, kap, register, weave)

        f = run(good)
        results.append(("a clean scene in Kap 1 has no finding", f == []))
        results.append(("the chapter is read from the path", chapter_of(p) == 1))
        results.append(("prose_of strips frontmatter and the head note", prose_of(good).startswith("Das Licht")))
        f = run(good.replace("Ich ziehe", f"{early} zieht"))
        results.append(("an early name fails and is not echoed", any(x["rule"] == "R01" and x["severity"] == "fail" and early not in json.dumps(x) for x in f)))
        f = run(good + "\nDas Kis" "sen liegt da.\n")
        results.append(("the trauma symbol fails", any(x["rule"] == "R02" and x["severity"] == "fail" for x in f)))
        f = run(good + "\nSilas kommt, und er bleibt.\n")
        results.append(("a pronoun after a part's name is a query even on a confirmed rule", any(x["rule"] == "R03" and x["figur"] == "Silas" and x["severity"] == "query" for x in f)))
        f = run(good.replace("Das Licht ist schon da, als ich erwache, und meine linke Hand hält meine rechte.", "Ich erwache."))
        results.append(("a different first sentence is a query on the open rule", any(x["rule"] == "L3" and x["severity"] == "query" for x in f)))
        f = run(good + "\nEs wird warm.\n")
        results.append(("a forbidden word in scope is a query", any(x["rule"] == "L6" and x["wort"] == "warm" for x in f)))
        f = run(good + "\nDie Knöchel brennen.\n")
        results.append(("a Kernwelt scope reaches Kap 1", any(x["rule"] == "L7" for x in f)))
        f = run(good + "\nDie Knöchel brennen.\n", kap=14)
        results.append(("a Kernwelt scope stops at Kap 13", not any(x["rule"] == "L7" for x in f)))
        f = run(good + "\nDas Trennungsprotokoll läuft.\n")
        results.append(("a route scope reaches a hard-a chapter", any(x["rule"] == "T" for x in f)))
        f = run(good + "\nDas Trennungsprotokoll läuft.\n", kap=6)
        results.append(("a route scope leaves a hard-b chapter alone", not any(x["rule"] == "T" for x in f)))
        f = run("---\n---\n\nEr war da. Er sagte nichts. Er ging. Sie kam.\n")
        results.append(("third person past is an erzaehlform query", any(x["rule"] == "E" for x in f)))
        f = run(good)
        results.append(("a rejected rule is not checked", not any(x["rule"] == "V" for x in f)))
        reg = root / "r.jsonl"
        save(register, reg)
        set_status("L3", "bestätigt", "ja, der Satz bleibt", "author", "2026-10-26", reg)
        p.write_text(good.replace("Das Licht ist schon da, als ich erwache, und meine linke Hand hält meine rechte.", "Ich erwache."), encoding="utf-8")
        f = check(p, None, rows(reg), weave)
        results.append(("confirm turns a query into a failure", rows(reg)[3]["status"] == "bestätigt"
                        and any(x["rule"] == "L3" and x["severity"] == "fail" for x in f)))
        try:
            set_status("L3", "verworfen", "", "author", None, reg)
            results.append(("a status without the author's words is refused", False))
        except SystemExit as e:
            results.append(("a status without the author's words is refused", "--words" in str(e)))
        bad = register + [{"id": "R01", "text": "x", "source": "s", "scope": "alle", "status": "bestätigt", "added": "t"},
                          {"id": "X", "text": "x", "source": "s", "scope": {"kap": [1]}, "status": "unklar", "added": "t",
                           "check": {"kind": "nope"}}]
        probs = register_problems(bad, landed={"doc"})
        results.append(("the register check names a repeated id, a missing word, a bad status, scope and check",
                        any("repeats" in x for x in probs) and any("without the author" in x for x in probs)
                        and any("status 'unklar'" in x for x in probs) and any("scope" in x for x in probs) and any("unknown check" in x for x in probs)))
        results.append(("the register check accepts the fixture", register_problems(register, landed={"doc"}) == []))
        probs = register_problems([{**register[3], "source": "^[nirgends.md:L1]"}], landed={"doc"})
        results.append(("a source citing no landed document is named", any("no landed document" in x for x in probs)))
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
    if verb == "list":
        print(listing(int(opt("--kap")) if opt("--kap") else None, opt("--status") or None))
        return 0
    if verb == "show" and rest:
        r = next((x for x in rows() if x["id"] == rest[0]), None)
        print(json.dumps(r, ensure_ascii=False, indent=1) if r else f"no rule {rest[0]}")
        return 0 if r else 1
    if verb in ("confirm", "reject") and rest:
        print(json.dumps(set_status(rest[0], "bestätigt" if verb == "confirm" else "verworfen", opt("--words"), opt("--by", "author")), ensure_ascii=False))
        return 0
    if verb == "check" and rest:
        findings = check(Path(rest[0]), int(opt("--kap")) if opt("--kap") else None)
        if "--json" in rest:
            print(json.dumps(findings, ensure_ascii=False, indent=1))
        else:
            for f in findings:
                print(f"{f['severity']:5} {f['rule']:5} Absatz {f['absatz']:>3}  {f['wort']!s:28} {f['stelle']}")
            fails = sum(1 for f in findings if f["severity"] == "fail")
            print(f"{len(findings)} finding(s), {fails} failure(s), {len(findings) - fails} query(ies)")
        return 1 if any(f["severity"] == "fail" for f in findings) else 0
    if verb == "register":
        probs = register_problems()
        for p in probs:
            print("FAIL  " + p)
        items = rows()
        print(f"{len(items)} rule(s): " + ", ".join(f"{sum(1 for r in items if r['status'] == s)} {s}" for s in STATUSES) + f", {len(probs)} problem(s)")
        return 1 if probs else 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
