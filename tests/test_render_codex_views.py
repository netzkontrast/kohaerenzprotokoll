"""Structural tests for the small-page Codex renderer."""
from __future__ import annotations

import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import render_codex_views as renderer  # noqa: E402


def graph() -> sqlite3.Connection:
    con = sqlite3.connect(":memory:")
    con.executescript("""
        CREATE TABLE node_labels (node_id INTEGER, label TEXT);
        CREATE TABLE property_keys (id INTEGER PRIMARY KEY, key TEXT UNIQUE);
        CREATE TABLE node_props_text (node_id INTEGER, key_id INTEGER, value TEXT);
        CREATE TABLE node_props_int (node_id INTEGER, key_id INTEGER, value INTEGER);
        CREATE TABLE node_props_bool (node_id INTEGER, key_id INTEGER, value INTEGER);
        CREATE TABLE edges (source_id INTEGER, target_id INTEGER, type TEXT);
    """)
    keys: dict[str, int] = {}

    def add(node_label: str, **props: object) -> int:
        node_id = con.execute("SELECT COALESCE(MAX(node_id), 0) + 1 FROM node_labels").fetchone()[0]
        con.execute("INSERT INTO node_labels VALUES (?, ?)", (node_id, node_label))
        for key, value in props.items():
            if key not in keys:
                key_id = len(keys) + 1
                keys[key] = key_id
                con.execute("INSERT INTO property_keys VALUES (?, ?)", (key_id, key))
            table = "node_props_bool" if isinstance(value, bool) else (
                "node_props_int" if isinstance(value, int) else "node_props_text")
            con.execute(f"INSERT INTO {table} VALUES (?, ?, ?)", (node_id, keys[key], value))
        return node_id

    add("CodexEntry", id="entry:argus", novel=renderer.NOVEL, slug="argus",
        name="Argus", kind="concept", triggers="Argus, Beobachter",
        body="**Kategorie:** term  ## Quelle: Canon/test.md  Argus beobachtet Kohärenz.",
        vto=renderer.OPEN_VTO)
    add("StoryTimeEvent", id="event:start", novel=renderer.NOVEL,
        label="Der Roman beginnt", when_story="Romanbeginn", vto=renderer.OPEN_VTO)
    world = add("World", id="world:kw1", slug="kw1", name="KW1", vto=renderer.OPEN_VTO)
    axiom = add("WorldAxiom", id="axiom:1", severity="hard", text="Regen bleibt kalt.",
                vto=renderer.OPEN_VTO)
    con.execute("INSERT INTO edges VALUES (?, ?, 'PART_OF_WORLD')", (axiom, world))
    con.commit()
    return con


def test_renderer_emits_small_pages_and_compact_compatibility_indexes():
    con = graph()
    rendered = renderer.render_files(con)
    assert "glossary/concept/argus.md" in rendered
    assert "Argus beobachtet Kohärenz" in rendered["glossary/concept/argus.md"]
    assert "Argus beobachtet Kohärenz" not in rendered["GLOSSARY.md"]
    assert "timeline/romanbeginn-akt-i.md" in rendered
    assert "worlds/kw1.md" in rendered
    assert "Kapitel- und Spoilersicherheit" in rendered["glossary/concept/argus.md"]


def test_every_generated_detail_page_is_linked_from_an_index():
    con = graph()
    rendered = renderer.render_files(con)
    assert "argus.md" in rendered["glossary/concept/README.md"]
    assert "concept/README.md" in rendered["glossary/README.md"]
    assert "romanbeginn-akt-i.md" in rendered["timeline/README.md"]
    assert "kw1.md" in rendered["worlds/README.md"]
