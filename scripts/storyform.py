#!/usr/bin/env python3
"""The novel's two Dramatica storyforms: check them, compare them with the derivation, and write what follows.

The storyforms live in `Plan/storyform/a.json` and `b.json` — the source of truth, every value the author's
decision, a source's position or a derivation, and every value carrying its provenance (decision 025). This
script reads them and writes nothing else into them:

  * refuses a storyform `dramatica.check` finds an error in (the chart's rules R1–R8);
  * refuses a value without provenance, and a provenance naming no value;
  * compares the values with what `dramatica.derive` fixes from the twelve answers (D1–D7) and reports every
    disagreement — a disagreement is not an error, it is a question for the author;
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
        "id": f"story_kp_storyform_{k}", "title": "Kohärenz Protokoll — " + sf["title"], "logline": "", "genre": "",
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
        L += ["", f"## {sf['title']}", "",
              "| Strang | Klasse | Concern | Issue | Problem → Solution | Focus → Direction | Akte |", "|---|---|---|---|---|---|---|"]
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
    if failed:
        print("refused: nothing written")
        return 1
    want = {HOME / "overview.md": overview(forms)}
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
