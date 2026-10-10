"""Write index.html for the explainer animatic from assets/vo/timings.json.

One composition, nine timed sections (#s1..#s9), one paused GSAP timeline. Every cue sits on the start of the
sentence it illustrates, so picture and voice cannot drift. Design truth: DESIGN.md.
"""
import html
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
T = json.loads((ROOT / "assets/vo/timings.json").read_text(encoding="utf-8"))
HOLD = {1: 1.0, 9: 3.0}          # picture-only seconds after the voice ends
DUR = {n: round(T[str(n)]["duration"] + HOLD.get(n, 0.0), 3) for n in range(1, 10)}
OFF, acc = {}, 0.0
for n in range(1, 10):
    OFF[n] = round(acc, 3)
    acc += DUR[n]
TOTAL = round(acc, 3)
TITLES = {1: "DER HAKEN", 2: "DAS PROBLEM", 3: "LANDEN", 4: "LESEN", 5: "ABGLEICHEN",
          6: "DER WIDERSPRUCH", 7: "DAS NETZ", 8: "KANON", 9: "SCHLUSS"}


def cue(n, i, plus=0.0):
    """Absolute time of sentence i of scene n."""
    return round(OFF[n] + T[str(n)]["captions"][i]["start"] + plus, 3)


def e(s):
    return html.escape(s, quote=False)


tl = []        # timeline statements
def at(t, js):
    tl.append(f"  {js.replace('@', str(round(t, 3)))}")


# ---------------------------------------------------------------- scenes
S = {}

def chrome(n):
    return (f'<div class="bar"><span>KOHÄRENZ PROTOKOLL / ERKLÄRT</span>'
            f'<span>{n:02d} / 09 · {TITLES[n]}</span></div>')

# 1 · Hook — the narration is the picture
lines1 = ["Eine Maschine, die einen Roman schreibt?", "Hier schreibt sie keinen einzigen Satz.",
          "Sie findet Widersprüche.", "Und dann hält sie an.", "Folgen wir einem Dokument."]
S[1] = chrome(1) + '<div class="axis">' + "".join(
    f'<div class="hook" id="h1-{i}">{e(x)}</div>' for i, x in enumerate(lines1)) + \
    '<div class="cursor" id="h1-cur"></div></div>'
caps1 = [c["text"] for c in T["1"]["captions"]]
def first(n, needle):
    for i, c in enumerate(T[str(n)]["captions"]):
        if needle in c["text"]:
            return i
    raise KeyError(needle)
shows = [first(1, "Roman schreibt"), first(1, "keinen einzigen"), first(1, "Widersprüche"),
         first(1, "hält sie an"), first(1, "Folgen wir")]
for k, i in enumerate(shows):
    t0 = cue(1, i)
    if k:
        at(t0, f'tl.set("#h1-{k-1}", {{opacity: 0}}, @);')
    at(t0, f'tl.fromTo("#h1-{k}", {{opacity: 0, y: 24}}, {{opacity: 1, y: 0, duration: 0.35, ease: "power3.out"}}, @);')
at(cue(1, shows[3], 0.6), 'tl.fromTo("#h1-cur", {opacity: 0}, {opacity: 1, duration: 0.01}, @);')
at(cue(1, shows[3], 0.9), 'tl.to("#h1-cur", {opacity: 0, duration: 0.3, repeat: 5, yoyo: true, ease: "steps(1)"}, @);')
at(cue(1, shows[4]), 'tl.set("#h1-cur", {opacity: 0}, @);')

# 2 · The problem — 586 documents, 93 copies fall away, two flash red
rng = random.Random(586)
cells = list(range(586))
gone = set(rng.sample(cells, 93))
red = rng.sample([c for c in cells if c not in gone], 2)
grid = "".join(f'<i class="c{" g" if c in gone else ""}{" r" if c in red else ""}"></i>' for c in cells)
S[2] = chrome(2) + f'''<div class="split">
  <div class="left"><div class="num" id="n2">586</div><div class="mono lab">DOKUMENTE GELANDET</div>
    <div class="mono cats" id="cats2">KONZEPTE<br/>WELTENTWÜRFE<br/>FIGURENBIBELN<br/>KAPITELPLÄNE</div>
    <div class="num small" id="n2b">−93</div><div class="mono lab" id="l2b">KOPIEN AUSSORTIERT</div></div>
  <div class="cells" id="cells2">{grid}</div></div>'''
at(cue(2, 0), 'tl.fromTo("#n2", {opacity: 0, x: -30}, {opacity: 1, x: 0, duration: 0.5, ease: "expo.out"}, @);')
at(cue(2, 0, 0.2), 'tl.fromTo("#cells2 i", {opacity: 0}, {opacity: 1, duration: 0.02, stagger: {each: 0.004, from: "start"}}, @);')
at(cue(2, 1), 'tl.fromTo("#cats2", {opacity: 0}, {opacity: 1, duration: 0.4}, @);')
i_copies = first(2, "mehrfach")
at(cue(2, i_copies, 1.2), 'tl.to("#cells2 i.g", {backgroundColor: "#B9B9B2", duration: 0.3}, @);')
at(cue(2, i_copies, 1.8), 'tl.to("#cells2 i.g", {opacity: 0, y: 30, duration: 0.6, stagger: 0.004, ease: "power2.in"}, @);')
at(cue(2, i_copies, 1.8), 'tl.fromTo(["#n2b", "#l2b"], {opacity: 0}, {opacity: 1, duration: 0.4}, @);')
i_wider = first(2, "widerruft")
at(cue(2, i_wider), 'tl.to("#cells2 i.r", {backgroundColor: "#E61919", duration: 0.12, repeat: 3, yoyo: true}, @);')
at(cue(2, i_wider, 0.8), 'tl.set("#cells2 i.r", {backgroundColor: "#E61919"}, @);')

# 3 · Landing — the plate, the path, the checksum
SHA = "90964faa00fcf394e59847f2ef6fde311b2f1110fa2f080530e5a5609473d7a1"
PATH = "Sources/drive/guardians-und-kern-welten-konzept.md"
S[3] = chrome(3) + f'''<div class="split">
  <div class="left"><div class="big" id="w3">UNVER&shy;ÄNDER&shy;LICH</div>
    <div class="mono lab">EINMAL GELANDET, NIE WIEDER VERÄNDERT</div></div>
  <div class="right"><div class="plate" id="p3">
      <div class="mono meta">guardians-und-kern-welten-konzept · 2025-04-17 · worldbuilding</div>
      <div class="ptitle">Detaillierte konzeptionelle Ausarbeitung: Guardians und Kern-Welten für „Das Seelen-Kohärenz-Protokoll“</div>
      <div class="mono meta">Zeile 11 von {PATH.split("/")[-1]}</div></div>
    <div class="mono type" id="t3a"><span>{PATH}</span></div>
    <div class="mono shalab" id="t3l">sha256</div>
    <div class="mono type sha" id="t3b"><span>{SHA}</span></div></div></div>'''
at(cue(3, 0), 'tl.fromTo("#p3", {opacity: 0, y: 40}, {opacity: 1, y: 0, duration: 0.6, ease: "power4.out"}, @);')
i_drive = first(3, "Google Drive")
at(cue(3, i_drive), 'tl.fromTo("#t3a", {"--p": 0}, {"--p": 1, duration: 1.6, ease: "steps(51)"}, @);')
i_sum = first(3, "Prüfsumme")
at(cue(3, i_sum), 'tl.fromTo("#t3l", {opacity: 0}, {opacity: 1, duration: 0.2}, @);')
at(cue(3, i_sum, 0.2), 'tl.fromTo("#t3b", {"--p": 0}, {"--p": 1, duration: 2.0, ease: "steps(64)"}, @);')
at(cue(3, first(3, "pedantisch")), 'tl.fromTo("#w3", {opacity: 0, x: -40}, {opacity: 1, x: 0, duration: 0.5, ease: "expo.out"}, @);')

# 4 · Reading — L96, the note pointing at its line, 219
src_lines = [(94, "## IV. Guardian/Welt-Paar: Kairos & Sophia & Der Möglichkeits-Garten"), (95, ""),
             (96, "(Anmerkung: Kairos und Sophia werden als zwei distinkte, aber komplementäre Guardians dargestellt, die gemeinsam über diese Domäne wachen.)"),
             (97, ""), (98, "### A. Guardian Kairos")]
rows = "".join(f'<div class="ln{" hot" if n == 96 else ""}" id="l4-{n}"><b>L{n}</b><span>{e(x)}</span></div>' for n, x in src_lines)
S[4] = chrome(4) + f'''<div class="split">
  <div class="left"><div class="card" id="note4"><div class="mono meta">NOTIZ · guardians-und-kern-welten-konzept</div>
      <div class="ctext">„Kairos und Sophia werden als zwei distinkte, aber komplementäre Guardians dargestellt …“</div>
      <div class="mono cite">^[L96]</div></div>
    <div class="card" id="list4"><div class="mono meta">BEGRIFFE</div><div class="mono terms">Guardians · Kairos · Sophia · Kern-Welten · Möglichkeits-Garten</div></div>
    <div class="num" id="n4">219</div><div class="mono lab" id="l4">DOKUMENTE GELESEN</div></div>
  <div class="right"><div class="plate src" id="p4">{rows}</div><div class="link" id="k4"></div></div></div>'''
at(cue(4, 0), 'tl.fromTo("#p4", {opacity: 0}, {opacity: 1, duration: 0.4}, @);')
at(cue(4, 0, 0.3), 'tl.fromTo("#list4", {opacity: 0, x: -30}, {opacity: 1, x: 0, duration: 0.45, ease: "power3.out"}, @);')
at(cue(4, first(4, "Notiz")), 'tl.fromTo("#note4", {opacity: 0, x: -30}, {opacity: 1, x: 0, duration: 0.45, ease: "power3.out"}, @);')
i96 = first(4, "sechsundneunzig")
at(cue(4, i96), 'tl.fromTo("#k4", {scaleX: 0}, {scaleX: 1, duration: 0.5, ease: "power2.inOut"}, @);')
at(cue(4, i96, 0.4), 'tl.to("#l4-96", {backgroundColor: "#111111", color: "#F4F4F0", duration: 0.2}, @);')
at(cue(4, first(4, "Zweihundertneunzehn")), 'tl.fromTo(["#n4", "#l4"], {opacity: 0, y: 20}, {opacity: 1, y: 0, duration: 0.45, ease: "expo.out"}, @);')

# 5 · Reconciling — the pinned pipeline, three readings side by side
cols5 = [("2025-04-17", "guardians-und-kern-welten-konzept", "fünf Guardians, mit Welten gepaart"),
         ("2025-04-18", "roman-lokalitaeten-konzept-und-ausarbeitung", "vier Träger, je einer für KW1–KW4"),
         ("2026-06-10", "kohaerenz-protokoll-storyform-und-outline", "zwei Guardians, kein Guardian-1:1")]
colh = "".join(f'<div class="col" id="c5-{k}"><div class="mono meta">{d}</div><div class="mono src5">{e(s)}</div>'
               f'<div class="ctext">{e(x)}</div></div>' for k, (d, s, x) in enumerate(cols5))
S[5] = chrome(5) + f'''<div class="pipe" id="pipe5">
    <div class="box">SOURCES</div><i class="ar"></i><div class="box">LESEN</div><i class="ar"></i>
    <div class="box on" id="b5w">WIKI</div><i class="ar"></i><div class="box">KANON</div></div>
  <div class="page" id="page5"><div class="phead"><span class="ptitle2">Guardians</span>
      <span class="mono meta">Wiki/candidates/guardians.md · eine von 106 Seiten</span></div>
    <div class="cols">{colh}</div>
    <div class="mono rule5" id="r5">JEDE LESART BEHÄLT IHREN ABSENDER · NICHTS WIRD GEGLÄTTET</div></div>'''
at(cue(5, 0), 'tl.fromTo("#pipe5 .box", {opacity: 0, y: -16}, {opacity: 1, y: 0, duration: 0.3, stagger: 0.12, ease: "power3.out"}, @);')
at(cue(5, 0, 0.3), 'tl.fromTo("#pipe5 .ar", {scaleX: 0}, {scaleX: 1, duration: 0.3, stagger: 0.12}, @);')
at(cue(5, first(5, "hundertsechs")), 'tl.fromTo("#page5", {opacity: 0, y: 30}, {opacity: 1, y: 0, duration: 0.5, ease: "power4.out"}, @);')
i_ours = first(5, "unser Dokument")
at(cue(5, i_ours), 'tl.fromTo("#c5-0", {opacity: 0, x: -60}, {opacity: 1, x: 0, duration: 0.5, ease: "expo.out"}, @);')
i_next = first(5, "Daneben")
at(cue(5, i_next), 'tl.fromTo("#c5-1", {opacity: 0, x: -60}, {opacity: 1, x: 0, duration: 0.5, ease: "expo.out"}, @);')
at(cue(5, i_next, 0.6), 'tl.fromTo("#c5-2", {opacity: 0, x: -60}, {opacity: 1, x: 0, duration: 0.5, ease: "expo.out"}, @);')
at(cue(5, first(5, "zusammengefasst")), 'tl.fromTo("#r5", {opacity: 0}, {opacity: 1, duration: 0.4}, @);')

# 6 · The contradiction — the one motion moment
S[6] = chrome(6) + '''<div class="stage6">
  <div class="mono over" id="o6"><span>„bei Konflikt gewinnt das Neuere“<i></i></span>
    <b class="mono meta">kohaerenz-protokoll-storyform-und-outline-2026-06-10-md · L13</b></div>
  <div class="plate q" id="q6a"><div class="mono meta">2025-04-17 · guardians-und-kern-welten-konzept · L96</div>
    <div class="qtext">„Kairos und Sophia werden als zwei distinkte, aber komplementäre Guardians dargestellt …“</div>
    <div class="tag">FÜNF</div></div>
  <div class="redrule" id="r6"></div>
  <div class="plate q" id="q6b"><div class="mono meta">2026-06-10 · storyform-und-outline · L282</div>
    <div class="qtext">„Architektur (post-Reset): zwei Guardians (Mnemosyne + Erasure-Pol)“</div>
    <div class="tag">ZWEI</div></div>
  <div class="mono third" id="q6c">2025-04-18 · roman-lokalitaeten-konzept-und-ausarbeitung · VIER</div>
  <div class="c6" id="c6"><div class="num red">C6</div><div class="mono lab">KONFLIKTBERICHT · EINER VON 17</div></div></div>'''
at(cue(6, first(6, "Ein Jahr später")), 'tl.fromTo("#q6a", {opacity: 0, x: -120}, {opacity: 1, x: 0, duration: 0.6, ease: "power3.out"}, @);')
at(cue(6, first(6, "Es gibt zwei")), 'tl.fromTo("#q6b", {opacity: 0, x: 120}, {opacity: 1, x: 0, duration: 0.6, ease: "power3.out"}, @);')
at(cue(6, first(6, "drittes")), 'tl.fromTo("#q6c", {opacity: 0}, {opacity: 1, duration: 0.4}, @);')
at(cue(6, first(6, "gewinnt das Neuere")), 'tl.fromTo("#o6", {opacity: 0, y: -10}, {opacity: 1, y: 0, duration: 0.4}, @);')
at(cue(6, first(6, "glaubt ihm nicht")), 'tl.fromTo("#o6 i", {scaleX: 0}, {scaleX: 1, duration: 0.5, ease: "power2.inOut"}, @);')
hero = cue(6, first(6, "Konfliktbericht"))
at(hero, 'tl.to("#q6c", {opacity: 0.25, duration: 0.4}, @);')
at(hero + 0.2, 'tl.to("#q6a", {x: 84, duration: 1.2, ease: "power4.out"}, @);')
at(hero + 0.2, 'tl.to("#q6b", {x: -84, duration: 1.2, ease: "power4.out"}, @);')
at(hero + 1.4, 'tl.fromTo("#r6", {scaleY: 0}, {scaleY: 1, duration: 0.6, ease: "power2.inOut"}, @);')
at(cue(6, first(6, "Hier endet")), 'tl.to(["#q6a", "#q6b", "#o6", "#q6c"], {opacity: 0.08, duration: 0.6}, @); tl.to("#r6", {opacity: 0.25, duration: 0.6}, @);')
at(cue(6, first(6, "Hier endet"), 0.2), 'tl.fromTo("#c6", {opacity: 0, scale: 0.92}, {opacity: 1, scale: 1, duration: 0.6, ease: "expo.out"}, @);')

# 7 · The net — seeded layout, one red edge to C6
rng = random.Random(340)
cx, cy, W, H = 560, 430, 1040, 700
nodes = [(cx, cy)]
while len(nodes) < 64:
    x, y = rng.uniform(40, W - 40), rng.uniform(40, H - 40)
    if all((x - a) ** 2 + (y - b) ** 2 > 70 ** 2 for a, b in nodes):
        nodes.append((x, y))
edges = set()
for i, (x, y) in enumerate(nodes):
    near = sorted(range(len(nodes)), key=lambda j: (nodes[j][0] - x) ** 2 + (nodes[j][1] - y) ** 2)[1:4]
    for j in near:
        edges.add(tuple(sorted((i, j))))
for j in list(range(1, 9)) + [9]:
    edges.add((0, j))
C6N = 9
svg = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" id="net7">']
for k, (a, b) in enumerate(sorted(edges)):
    red_edge = (a, b) == (0, C6N)
    svg.append(f'<line class="e{" re" if red_edge else ""}" x1="{nodes[a][0]:.0f}" y1="{nodes[a][1]:.0f}" '
               f'x2="{nodes[b][0]:.0f}" y2="{nodes[b][1]:.0f}"/>')
for k, (x, y) in enumerate(nodes):
    r = 16 if k == 0 else (11 if k == C6N else 6)
    svg.append(f'<circle class="n{" hub" if k == 0 else ""}{" rn" if k == C6N else ""}" cx="{x:.0f}" cy="{y:.0f}" r="{r}"/>')
qs = rng.sample(range(10, 64), 9)
for k in qs:
    svg.append(f'<text class="q" x="{nodes[k][0] + 10:.0f}" y="{nodes[k][1] - 10:.0f}">?</text>')
svg.append(f'<text class="hubl" x="{cx + 24}" y="{cy + 8}">Guardians</text>')
svg.append(f'<text class="c6l" x="{nodes[C6N][0] + 16:.0f}" y="{nodes[C6N][1] + 8:.0f}">C6</text></svg>')
S[7] = chrome(7) + f'''<div class="split net">
  <div class="netbox">{"".join(svg)}<div class="mono tagline" id="tag7">guardians-und-kern-welten-konzept.md:L96</div></div>
  <div class="stats"><div class="num mid" id="s7a">340</div><div class="mono lab">KNOTEN</div>
    <div class="num mid" id="s7b">11 238</div><div class="mono lab">VERBINDUNGEN</div>
    <div class="num mid" id="s7c">21 901</div><div class="mono lab">GEPRÜFTE ZITATE ALS BELEGE</div>
    <div class="num mid" id="s7d">9</div><div class="mono lab" id="s7dl">OFFENE FRAGEN</div></div></div>'''
at(cue(7, 0), 'tl.fromTo("#net7 circle", {opacity: 0, scale: 0, transformOrigin: "50% 50%"}, {opacity: 1, scale: 1, duration: 0.25, stagger: 0.03, ease: "back.out(2)"}, @);')
at(cue(7, 0, 0.6), 'tl.fromTo("#net7 line", {opacity: 0}, {opacity: 1, duration: 0.2, stagger: 0.012}, @);')
at(cue(7, 0, 0.5), 'tl.fromTo(["#s7a", "#s7b"], {opacity: 0, x: 30}, {opacity: 1, x: 0, duration: 0.45, stagger: 0.5, ease: "expo.out"}, @);')
i_line = first(7, "Zeile zeigen")
at(cue(7, i_line), 'tl.fromTo("#tag7", {opacity: 0, y: 10}, {opacity: 1, y: 0, duration: 0.35}, @);')
at(cue(7, i_line, 0.6), 'tl.fromTo("#s7c", {opacity: 0, x: 30}, {opacity: 1, x: 0, duration: 0.45, ease: "expo.out"}, @);')
at(cue(7, first(7, "Konflikte")), 'tl.to("#net7 .re", {stroke: "#E61919", strokeWidth: 6, duration: 0.3}, @);')
at(cue(7, first(7, "Konflikte")), 'tl.to("#net7 .rn", {fill: "#E61919", duration: 0.3}, @);')
i_q = first(7, "Neun")
at(cue(7, i_q), 'tl.fromTo("#net7 .q", {opacity: 0}, {opacity: 1, duration: 0.2, stagger: 0.08}, @);')
at(cue(7, i_q), 'tl.fromTo(["#s7d", "#s7dl"], {opacity: 0, x: 30}, {opacity: 1, x: 0, duration: 0.45, ease: "expo.out"}, @);')

# 8 · Canon — the row C6, five names, the red rule turns ink
names = ["LogOS", "Mnemosyne", "Cerberus", "Kairos", "Sophia"]
S[8] = chrome(8) + f'''<div class="canon">
  <div class="big k" id="w8">KANON</div>
  <div class="mono lab path8">Manuscript/kanon.md · die einzige Datei, die für den Roman gilt</div>
  <div class="row8" id="row8"><div class="mono">C6</div><div class="mono">2026-09-24</div>
    <div class="ctext">Es gibt fünf Guardians: LogOS, Mnemosyne, Cerberus, Kairos und Sophia.</div></div>
  <div class="names">{"".join(f'<span id="nm8-{i}">{x}</span>' for i, x in enumerate(names))}</div>
  <div class="rule8" id="r8"></div>
  <div class="mono lab foot8" id="f8">Manuscript/ · KEIN ENTWURF WIRD KANON, NUR WEIL ER GESCHRIEBEN WURDE</div></div>'''
at(cue(8, 0), 'tl.fromTo("#w8", {opacity: 0, x: -40}, {opacity: 1, x: 0, duration: 0.5, ease: "expo.out"}, @);')
at(cue(8, 0, 0.2), 'tl.fromTo("#r8", {scaleX: 0, backgroundColor: "#E61919"}, {scaleX: 1, duration: 0.5}, @);')
i_five = first(8, "Es sind fünf")
at(cue(8, i_five), 'tl.to("#r8", {backgroundColor: "#111111", duration: 0.6}, @);')
i_names = first(8, "LogOS")
for k in range(5):
    at(cue(8, i_names, 0.45 * k), f'tl.fromTo("#nm8-{k}", {{opacity: 0, y: 30}}, {{opacity: 1, y: 0, duration: 0.35, ease: "power3.out"}}, @);')
at(cue(8, first(8, "Diese Zeile")), 'tl.fromTo("#row8", {opacity: 0, y: 20}, {opacity: 1, y: 0, duration: 0.5, ease: "power4.out"}, @);')
at(cue(8, first(8, "Der Roman selbst")), 'tl.fromTo("#f8", {opacity: 0}, {opacity: 1, duration: 0.4}, @);')

# 9 · Close
S[9] = chrome(9) + '''<div class="axis end">
  <div class="mono lab big9" id="e9a">Freigegebene Kapitel: Keines.</div>
  <div class="hook" id="e9b">Noch.</div>
  <div class="title9" id="e9c"><div class="ttl">KOHÄRENZ PROTOKOLL</div><div class="trule"></div>
    <div class="mono lab">Zeile für Zeile belegt</div></div></div>'''
at(cue(9, 0), 'tl.fromTo("#e9a", {opacity: 0}, {opacity: 1, duration: 0.4}, @);')
at(cue(9, first(9, "Noch")), 'tl.fromTo("#e9b", {opacity: 0, scale: 0.94}, {opacity: 1, scale: 1, duration: 0.4, ease: "expo.out"}, @);')
i_boden = first(9, "Kohärenz Protokoll baut")
at(cue(9, i_boden), 'tl.to(["#e9a", "#e9b"], {opacity: 0, duration: 0.4}, @);')
at(cue(9, i_boden, 0.4), 'tl.fromTo("#e9c", {opacity: 0}, {opacity: 1, duration: 0.6}, @);')
at(cue(9, i_boden, 0.6), 'tl.fromTo("#e9c .trule", {scaleX: 0}, {scaleX: 1, duration: 0.8, ease: "power2.inOut"}, @);')

# ---------------------------------------------------------------- captions and audio
caps, auds = [], []
for n in range(1, 10):
    auds.append(f'<audio id="vo-{n}" src="assets/vo/scene-{n}.wav" data-start="{OFF[n]}" data-duration="{T[str(n)]["duration"]}" '
                f'data-track-index="30" data-volume="1"></audio>')
    if n in (1, 9):
        continue
    cs = T[str(n)]["captions"]
    for i, c in enumerate(cs):
        start = OFF[n] + c["start"]
        end = OFF[n] + (cs[i + 1]["start"] if i + 1 < len(cs) else c["end"] + 0.4)
        caps.append(f'<div class="clip cap" id="cap-{n}-{i}" data-start="{start:.3f}" data-duration="{end - start:.3f}" '
                    f'data-track-index="20"><span>{e(c["text"])}</span></div>')

sections = "\n".join(
    f'<section class="clip scene" id="s{n}" data-start="{OFF[n]}" data-duration="{DUR[n]}" data-track-index="{1 + (n - 1) % 2}">{S[n]}</section>'
    for n in range(1, 10))

FONTS = "".join(f'@font-face {{ font-family: "{f}"; src: url("assets/fonts/{file}") format("woff2"); font-weight: {w}; font-style: normal; }}\n'
                for f, file, w in [("Archivo", "archivo-latin-400-normal.woff2", 400), ("Archivo", "archivo-latin-600-normal.woff2", 600),
                                   ("Archivo", "archivo-latin-700-normal.woff2", 700), ("Archivo Black", "archivo-black-latin-400-normal.woff2", 400),
                                   ("JetBrains Mono", "jetbrains-mono-latin-400-normal.woff2", 400), ("JetBrains Mono", "jetbrains-mono-latin-500-normal.woff2", 500)])
CSS = (ROOT / "tools/style.css").read_text(encoding="utf-8")
NOISE = ("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence "
         "type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")
cols = "".join(f'<i style="left:{96 + k * 144}px"></i>' for k in range(13))
crosses = "".join(f'<b style="left:{x}px;top:{y}px"></b>' for x in (96, 960, 1824) for y in (120, 960))

page = f'''<!doctype html>
<html lang="de" data-resolution="landscape">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=1920, height=1080" />
<script src="assets/vendor/gsap.min.js"></script>
<style>
{FONTS}{CSS}
#grain {{ background-image: url("{NOISE}"); }}
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1920" data-height="1080">
  <div id="paper"></div>
  <div id="grid">{cols}{crosses}</div>
  <div id="grain"></div>
{sections}
{chr(10).join(caps)}
{chr(10).join(auds)}
</div>
<script>
  const tl = gsap.timeline({{ paused: true }});
{chr(10).join(tl)}
  tl.fromTo("#grain", {{x: 0, y: 0}}, {{x: -40, y: -24, duration: {TOTAL}, ease: "none"}}, 0);
  window.__timelines["main"] = tl;
</script>
</body>
</html>
'''
(ROOT / "index.html").write_text(page, encoding="utf-8")
print(f"index.html: {TOTAL:.2f} s ({int(TOTAL // 60)}:{TOTAL % 60:05.2f}), {len(caps)} captions, {len(tl)} timeline statements")
for n in range(1, 10):
    print(f"  s{n} {OFF[n]:7.2f} + {DUR[n]:6.2f}  {TITLES[n]}")
