# Failure Cases

Use these cases to debug the control layer rather than blaming the model automatically.

## Invalid transition
A state attempts to jump to a status not permitted by the transition table.

## Infinite inspection loop
The controller repeatedly remains in `INSPECTING` without reducing remaining work.

## Retry limit exceeded
A recoverable failure keeps retrying after the configured budget is exhausted.

## Missing required state
A restored or mutated state lacks data required for the next transition.

## Corrupt checkpoint
Saved state cannot be parsed or violates invariants when restored.

## Completed without recommendation
The controller reaches `COMPLETED` even though no recommendation exists.

## Terminal state executes another action
`FAILED`, `COMPLETED`, or `NEEDS_HUMAN` should not continue normal execution.

## Retry counter not reset
Retries from one tool or phase leak into another phase and cause premature failure.

## Inconsistent transition condition
The evidence says one branch should be taken but the controller selects another.

## Resume from terminal state
A checkpoint already in a terminal state is mistakenly re-entered into the execution loop.

## Debugging checklist

For each failure, record:

1. current state;
2. attempted transition;
3. transition guard or evidence;
4. invariant that should have caught it;
5. expected terminal or next state.

Key question: **Is the failure caused by the model, tool, or state machine?**
