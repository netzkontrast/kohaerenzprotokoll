"""Split the axiom and timeline views into subfolders, and render the routers.

`Codex/` follows one naming convention, and this module is where it is
implemented for the two views that are not codex entries:

    Codex/<view>/README.md          the rendered index of that view
    Codex/<view>/<slug>.md          one retrievable unit
    Codex/<VIEW>.md                 navigation only — counts and links, no content

A "retrievable unit" is whatever a reader asks for in one go. For codex
entries that is the entry (`tools/kpcodex`). For world axioms it is a whole
world's rule set, because nobody fetches a single axiom. For the timeline it
is a story phase. Slugs are lowercase and hyphenated throughout.

The three root files carry no bodies. They exist so a reader who does not know
the tree can find the partition they need without loading it.
"""
from __future__ import annotations

import re

from . import HEADER, codex_dir

NOVEL = "novel:9d170c31"

# Story-time phases in narrative order; `when_story` is free text, so each
# event is bucketed by the first phase whose pattern matches. A reading aid,
# never canon.
PHASES = [
    ("Genesis — vor der Romanhandlung", r"^Genesis(?!-Krise)|Basisrealität|atemporal"),
    ("Genesis-Krise / Trennung", r"Genesis-Krise|^Krise|Fragmentierung|Ende der Genesis"),
    ("Romanbeginn / Akt I", r"Romanbeginn|Akt I(?![I-])|früher Akt I"),
    ("Akt II", r"Akt II(?!I)|Beginn Akt II|Ende Akt II"),
    ("Akt III-A (vor Vortex 1)", r"Akt III"),
    ("Vortex 1", r"^Vortex 1"),
    ("Nach Vortex 1 — trügerischer Frieden", r"nach Vortex 1"),
    ("Vortex 2", r"^Vortex 2"),
]
UNPLACED = "Nicht zugeordnet"


def slugify(text: str) -> str:
    """`Akt III-A (vor Vortex 1)` -> `akt-iii-a-vor-vortex-1`."""
    lowered = (text.lower().replace("ä", "ae").replace("ö", "oe")
               .replace("ü", "ue").replace("ß", "ss"))
    return re.sub(r"[^a-z0-9]+", "-", lowered).strip("-") or "x"


def phase_index(when: str) -> int:
    for index, (_, pattern) in enumerate(PHASES):
        if re.search(pattern, when or ""):
            return index
    return len(PHASES)


def phase_title(index: int) -> str:
    return PHASES[index][0] if index < len(PHASES) else UNPLACED


# --- world axioms --------------------------------------------------------------------


def axioms_by_world(graph) -> tuple[list[tuple[dict, list[dict]]], list[dict]]:
    """`[(world, axioms)]` ordered by world name, plus the axioms with no world."""
    worlds = sorted(graph.nodes("World"), key=lambda w: w.get("name", ""))
    placed, grouped = set(), []
    for world in worlds:
        found = sorted(graph.axioms_of(world["_nid"]),
                       key=lambda a: (a.get("severity", ""), a.get("text", "")))
        placed.update(a["_nid"] for a in found)
        grouped.append((world, found))
    orphans = [a for a in graph.nodes("WorldAxiom") if a["_nid"] not in placed]
    return grouped, orphans


def render_world_axioms(world: dict, axioms: list[dict]) -> str:
    lines = [HEADER, f"# {world.get('name', '?')}  `{world.get('id', '')}`\n",
             "[Up](README.md)\n",
             f"{len(axioms)} Axiome. Schwere: `hard` = Verstoß ist ein Defekt; "
             "`soft` = Reviewer prüft.\n"]
    lines += [f"- **[{a.get('severity', '?')}]** {a.get('text', '')}" for a in axioms] or ["_keine_"]
    return "\n".join(lines) + "\n"


def axiom_views(graph) -> dict[str, str]:
    """One file per world, its index and its router — repo-relative keys."""
    grouped, orphans = axioms_by_world(graph)
    root = f"{codex_dir()}/axioms"
    files, counts = {}, []
    for world, axioms in grouped:
        slug = world.get("slug") or slugify(world.get("name", ""))
        files[f"{root}/{slug}.md"] = render_world_axioms(world, axioms)
        counts.append((world.get("name", "?"), slug, len(axioms)))
    if orphans:
        files[f"{root}/ohne-welt.md"] = render_world_axioms(
            {"name": "Ohne Welt-Zuordnung"}, orphans)
        counts.append(("Ohne Welt-Zuordnung", "ohne-welt", len(orphans)))
    files[f"{root}/README.md"] = render_index("Welt-Axiome", counts, "../WORLD-AXIOMS.md")
    files[f"{codex_dir()}/WORLD-AXIOMS.md"] = render_router(
        "Welt-Axiome — Kohärenz Protokoll",
        "Die harten und weichen Regeln je Kernwelt / Ebene. Quelle der Wahrheit: "
        "`Canon/kohaerenz-protokoll_kernwelten-vollstaendig_2026-06-10.md`; Widersprüche "
        "prüft `python3 scripts/world_check.py`.",
        [(name, f"axioms/{slug}.md", count) for name, slug, count in counts], "axioms")
    return files


# --- timeline ------------------------------------------------------------------------


def events_by_phase(graph) -> list[tuple[int, list[dict]]]:
    events = [e for e in graph.nodes("StoryTimeEvent") if e.get("novel", NOVEL) == NOVEL]
    buckets: dict[int, list[dict]] = {}
    for event in events:
        buckets.setdefault(phase_index(event.get("when_story", "")), []).append(event)
    return sorted(buckets.items())


def scene_reference(graph, event: dict, edge_type: str) -> str:
    """`Kap 0 / vorwort` for each scene joined to this event, or an em dash."""
    chapters = {c.get("id"): c for c in graph.nodes("Chapter")}
    names = []
    for scene in graph.targets_of(event["_nid"], edge_type) + graph.sources_of(event["_nid"], edge_type):
        if scene.get("slug") is None:
            continue
        number = chapters.get(scene.get("chapter"), {}).get("number")
        names.append(f"Kap {number} / {scene['slug']}" if number is not None else scene["slug"])
    return ", ".join(dict.fromkeys(names)) or "—"


def render_phase(graph, index: int, events: list[dict]) -> str:
    lines = [HEADER, f"# {phase_title(index)}\n", "[Up](README.md)\n",
             f"{len(events)} Ereignisse. `when_story` ist Freitext; die Phasen-Zuordnung "
             "ist eine Lesehilfe, kein Kanon.\n",
             "| Story-Zeit | Ereignis | passiert in | enthüllt in |", "|---|---|---|---|"]
    for event in sorted(events, key=lambda e: (e.get("when_story", ""), e.get("label", ""))):
        lines.append(f"| {event.get('when_story', '')} | {event.get('label', '')} "
                     f"| {scene_reference(graph, event, 'HAPPENS_AT')} "
                     f"| {scene_reference(graph, event, 'REVEALED_IN')} |")
    return "\n".join(lines) + "\n"


def timeline_views(graph) -> dict[str, str]:
    """One file per story phase, its index and its router — repo-relative keys."""
    root = f"{codex_dir()}/timeline"
    files, counts = {}, []
    for index, events in events_by_phase(graph):
        slug = slugify(phase_title(index))
        files[f"{root}/{slug}.md"] = render_phase(graph, index, events)
        counts.append((phase_title(index), slug, len(events)))
    files[f"{root}/README.md"] = render_index("Master-Timeline", counts,
                                              "../MASTER-TIMELINE.md")
    files[f"{codex_dir()}/MASTER-TIMELINE.md"] = render_router(
        "Master-Timeline — Kohärenz Protokoll",
        "StoryTimeEvents nach Story-Zeit gebucht. `when_story` ist Freitext; die "
        "Phasen-Zuordnung ist eine Lesehilfe, kein Kanon.",
        [(name, f"timeline/{slug}.md", count) for name, slug, count in counts], "timeline")
    return files


# --- indexes and routers -------------------------------------------------------------


def render_index(title: str, rows: list[tuple[str, str, int]], up: str) -> str:
    total = sum(n for _, _, n in rows)
    lines = [HEADER, f"# {title} ({total})\n", f"[Up]({up})\n",
             "| Partition | Einträge |", "|---|---:|"]
    lines += [f"| [{name}]({slug}.md) | {count} |" for name, slug, count in rows]
    return "\n".join(lines) + "\n"


def render_router(title: str, intro: str, rows: list[tuple[str, str, int]], folder: str) -> str:
    """A root view: counts and links only, never a body.

    `rows` are `(name, link relative to Codex/, count)`. The page exists so a
    reader who does not know the tree can find the one partition they need
    without loading any of them.
    """
    total = sum(n for _, _, n in rows)
    lines = [HEADER, f"# {title}\n",
             f"{total} Einträge in {len(rows)} Partitionen, generiert aus `Graph/`.\n",
             intro, "",
             f"**Navigation only.** The content lives under `Codex/{folder}/`, one file "
             "per partition — open the one you need rather than this page.\n",
             "| Partition | Einträge | Datei |", "|---|---:|---|"]
    lines += [f"| {name} | {count} | [`{link}`]({link}) |" for name, link, count in rows]
    lines += ["", "Assemble a chapter packet with `python3 scripts/context_packet.py "
              "--chapter N`; it reads this tree through the rules in `Graph/schema.yaml`."]
    return "\n".join(lines) + "\n"
