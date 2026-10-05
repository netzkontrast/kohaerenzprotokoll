#!/usr/bin/env python3
"""The Dramatica Table of Story Elements as data, and a checker for a storyform.

The table is transcribed by hand from Screenplay Systems' own charts:

  * „Dramatica Table of Story Elements", © 1995, 1999 Screenplay Systems
    (https://www.storymind.com/dramatica/downloads/structure_chart.pdf) — the
    arrangement of every variation and element inside each class;
  * „Reference Part 1 — Appendices", Alpha Documentation, 1995
    (https://www.storymind.com/content/downloads/files/Dramatica%20Charts%20and%20Tables.pdf)
    — the names of the 16 types and the variations per type, as plain lists.

Every quad is written top-left, top-right, bottom-left, bottom-right, as the
chart prints it; the diagonals are the dynamic pairs. `selftest` proves the
transcription can fail: each class must hold all 64 elements exactly once, and
every element pair named on the chart must sit on a diagonal.

The newer Narrative First / Subtxt model (Justification Model v5.3) keeps this
nesting (Narrative First's own analyses use Progress → Fact/Fantasy) but orders
signposts and progressions differently, and that order is not published; this
file computes **no signpost order**.

What `check` enforces — only rules the chart itself carries:
  R1  four throughlines, each class once (Dramatica H1/H2)
  R2  MC and IC one dynamic pair of classes, OS and RS the other (H3)
  R3  a concern is a type of its throughline's class
  R4  an issue is a variation under that concern; the counterpoint is its pair
  R5  problem, solution, focus, direction lie under that concern; problem and
      solution are a dynamic pair, focus and direction the other pair of the
      same element quad
  R6  IC resolve is the opposite of MC resolve
  R7  the four signposts of a throughline are the four types of its class
  R8  each plot story point (requirements, consequence, forewarnings, …) is a type
What it does not enforce, because neither chart states it: how the four
throughlines' concerns relate to each other, which element is crucial, and the
plot story points beyond their being types.

    python3 scripts/dramatica.py selftest
    python3 scripts/dramatica.py check <spec.json>
    python3 scripts/dramatica.py under <Type>            # variations and element quads of a type
    python3 scripts/dramatica.py where <Element|Variation>
    python3 scripts/dramatica.py derive <twelve.json>   # what the engine derives (D1–D7, see below)
"""
import json, sys

# class -> [(type, alias, [(variation, [e_tl, e_tr, e_bl, e_br]) x4 in TL,TR,BL,BR])] in TL,TR,BL,BR
TABLE = {
  "Universe": [  # chart: Situation
    ("Past", "Past", [
      ("Fate", ["Knowledge", "Order", "Chaos", "Thought"]),
      ("Prediction", ["Actuality", "Inertia", "Change", "Perception"]),
      ("Interdiction", ["Ability", "Equity", "Inequity", "Desire"]),
      ("Destiny", ["Aware", "Projection", "Speculation", "Self-Aware"])]),
    ("Progress", "How Things Are Changing", [
      ("Fact", ["Proven", "Accurate", "Non-Accurate", "Unproven"]),
      ("Security", ["Effect", "Result", "Process", "Cause"]),
      ("Threat", ["Theory", "Expectation", "Determination", "Hunch"]),
      ("Fantasy", ["Trust", "Ending", "Unending", "Test"])]),
    ("Future", "Future", [
      ("Openness", ["Consideration", "Faith", "Disbelief", "Reconsideration"]),
      ("Delay", ["Pursuit", "Support", "Oppose", "Avoid"]),
      ("Choice", ["Logic", "Conscience", "Temptation", "Feeling"]),
      ("Preconception", ["Control", "Help", "Hinder", "Uncontrolled"])]),
    ("Present", "Present", [
      ("Work", ["Certainty", "Deduction", "Induction", "Potentiality"]),
      ("Attract", ["Proaction", "Acceptance", "Non-Acceptance", "Reaction"]),
      ("Repel", ["Probability", "Reduction", "Production", "Possibility"]),
      ("Attempt", ["Inaction", "Evaluation", "Reevaluation", "Protection"])]),
  ],
  "Physics": [  # chart: Activity
    ("Understanding", "Understanding", [
      ("Instinct", ["Knowledge", "Ability", "Desire", "Thought"]),
      ("Senses", ["Actuality", "Aware", "Self-Aware", "Perception"]),
      ("Interpretation", ["Order", "Equity", "Inequity", "Chaos"]),
      ("Conditioning", ["Inertia", "Projection", "Speculation", "Change"])]),
    ("Doing", "Doing", [
      ("Wisdom", ["Proven", "Theory", "Hunch", "Unproven"]),
      ("Skill", ["Effect", "Trust", "Test", "Cause"]),
      ("Experience", ["Accurate", "Expectation", "Determination", "Non-Accurate"]),
      ("Enlightenment", ["Result", "Ending", "Unending", "Process"])]),
    ("Obtaining", "Obtaining", [
      ("Approach", ["Consideration", "Logic", "Feeling", "Reconsideration"]),
      ("Self-Interest", ["Pursuit", "Control", "Uncontrolled", "Avoid"]),
      ("Morality", ["Faith", "Conscience", "Temptation", "Disbelief"]),
      ("Attitude", ["Support", "Help", "Hinder", "Oppose"])]),
    ("Learning", "Gathering Information", [
      ("Prerequisites", ["Certainty", "Probability", "Possibility", "Potentiality"]),
      ("Strategy", ["Proaction", "Inaction", "Protection", "Reaction"]),
      ("Analysis", ["Deduction", "Reduction", "Production", "Induction"]),
      ("Preconditions", ["Acceptance", "Evaluation", "Reevaluation", "Non-Acceptance"])]),
  ],
  "Psychology": [  # chart: Manipulation
    ("Conceptualizing", "Developing A Plan", [
      ("State of Being", ["Knowledge", "Inertia", "Change", "Thought"]),
      ("Situation", ["Actuality", "Order", "Chaos", "Perception"]),
      ("Circumstances", ["Aware", "Equity", "Inequity", "Self-Aware"]),
      ("Sense of Self", ["Ability", "Projection", "Speculation", "Desire"])]),
    ("Being", "Playing A Role", [
      ("Knowledge", ["Proven", "Result", "Process", "Unproven"]),
      ("Ability", ["Effect", "Accurate", "Non-Accurate", "Cause"]),
      ("Desire", ["Trust", "Expectation", "Determination", "Test"]),
      ("Thought", ["Theory", "Ending", "Unending", "Hunch"])]),
    ("Becoming", "Changing One's Nature", [
      ("Rationalization", ["Consideration", "Support", "Oppose", "Reconsideration"]),
      ("Commitment", ["Pursuit", "Faith", "Disbelief", "Avoid"]),
      ("Responsibility", ["Control", "Conscience", "Temptation", "Uncontrolled"]),
      ("Obligation", ["Logic", "Help", "Hinder", "Feeling"])]),
    ("Conceiving", "Conceiving An Idea", [
      ("Permission", ["Certainty", "Acceptance", "Non-Acceptance", "Potentiality"]),
      ("Need", ["Proaction", "Deduction", "Induction", "Reaction"]),
      ("Expediency", ["Inaction", "Reduction", "Production", "Protection"]),
      ("Deficiency", ["Probability", "Evaluation", "Reevaluation", "Possibility"])]),
  ],
  "Mind": [  # chart: Fixed Attitude
    ("Memory", "Memories", [
      ("Truth", ["Knowledge", "Actuality", "Perception", "Thought"]),
      ("Evidence", ["Ability", "Aware", "Self-Aware", "Desire"]),
      ("Suspicion", ["Order", "Inertia", "Change", "Chaos"]),
      ("Falsehood", ["Equity", "Projection", "Speculation", "Inequity"])]),
    ("Preconscious", "Impulsive Responses", [
      ("Value", ["Proven", "Effect", "Cause", "Unproven"]),
      ("Confidence", ["Theory", "Trust", "Test", "Hunch"]),
      ("Worry", ["Accurate", "Result", "Process", "Non-Accurate"]),
      ("Worth", ["Expectation", "Ending", "Unending", "Determination"])]),
    ("Subconscious", "Innermost Desires", [
      ("Closure", ["Consideration", "Pursuit", "Avoid", "Reconsideration"]),
      ("Hope", ["Logic", "Control", "Uncontrolled", "Feeling"]),
      ("Dream", ["Faith", "Support", "Oppose", "Disbelief"]),
      ("Denial", ["Conscience", "Help", "Hinder", "Temptation"])]),
    ("Conscious", "Contemplations", [
      ("Investigation", ["Certainty", "Proaction", "Reaction", "Potentiality"]),
      ("Appraisal", ["Probability", "Inaction", "Protection", "Possibility"]),
      ("Reappraisal", ["Deduction", "Acceptance", "Non-Acceptance", "Induction"]),
      ("Doubt", ["Reduction", "Evaluation", "Reevaluation", "Production"])]),
  ],
}

CLASS_PAIRS = [("Universe", "Mind"), ("Physics", "Psychology")]
THROUGHLINES = ["MC", "IC", "OS", "RS"]
# the element dynamic pairs, as the 1995 dictionary names them (selftest checks the chart against them)
ELEMENT_PAIRS = [("Knowledge", "Thought"), ("Ability", "Desire"), ("Actuality", "Perception"),
  ("Aware", "Self-Aware"), ("Order", "Chaos"), ("Equity", "Inequity"), ("Inertia", "Change"),
  ("Projection", "Speculation"), ("Proven", "Unproven"), ("Theory", "Hunch"), ("Effect", "Cause"),
  ("Trust", "Test"), ("Accurate", "Non-Accurate"), ("Expectation", "Determination"),
  ("Result", "Process"), ("Ending", "Unending"), ("Consideration", "Reconsideration"),
  ("Logic", "Feeling"), ("Pursuit", "Avoid"), ("Control", "Uncontrolled"), ("Certainty", "Potentiality"),
  ("Probability", "Possibility"), ("Proaction", "Reaction"), ("Inaction", "Protection"),
  ("Faith", "Disbelief"), ("Conscience", "Temptation"), ("Support", "Oppose"), ("Help", "Hinder"),
  ("Deduction", "Induction"), ("Reduction", "Production"), ("Acceptance", "Non-Acceptance"),
  ("Evaluation", "Reevaluation")]
VARIATION_PAIRS = [("Fate", "Destiny"), ("Prediction", "Interdiction"), ("Fact", "Fantasy"),
  ("Security", "Threat"), ("Truth", "Falsehood"), ("Evidence", "Suspicion"), ("Closure", "Denial"),
  ("Hope", "Dream"), ("Morality", "Self-Interest"), ("Approach", "Attitude")]
TYPE_PAIRS = [("Past", "Present"), ("Progress", "Future"), ("Memory", "Conscious"),
  ("Understanding", "Learning"), ("Doing", "Obtaining"), ("Being", "Becoming")]


def diag(quad):
    """The two dynamic pairs of a TL,TR,BL,BR quad."""
    return {frozenset((quad[0], quad[3])), frozenset((quad[1], quad[2]))}


def pair_of(name, quad):
    for p in diag(quad):
        if name in p:
            return next(iter(p - {name}))
    return None


def index():
    types, variations = {}, {}
    for cls, ts in TABLE.items():
        for t, alias, vs in ts:
            types[t] = (cls, alias, vs)
            for v, els in vs:
                variations[(cls, v)] = (t, els)
    return types, variations


def type_quad(cls):
    return [t for t, _, _ in TABLE[cls]]


def under(t):
    """Variations and the 16 elements under a type, as element quads."""
    types, _ = index()
    cls, alias, vs = types[t]
    return cls, alias, vs


def where(name):
    out = []
    for cls, ts in TABLE.items():
        for t, _, vs in ts:
            for v, els in vs:
                if v == name:
                    out.append(f"variation  {cls} / {t} / {v}  (pair: {pair_of(v, [x for x, _ in vs])})")
                if name in els:
                    out.append(f"element    {cls} / {t} / {v}  (pair: {pair_of(name, els)})")
    return out


def selftest():
    fails = []
    for cls, ts in TABLE.items():
        els = [e for _, _, vs in ts for _, q in vs for e in q]
        if len(els) != 64 or len(set(els)) != 64:
            fails.append(f"{cls}: {len(set(els))} distinct of {len(els)} elements, want 64/64")
        if len(ts) != 4 or any(len(vs) != 4 for _, _, vs in ts):
            fails.append(f"{cls}: not four types of four variations")
        for t, _, vs in ts:
            for v, q in vs:
                for a, b in ELEMENT_PAIRS:
                    if a in q and b in q and frozenset((a, b)) not in diag(q):
                        fails.append(f"{cls}/{t}/{v}: {a}–{b} not on a diagonal")
                    if (a in q) != (b in q):
                        fails.append(f"{cls}/{t}/{v}: {a} and {b} split across quads")
            vq = [v for v, _ in vs]
            for a, b in VARIATION_PAIRS:
                if a in vq and frozenset((a, b)) not in diag(vq):
                    fails.append(f"{cls}/{t}: variations {a}–{b} not on a diagonal")
        tq = type_quad(cls)
        for a, b in TYPE_PAIRS:
            if a in tq and frozenset((a, b)) not in diag(tq):
                fails.append(f"{cls}: types {a}–{b} not on a diagonal")
    allv = [v for ts in TABLE.values() for _, _, vs in ts for v, _ in vs]
    if len(allv) != 64 or len(set(allv)) != 64:
        fails.append(f"variations: {len(set(allv))} distinct of {len(allv)}, want 64/64")
    # the checker must catch a broken storyform: the sources' own Storyform A element chain
    bad = {"classes": {"MC": "Mind", "IC": "Universe", "OS": "Psychology", "RS": "Physics"},
           "MC": {"concern": "Memory", "issue": "Falsehood", "problem": "Avoid", "solution": "Pursuit"},
           "dynamics": {"main_character_resolve": "change"}}
    if not any("R5" in m for m in check(bad)[0]):
        fails.append("check() accepted Avoid under Memory")
    # derive() against the thread's worked example: OS Universe / Past / Fate / Knowledge
    base = {"os_domain": "Universe", "os_concern": "Past", "os_issue": "Fate", "os_problem": "Knowledge",
            "outcome": "success"}
    for r, ap, g, want in (("change", "do_er", "stop", ("Physics", "Instinct", "State of Being")),
                           ("change", "be_er", "start", ("Psychology", "State of Being", "Instinct")),
                           ("steadfast", "do_er", "stop", ("Physics", "Interpretation", "Circumstances")),
                           ("steadfast", "be_er", "start", ("Psychology", "Situation", "Senses"))):
        out, _ = derive(dict(base, resolve=r, approach=ap, growth=g))
        got = (out["classes"]["MC"], out["MC"]["issue"], out["IC"]["issue"])
        if got != want:
            fails.append(f"derive {r}/{ap}: {got}, the thread has {want}")
    for oc, want in (("success", "Inertia"), ("failure", "Knowledge")):
        out, _ = derive(dict(base, resolve="change", approach="do_er", growth="stop", outcome=oc))
        if out["RS"]["problem"] != want:
            fails.append(f"derive RS problem ({oc}): {out['RS']['problem']}, the thread has {want}")
    out, _ = derive(dict(base, resolve="change", approach="do_er", growth="stop"))
    if out["RS"]["issue(D7)"] != "Truth":
        fails.append(f"derive RS issue: {out['RS']['issue(D7)']}, the thread has Truth")
    if not derive(dict(base, resolve="change", approach="do_er", growth="start"))[1]:
        fails.append("derive accepted start + do_er with OS Universe (D1)")
    for f in fails:
        print("FAIL", f)
    print("held" if not fails else f"FAILED ({len(fails)})")
    return not fails


def check(spec):
    """Return (errors, notes) for a storyform spec (see README.md for the format)."""
    errors, notes = [], []
    types, variations = index()
    cls = spec.get("classes", {})
    if sorted(cls) != sorted(THROUGHLINES) or sorted(cls.values()) != sorted(TABLE):
        errors.append(f"R1 each throughline needs a class and each class is used once: {cls}")
        return errors, notes
    pair = {c: d for a, b in CLASS_PAIRS for c, d in ((a, b), (b, a))}
    if pair[cls["MC"]] != cls["IC"]:
        errors.append(f"R2 MC {cls['MC']} and IC {cls['IC']} are not a dynamic pair of classes")
    dyn = spec.get("dynamics", {})
    mcr, icr = dyn.get("main_character_resolve"), dyn.get("influence_character_resolve")
    if mcr:
        want = {"change": "steadfast", "steadfast": "change"}[mcr]
        if icr and icr != want:
            errors.append(f"R6 IC resolve {icr} with MC resolve {mcr}; must be {want}")
        elif not icr:
            notes.append(f"R6 IC resolve follows: {want}")
    for tl in THROUGHLINES:
        s = spec.get(tl, {})
        c = s.get("concern")
        if not c:
            notes.append(f"{tl}: concern open — any of {type_quad(cls[tl])}")
            continue
        if c not in types or types[c][0] != cls[tl]:
            errors.append(f"R3 {tl} concern {c} is not a type of {cls[tl]}")
            continue
        vs = types[c][2]
        vnames = [v for v, _ in vs]
        i = s.get("issue")
        if i:
            if i not in vnames:
                errors.append(f"R4 {tl} issue {i} is not under {c} ({', '.join(vnames)})")
            else:
                notes.append(f"{tl}: counterpoint of {i} is {pair_of(i, vnames)}")
        else:
            notes.append(f"{tl}: issue open — any of {vnames}")
        quads = {v: q for v, q in vs}
        p, so = s.get("problem"), s.get("solution")
        if p:
            home = [v for v, q in quads.items() if p in q]
            if not home:
                legal = [x for v, q in quads.items() for x in q]
                errors.append(f"R5 {tl} problem {p} is not under {c}; the 16 there: {', '.join(legal)}")
            else:
                q = quads[home[0]]
                want = pair_of(p, q)
                if so and so != want:
                    errors.append(f"R5 {tl} solution {so} is not the pair of {p} ({want})")
                rest = [x for x in q if x not in (p, want)]
                fo, di = s.get("focus"), s.get("direction")
                if fo or di:
                    if sorted([fo or "", di or ""]) != sorted(rest):
                        errors.append(f"R5 {tl} focus/direction {fo}/{di} are not the other pair {rest[0]}/{rest[1]}")
                else:
                    notes.append(f"{tl}: problem {p} / solution {want} sit under {home[0]}; "
                                 f"focus/direction are {rest[0]}/{rest[1]} in some order")
        else:
            notes.append(f"{tl}: problem open — one of the four element quads under {c}: "
                         + "; ".join(f"{v}: {'/'.join(q)}" for v, q in quads.items()))
        sp = s.get("signposts")
        if sp and sorted(sp) != sorted(type_quad(cls[tl])):
            errors.append(f"R7 {tl} signposts {sp} are not the four types of {cls[tl]}")
    for k, v in spec.get("plot", {}).items():
        if v not in types:
            errors.append(f"R8 plot story point {k} = {v} is not a type")
    return errors, notes


# --- what the engine derives from the twelve answers -------------------------------------------
# Reverse-engineered rules, NOT official (bobRaskoph, discuss.dramatica.com/t/499, 2016); see
# engine-rules.md. D1 is the one bit that halves 2^16 to the official 32 768 storyforms.
#   D1  Stop+Do-er or Start+Be-er -> OS in {Universe, Physics}; otherwise OS in {Mind, Psychology}
#   D2  Do-er -> MC in the external class of the MC/IC pair (Universe, Physics); Be-er -> internal
#   D3  Change: MC problem = OS problem; MC issue/concern = the variation/type above it in the MC
#       class; IC issue/concern = above it in the IC class
#   D4  Steadfast: MC focus/direction pair = the OS pair; MC issue/concern above it in the MC class,
#       MC problem = the element of the other pair in the same row as the OS problem
#   D3/D4 IC issue/concern = the variation/type above the MC problem in the IC class (both resolves;
#       checked against all four worked cases of the thread in selftest)
#   D5  RS problem: Outcome Failure -> the OS problem; Success -> in the RS class, the quad holding the
#       OS focus/direction pair, the element of the other pair in the same row as the OS problem
#   D6  RS concern = the type in the OS concern's quad position, in the RS class
#   D7  RS issue = the variation in the OS issue's quad position, under the RS concern (thread: Fate -> Truth)
# Not derived here (unknown): IC problem, RS issue when D5 leaves the D6 quad, focus vs direction
# order, plot story points, and every signpost.
EXTERNAL = {"Universe", "Physics"}
POS = {0: "TL", 1: "TR", 2: "BL", 3: "BR"}


def _home(cls, element):
    for t, _, vs in TABLE[cls]:
        for v, q in vs:
            if element in q:
                return t, v, q
    raise KeyError(element)


def derive(answers):
    """Derive what the rules D1-D6 fix from the twelve answers; return (values, violations)."""
    a, out, bad = answers, {}, []
    os_cls, grow, appr = a["os_domain"], a["growth"], a["approach"]
    want = {"Universe", "Physics"} if (grow, appr) in (("stop", "do_er"), ("start", "be_er")) else {"Mind", "Psychology"}
    if os_cls not in want:
        bad.append(f"D1 growth {grow} + approach {appr} needs OS in {sorted(want)}, not {os_cls}")
    pair = {c: d for x, y in CLASS_PAIRS for c, d in ((x, y), (y, x))}
    rs_cls = pair[os_cls]
    mi = [c for c in TABLE if c not in (os_cls, rs_cls)]
    mc_cls = next(c for c in mi if (c in EXTERNAL) == (appr == "do_er"))
    ic_cls = pair[mc_cls]
    out["classes"] = {"MC": mc_cls, "IC": ic_cls, "OS": os_cls, "RS": rs_cls}
    ot, ov, oq = _home(os_cls, a["os_problem"])
    if ot != a["os_concern"]:
        bad.append(f"OS problem {a['os_problem']} is not under OS concern {a['os_concern']}")
    osol = pair_of(a["os_problem"], oq)
    ofd = [x for x in oq if x not in (a["os_problem"], osol)]
    row = oq.index(a["os_problem"]) // 2
    out["OS"] = {"concern": ot, "issue": a["os_issue"], "problem": a["os_problem"], "solution": osol,
                 "focus/direction": ofd}
    if a["resolve"] == "change":
        t, v, _ = _home(mc_cls, a["os_problem"]); out["MC"] = {"concern": t, "issue": v, "problem": a["os_problem"],
                                                            "solution": osol}
        t, v, _ = _home(ic_cls, a["os_problem"]); out["IC"] = {"concern": t, "issue": v}
    else:
        t, v, q = _home(mc_cls, ofd[0])
        rest = [x for x in q if x not in ofd]
        p = next(x for x in rest if q.index(x) // 2 == row)
        out["MC"] = {"concern": t, "issue": v, "problem": p, "solution": pair_of(p, q), "focus/direction": ofd}
        t, v, _ = _home(ic_cls, p); out["IC"] = {"concern": t, "issue": v}
    rs_concern = type_quad(rs_cls)[type_quad(os_cls).index(ot)]
    if a["outcome"] == "failure":
        t, v, q = _home(rs_cls, a["os_problem"]); p = a["os_problem"]
    else:
        t, v, q = _home(rs_cls, ofd[0])
        p = next(x for x in q if x not in ofd and q.index(x) // 2 == row)
    os_vq = [x for x, _ in TABLE[os_cls][type_quad(os_cls).index(ot)][2]]
    rs_vq = [x for x, _ in TABLE[rs_cls][type_quad(rs_cls).index(rs_concern)][2]]
    out["RS"] = {"concern(D6)": rs_concern, "issue(D7)": rs_vq[os_vq.index(a["os_issue"])],
                 "problem quad (D5)": f"{t}/{v}", "problem": p, "solution": pair_of(p, q)}
    if t != rs_concern:
        bad.append(f"D5/D6 disagree: RS problem {p} sits under {t}, the RS concern by position is {rs_concern}")
    return out, bad


def main(argv):
    if not argv or argv[0] == "selftest":
        return 0 if selftest() else 1
    if argv[0] == "check":
        spec = json.load(open(argv[1]))
        errors, notes = check(spec)
        for e in errors:
            print("ERROR", e)
        for n in notes:
            print("note ", n)
        print("ok" if not errors else f"{len(errors)} error(s)")
        return 1 if errors else 0
    if argv[0] == "derive":
        out, bad = derive(json.load(open(argv[1])))
        print(json.dumps(out, ensure_ascii=False, indent=1))
        for b in bad:
            print("NOTE", b)
        return 0
    if argv[0] == "under":
        cls, alias, vs = under(argv[1])
        print(f"{argv[1]} ({alias}), class {cls}")
        for v, q in vs:
            print(f"  {v:15s} {q[0]:>15s} {q[1]:<15s}\n  {'':15s} {q[2]:>15s} {q[3]:<15s}")
        return 0
    if argv[0] == "where":
        print("\n".join(where(argv[1])) or "not in the table")
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
