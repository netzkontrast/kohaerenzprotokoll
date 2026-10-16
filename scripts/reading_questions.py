"""Reading-question drafts, kept apart from the unresolved Q records.

Each existing wiki term has 100 additional prompts: five selected concerns explored
from eight angles, plus five selected term comparisons explored from twelve angles.
Concerns and comparison partners are editorial choices in reading-topics.json;
the phrasing and identity are deterministic. These are prompts, not findings:
answer coverage is unchecked and a comparison never asserts a relation exists.
No model calls, promotions, source changes or canon decisions.

    python3 scripts/reading_questions.py build   # refuses to replace existing banks
    python3 scripts/reading_questions.py check   # coverage, counts, references, identity
    python3 scripts/reading_questions.py show aegis
    python3 scripts/reading_questions.py selftest
"""
from __future__ import annotations
import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANKS = ROOT / 'Wiki/questions/reading'
TOPICS = ROOT / 'Plan/concept/reading-topics.json'
CATEGORIES = ['Begriff', 'Belege', 'Grenzen', 'Perspektive', 'Handlung', 'Konsequenzen', 'Darstellung', 'Autorentscheidung']
LOCAL = [
 ('Begriff', 'Was bedeutet bei {a} der Themenpunkt „{focus}“ konkret, und welche Deutung ist lediglich vorgeschlagen?'),
 ('Belege', 'Welche Lesarten auf der Seite zu {a} stützen oder begrenzen „{focus}“, und was ist noch unbelegt?'),
 ('Grenzen', 'Welcher Grenzfall würde bei {a} die Annahmen über „{focus}“ infrage stellen?'),
 ('Perspektive', 'Wer könnte innerhalb des Romans bei {a} etwas über „{focus}“ wissen, und woran wäre dieses Wissen begrenzt?'),
 ('Handlung', 'Welche konkrete Entscheidung könnte „{focus}“ bei {a} in einer Szene erfahrbar machen?'),
 ('Konsequenzen', 'Welche spätere Folge müsste eine Festlegung zu „{focus}“ bei {a} haben, damit sie nicht folgenlos bleibt?'),
 ('Darstellung', 'Wie lässt sich „{focus}“ bei {a} zeigen, ohne den Begriff durch einen erklärenden Absatz einzuführen?'),
 ('Autorentscheidung', 'Welche Alternativen sollte der Autor bei {a} für „{focus}“ vergleichen, und welche Frage ist bereits entschieden?'),
]
CROSS = [
 ('Begriff', 'Wo unterscheiden sich {a} und {b}, wenn man sie unter dem Gesichtspunkt „{focus}“ liest?'),
 ('Belege', 'Welche Quelle verbindet {a} mit {b} in Bezug auf „{focus}“ ausdrücklich, und wo wäre die Verbindung erst ein Vorschlag?'),
 ('Grenzen', 'Welche Grenzen aus der Seite zu {b} müsste eine Deutung von {a} unter „{focus}“ beachten?'),
 ('Perspektive', 'Wie könnte sich das Wissen über {a} vom Wissen über {b} unterscheiden, wenn „{focus}“ in einer Szene wichtig wird?'),
 ('Handlung', 'Welche Handlung könnte einen möglichen Zusammenhang zwischen {a} und {b} bei „{focus}“ prüfen, statt ihn nur zu behaupten?'),
 ('Konsequenzen', 'Falls {a} im Hinblick auf „{focus}“ anders festgelegt wird: Welche Aussagen über {b} müssten erneut geprüft werden?'),
 ('Darstellung', 'Welche unterschiedlichen Sinneseindrücke könnten {a} und {b} bei „{focus}“ unterscheidbar halten?'),
 ('Autorentscheidung', 'Braucht der Roman eine Verbindung von {a} und {b} bei „{focus}“, oder wäre eine ausdrücklich benannte Trennung hilfreicher?'),
 ('Grenzen', 'In welchem denkbaren Fall könnte {a} bestehen, ohne dass {b} dieselbe Funktion übernimmt, und was würde das für „{focus}“ zeigen?'),
 ('Konsequenzen', 'Welche Kosten könnte eine Verbindung von {a} und {b} in Bezug auf „{focus}“ erzeugen, und wer müsste sie tragen?'),
 ('Perspektive', 'Welche ältere Lesart von {a} oder {b} könnte die Gegenüberstellung unter „{focus}“ verfälschen?'),
 ('Darstellung', 'Welche spätere Szene könnte eine frühe Gegenüberstellung von {a} und {b} unter „{focus}“ neu lesbar machen?'),
]


def read_banks(root: Path = ROOT) -> list[dict]:
    return [json.loads(p.read_text()) for p in sorted((root / 'Wiki/questions/reading').glob('*.json'))]


def terms(root: Path) -> dict[str, dict]:
    from wiki_index import frontmatter
    return {p.stem: {'title': frontmatter(p.read_text()).get('term', p.stem), 'path': p.relative_to(root).as_posix(),
                     'hash': hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted((root / 'Wiki/candidates').glob('*.md'))}


def make(slug: str, topic: dict, pages: dict) -> dict:
    concerns, peers = topic['concerns'], topic['peers']
    if len(concerns) != 5 or len(peers) != 5 or len(set(peers)) != 5 or slug in peers:
        raise ValueError(f'{slug}: five concerns and five distinct other terms required')
    a = pages[slug]['title']
    rows = []
    for ci, focus in enumerate(concerns):
        for category, pattern in LOCAL:
            rows.append({'id': f'RQ-{slug}-{len(rows)+1:03}', 'question': pattern.format(a=a, focus=focus),
                         'category': category, 'focus': ci, 'terms': [slug]})
    for pi, peer in enumerate(peers):
        for category, pattern in CROSS:
            rows.append({'id': f'RQ-{slug}-{len(rows)+1:03}', 'question': pattern.format(a=a, b=pages[peer]['title'], focus=concerns[pi]),
                         'category': category, 'focus': pi, 'terms': [slug, peer]})
    if topic.get('opening_question'): rows[0]['question'] = topic['opening_question']
    return {'version': 1, 'term': slug, 'title': a, 'written': '2026-10-14', 'status': 'proposed', 'answer_status': 'unchecked',
            'method': 'editorial concerns and comparison partners; deterministic exploration lenses',
            'concerns': concerns, 'basis': {s: pages[s] for s in [slug] + peers}, 'questions': rows}


def validate(banks: list[dict], root: Path = ROOT) -> tuple[list[str], list[str]]:
    pages = terms(root)
    errors, notices = [], []
    slugs = [b.get('term') for b in banks]
    if set(slugs) != set(pages) or len(slugs) != len(set(slugs)):
        errors.append(f'coverage: missing {sorted(set(pages)-set(slugs))}; extra/duplicate {sorted(set(slugs)-set(pages))}')
    ids, texts = set(), set()
    for b in banks:
        slug = b.get('term'); rows = b.get('questions', [])
        if len(rows) != 100: errors.append(f'{slug}: expected 100, found {len(rows)}')
        if b.get('status') != 'proposed' or b.get('answer_status') != 'unchecked': errors.append(f'{slug}: bank must remain a proposed exploration with unchecked answers')
        if sum(len(r.get('terms', [])) > 1 for r in rows) != 60: errors.append(f'{slug}: expected 60 cross-term prompts')
        for s, basis in b.get('basis', {}).items():
            expected = pages.get(s)
            if not expected or basis.get('path') != expected['path']: errors.append(f'{slug}: broken basis {s}')
            elif basis.get('hash') != expected['hash']: notices.append(f'{slug}: reading basis {s} has changed; review the prompts')
        for no, r in enumerate(rows, 1):
            ident, q = r.get('id', ''), r.get('question', '')
            if ident != f'RQ-{slug}-{no:03}' or ident in ids: errors.append(f'{slug}: invalid or duplicate id {ident}')
            ids.add(ident)
            folded = re.sub(r'\s+', ' ', q).casefold()
            if not q.endswith('?') or len(q) < 45 or folded in texts: errors.append(f'{ident}: empty, malformed or duplicate question')
            texts.add(folded)
            related = r.get('terms', [])
            if not related or related[0] != slug or len(set(related)) != len(related) or any(s not in pages or s not in b.get('basis', {}) for s in related): errors.append(f'{ident}: invalid terms/basis')
            if r.get('category') not in CATEGORIES or not isinstance(r.get('focus'), int) or not 0 <= r['focus'] < len(b.get('concerns', [])): errors.append(f'{ident}: invalid category/focus')
    return errors, sorted(set(notices))


def selftest() -> None:
    from copy import deepcopy
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp); path = root / 'Wiki/candidates'; path.mkdir(parents=True)
        for s in 'abcdef': (path / f'{s}.md').write_text(f'---\nterm: Begriff {s}\n---\n# {s}\n')
        pages = terms(root)
        banks = [make(s, {'concerns': [f'Thema {i}' for i in range(5)], 'peers': [p for p in pages if p != s]}, pages) for s in pages]
        assert not validate(banks, root)[0]
        for mutate in [lambda b: b.pop(), lambda b: b[0]['questions'].pop(),
                       lambda b: b[0]['questions'][0].update(terms=['missing']),
                       lambda b: b[0]['basis']['a'].update(path='missing'),
                       lambda b: b[0]['questions'][0].update(question=b[1]['questions'][0]['question']),
                       lambda b: b[0].update(status='canon')]:
            broken = deepcopy(banks); mutate(broken); assert validate(broken, root)[0]
        (path / 'a.md').write_text('---\nterm: Begriff a\n---\n# changed\n')
        assert not validate(banks, root)[0] and validate(banks, root)[1]
    print('reading questions: coverage, counts, identity, reference, duplicate, status and staleness fixtures held')


def main(argv: list[str]) -> int:
    if argv == ['selftest']: selftest(); return 0
    if argv[:1] == ['build']:
        pages = terms(ROOT); topics = json.loads(TOPICS.read_text())
        if set(topics) != set(pages): raise SystemExit('topics must cover exactly the existing terms')
        banks = [make(s, topics[s], pages) for s in pages]
        errors, _ = validate(banks)
        if errors: raise SystemExit('\n'.join(errors))
        if any(BANKS.glob('*.json')): raise SystemExit('banks exist; do not overwrite editorial work — edit a bank explicitly')
        BANKS.mkdir(parents=True, exist_ok=True)
        for b in banks: (BANKS / f"{b['term']}.json").write_text(json.dumps(b, ensure_ascii=False, indent=1)+'\n')
    banks = read_banks()
    if argv[:1] == ['show'] and len(argv) == 2:
        for b in banks:
            if b['term'] == argv[1]:
                for q in b['questions']: print(q['id'], q['question'])
                return 0
        raise SystemExit('unknown term')
    errors, notices = validate(banks)
    for e in errors: print('DEFECT', e)
    for e in notices: print('STALE', e)
    print(f"reading questions: {len(banks)} terms, {sum(len(b['questions']) for b in banks)} prompts, {len(errors)} defects, {len(notices)} changed bases")
    return bool(errors)

if __name__ == '__main__': sys.exit(main(sys.argv[1:] or ['check']))
