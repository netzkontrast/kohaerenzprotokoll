#!/usr/bin/env python3
"""The novel's two Dramatica storyforms: check them, compare them with the derivation, and write what follows.

The storyforms live in `Plan/storyform/a.json` and `b.json` — the source of truth, every value the author's
decision, a source's position or a derivation, and every value carrying its provenance (decision 025). This
script reads them and writes nothing else into them:

  * refuses a storyform `dramatica.check` finds an error in (the chart's rules R1–R8);
  * refuses a value without provenance, and a provenance naming no value;
  * compares the values with what `dramatica.derive` fixes from the twelve answers (D1–D7) and reports every
    disagreement — a disagreement is not an error, it is a question for the author;
  * refuses a storyweaving scaffold (`weave.json`, step 23) that leaves a signpost unwoven, a bridge without one
    of the five anchors, a bridge band overrun, a hard-b count the author did not set, or a chapter without provenance;
  * writes `Plan/storyform/overview.md` (generated — never edit it) and `Plan/storyform/ncp/storyform-{a,b}.ncp.json`
    (NCP 1.3.0, the shape of the ncp-author skill; status `draft`, nothing undecided is filled in).

    python3 scripts/storyform.py            # check, compare, write
    python3 scripts/storyform.py --check    # exit 1 if anything is refused or a written file is stale
    python3 scripts/storyform.py selftest   # the checks can fail

It does not decide anything, choose a signpost (their function is licensed Dramatica intelligence, not
derivable here), or write prose. How a change is made — one question to the author at a time — is the
`storyform` skill's.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dramatica  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "Plan" / "storyform"
TL = {"MC": "Main Character", "IC": "Influence Character", "OS": "Objective Story", "RS": "Relationship Story"}
PID = {k: f"persp_{v.lower().replace(' ', '_')}" for k, v in TL.items()}
DYN_ORDER = ["story_driver", "story_outcome", "story_judgment", "story_limit", "problem_solving_style",
             "main_character_resolve", "influence_character_resolve", "main_character_growth",
             "main_character_approach"]
PLOT = {"goal": "Story Goal", "requirements": "Story Requirements", "consequence": "Story Consequence",
        "forewarnings": "Story Forewarnings", "costs": "Story Costs", "dividends": "Story Dividends",
        "prerequisites": "Story Prerequisites", "preconditions": "Story Preconditions"}
# the 1999 chart's spelling -> NCP 1.3.0's canonical_narrative_function
NCP_NAME = {"Consideration": "Consider", "Reconsideration": "Reconsider", "Non-Acceptance": "Non-acceptance",
            "Non-Accurate": "Non-accurate", "Reevaluation": "Re-evaluation", "Self-Aware": "Self-aware",
            "Self-Interest": "Self Interest", "Morality": "Selflessness"}
ACTS = ["Akt I", "Akt II", "Akt III", "Vortex"]


def nf(name):
    return NCP_NAME.get(name, name)


def leaves(sf):
    """Every value the storyform states, by path (`MC.problem`, `dynamics.story_limit`, `classes`)."""
    out = {"classes": sf["classes"]}
    out.update({f"dynamics.{k}": v for k, v in sf["dynamics"].items()})
    for t in TL:
        out.update({f"{t}.{k}": v for k, v in sf[t].items()})
    out.update({f"plot.{k}": v for k, v in sf["plot"].items()})
    out.update({k: sf[k] for k in ("logline", "genre") if sf.get(k)})
    return out


def twelve(sf):
    d = sf["dynamics"]
    return {"limit": d["story_limit"], "resolve": d["main_character_resolve"], "outcome": d["story_outcome"],
            "judgment": d["story_judgment"], "growth": d["main_character_growth"], "driver": d["story_driver"],
            "approach": d["main_character_approach"], "style": d["problem_solving_style"],
            "os_domain": sf["classes"]["OS"], "os_concern": sf["OS"]["concern"], "os_issue": sf["OS"]["issue"],
            "os_problem": sf["OS"]["problem"]}


def compare(sf):
    """Where the stated values and the derivation D1–D7 disagree, and the derivation's own violations."""
    out, bad = dramatica.derive(twelve(sf))
    diff = [f"classes: stated {sf['classes']}, derived {out['classes']}"] if sf["classes"] != out["classes"] else []
    for t in ("MC", "IC", "OS"):
        for k, v in out[t].items():
            if k in sf[t] and sf[t][k] != v:
                diff.append(f"{t}.{k}: stated {sf[t][k]}, derived {v}")
    rs = out["RS"]
    for k, v in (("concern", rs["concern(D6)"]), ("issue", rs["issue(D7)"]), ("problem", rs["problem"]),
                 ("solution", rs["solution"])):
        if k in sf["RS"] and sf["RS"][k] != v:
            diff.append(f"RS.{k}: stated {sf['RS'][k]}, derived {v}")
    return diff, bad


def audit(sf):
    """(errors, disagreements) for one storyform."""
    errors, _ = dramatica.check(sf)
    have, prov = leaves(sf), sf.get("provenance", {})
    errors += [f"no provenance for {p}" for p in have if p not in prov]
    errors += [f"provenance for {p}, which states no value" for p in prov if p not in have]
    diff, bad = compare(sf)
    return errors, bad + diff


def ncp(sf):
    k, tx = sf["storyform"].lower(), sf["texts"]
    src = f"Entscheidung des Autors ({sf['decision']})"
    persp = [{"id": PID[t], "author_structural_pov": tx["perspectives"][t][0], "summary": tx["perspectives"][t][1],
              "storytelling": tx["perspectives"][t][2]} for t in TL]
    dyn = [{"id": f"dyn_{d}", "dynamic": d, "vector": sf["dynamics"][d], "summary": f"{d} = {sf['dynamics'][d]}",
            "storytelling": f"{src}; {sf['provenance'][f'dynamics.{d}']}."} for d in DYN_ORDER]
    sps = []

    def sp(appr, fn, tl, illus, story):
        sps.append({"id": f"sp_{len(sps) + 1:02d}", "appreciation": appr, "narrative_function": nf(fn),
                    **({"throughline": TL[tl]} if tl else {}), "illustration": illus or appr,
                    "summary": f"{appr}: {nf(fn)}", "storytelling": story,
                    "perspectives": [{"perspective_id": PID[tl or "OS"]}]})

    il, prov = tx["illustrations"], sf["provenance"]
    for t in TL:
        s, why = sf[t], tx["why"][t]
        sp(f"{TL[t]} Domain", sf["classes"][t], t, tx["perspectives"][t][2], why)
        for key, part in (("concern", "Concern"), ("issue", "Issue"), ("problem", "Problem"), ("solution", "Solution"),
                          ("focus", "Symptom"), ("direction", "Response")):
            if key in s:
                story = f"{why} Herkunft: {prov[f'{t}.{key}']}."
                if key == "issue":
                    _, _, vs = dramatica.under(s["concern"])
                    story += f" Gegenpol (Counterpoint): {nf(dramatica.pair_of(s['issue'], [v for v, _ in vs]))}."
                sp(f"{TL[t]} {part}", s[key], t, il.get(f"{t} {part}", il.get(f"{t} {key.title()}", "")), story)
    resolve = sf["dynamics"]["main_character_resolve"]
    crucial = sf["OS"]["problem"] if resolve == "change" else sf["OS"]["solution"]
    sp("Main Character Pivotal Element", crucial, "MC", "Das Crucial Element: das OS-Element, auf dem die Hauptfigur sitzt.",
       "Change → das OS-Problem, das die Hauptfigur aufgibt; Steadfast → die OS-Lösung, an der sie festhält.")
    plot = {"goal": sf["OS"]["concern"], **sf["plot"]}
    for key, appr in PLOT.items():
        if key in plot:
            story = "Das Ziel liegt auf dem OS-Concern." if key == "goal" else f"Herkunft: {prov[f'plot.{key}']}."
            if key == "consequence":
                story += (" Stop-Story: die Folgen laufen schon." if sf["dynamics"]["main_character_growth"] == "stop"
                          else " Start-Story: die Folgen drohen nur.")
            sp(appr, plot[key], None, il.get("Story Goal") if key == "goal" else tx["plot"].get(key, ""), story)
    beats = []
    for t in TL:
        for i, typ in enumerate(sf[t].get("signposts", []), 1):
            beats.append({"id": f"beat_{t.lower()}_signpost_{i}", "scope": "signpost", "sequence": i, "throughline": TL[t],
                          "appreciation": f"{TL[t]} Signpost {i}", "narrative_function": nf(typ),
                          "summary": tx["signposts"].get(f"{t}.{typ}", tx["signposts"].get(typ, typ)),
                          "storytelling": f"{sf['chapters'][str(i)]}. Herkunft: {prov[f'{t}.signposts']}; nicht berechnet.",
                          "perspectives": [{"perspective_id": PID[t]}]})
    return {"schema_version": "1.3.0", "story": {
        "id": f"story_kp_storyform_{k}", "title": "Kohärenz Protokoll — " + sf["title"], "logline": sf.get("logline", ""), "genre": sf.get("genre", ""),
        "created_at": "2026-10-05T00:00:00Z",
        "narratives": [{"id": f"narrative-{k}", "title": sf["title"], "status": "draft",
                        "subtext": {"perspectives": persp, "players": [], "dynamics": dyn, "storypoints": sps,
                                    "storybeats": beats},
                        "storytelling": {"overviews": [], "moments": []}}]}}


def overview(forms):
    a, b = forms
    L = ["# Die Storyforms — Übersicht", "",
         "*Generiert von `python3 scripts/storyform.py` aus `a.json` und `b.json`. Nicht von Hand ändern — eine Änderung "
         "geht in die JSON-Datei, mit Herkunft (Skill `storyform`).*", "",
         f"**Prämisse:** „{a['premise']}\"", "",
         "## Die zwölf Antworten", "", "| | " + a["title"] + " | " + b["title"] + " |", "|---|---|---|"]
    for k in twelve(a):
        L.append(f"| {k} | {twelve(a)[k]} | {twelve(b)[k]} |")
    for sf in forms:
        L += ["", f"## {sf['title']}", ""]
        L += [f"**Logline:** „{sf['logline']}\"", ""] if sf.get("logline") else []
        L += [f"**Genre:** {sf['genre']}", ""] if sf.get("genre") else []
        L += ["| Strang | Klasse | Concern | Issue | Problem → Solution | Focus → Direction | Akte |", "|---|---|---|---|---|---|---|"]
        for t in TL:
            s = sf[t]
            L.append(f"| {t} | {sf['classes'][t]} | {s.get('concern', '—')} | {s.get('issue', '—')} | "
                     f"{s.get('problem', '—')} → {s.get('solution', '—')} | {s.get('focus', '—')} → {s.get('direction', '—')} | "
                     f"{' → '.join(s.get('signposts', [])) or '—'} |")
        plot = {"goal": sf["OS"]["concern"], **sf["plot"]}
        L += ["", "Plot: " + " · ".join(f"{k} **{v}**" for k, v in plot.items()), "",
              "Besetzung: " + "; ".join(f"{p['name']} — {p['role']}" + (f" ({', '.join(p['os_elements'])})" if p["os_elements"] else "")
                                       for p in sf["players"]),
              "", "Offen: " + "; ".join(sf["open"])]
        errors, notes = audit(sf)
        L += ["", "Gegen die Ableitung D1–D7 (`dramatica.py derive`): " + ("stimmt überein." if not notes else
              "; ".join(notes))]
    L += ["", "Akte und Kapitel: " + " · ".join(f"{ACTS[int(i) - 1]} = {v}" for i, v in a["chapters"].items()), ""]
    return "\n".join(L)


ROUTES = {"hard-a", "hard-b", "bridge"}


def act_of(weave, n):
    """The act (1–4) a chapter's signposts belong to; B's prologue (Kap 0) is B's act 1; None outside the acts."""
    for k, (lo, hi) in weave["acts"].items():
        if lo <= n <= hi:
            return int(k)
    return None


def weave_audit(weave, forms):
    """Errors in the storyweaving scaffold `weave.json` (decision 025 step 23); [] when it holds."""
    errors, ch = [], weave["chapters"]
    missing = [n for n in range(41) if str(n) not in ch]
    if missing:
        errors.append(f"chapters missing: {missing}")
    for key, c in ch.items():
        n = int(key)
        if c["route"] not in ROUTES:
            errors.append(f"Kap {n}: route {c['route']!r} is none of {sorted(ROUTES)}")
        if (c["route"] == "bridge") != (c["anchor"] is not None):
            errors.append(f"Kap {n}: a bridge names an anchor, nothing else does")
        if c["anchor"] is not None and c["anchor"] not in weave["anchors"]:
            errors.append(f"Kap {n}: anchor {c['anchor']!r} is not one of the five")
        for side in ("A", "B"):
            bad = [t for t in c[side] if t not in TL]
            if bad:
                errors.append(f"Kap {n}: {side} names {bad}, not a throughline")
        inside = act_of(weave, n) is not None or n == weave["b_prologue"]
        if inside and c["route"] in ("hard-a", "bridge") and not c["A"]:
            errors.append(f"Kap {n}: route {c['route']} carries no throughline of A")
        if inside and c["route"] in ("hard-b", "bridge") and not c["B"]:
            errors.append(f"Kap {n}: route {c['route']} carries no throughline of B")
        if n == weave["b_prologue"] and c["A"]:
            errors.append(f"Kap {n}: the prologue is B's alone")
    for k in weave["acts"]:
        for side in ("A", "B"):
            nums = [n for n in map(int, ch) if act_of(weave, n) == int(k) or (side == "B" and k == "1" and n == weave["b_prologue"])]
            have = {t for n in nums for t in ch[str(n)][side]}
            if have != set(TL):
                errors.append(f"act {k}: {side} never carries {sorted(set(TL) - have)} — its signpost goes unwoven")
    for block, want in weave["bands"].items():
        lo, hi = map(int, block.split("-"))
        nums = [n for n in range(lo, hi + 1) if str(n) in ch]
        share = 100 * sum(ch[str(n)]["route"] == "bridge" for n in nums) / max(len(nums), 1)
        if abs(share - want) > weave["band_tolerance"]:
            errors.append(f"Kap {block}: bridges {share:.0f} %, the band is {want} ± {weave['band_tolerance']}")
    for k, want in weave["hard_b"].items():
        nums = [n for n in map(int, ch) if (n == weave["b_prologue"] if k == "0" else act_of(weave, n) == int(k) and n != weave["b_prologue"])]
        got = sum(ch[str(n)]["route"] == "hard-b" for n in nums)
        if got != want:
            errors.append(f"act {k}: {got} hard-b chapters, the author set {want}")
    prov = weave["provenance"]["chapters"]
    errors += [f"Kap {n}: no provenance" for n in ch if n not in prov]
    errors += [f"provenance for Kap {n}, which the weave does not have" for n in prov if n not in ch]
    return errors


def weave_table(weave, forms):
    a, b = forms
    L = ["", "## Storyweaving (Gerüst)", "",
         "Aus `weave.json` (Entscheidung 025, Schritt 23). Route nach dem Skill chapter-draft-engine: hard-a = Kael "
         "und die Alters, hard-b = AEGIS als Ich (W6 C), bridge = beide Ebenen in einer Szene. Ein Strang steht mit "
         "dem Signpost seines Akts. Bestätigt je Akt: "
         + ", ".join(f"{k} {'ja' if v else 'nein'}" for k, v in weave["approved"].items()) + ".", "",
         "| Kap | Akt | Route | A | B | Anker |", "|---|---|---|---|---|---|"]
    for n in range(41):
        c = weave["chapters"].get(str(n))
        if not c:
            continue
        k = act_of(weave, n) or (1 if n == weave["b_prologue"] else None)
        sp = lambda sf, t: f"{t}·{sf[t]['signposts'][k - 1]}" if k else t
        L.append(f"| {n} | {k or '—'} | {c['route']} | {', '.join(sp(a, t) for t in c['A']) or '—'} | "
                 f"{', '.join(sp(b, t) for t in c['B']) or '—'} | {c['anchor'] or '—'} |")
    L += ["", "Offen: " + "; ".join(weave["open"])]
    return L


def load_weave():
    p = HOME / "weave.json"
    return json.loads(p.read_text()) if p.exists() else None


def load():
    return [json.load(open(HOME / f"{k}.json")) for k in "ab"]


def run(check_only=False):
    forms, failed = load(), False
    for sf in forms:
        errors, notes = audit(sf)
        for e in errors:
            print(f"ERROR {sf['storyform']}: {e}")
        for n in notes:
            print(f"note  {sf['storyform']}: {n}")
        failed |= bool(errors)
    weave = load_weave()
    for e in weave_audit(weave, forms) if weave else []:
        print(f"ERROR weave: {e}")
        failed = True
    if failed:
        print("refused: nothing written")
        return 1
    text = overview(forms)
    if weave:
        text = text.rstrip("\n") + "\n" + "\n".join(weave_table(weave, forms)) + "\n"
    want = {HOME / "overview.md": text}
    for sf in forms:
        want[HOME / "ncp" / f"storyform-{sf['storyform'].lower()}.ncp.json"] = json.dumps(ncp(sf), ensure_ascii=False, indent=2) + "\n"
    stale = [p for p, text in want.items() if not p.exists() or p.read_text() != text]
    if check_only:
        for p in stale:
            print(f"STALE {p.relative_to(ROOT)} — run python3 scripts/storyform.py")
        print("ok" if not stale else f"{len(stale)} stale")
        return 1 if stale else 0
    for p, text in want.items():
        p.parent.mkdir(exist_ok=True)
        p.write_text(text)
    print(f"ok — wrote {len(want)} files ({len(stale)} changed)")
    return 0


def selftest():
    fails = []
    good = load()[0]
    if audit(good)[0]:
        fails.append(f"the live storyform A is refused: {audit(good)[0]}")
    broken = json.loads(json.dumps(good))
    broken["MC"]["problem"] = "Avoid"                       # not under Memory: R5
    if not any("R5" in e for e in audit(broken)[0]):
        fails.append("an element outside its concern was accepted")
    bare = json.loads(json.dumps(good))
    bare["provenance"].pop("MC.issue")
    if not any("no provenance for MC.issue" in e for e in audit(bare)[0]):
        fails.append("a value without provenance was accepted")
    ghost = json.loads(json.dumps(good))
    ghost["provenance"]["MC.ghost"] = "x"
    if not any("states no value" in e for e in audit(ghost)[0]):
        fails.append("a provenance without a value was accepted")
    drift = json.loads(json.dumps(good))
    drift["MC"].update({"issue": "Truth"})                  # still legal by the chart? no — Inertia is under Suspicion
    if not audit(drift)[0] and not audit(drift)[1]:
        fails.append("a changed issue went unnoticed")
    weave = load_weave()
    if weave:
        forms = load()
        if weave_audit(weave, forms):
            fails.append(f"the live weave is refused: {weave_audit(weave, forms)[:2]}")
        for name, edit, want in [
                ("a throughline left unwoven", lambda w: [w["chapters"][str(n)].update(A=["MC"]) for n in range(1, 14)
                                                          if w["chapters"][str(n)]["A"]], "never carries"),
                ("a bridge without an anchor", lambda w: w["chapters"]["13"].update(anchor=None), "anchor"),
                ("a band overrun", lambda w: [w["chapters"][str(n)].update(route="bridge", anchor="Riss-Szene", B=["MC"])
                                              for n in (1, 2, 3, 4)], "the band is"),
                ("a hard-b count the author did not set", lambda w: w["chapters"]["6"].update(route="hard-a", A=["MC"]),
                 "the author set"),
                ("a chapter without provenance", lambda w: w["provenance"]["chapters"].pop("7"), "no provenance")]:
            w = json.loads(json.dumps(weave))
            edit(w)
            if not any(want in e for e in weave_audit(w, forms)):
                fails.append(f"{name} was accepted")
    doc = ncp(good)
    beats = doc["story"]["narratives"][0]["subtext"]["storybeats"]
    if len({(x["throughline"], x["sequence"]) for x in beats}) != len(beats):
        fails.append("NCP signposts collide")
    for f in fails:
        print("FAIL", f)
    print("held" if not fails else f"FAILED ({len(fails)})")
    return 0 if not fails else 1


if __name__ == "__main__":
    arg = sys.argv[1:]
    if arg[:1] == ["selftest"]:
        sys.exit(selftest())
    sys.exit(run(check_only="--check" in arg))
