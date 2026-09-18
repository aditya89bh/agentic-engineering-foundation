# Day 5 Failure Cases

Use these to debug context assembly rather than blaming the model first.

## Entire history passed every time
**Risk:** cost, distraction, stale facts, duplicated evidence.

## Stale supplier price selected
**Risk:** outdated context drives a wrong recommendation.

## Latest constraint omitted
**Risk:** current user intent is replaced by an older requirement.

## Duplicate tool results
**Risk:** repeated evidence appears more important than it is.

## Context exceeds budget
**Risk:** truncation becomes uncontrolled or important fields are lost.

## Irrelevant data dominates
**Risk:** the model attends to information that cannot change the next action.

## Summary drops a hard constraint
**Risk:** semantic compression removes a non-negotiable requirement.

## Wrong tools included
**Risk:** the model is offered capabilities that are irrelevant or unsafe in the current state.

## Conflicting requirements
**Risk:** two incompatible facts enter the same decision without an explicit precedence policy.

## Missing provenance
**Risk:** the system cannot explain where a fact came from or whether it is current.

## Debugging question

For every bad decision, ask:

> Did the model reason poorly, or did the context manager give it poor information?
