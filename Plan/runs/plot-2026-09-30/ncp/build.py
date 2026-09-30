#!/usr/bin/env python3
"""Build the two provisional NCP documents (Storyform A and B) from one table.

Every value comes from the Dramatica status report of 2026-05-07
(`Sources/drive/dramatica-dual-storyform-status-2026-05-07-md.md`, §II.1) and is a
source position, not a decision of the author (Decision 006; W1 B). What the
source does not say is left out and listed in README.md. Nothing here is prose.

    python3 build.py <template-storyform.json>     # the ncp-author skill's template
"""
import json, sys, pathlib

SRC = "dramatica-dual-storyform-status-2026-05-07-md.md"
TABLE = {
  "A": {
    "title": "Storyform A — Heuristics of Integration (K1)",
    "persp": {"mc": ("Kael (MC)", "i"), "ic": ("Juna (IC, Universe/Past)", "you"),
              "os": ("AEGIS und Guardians: Manipulation der Simulation", "they"),
              "rs": ("Kael und Juna: der Moonshine-Link", "we")},
    "dyn": [("story_driver","decision"),("story_outcome","success"),("story_judgment","good"),
            ("story_limit","optionlock"),("problem_solving_style","holistic"),
            ("main_character_resolve","change"),("main_character_growth","start"),
            ("main_character_approach","be_er")],
    "sp": [("Main Character Domain","Mind"),("Main Character Concern","Memory"),
           ("Main Character Issue","Falsehood"),("Main Character Problem","Avoid"),
           ("Main Character Solution","Pursuit"),
           ("Influence Character Domain","Universe"),("Influence Character Concern","Past"),
           ("Objective Story Domain","Psychology"),("Relationship Story Domain","Physics")],
  },
  "B": {
    "title": "Storyform B — Phoenix Collapse (K0)",
    "persp": {"mc": ("AEGIS (MC)", "i"), "ic": ("Kael (IC, Mind/Conscious)", "you"),
              "os": ("Kybernetischer Krieg: Erasure-Sweeps, Guardian-Operationen", "they"),
              "rs": ("Kael und AEGIS: Host/System", "we")},
    "dyn": [("story_driver","action"),("story_outcome","failure"),("story_judgment","bad"),
            ("story_limit","timelock"),("problem_solving_style","linear"),
            ("main_character_resolve","steadfast"),("main_character_growth","stop"),
            ("main_character_approach","do_er")],
    "sp": [("Main Character Domain","Universe"),("Main Character Concern","Progress"),
           ("Main Character Issue","Fact"),("Main Character Problem","Logic"),
           ("Main Character Solution","Feeling"),
           ("Influence Character Domain","Mind"),("Influence Character Concern","Conscious"),
           ("Objective Story Domain","Physics"),("Relationship Story Domain","Psychology")],
  },
}
PERSP_ID = {"mc":"persp_main_character","ic":"persp_influence_character",
            "os":"persp_objective_story","rs":"persp_relationship_story"}
def tl(appr):
    for k,key in (("Main","mc"),("Influence","ic"),("Objective","os"),("Relationship","rs")):
        if appr.startswith(k): return key

def build(tpl, which):
    t = TABLE[which]; d = json.loads(json.dumps(tpl)); s = d["story"]
    s["id"] = f"kp-storyform-{which.lower()}-provisional"
    s["title"] = "Kohärenz Protokoll — " + t["title"]
    s["logline"] = ""; s["genre"] = ""
    n = s["narratives"][0]; n["id"] = f"narrative-{which.lower()}"; n["title"] = t["title"]
    n["status"] = "candidate"
    sub = n["subtext"]
    for p in sub["perspectives"]:
        key = {v:k for k,v in PERSP_ID.items()}[p["id"]]
        p["author_structural_pov"] = t["persp"][key][1]
        p["summary"] = t["persp"][key][0]
        p["storytelling"] = f"Quelle: {SRC}, §II.1–II.3. Forschungsposition, nicht entschieden."
    sub["dynamics"] = [{"id": f"dyn_{k}", "dynamic": k, "vector": v,
        "summary": f"{k} = {v}", "storytelling": f"Quelle: {SRC}, §II.1 (Lock-In 2026-05-07, berichtet)."}
        for k, v in t["dyn"]]
    sub["storypoints"] = [{"id": f"sp_{i:02d}", "appreciation": a, "narrative_function": nf,
        "illustration": "", "summary": f"{a}: {nf}",
        "storytelling": f"Quelle: {SRC}, §II.1. Forschungsposition.",
        "perspectives": [{"perspective_id": PERSP_ID[tl(a)]}]}
        for i, (a, nf) in enumerate(t["sp"], 1)]
    for b in sub["storybeats"]:
        b["summary"] = ""; b["storytelling"] = ""
    return d

if __name__ == "__main__":
    tpl = json.load(open(sys.argv[1])); here = pathlib.Path(__file__).parent
    for w in "AB":
        json.dump(build(tpl, w), open(here / f"storyform-{w.lower()}.provisional.ncp.json", "w"),
                  ensure_ascii=False, indent=2)
