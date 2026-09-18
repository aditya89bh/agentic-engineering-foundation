# Day 8 Failure Cases

## Unauthorized role attempts a write action
**Risk:** capability is mistaken for permission.

## Agent bypasses approval
**Risk:** consequential action executes without human review.

## Approval references wrong action ID
**Risk:** unrelated authority is applied to a different action.

## Approval reused for different arguments
**Risk:** a previously approved action is silently changed.

## Order value changes after approval
**Risk:** approval no longer matches the actual impact.

## Rejected action is retried unchanged
**Risk:** human decision is ignored.

## Missing approver identity
**Risk:** the system cannot establish who authorized the action.

## Approval timeout ignored
**Risk:** the agent waits indefinitely or executes without a valid decision.

## Audit log missing
**Risk:** consequential actions become impossible to reconstruct.

## Write executes before policy check
**Risk:** governance happens after the damage.

## Forbidden tool proposed by model
**Risk:** the runtime exposes capabilities outside the policy surface.

## Debugging question

> Did the system control the action before it happened?
