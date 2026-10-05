#!/usr/bin/env python3
"""Build the NCP documents of Storyform A and B from the author's specs (decision 024).

Reads `specs/a-author.json` and `specs/b-author.json`, refuses to build if
`dramatica.check` finds an error, and writes `ncp/storyform-a.ncp.json` and
`ncp/storyform-b.ncp.json` in NCP 1.3.0, following the ncp-author skill
(stages 0, 2, 3, 5, 6): four perspectives, nine dynamics, the storypoints the
author chose, and only the signposts the author ordered. Nothing is invented: a
slot the author has not decided is left out, so the status stays `draft`.
The `illustration` and `storytelling` texts are the consequences that were put to
the author with each option — work language, never prose of the novel.

    python3 build_ncp.py
    node <ncp-author>/scripts/validate.js ncp/storyform-a.ncp.json
"""
import json, pathlib, sys

import dramatica

HERE = pathlib.Path(__file__).parent
DEC = "Plan/decisions/024-dramatica-is-the-recipe.md"
# the 1999 chart's spelling -> NCP 1.3.0's canonical_narrative_function
NCP_NAME = {"Consideration": "Consider", "Reconsideration": "Reconsider",
            "Non-Acceptance": "Non-acceptance", "Non-Accurate": "Non-accurate",
            "Reevaluation": "Re-evaluation", "Self-Aware": "Self-aware",
            "Self-Interest": "Self Interest", "Morality": "Selflessness"}
TL = {"MC": "Main Character", "IC": "Influence Character", "OS": "Objective Story", "RS": "Relationship Story"}
PID = {k: f"persp_{v.lower().replace(' ', '_')}" for k, v in TL.items()}

STORY = {
  "a": {
    "title": "Storyform A — Heuristik der Integration (K1)",
    "persp": {"MC": ("i", "Kael (MC, Mind)", "Kaels innere Linie: Memory, Suspicion ↔ Evidence, Inertia → Change."),
              "IC": ("you", "Juna (IC, Universe/Past)", "Juna bezeugt, ohne zu zwingen; sie verkörpert Change gegen Kaels Inertia."),
              "OS": ("they", "AEGIS, Guardians und System: Manipulation der Simulation (Psychology)",
                     "Ziel Conceptualizing; alle ringen um State of Being ↔ Sense of Self."),
              "RS": ("we", "Kael und Juna: der Moonshine-Link (Physics)",
                     "Die Beziehung ringt darum, einander über eine trennende Grenze zu verstehen.")},
    "why": {"MC": "Schritt 6: die Kette, in der Kaels innere Trägheit das Problem ist.",
            "IC": "Schritt 9a: Juna trägt Change, das Gegenstück zu Kaels Inertia.",
            "OS": "Schritt 8a: Thema und Crucial Element greifen im selben Quad ineinander.",
            "RS": "Schritt 10a: verbindet den Link mit Sensorik (W5) und W9/W15."},
    "illus": {"MC Problem": "Kael hält am Bestehenden fest, auch wenn es zerfällt.",
              "MC Solution": "Kael lässt Veränderung zu.",
              "MC Issue": "Verdacht gegen Beleg: was Kael über sich und seine Anteile glaubt.",
              "IC Issue": "Was kommen wird, gegen den Versuch, es abzuwenden.",
              "IC Problem": "Juna steht für den Wandel, den Kael verweigert.",
              "IC Solution": "Beharren — das Gegenstück, das Juna in Kael trifft.",
              "OS Issue": "Was jemand wirklich ist gegen das Bild, das er von sich hat.",
              "OS Problem": "Das System hält am Bestehenden fest — das Crucial Element, das Kael aufgibt.",
              "OS Solution": "Veränderung des Bestehenden.",
              "Story Goal": "Einen Plan, ein Konzept der Ordnung entwickeln.",
              "RS Issue": "Was man wahrnimmt (Telefon-Stille, Körpersignale) gegen was man daraus liest."},
    "plot_text": {"requirements": "Kael muss seine eigene Geschichte lesen und ihr folgen: Register, Fundsachen, Logs.",
                  "consequence": "Die Fragmentierungsnacht wiederholt sich.",
                  "forewarnings": "Impulsive Antworten der Anteile brechen durch (Nyx, Kiko); Zeitlücken, Körperreaktionen.",
                  "costs": "Kaels funktionierende Fassade zerfällt: Host-Rolle, Alltag, Routinen.",
                  "dividends": "Kael wird funktional plural; die Anteile werden Verbündete."},
    "signpost_text": {"Being": "Rollen; die Fassade hält.", "Becoming": "Das Wesen bricht auf.",
                      "Conceiving": "Der Einfall.", "Conceptualizing": "Der Plan wird entwickelt (das Ziel).",
                      "Memory": "Erinnerungslosigkeit, das Register.", "Subconscious": "Trauma-Wiederbegegnung, Sehnsucht.",
                      "Preconscious": "Reflexe unter Stress, aber mit Absicht.", "Conscious": "Bewusste Entscheidung, Wieder-Erkennen.",
                      "Past": "Junas Resonanz löst die Genesis-Krise aus.", "Progress": "Der Wandel rückt näher.",
                      "Present": "Reine Präsenz, Telefon-Stille.", "Future": "Juna manifestiert ontologisch.",
                      "Learning": "Junas Präsenz spüren.", "Doing": "Die Verbindung als Werkzeug.",
                      "Obtaining": "Der Kanal als Ressource.", "Understanding": "Verstehen ohne Worte."},
  },
  "b": {
    "title": "Storyform B — Phönix-Kollaps (K0)",
    "persp": {"MC": ("i", "AEGIS (MC, Universe)", "AEGIS' Linie: Progress, Fantasy ↔ Fact, Test, nie Trust. Strukturelle Sicht, keine Ich-Prosa (W6)."),
              "IC": ("you", "Kael (IC, Mind/Conscious)", "Kael sät Zweifel, den AEGIS nicht auflösen kann; er ändert sich am Vortex."),
              "OS": ("they", "Kybernetischer Krieg: Sweeps, Guardian-Operationen (Physics)",
                     "Ziel Obtaining; der Kampf um Approach ↔ Attitude."),
              "RS": ("we", "Kael und AEGIS: Host und System (Psychology)",
                     "Beide spielen einander Rollen vor; die Beziehung zerbricht, wenn die Rollen fallen.")},
    "why": {"MC": "Schritt 7: Zero-Trust als Dramatica-Haltung; erzeugt Prüfläufe, Quarantänen, Sweeps.",
            "IC": "Schritt 9b: das Gödel-Gambit als Zweifel, der AEGIS' Problem Test nie enden lässt.",
            "OS": "Schritt 3b/8b: Logic ist die Lösung; Thema und Crucial Element im selben Quad.",
            "RS": "Schritt 10b: passt zu Do-er AEGIS und zur operativen Interiorität."},
    "illus": {"MC Problem": "AEGIS prüft und verifiziert alles und vertraut nie.",
              "MC Solution": "Vertrauen — die Lösung, die AEGIS nie ergreift.",
              "MC Issue": "Die Fantasie absoluter Reinheit gegen die Fakten wachsender Anomalien.",
              "IC Issue": "Ein Zweifel, den Untersuchung nicht auflösen kann.",
              "OS Issue": "Die Methode gegen die Haltung: rechtfertigt das Vorgehen die Haltung?",
              "OS Problem": "Gefühle, Risse, Entropie — was die Ordnung stört.",
              "OS Solution": "Logic: AEGIS hält am Richtigen fest, und die Welt scheitert trotzdem.",
              "Story Goal": "Lückenlose Geschlossenheit erlangen: alle offenen Posten auf null."},
    "plot_text": {"requirements": "Die Sweeps müssen ausgeführt werden; jeder ist ein sichtbarer Schritt aufs Ziel.",
                  "consequence": "Das System wird, was es verhindern wollte: entropisch (Formel-Inversion).",
                  "forewarnings": "Wartungsfenster werden dichter, der Takt unregelmäßig; die Schlange steigt ab Kap 26 (F1).",
                  "costs": "Jeder Sweep frisst AEGIS' eigenes Gedächtnis; Erasure-Logs überschreiben sich.",
                  "dividends": "AEGIS versteht Kael mit jedem Zug genauer."},
    "signpost_text": {"Doing": "Sweeps laufen, Verluste sind im Gang.", "Learning": "Anomalien erkunden.",
                      "Understanding": "Das Muster begreifen.", "Obtaining": "Letzter Sweep; das Ziel scheitert.",
                      "Past": "Genesis-Trauma verdrängt; Erasure-Logs.", "Present": "Sweeps, Kontrollprotokoll.",
                      "Progress": "Countdown; die Architektur degradiert sichtbar.", "Future": "Ende der Operativität; Phoenix-Collapse.",
                      "Conscious": "Kael, der unfixbare Bug.", "Memory": "Kaels Erinnerung als Druck auf AEGIS.",
                      "Preconscious": "Reflexhafte Eskalation.", "Subconscious": "Wieder-Verbinden; Kael gibt nach.",
                      "Being": "Rollen: Wächter und Host.", "Conceiving": "AEGIS formuliert Kael als unkontrollierbar um.",
                      "Conceptualizing": "Pläne gegeneinander.", "Becoming": "Kaels Wandel, die Vortex-Inversion."},
  },
}

DYN_ORDER = ["story_driver", "story_outcome", "story_judgment", "story_limit", "problem_solving_style",
             "main_character_resolve", "influence_character_resolve", "main_character_growth",
             "main_character_approach"]


def nf(name):
    return NCP_NAME.get(name, name)


def build(key):
    spec = json.load(open(HERE / f"specs/{key}-author.json"))
    errors, _ = dramatica.check(spec)
    if errors:
        sys.exit(f"{key}: refuses to build, dramatica.check: {errors}")
    st = STORY[key]
    src = f"Entscheidung des Autors ({DEC})"
    persp = [{"id": PID[t], "author_structural_pov": st["persp"][t][0], "summary": st["persp"][t][1],
              "storytelling": st["persp"][t][2]} for t in TL]
    dyn = [{"id": f"dyn_{d}", "dynamic": d, "vector": spec["dynamics"][d], "summary": f"{d} = {spec['dynamics'][d]}",
            "storytelling": src + (" — abgeleitet: Gegenteil von main_character_resolve (Regel R6)."
                                   if d == "influence_character_resolve" else ".")} for d in DYN_ORDER]
    sps = []

    def sp(appr, fn, tl, illus, story):
        sps.append({"id": f"sp_{len(sps) + 1:02d}", "appreciation": appr, "narrative_function": nf(fn),
                    **({"throughline": TL[tl]} if tl else {}),
                    "illustration": illus, "summary": f"{appr}: {nf(fn)}", "storytelling": story,
                    "perspectives": [{"perspective_id": PID[tl or "OS"]}]})

    for t in TL:
        s = spec[t]
        why = st["why"][t]
        sp(f"{TL[t]} Domain", spec["classes"][t], t, st["persp"][t][2], why)
        sp(f"{TL[t]} Concern", s["concern"], t, st["illus"].get(f"{t} Concern", st["persp"][t][2]), why)
        if s.get("issue"):
            _, _, vs = dramatica.under(s["concern"])
            cp = dramatica.pair_of(s["issue"], [v for v, _ in vs])
            sp(f"{TL[t]} Issue", s["issue"], t, st["illus"].get(f"{t} Issue", ""),
               f"{why} Gegenpol (Counterpoint): {nf(cp)}.")
        for part in ("Problem", "Solution"):
            if s.get(part.lower()):
                sp(f"{TL[t]} {part}", s[part.lower()], t, st["illus"].get(f"{t} {part}", ""), why)
    crucial = spec["OS"]["problem"] if spec["dynamics"]["main_character_resolve"] == "change" else spec["OS"]["solution"]
    sp("Main Character Pivotal Element", crucial, "MC",
       "Das Crucial Element: das OS-Element, auf dem die Hauptfigur sitzt.",
       "Change → das OS-Problem, das die Hauptfigur aufgibt; Steadfast → die OS-Lösung, an der sie festhält. " + src + ".")
    sp("Story Goal", spec["OS"]["concern"], None, st["illus"]["Story Goal"],
       "Das Ziel liegt auf dem OS-Concern; durch das Crucial Element festgelegt (Schritt 8). " + src + ".")
    PLOT = {"requirements": ("Story Requirements", "Was geschehen muss, damit das Ziel erreichbar wird."),
            "consequence": ("Story Consequence", "Was eintritt, wenn das Ziel scheitert."),
            "forewarnings": ("Story Forewarnings", "Woran der Leser sieht, dass die Folgen näherkommen."),
            "costs": ("Story Costs", "Was das Verfolgen des Ziels unterwegs kostet."),
            "dividends": ("Story Dividends", "Was das Verfolgen des Ziels unterwegs einbringt.")}
    growth = spec["dynamics"]["main_character_growth"]
    for k, (appr, what) in PLOT.items():
        if k in spec.get("plot", {}):
            sp(appr, spec["plot"][k], None, st["plot_text"][k], what + (" Stop-Story: die Folgen laufen schon."
               if k == "consequence" and growth == "stop" else " Start-Story: die Folgen drohen nur."
               if k == "consequence" else "") + (" Schritt 14; Vorschlag der Sitzung. " if k in ("costs", "dividends") else " Schritt 13; WP-Kandidat. ") + src + ".")
    for s_ in sps:
        if s_["appreciation"] == "Story Goal":
            s_.pop("throughline", None)
    beats = []
    for t in TL:
        for i, typ in enumerate(spec[t].get("signposts", []), 1):
            beats.append({"id": f"beat_{t.lower()}_signpost_{i}", "scope": "signpost", "sequence": i,
                          "throughline": TL[t], "appreciation": f"{TL[t]} Signpost {i}", "narrative_function": nf(typ),
                          "summary": st["signpost_text"].get(typ, typ),
                          "storytelling": f"{['Akt I (Kap 1–13)', 'Akt II (Kap 14–26)', 'Akt III (Kap 27–34)', 'Vortex (Kap 35–39)'][i - 1]}. "
                                          "Reihenfolge vom Autor gewählt (Schritte 11–12, signposts-in-sources.md); "
                                          "nicht berechnet, wird gegen das Treatment geprüft.",
                          "perspectives": [{"perspective_id": PID[t]}]})
    return {"schema_version": "1.3.0", "story": {
        "id": f"story_kp_storyform_{key}", "logline": "", "genre": "", "title": "Kohärenz Protokoll — " + st["title"],
        "created_at": "2026-10-05T00:00:00Z",
        "narratives": [{"id": f"narrative-{key}", "title": st["title"], "status": "draft",
                        "subtext": {"perspectives": persp, "players": [], "dynamics": dyn,
                                    "storypoints": sps, "storybeats": beats},
                        "storytelling": {"overviews": [], "moments": []}}]}}


if __name__ == "__main__":
    (HERE / "ncp").mkdir(exist_ok=True)
    for k in "ab":
        doc = build(k)
        n = doc["story"]["narratives"][0]["subtext"]
        json.dump(doc, open(HERE / f"ncp/storyform-{k}.ncp.json", "w"), ensure_ascii=False, indent=2)
        print(f"storyform-{k}.ncp.json: {len(n['dynamics'])} dynamics, {len(n['storypoints'])} storypoints, "
              f"{len(n['storybeats'])} signposts")
