# Exercise 1: Draw the State Machine

Design the control flow for a supplier research agent using these states:

- START
- SEARCHING
- INSPECTING
- COMPARING
- COMPLETED
- FAILED
- NEEDS_HUMAN

For each state, define:

1. what it means;
2. which transitions are allowed;
3. what condition triggers each transition;
4. whether the state is terminal;
5. whether retries are allowed.

Then draw the transition diagram and trace one successful path and one failure path.

## Review questions

- Which transitions should never be legal?
- Where can the agent loop?
- How do you prove the loop is making progress?
- Which transition should require human intervention?
