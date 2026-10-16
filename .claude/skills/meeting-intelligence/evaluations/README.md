# Meeting Intelligence - Evaluation Scenarios

<!-- readme-context:start -->
Vendored upstream documentation. The scenarios below describe upstream behavior,
not authorization to transfer this project’s corpus or a claim of local test success.
Project integration follows CLAUDE.md; upstream examples retain their original scope.

[Project](../../../../README.md) · [Current work](../../../../NOW.md) · [Integration rules](../../../../CLAUDE.md)
<!-- readme-context:end -->

Test scenarios for validating meeting preparation and agenda creation.

## Running Evaluations

1. Provide meeting context (topic, attendees, date)
2. Request meeting preparation
3. Verify output includes:
   - Comprehensive agenda with timing
   - Relevant background context
   - Prepared materials
   - Discussion talking points

## Evaluation Criteria

**Agenda Quality**
- Clear objectives for each item
- Realistic timing allocations
- Logical flow and progression
- All necessary topics covered

**Context Gathering**
- Relevant background retrieved
- Stakeholder information included
- Previous decisions/discussions referenced
- Potential issues surfaced

**Practicality**
- Agenda ready to use immediately
- Materials referenced are accessible
- Talking points are specific
- Decision points clearly identified

## Test Scenarios Included

- Executive status meeting
- Cross-functional planning session
- 1-on-1 conversation prep
- Client meeting preparation
- Sprint planning meeting
