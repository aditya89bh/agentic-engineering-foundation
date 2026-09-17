# Mini-Project: Stateful Supplier Analysis Agent

Extend the earlier supplier system into an explicit finite-state machine.

## Target flow

```text
START
  ↓
SEARCHING
  ↓
INSPECTING
  ↓
COMPARING
  ↓
COMPLETED
```

Alternative paths should include:

```text
SEARCHING -> FAILED
INSPECTING -> INSPECTING
INSPECTING -> FAILED
COMPARING -> NEEDS_HUMAN
```

## Required engineering properties

- explicit `status` field;
- finite set of states;
- transition table;
- transition validation;
- retry counter;
- terminal states and stop reasons;
- state invariants;
- step budget;
- checkpoint save/load;
- at least 10 transition or controller tests.

## Acceptance checks

- `START -> SEARCHING` succeeds;
- illegal jumps are rejected;
- no candidates ends in `FAILED`;
- all candidates are inspected before comparison;
- `COMPLETED` always has a recommendation;
- terminal states do not continue normal execution;
- saved state can be loaded and validated;
- execution cannot exceed the step budget.

## Reflection

Explain which decisions could later be model-driven and which transitions must remain deterministic. Identify one state where human intervention is safer than autonomous continuation.
