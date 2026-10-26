"""Strict, standard-library validation of the TS character contract.

JSON is the persisted session input. Validation does not grant canon authority.
"""
from __future__ import annotations

import json
from pathlib import Path

FIELDS = {
    'figures': {'id', 'name', 'origin'}, 'traits': {'id', 'label'},
    'instances': {'id', 'figure_id', 'session_id', 'trait_ids'},
    'event_roles': {'id', 'label'}, 'relationship_roles': {'id', 'label'},
    'events': {'id', 'session_id', 'position', 'roles'},
    'relationships': {'id', 'session_id', 'participants'},
    'transitions': {'id', 'instance_id', 'event_id', 'before', 'after'},
    'chapters': {'id', 'session_id', 'event_ids'},
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def string(value):
    return isinstance(value, str) and bool(value.strip())


def validate(data: dict) -> dict:
    require(isinstance(data, dict), 'document must be an object')
    require(set(data) == {'version', *FIELDS}, 'unknown or missing document fields')
    require(type(data['version']) is int and data['version'] == 1, 'unsupported version')
    tables = {}
    all_ids = set()
    for kind, fields in FIELDS.items():
        require(isinstance(data[kind], list), f'{kind}: expected array')
        tables[kind] = {}
        for row in data[kind]:
            require(isinstance(row, dict), f'{kind}: expected object')
            extra = {'promotion'} if kind == 'chapters' else set()
            require(fields <= set(row) <= fields | extra, f'{kind}: unknown or missing fields')
            for key in fields - {'trait_ids', 'event_ids', 'roles', 'participants', 'position'}:
                require(string(row[key]), f'{kind}.{key}: expected nonempty string')
            require(row['id'] not in all_ids, 'duplicate id')
            all_ids.add(row['id'])
            tables[kind][row['id']] = row
    def ref(kind, key):
        require(string(key) and key in tables[kind], f'unknown {kind} reference: {key}')
        return tables[kind][key]
    def refs(kind, values):
        require(isinstance(values, list), f'{kind}: expected reference array')
        require(all(string(v) for v in values), f'{kind}: invalid reference')
        require(len(values) == len(set(values)), f'{kind}: duplicate reference')
        return [ref(kind, value) for value in values]
    for row in data['figures']:
        require(row['origin'] in {'originalCharacter', 'fanfictionCharacter'}, 'invalid origin')
    for row in data['instances']:
        ref('figures', row['figure_id'])
        refs('traits', row['trait_ids'])
    positions = set()
    for event in data['events']:
        require(type(event['position']) is int and event['position'] >= 0, 'invalid event position')
        key = (event['session_id'], event['position'])
        require(key not in positions, 'duplicate session event position')
        positions.add(key)
    for kind, field, vocab in [('events', 'roles', 'event_roles'),
                                ('relationships', 'participants', 'relationship_roles')]:
        for row in data[kind]:
            require(isinstance(row[field], list), f'{field}: expected array')
            seen = set()
            for part in row[field]:
                require(isinstance(part, dict) and set(part) == {'instance_id', 'role_id'}, 'invalid participant')
                instance = ref('instances', part['instance_id'])
                ref(vocab, part['role_id'])
                require(instance['session_id'] == row['session_id'], 'cross-session participant')
                pair = (part['instance_id'], part['role_id'])
                require(pair not in seen, 'duplicate participant role')
                seen.add(pair)
            if kind == 'relationships':
                require(len({p['instance_id'] for p in row[field]}) >= 2, 'relationship needs two figures')
    chains = {}
    for row in data['transitions']:
        instance = ref('instances', row['instance_id'])
        event = ref('events', row['event_id'])
        require(instance['session_id'] == event['session_id'], 'cross-session transition')
        require(any(p['instance_id'] == instance['id'] for p in event['roles']), 'transition figure absent from event')
        require(row['before'] != row['after'], 'transition must change state')
        chains.setdefault(instance['id'], []).append((event['position'], row))
    for chain in chains.values():
        chain.sort(key=lambda item: item[0])
        require(len({p for p, _ in chain}) == len(chain), 'ambiguous simultaneous transitions')
        for (_, previous), (_, current) in zip(chain, chain[1:]):
            require(previous['after'] == current['before'], 'broken state chain')
    for chapter in data['chapters']:
        events = refs('events', chapter['event_ids'])
        require(bool(events), 'chapter needs events')
        require(all(e['session_id'] == chapter['session_id'] for e in events), 'cross-session chapter')
        if 'promotion' in chapter:
            promotion = chapter['promotion']
            require(isinstance(promotion, dict) and set(promotion) == {'decision_path'}
                    and string(promotion['decision_path']), 'invalid promotion reference')
    return data


def load(path: str | Path) -> dict:
    return validate(json.loads(Path(path).read_text(encoding='utf-8')))


def chapter_events(data: dict, chapter_id: str, *, canon=False, root: Path | None = None) -> list[dict]:
    """Syuzhet order; promotion requires a real decision file supplied by the caller.

    The file's editorial authority still requires human review, not a string flag.
    """
    validate(data)
    chapter = next(c for c in data['chapters'] if c['id'] == chapter_id)
    if canon:
        require(root is not None and 'promotion' in chapter, 'chapter is a session proposal')
        base = root.resolve()
        path = (base / chapter['promotion']['decision_path']).resolve()
        require(path.is_relative_to(base / 'Plan' / 'decisions') and path.suffix == '.md'
                and path.is_file(), 'promotion decision must exist under Plan/decisions')
    events = {e['id']: e for e in data['events']}
    return [events[eid] for eid in chapter['event_ids']]
