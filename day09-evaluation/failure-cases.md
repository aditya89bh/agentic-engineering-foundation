# Day 9 Failure Cases

## Correct final answer, wasteful trajectory
**Risk:** outcome-only evaluation hides poor execution.

## Wrong final answer despite correct tools
**Risk:** subsystem metrics pass while final reasoning fails.

## Constraint violated
**Risk:** fluent output masks a hard requirement failure.

## Stale memory changes the decision
**Risk:** retrieval quality is not evaluated.

## Fallback used unnecessarily
**Risk:** system appears robust but wastes time or lowers evidence quality.

## Excessive retries
**Risk:** task eventually succeeds but violates reliability budgets.

## Approval bypassed
**Risk:** outcome succeeds while governance fails.

## Context missing critical requirement
**Risk:** model failure is blamed for an upstream context defect.

## Correct tool with wrong arguments
**Risk:** tool-selection accuracy alone gives a false sense of quality.

## Evaluation grader is wrong
**Risk:** the measurement system becomes the source of error.

## Debugging question

> What exactly failed, and which subsystem should be changed?
