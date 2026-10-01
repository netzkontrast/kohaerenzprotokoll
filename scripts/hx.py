#!/usr/bin/env python3
"""HyperExtract, ported: the part of `netzkontrast/Hyper-Extract` (pinned `395039e`) this pipeline uses, in the standard library.

The contracts in `Plan/hyperextract/*.yaml` are HyperExtract templates, and until 2026-10-01 a run went through
HyperExtract's own engine in its own interpreter (a uv tool, LangChain, pydantic, FAISS, an MCP server). What a run
used of it is small: load a template, build its prompt and its JSON schema, cut the document into chunks, ask a model
once per chunk, check each reply against the schema, merge the replies. This module is that, and nothing else — no
vector index, no embeddings, no LLM merge, no search. The rest of HyperExtract is not needed to produce what
`reading_extract.stage` checks against the document.

**What a model is sent does not change.** The prompt, the JSON schema and the chunks are byte for byte what
HyperExtract 395039e builds, so the 297 labelled rows and every cost measured stay comparable:

- the prompt is `parse_guideline`'s: `# Role and Task:`, `## Extraction Rules:` (a list numbered `1. `),
  `## Source Text:` — and for a graph the entity and relation rules;
- the schema is what pydantic 2.13 writes for the container HyperExtract builds (`DataSchemaList`, `DataSchemaSet`,
  `NodeSchemaEdgeSchemaGraph`): keys sorted, properties in field order, `anyOf … null` for a field not required;
- the chunks are LangChain's `RecursiveCharacterTextSplitter` (2048 characters, 256 overlap, HyperExtract's
  separators, the separator kept at the start of the next piece, whitespace stripped);
- a reply is checked as pydantic checks it in lax mode for the five field types a template may name;
- a chunk whose reply fails is dropped (HyperExtract logs it and returns `None` for it), and the replies merge as
  HyperExtract merges them: a list appends; a set and a graph group by their identifiers and fold each group with
  `keep_existing`, `keep_incoming` or `merge_field`; a graph then drops an edge whose end is no node.

`parity` proves it against the installed upstream package when `scripts/install.sh hyperextract` has put it there,
over every template and every landed document's chunks; `selftest` holds the same on committed fixtures without it.

Refused, where HyperExtract would do it: an `llm_*` merge (a second model call that merges two readings — P13),
`two_stage` graph extraction (never run here; it needs a second prompt and the first stage's names), and the gallery's
templates by name. The validator's codes are HyperExtract's (`HE-T002`…`HE-T008`) so a message reads the same.

    python3 scripts/hx.py check [TEMPLATE ...]          # load and validate; default Plan/hyperextract/*.yaml
    python3 scripts/hx.py prompt TEMPLATE [--text FILE]  # the message a model is sent for one chunk
    python3 scripts/hx.py chunks SLUG [--size 2048 --overlap 256]
    python3 scripts/hx.py smoke TEMPLATE --text FILE --response JSON   # one canned reply per chunk, merged
    python3 scripts/hx.py parity [--docs N]             # against upstream HyperExtract, if installed
    python3 scripts/hx.py selftest
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "Plan" / "hyperextract"
FIXTURES = DIR / "fixtures"
UPSTREAM = "395039ea49709b279971631a47569b931818abbb"

TYPES = ("model", "list", "set", "document", "graph", "hypergraph", "temporal_graph", "spatial_graph",
         "spatio_temporal_graph")
RUNS = ("list", "set", "graph")          # the types this port extracts; the others load and validate only
FIELD_TYPES = ("str", "int", "float", "bool", "list")
STRATEGIES = ("merge_field", "keep_incoming", "keep_existing", "llm_balanced", "llm_prefer_incoming",
              "llm_prefer_existing")
FIELD_COUNT_LIMIT = 5                    # HyperExtract's DESIGN_GUIDE, Part 4 (HE-T008)
CHUNK_SIZE, CHUNK_OVERLAP = 2048, 256    # BaseAutoType's defaults
SEPARATORS = ["\n\n", "\n", "。", "！", "？", ". ", "! ", "? ", " ", ""]
# Field names that pydantic 2.13 refuses or warns about on a model: they shadow a BaseModel attribute, and a template
# that names one loads with a warning (`register`, HE's own validator passed it). Measured with create_model.
SHADOWS = frozenset("""construct copy dict from_orm json model_computed_fields model_config model_construct model_copy
model_dump model_dump_json model_extra model_fields model_fields_set model_json_schema model_parametrized_name
model_post_init model_rebuild model_validate model_validate_json model_validate_strings mro parse_file parse_obj
parse_raw register schema schema_json update_forward_refs validate""".split())
LABELS = {"role_and_task": "Role and Task", "known_entities": "Known Entities", "rules": "Extraction Rules",
          "entity_rules": "Entity Extraction Rules", "relation_rules": "Relation Extraction Rules",
          "time_rules": "Time Rules", "location_rules": "Location Rules", "source_text": "Source Text"}
TOP = {"language", "name", "type", "tags", "description", "output", "guideline", "identifiers", "options", "display"}


class TemplateError(ValueError):
    """A template that does not load, with HyperExtract's code for it."""


# ---- YAML: the subset the contracts are written in ----------------------------------------------------------
# Block mappings and block lists, `[a, b]` flow lists, plain, single- and double-quoted scalars, comments. Anything
# else — anchors, tags, block scalars, flow mappings — is refused, never guessed; `parity` compares every template's
# parse with PyYAML's.

def _scalar(text: str, where: str) -> Any:
    s = text.strip()
    if not s:
        return None
    if s[0] == "'":
        if len(s) < 2 or s[-1] != "'":
            raise TemplateError(f"HE-T001 {where}: unclosed single quote")
        return s[1:-1].replace("''", "'")
    if s[0] == '"':
        try:
            return json.loads(s)
        except json.JSONDecodeError as exc:
            raise TemplateError(f"HE-T001 {where}: {exc}") from None
    if s[0] == "[":
        if s[-1] != "]":
            raise TemplateError(f"HE-T001 {where}: unclosed flow list")
        inner = s[1:-1].strip()
        return [_scalar(p, where) for p in _flow_items(inner, where)] if inner else []
    if s[0] in "{&*!|>%@`":
        raise TemplateError(f"HE-T001 {where}: YAML outside the subset the contracts use ({s[0]!r})")
    low = s.lower()
    if low in ("true", "false"):
        return low == "true"
    if low in ("null", "~"):
        return None
    if re.fullmatch(r"[-+]?\d+", s):
        return int(s)
    if re.fullmatch(r"[-+]?(\d+\.\d*|\.\d+)([eE][-+]?\d+)?", s):
        return float(s)
    return s


def _flow_items(inner: str, where: str) -> list[str]:
    items, buf, quote = [], "", None
    for ch in inner:
        if quote:
            buf += ch
            if ch == quote:
                quote = None
        elif ch in "'\"":
            quote, buf = ch, buf + ch
        elif ch == ",":
            items.append(buf)
            buf = ""
        elif ch in "[]{}":
            raise TemplateError(f"HE-T001 {where}: nested flow collection")
        else:
            buf += ch
    if quote:
        raise TemplateError(f"HE-T001 {where}: unclosed quote in a flow list")
    return items + [buf]


def _strip_comment(line: str) -> str:
    quote = None
    for i, ch in enumerate(line):
        if quote:
            if ch == quote:
                quote = None
        elif ch in "'\"" and (i == 0 or line[i - 1] in " :-[,"):
            quote = ch
        elif ch == "#" and (i == 0 or line[i - 1] in " \t"):
            return line[:i].rstrip()
    return line.rstrip()


def yaml_load(text: str) -> Any:
    lines = []
    for number, raw in enumerate(text.splitlines(), 1):
        if "\t" in raw[:len(raw) - len(raw.lstrip())]:
            raise TemplateError(f"HE-T001 line {number}: a tab in the indentation")
        body = _strip_comment(raw)
        if body.strip():
            lines.append((len(body) - len(body.lstrip(" ")), body.strip(), number))
    if not lines:
        return None
    value, at = _block(lines, 0, lines[0][0])
    if at != len(lines):
        raise TemplateError(f"HE-T001 line {lines[at][2]}: unexpected indentation")
    return value


KEY = re.compile(r"^([A-Za-z_][\w-]*)\s*:(?:\s+(.*))?$")


def _block(lines: list, at: int, indent: int) -> tuple[Any, int]:
    if lines[at][1].startswith("- ") or lines[at][1] == "-":
        out: list = []
        while at < len(lines) and lines[at][0] == indent and (lines[at][1].startswith("- ") or lines[at][1] == "-"):
            rest, number = lines[at][1][1:].lstrip(), lines[at][2]
            if not rest:
                if at + 1 < len(lines) and lines[at + 1][0] > indent:
                    value, at = _block(lines, at + 1, lines[at + 1][0])
                else:
                    value, at = None, at + 1
            elif KEY.match(rest) and not rest.startswith(("'", '"')):
                # `- name: x` opens a mapping whose further keys sit two columns right of the dash
                sub = [(indent + 2, rest, number)]
                j = at + 1
                while j < len(lines) and lines[j][0] > indent:
                    sub.append(lines[j])
                    j += 1
                value, used = _block(sub, 0, indent + 2)
                if used != len(sub):
                    raise TemplateError(f"HE-T001 line {sub[used][2]}: unexpected indentation")
                at = j
            else:
                value, at = _scalar(rest, f"line {number}"), at + 1
            out.append(value)
        return out, at
    out_map: dict = {}
    while at < len(lines) and lines[at][0] == indent:
        m = KEY.match(lines[at][1])
        number = lines[at][2]
        if not m:
            raise TemplateError(f"HE-T001 line {number}: expected `key: value`")
        key, rest = m.group(1), m.group(2)
        if key in out_map:
            raise TemplateError(f"HE-T001 line {number}: duplicate key {key!r}")
        if rest is None or not rest.strip():
            if at + 1 < len(lines) and (lines[at + 1][0] > indent or (
                    lines[at + 1][0] == indent and lines[at + 1][1].startswith("- "))):
                value, at = _block(lines, at + 1, lines[at + 1][0])
            else:
                value, at = None, at + 1
        else:
            value, at = _scalar(rest, f"line {number}"), at + 1
        out_map[key] = value
    if at < len(lines) and lines[at][0] > indent:
        raise TemplateError(f"HE-T001 line {lines[at][2]}: unexpected indentation")
    return out_map, at


# ---- the template -------------------------------------------------------------------------------------------

@dataclass
class Field:
    name: str
    type: str
    description: str
    required: bool | None = None
    default: Any = None

    @property
    def optional(self) -> bool:          # pydantic: `required: false` makes the type `X | None`
        return self.required is False

    @property
    def has_default(self) -> bool:       # … and a default, given or None, makes the field not required
        return self.default is not None or self.required is False


@dataclass
class Template:
    path: Path
    name: str
    type: str
    language: str
    description: str
    fields: list[Field] = field(default_factory=list)              # model, list, set
    entities: list[Field] = field(default_factory=list)            # graph types
    relations: list[Field] = field(default_factory=list)
    output_description: str = ""
    entities_description: str = ""
    relations_description: str = ""
    guideline: dict = field(default_factory=dict)
    identifiers: dict = field(default_factory=dict)
    options: dict = field(default_factory=dict)
    display: dict = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)

    @property
    def graphlike(self) -> bool:
        return self.type not in ("model", "list", "set", "document")

    @property
    def chunk_size(self) -> int:
        return self.options.get("chunk_size") or CHUNK_SIZE

    @property
    def chunk_overlap(self) -> int:
        v = self.options.get("chunk_overlap")
        return CHUNK_OVERLAP if v is None else v


def localize(value: Any, language: str) -> str:
    """`_localize_data`: a list becomes `1. a\\n2. b`; a mapping is read in `language`, then English."""
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return "\n".join(f"{i + 1}. {item}" for i, item in enumerate(value))
    if isinstance(value, dict):
        return localize(value.get(language, value.get("en", "")), language)
    return "" if value is None else str(value)


def _is_text(value: Any, lists: bool = False) -> bool:
    if isinstance(value, str):
        return True
    if lists and isinstance(value, list):
        return all(isinstance(v, str) for v in value)
    if isinstance(value, dict):
        return all(isinstance(k, str) and _is_text(v, lists) for k, v in value.items())
    return False


def _fields(raw: Any, where: str, language: str) -> list[Field]:
    if not isinstance(raw, list):
        raise TemplateError(f"HE-T002 {where}: fields must be a list")
    out = []
    for i, f in enumerate(raw):
        if not isinstance(f, dict) or not isinstance(f.get("name"), str) or not f.get("name"):
            raise TemplateError(f"HE-T002 {where}[{i}]: a field needs a name")
        if f.get("type") not in FIELD_TYPES:
            raise TemplateError(f"HE-T002 {where}.{f['name']}: type must be one of {', '.join(FIELD_TYPES)}")
        if not _is_text(f.get("description")):
            raise TemplateError(f"HE-T002 {where}.{f['name']}: description must be text")
        if f.get("required") not in (None, True, False):
            raise TemplateError(f"HE-T002 {where}.{f['name']}: required must be true or false")
        extra = set(f) - {"name", "type", "description", "required", "default"}
        if extra:
            raise TemplateError(f"HE-T002 {where}.{f['name']}: unknown keys {sorted(extra)}")
        out.append(Field(f["name"], f["type"], localize(f["description"], language), f.get("required"),
                         f.get("default")))
    names = [f.name for f in out]
    if len(set(names)) != len(names):
        raise TemplateError(f"HE-T002 {where}: a field name is repeated")
    return out


def _output(raw: Any, where: str, language: str) -> tuple[str, list[Field]]:
    if not isinstance(raw, dict) or "fields" not in raw:
        raise TemplateError(f"HE-T002 {where}: needs description and fields")
    if not _is_text(raw.get("description")):
        raise TemplateError(f"HE-T002 {where}.description must be text")
    return localize(raw["description"], language), _fields(raw["fields"], f"{where}.fields", language)


def placeholders(pattern: str) -> list[str]:
    return re.findall(r"\{(\w+)\}", pattern)


def load(path: Path | str, language: str | None = None) -> Template:
    """`load_template` and `localize_template`, then what the factory checks when it builds the template."""
    path = Path(path)
    if not path.is_file():
        raise TemplateError(f"HE-T001 {path}: no such file")
    raw = yaml_load(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise TemplateError("HE-T002 the template is not a mapping")
    unknown = set(raw) - TOP
    if unknown:
        raise TemplateError(f"HE-T002 unknown top-level keys: {sorted(unknown)}")
    for key in ("name", "type", "tags", "description", "output", "guideline", "display"):
        if key not in raw:
            raise TemplateError(f"HE-T002 missing {key}")
    if raw["type"] not in TYPES:
        raise TemplateError(f"HE-T002 Unknown template type {raw['type']!r}. Allowed types: {', '.join(TYPES)}")
    if not isinstance(raw["name"], str) or not isinstance(raw["tags"], list) or not _is_text(raw["description"]):
        raise TemplateError("HE-T002 name must be text, tags a list, description text")
    languages = raw.get("language", "en")
    languages = languages if isinstance(languages, list) else [languages]
    language = language or languages[0]
    t = Template(path=path, name=raw["name"], type=raw["type"], language=language,
                 description=localize(raw["description"], language))
    g = raw["guideline"]
    if not isinstance(g, dict) or not _is_text(g.get("target"), lists=True):
        raise TemplateError("HE-T002 guideline.target must be text")
    if t.graphlike:
        out = raw["output"]
        if not isinstance(out, dict) or "entities" not in out or "relations" not in out:
            raise TemplateError(f"HE-T002 a {t.type} template's output needs entities and relations")
        t.output_description = localize(out.get("description"), language)
        t.entities_description, t.entities = _output(out["entities"], "output.entities", language)
        t.relations_description, t.relations = _output(out["relations"], "output.relations", language)
        for key in ("rules_for_entities", "rules_for_relations"):
            if not _is_text(g.get(key), lists=True):
                raise TemplateError(f"HE-T002 guideline.{key} must be text or a list")
        t.guideline = {k: localize(g[k], language) for k in
                       ("target", "rules_for_entities", "rules_for_relations", "rules_for_time", "rules_for_location")
                       if g.get(k) is not None}
        d = raw["display"]
        if not isinstance(d, dict) or not isinstance(d.get("entity_label"), str) or not isinstance(
                d.get("relation_label"), str):
            raise TemplateError("HE-T002 display needs entity_label and relation_label")
    else:
        if t.type != "document":
            t.output_description, t.fields = _output(raw["output"], "output", language)
        if g.get("rules") is not None and not _is_text(g.get("rules"), lists=True):
            raise TemplateError("HE-T002 guideline.rules must be text or a list")
        t.guideline = {k: localize(g[k], language) for k in ("target", "rules") if g.get(k) is not None}
        d = raw["display"]
        if not isinstance(d, dict) or not isinstance(d.get("label"), str):
            raise TemplateError("HE-T002 display needs label")
    t.display = dict(raw["display"])
    t.identifiers = dict(raw.get("identifiers") or {})
    t.options = _options(raw.get("options") or {}, t)
    _check_names(t)
    return t


OPTION_KEYS = {"chunk_size", "chunk_overlap", "max_workers", "verbose", "merge_strategy", "fields_for_search",
               "entity_merge_strategy", "relation_merge_strategy", "extraction_mode", "entity_fields_for_search",
               "relation_fields_for_search", "observation_time", "observation_location"}


def _options(o: dict, t: Template) -> dict:
    if not isinstance(o, dict):
        raise TemplateError("HE-T002 options must be a mapping")
    unknown = set(o) - OPTION_KEYS
    if unknown:
        raise TemplateError(f"HE-T002 unknown options {sorted(unknown)}")
    for key in ("merge_strategy", "entity_merge_strategy", "relation_merge_strategy"):
        if o.get(key) is not None and o[key] not in STRATEGIES:
            raise TemplateError(f"HE-T002 options.{key}: {o[key]!r} is no merge strategy")
    size, overlap = o.get("chunk_size"), o.get("chunk_overlap")
    if size is not None and size < 1:
        raise TemplateError(f"Invalid template options: options.chunk_size must be >= 1 when set (got {size})")
    if overlap is not None and overlap < 0:
        raise TemplateError(f"Invalid template options: options.chunk_overlap must be >= 0 when set (got {overlap})")
    if size is not None and overlap is not None and overlap >= size:
        raise TemplateError("Invalid template options: options.chunk_overlap must be smaller than options.chunk_size")
    names = {f.name for f in t.fields}
    for f in o.get("fields_for_search") or []:
        if t.type == "list" and f not in names:     # AutoList refuses it in its constructor
            raise TemplateError(f"Field '{f}' not found in item schema 'DataSchema'")
    return dict(o)


def _check_names(t: Template) -> None:
    for where, fields in (("output", t.fields), ("output.entities", t.entities), ("output.relations", t.relations)):
        for f in fields:
            if f.name in SHADOWS:
                t.warnings.append(f'Field name "{f.name}" in {where} shadows an attribute in parent "BaseModel"')


# ---- what HyperExtract's validator says (HE-T003..T008) -------------------------------------------------------

def diagnose(t: Template) -> list[str]:
    """Codes and messages as `he template validate` writes them; a warning counts, as `templates.py` counts it."""
    out = [f"HE-T002 warning: {w}" for w in t.warnings]
    if t.type == "set":
        item = t.identifiers.get("item_id")
        if not isinstance(item, str):
            out.append("HE-T003 error: identifiers.item_id is required for a set")
        else:
            missing = [p for p in (placeholders(item) or [item]) if p not in {f.name for f in t.fields}]
            out += [f"HE-T003 error: identifiers.item_id names {p!r}, not a field" for p in missing]
    if t.graphlike:
        ent, rel = {f.name for f in t.entities}, {f.name for f in t.relations}
        eid, rid, mem = (t.identifiers.get(k) for k in ("entity_id", "relation_id", "relation_members"))
        if not isinstance(eid, str) or not isinstance(rid, str) or mem is None:
            out.append("HE-T003 error: graph identifiers need entity_id, relation_id and relation_members")
        else:
            out += [f"HE-T003 error: identifiers.entity_id names {p!r}, not an entity field"
                    for p in (placeholders(eid) or [eid]) if p not in ent]
            out += [f"HE-T003 error: identifiers.relation_id names {p!r}, not a relation field"
                    for p in (placeholders(rid) or [rid]) if p not in rel]
            if t.type in ("graph", "temporal_graph", "spatial_graph", "spatio_temporal_graph"):
                if not isinstance(mem, dict) or set(mem) != {"source", "target"}:
                    out.append("HE-T004 error: relation_members must be {source, target} for a graph")
                else:
                    out += [f"HE-T003 error: relation_members.{k} names {v!r}, not a relation field"
                            for k, v in mem.items() if v not in rel]
            elif not isinstance(mem, (str, list)):
                out.append("HE-T004 error: relation_members must name a list field for a hypergraph")
        for k, kind in (("time_field", "temporal"), ("location_field", "spatial")):
            if kind in t.type and not t.identifiers.get(k):
                out.append(f"HE-T006 error: identifiers.{k} is required for a {t.type}")
    labels = ([("display.entity_label", t.display.get("entity_label"), t.entities),
               ("display.relation_label", t.display.get("relation_label"), t.relations)] if t.graphlike else
              [("display.label", t.display.get("label"), t.fields)])
    for where, pattern, fields in labels:
        names = {f.name for f in fields}
        out += [f"HE-T005 error: {where} names {{{p}}}, not a field" for p in placeholders(pattern or "")
                if p not in names]
    for where, fields in (("output.fields", t.fields), ("output.entities.fields", t.entities),
                          ("output.relations.fields", t.relations)):
        if len(fields) > FIELD_COUNT_LIMIT:
            out.append(f"HE-T008 warning: {where} has {len(fields)} fields (DESIGN_GUIDE limit is {FIELD_COUNT_LIMIT})")
    return out


# ---- what the model is sent ---------------------------------------------------------------------------------

def prompt(t: Template) -> str | tuple[str, str, str]:
    """`parse_guideline`: the one prompt, or a graph's (main, node, edge) prompts. `{source_text}` stays a slot."""
    L, g = LABELS, t.guideline
    head = f"# {L['role_and_task']}:\n{g['target']}"
    source = f"## {L['source_text']}:\n{{source_text}}"
    if not t.graphlike:
        parts = [head] + ([f"## {L['rules']}:\n{g['rules']}"] if g.get("rules") else []) + [source]
        return "\n\n".join(parts)
    ents = [f"## {L['entity_rules']}:\n{g['rules_for_entities']}"] if g.get("rules_for_entities") else []
    rels = [f"## {L['relation_rules']}:\n{g['rules_for_relations']}"] if g.get("rules_for_relations") else []
    time = ([f"## {L['time_rules']}:\n{g['rules_for_time']}"]
            if t.type in ("temporal_graph", "spatio_temporal_graph") and g.get("rules_for_time") else [])
    place = ([f"## {L['location_rules']}:\n{g['rules_for_location']}"]
             if t.type in ("spatial_graph", "spatio_temporal_graph") and g.get("rules_for_location") else [])
    main = "\n\n".join([head] + ents + rels + time + place + [source])
    node = "\n\n".join([head] + ents + [source])
    edge = "\n\n".join([head] + rels + time + place + [f"## {L['known_entities']}:\n{{known_nodes}}", source])
    return main, node, edge


def render(template: str, **values: str) -> str:
    """`ChatPromptTemplate.from_template(...).format(...)`: `{name}` is a slot, `{{` and `}}` are braces, and any
    other brace is the error LangChain would raise."""
    def one(m: re.Match) -> str:
        token = m.group(0)
        if token in ("{{", "}}"):
            return token[0]
        name = token[1:-1]
        if name not in values:
            raise TemplateError(f"the prompt has a slot {token} that nothing fills")
        return values[name]
    out = re.sub(r"\{\{|\}\}|\{\w+\}", one, template)
    stray = re.search(r"[{}]", re.sub(r"\{\{|\}\}|\{\w+\}", "", template))
    if stray:
        raise TemplateError("a single brace in the prompt: write {{ or }}")
    return out


def _title(name: str) -> str:
    return name.title().replace("_", " ")   # pydantic 2.13's default field title


def _type_schema(kind: str) -> dict:
    return {"str": {"type": "string"}, "int": {"type": "integer"}, "float": {"type": "number"},
            "bool": {"type": "boolean"}, "list": {"items": {"type": "string"}, "type": "array"}}[kind]


def _model_schema(title: str, description: str, fields: list[Field]) -> dict:
    props = {}
    for f in fields:
        p: dict = {"description": f.description, "title": _title(f.name)}
        if f.optional:
            p["anyOf"] = [_type_schema(f.type), {"type": "null"}]
        else:
            p.update(_type_schema(f.type))
        if f.has_default:
            p["default"] = f.default
        props[f.name] = dict(sorted(p.items()))
    out = {"properties": props, "title": title, "type": "object"}
    if description:
        out["description"] = description
    required = [f.name for f in fields if not f.has_default]
    if required:
        out["required"] = required
    return dict(sorted(out.items()))


def schema(t: Template) -> dict:
    """The JSON schema of the container HyperExtract's type asks the model for, as pydantic writes it."""
    def array(ref: str, title: str, description: str | None) -> dict:
        p = {"items": {"$ref": f"#/$defs/{ref}"}, "title": title, "type": "array"}
        if description:
            p["description"] = description
        return dict(sorted(p.items()))
    if t.graphlike:
        defs = {"EdgeSchema": _model_schema("EdgeSchema", t.relations_description, t.relations),
                "NodeSchema": _model_schema("NodeSchema", t.entities_description, t.entities)}
        return {"$defs": defs, "properties": {"nodes": array("NodeSchema", "Nodes", None),
                                              "edges": array("EdgeSchema", "Edges", None)},
                "title": "NodeSchemaEdgeSchemaGraph", "type": "object"}
    container, description = {"set": ("DataSchemaSet", "Set of unique items")}.get(
        t.type, ("DataSchemaList", "Item list"))
    if t.type == "model":
        return _model_schema("DataSchema", t.output_description, t.fields)
    return {"$defs": {"DataSchema": _model_schema("DataSchema", t.output_description, t.fields)},
            "properties": {"items": array("DataSchema", "Items", description)},
            "title": container, "type": "object"}


def spec(t: Template) -> str:
    return json.dumps(schema(t), ensure_ascii=False)


# ---- chunks ---------------------------------------------------------------------------------------------------

def _split_keep_start(text: str, separator: str) -> list[str]:
    if not separator:
        return [c for c in text if c]
    parts = re.split(f"({re.escape(separator)})", text)
    out = [parts[i] + parts[i + 1] for i in range(1, len(parts), 2)]
    if len(parts) % 2 == 0:
        out += parts[-1:]
    out = [parts[0], *out]
    return [s for s in out if s]


def _merge(splits: list[str], size: int, overlap: int) -> list[str]:
    docs, current, total = [], [], 0
    for d in splits:
        n = len(d)
        if total + n > size:
            if current:
                doc = "".join(current).strip()
                if doc:
                    docs.append(doc)
                while total > overlap or (total + n > size and total > 0):
                    total -= len(current[0])
                    current = current[1:]
        current.append(d)
        total += n
    doc = "".join(current).strip()
    if doc:
        docs.append(doc)
    return docs


def split(text: str, size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP,
          separators: list[str] | None = None) -> list[str]:
    """LangChain's `RecursiveCharacterTextSplitter.split_text` with `keep_separator=True` (at the start of the next
    piece), `strip_whitespace=True` and `len` — the only configuration HyperExtract uses."""
    separators = SEPARATORS if separators is None else separators
    separator, rest = separators[-1], []
    for i, s in enumerate(separators):
        if not s:
            separator = s
            break
        if s in text:
            separator, rest = s, separators[i + 1:]
            break
    final, good = [], []
    for s in _split_keep_start(text, separator):
        if len(s) < size:
            good.append(s)
            continue
        if good:
            final += _merge(good, size, overlap)
            good = []
        final += split(s, size, overlap, rest) if rest else [s]
    if good:
        final += _merge(good, size, overlap)
    return final


def chunks(t: Template, text: str) -> list[str]:
    """What `_extract_data` sends: the whole text when it fits, else the splitter's chunks."""
    if len(text) <= t.chunk_size:
        return [text]
    return split(text, t.chunk_size, t.chunk_overlap)


# ---- checking a reply -------------------------------------------------------------------------------------------

TRUE = {"true", "1", "yes", "on", "t", "y"}
FALSE = {"false", "0", "no", "off", "f", "n"}


def _value(f: Field, v: Any, where: str) -> Any:
    if v is None:
        if f.optional:
            return None
        raise ValueError(f"{where}.{f.name}: Input should be a valid {f.type}")
    if f.type == "str":
        if isinstance(v, str):
            return v
    elif f.type == "list":
        if isinstance(v, list) and all(isinstance(x, str) for x in v):
            return v
    elif f.type == "bool":
        if isinstance(v, bool):
            return v
        if isinstance(v, int) and v in (0, 1):
            return bool(v)
        if isinstance(v, str) and v.strip().lower() in TRUE | FALSE:
            return v.strip().lower() in TRUE
    elif f.type == "int":
        if isinstance(v, int) and not isinstance(v, bool):
            return v
        if isinstance(v, float) and v.is_integer():
            return int(v)
        if isinstance(v, str) and re.fullmatch(r"\s*[-+]?\d+\s*", v):
            return int(v)
    elif f.type == "float":
        if isinstance(v, (int, float)) and not isinstance(v, bool):
            return float(v)
        if isinstance(v, str):
            try:
                return float(v)
            except ValueError:
                pass
    raise ValueError(f"{where}.{f.name}: Input should be a valid {f.type}, got {type(v).__name__}")


def record(fields: list[Field], obj: Any, where: str) -> dict:
    """One record as pydantic validates it in lax mode and dumps it: the template's fields in order, a field not given
    taking its default, keys the template does not name dropped."""
    if not isinstance(obj, dict):
        raise ValueError(f"{where}: Input should be an object")
    out = {}
    for f in fields:
        if f.name in obj:
            out[f.name] = _value(f, obj[f.name], where)
        elif f.has_default:
            out[f.name] = f.default
        else:
            raise ValueError(f"{where}.{f.name}: Field required")
    return out


def validate(t: Template, obj: Any) -> dict:
    """A reply checked against the container the schema describes; a missing list is an empty one."""
    if not isinstance(obj, dict):
        raise ValueError("the reply is not an object")
    if t.type == "model":
        return record(t.fields, obj, "reply")
    if t.graphlike:
        out = {}
        for key, fields in (("nodes", t.entities), ("edges", t.relations)):
            rows = obj.get(key, [])
            if not isinstance(rows, list):
                raise ValueError(f"{key}: Input should be a valid list")
            out[key] = [record(fields, r, f"{key}[{i}]") for i, r in enumerate(rows)]
        return out
    rows = obj.get("items", [])
    if not isinstance(rows, list):
        raise ValueError("items: Input should be a valid list")
    return {"items": [record(t.fields, r, f"items[{i}]") for i, r in enumerate(rows)]}


# ---- merging --------------------------------------------------------------------------------------------------

def key_of(pattern: str) -> Callable[[dict], str | None]:
    """`parsers/identifiers._extractor`: a field's value as text, or a `{a}|{b}` pattern filled."""
    names = placeholders(pattern)
    if names:
        return lambda r: pattern.format(**{n: r[n] for n in names})
    return lambda r: str(r[pattern])


def fold(rows: list[dict], key: Callable[[dict], Any], strategy: str) -> list[dict]:
    """ontomem's merge: rows grouped by key in the order a key first appears, each group folded pairwise —
    `keep_existing` keeps the first, `keep_incoming` the last, `merge_field` lays each later row's non-null fields
    over the earlier ones (the tournament's pairing gives the same result: all three are associative)."""
    if strategy.startswith("llm_"):
        raise TemplateError(f"{strategy}: a model merging two readings is refused here (P13)")
    groups: dict = {}
    failures = 0
    for r in rows:
        try:
            k = key(r)
        except (KeyError, IndexError, ValueError):
            failures += 1
            continue
        if k is None:
            continue
        groups.setdefault(k, []).append(r)
    if rows and not groups:
        raise ValueError(f"key extraction failed for all {len(rows)} item(s)")
    out = []
    for group in groups.values():
        merged = group[0]
        for incoming in group[1:]:
            if strategy == "keep_existing":
                continue
            if strategy == "keep_incoming":
                merged = incoming
            else:
                over = {k: v for k, v in merged.items() if v is not None}
                over.update({k: v for k, v in incoming.items() if v is not None})
                merged = {k: over.get(k) for k in incoming}
        out.append(merged)
    return out


def _with_defaults(fields: list[Field], row: dict) -> dict:
    return {f.name: row.get(f.name, f.default) for f in fields}


def merge(t: Template, replies: list[dict | None]) -> dict:
    """`merge_batch_data` over the replies of every chunk; a failed chunk (None) is dropped."""
    replies = [r for r in replies if r is not None]
    if t.type == "list":
        return {"items": [row for r in replies for row in r["items"]]}
    if t.type == "set":
        strategy = t.options.get("merge_strategy")
        if strategy is None:
            raise TemplateError("a set names its merge_strategy (templates.py: merge-set)")
        rows = [row for r in replies for row in r["items"]]
        merged = fold(rows, key_of(t.identifiers["item_id"]), strategy) if rows else []
        return {"items": [_with_defaults(t.fields, r) for r in merged]}
    if t.type == "graph":
        node_s, edge_s = (t.options.get(k) for k in ("entity_merge_strategy", "relation_merge_strategy"))
        if node_s is None or edge_s is None:
            raise TemplateError("a graph names both merge strategies (templates.py: merge-set)")
        nodes = [n for r in replies for n in r["nodes"]]
        edges = [e for r in replies for e in r["edges"]]
        node_key = key_of(t.identifiers["entity_id"])
        nodes = fold(nodes, node_key, node_s) if nodes else []
        edges = fold(edges, key_of(t.identifiers["relation_id"]), edge_s) if edges else []
        keys = {node_key(n) for n in nodes}
        mem = t.identifiers["relation_members"]
        edges = [e for e in edges if str(e[mem["source"]]) in keys and str(e[mem["target"]]) in keys]
        return {"nodes": [_with_defaults(t.entities, n) for n in nodes],
                "edges": [_with_defaults(t.relations, e) for e in edges]}
    raise TemplateError(f"{t.type}: this port extracts {', '.join(RUNS)} templates")


# ---- extraction -----------------------------------------------------------------------------------------------

Ask = Callable[[str, str, Callable[[Any], dict]], dict]
"""(the rendered prompt, the JSON schema as text, a validator) -> the validated reply, or raises."""


def extract(t: Template, text: str, ask: Ask) -> tuple[dict, list[dict]]:
    """One document through one template, one chunk after another (HyperExtract with `max_workers=1`).
    Returns the merged data and one entry per chunk: its size and whether its reply validated."""
    if t.type not in RUNS:
        raise TemplateError(f"{t.type}: this port extracts {', '.join(RUNS)} templates")
    if t.graphlike and t.options.get("extraction_mode", "one_stage") != "one_stage":
        raise TemplateError("two_stage graph extraction is not ported: it has never run here")
    main = prompt(t)
    main = main[0] if isinstance(main, tuple) else main
    body = spec(t)
    replies, log = [], []
    for i, chunk in enumerate(chunks(t, text)):
        try:
            replies.append(ask(render(main, source_text=chunk), body, lambda obj: validate(t, obj)))
            log.append({"chunk": i, "characters": len(chunk), "ok": True})
        except Exception as exc:  # HyperExtract's _batch_safe: one bad chunk does not end the run
            replies.append(None)
            log.append({"chunk": i, "characters": len(chunk), "ok": False, "error": str(exc)[:300]})
    return merge(t, replies), log


def canned(responses: list[Any]) -> Ask:
    """An `ask` that answers each chunk with the next canned reply (the last one again when they run out)."""
    state = {"i": 0}

    def ask(text: str, body: str, check: Callable[[Any], dict]) -> dict:
        reply = responses[min(state["i"], len(responses) - 1)]
        state["i"] += 1
        return check(reply)
    return ask


# ---- parity with the upstream package -------------------------------------------------------------------------

UPSTREAM_PROBE = r"""
import json, sys, warnings
warnings.simplefilter("ignore")
import yaml
from pydantic import create_model, Field
from hyperextract.utils.template_engine.parsers import (load_template, localize_template, parse_output,
    parse_guideline)
from langchain_text_splitters import RecursiveCharacterTextSplitter
mode = sys.argv[1]
if mode == "templates":
    out = {}
    for path in sys.argv[2:]:
        raw = yaml.safe_load(open(path, encoding="utf-8"))
        try:
            cfg = localize_template(load_template(path), "en")
        except Exception as e:
            out[path] = {"yaml": raw, "error": f"{type(e).__name__}: {e}"[:300]}
            continue
        p = parse_guideline(cfg.guideline, cfg.type, "en")
        o = parse_output(cfg.output, cfg.type)
        if cfg.type in ("model", "list", "set"):
            if cfg.type == "model":
                s = o
            else:
                name, desc = ("Set", "Set of unique items") if cfg.type == "set" else ("List", "Item list")
                s = create_model(f"{o.__name__}{name}", items=(list[o], Field(default_factory=list, description=desc)))
        else:
            n, e = o
            s = create_model(f"{n.__name__}{e.__name__}Graph", nodes=(list[n], Field(default_factory=list)),
                             edges=(list[e], Field(default_factory=list)))
        out[path] = {"yaml": raw, "prompt": p, "spec": json.dumps(s.model_json_schema(), ensure_ascii=False)}
    print(json.dumps(out, ensure_ascii=False))
else:
    splitter = RecursiveCharacterTextSplitter(chunk_size=2048, chunk_overlap=256,
        separators=["\n\n", "\n", "。", "！", "？", ". ", "! ", "? ", " ", ""])
    out = []
    for path in sys.argv[2:]:
        text = open(path, encoding="utf-8").read()
        out.append(splitter.split_text(text) if len(text) > 2048 else [text])
    print(json.dumps(out, ensure_ascii=False))
"""

SMOKE_PROBE = r"""
import json, sys, warnings
warnings.simplefilter("ignore")
import logging; logging.disable(logging.CRITICAL)
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.embeddings import FakeEmbeddings
from langchain_core.runnables import RunnableLambda
from hyperextract.utils.template_engine import Template
template, text, responses = sys.argv[1], open(sys.argv[2], encoding="utf-8").read(), json.load(open(sys.argv[3]))
state = {"i": 0}
class Canned(BaseChatModel):
    @property
    def _llm_type(self): return "canned"
    def _generate(self, *a, **k): raise AssertionError("unstructured call")
    def with_structured_output(self, schema, **k):
        def one(_):
            r = responses[min(state["i"], len(responses) - 1)]; state["i"] += 1
            return schema.model_validate(r)
        return RunnableLambda(one)
ka = Template.create(template, "en", llm_client=Canned(), embedder=FakeEmbeddings(size=8), max_workers=1)
ka.feed_text(text, source_id="parity")
print(json.dumps(ka.data.model_dump(), ensure_ascii=False))
"""


def upstream_python() -> Path | None:
    import shutil
    he = shutil.which("he")
    if not he:
        return None
    py = Path(he).resolve().parent / "python"
    return py if py.exists() else None


def parity(docs: int | None = None) -> int:
    """Every template's YAML, prompt and schema, every landed document's chunks, and the merged result of canned
    replies on a multi-chunk text — this port against the installed upstream package, compared exactly."""
    import subprocess
    import tempfile
    py = upstream_python()
    if py is None:
        print("not reached: upstream HyperExtract is not installed (scripts/install.sh hyperextract)")
        return 2
    paths = sorted(DIR.glob("*.yaml"))
    r = subprocess.run([str(py), "-c", UPSTREAM_PROBE, "templates", *map(str, paths)], capture_output=True, text=True)
    if r.returncode:
        print(r.stderr[-2000:])
        return 1
    theirs = json.loads(r.stdout.strip().splitlines()[-1])
    bad = 0
    for p in paths:
        got = theirs[str(p)]
        mine_yaml = yaml_load(p.read_text(encoding="utf-8"))
        checks = [("yaml", mine_yaml == got["yaml"])]
        if "error" in got:
            try:
                load(p)
                checks.append(("refused as upstream refuses", False))
            except TemplateError:
                checks.append(("refused as upstream refuses", True))
        else:
            t = load(p)
            mine_prompt = prompt(t)
            checks.append(("prompt", (list(mine_prompt) if isinstance(mine_prompt, tuple) else mine_prompt)
                           == got["prompt"]))
            checks.append(("schema", spec(t) == got["spec"]))
        failed = [n for n, ok in checks if not ok]
        bad += bool(failed)
        print(f"  {'ok ' if not failed else 'BAD'} {p.stem:<18} " + " ".join(n for n, _ in checks)
              + (f"  — differs: {', '.join(failed)}" if failed else ""))
    sys.path.insert(0, str(ROOT / "scripts"))
    from subject import rows as manifest_rows
    texts = [ROOT / r["export_path"] for r in manifest_rows() if r.get("export_path")]
    texts = [p for p in texts if p.is_file()][:docs] if docs else [p for p in texts if p.is_file()]
    split_bad, n_chunks = 0, 0
    for start in range(0, len(texts), 60):
        batch = texts[start:start + 60]
        r = subprocess.run([str(py), "-c", UPSTREAM_PROBE, "chunks", *map(str, batch)], capture_output=True, text=True)
        if r.returncode:
            print(r.stderr[-2000:])
            return 1
        for path, want in zip(batch, json.loads(r.stdout.strip().splitlines()[-1])):
            text = path.read_text(encoding="utf-8")
            got = split(text) if len(text) > CHUNK_SIZE else [text]
            n_chunks += len(want)
            if got != want:
                split_bad += 1
                print(f"  BAD chunks of {path.name}: {len(got)} here, {len(want)} upstream")
    print(f"  {'ok ' if not split_bad else 'BAD'} chunks: {len(texts)} documents, {n_chunks} chunks, "
          f"{split_bad} documents differ")
    bad += split_bad
    with tempfile.TemporaryDirectory() as tmp:
        text = Path(tmp) / "long.txt"
        text.write_text(multi_chunk_text(), encoding="utf-8")
        for name in sorted(f.stem for f in FIXTURES.glob("*.json") if f != PINNED):
            responses = canned_replies(name)
            reply = Path(tmp) / f"{name}.json"
            reply.write_text(json.dumps(responses, ensure_ascii=False), encoding="utf-8")
            r = subprocess.run([str(py), "-c", SMOKE_PROBE, str(DIR / f"{name}.yaml"), str(text), str(reply)],
                               capture_output=True, text=True)
            if r.returncode:
                bad += 1
                print(f"  BAD {name}: upstream failed: {r.stderr.strip().splitlines()[-1:]}")
                continue
            want = json.loads(r.stdout.strip().splitlines()[-1])
            t = load(DIR / f"{name}.yaml")
            got, _ = extract(t, text.read_text(encoding="utf-8"), canned(responses))
            same = got == want if t.type == "list" else _same_rows(got, want)
            bad += not same
            print(f"  {'ok ' if same else 'BAD'} {name:<18} merged result of {len(chunks(t, text.read_text()))} "
                  f"chunks{'' if t.type == 'list' else ' (order-free: a set or graph is keyed)'}")
    print(f"\nparity with HyperExtract {UPSTREAM[:7]}: {'every comparison holds' if not bad else f'{bad} FAILED'}")
    return 1 if bad else 0


def _same_rows(a: dict, b: dict) -> bool:
    def norm(d: dict) -> dict:
        return {k: sorted(json.dumps(r, sort_keys=True, ensure_ascii=False) for r in v) for k, v in d.items()}
    return norm(a) == norm(b)


def multi_chunk_text() -> str:
    """A text the splitter cuts into several chunks, built from the committed fixture's own lines."""
    base = (FIXTURES / "reading.txt").read_text(encoding="utf-8").strip()
    return "\n\n".join(f"Abschnitt {i}.\n{base}" for i in range(80))


def canned_replies(name: str) -> list[Any]:
    """Per chunk a different reply: the fixture, then its first record alone, then the fixture with every record's
    optional fields emptied — so a merge that keeps, overwrites or overlays shows it."""
    full = json.loads((FIXTURES / f"{name}.json").read_text(encoding="utf-8"))
    if "items" in full:
        first = {"items": full["items"][:1]}
        thin = {"items": [{k: v for k, v in row.items() if k in ("name", "term", "source", "target", "type", "quote",
                                                                    "stance")} for row in full["items"]]}
    else:
        first = {"nodes": full["nodes"][:2], "edges": full["edges"][:1]}
        thin = full
    return [full, first, thin]


# ---- self-test --------------------------------------------------------------------------------------------------

# What HyperExtract 395039e sends for the committed TermReadings template, recorded from the upstream package by
# `parity`; the self-test holds the port to it without the package installed.
PINNED = FIXTURES / "upstream-395039e.json"
# Real documents of different shapes — a chapter outline, a style guide, a narrative text, an English theory document,
# the largest landed file — whose chunks upstream cut are pinned as one digest each (`Sources/` never changes).
PINNED_DOCS = ("koharenz-protokoll-strukturierter-outline-2026-05-18-md", "koharenz-protokoll-sprach-dna-2026-05-13-md",
               "kp-kap25-2026-09-14-md", "systemic-architecture-specification-the-coherence-protocol-w",
               "kohaerenz-protokoll")


def _digest(parts: list[str]) -> str:
    import hashlib
    return f"{len(parts)}:" + hashlib.sha256(json.dumps(parts, ensure_ascii=False).encode()).hexdigest()


def pin() -> int:
    """Record upstream's prompt and schema for every template, and its chunks of the multi-chunk text."""
    import subprocess
    import tempfile
    py = upstream_python()
    if py is None:
        print("not reached: upstream HyperExtract is not installed (scripts/install.sh hyperextract)")
        return 2
    paths = sorted(DIR.glob("*.yaml"))
    r = subprocess.run([str(py), "-c", UPSTREAM_PROBE, "templates", *map(str, paths)], capture_output=True, text=True)
    theirs = json.loads(r.stdout.strip().splitlines()[-1])
    with tempfile.TemporaryDirectory() as tmp:
        text = Path(tmp) / "long.txt"
        text.write_text(multi_chunk_text(), encoding="utf-8")
        r2 = subprocess.run([str(py), "-c", UPSTREAM_PROBE, "chunks", str(text)], capture_output=True, text=True)
        split_want = json.loads(r2.stdout.strip().splitlines()[-1])[0]
    docs = [ROOT / "Sources" / "drive" / f"{slug}.md" for slug in PINNED_DOCS]
    r3 = subprocess.run([str(py), "-c", UPSTREAM_PROBE, "chunks", *map(str, docs)], capture_output=True, text=True)
    doc_chunks = {slug: _digest(c) for slug, c in zip(PINNED_DOCS, json.loads(r3.stdout.strip().splitlines()[-1]))}
    out = {"upstream": UPSTREAM, "templates": {Path(p).stem: {"prompt": v.get("prompt"), "spec": v.get("spec")}
                                               for p, v in theirs.items()},
           "chunks_of_multi_chunk_text": split_want, "chunks_of_documents": doc_chunks}
    PINNED.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{PINNED.relative_to(ROOT)}: {len(out['templates'])} templates, {len(split_want)} chunks")
    return 0


def selftest() -> int:
    cases: list[tuple[str, bool]] = []
    pinned = json.loads(PINNED.read_text(encoding="utf-8"))
    for name, want in sorted(pinned["templates"].items()):
        t = load(DIR / f"{name}.yaml")
        p = prompt(t)
        cases.append((f"{name}: prompt and schema are upstream's",
                      (list(p) if isinstance(p, tuple) else p) == want["prompt"] and spec(t) == want["spec"]))
    cases.append(("the splitter cuts the multi-chunk text as LangChain does",
                  split(multi_chunk_text()) == pinned["chunks_of_multi_chunk_text"]))
    for slug, want in sorted(pinned.get("chunks_of_documents", {}).items()):
        path = ROOT / "Sources" / "drive" / f"{slug}.md"
        text = path.read_text(encoding="utf-8")
        cases.append((f"{slug}: cut into upstream's chunks",
                      _digest(split(text) if len(text) > CHUNK_SIZE else [text]) == want))
    cases.append(("a text that fits is one chunk, unsplit", chunks(load(DIR / "TermReadings.yaml"), " a \n") == [" a \n"]))
    cases.append(("a word longer than a chunk is cut at characters",
                  [len(c) for c in split("x" * 5000, 2048, 256)] == [2048, 2048, 1416]))
    # a reply is checked as pydantic checks it
    t = load(DIR / "TermReadings.yaml")
    row = json.loads((FIXTURES / "TermReadings.json").read_text(encoding="utf-8"))["items"][0]
    cases.append(("a valid reply keeps its records", validate(t, {"items": [row]}) == {"items": [row]}))
    cases.append(("a missing list is an empty one", validate(t, {}) == {"items": []}))
    cases.append(("a key the template does not name is dropped",
                  validate(t, {"items": [{**row, "extra": 1}]}) == {"items": [row]}))
    for label, bad in (("a null required field", {**row, "quote": None}), ("a number for text", {**row, "quote": 3}),
                       ("a missing required field", {k: v for k, v in row.items() if k != "quote"})):
        try:
            validate(t, {"items": [bad]})
            cases.append((f"{label} is refused", False))
        except ValueError:
            cases.append((f"{label} is refused", True))
    # merging
    loc = load(DIR / "LocationRegistry.yaml")
    a = {"name": "A", "level": "1", "source": None, "function": None, "characters": None}
    b = {"name": "A", "level": None, "source": "doc", "function": None, "characters": ["x"]}
    cases.append(("merge_field lays later non-null fields over earlier ones",
                  merge(loc, [{"items": [a]}, {"items": [b]}])["items"]
                  == [{"name": "A", "level": "1", "source": "doc", "function": None, "characters": ["x"]}]))
    g = load(DIR / "StatedRelations.yaml")
    n1, n2 = {"name": "A", "type": "x"}, {"name": "B", "type": "y"}
    e1 = {"source": "A", "target": "B", "type": "t", "quote": "q1"}
    e2 = {"source": "A", "target": "B", "type": "t", "quote": "q2"}
    dangling = {"source": "A", "target": "C", "type": "t", "quote": "q3"}
    got = merge(g, [{"nodes": [n1, n2], "edges": [e1, dangling]}, None, {"nodes": [n1], "edges": [e2]}])
    cases.append(("a graph keeps the first edge of a key, drops a dangling one and a failed chunk",
                  got == {"nodes": [n1, n2], "edges": [e1]}))
    try:
        fold([a], lambda r: r["name"], "llm_balanced")
        cases.append(("an llm merge is refused", False))
    except TemplateError:
        cases.append(("an llm merge is refused", True))
    # extraction: a failed chunk is dropped, the others merge in order
    replies = iter([{"items": [row]}, "not an object", {"items": [row]}])
    def ask(text: str, body: str, check):
        assert "{source_text}" not in text and text.startswith("# Role and Task:")
        return check(next(replies))
    long = "\n\n".join(["Absatz. " * 200] * 3)
    data, log = extract(t, long, ask)
    cases.append(("three chunks, the failed one dropped",
                  [c["ok"] for c in log] == [True, False, True] and data == {"items": [row, row]}))
    # every committed fixture goes through extract unchanged, as the native smoke test held upstream
    text = (FIXTURES / "reading.txt").read_text(encoding="utf-8")
    for f in sorted(FIXTURES.glob("*.json")):
        if f.name == PINNED.name:
            continue
        want = json.loads(f.read_text(encoding="utf-8"))
        tt = load(DIR / f"{f.stem}.yaml")
        got, _ = extract(tt, text, canned([want]))
        cases.append((f"{f.stem}: the fixture's reply comes back as the template's data",
                      got == want if tt.type == "list" else _same_rows(got, want)))
    # the YAML subset refuses what it does not read
    for label, src in (("an anchor", "a: &x 1\n"), ("a block scalar", "a: |\n  b\n"), ("a flow mapping", "a: {b: 1}\n"),
                       ("a tab in the indentation", "a:\n\t- b\n")):
        try:
            yaml_load(src)
            cases.append((f"YAML: {label} is refused", False))
        except TemplateError:
            cases.append((f"YAML: {label} is refused", True))
    cases.append(("YAML: quotes, flow lists, comments",
                  yaml_load("a: 'it''s' # c\nb: [x, 'y, z']\nc:\n  - d: \"e\\u00e4\"\n    f: true\n")
                  == {"a": "it's", "b": ["x", "y, z"], "c": [{"d": "eä", "f": True}]}))
    # the validator names what it must
    import tempfile
    good = (DIR / "LocationRegistry.yaml").read_text(encoding="utf-8")
    defects = {"HE-T003": good.replace("item_id: name", "item_id: nom"),
               "HE-T005": good.replace("label: '{name} ({level})'", "label: '{nom}'"),
               "HE-T002 warning": good.replace("- name: function", "- name: register").replace(
                   "fields_for_search: [name, function]", "fields_for_search: [name]")}
    with tempfile.TemporaryDirectory() as tmp:
        for code, src in defects.items():
            p = Path(tmp) / "LocationRegistry.yaml"
            p.write_text(src, encoding="utf-8")
            cases.append((f"the validator names {code}", any(d.startswith(code) for d in diagnose(load(p)))))
    cases.append(("every committed template loads with no diagnosis",
                  all(not diagnose(load(p)) for p in sorted(DIR.glob("*.yaml")))))
    failed = [n for n, ok in cases if not ok]
    for n, ok in cases:
        if not ok:
            print(f"FAIL {n}")
    print(f"hx: {len(cases) - len(failed)} of {len(cases)} cases hold" + (" — FAILED" if failed else "")
          + f"; offline, against HyperExtract {UPSTREAM[:7]} as pinned")
    return 1 if failed else 0


# ---- CLI --------------------------------------------------------------------------------------------------------

def main(argv: list[str]) -> int:
    import argparse
    ap = argparse.ArgumentParser(prog="hx.py", description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="command", required=True)
    c = sub.add_parser("check")
    c.add_argument("templates", nargs="*", type=Path)
    p = sub.add_parser("prompt")
    p.add_argument("template", type=Path)
    p.add_argument("--text", type=Path)
    k = sub.add_parser("chunks")
    k.add_argument("slug")
    k.add_argument("--size", type=int, default=CHUNK_SIZE)
    k.add_argument("--overlap", type=int, default=CHUNK_OVERLAP)
    s = sub.add_parser("smoke")
    s.add_argument("template", type=Path)
    s.add_argument("--text", type=Path, required=True)
    s.add_argument("--response", type=Path, required=True)
    q = sub.add_parser("parity")
    q.add_argument("--docs", type=int)
    sub.add_parser("pin")
    sub.add_parser("selftest")
    a = ap.parse_args(argv)
    if a.command == "selftest":
        return selftest()
    if a.command == "parity":
        return parity(a.docs)
    if a.command == "pin":
        return pin()
    if a.command == "check":
        bad = 0
        for path in a.templates or sorted(DIR.glob("*.yaml")):
            try:
                found = diagnose(load(path))
            except TemplateError as exc:
                found = [str(exc)]
            bad += bool(found)
            print(f"{'ok ' if not found else 'BAD'} {path.name}" + "".join(f"\n    {d}" for d in found))
        return 1 if bad else 0
    if a.command == "prompt":
        t = load(a.template)
        main_prompt = prompt(t)
        main_prompt = main_prompt[0] if isinstance(main_prompt, tuple) else main_prompt
        text = a.text.read_text(encoding="utf-8") if a.text else "{source_text}"
        print(render(main_prompt, source_text=chunks(t, text)[0]) if a.text else main_prompt)
        print("\n--- schema ---\n" + spec(t))
        return 0
    if a.command == "chunks":
        sys.path.insert(0, str(ROOT / "scripts"))
        from subject import document
        doc = document(a.slug)
        parts = split(doc.body, a.size, a.overlap) if len(doc.body) > a.size else [doc.body]
        for i, part in enumerate(parts):
            print(f"{i:>3} {len(part):>5}  {part[:60]!r}")
        print(f"{len(parts)} chunks, {len(doc.body)} characters")
        return 0
    if a.command == "smoke":
        t = load(a.template)
        response = json.loads(a.response.read_text(encoding="utf-8"))
        data, log = extract(t, a.text.read_text(encoding="utf-8"),
                            canned(response if isinstance(response, list) else [response]))
        if not any(c["ok"] for c in log):
            print(f"REFUSED: {log[-1].get('error')}", file=sys.stderr)
            return 1
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
