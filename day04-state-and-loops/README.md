# Day 4: State Machines and Agent Loops

## Objective

By the end of Day 4, students should be able to model an agent as an explicit state machine, define legal transitions, handle branches and retries, stop in terminal states, and save or resume execution from a checkpoint.

## Learning outcomes

Students will be able to:

- distinguish full agent state from current workflow status;
- model states, transitions, guards, loops, retries, and terminal states;
- validate transitions before applying them;
- define state invariants;
- represent failure and human-intervention states explicitly;
- serialize and restore checkpoints;
- test control flow independently from model behavior.

## Mental model

```text
state -> decision -> action -> observation -> transition -> new state
```

An agent loop is a sequence of state transitions. The model may propose what should happen next, but the runtime decides whether that transition is legal.

## Suggested session plan

1. Read [concepts.md](concepts.md).
2. Complete [Draw the State Machine](exercises/draw-state-machine.md).
3. Complete [Invalid Transitions](exercises/invalid-transitions.md).
4. Implement the TODOs in `starter/`.
5. Compare with the reference implementation in `solution/`.
6. Run transition and controller tests.
7. Explore [failure-cases.md](failure-cases.md).
8. Build the [Stateful Supplier Analysis Agent](project.md).

## Run

From the repository root:

```bash
python day04-state-and-loops/solution/supplier_agent.py
python -m unittest discover day04-state-and-loops/tests -v
```

## Bridge from Day 3

Day 3 gave the system safe tools. Day 4 makes multi-step execution explicit and controllable.

```text
requirements -> tools -> state machine -> bounded execution
```
