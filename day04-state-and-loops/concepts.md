# Day 4 Concepts

## 1. Why state machines matter

Once an agent can understand requirements and call tools, the main engineering problem becomes control. Without explicit control flow, multi-step behavior is difficult to inspect, reproduce, and constrain.

```text
State
  ↓
Decision
  ↓
Action
  ↓
Observation
  ↓
Transition
  ↓
New State
```

**An agent loop is a sequence of state transitions.**

## 2. State vs status

State contains everything needed to continue execution:

```python
state = {
    "goal": "Find a supplier",
    "status": "SEARCHING",
    "step": 2,
    "retry_count": 0,
    "candidates": ["SUP-001"],
    "inspected": [],
}
```

Status describes the current workflow position. Example statuses:

`START`, `SEARCHING`, `INSPECTING`, `COMPARING`, `COMPLETED`, `FAILED`, `NEEDS_HUMAN`.

## 3. Finite-state machines

A finite-state machine defines a finite set of states and legal transitions.

```text
START -> SEARCHING -> INSPECTING -> COMPARING -> COMPLETED
                    \-> FAILED
```

Each transition should have a reason or guard condition.

## 4. Valid transitions

```python
VALID_TRANSITIONS = {
    "START": {"SEARCHING"},
    "SEARCHING": {"INSPECTING", "FAILED"},
    "INSPECTING": {"INSPECTING", "COMPARING", "FAILED"},
    "COMPARING": {"COMPLETED", "NEEDS_HUMAN", "FAILED"},
    "COMPLETED": set(),
    "FAILED": set(),
    "NEEDS_HUMAN": set(),
}
```

The decision component may propose a next state. The controller validates whether that transition is legal.

## 5. Branching

```text
SEARCHING
  ├─ results found -> INSPECTING
  └─ no results    -> FAILED
```

Branches should follow explicit evidence rather than hidden prompt behavior.

## 6. Loops and measurable progress

Some states repeat. Repetition is safe only when progress is measurable.

Useful progress signals:

- uninspected candidates decreases;
- evidence count increases;
- retry count increases;
- remaining step budget decreases.

A loop with no progress measure is a likely infinite loop.

## 7. Terminal states

Prefer explicit terminal states over only `done = True`.

```text
COMPLETED
FAILED
CANCELLED
NEEDS_HUMAN
```

Always preserve a terminal reason:

```python
state.stop_reason = "No eligible suppliers"
```

## 8. Retry states and retry budgets

Retries should be represented in state.

```text
TOOL_CALL
  ↓
Success?
  ├─ yes -> NEXT_STATE
  └─ no  -> RETRY
              ↓
       retries remaining?
          ├─ yes -> TOOL_CALL
          └─ no  -> FAILED
```

A retry is a controlled transition, not an unbounded `except: try again` loop.

## 9. Checkpoints

A checkpoint is a serializable snapshot of execution state.

```json
{
  "status": "INSPECTING",
  "step": 4,
  "retry_count": 0,
  "candidates": ["SUP-001", "SUP-002"],
  "inspected": ["SUP-001"]
}
```

Checkpoints enable debugging, crash recovery, human intervention, and later durable execution.

## 10. Resume execution

```python
save_state(state, "checkpoint.json")
state = load_state("checkpoint.json")
run_agent(state)
```

A restored checkpoint must be validated before execution resumes.

## 11. State invariants

Invariants are conditions that must always be true.

Examples:

- `step <= MAX_STEPS`
- `retry_count <= MAX_RETRIES`
- inspected suppliers must be a subset of candidates
- `COMPLETED` requires a recommendation
- terminal states cannot execute another tool

These checks make agent failures easier to locate.

## Design principle

> The model can influence decisions, but the runtime owns legal transitions, budgets, invariants, and terminal conditions.
