"""The chapter briefing: the contract for every scene — the decided, the proposed and the sources, marked apart.

Decision 030 (2026-10-26): a session writes a scene on beats the author approved, and what it writes is in the
chapter's briefing and nothing else. The briefing carries **the decided and the proposed, marked apart**, the
open Weichen as questions before the scene, the rules in scope, the continuity state at the chapter's start, and
the scenes with their status. It is written by code from the repository's records and judges nothing.

    python3 scripts/brief.py kap N               # writes Manuscript/kap-NN/briefing.md
    python3 scripts/brief.py check [kap N]        # a briefing is behind when an input changed since it was written
    python3 scripts/brief.py selftest

The sections, every bullet tagged:

| section | tag | from |
|---|---|---|
| Entschieden | `[K]` | `Manuscript/kanon.md` rows naming the chapter or its figures; the storypoints of `a.json`/`b.json` the chapter carries; the `weave.json` row (route, world, anchor); the parts of `anteile.json` that show here and how; the figure cards' `## Kanon` blocks; rules `bestätigt` in scope |
| Vorgeschlagen | `[V]` | the treatment paragraph; the `development.json` row; the beats of the scene architecture; the drafts that exist and their word counts; rules `offen` in scope |
| Quellen | `[S]` | the chapter page's summary and `## Where the sources differ`; the term pages the paragraph names, with their thought page where one exists |
| Kontinuität | `[D]` | `continuity.py` — the state at the chapter's start, and what is still to come |
| Offen | — | the Weichen that touch the chapter and are not answered, with options and recommendation: the author answers them before the first scene (`weiche.py answer`) |
| Szenen | — | the scene files of the chapter with status, beats and words; or none yet |

**The hash.** The frontmatter names `inputs` (every file the briefing was written from) and `inputs_hash`; `check`
recomputes it and says **behind** when canon, a Weiche, the treatment, the register, a card or a rule in scope
changed since. A scene is written only on a current briefing (`manuscript.py`).
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
STORYFORM = ROOT / "Plan" / "storyform"
TREATMENT = MANUSCRIPT / "plot" / "treatment.md"
ARCH = [ROOT / "Plan" / "runs" / "writing" / "book" / "scene-architecture_akt-1_2026-10-05.md",
        ROOT / "Plan" / "runs" / "writing" / "book" / "scene-architecture_akt-2_2026-10-05.md"]
CHAPTERS = ROOT / "Wiki" / "chapters"
TERMS = ROOT / "Wiki" / "terms"
WORD = lambda w: re.compile(r"(?<![\wÄÖÜäöüß])" + re.escape(w) + r"(?![\wÄÖÜäöüß])")  # noqa: E731
ROLE = {"Main Character": "MC", "Influence Character": "IC", "Objective Story": "OS", "Relationship Story": "RS"}


def folder_of(n: int) -> Path:
    return MANUSCRIPT / f"kap-{n:02d}"


# --- reading the records ----------------------------------------------------------

def treatment_paragraph(n: int, text: str | None = None) -> tuple[str, str]:
    """(title, body) of `### Kap N — …` in the treatment."""
    text = text if text is not None else (TREATMENT.read_text(encoding="utf-8") if TREATMENT.exists() else "")
    m = re.search(rf"^### Kap {n}\b[^\n]*\n(.*?)(?=^### |^## |\Z)", text, re.M | re.S)
    if not m:
        return "", ""
    title = re.search(rf"^### Kap {n}\b\s*[—–-]?\s*(.*)$", text, re.M)
    return (title.group(1).strip() if title else ""), m.group(1).strip()


def architecture(n: int) -> str:
    for p in ARCH:
        if not p.exists():
            continue
        m = re.search(rf"^### Kap {n}\b[^\n]*\n(.*?)(?=^### |^## |\Z)", p.read_text(encoding="utf-8"), re.M | re.S)
        if m:
            return m.group(1).strip()
    return ""


def storypoint_value(ref: list, forms: dict) -> str:
    """`["A", "Main Character Concern"]` → `A-MC Concern: Memory`, from the storyform's own fields."""
    sf = forms.get(ref[0], {})
    name = ref[1]
    for role, key in ROLE.items():
        if name.startswith(role + " "):
            field = name[len(role) + 1:].lower().replace(" ", "_")
            return f"{ref[0]}-{key} {name[len(role) + 1:]}: {sf.get(key, {}).get(field, '?')}"
    if name.startswith("Story "):
        field = name[6:].lower()
        return f"{ref[0]} {name}: {sf.get('plot', {}).get(field, '?')}"
    return f"{ref[0]} {name}"


def kanon_block(text: str) -> str:
    k = re.search(r"^## Kanon\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return k.group(1).strip() if k else ""


def holding_cards(manuscript: Path | None = None) -> list[dict]:
    """The figure and world cards that hold — a card resting by a later decision (033) is history, not decided."""
    import cards
    return [c for c in cards.load(manuscript or MANUSCRIPT) if not cards.rests(c)]


def card_canon(name_or_match: str) -> tuple[str, str] | None:
    """(file, the card's ## Kanon block) for the holding figure or world card whose `match` holds the word."""
    for c in holding_cards():
        if c["fm"].get("kind") != "voraussetzung" and name_or_match in (c["fm"].get("match") or []):
            return c["path"].relative_to(ROOT).as_posix(), kanon_block(c["text"])
    return None


def figures_in(text: str) -> list[str]:
    out = []
    for c in holding_cards():
        if c["fm"].get("kind") == "voraussetzung":
            continue  # a premise stands in every briefing, whether the paragraph names it or not
        for w in c["fm"].get("match") or []:
            if WORD(w).search(text) and w not in out:
                out.append(w)
    return out


def premise_lines(manuscript: Path | None = None) -> tuple[list[str], list[str]]:
    """([K] bullets for the world's premises, their files) — every chapter's briefing carries them (decision 033)."""
    import cards
    lines, files = [], []
    base = manuscript or MANUSCRIPT
    for c in cards.premises(base):
        block = " ".join(kanon_block(c["text"]).split())
        ids = ", ".join(c["fm"].get("kanon") or [])
        rel = c["path"].relative_to(ROOT).as_posix() if c["path"].is_relative_to(ROOT) else f"Manuscript/{c['rel']}"
        lines.append(f"- [K] Voraussetzung der Welt — {c['fm'].get('name')} ({ids}): {block or 'nichts entschieden'} (`{rel}`)")
        files.append(rel)
    return lines, files


SZENE = re.compile(r"\bSzene (\d+)\b")


def duties(rows: list[dict]) -> list[dict]:
    """The decided sentences that name a scene: {scene, id, sentence}. The pilot's F10 — W28 and W20 asked for a line
    in Szene 1, the beats were proposed without them, and no check said so. A duty is read, never judged answered:
    `manuscript.py check` lists it as a query until the author's approval."""
    out = []
    for r in rows:
        text = re.sub(r"^.*?(?:Liste|Gespräch[^:]*): „", "", r["what"]).rstrip("“ ")  # the answer, not its preamble
        sents = [x.strip() for x in re.split(r"(?<=[.!?])\s+", text) if x.strip()]
        for i, sent in enumerate(sents):
            for k in sorted(set(SZENE.findall(sent)), key=int):
                out.append({"scene": int(k), "id": r["id"], "sentence": sent,
                            "context": sents[i - 1] if i else ""})
    return out


def duties_of(n: int, k: int) -> list[dict]:
    """The duties of scene k in chapter n, from the rows the briefing stands on."""
    import weiche
    return [d for d in duties(decided_rows(n, weiche.kanon_rows())) if d["scene"] == k]


def decided_rows(n: int, kanon: list[dict], rest: dict | None = None) -> list[dict]:
    """The canon rows a briefing of chapter n stands on: naming the chapter, or the answer of a Weiche touching it —
    and holding: a row resting by a later decision (kanon.md § Ruhend) is history, not a duty."""
    import weiche
    touching = set()
    for wid in weiche.sheets():
        ch = weiche.chapters_of(wid)
        if n in set(ch["development"]) | set(ch["treatment"]) | set(ch["sheet"]):
            touching.add(wid)
    rest = weiche.resting() if rest is None else rest
    return [r for r in kanon if r["id"] not in rest and (WORD(f"Kap {n}").search(r["what"]) or r["id"] in touching)]


def terms_in(text: str) -> list[tuple[str, str, bool]]:
    """(slug, title, has a thought page) for every wiki term whose surface the text writes."""
    index = ROOT / "Wiki" / "index.json"
    if not index.exists():
        return []
    terms = json.loads(index.read_text(encoding="utf-8"))["terms"]
    out = []
    low = text.lower()
    for slug, row in terms.items():
        surfaces = [s for s in row.get("surfaces", []) if len(s) >= 4]
        if any(WORD(s.lower()).search(low) for s in surfaces):
            tp = TERMS / f"{slug}.md"
            thought = tp.exists() and "form: gedanken" in tp.read_text(encoding="utf-8")[:400]
            out.append((slug, row.get("title", slug), bool(thought)))
    return out


def chapter_page(n: int) -> tuple[str, str, Path | None]:
    p = CHAPTERS / f"kap-{n:02d}.md"
    if not p.exists():
        return "", "", None
    text = p.read_text(encoding="utf-8")
    summ = re.search(r"^## What this chapter is about[^\n]*\n(.*?)(?=^## )", text, re.M | re.S)
    diff = re.search(r"^## Where the sources differ\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    summary = re.sub(r"^Navigation, not a reading:.*?\n\n", "", summ.group(1).strip(), flags=re.S) if summ else ""
    return summary, (diff.group(1).strip() if diff else ""), p


def scenes_of(n: int) -> list[dict]:
    out = []
    for p in sorted(folder_of(n).glob("szene-*.md")):
        text = p.read_text(encoding="utf-8")
        fm = {}
        if text.startswith("---\n"):
            end = text.find("\n---\n", 4)
            for line in text[4:end].split("\n"):
                if ":" in line:
                    k, _, v = line.partition(":")
                    fm[k.strip()] = v.strip().strip('"')
        body = text[text.find("\n---\n", 4) + 5:] if text.startswith("---\n") else text
        out.append({"file": p.relative_to(ROOT).as_posix(), "name": p.stem, "status": fm.get("status", "?"),
                    "beats": fm.get("beats", ""), "words": len(re.findall(r"\w+", body))})
    return out


def drafts_of(n: int) -> list[tuple[str, int]]:
    return [(p.relative_to(ROOT).as_posix(), len(re.findall(r"\w+", p.read_text(encoding="utf-8"))))
            for p in sorted(folder_of(n).glob("entwurf-*.md"))]


# --- the briefing ------------------------------------------------------------------

def inputs_of(n: int, weichen: list[str], cards: list[str]) -> list[Path]:
    import continuity
    files = [MANUSCRIPT / "kanon.md", STORYFORM / "a.json", STORYFORM / "b.json", STORYFORM / "weave.json",
             STORYFORM / "anteile.json", STORYFORM / "development.json", TREATMENT, MANUSCRIPT / "regeln.jsonl",
             CHAPTERS / f"kap-{n:02d}.md"] + ARCH
    files += [continuity.path_of(k) for k in range(0, n + 1)]
    files += [ROOT / w for w in weichen] + [ROOT / c for c in cards]
    return [f for f in files if f.exists()]


def hash_of(files: list[Path]) -> str:
    h = hashlib.sha256()
    for f in sorted(files):
        h.update(f.relative_to(ROOT).as_posix().encode() + b"\0" + f.read_bytes() + b"\0")
    return h.hexdigest()


def build(n: int, today: str | None = None) -> str:
    import continuity
    import prose_rules
    import weiche
    today = today or datetime.date.today().isoformat()
    forms = {"A": json.loads((STORYFORM / "a.json").read_text(encoding="utf-8")),
             "B": json.loads((STORYFORM / "b.json").read_text(encoding="utf-8"))}
    weave = json.loads((STORYFORM / "weave.json").read_text(encoding="utf-8"))
    anteile = json.loads((STORYFORM / "anteile.json").read_text(encoding="utf-8"))
    dev = json.loads((STORYFORM / "development.json").read_text(encoding="utf-8"))["chapters"].get(str(n), {})
    title, para = treatment_paragraph(n)
    wrow = weave["chapters"].get(str(n), {})
    world = next((w for w in weave.get("worlds", []) if w["chapters"][0] <= n <= w["chapters"][1]), None)
    act = next((k for k, (lo, hi) in weave["acts"].items() if lo <= n <= hi), None)
    kanon = weiche.kanon_rows()
    figures = figures_in(para + "\n" + json.dumps(dev, ensure_ascii=False))
    cards = []
    out = ["---", f"kapitel: {n}", f"titel: {title or '—'}", f"written: {today}", "by: brief.py", "status: briefing"]

    K, V, S = [], [], []
    # [K] canon rows naming the chapter or its figures, and the answer of every Weiche that touches the chapter —
    # the same set § Offen lists while it is open; an answer given for this chapter must not drop out of its briefing
    touching = set()
    for wid in weiche.sheets():
        ch = weiche.chapters_of(wid)
        if n in set(ch["development"]) | set(ch["treatment"]) | set(ch["sheet"]):
            touching.add(wid)
    rest, resting_named = weiche.resting(), []
    # [K] the world's premises, in every chapter (decision 033)
    premises, premise_files = premise_lines()
    K += premises
    for r in kanon:
        if WORD(f"Kap {n}").search(r["what"]) or any(WORD(f).search(r["what"]) for f in figures if f not in ("AEGIS", "Kael")) \
                or r["id"] in touching:
            if r["id"] in rest:
                resting_named.append(f"{r['id']} (seit {rest[r['id']]['since']})")
                continue
            K.append(f"- [K] **{r['id']}** ({r['date']}): {r['what']} — `{r['where'].strip('`')}`")
    if resting_named:
        K.append(f"- [L] Ruhend, nicht entschieden: {', '.join(resting_named)} — Geschichte, keine Pflicht (`Manuscript/kanon.md` § Ruhend)")
    # [K] storypoints
    for sp in dev.get("storypoints", []):
        K.append(f"- [K] Storypoint {storypoint_value(sp, forms)} (`Plan/storyform/{'a' if sp[0] == 'A' else 'b'}.json`, Entscheidung 025)")
    # [K] weave
    if wrow:
        K.append(f"- [K] Weaving: Route `{wrow.get('route')}`, A trägt {', '.join(wrow.get('A', [])) or '—'}, B trägt {', '.join(wrow.get('B', [])) or '—'}"
                 + (f", Anker „{wrow['anchor']}“" if wrow.get("anchor") else "") + f"; Akt {act or '?'}"
                 + ("" if "Kernwelten" in rest else
                    f", {world['world']} ({world['label']}, Kap {world['chapters'][0]}–{world['chapters'][1]})" if world else ", der Rahmen")
                 + (" (`Plan/storyform/weave.json`; die Welt des Kapitels ruht mit der Kanonzeile Kernwelten, 033)" if "Kernwelten" in rest
                    else " (`Plan/storyform/weave.json`, Kanonzeile Kernwelten)"))
    # [K] parts (the author's working base, step 32) — named as such
    for app in anteile.get("appearances", []):
        if n in app.get("chapters", []):
            K.append(f"- [K] Anteil {', '.join(app['parts'])} zeigt sich über {app.get('channel')}: {app.get('how', '')} — ohne Namen vor Kap {anteile.get('unnamed_until', 13)} (`Plan/storyform/anteile.json`, Arbeitsgrundlage des Autors vom 2026-10-05, Schritt 32)")
    # [K] figure cards
    for f in figures:
        cc = card_canon(f)
        if cc:
            file, block = cc
            cards.append(file)
            line = " ".join(block.split())[:400] if block else "nichts entschieden"
            K.append(f"- [K] Karte {f}: {line} (`{file}`)")
    # [K] duties: a decided sentence that names a scene (F10)
    for d in duties([r for r in kanon if any(f"**{r['id']}**" in k for k in K)]):
        K.append(f"- [K] Pflicht Szene {d['scene']} ({d['id']}): " + (f"{d['context']} " if d["context"] else "") + d["sentence"])
    # rules
    rules_in = [r for r in prose_rules.rows() if prose_rules.in_scope(r, n)]
    for r in rules_in:
        if r["status"] == "bestätigt":
            K.append(f"- [K] Regel {r['id']}: {r['text']}" + (f" — geprüft: `{r['check']['kind']}`" if r.get("check") else "") + f" (`Manuscript/regeln.jsonl`, {r.get('on', '')})")
    # [V] treatment, development, beats, drafts, open rules
    if para:
        V.append(f"- [V] Treatment, Kap {n} — {title}:")
        V += ["  " + ln for ln in para.split("\n")]
    if dev:
        for key, label in (("goal", "Ziel"), ("opposition", "Widerstand"), ("action", "Handlung"), ("turn", "Wende"), ("cost", "Preis"),
                           ("knowledge", "Wissen"), ("reader", "Leser"), ("timing", "Zeit"), ("next", "Danach"), ("open", "Offen")):
            if dev.get(key):
                V.append(f"- [V] {label}: {dev[key]} (`Plan/storyform/development.json`, Status {dev.get('status', 'proposal')})")
    arch = architecture(n)
    if arch:
        V.append(f"- [V] Beats der Szenenarchitektur (`Plan/runs/writing/book/scene-architecture_akt-*_2026-10-05.md`, Vorschlag):")
        V += ["  " + ln for ln in arch.split("\n")]
    for file, words in drafts_of(n):
        V.append(f"- [V] Entwurf `{file}`, {words} Wörter — ein Pol, keine Grundlage (Entscheidung 030, Antwort 3)")
    for r in rules_in:
        if r["status"] == "offen":
            V.append(f"- [V] Regel {r['id']} (offen, {r['source']}): {r['text']}" + (f" — Rückfrage: `{r['check']['kind']}`" if r.get("check") else ""))
    # [S] chapter page, terms
    summary, differ, page = chapter_page(n)
    if page:
        if summary:
            S.append(f"- [S] Die Kapitelseite fasst die gelesenen Quellen so zusammen (`{page.relative_to(ROOT).as_posix()}`): " + " ".join(summary.split())[:1200])
        if differ:
            S.append(f"- [S] Wo die Quellen auseinandergehen (`{page.relative_to(ROOT).as_posix()}` § Where the sources differ):")
            S += ["  " + ln for ln in differ.split("\n") if ln.strip()][:12]
    for slug, ttitle, thought in terms_in(para + "\n" + json.dumps(dev, ensure_ascii=False)):
        S.append(f"- [S] Begriff [[{slug}|{ttitle}]]" + (f" — Gedankenseite `Wiki/terms/{slug}.md`" if thought else f" — Kandidatenseite `Wiki/candidates/{slug}.md`"))
    # continuity
    st = continuity.state_at(n)
    C = [f"- [D] Zu Beginn von Kap {n} gelten {len(st['wissen'])} Wissenszeilen, {len(st['zeit'])} Zeitangaben, {len(st['zahlen'])} Zahlen, {len(st['dinge'])} Dinge (`python3 scripts/continuity.py show kap-{n:02d}`)."]
    for r in st["zahlen"]:
        C.append(f"- [D] {r['name']} = {r['wert']} (Kap {r['kapitel']}, {r.get('status')}; {r.get('quelle', '')})")
    for r in st["zeit"]:
        C.append(f"- [D] Zeit, Kap {r['kapitel']}: {r.get('wert')} ({r.get('status')}; {r.get('quelle', '')})")
    for r in st["dinge"]:
        C.append(f"- [D] {r['name']} ({r.get('art')}, seit Kap {r['seit']}, {r.get('status')})" + (f" — {r['hinweis']}" if r.get("hinweis") else ""))
    for r in st["wissen"]:
        if r["kapitel"] == n or r.get("status") != "proposal":
            who = "Es gilt" if r.get("wer") == "Stand" else f"{r.get('wer')} weiß"
            C.append(f"- [D] {who} (seit Kap {r['seit']}, {r.get('status')}): {' '.join(str(r.get('fakt')).split())[:300]}")
    coming = [r for r in st["later"] if r["seit"] <= n + 3]
    if coming:
        C.append("- [D] Noch nicht eingetreten, bald: " + "; ".join(f"{r.get('name') or r.get('fakt')[:40]} (ab Kap {r['seit']})" for r in coming[:12]))
    # open Weichen
    O = []
    weichen_files = []
    for wid, path in weiche.sheets().items():
        meta = weiche.frontmatter(path.read_text(encoding="utf-8"))
        ch = weiche.chapters_of(wid)
        touched = set(ch["development"]) | set(ch["treatment"]) | set(ch["sheet"])
        if n not in touched or meta.get("status") == "beantwortet":
            continue
        weichen_files.append(path.relative_to(ROOT).as_posix())
        text = path.read_text(encoding="utf-8")
        opts = weiche.options_of(text)
        how = "aus development.json/Treatment" if n in set(ch["development"]) | set(ch["treatment"]) else "das Blatt nennt das Kapitel"
        O.append(f"- **{wid}** ({meta.get('status')}, {meta.get('frage_art')}; {how}) — `{path.relative_to(ROOT).as_posix()}`"
                 + (": " + "; ".join(f"{k} {t}" for k, t in opts) if opts else "")
                 + f". Empfehlung: {meta.get('empfehlung', '—')}. Antwort: `python3 scripts/weiche.py answer {wid} --option X --words \"…\"`")
    # scenes
    Z = []
    for s in scenes_of(n):
        Z.append(f"- `{s['file']}` — {s['status']}, {s['words']} Wörter" + (f"; Beats: {s['beats'][:120]}" if s["beats"] else ""))
    if not Z:
        Z.append(f"- Noch keine Szene. Die erste entsteht auf Beats, die der Autor freigibt (`python3 scripts/manuscript.py beats kap-{n:02d} 1 --words \"…\"`), bei 3 000–5 000 Wörtern je Kapitel (W16).")

    files = inputs_of(n, weichen_files, cards + premise_files)
    out += ["inputs: [" + ", ".join(f'"{f.relative_to(ROOT).as_posix()}"' for f in files) + "]", f"inputs_hash: {hash_of(files)}", "---", ""]
    out += [f"# Briefing Kap {n}" + (f" — {title}" if title else ""), "",
            f"Geschrieben am {today} von `brief.py` aus den Unterlagen des Repositoriums; es urteilt nicht. `[K]` ist entschieden (Kanon, Storyform, Weaving, Karten, bestätigte Regeln), `[V]` vorgeschlagen (Treatment, Entwicklung, Beats, Entwürfe, offene Regeln), `[S]` sagen die Quellen (Forschung, nie Kanon), `[D]` abgeleitet (Kontinuität). Was eine Szene schreibt, steht hier und nirgends sonst (Entscheidung 030).", "",
            "## Entschieden", ""] + (K or ["- [L] Nichts Entschiedenes nennt dieses Kapitel."]) + ["", "## Vorgeschlagen", ""] + (V or ["- [L] Kein Vorschlag."]) \
        + ["", "## Quellen", ""] + (S or ["- [L] Keine Kapitelseite."]) + ["", "## Kontinuität", ""] + C \
        + ["", "## Offen — vor der ersten Szene zu beantworten", ""] + (O or ["- Keine offene Weiche nennt dieses Kapitel."]) \
        + ["", "## Szenen", ""] + Z + [""]
    return "\n".join(out)


def write(n: int, today: str | None = None) -> Path:
    folder_of(n).mkdir(parents=True, exist_ok=True)
    p = folder_of(n) / "briefing.md"
    p.write_text(build(n, today), encoding="utf-8")
    return p


def status(n: int) -> tuple[str, str]:
    """('current' | 'behind' | 'none', why)."""
    p = folder_of(n) / "briefing.md"
    if not p.exists():
        return "none", f"no briefing for Kap {n}"
    text = p.read_text(encoding="utf-8")
    m = re.search(r"^inputs: \[(.*)\]$", text, re.M)
    h = re.search(r"^inputs_hash: (\w+)$", text, re.M)
    if not m or not h:
        return "behind", "the briefing names no inputs"
    files = [ROOT / x.strip().strip('"') for x in m.group(1).split(",") if x.strip()]
    missing = [f for f in files if not f.exists()]
    if missing:
        return "behind", "an input is gone: " + ", ".join(x.relative_to(ROOT).as_posix() for x in missing)
    if hash_of(files) != h.group(1):
        changed = []
        return "behind", "an input changed since the briefing was written — run brief.py kap " + str(n)
    return "current", "current"


# --- selftest ---------------------------------------------------------------------------

def selftest() -> int:
    results = []
    forms = {"A": {"MC": {"concern": "Memory", "unique_ability": "Thought"}, "plot": {"requirements": "Learning"}}, "B": {"IC": {"solution": "Faith"}}}
    results.append(("a storypoint reference resolves to the storyform's value", storypoint_value(["A", "Main Character Concern"], forms) == "A-MC Concern: Memory"
                    and storypoint_value(["A", "Story Requirements"], forms) == "A Story Requirements: Learning"
                    and storypoint_value(["B", "Influence Character Solution"], forms) == "B-IC Solution: Faith"
                    and storypoint_value(["A", "Main Character Unique Ability"], forms) == "A-MC Unique Ability: Thought"))
    t = "## 2b\n\n### Kap 1 — Vorkühlung\n- a\n- b\n\n### Kap 2 — Rolle\n- c\n"
    results.append(("the treatment paragraph of a chapter is cut at the next heading", treatment_paragraph(1, t) == ("Vorkühlung", "- a\n- b") and treatment_paragraph(2, t) == ("Rolle", "- c") and treatment_paragraph(9, t) == ("", "")))
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "a.txt").write_text("x", encoding="utf-8")
        (root / "b.txt").write_text("y", encoding="utf-8")
        global ROOT
        saved = ROOT
        ROOT = root
        try:
            h1 = hash_of([root / "a.txt", root / "b.txt"])
            (root / "b.txt").write_text("z", encoding="utf-8")
            h2 = hash_of([root / "a.txt", root / "b.txt"])
            results.append(("the inputs hash changes when an input changes", h1 != h2 and len(h1) == 64))
        finally:
            ROOT = saved
    # the live chapter 1 briefing, if the repository is here: it builds, carries every section, names its inputs
    if TREATMENT.exists() and (STORYFORM / "a.json").exists():
        text = build(1, "2026-10-26")
        heads = [ln for ln in text.split("\n") if ln.startswith("## ")]
        results.append(("the briefing of Kap 1 has its six sections in order", heads == ["## Entschieden", "## Vorgeschlagen", "## Quellen", "## Kontinuität", "## Offen — vor der ersten Szene zu beantworten", "## Szenen"]))
        results.append(("it carries a storypoint, the weaving row and a card", "Storypoint A-MC Concern: Memory" in text and "Route `hard-a`" in text and "Karte " in text))
        results.append(("it carries the treatment paragraph as [V] and an open Weiche", "- [V] Treatment, Kap 1" in text and "weiche.py answer" in text))
        results.append(("every bullet of the first four sections is tagged", all(re.match(r"^(- \[[KVSDL]\]|  |$|## |# |[^-])", ln) for ln in text.split("\n## Offen")[0].split("# Briefing")[1].split("\n"))))
        results.append(("it names its inputs and their hash", re.search(r"^inputs_hash: [0-9a-f]{64}$", text, re.M) is not None and "Manuscript/kanon.md" in text.split("---")[1]))
        import weiche
        answered = [wid for wid, path in weiche.sheets().items()
                    if weiche.frontmatter(path.read_text(encoding="utf-8")).get("status") == "beantwortet"
                    and 1 in set(weiche.chapters_of(wid)["development"]) | set(weiche.chapters_of(wid)["treatment"]) | set(weiche.chapters_of(wid)["sheet"])
                    and any(r["id"] == wid for r in weiche.kanon_rows())]
        rows = [{"id": "W90", "what": "A: Gewählt vom Autor im Gespräch der Sitzung x am 2026-10-27, als Option aus der vorgelegten Liste: „A: Löschung — Der Korridor verliert 0,73 m. In Szene 1 steht der Abschnitt auf der Löschliste.“"},
                {"id": "W91", "what": "Szene 2 braucht eine Zeile. Kap 1 hat drei Szenen."}]
        du = duties(rows)
        results.append(("a decided sentence naming a scene is a duty of that scene, with its answer, not its preamble (F10)",
                        [(d["scene"], d["id"]) for d in du] == [(1, "W90"), (2, "W91")]
                        and du[0]["sentence"] == "In Szene 1 steht der Abschnitt auf der Löschliste."
                        and du[0]["context"] == "A: Löschung — Der Korridor verliert 0,73 m." and "Gewählt" not in du[0]["context"]))
        ms = Path(tmp) / "ms"
        for d in ("figuren", "welt"):
            (ms / d).mkdir(parents=True)
        (ms / "welt" / "dkt.md").write_text('---\nname: Die Dual-Kernel-Theorie\nkind: voraussetzung\nkanon: ["033"]\nmatch: ["DKT"]\n---\n\n'
                                           '## Kanon\n\nVoraussetzung der Welt (033).\n\n## Was die Quellen sagen\n\n- viel\n', encoding="utf-8")
        (ms / "welt" / "stadt.md").write_text('---\nname: Stadt\nkind: welt\nstatus: ruht\nruht_seit: "033"\nmatch: ["Stadt"]\n---\n\n## Kanon\n\nKW1.\n', encoding="utf-8")
        pl, pf = premise_lines(ms)
        results.append(("a premise card is a [K] line of every briefing, with its decision and its Kanon block only (033)",
                        pl == ["- [K] Voraussetzung der Welt — Die Dual-Kernel-Theorie (033): Voraussetzung der Welt (033). (`Manuscript/welt/dkt.md`)"]))
        results.append(("a resting card is not a holding card", [c["rel"] for c in holding_cards(ms)] == ["welt/dkt.md"]))
        rows2 = [{"id": "Kernwelten", "what": "Vier Welten, Kap 1–13.", "date": "", "where": ""}, {"id": "W9", "what": "Kap 1 beginnt kalt.", "date": "", "where": ""}]
        results.append(("a resting canon row is not a row the briefing stands on, even when it names the chapter",
                        [r["id"] for r in decided_rows(1, rows2, rest={"Kernwelten": {"since": "033"}})] == ["W9"]))
        decided = text.split("## Vorgeschlagen")[0]
        results.append(("every answered Weiche touching Kap 1 stands under Entschieden, whatever its words name",
                        all(f"**{wid}**" in decided for wid in answered)))
        early = "Mich" "ael"
        results.append(("it writes no early name", early not in text and "Isab" "ella" not in text))
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
    if verb == "selftest":
        return selftest()
    if verb == "kap" and rest:
        p = write(int(re.sub(r"\D", "", rest[0])))
        print(f"wrote {p.relative_to(ROOT)}")
        return 0
    if verb == "check":
        ns = [int(re.sub(r"\D", "", rest[1]))] if len(rest) > 1 and rest[0] == "kap" else \
            sorted(int(p.parent.name.split("-")[1]) for p in MANUSCRIPT.glob("kap-*/briefing.md"))
        bad = 0
        for n in ns:
            st, why = status(n)
            print(f"{st:8} Kap {n}: {why}")
            bad += st == "behind"
        print(f"{len(ns)} briefing(s), {bad} behind")
        return 1 if bad else 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
