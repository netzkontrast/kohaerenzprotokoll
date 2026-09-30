#!/usr/bin/env python3
"""HyperExtract candidates as proposal relations of the shared store — and the report that says what each contract yielded.

`reading_extract.py stage` keeps what a model extracted, its quotation placed on a line by code and its
names checked against the document: `Plan/runs/<slug>/hyperextract/<run>/candidates.jsonl`. This module reads
those files, never the model, and does three things with them:

- **loads** them into the store's one build (`askdb.collect`) as `P_HE_<KIND>` edges from the line that holds
  the quotation to each term page or verified entity the candidate's names contain. Like every `P_` type they
  stay out of the core ranking, the paths and the communities, and no query for stated facts names one. A
  candidate is a proposal, so every edge says its template, its run, its stance and its quality;
- **grades** each candidate by code, never by judgement: `quality` 2 when its cue words stand in the quote and
  every name stands inside it, 1 when one of the two does, 0 when neither. The cues are the words each
  contract's rules tell the model to look for. **The grade is not a filter**: against 199 records a reader
  labelled, the share marked ok was 64 %, 52 % and 79 % at grades 0, 1 and 2, because the contracts that read
  structure — a list item under a heading — are right without a cue or a name in the quotation. Only where the
  cue is the contract (`CUE_REQUIRED`) does a missing one rule a record out;
- **reports** per contract what it yielded — candidates, refusals by reason, how many grade 2, how many attach to
  a page or an entity, what it cost — and which names attach to nothing, which is a list of terms the wiki
  has no page for.

It also **gates** a document for a contract: `gate(slug, template)` keeps the paragraphs whose words hold a cue of
the contract, with their neighbours, so that a run sends the model a fifth of the text and pays a fifth. Quotations
are still placed against the whole document.

    python3 scripts/hegraph.py report [--unresolved 15]   # what each contract yielded, and at what price
    python3 scripts/hegraph.py gate <slug> <Template>     # the share of a document a contract would send
    python3 scripts/hegraph.py selftest

Standard library only.
"""

from __future__ import annotations

import json
import re
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

RUNS = ROOT / "Plan" / "runs"
TEMPLATES = ROOT / "Plan" / "hyperextract"

# template stem -> the store's relation name, P_HE_<KIND>. A template with no entry is not loaded; the selftest
# fails on a template file that has none, so adding a contract means naming its relation here.
KIND = {
    "TermReadings": "READING", "StatedRelations": "REL", "RelationReadings": "REL",
    "AliasPairs": "ALIAS", "TermContrasts": "CONTRAST", "TermDefinitions": "DEFINES", "Analogies": "ANALOGY",
    "TermTaxonomy": "TAXON", "CausalLinks": "CAUSAL", "Attributions": "SAYS", "Rules": "RULE", "Quantities": "QUANT",
    "StandingClaims": "STANDING", "CastRoles": "ROLE", "Precedence": "BEFORE", "ChapterBeats": "BEAT",
    "OpenPoints": "OPEN", "CardFields": "CARD", "ChapterCards": "CHAPTER", "Anchors": "ANCHOR", "Knowledge": "KNOWS",
    "ProseRules": "PROSERULE", "StructureBeats": "STRUCT", "ThemeMotifs": "THEME", "EntityFacts": "FACT",
    "Storypoints": "STORYPOINT", "DiegeticTerms": "DIEGETIC", "Locks": "LOCK", "Utterances": "UTTERANCE",
    "Pitch": "PITCH", "LocationRegistry": "LOCATION", "TermCensus": "CENSUS",
}

# the words each contract's rules name, as a regex on the quotation and on the paragraphs a gate keeps. Broad on
# purpose: a cue that is absent rules a candidate out, a cue that is present proves little.
CUES = {
    "ALIAS": r"\(|/|\boder\b|\bbzw\b|\bauch\b|genannt|\balias\b|\bd\. ?h\b|im Folgenden|=|sogenannt|\bsog\.",
    "CONTRAST": r"\bvs\b|versus|Gegensatz|\bnicht\b[^.]{0,60}\bsondern\b|Spannung|Unterschied|unterscheid|während|hingegen|dagegen|einerseits|andererseits|im Vergleich|gegenüber|\bstatt\b|anstatt|abgrenz|Kontrast|\|",
    "DEFINES": r"\bist\b|\bsind\b|bezeichnet|bedeutet|versteht|verstanden|definiert|\bheißt\b|\bnennt\b|beschreibt|steht für|d\. ?h\.|:",
    "ANALOGY": r"entspricht|analog|Metapher|basiert|modelliert|steht für|verkörpert|angelehnt|Vorbild|Äquivalent|Analogie|Abbild|übersetzt|abgeleitet|Muster|Bezug|\|",
    "TAXON": r"\bist ein|\bist eine|Art von|gehört zu|Teil von|besteht aus|umfasst|unterteilt|enthält|Mitglied|Gruppe|Klasse|Untertyp|Kategorie|zählt zu|:",
    "CAUSAL": r"führt zu|verursacht|löst aus|ermöglicht|verhindert|\bweil\b|\bdaher\b|dadurch|infolge|erzwingt|setzt voraus|Folge|bewirkt|deshalb|deswegen|daraus|blockiert|erzeugt",
    "SAYS": r"\bnach\b|\blaut\b|gemäß|postuliert|zeigt|besagt|formuliert|argumentiert|Studie|Theorie|Leitlinie|zufolge|betont|definiert|beschreibt|zeigen|belegen",
    "RULE": r"\bmuss\b|\bmüssen\b|\bdarf\b|dürfen|nur wenn|\bimmer\b|\bstets\b|kann nur|wenn\b[^.]{0,80}\bdann\b|verpflichtet|Regel|Direktive|Axiom|verboten|niemals|\bnie\b|\bkeine?\b|ausschließlich|Gesetz|Prinzip",
    "QUANT": r"\d|\b(?:zwei|drei|vier|fünf|sechs|sieben|acht|neun|zehn|elf|zwölf|dreizehn)\b",
    "STANDING": r"Canon|kanonisch|verbindlich|Source of Truth|Ground Truth|Entwurf|veraltet|ersetzt|überholt|gilt nicht mehr|maßgeblich|autoritativ|gültig|deprecated",
    "ROLE": r"\bist der\b|\bist die\b|\bist das\b|fungiert|Rolle|übernimmt|verwaltet|zuständig|verantwortlich|Funktion|Hüter|Guardian|Protagonist|Antagonist|Aufgabe|\|",
    "BEFORE": r"\bvor\b|\bnach\b|zuerst|\bdann\b|danach|anschließend|folgt|geht voraus|Phase|bevor|sobald|Schritt|Stufe|zunächst|schließlich|\bAkt\b",
    "BEAT": r"Kap(?:itel|\.)?\s*\d|Chapter\s*\d",
    "OPEN": r"offen|ungeklärt|unklar|noch zu|muss geprüft|TBD|Frage|bleibt|nicht geklärt|\?|\bOQ",
    "CARD": r"\bwill\b|wünscht|möchte|\bZiel\b|Wunsch|braucht|Bedürfnis|Angst|fürchtet|Wunde|Trauma|Lüge|Glaube|Widerspruch|Bogen|Stimme|spricht|\bTon\b|Beziehung|Funktion|Motivation|Überzeugung|Verletzung|Rolle",
    "CHAPTER": r"Kap(?:itel|\.)?\s*\d|Chapter\s*\d",
    "ANCHOR": r"gepflanzt|aufgegriffen|kehrt wieder|ausgezahlt|aufgelöst|geschlossen|vorbereitet|Payoff|Setup|Motiv|Anker|Echo|Foreshadow|Vorausdeutung|pflanzt|Vorbereitung|Auflösung",
    "KNOWS": r"\bweiß\b|weiss|glaubt|ahnt|erfährt|kann noch nicht|missversteht|Leser|Wissen|Informationsbilanz|\bkennt\b|erkennt|bemerkt|versteht",
    "PROSERULE": r"\bnie\b|keine|\bimmer\b|\bmuss\b|verboten|Lock|gelockt|Regel|bewusst|absichtlich|Stilcode|Verbot|Prosa|Stimme|Erzähl|Tempus|Perspektive|Metapher|\bTon\b",
    "STRUCT": r"\bAkt\b|Phase|Mittelpunkt|Wendepunkt|Höhepunkt|Krise|Auslöser|Klammer|Modus|Storyform|Rahmen|\bEnde\b|Beginn|Übergang|Ketsu|Kishōtenketsu",
    "THEME": r"These|Prämisse|Thema|steht für|symbolisiert|Motiv|Leitmotiv|\bFrage\b|\bKern\b|Grundton|Bedeutung|zentral|Botschaft",
    "FACT": r"\bheißt\b|genannt|\balt\b|Jahre|aussieht|\bträgt\b|Farbe|Haar|Augen|geboren|Vergangenheit|befindet|\bliegt\b|besteht|Größe|Höhe|\bName\b",
    "STORYPOINT": r"Signpost|Dynamic|Resolve|Throughline|Storypoint|Storyform|\bträgt\b|Concern|Issue|Problem|Solution|Focus|Direction|Growth|Approach",
    "DIEGETIC": r"erscheint als|heißt in der Prosa|diegetisch|wird zu|\bstatt\b|nie als|umbenannt|im Text|Prosa|Vokabel|Übersetzung|Begriff",
    "LOCK": r"Lock|gelockt|fixiert|festgelegt|beschlossen|Entscheidung|\bStand\b|\d{4}-\d{2}-\d{2}",
    "UTTERANCE": r"[„»\"“]|—|–\s*[A-ZÄÖÜ]",
    "PITCH": r"Logline|Genre|vergleichbar|Zielgruppe|Hook|Pitch|Versprechen|Leser von|Roman|Thriller|Science|Horror",
}
CUES = {k: re.compile(v, re.I) for k, v in CUES.items()}
MAX_QUOTE = 400


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()] if path.exists() else []


def staged(root: Path = RUNS):
    """Every row a run staged whose quotation is placed on exactly one line, with the run it came from:
    (slug, run, row). `row["admitted"]` says on what footing it enters the store:

    - `names`: a candidate — the quotation is placed and every name the model wrote stands in the document;
    - `quote`: refused only for `surface absent from document` — the model's slot text is its own wording
      (an inflection, a clause, `Lex` before the gate learned three-letter names) — while the quotation is
      placed on one line. The line is the evidence, and the pages in it are found by code, never by the slot."""
    for f in sorted(root.glob("*/hyperextract/*/report.json")):
        slug, run = f.parts[-4], f.parts[-2]
        for row in json.loads(f.read_text(encoding="utf-8"))["rows"]:
            if row.get("quote_status") != "placed" or len(row.get("lines") or []) != 1:
                continue
            if row["status"] == "candidate":
                tier = "names"
            elif row["status"] == "refused" and row.get("reason") == "surface absent from document":
                tier = "quote"
            else:
                continue
            yield slug, run, {**row, "template": row.get("template", "TermReadings.yaml"), "admitted": tier}


# Contracts whose record is wrong without its cue: on the 2026-09-30 labels an alias without an alias word was
# ok in 0 of 7 rows (with one, 5 of 7) and an order without an order word in 0 of 9 (with one, 2 of 2). The other
# contracts read structure — a list item under a heading — and their right rows carry no cue, so a cue is not asked
# of them. Provisional: seven and nine rows; retire when a larger labelled sample says the cue does not matter.
CUE_REQUIRED = {"ALIAS", "BEFORE"}


def admitted(row: dict) -> bool:
    """Whether a staged candidate enters the store: its quotation is placed on one line, its names are in the
    document (the staging gate), and, for the contracts in `CUE_REQUIRED`, its cue words stand in the quotation."""
    kind = kind_of(row)
    return bool(kind) and (kind not in CUE_REQUIRED or bool(CUES[kind].search(row["raw"]["quote"])))


def names(row: dict) -> list[str]:
    raw = row["raw"]
    return [raw["term"]] if row["kind"] == "reading" else [raw["source"], raw["target"]]


def kind_of(row: dict) -> str | None:
    return KIND.get(row.get("template", "").removesuffix(".yaml"))


def quality(row: dict) -> int:
    """2: a cue of the contract and every name stand in the quotation. 1: one of the two. 0: neither."""
    kind = kind_of(row)
    quote = row["raw"]["quote"]
    cue = bool(kind and (kind not in CUES or CUES[kind].search(quote)))
    inside = all(n.lower() in quote.lower() for n in names(row))
    return int(cue) + int(inside)


def surface_matcher(surfaces: dict[str, str]):
    """One pattern for every surface, longest first, standing alone as `wiki_index.mention` does."""
    ordered = sorted((s for s in surfaces if len(s) >= 3), key=len, reverse=True)
    if not ordered:
        return None
    return re.compile(r"(?<![\w-])(?:" + "|".join(re.escape(s) for s in ordered) + r")(?![\w-])")


def resolve(text: str, matcher, surfaces: dict[str, str]) -> list[str]:
    """The nodes a name contains: every page surface or verified entity standing alone in it."""
    if not matcher:
        return []
    return list(dict.fromkeys(surfaces[m.group(0)] for m in matcher.finditer(text)))


def edges(nodes: dict, surfaces: dict[str, str], root: Path = RUNS, marked: dict | None = None) -> tuple[dict, list[tuple]]:
    """What `askdb.collect` loads: the contract nodes the edges need, and the edges
    (line key, node key, props, `P_HE_<KIND>`), every end a node of the store.

    Each admitted row gives one edge from its quotation's line to its contract (`he:<KIND>`, role `line`): the
    line was read as a <kind>, which is what a finder asks. A row whose names stand in the document adds one
    edge to each page or entity a name contains (role `term`, `source` or `target`); a row whose slot text is
    the model's own wording adds one to each page or entity the *quotation* contains, found by code (role `quote`).
    Two runs that read one line the same way are two edges: that is agreement, and it is kept."""
    matcher = surface_matcher(surfaces)
    marked = labels() if marked is None and root == RUNS else (marked or {})
    new, out, seen, tally = {}, [], set(), defaultdict(Counter)
    for slug, run, row in staged(root):
        kind = kind_of(row)
        if not admitted(row):
            continue
        line = f"line:{slug}:{row['lines'][0]}"
        if line not in nodes:
            continue
        raw = row["raw"]
        hub = f"he:{kind}"
        new[hub] = ({"kind": kind}, "Contract")
        if row["id"][6:14] in marked:
            tally[kind][marked[row["id"][6:14]]["label"]] += 1
        base = {"template": row["template"].removesuffix(".yaml"), "run": run, "quality": quality(row),
                "stance": raw.get("stance", ""), "extractor": row.get("extractor", ""), "id": row["id"],
                "admitted": row["admitted"]}
        if "type" in raw:
            base["type"] = raw["type"][:80]
        ends = [("line", hub, "")]
        if row["admitted"] == "names":
            slots = [("term", raw["term"])] if row["kind"] == "reading" else [("source", raw["source"]), ("target", raw["target"])]
            for role, text in slots:
                other = "" if row["kind"] == "reading" else (raw["target"] if role == "source" else raw["source"])[:120]
                ends += [(role, key, other) for key in resolve(text, matcher, surfaces)]
        else:
            ends += [("quote", key, "") for key in resolve(raw["quote"], matcher, surfaces)]
        for role, key, other in ends:
            if key != hub and key not in nodes:
                continue
            if (line, key, kind, role, run) in seen:
                continue
            seen.add((line, key, kind, role, run))
            out.append((line, key, {**base, "role": role, **({"other": other} if other else {})}, f"P_HE_{kind}"))
    # what a reader labelled, on the contract's node: how many rows, how many right. Absent when nothing was
    # labelled — an unmeasured contract has no precision, not a precision of zero (P23).
    for kind, c in tally.items():
        n = sum(c.values())
        new[f"he:{kind}"][0].update(labelled=n, ok=c[GOOD], part=c[PART], wrong=c[WRONG],
                                    precision=round(c[GOOD] / n, 3), precision_lenient=round((c[GOOD] + c[PART]) / n, 3))
    return new, out


# ── the labels ────────────────────────────────────────────────────────────────

LABELS = ROOT / "Plan" / "runs" / "hyperextract-templates-2026-09-30" / "labels.jsonl"
GOOD, PART, WRONG = "ok", "part", "wrong"


def labels(path: Path = LABELS) -> dict[str, dict]:
    """A person's or a session's reading of a sample, by the first eight characters of a candidate's id:
    `ok` (the quotation states what the record says, as typed), `part` (it says something near it), `wrong`.
    They are the only measure of precision here; the grade is measured against them, never the reverse."""
    return {r["id"]: r for r in read_jsonl(path)}


# ── the report ────────────────────────────────────────────────────────────────

def catalogue(root: Path = ROOT) -> tuple[dict[str, str], dict[str, str]]:
    """Page surfaces and verified entity names, each mapped to its node key."""
    index = json.loads((root / "Wiki" / "index.json").read_text(encoding="utf-8"))
    pages = {}
    for slug, term in index["terms"].items():
        for s in term.get("surfaces") or []:
            if len(s) >= 3:
                pages.setdefault(s, f"term:{slug}")
    import entities
    ents = {n: f"entity:{n}" for n in entities.verified_entities(entities.lists()) if len(n) >= 3}
    return pages, {**ents, **pages}


def agreement(found: dict[str, set], cited: dict[str, set]) -> str:
    """Of the lines a contract found, the share some term page also quotes; and of the lines the pages quote in
    the documents the contract ran on, the share it found. Two numbers, neither a precision: a page cites what a
    reader chose, a contract quotes what its rules match."""
    mine = sum(len(v) for v in found.values())
    hit = sum(len(v & cited.get(d, set())) for d, v in found.items())
    theirs = sum(len(cited.get(d, set())) for d in found)
    return f"{hit / mine:.0%} ({hit}/{mine}) | {hit / theirs:.0%} ({hit}/{theirs}) |" if mine and theirs else " | |"


def share(c: Counter, keys: tuple[str, ...]) -> str:
    n = sum(c.values())
    return "" if not n else f"{n}: " + " / ".join(f"{sum(c[k] for k in keys[:i + 1]) / n:.0%}" for i in range(len(keys) - 1))


def report(root: Path = ROOT, unresolved: int = 15) -> str:
    pages, surfaces = catalogue(root)
    matcher = surface_matcher(surfaces)
    runs = root / "Plan" / "runs"
    marked = labels(runs / "hyperextract-templates-2026-09-30" / "labels.jsonl")
    import graph as kg
    cited = defaultdict(set)                # the lines the term pages quote, verified, by document
    for evs in kg.build()["evidence"].values():
        for ev in evs:
            if ev.get("status") == "verified" and ev.get("doc"):
                cited[ev["doc"]].add(ev["line"])
    per = defaultdict(lambda: {"docs": set(), "empty": 0, "tier": Counter(), "q": Counter(), "attach": Counter(),
                               "refused": Counter(), "cost": 0.0, "lab": defaultdict(Counter), "by_q": defaultdict(Counter),
                               "found": defaultdict(set)})
    by_doc = defaultdict(lambda: {"contracts": set(), "cost": 0.0, "found": set()})
    loose = Counter()
    for f in sorted(runs.glob("*/hyperextract/*/report.json")):
        for r in json.loads(f.read_text(encoding="utf-8"))["rows"]:
            name = r.get("template", "TermReadings.yaml").removesuffix(".yaml")
            kept = r.get("quote_status") == "placed" and len(r.get("lines") or []) == 1 and \
                r.get("reason") in (None, "surface absent from document")
            if r["status"] == "refused" and not kept:
                per[name]["refused"][r["reason"]] += 1
    for usage in sorted(runs.glob("*/hyperextract/*/usage.json")):
        u = json.loads(usage.read_text(encoding="utf-8"))
        name = u["template"].removesuffix(".yaml")
        per[name]["docs"].add(usage.parts[-4])
        per[name]["cost"] += u.get("cost_usd", 0.0)
        by_doc[usage.parts[-4]]["contracts"].add(name)
        by_doc[usage.parts[-4]]["cost"] += u.get("cost_usd", 0.0)
        # every call answered and the list came back empty: the contract found nothing in this document. Only the
        # calls' own record can say so — `reading_extract` refuses an empty list, because HyperExtract can also
        # swallow a schema error into one (its rule, kept).
        if str(u.get("failed", "")).startswith("empty or invalid candidate list") and not u.get("failed_calls"):
            per[name]["empty"] += 1
    for slug, run, row in staged(runs):
        name = row["template"].removesuffix(".yaml")
        p, tier = per[name], row["admitted"]
        p["docs"].add(slug)
        p["tier"][tier] += 1
        p["q"][quality(row)] += 1
        p["found"][slug].add(row["lines"][0])
        by_doc[slug]["found"].add(row["lines"][0])
        ends = [resolve(t, matcher, surfaces) for t in names(row)]
        inside = resolve(row["raw"]["quote"], matcher, surfaces)
        p["attach"][(tier, "all" if all(ends) else "some" if any(ends) else "none")] += 1
        p["attach"][(tier, "quote" if inside else "noquote")] += 1
        if tier == "names":
            for t, e in zip(names(row), ends):
                if not e and len(t) <= 60:
                    loose[t] += 1
        mark = marked.get(row["id"][6:14])
        if mark:
            p["lab"][tier][mark["label"]] += 1
            p["by_q"][quality(row)][mark["label"]] += 1
    lines = ["# What each contract yielded", "",
             "Per contract, over every run staged in `Plan/runs/*/hyperextract/`. A row enters the store on one of two footings "
             "(`hegraph.staged`): **names** — its quotation is placed on one line and every name the model wrote stands in the "
             "document — or **quote** — refused only because a slot is the model's own wording (an inflection, a clause, a "
             "three-letter name before the gate learned them), while its quotation is placed on one line, so the line is "
             "evidence and the code finds the pages in it. `refused` is what stays out: a quotation not placed, on several "
             "lines, joined, or an empty reply. Precision is only what a reader labelled (`labels.jsonl`): `ok` the quotation "
             "states what the record says, `part` something near it, `wrong` neither.", "",
             "| contract | documents tried | answered, found nothing | rows: names / quote | refused for good | cost, USD | per row | "
             "names: labelled, ok / ok+part | quote: labelled, ok / ok+part | names: every end / one end is a page or entity | "
             "pages found in a quotation | lines a page also cites | the pages' cited lines it finds |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for name in sorted(per):
        p = per[name]
        n = sum(p["tier"].values()) or 1
        refused = sum(p["refused"].values())
        reasons = ", ".join(f"{v} {k.split(':')[0][:24]}" for k, v in p["refused"].most_common(2))
        got = sum(v for (t, k), v in p["attach"].items() if k == "quote")
        lines.append(f"| {name} | {len(p['docs'])} | {p['empty']} | {p['tier']['names']} / {p['tier']['quote']} | "
                     f"{refused}{f' ({reasons})' if refused else ''} | {p['cost']:.2f} | {p['cost'] / n:.3f} | "
                     f"{share(p['lab']['names'], (GOOD, PART, WRONG))} | {share(p['lab']['quote'], (GOOD, PART, WRONG))} | "
                     f"{p['attach'][('names', 'all')] / max(p['tier']['names'], 1):.0%} / "
                     f"{(p['attach'][('names', 'all')] + p['attach'][('names', 'some')]) / max(p['tier']['names'], 1):.0%} | "
                     f"{got / n:.0%} | " + agreement(p["found"], cited))
    graded = Counter()
    for p in per.values():
        for q, c in p["by_q"].items():
            graded.update({(q, k): v for k, v in c.items()})
    if graded:
        lines += ["", "## Does the grade predict a good record?", "",
                  "Over every labelled row: the share a reader marked `ok`, by the grade code gave it (2: a cue of the contract "
                  "and every name stand in the quotation; 1: one of the two; 0: neither). A grade that does not separate them "
                  "is not a filter and is not used as one; only `CUE_REQUIRED` contracts drop a row without its cue.", "",
                  "| grade | labelled | ok | part | wrong | ok share |", "|---|---|---|---|---|---|"]
        for q in (0, 1, 2):
            tot = sum(graded[(q, k)] for k in (GOOD, PART, WRONG))
            if tot:
                lines.append(f"| {q} | {tot} | {graded[(q, GOOD)]} | {graded[(q, PART)]} | {graded[(q, WRONG)]} | "
                             f"{graded[(q, GOOD)] / tot:.0%} |")
    lines += ["", "## Per document: how much of what the pages cite the contracts, together, find", "",
              "| document | lines the pages cite | lines any contract found | of them cited | contracts run | cost, USD |",
              "|---|---|---|---|---|---|"]
    for slug, d in sorted(by_doc.items()):
        theirs = cited.get(slug, set())
        hit = len(d["found"] & theirs)
        lines.append(f"| {slug[:60]} | {len(theirs)} | {len(d['found'])} | "
                     f"{f'{hit} ({hit / len(theirs):.0%} of the pages’ lines)' if theirs else '—'} | {len(d['contracts'])} | {d['cost']:.2f} |")
    lines += ["", f"## Names that attach to nothing — the {unresolved} most frequent", "",
              "A name a contract found in a quotation and no page or entity contains. Each is a candidate for a page, "
              "an alias or an entity, and none is any of them until a person says so.", ""]
    lines += [f"- `{t}` × {c}" for t, c in loose.most_common(unresolved)]
    return "\n".join(lines) + "\n"


# ── the gate ──────────────────────────────────────────────────────────────────

def gate(text: str, template: str, neighbours: int = 1) -> str:
    """The paragraphs of `text` that hold a cue of the contract, with their neighbours, in order."""
    kind = KIND.get(template)
    cue = CUES.get(kind or "")
    paragraphs = re.split(r"\n\s*\n", text)
    if cue is None:
        return text
    keep = set()
    for i, p in enumerate(paragraphs):
        if cue.search(p):
            keep.update(range(max(0, i - neighbours), min(len(paragraphs), i + neighbours + 1)))
    return "\n\n".join(paragraphs[i] for i in sorted(keep))


def cmd_gate(slug: str, template: str) -> None:
    from subject import document
    doc = document(slug)
    kept = gate(doc.body, template)
    print(f"{template} on {slug}: {len(kept):,} of {len(doc.body):,} characters ({len(kept) / len(doc.body):.0%}) "
          f"would be sent; a run costs about that share")


def selftest() -> int:
    cases = []
    names_in_files = {p.stem for p in TEMPLATES.glob("*.yaml")}
    cases.append(("every contract names its store relation", not (names_in_files - set(KIND))))
    cases.append(("every relation has a cue set, or reads plainly", all(k in CUES or k in ("READING", "REL", "LOCATION", "CENSUS")
                                                                        for k in KIND.values())))
    row = {"template": "AliasPairs.yaml", "kind": "relation_reading",
           "raw": {"source": "Juna", "target": "Julia", "type": "same_as", "quote": "Juna (oder Julia) fungiert als Anker", "stance": "asserts"}}
    cases.append(("a cue and both names inside the quote grade 2", quality(row) == 2))
    bad = {**row, "raw": {**row["raw"], "quote": "Juna fungiert als Anker und Julia bleibt still"}}
    cases.append(("no cue but both names inside the quote grades 1", quality(bad) == 1))
    far = {**row, "raw": {**row["raw"], "target": "Julia Mueller", "quote": "Juna fungiert als Anker"}}
    cases.append(("no cue and a name outside the quote grades 0", quality(far) == 0))
    surfaces = {"Juna": "term:juna", "Kael": "term:kael", "Nexus": "entity:Nexus"}
    m = surface_matcher(surfaces)
    cases.append(("a name resolves to every page or entity it contains", resolve("Kael und Juna", m, surfaces) == ["term:kael", "term:juna"]))
    cases.append(("a compound is not the surface it contains", resolve("Junas Weg", m, surfaces) == []))
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        d = root / "doc-x" / "hyperextract" / "run1"
        d.mkdir(parents=True)
        base = {"kind": "relation_reading", "document": "doc-x", "quote_status": "placed", "extractor": "test"}
        good = {**base, "id": "claim:1", "raw": row["raw"], "template": "AliasPairs.yaml", "lines": [12], "status": "candidate", "reason": None}
        two = {**good, "id": "claim:2", "lines": [3, 4]}
        para = {**base, "id": "claim:3", "template": "Knowledge.yaml", "lines": [20], "status": "refused",
                "reason": "surface absent from document",
                "raw": {"source": "Kael", "target": "die Sonde des Lesers", "type": "knows",
                        "quote": "Kael ist die Sonde, die der Leser in das Trauma geschickt hat.", "stance": "asserts"}}
        lost = {**para, "id": "claim:4", "reason": "quote not placed", "quote_status": "unplaced"}
        nocue = {**good, "id": "claim:5", "lines": [30], "raw": {**row["raw"], "quote": "Juna fungiert als Anker und Julia bleibt still"}}
        (d / "report.json").write_text(json.dumps({"rows": [good, two, para, lost, nocue]}), encoding="utf-8")
        nodes = {"line:doc-x:12": ({}, "Line"), "line:doc-x:20": ({}, "Line"), "line:doc-x:30": ({}, "Line"),
                 "term:juna": ({}, "Term"), "term:kael": ({}, "Term")}
        surf = {"Juna": "term:juna", "Julia": "term:julia", "Kael": "term:kael"}
        made, got = edges(nodes, surf, root)
        have = {(e[0], e[1], e[2]["role"], e[3]) for e in got}
        cases.append(("a row gives an edge from its line to its contract", ("line:doc-x:12", "he:ALIAS", "line", "P_HE_ALIAS") in have))
        cases.append(("its names give edges to the pages they contain", ("line:doc-x:12", "term:juna", "source", "P_HE_ALIAS") in have))
        cases.append(("a name that is no node of the store gives no edge", not any(e[1] == "term:julia" for e in got)))
        cases.append(("a slot the document does not hold is admitted on its quotation, the pages found in the quotation",
                      ("line:doc-x:20", "he:KNOWS", "line", "P_HE_KNOWS") in have and ("line:doc-x:20", "term:kael", "quote", "P_HE_KNOWS") in have
                      and all(e[2]["admitted"] == "quote" for e in got if e[0] == "line:doc-x:20")))
        cases.append(("a quotation on two lines and one not placed give nothing",
                      not any(e[0] in ("line:doc-x:3", "line:doc-x:4") for e in got) and len([1 for e in got if e[2]["id"] == "claim:4"]) == 0))
        cases.append(("an alias without its cue is not admitted", not any(e[2]["id"] == "claim:5" for e in got)))
        cases.append(("an edge says its template, run, quality, role and the other name",
                      any(e[2]["template"] == "AliasPairs" and e[2]["run"] == "run1" and e[2]["quality"] == 2
                          and e[2]["role"] == "source" and e[2]["other"] == "Julia" for e in got)))
        cases.append(("the contracts an edge needs come with it", set(made) == {"he:ALIAS", "he:KNOWS"}
                      and all(v[1] == "Contract" for v in made.values())))
        cases.append(("the two footings are told apart", {r["admitted"] for _, _, r in staged(root)} == {"names", "quote"}))
        made2, _ = edges(nodes, surf, root, marked={"1": {"label": "ok"}, "3": {"label": "part"}})
        cases.append(("a labelled contract carries its measured precision on its node",
                      made2["he:ALIAS"][0].get("precision") == 1.0 and made2["he:KNOWS"][0].get("precision") == 0.0
                      and made2["he:KNOWS"][0].get("precision_lenient") == 1.0 and made2["he:KNOWS"][0]["labelled"] == 1))
        cases.append(("an unlabelled contract has no precision, not a precision of zero", "precision" not in made["he:ALIAS"][0]))
    cases.append(("a structural row is admitted without a cue",
                  admitted({"template": "ChapterBeats.yaml", "kind": "relation_reading",
                            "raw": {"source": "Kap 3", "target": "Kiko", "type": "introduces", "quote": "Kiko erscheint", "stance": "asserts"}})))
    text = "Eins ohne Stichwort.\n\nZwei mit Regel: das darf nie geschehen.\n\nDrei nichts.\n\nVier nichts.\n\nFünf nichts."
    kept = gate(text, "Rules")
    cases.append(("a gate keeps the cue paragraph and its neighbours only", kept.count("\n\n") == 2 and "Vier" not in kept))
    failed = [n for n, ok in cases if not ok]
    print(f"hegraph: {len(cases) - len(failed)} of {len(cases)} cases hold" + (" — FAILED: " + ", ".join(failed) if failed else ""))
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    if argv[:1] == ["selftest"]:
        return selftest()
    if argv[:1] == ["report"]:
        n = int(argv[argv.index("--unresolved") + 1]) if "--unresolved" in argv else 15
        text = report(unresolved=n)
        out = ROOT / "Plan" / "runs" / "hyperextract-templates-2026-09-30" / "yield.md"
        out.write_text(text, encoding="utf-8")
        print(text)
        return 0
    if argv[:1] == ["gate"] and len(argv) == 3:
        cmd_gate(argv[1], argv[2])
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
