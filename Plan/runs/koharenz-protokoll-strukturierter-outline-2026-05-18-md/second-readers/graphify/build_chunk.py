#!/usr/bin/env python3
"""graphify chunk for one document. Every source_location is placed by code from an
anchor string (P26: ask for an identifier, never type one); an anchor the document
does not contain refuses the whole build."""
import json
import re
import sys
import unicodedata
from pathlib import Path

SF = "/home/user/kohaerenzprotokoll/Sources/drive/koharenz-protokoll-strukturierter-outline-2026-05-18-md.md"
OUT = Path("/home/user/kohaerenzprotokoll/Plan/runs/koharenz-protokoll-strukturierter-outline-2026-05-18-md/second-readers/graphify/.graphify_chunk_01.json")
STEM = "sources_drive_koharenz_protokoll_strukturierter_outline_2026_05_18_md"
LINES = Path(SF).read_text(encoding="utf-8").splitlines()
N = len(LINES)

GERMAN = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "Ä": "ae", "Ö": "oe", "Ü": "ue", "ß": "ss"})


def slug(text):
    t = unicodedata.normalize("NFKD", text.translate(GERMAN))
    t = "".join(c for c in t if not unicodedata.combining(c)).lower()
    return re.sub(r"[^a-z0-9]+", "_", t).strip("_")


def plain(s):
    return s.replace("\\", "").replace("*", "")


def find(anchor, lo=1, hi=None, normalized=False):
    hi = hi or N
    for i in range(lo, hi + 1):
        hay = plain(LINES[i - 1]) if normalized else LINES[i - 1]
        if anchor in hay:
            return i
    sys.exit(f"REFUSED: anchor {anchor!r} not found in L{lo}-L{hi}")


# ---- chapters: labels read from the headings themselves ----------------------
HEADS = [i for i, l in enumerate(LINES, 1) if re.match(r"^#{1,6}\s+", l)]
CH = {}
for i in HEADS:
    title = re.match(r"^(#{1,6})\s+(.+)", LINES[i - 1]).group(2).strip()
    m = re.match(r"Kap (\d+) — ", title)
    if m:
        CH[int(m.group(1))] = (i, title)
assert sorted(CH) == list(range(41)), sorted(CH)


def rng(n):
    start = CH[n][0]
    later = [h for h in HEADS if h > start]
    return start, (later[0] - 1 if later else N)


def fc(n, anchor):
    return find(anchor, *rng(n))


# ---- nodes -------------------------------------------------------------------
NODES, KEY = {}, {}
FT = {"code", "document", "paper", "image", "rationale", "concept"}


def R(*quotes):
    parts = []
    for q in quotes:
        parts.append(f"„{q}\" (L{find(q, normalized=True)})")
    return " · ".join(parts)


def node(key, label, ftype, line, rationale=None, nid=None):
    nid = nid or f"{STEM}_{slug(label)}"
    assert re.fullmatch(r"[a-z0-9_]+", nid) and "__" not in nid, nid
    assert len(nid) <= 256, nid
    assert ftype in FT, ftype
    assert key not in KEY, f"duplicate key {key}"
    assert nid not in NODES, f"duplicate id {nid} ({key})"
    KEY[key] = nid
    n = {"id": nid, "label": label, "file_type": ftype, "source_file": SF,
         "source_location": f"L{line}", "source_url": None, "captured_at": None,
         "author": None, "contributor": None}
    if rationale:
        n["rationale"] = rationale
    NODES[nid] = n


# the file itself: same id and label the markdown extractor gives it
node("DOC", Path(SF).name, "document", 1, nid=STEM, rationale=R(
    "Vollständiger Outline-Stand für Kap 0–40, mit vier simultanen strukturellen Ebenen pro Kapitel",
    "Bei Konflikt zwischen Quellen gewinnt das Konzept-Dokument 2026-05-08."))

# sources it names
node("konzept", "koharenz-protokoll-konzept-konsolidiert-2026-05-08.md", "document",
     find("koharenz-protokoll-konzept-konsolidiert-2026-05-08.md"))
node("dramatica", "dramatica-dual-storyform-status_2026-05-07.md", "document",
     find("dramatica-dual-storyform-status"))
node("threemode", "three-mode-architecture-39-chapters.md", "document",
     find("three-mode-architecture-39-chapters.md"))
node("storyweaving", "Storyweaving-Startdokument", "document", find("Storyweaving-Startdokument"))
node("lockin", "Dual-Storyform-Lock-In", "document", find("Dual-Storyform-Lock-In"))

# the four levels
node("kisho", "Kishōtenketsu", "rationale", find("### Ebene 1 — Kishōtenketsu"), R(
    "Klassisches japanisches Erzählmodell, nicht westlich-konflikt-getrieben: Aufbau ohne kausalen Konflikt, die Wendung erzeugt nachträgliche Bedeutung statt sie auszulösen.",
    "Es erlaubt der Erzählung, ihre wahre Bedeutung nachträglich zu erzeugen, statt sie kausal abzuleiten.",
    "Ketsu ist nicht die Konsequenz von Ten, sondern die Verstehens-Form aller vorherigen Beats."))
node("dual", "Dramatica-Dual-Storyform", "rationale", find("### Ebene 2 — Dramatica-Dual-Storyform"), R(
    "Die Dual-Storyform ist die Form der Trennung in Erzählform — und ihre Heilung das Wiederzusammenfinden in dritter, pluraler Form."))
node("modi", "Drei narrative Modi", "rationale", find("### Ebene 3 — Drei narrative Modi"), R(
    "Die Modus-Grenzen (13/14, 26/27) sind keine Storyform-Grenzen.",
    "Die zentrale Erzählform-Wendung ist Ten (転) im Doppel-Vortex, nicht im Modus-Wechsel.",
    "Die Modi sind die Form der Bewegung, nicht die Form der Wendung — die Wendung sitzt im Vortex 2."))
node("ebene4", "Plot-und-Charakter-Detail", "rationale", find("Plot-und-Charakter-Detail"))

node("ki", "Ki (起)", "rationale", find("**Ki (起)"))
node("sho", "Shō (承)", "rationale", find("**Shō (承)"))
node("ten", "Ten (転)", "rationale", find("**Ten (転)"))
node("ketsu", "Ketsu (結)", "rationale", find("**Ketsu (結)"))

# storyforms and their mechanics
node("sfA", "Storyform A — Heuristics of Integration", "rationale", find("Heuristics of Integration"), R(
    "Resolve: Change · Growth: Start · Approach: Be-er · Style: Holistic",
    "Domain MC: Mind · Concern: Memory · Issue: Falsehood-vs-Truth · Problem: Avoidance → Solution: Pursuit",
    "Driver: Decision (konstant) · Limit: Optionlock · Outcome: Success · Judgment: Good with high Cost",
    "IC: Juna (Universe/Past) · OS: Psychology (Manipulation der Simulation) · RS: Physics (Moonshine-Link)",
    "Cost A: Verlust der Privatheit des Wir-Geflechts. Dividend A: Liebe bleibt — Junas Verbindungs-Modus."))
node("sfB", "Storyform B — Phoenix Collapse", "rationale", find("Phoenix Collapse"), R(
    "Resolve: Steadfast · Growth: Stop · Approach: Do-er · Style: Linear",
    "Domain MC: Universe · Concern: Progress · Issue: Fact-vs-Fantasy · Problem: Logic → Solution: Feeling (nie adoptiert)",
    "Driver: Action (konstant) · Limit: Timelock · Outcome: Failure · Judgment: Bad with Dividend",
    "IC: Kael als lebende Paradoxie (Mind/Conscious) · OS: Physics (kybernetischer Krieg) · RS: Psychology (Host-System-Verstrickung)",
    "Cost B: AEGIS-monolithisch erlischt. Dividend B: Funktion bleibt — plurale Übernahme."))
node("synthese", "Synthese (c)", "rationale", find("Synthese (c)"))
node("bridge", "Bridge-Frequenz", "rationale", find("Bridge-Frequenz (Anteil"))
node("softlayer", "Soft-Layering", "rationale", find("Soft-Layering"))
node("kleinc", "Klein-c-Schema", "rationale", find("Klein-c-Schema"))
node("doppelvortex", "Doppel-Vortex", "rationale", find("Der Doppel-Vortex ist"), R(
    "Der Doppel-Vortex ist die Wendungs-Architektur dieses Romans: Vortex 1 ist operativ (orthodoxer Dramatica-Klimax), Vortex 2 ist ontologisch (post-Dramatica-Synthese).",
    "Die plurale Apotheose ist nicht innerhalb des Klein-c-Schemas beschreibbar — sie ist seine Überschreitung."))
node("v1", "Vortex 1 (operativ)", "document", find("| Vortex 1 (operativ) |"))
node("v2", "Vortex 2 (ontologisch)", "document", find("| Vortex 2 (ontologisch) |"))

# the three narrative modes
node("m1", "Heldinnenreise innen", "document", find("| Heldinnenreise innen | 1"))
node("m2", "Zyklischer Modus", "document", find("| Zyklischer Modus | 14"))
node("m3", "Heldenreise außen + Doppel-Vortex", "document", find("| Heldenreise außen + Doppel-Vortex |"))
node("murdock", "Murdock/Schmidt (Heldinnenreise)", "rationale", find("Murdock/Schmidt"))
node("campbell", "Campbell/Vogler (Heldenreise)", "rationale", find("Campbell/Vogler"))

# storypoints the chapter accents keep returning to
for key, label, anchor in [
    ("memory", "Memory (MC-Concern A)", "Concern: Memory"),
    ("falsehood", "Falsehood-vs-Truth (MC-Issue A)", "Issue: Falsehood-vs-Truth"),
    ("avoid", "Avoidance (MC-Problem A)", "Problem: Avoidance"),
    ("pursuit", "Pursuit (MC-Solution A)", "Solution: Pursuit"),
    ("decision", "Decision (Driver A)", "Driver: Decision"),
    ("optionlock", "Optionlock (Limit A)", "Limit: Optionlock"),
    ("progress", "Progress (Concern B)", "Concern: Progress"),
    ("factfantasy", "Fact-vs-Fantasy (Issue B)", "Issue: Fact-vs-Fantasy"),
    ("logic", "Logic (Problem B)", "Problem: Logic"),
    ("feeling", "Feeling (Solution B)", "Solution: Feeling"),
    ("action", "Action (Driver B)", "Driver: Action"),
    ("timelock", "Timelock (Limit B)", "Limit: Timelock"),
    ("forewarning", "Forewarning B", "Forewarning B"),
]:
    node(key, label, "rationale", find(anchor))

# characters
node("aegis", "AEGIS", "document", find("### 1.1 AEGIS"), R(
    "Keine Schurke — die operative Hälfte, die nach dem Trennungsprotokoll übrig blieb.",
    "Trägt die Bewahrung-Funktion ohne Resonanz-Fähigkeit.",
    "AEGIS-Logs als Format: bürokratische Statuszeilen, niemals moralisches Vokabular."))
node("juna", "Juna", "document", find("### 1.2 Juna"), R(
    "Strukturelle Position, nicht Charakter.",
    "Niemals physisch beschrieben.",
    "Wird nur durch Wirkung wahrnehmbar",
    "Juna ist nicht in der Welt. Juna ist die Bewegung, die Welt erst möglich macht."))
node("kael", "Kael", "document", find("### 1.3 Kael"), R(
    "Nicht ein Mensch — ein System aus dreizehn Fragmenten."))
node("komp", "Komponente 734", "document", find("Komponente 734"))

ALTERS = [  # key, label, table anchor, group, DKT cell
    ("kaelhost", "Kael (Host)", "Kael (Host)", "anps", "Hubble-Volumen / Big Rip"),
    ("lex", "Lex", "Lex (Rationalist)", "anps", "Gödel + Halteproblem"),
    ("alex", "Alex", "Alex (Beschützer)", "anps", "Asymptotische Freiheit"),
    ("rhys", "Rhys", "Rhys (Caregiver)", "anps", "Maxwells Dämon"),
    ("selene", "Selene", "Selene (ISH)", "anps", "Wurmlöcher + Entanglement Islands"),
    ("nyx", "Nyx", "Nyx (Fight)", "eps", "CPT-Verletzung"),
    ("kiko", "Kiko", "Kiko (Freeze)", "eps", "Planck-Skala"),
    ("lia", "Lia", "Lia (Ambivalent)", "eps", "Quanten-Superposition"),
    ("isabelle", "Isabelle", "Isabelle (Sexualisiert)", "eps", "Pauli-Ausschluss"),
    ("moros", "Moros", "Moros (Kollaps)", "eps", "Big Freeze"),
    ("argus", "Argus", "Argus (Meta-Kognition)", "sonder", "Fraktale"),
    ("silas", "Silas", "Silas (Juna-Echo)", "sonder", "Coheron-Echo, Tunneling"),
    ("oblivion", "Oblivion", "Oblivion (AEGIS-Echo)", "sonder", "Erason-Operator"),
]
for key, label, anchor, _, _ in ALTERS:
    node(key, label, "document", find(anchor))

node("alters13", "13 Alters", "document", find("exakt 13 Alters"))
node("anps", "ANPs (Apparently Normal Parts)", "document", find("Die fünf ANPs (Apparently Normal Parts)"))
node("eps", "EPs (Emotional Parts)", "document", find("Die fünf EPs (Emotional Parts)"))
node("sonder", "Sonderfiguren", "document", find("Drei Sonderfiguren"))
node("spiegel", "Spiegel-Alter", "document", find("Spiegel-Alter"))
node("dkt", "DKT-Korrelat", "rationale", find("DKT-Korrelat"))
for key, _, anchor, _, cell in ALTERS:
    node("dkt_" + key, cell, "rationale", find(cell, find(anchor), find(anchor)))

node("guardians", "Guardians", "document", find("Die zwei Guardians"))
node("mnemosyne", "Mnemosyne", "document", find("**Mnemosyne** — Erinnerungs-Hüterin"), R(
    "Tragik: bewahrt Trauma als Daten, ohne emotionalen Kontext zu erfassen."))
node("erasurepol", "Erasure-Pol", "document", find("**Erasure-Pol** —"))
node("logos", "LogOS", "document", find("LogOS"))
node("cerberus", "Cerberus", "document", find("Cerberus-, LogOS"))
node("kairos", "Kairos/Sophia", "document", find("Kairos/Sophia"))

# worlds and places
node("kernwelten", "Kernwelten", "document", find("die vier Kernwelten"))
node("kw1", "KW1 — Logos-Prime", "document", find("KW1 — Logos-Prime"))
node("kw2", "KW2 — Mnemosyne-Archipel", "document", find("KW2 — Mnemosyne-Archipel"), R(
    "Setting des Klimax: Mnemosyne-Archipel ist der einzige Ort, an dem Erasure nicht greift, weil Erinnerung dort Schauplatz statt Inhalt ist."))
node("kw3", "KW3 — Cerberus-Labyrinth", "document", find("KW3 — Cerberus-Labyrinth"))
node("kw4", "KW4 — Möglichkeits-Garten", "document", find("KW4 — Möglichkeits-Garten"))
node("basis", "Basisrealität — Köln 2026", "document", find("Basisrealität — Köln 2026"), R(
    "Kommt nie als Bühne in Erscheinung — nur als Erinnerungsfragment, Telefonton, Geruch."))
node("konstrukt", "Konstrukt-Stadt", "document", find("Konstrukt-Stadt"))
node("wohneinheit", "Wohneinheit 14/Sektor 7", "document", find("Wohneinheit 14/Sektor 7"))
node("innereweite", "Innere Weite (Überwelt)", "document", find("Innere Weite"))
node("lyons", "Lyons-Welt", "document", find("Lyons-Welt"))
node("babymonster", "Babymonster-Welt", "document", find("Babymonster-Welt"))
node("potentialmeer", "Potentialmeer", "document", find("Potentialmeer"))
node("ouroboros", "Ouroboros", "document", find("Ouroboros"))

# events, mechanisms, figures of thought
node("genesis", "Genesis", "document", find("**Genesis-Sequenz:**"))
node("genesiskrise", "Genesis-Krise", "document", find("Genesis-Krise"))
node("trennung", "Trennungsprotokoll", "document", find("Trennungsprotokoll"), R(
    "was am Anfang als Trennungsprotokoll erschien, wird als das verstanden, was es immer war — die Geburt der Welt.",
    "Das Trennungsprotokoll war nicht Selbst-Verstümmelung im moralischen Sinn; es war der notwendige Bruch, der Existenz erst möglich machte."))
node("cluster", "Cluster-Bildung", "document", find("Cluster-Bildung"))
node("resonanzkaskade", "Resonanzkaskade", "document", find("Resonanzkaskade"))
node("stresstest", "Stress-Test Delta-7", "document", find("Stress-Test Delta-7"))
node("cfp", "Controlled Fragmentation Protocol", "document", find("Controlled Fragmentation Protocol"))
node("bunker", "Bunker", "rationale", find("Bunker"))
node("cache", "Cache-Konflikt", "rationale", find("Cache-Konflikt"))
node("erasure", "Erasure", "rationale", find("Erasure-Funktion"))
node("erasureop", "Erasure-Operator", "rationale", find("Erasure-Operator"))
node("erason", "Erason", "rationale", find("Erason-Bilanz"))
node("coheron", "Coheron", "rationale", find("atemporales Coheron"))
node("moonshine", "Moonshine-Link", "rationale", find("Moonshine-Link"))
node("kj", "K-J-Verbindung", "rationale", find("K-J-Verbindung"))
node("nonlocal", "Quanten-Nichtlokalität", "rationale", find("Quanten-Nichtlokalität"))
node("hostsys", "Host-System-Verstrickung", "rationale", find("Host-System-Verstrickung"))
node("telefon", "Telefon-Stille", "rationale", find("Telefon-Stille"))
node("witness", "Witness-Funktion", "rationale", find("Witness-Funktion"))
node("chaitin", "Chaitin-Konstante", "rationale", find("Chaitin-Konstante"))
node("goedelaussage", "Lebende Gödel-Aussage", "rationale", find("Lebende Gödel-Aussage"))
node("paradox", "Lebende Paradoxie", "rationale", find("lebende Paradoxie"))
node("gambit", "Gödel-Gambit", "rationale", find("Gödel-Gambit"))
node("dialetheia", "Lebende Dialetheia", "rationale", find("lebende Dialetheia"))
node("parakons", "Parakonsistente Logik", "rationale", find("parakonsistente Logik"))
node("landauer", "Landauer-Wärme", "rationale", find("Landauer-Wärme"))
node("algomel", "Algorithmische Melancholie", "rationale", find("Algorithmische Melancholie"))
node("fm", "Funktionale Multiplizität", "rationale", find("Funktionale Multiplizität"))
node("wir", "Wir-Geflecht", "document", find("Wir-Geflecht"))
node("wiraegis", "Wir-AEGIS-plural", "document", find("Wir-AEGIS-plural"))
node("plural", "Plurale Bewahrung", "rationale", find("plurale Bewahrung"))
node("mosaik", "Mosaik-Herz", "rationale", find("Mosaik-Herz"))
node("reinform", "Reinform (K1)", "rationale", find("Reinform"))
node("schleier", "Multiplizitäts-Schleier-Disziplin", "rationale", find("Multiplizitäts-Schleier-Disziplin"), R(
    "Aber: das Wort „Alters\" fällt nicht.",
    "Das Wort Alters fällt nicht."))
node("formel", "AEGIS-Formel („AEGIS ist, was AEGIS verhindert, dass es nicht ist\")", "rationale",
     find("AEGIS ist, was AEGIS verhindert, dass es nicht ist"))
node("inversion", "Formel-Inversion („Wir-AEGIS ist, was Wir-AEGIS bewahrt, dass es ist\")", "rationale",
     find("Formel-Inversion"))
node("kohaerenz", "Kohärenz", "rationale", find("Zwei Arten der Kohärenz prallen"))
node("schleife", "Ontologische Heilungs-Schleife", "rationale", find("ontologische Heilungs-Schleife"), R(
    "Anfang und Ende fallen zusammen, aber das Sehen hat sich verändert."))
node("liebe", "Liebe bleibt, wie der Schmerz", "rationale", find("Liebe bleibt, wie der Schmerz"))
node("gaertner", "Gärtner", "document", find("Gärtner"))
node("genesisecho", "Genesis-Echo", "rationale", find("Genesis-Echo-Marker"))
node("flashback", "Genesis-Flashback", "rationale", find("Genesis-Flashback"))
node("flashstimme", "Genesis-Flashback-Stimme", "document", find("Genesis-Flashback-Stimme"))
node("funkenich", "Funken-Ich", "document", find("Funken-Ich"))
MOTIFS = [("rauschen", "Rauschen-Motiv"), ("form", "Form-Motiv"), ("klick", "Klick-Motiv"),
          ("phantom", "Phantom-Motiv"), ("resonanzmotiv", "Resonanz-Motiv")]
for key, label in MOTIFS:
    node(key, label, "rationale", find("Rauschen, Form, Klick, Phantom, Resonanz"))

# open questions
for key, label, anchor in [
    ("oqA", "OQ-A — Naming der finalen Form", "Naming der finalen Form"),
    ("oqB", "OQ-B — Junas Erscheinungsmodi-Anker", "Junas Erscheinungsmodi-Anker"),
    ("oqC", "OQ-C — Genesis-Cluster-Zuordnung Akt II", "Genesis-Cluster-Zuordnung Akt II"),
    ("oqD", "OQ-D — MC Symptom/Response in beiden Storyforms", "MC Symptom/Response in beiden Storyforms"),
    ("oqE", "OQ-E — Spiegel-Alter-Konzeption (Silas, Oblivion)", "Spiegel-Alter-Konzeption (Silas, Oblivion)"),
    ("oqF", "OQ-F — Moonshine-Boundary", "Moonshine-Boundary"),
    ("oqG", "OQ-G — Post-Vortex-AEGIS-Status", "Post-Vortex-AEGIS-Status"),
]:
    node(key, label, "document", find(anchor))

# chapters — label is the heading text, so the builder folds each onto the heading node
CH_RATIONALE = {
    26: R("Kap 26 nicht Kampfbeginn — Schwellen-Tritt."),
    27: R("Kap 27 nicht Triumphalismus — Klarheit."),
    35: R("AEGIS muss die Genesis zeigen, weil ihm die Lösch-Kapazität ausgeht"),
    36: R("Beat 5 öffnet jetzt auf etwas, statt zu schließen.", "Die operative Wendung ist nicht das Ende."),
    37: R("Klassischer Reward-Beat als falscher Frieden."),
    39: R("Kein didaktischer Tonfall. Keine Glossierung. Sensorik trägt; Bedeutung entsteht beim Reader."),
    40: R("Kap 40 erzählt dieselben Ereignisse wie Kap 0 — aber aus der Position der vollzogenen pluralen Heilung.",
          "Kap 40 ist nicht die Konsequenz von Kap 39, sondern die Verstehens-Form aller vorherigen Beats.",
          "Deutlich kürzer als Kap 0 — vielleicht halb so lang. Echo, nicht Wiederholung."),
}
for n in range(41):
    node(f"C{n}", CH[n][1], "document", CH[n][0], CH_RATIONALE.get(n))

# ---- edges -------------------------------------------------------------------
EDGES, SEEN = [], set()
RELS = {"calls", "implements", "references", "cites", "conceptually_related_to",
        "shares_data_with", "semantically_similar_to", "rationale_for"}
INFERRED_SCORES = {0.95, 0.85, 0.75, 0.65, 0.55}


def E(a, b, line, rel="conceptually_related_to", conf="EXTRACTED", score=None):
    s, t = KEY[a], KEY[b]
    assert rel in RELS and s != t
    if conf == "EXTRACTED":
        assert score is None
        score = 1.0
    elif conf == "INFERRED":
        assert score in INFERRED_SCORES, (a, b, score)
    else:
        assert conf == "AMBIGUOUS" and 0.1 <= score <= 0.3, (a, b, score)
    k = (s, t, rel)
    symmetric = rel in ("conceptually_related_to", "semantically_similar_to", "shares_data_with")
    if k in SEEN or (symmetric and (t, s, rel) in SEEN):
        sys.exit(f"REFUSED: duplicate edge {a} -> {b} ({rel})")
    SEEN.add(k)
    EDGES.append({"source": s, "target": t, "relation": rel, "confidence": conf,
                  "confidence_score": score, "source_file": SF,
                  "source_location": f"L{line}", "weight": 1.0})


def ref(a, b, line, conf="EXTRACTED", score=None):
    E(a, b, line, "references", conf, score)


# the document and what it names
for key in ("konzept", "dramatica", "threemode", "storyweaving"):
    E("DOC", key, find("Dieser Outline integriert"), "cites")
ref("DOC", "lockin", find("Dual-Storyform-Lock-In"))
E("lockin", "dramatica", find("Dual-Storyform-Lock-In"), conf="INFERRED", score=0.85)
ref("dual", "dramatica", find("die Storyform-Spec aus"))
ref("modi", "threemode", find("die Modus-Spec aus"))
for key in ("kisho", "dual", "modi", "ebene4"):
    ref("DOC", key, find("Plot-und-Charakter-Detail"))

# Kishōtenketsu
for key, anchor in (("ki", "**Ki (起)"), ("sho", "**Shō (承)"), ("ten", "**Ten (転)"), ("ketsu", "**Ketsu (結)")):
    E("kisho", key, find(anchor))
E("ki", "C0", find("**Ki (起)"))
E("ki", "m1", find("| Heldinnenreise innen | Ki"))
E("sho", "m2", find("| Zyklischer Modus | Shō"))
E("ten", "m3", find("**Ten (転)"))
E("ten", "doppelvortex", find("Der Doppel-Vortex ist"))
E("ten", "v1", find("| Vortex 1 (operativ) |"))
E("ten", "C37", find("| Trügerischer Sieg | Ten"))
E("ten", "v2", find("| Vortex 2 (ontologisch) |"))
E("ketsu", "v2", find("**Ketsu (結)"))
E("ketsu", "C39", find("**Ketsu (結)"))
E("ketsu", "C40", find("**Ketsu (結)"))
E("kisho", "schleife", find("ontologische Heilungs-Schleife"))
E("flashback", "ten", find("Ten-Wirkung retroaktiv"))
E("genesisecho", "kisho", find("Verstehens-Form"), conf="INFERRED", score=0.75)

# dual storyform
E("dual", "sfA", find("Heuristics of Integration"))
E("dual", "sfB", find("Phoenix Collapse"))
E("sfA", "sfB", find("Klein-c-Inversion"))
E("dual", "kleinc", find("Klein-c-Inversion"))
E("synthese", "kleinc", find("Klein-c-Schema"))
E("dual", "synthese", find("Klein-c-Inversion"))
E("dual", "bridge", find("Bridge-Frequenz (Anteil"))
E("bridge", "softlayer", find("Bridge-Frequenz (Anteil"))
E("sfA", "kael", find("(Kael-MC)"))
E("sfA", "juna", find("IC: Juna (Universe/Past)"))
E("sfA", "moonshine", find("RS: Physics (Moonshine-Link)"))
E("sfB", "aegis", find("(AEGIS-MC)"))
E("sfB", "kael", find("IC: Kael als lebende Paradoxie"))
E("sfB", "paradox", find("IC: Kael als lebende Paradoxie"))
E("sfB", "hostsys", find("RS: Psychology (Host-System-Verstrickung)"))
for key, anchor in (("memory", "Concern: Memory"), ("falsehood", "Issue: Falsehood-vs-Truth"),
                    ("avoid", "Problem: Avoidance"), ("pursuit", "Solution: Pursuit"),
                    ("decision", "Driver: Decision"), ("optionlock", "Limit: Optionlock")):
    E("sfA", key, find(anchor))
for key, anchor in (("progress", "Concern: Progress"), ("factfantasy", "Issue: Fact-vs-Fantasy"),
                    ("logic", "Problem: Logic"), ("feeling", "Solution: Feeling"),
                    ("action", "Driver: Action"), ("timelock", "Limit: Timelock"),
                    ("forewarning", "Forewarning B")):
    E("sfB", key, find(anchor))
E("avoid", "pursuit", find("Problem: Avoidance → Solution: Pursuit"))
E("logic", "feeling", find("Problem: Logic → Solution: Feeling"))
E("sfA", "wir", find("Verlust der Privatheit des Wir-Geflechts"))
E("sfA", "liebe", find("Dividend A:"), conf="INFERRED", score=0.85)
E("sfB", "wiraegis", find("Dividend B:"), conf="INFERRED", score=0.85)
E("v1", "sfB", find("B beginnt zu erlöschen"))
E("v1", "softlayer", find("maximales Soft-Layering"))
E("v2", "synthese", find("| Vortex 2 (38–39) |"))
E("v2", "kleinc", find("nicht innerhalb des Klein-c-Schemas"))
E("doppelvortex", "v1", find("Der Doppel-Vortex ist"))
E("doppelvortex", "v2", find("Der Doppel-Vortex ist"))
E("v1", "C35", find("| Vortex 1 (operativ) |"))
E("v1", "C36", find("| Vortex 1 (operativ) |"))
E("v2", "C38", find("| Vortex 2 (ontologisch) |"))
E("v2", "C39", find("| Vortex 2 (ontologisch) |"))
E("synthese", "wiraegis", find("in dritter, pluraler Form"), conf="INFERRED", score=0.85)
E("m1", "sfA", find("| Akt I (1"))
E("m2", "sfA", find("| Akt II (14"))
E("m2", "sfB", find("| Akt II (14"))
E("m3", "sfA", find("| Heldenreise außen Phase A |"))
E("m3", "sfB", find("| Heldenreise außen Phase A |"))

# the three modes and the chapters they hold
E("modi", "m1", find("| Heldinnenreise innen | 1"))
E("modi", "m2", find("| Zyklischer Modus | 14"))
E("modi", "m3", find("| Heldenreise außen + Doppel-Vortex |"))
ref("m1", "murdock", find("Murdock/Schmidt"))
ref("m3", "campbell", find("Campbell/Vogler"))
E("m3", "doppelvortex", find("| Heldenreise außen + Doppel-Vortex |"))
for mode, anchor, chapters in (("m1", "| Heldinnenreise innen | 1", range(1, 14)),
                               ("m2", "| Zyklischer Modus | 14", range(14, 27)),
                               ("m3", "| Heldenreise außen + Doppel-Vortex |", range(27, 40))):
    for n in chapters:
        E(mode, f"C{n}", find(anchor))
E("modi", "C0", find("eingerahmt von Genesis-Klammer"))
E("modi", "C40", find("eingerahmt von Genesis-Klammer"))

# the thirteen alters, their groups and physics correlates
E("kael", "alters13", find("ein **System** aus dreizehn Fragmenten"))
E("alters13", "anps", find("Die fünf ANPs"))
E("alters13", "eps", find("Die fünf EPs"))
E("alters13", "sonder", find("Drei Sonderfiguren"))
for key, _, anchor, group, _ in ALTERS:
    row = find(anchor)
    E(key, group, row)
    E(key, "dkt_" + key, row)
    E("dkt_" + key, "dkt", row)
E("silas", "spiegel", find("Silas (Juna-Echo)"))
E("oblivion", "spiegel", find("Oblivion (AEGIS-Echo)"))
E("kaelhost", "kael", find("### 1.3 Kael"))
E("silas", "juna", find("Silas (Juna-Echo)"))
E("silas", "moonshine", find("Moonshine-Resonanzkörper"))
E("oblivion", "aegis", find("Oblivion (AEGIS-Echo)"))
E("oblivion", "erasure", find("Internalisierte Erasure-Funktion"))
E("oblivion", "erasureop", find("Oblivion = Erasure-Operator"))
E("dkt_oblivion", "erasureop", find("Oblivion (AEGIS-Echo)"), conf="AMBIGUOUS", score=0.3)
E("dkt_oblivion", "erason", find("Oblivion (AEGIS-Echo)"), conf="INFERRED", score=0.95)
E("dkt_silas", "coheron", find("Silas (Juna-Echo)"), conf="INFERRED", score=0.95)

# who is what
E("juna", "coheron", find("atemporales Coheron"))
E("juna", "erason", find("anomale Erason-Bilanz"))
E("juna", "telefon", find("Telefon-Stille als Anker"))
E("juna", "witness", find("Witness-Funktion"))
E("juna", "chaitin", find("Chaitin-Konstante"))
E("juna", "goedelaussage", find("Lebende Gödel-Aussage"))
E("juna", "paradox", find("zur lebenden Paradoxie"))
E("juna", "genesiskrise", find("Genesis-Krisen-Auslöser"))
E("kael", "paradox", find("IC (lebende Paradoxie"))
E("kael", "komp", find("**Komponente 734**"))
E("kael", "basis", find("Bindungstrauma in der Basisrealität"))
E("kael", "genesiskrise", find("Fragmentierungsnacht / Genesis-Krise"))
E("kael", "wir", fc(11, "Kael (Wir-Geflecht)"))
E("kael", "kohaerenz", find("Kaels positiv definierte"))
E("aegis", "formel", find("AEGIS ist, was AEGIS verhindert, dass es nicht ist"))
E("aegis", "trennung", find("die nach dem Trennungsprotokoll übrig blieb"))
E("aegis", "algomel", find("Algorithmische Melancholie — eine Maschine"))
E("aegis", "erasure", find("AEGIS' Erasure-Funktion"))
E("aegis", "wiraegis", find("AEGIS-plural entsteht"))
E("aegis", "stresstest", find("AEGIS initiiert Phase 2"))
E("aegis", "kohaerenz", find("AEGIS' negativ definierte"))
E("formel", "kohaerenz", find("AEGIS' negativ definierte"), conf="INFERRED", score=0.85)
E("inversion", "kohaerenz", find("Formel-Inversion"), conf="INFERRED", score=0.85)
E("inversion", "formel", find("Formel-Inversion"))
E("funkenich", "aegis", find("Funken-Ich ↔ AEGIS-Beschreibung"), conf="INFERRED", score=0.75)
E("komp", "wohneinheit", find("Wohneinheit 14/Sektor 7"))
E("cluster", "komp", find("das Cluster, das Komp 734 wird"))
E("cluster", "kael", find("ist Kaels werdende Substanz"))
E("moonshine", "cluster", find("Moonshine als Echo der Cluster-Bildung"))
E("kj", "moonshine", find("K-J-Verbindung wird stärker (Moonshine-Bewusstwerdung)"), conf="INFERRED", score=0.95)
E("kj", "nonlocal", find("Quanten-Nichtlokalität als Mechanik der Verbindung"))
E("kj", "juna", fc(30, "Die Verbindung zu Juna"), conf="INFERRED", score=0.95)
E("kj", "kael", fc(30, "Die Verbindung zu Juna"), conf="INFERRED", score=0.95)

# guardians, the old guardian functions, worlds
E("mnemosyne", "guardians", find("**Mnemosyne** — Erinnerungs-Hüterin"))
E("erasurepol", "guardians", find("**Erasure-Pol** —"))
E("erasurepol", "erasure", find("Löschungs-Exekutive"))
E("cerberus", "erasurepol", find("Cerberus-, LogOS"))
E("logos", "erasurepol", find("Cerberus-, LogOS"), conf="AMBIGUOUS", score=0.2)   # L161 says Erasure-Pol ...
E("logos", "mnemosyne", find("(LogOS, in Mnemosyne absorbiert)"), conf="AMBIGUOUS", score=0.2)  # ... L172 says Mnemosyne
E("kairos", "erasurepol", find("Cerberus-, LogOS"), conf="AMBIGUOUS", score=0.3)  # absorbed (L161) vs latent (L175)
E("kairos", "kw4", find("Kairos/Sophia"))
E("logos", "kw1", find("(LogOS, in Mnemosyne absorbiert)"))
E("cerberus", "kw3", find("(Cerberus, in Erasure-Pol absorbiert)"))
E("mnemosyne", "kw2", find("KW2 — Mnemosyne-Archipel"))
for key, anchor in (("kw1", "KW1 — Logos-Prime"), ("kw2", "KW2 — Mnemosyne-Archipel"),
                    ("kw3", "KW3 — Cerberus-Labyrinth"), ("kw4", "KW4 — Möglichkeits-Garten")):
    E(key, "kernwelten", find(anchor))
E("kw1", "anps", find("ANP-Domäne"))
E("kw2", "eps", find("EP-Domäne"))
E("kw2", "parakons", find("KW2 — Mnemosyne-Archipel"))
E("kw2", "erasure", find("an dem Erasure nicht greift"))
E("kw1", "innereweite", fc(1, "Innere Weite (Überwelt) aus Kap 0"), conf="INFERRED", score=0.85)
E("konstrukt", "kw1", fc(1, "Kernwelt 1 (KW1 — Logos-Prime)"), conf="INFERRED", score=0.75)
E("lyons", "kw4", find("Lyons-Welt, KW4-Vorgriff"))
E("selene", "guardians", find("Guardian → Mediator"), conf="AMBIGUOUS", score=0.2)

# echoes, mirrors and figures of thought the document relates
E("oblivion", "erasurepol", find("Oblivion (AEGIS-Echo)"), "semantically_similar_to", "INFERRED", 0.75)
E("paradox", "goedelaussage", find("Lebende Gödel-Aussage"), "semantically_similar_to", "INFERRED", 0.75)
E("paradox", "dialetheia", find("lebende Dialetheia"), "semantically_similar_to", "INFERRED", 0.85)
E("gambit", "paradox", find("als lebenden Widerspruch (Gödel-Gambit-Vorbereitung)"), conf="INFERRED", score=0.85)
E("dialetheia", "parakons", find("lebende Dialetheia"), conf="INFERRED", score=0.75)
E("cfp", "trennung", find("Controlled Fragmentation Protocol"), "semantically_similar_to", "INFERRED", 0.65)
E("gaertner", "kw4", fc(37, "als „Gärtner"), conf="INFERRED", score=0.65)
E("bunker", "trennung", find("der Bunker ist die innere Spiegelung von AEGIS' eigenem Trennungsprotokoll"))
E("bunker", "avoid", find("Bunker-Bau als Vermeidung"))
E("lex", "bunker", find("Lex baut, was AEGIS einst baute"))
E("cache", "resonanzkaskade", find("Echo der ursprünglichen Resonanz-Kaskade"))
E("genesiskrise", "resonanzkaskade", find("**Die Krise:**"))
E("genesiskrise", "trennung", find("**Die Krise:**"))
E("genesis", "genesiskrise", find("**Die Krise:**"), conf="INFERRED", score=0.95)
E("genesis", "innereweite", find("**Genesis-Sequenz:**"))
E("genesis", "komp", find("**Genesis-Sequenz:**"))
E("genesis", "formel", find("**Genesis-Sequenz:**"))
E("genesis", "rauschen", find("**Genesis-Sequenz:**"))
E("flashback", "genesis", find("**Erster Genesis-Flashback"))
E("flashstimme", "flashback", fc(18, "Genesis-Flashback-Stimme"), conf="INFERRED", score=0.95)
E("klick", "trennung", find("Echo des Trennungsprotokoll-Klicks aus Kap 0"))
E("resonanzmotiv", "juna", find("Resonanz-Motiv — Junas durchgehende Frequenz"))
E("forewarning", "resonanzmotiv", find("Forewarning B: die Resonanz selbst"))
E("decision", "trennung", find("die Decision rastet ein, wie das Trennungsprotokoll einrastete"))
E("action", "landauer", find("B versucht das Action-Mandat zu vollenden"))
E("mosaik", "plural", find("Mosaik-Herz als Vorgriff auf plurale Bewahrung"))
E("wir", "wiraegis", find("Wir-Geflecht → Wir-AEGIS-plural"))
E("wir", "fm", find("Wir in funktionaler Multiplizität"))
E("reinform", "trennung", find("Vor-Trennungs-Stille der Reinform"), conf="INFERRED", score=0.85)
E("schleier", "alters13", find("Multiplizitäts-Schleier-Disziplin"))

# open questions
ref("oqA", "wiraegis", find("Naming der finalen Form"))
ref("oqA", "C39", find("Naming der finalen Form"))
for key in ("juna", "C7", "C24", "C30", "telefon"):
    ref("oqB", key, find("Junas Erscheinungsmodi-Anker"))
for key in ("flashback", "C18", "C21", "C22"):
    ref("oqC", key, find("Genesis-Cluster-Zuordnung Akt II"))
for key in ("sfA", "sfB", "doppelvortex"):
    ref("oqD", key, find("MC Symptom/Response in beiden Storyforms"))
for key in ("spiegel", "silas", "oblivion", "C31", "C32"):
    ref("oqE", key, find("Spiegel-Alter-Konzeption (Silas, Oblivion)"))
for key in ("moonshine", "C7", "C10", "C24", "C30"):
    ref("oqF", key, find("Moonshine-Boundary"))
for key in ("aegis", "algomel", "C37", "C38", "C39", "C40"):
    ref("oqG", key, find("Post-Vortex-AEGIS-Status"))

# chapters: who appears (the chapter's own „Charaktere:" line)
CAST = {
    0: ["aegis", "juna", "komp"], 1: ["kaelhost"], 2: ["kaelhost", "lex"], 3: ["kaelhost", "lex"],
    4: ["kael", "lex", "aegis"], 5: ["kael", "lex", "rhys"], 6: ["kael", "lex", "rhys", "alex", "nyx"],
    7: ["kael", "juna"], 8: ["kael", "lex", "alex", "selene"], 9: ["kael", "lex", "rhys", "selene", "alex"],
    10: ["kael", "lex", "selene", "juna", "silas"],
    11: ["kael", "anps", "lex", "alex", "rhys", "selene", "kiko"],
    12: ["kael", "wir", "aegis"], 13: ["kael", "wir", "aegis"],
    14: ["kael", "lex", "rhys", "aegis", "mnemosyne"], 15: ["kael", "nyx", "kiko"],
    16: ["kael", "lex", "selene", "moros", "aegis"], 17: ["kael", "selene", "rhys", "lex"],
    18: ["kael", "lex", "alex", "rhys", "nyx", "lia", "aegis", "flashstimme"],
    19: ["kael", "aegis", "mnemosyne", "juna"], 20: ["kael", "wir", "selene"],
    21: ["kael", "juna", "aegis", "flashstimme", "silas"], 22: ["kael", "aegis", "mnemosyne", "flashstimme"],
    23: ["kael", "wir", "anps", "eps"], 24: ["kael", "juna", "silas", "aegis"],
    25: ["kael", "selene", "wir", "aegis"], 26: ["kael", "wir", "aegis"],
    27: ["kael", "wir", "alters13", "aegis"], 28: ["kael", "aegis", "mnemosyne", "juna"],
    29: ["kael", "kiko", "moros", "selene", "rhys"], 30: ["kael", "juna", "silas"],
    31: ["kael", "silas", "aegis", "mnemosyne"],
    32: ["kael", "oblivion", "mnemosyne", "erasurepol", "anps", "eps"],
    33: ["kael", "wir", "alters13", "aegis"], 34: ["kael", "wir", "aegis", "mnemosyne"],
    35: ["kael", "wir", "aegis", "mnemosyne", "oblivion"], 36: ["kael", "aegis", "oblivion"],
    37: ["kael", "wir", "aegis"], 38: ["kael", "wir", "juna", "alters13", "aegis"],
    39: ["juna", "alters13"], 40: ["juna", "aegis"],
}
for n, keys in CAST.items():
    line = fc(n, "**Charaktere:**")
    for key in keys:
        ref(f"C{n}", key, line)

# chapters: what each one places, accents, echoes
X = "EXTRACTED"
PLACES = [
    (0, "funkenich", "Funken-Ich"), (0, "sfB", "nur B aktiv"), (0, "action", "Driver B (Action)"),
    (0, "forewarning", "Forewarning B"), (0, "cluster", "das Cluster, das Komp 734 wird"),
    (0, "genesis", "**Genesis-Sequenz:**"), (0, "formel", "(Formel:"), (0, "innereweite", "Die Innere Weite"),
    (0, "genesiskrise", "**Die Krise:**", "INFERRED", 0.95), (0, "trennung", "**Die Krise:**"),
    (0, "resonanzkaskade", "Resonanzkaskade"), (0, "genesisecho", "Hier ist die Quelle, kein Echo"),
    (0, "C1", "schließt nahtlos an Kap 1 an"),
    (1, "konstrukt", "Erwachen in der Konstrukt-Stadt"), (1, "memory", "MC-S1 (A) Memory"),
    (1, "kw1", "Kernwelt 1 (KW1 — Logos-Prime)"), (1, "komp", "Lebt als Komp 734"),
    (1, "wohneinheit", "Wohneinheit 14/Sektor 7"), (1, "juna", "ein Wort ohne Referent"),
    (1, "innereweite", "Innere Weite (Überwelt) aus Kap 0"), (1, "C0", "Innere Weite (Überwelt) aus Kap 0"),
    (2, "falsehood", "MC-Issue Falsehood-vs-Truth"), (2, "cfp", "Controlled Fragmentation Protocol"),
    (2, "komp", "Die Zahl 734 taucht erstmals"), (2, "phantom", "Phantom-Motiv"),
    (3, "avoid", "MC-Problem Avoidance"), (3, "bunker", "Bunker-Bau als Vermeidung"),
    (3, "aegis", "in AEGIS' Methoden"), (3, "trennung", "eigenem Trennungsprotokoll"),
    (4, "paradox", "Bug"), (4, "kw1", "Logische Fallen in KW1"), (4, "klick", "Klick-Motiv"),
    (5, "memory", "MC-Concern Memory"), (5, "kw1", "Übergang KW1 → KW2-Rand"),
    (5, "kw2", "Übergang KW1 → KW2-Rand"), (5, "reinform", "Reinform"),
    (6, "pursuit", "MC-Solution Pursuit"), (6, "cache", "Cache-Konflikt"),
    (6, "landauer", "Landauer-Wärme"), (6, "C0", "Resonanz-Kaskade aus Kap 0"),
    (7, "kj", "K-J-Verbindung wird stärker"), (7, "moonshine", "Moonshine-Bewusstwerdung"),
    (7, "telefon", "Telefon-Stille als erster expliziter Anker"), (7, "C0", "in Kap 0 als Bedrohung"),
    (8, "hostsys", "Host-System-Verstrickung"), (8, "wir", "Erste Wir-Stimme-Andeutung", "INFERRED", 0.85),
    (8, "schleier", "Das Wort *Alters* fällt"),
    (9, "wir", "Wir-Geflecht im frühen Aufbau"), (9, "schleier", "ohne dass das Wort *Alters* fällt"),
    (9, "reinform", "K1-Reinform-Erinnerung"),
    (10, "moonshine", "Moonshine als Werkzeug"), (10, "nonlocal", "(Quanten-Nichtlokalität)"),
    (10, "erasure", "Erasure-Sweeps werden hörbar"), (10, "kj", "K-J-Verbindung wird zum"),
    (10, "komp", "Die Zahl 734 taucht zum zweiten Mal"), (10, "cluster", "Echo der Cluster-Bildung"),
    (11, "mosaik", "Mosaik-Herz"), (11, "wir", "Erste klare Wir-Geflecht-Szenen"),
    (11, "schleier", "Multiplizitäts-Schleier-Disziplin"), (11, "plural", "plurale Bewahrung in Kap 39"),
    (11, "C39", "plurale Bewahrung in Kap 39"),
    (12, "reinform", "Reinform"),
    (13, "forewarning", "(Forewarning B aktiviert)"), (13, "kw4", "Möglichkeits-Garten (KW4-Vorgriff)"),
    (13, "stresstest", "Stress-Test Delta-7"), (13, "reinform", "die Reinform als Praxis"),
    (13, "C14", "**Übergang zu Kap 14:**"),
    (14, "erasure", "erste Erasure-Welle"), (14, "stresstest", "Stress-Test Delta-7"),
    (14, "form", "Form-Motiv"), (14, "reinform", "wie damals die Reinform"),
    (15, "avoid", "MC-Problem Avoidance reaktiviert"), (15, "kw2", "(KW2-Rand)"),
    (15, "babymonster", "Babymonster-Welt-Resonanz"),
    (16, "avoid", "MC-Problem — Flucht in Betäubung", "INFERRED", 0.95), (16, "bunker", "Bunker reaktiviert"),
    (16, "trennung", "Bunker als interne Wiederholung von AEGIS' Trennungsprotokoll"),
    (17, "pursuit", "MC-Solution Pursuit"), (17, "decision", "Driver-Anker A: Decision"),
    (17, "kj", "die K-J-Verbindung hilft Kael"),
    (18, "memory", "MC-Concern Memory unter Stress"), (18, "cache", "Cache-Konflikt zwischen Anteilen"),
    (18, "flashback", "**Erster Genesis-Flashback"), (18, "cluster", "(Bridge): Cluster-Bildung."),
    (18, "C0", "Der Reader erkennt: das ist Kap 0."),
    (19, "falsehood", "Avoidance als Falsehood erkennbar"), (19, "avoid", "Avoidance als Falsehood erkennbar"),
    (19, "erasure", "AEGIS' Erasure-Logik"), (19, "action", "Action-Driver greift härter"),
    (19, "kohaerenz", "Kaels wachsende Kohärenz"), (19, "klick", "Klick-Motiv"),
    (19, "C0", "Trennungsprotokoll-Klicks aus Kap 0"),
    (20, "pursuit", "MC-Solution Pursuit"), (20, "lyons", "Lyons-Welt, KW4-Vorgriff"),
    (20, "kw4", "Lyons-Welt, KW4-Vorgriff"),
    (21, "memory", "MC-Concern Memory"), (21, "potentialmeer", "Potentialmeer"),
    (21, "flashback", "**Zweiter Genesis-Flashback"), (21, "trennung", "(Bridge): Trennungsprotokoll."),
    (22, "erasure", "Erasure-Kosten sichtbar"), (22, "forewarning", "Erasure-Kosten sichtbar (Forewarning B)"),
    (22, "flashback", "**Dritter Genesis-Flashback"), (22, "komp", "(Bridge): Komp 734 / Funktionalisierung."),
    (23, "pursuit", "Solution Pursuit"), (23, "mosaik", "Mosaik-Bildung als aktiver Prozess", "INFERRED", 0.85),
    (23, "C39", "kosmischen Schöpfung von Kap 39"),
    (24, "hostsys", "Host-System-Verstrickung"), (24, "kj", "Die K-J-Verbindung wird zyklisch"),
    (24, "telefon", "**Telefon-Stille als hörbare Substanz.**"),
    (24, "witness", "Juna (Witness-Modus)", "INFERRED", 0.95), (24, "resonanzmotiv", "Resonanz-Motiv"),
    (25, "memory", "MC-Concern Memory"), (25, "optionlock", "Optionlock-Spürbarkeit"),
    (25, "erasure", "Erasure-Drohung intensiviert"), (25, "forewarning", "(Forewarning B Maximum)"),
    (25, "komp", "Die Zahl 734 erscheint zum dritten Mal"), (25, "phantom", "Phantom-Motiv"),
    (26, "forewarning", "Erasure-Vorbereitung als Forewarning"), (26, "decision", "Driver-Decision-Anker"),
    (26, "erasure", "Erasure-Vorbereitung eskaliert"), (26, "klick", "Klick-Motiv als innerer Klick"),
    (26, "trennung", "wie das Trennungsprotokoll einrastete"), (26, "C27", "**Übergang zu Kap 27:**"),
    (27, "progress", "OS-S3 (B) Progress"), (27, "fm", "in funktionaler Multiplizität"),
    (27, "form", "Form-Motiv"),
    (28, "forewarning", "B-Forewarning explizit"), (28, "erasure", "Erasure-Drohung explizit"),
    (28, "timelock", "Timelock-Countdown sichtbar"), (28, "oqB", "OQ-B-abhängig"),
    (28, "klick", "Klick-Motiv"),
    (29, "avoid", "MC-Problem Avoidance"), (29, "hostsys", "Host-System-Symbiose", "INFERRED", 0.95),
    (29, "phantom", "Phantom-Motiv"),
    (30, "moonshine", "Moonshine als bewusster Kanal"), (30, "kj", "K-J als stabile Ressource"),
    (30, "telefon", "nur die Telefon-Stille wird zur klingenden Substanz"),
    (30, "witness", "Juna (Witness in voller Form", "INFERRED", 0.95), (30, "resonanzmotiv", "Resonanz-Motiv in Reife"),
    (31, "oqE", "OQ-E"), (31, "memory", "MC-Concern Memory als Waffe"), (31, "action", "Action-Driver eskaliert"),
    (31, "kw2", "Mnemosyne-Archipel beginnt sich am Horizont zu zeigen"), (31, "klick", "Klick-Motiv"),
    (32, "oqE", "OQ-E"), (32, "falsehood", "MC-Issue Falsehood-vs-Truth"),
    (32, "guardians", "Guardians als Sub-Antagonisten"), (32, "erasureop", "Oblivion = Erasure-Operator"),
    (32, "kw3", "logische Labyrinthe", "INFERRED", 0.55),
    (33, "memory", "MC-Concern Memory"), (33, "fm", "**Funktionale Multiplizität ist erreicht**"),
    (33, "parakons", "parakonsistente Logik als Architektur"), (33, "kw2", "Mnemosyne-Archipel öffnet sich"),
    (33, "phantom", "Phantom-Motiv"), (33, "komp", "Hintergrundrauschen der Komp 734"),
    (34, "pursuit", "Pursuit als Stand"), (34, "mosaik", "Mosaik-Herz vor Vortex"),
    (34, "kohaerenz", "Zwei Arten der Kohärenz prallen"), (34, "form", "Form-Motiv"),
    (35, "softlayer", "vollständiges Soft-Layering"), (35, "pursuit", "MC-Solution Pursuit"),
    (35, "decision", "Decision aktiviert"), (35, "feeling", "AEGIS-Solution Feeling"),
    (35, "kw2", "Setting: Mnemosyne-Archipel"), (35, "erasure", "finalen Erasure-Sweep"),
    (35, "gambit", "Gödel-Gambit-Vorbereitung"), (35, "dialetheia", "lebende Dialetheia"),
    (35, "genesis", "AEGIS muss die Genesis zeigen"),
    (36, "sfA", "Resolve=Change vollzogen"), (36, "sfB", "erlischt monolithisch"),
    (36, "algomel", "Algorithmische Melancholie"), (36, "landauer", "Heat-Spike (Landauer"),
    (36, "timelock", "Limit-B (Timelock) erreicht"), (36, "action", "Action-Mandat"),
    (36, "klick", "der Klick des Trennungsprotokolls kehrt als Klick des Erlöschens wieder"),
    (36, "trennung", "der Klick des Trennungsprotokolls kehrt als Klick des Erlöschens wieder"),
    (37, "sfA", "nur A aktiv (scheinbar)"), (37, "fm", "Funktionale Multiplizität gefestigt"),
    (37, "gaertner", "als „Gärtner"), (37, "algomel", "algorithmische Melancholie"),
    (37, "rauschen", "Nichts-Rauschen aus Kap 0"), (37, "C0", "Nichts-Rauschen aus Kap 0"),
    (38, "synthese", "Synthese (c) entsteht"), (38, "moonshine", "RS-Physics maximal", "INFERRED", 0.95),
    (38, "rauschen", "Das Rauschen kommt"), (38, "plural", "Plurale Bewahrung als Lösung"),
    (38, "ouroboros", "ins Ouroboros zu gehen"), (38, "decision", "Driver-Decision-Anker A in finaler Form"),
    (38, "resonanzmotiv", "die Resonanz aus Kap 0 ist hier in geheilter Form"),
    (38, "C0", "die Resonanz aus Kap 0 ist hier in geheilter Form"), (38, "C35", "anders als Vortex-1-Beat-3"),
    (39, "wiraegis", "→ Wir-AEGIS-plural"), (39, "synthese", "Synthese vollzogen"),
    (39, "sfA", "Outcome=Success"), (39, "sfB", "Outcome=Failure"), (39, "wir", "Verlust der Privatheit des Wir"),
    (39, "aegis", "AEGIS-monolithisch erlischt; AEGIS-plural entsteht"),
    (39, "liebe", "Liebe bleibt, wie der Schmerz"), (39, "genesis", "Genesis 4. Beat vollzogen"),
    (39, "inversion", "Formel-Inversion"), (39, "plural", "alle 13 Alters in pluraler Bewahrung"),
    (40, "wiraegis", "**POV:** Wir-AEGIS-plural"), (40, "C0", "Kap 40 erzählt dieselben Ereignisse wie Kap 0"),
    (40, "komp", "Das Cluster, das Komp 734 wurde"), (40, "cluster", "Das Cluster, das Komp 734 wurde"),
    (40, "trennung", "**Echo des Trennungsprotokolls**"), (40, "liebe", "Liebe bleibt. Wie der Schmerz."),
    (40, "mosaik", "das Mosaik, das die Welt hält", "INFERRED", 0.85),
    (40, "genesisecho", "alle Echos der vorherigen 39 Kapitel"),
]
for item in PLACES:
    n, key, anchor = item[:3]
    conf, score = (item[3], item[4]) if len(item) > 3 else (X, None)
    ref(f"C{n}", key, fc(n, anchor), conf, score)
for key, _ in MOTIFS:
    ref("C0", key, fc(0, "Rauschen, Form, Klick, Phantom, Resonanz"))
    ref("C39", key, fc(39, "alle Genesis-Motive simultan"))
ref("C40", "schleife", find("Genesis-Schleife schließt sich rekursiv"), "INFERRED", 0.85)

# ---- hyperedges ----------------------------------------------------------------
HYPER = [
    ("vier_strukturelle_ebenen", "Vier simultane strukturelle Ebenen", ["kisho", "dual", "modi", "ebene4"], "form"),
    ("fuenf_genesis_motive", "Fünf Genesis-Motive", [k for k, _ in MOTIFS], "form"),
    ("vortex_2_plurale_apotheose", "Vortex 2 — plurale Apotheose",
     ["C38", "C39", "juna", "wir", "wiraegis", "aegis", "synthese", "plural"], "participate_in"),
]
hyperedges = [{"id": f"{STEM}_{hid}", "label": label, "nodes": [KEY[k] for k in members],
               "relation": rel, "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": SF}
              for hid, label, members, rel in HYPER]
assert len(hyperedges) <= 3

out = {"nodes": list(NODES.values()), "edges": EDGES, "hyperedges": hyperedges,
       "input_tokens": 0, "output_tokens": 0}

ids = set(NODES)
for e in EDGES:
    assert e["source"] in ids and e["target"] in ids
for h in hyperedges:
    assert all(m in ids for m in h["nodes"])
linked = {e["source"] for e in EDGES} | {e["target"] for e in EDGES}
orphans = sorted(n["label"] for n in NODES.values() if n["id"] not in linked)

if "--write" in sys.argv:
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
from collections import Counter
print(f"nodes {len(NODES)}  edges {len(EDGES)}  hyperedges {len(hyperedges)}")
print("confidence:", dict(Counter(e['confidence'] for e in EDGES)))
print("relations:", dict(Counter(e['relation'] for e in EDGES)))
print("file_type:", dict(Counter(n['file_type'] for n in NODES.values())))
print("orphans:", orphans)
