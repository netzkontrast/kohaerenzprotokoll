"""Numbers about a German prose text's rhythm, and the word-level difference between two versions.

Taken from `netzkontrast/writing-intelligence` (the deterministic voice-metric vector with a drift direction,
`references/` voice fingerprint), with its rule against rewriting kept and its English metrics left behind: this
splits German sentences, counts, and compares. It never judges a sentence, never proposes a word, and never
writes `Manuscript/`.

    python3 scripts/voice_metrics.py measure <file>          the metrics of one text
    python3 scripts/voice_metrics.py compare <a> <b>         metrics side by side and the word-level diff a → b
    python3 scripts/voice_metrics.py baseline [--write]      the metrics of every approved scene (status freigegeben)
    python3 scripts/voice_metrics.py check <file>            each metric against the baseline, with its direction
    python3 scripts/voice_metrics.py selftest

A scene file's head (everything above its second `---`) is stripped, as `prose_rules.prose_of` does. The baseline
is read only from scenes the author approved — the pilot's instruction that a style sheet is "fed only by my
approved text"; with none approved, `baseline` and `check` say so and stop.

The drift threshold below is provisional:

    DRIFT = 0.15     # provisional — relative change at which a metric is reported as moving
                     # may not: call a text good or bad, gate an approval, run in CI
                     # retire when: the author has read five checks and none of their directions told him anything
"""

from __future__ import annotations

import difflib
import json
import re
import statistics
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / "Plan" / "runs" / "voice" / "baseline.json"
DRIFT = 0.15
ABBREV = ("z. B.", "d. h.", "u. a.", "z.B.", "d.h.", "u.a.", "ca.", "Nr.", "Dr.", "bzw.", "usw.", "vgl.", "etc.", "Kap.")
WORD = re.compile(r"(?<![°])[0-9A-Za-zÄÖÜäöüß][0-9A-Za-zÄÖÜäöüß'’,.·×⁰¹²³⁴⁵⁶⁷⁸⁹°-]*")
END = re.compile(r"(?:(?<=[.!?…])|(?<=[.!?…][“\"’»)]))\s+(?=[„\"‘»«(]?[A-ZÄÖÜ0-9])")


def prose_of(text: str) -> str:
    """The prose of a scene file (below the second `---` of its head), or the text unchanged."""
    if text.startswith("---\n"):
        parts = text.split("\n---\n", 2)
        if len(parts) == 3:
            return parts[2]
    return text


def paragraphs(text: str) -> list[str]:
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip() and p.strip() != "---" and not p.strip().startswith(">")]


def sentences(par: str) -> list[str]:
    """German sentences of one paragraph. A line without end punctuation (a directive in capitals, a number on its own
    line) is its own sentence; abbreviations do not end one."""
    out = []
    for line in [ln.strip() for ln in par.split("\n") if ln.strip()] if "\n" in par.strip() else [par.strip()]:
        masked = line
        for i, a in enumerate(ABBREV):
            masked = masked.replace(a, a.replace(".", "\x00"))
        out += [s.replace("\x00", ".").strip() for s in END.split(masked) if s.strip()]
    return out


def words(s: str) -> list[str]:
    return [w.rstrip(",.") for w in WORD.findall(s) if w.rstrip(",.")]


def metrics(text: str) -> dict:
    pars = paragraphs(prose_of(text))
    sents = [s for p in pars for s in sentences(p)]
    sl = [len(words(s)) for s in sents if words(s)]
    pl = [len(words(p)) for p in pars]
    nw = sum(pl)
    openers = [(words(s) or [""])[0].lower() for s in sents if words(s)]
    repeats = sum(1 for a, b in zip(openers, openers[1:]) if a == b)

    def sd(x):
        return round(statistics.pstdev(x), 2) if len(x) > 1 else 0.0

    return {"words": nw, "sentences": len(sl), "paragraphs": len(pars),
            "sentence_mean": round(statistics.mean(sl), 2) if sl else 0.0, "sentence_sd": sd(sl),
            "paragraph_mean": round(statistics.mean(pl), 2) if pl else 0.0, "paragraph_sd": sd(pl),
            "commas_per_100": round(100 * sum(s.count(",") for s in sents) / nw, 2) if nw else 0.0,
            "questions_per_500": round(500 * sum(s.count("?") for s in sents) / nw, 2) if nw else 0.0,
            "same_opener_share": round(repeats / (len(openers) - 1), 3) if len(openers) > 1 else 0.0}


SHAPE = ("sentence_mean", "sentence_sd", "paragraph_mean", "paragraph_sd", "commas_per_100", "questions_per_500",
         "same_opener_share")


def direction(value: float, base: float, current: float | None = None) -> str:
    """`stable` within DRIFT of the baseline; otherwise `higher`/`lower`; with a previous value, whether it moved
    closer to or further from the baseline."""
    if base == 0:
        rel = 0.0 if value == 0 else 1.0
    else:
        rel = (value - base) / base
    if abs(rel) < DRIFT:
        return "stable"
    side = "higher" if rel > 0 else "lower"
    if current is None:
        return side
    return side + (", closer to baseline" if abs(value - base) < abs(current - base) else ", further from baseline")


def word_diff(a: str, b: str) -> dict:
    """The word-level difference a → b: words kept, deleted, inserted, and the replaced spans, by difflib over word
    tokens (punctuation attached to its word, so a moved comma counts as a changed word)."""
    wa, wb = prose_of(a).split(), prose_of(b).split()
    sm = difflib.SequenceMatcher(a=wa, b=wb, autojunk=False)
    kept = deleted = inserted = 0
    spans = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            kept += i2 - i1
            continue
        deleted += i2 - i1
        inserted += j2 - j1
        spans.append({"op": op, "from": " ".join(wa[i1:i2]), "to": " ".join(wb[j1:j2]), "at_word": i1 + 1})
    return {"words_a": len(wa), "words_b": len(wb), "kept": kept, "deleted": deleted, "inserted": inserted,
            "changed_share_of_a": round(1 - kept / len(wa), 3) if wa else 0.0, "spans": spans}


def approved_scenes() -> list[Path]:
    out = []
    for p in sorted((ROOT / "Manuscript").glob("kap-*/szene-*.md")):
        if re.search(r"^status: freigegeben$", p.read_text(encoding="utf-8"), re.M):
            out.append(p)
    return out


def baseline(files: list[Path] | None = None) -> dict | None:
    files = approved_scenes() if files is None else files
    if not files:
        return None
    m = metrics("\n\n".join(prose_of(f.read_text(encoding="utf-8")) for f in files))
    return {"from": [f.relative_to(ROOT).as_posix() if f.is_relative_to(ROOT) else f.name for f in files], "metrics": m,
            "drift": DRIFT, "note": "provisional; read from approved scenes only; never a judgement of the prose"}


def check(text: str, base: dict) -> list[tuple[str, float, float, str]]:
    m = metrics(text)
    return [(k, m[k], base["metrics"][k], direction(m[k], base["metrics"][k])) for k in SHAPE]


# --- selftest --------------------------------------------------------------------------------

def selftest() -> int:
    results = []
    s = sentences("Ich ziehe z. B. die Jacke an. Dann erst öffne ich das Fach! Wer sitzt dort? „Niemand.“ Sie sieht auf.")
    results.append(("an abbreviation does not end a sentence; ., ! and ? do, before a quote too",
                    s == ["Ich ziehe z. B. die Jacke an.", "Dann erst öffne ich das Fach!", "Wer sitzt dort?", "„Niemand.“", "Sie sieht auf."]))
    s = sentences("WARTUNG SEKTOR 04\nHEUTE 16:40 – 16:43\nVORKÜHLUNG LÄUFT")
    results.append(("a directive block is one sentence per line", len(s) == 3))
    results.append(("a number with a decimal comma is one word", words("Die Wand zeigt 20,6 °C.") == ["Die", "Wand", "zeigt", "20,6"]))
    head = "---\nkapitel: 1\nstatus: entwurf\n---\n> Beats: viele Wörter hier.\n\n---\n\n"
    m = metrics(head + "Ich gehe. Ich stehe.\n\nIch sehe die Bank, und sie ist leer.")
    results.append(("a scene's head and beats are not counted", m["words"] == 12 and m["paragraphs"] == 2 and m["sentences"] == 3))
    results.append(("two sentences in a row opening with the same word count as a repeat", m["same_opener_share"] == 1.0))
    results.append(("commas are counted per hundred words", m["commas_per_100"] == round(100 / 12, 2)))
    results.append(("within the drift it is stable, beyond it the side is named", direction(10.5, 10) == "stable" and direction(13, 10) == "higher"
                    and direction(7, 10) == "lower" and direction(12, 10, 14) == "higher, closer to baseline"))
    d = word_diff("Ich gehe an der Bank vorbei.", "Ich gehe langsam an der Bank vorbei.")
    results.append(("a word added in b is one insert and nothing deleted", d["kept"] == 6 and d["inserted"] == 1 and d["deleted"] == 0
                    and d["spans"][0]["to"] == "langsam"))
    d = word_diff("Sie hat keine Lehne.", "Sie hat eine Lehne.")
    results.append(("a replaced word counts once as deleted and once as inserted", (d["deleted"], d["inserted"]) == (1, 1)
                    and d["changed_share_of_a"] == 0.25))
    with tempfile.TemporaryDirectory() as tmp:
        f = Path(tmp) / "a.md"
        f.write_text(head + "Ich gehe. Ich stehe.\n", encoding="utf-8")
        b = baseline([f])
        rows = check("Ich gehe sehr lange und sehr weit durch den grauen Korridor, und niemand sieht mich an.", b)
        results.append(("check reports every shape metric against the baseline with a direction",
                        [r[0] for r in rows] == list(SHAPE) and dict((r[0], r[3]) for r in rows)["sentence_mean"] == "higher"))
    results.append(("with no approved scene there is no baseline", baseline([]) is None))
    for name, ok in results:
        print(f"{'held' if ok else 'FAILED':7} {name}")
    held = sum(ok for _, ok in results)
    print(f"{held} of {len(results)} held")
    return 0 if held == len(results) else 1


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    verb, rest = argv[0], argv[1:]
    if verb == "selftest":
        return selftest()
    if verb == "measure" and rest:
        print(json.dumps(metrics(Path(rest[0]).read_text(encoding="utf-8")), ensure_ascii=False, indent=1))
        return 0
    if verb == "compare" and len(rest) >= 2:
        a, b = (Path(x).read_text(encoding="utf-8") for x in rest[:2])
        ma, mb = metrics(a), metrics(b)
        for k in ma:
            print(f"{k:20} {ma[k]:>9} {mb[k]:>9}  {direction(mb[k], ma[k]) if k in SHAPE else ''}")
        d = word_diff(a, b)
        print(f"\nWörter {d['words_a']} → {d['words_b']}: {d['kept']} gleich, {d['deleted']} gestrichen, {d['inserted']} neu; "
              f"{d['changed_share_of_a']:.1%} der Wörter von a geändert, in {len(d['spans'])} Stellen")
        if "--spans" in rest:
            for sp in d["spans"]:
                print(f"  Wort {sp['at_word']:>5} {sp['op']:8} „{sp['from']}“ → „{sp['to']}“")
        return 0
    if verb == "baseline":
        b = baseline()
        if b is None:
            print("no approved scene (status freigegeben) yet: there is no baseline, and none is invented")
            return 1
        print(json.dumps(b, ensure_ascii=False, indent=1))
        if "--write" in rest:
            BASELINE.parent.mkdir(parents=True, exist_ok=True)
            BASELINE.write_text(json.dumps(b, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            print(f"wrote {BASELINE.relative_to(ROOT)}")
        return 0
    if verb == "check" and rest:
        b = baseline()
        if b is None:
            print("no approved scene (status freigegeben) yet: nothing to compare against")
            return 1
        for k, v, base, d in check(Path(rest[0]).read_text(encoding="utf-8"), b):
            print(f"{k:20} {v:>9} baseline {base:>9}  {d}")
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
