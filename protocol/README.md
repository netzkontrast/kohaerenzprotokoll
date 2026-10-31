# Character protocol — offline pilot v1

This is an isolated contract, not the research graph or manuscript canon. No
existing `protocol/` schema existed on main when this pilot was added.
TypeScript consumers use `characters.ts`; Python consumers load persisted JSON
with `characters.load`. Neither path calls a provider or endpoint.

## Adopted mapping

| Author-supplied ontology reference | Local representation |
|---|---|
| G0 / G1 / G17 (golem.ttl lines 1321 / 1541 / 1524) | figure / session-bound figure instance / trait |
| originalCharacter / fanfictionCharacter (Character_RDF_final_updated.ttl 1484–1488) | figure.origin |
| G11 | global event_roles vocabulary; event participation |
| G6 | separate global relationship_roles vocabulary |
| G4 | identified relationship node with participants and their roles |
| G3_Psychological_State (golem.ttl 1596) | event-bound before/after transition on a fictional instance |
| G5/G7 versus G8/G9 | chronological session events versus ordered chapter event references |

References above are from the author's brief, **not independently verified**.
The paper, TTL files and CQ-SPARQL.xlsx are not present in this checkout or the
attached novel PDFs. No external ontology code or AO3 case data is copied.
The author's license observation is CC BY 4.0 only for golem.ttl line 22; it
must not be extended to the paper, spreadsheet or case data. Before copying any
source material, obtain its exact version, attribution and applicable license.
The reported 44 G4 case instances and unused G3 state class are research notes,
not measured properties of this fixture.

## Persistence and authority

The JSON fixture demonstrates two sessions sharing a figure but not its traits
or inner state. Persist session JSON explicitly through the caller's storage;
this pilot has no database, write API or automatic persistence. This makes M1
conditional on a future consumer actually storing the session instances; M2 is
represented by event-bound transitions. R/F and TS/Python remain separate from
any model or player profile.

Relationships point only to figure instances; unknown fields and broken,
cross-session or wrong-vocabulary references are rejected. Psychological state
is fictional scenario data. No player inference, state attachment or player
identifier belongs to this contract. Free-text labels are not a privacy filter;
callers remain responsible for admitting fictional data only.

`chapter_events` returns the chapter's presentation order without rewriting the
session's chronology. By default that output is a proposal. Its `canon=True`
preflight requires a decision path that exists under `Plan/decisions/`; it checks
file existence and scope only, **not the author's approval or its semantic
scope**. Editorial review must establish that the cited decision approves this
exact chapter and its variants before any consumer writes canon. There is no
promotion command and no manuscript writer. A session cannot promote itself by
setting a status string. The synthetic fixture is never novel canon.

## Verification

Run from repository root:

```bash
python3 -m unittest discover -s protocol -p 'test_*.py' -v
```

Ten numbered tests are **local acceptance questions derived from the brief**,
not the ten original spreadsheet CQs. They cover identity/instances, reverse
identity, traits, origins, event roles, relationship nodes, relationship roles,
state transitions, fabula/syuzhet and proposal authority. Two additional tests
exercise malformed references, cross-session leaks, extra player fields,
duplicate identities/positions and promotion path checks.

**Missing:** source-to-test mapping for all ten CQ-SPARQL.xlsx rows. Once the
workbook is available, record each row's question, synthetic expected result
and local test identifier; mark unsupported rows explicitly. Do not execute
SPARQL, install RDF/OWL, query endpoints or import the AO3 corpus.

This pilot is tested in CI but has no UI, public API, deployment, live-model
adapter or automatic graph integration. Python validation is the runtime gate;
TS declarations alone do not validate untrusted JSON.

## Event-time reconstruction

`characters.state_at(data, instance_id, event_id)` reconstructs the state after
that event in fabula order, even if chapter order is reversed. Before the first
transition it returns the explicitly recorded `before`; without transitions it
returns `None` (unknown). Cross-session queries and broken or simultaneous state
chains are refused. This reads fictional session data only and never infers a
player state. Additional regression cases cover these boundaries and missing
chapter IDs.
