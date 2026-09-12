# Failure Cases

Agentic systems fail through control flow as well as incorrect answers. Use these cases to inspect the state and trace, not merely the final message.

## Agent never stops

**Symptom:** the loop continues after a recommendation is available.  
**Likely cause:** no terminal state or stopping check.  
**Defense:** explicit `done`, success/failure reasons, and a hard `MAX_STEPS` guard.

## Same action repeatedly selected

**Symptom:** the agent inspects the same supplier every step.  
**Likely cause:** action history or inspected IDs are missing from state.  
**Defense:** record completed actions and select only uninspected candidates; optionally detect repeated identical actions.

## No suppliers found

**Symptom:** the agent tries to inspect an empty candidate list.  
**Likely cause:** the empty observation was not modeled as a valid result.  
**Defense:** transition directly from `SEARCH` to `FINISH` with a clear no-match reason.

## Invalid action returned

**Symptom:** the controller receives `EMAIL`, a misspelled action, or malformed arguments.  
**Likely cause:** decision output was trusted without validation.  
**Defense:** compare against an allowlist and validate required arguments before any tool executes.

## Maximum step count reached

**Symptom:** execution uses the full budget without reaching a terminal decision.  
**Likely cause:** poor policy, repeated recoverable errors, or insufficient evidence.  
**Defense:** stop safely, report incomplete status, preserve the trace, and never label the run successful.

## Incomplete state

**Symptom:** the policy expects `candidates` or `goal`, but the field is absent or inconsistent.  
**Likely cause:** ad hoc state mutation or an unvalidated restore.  
**Defense:** initialize state in one function, validate invariants, and update it through defined transitions.

## Unavailable action

**Symptom:** an action is valid in theory but its tool or external service is currently unavailable.  
**Likely cause:** outage, missing permission, rate limit, or environment mismatch.  
**Defense:** distinguish unavailable from invalid; retry only safe transient failures, choose a permitted fallback, or stop and request human help.

## Debugging prompt

For each case, record:

1. the state before the failure;
2. the selected action and arguments;
3. the observation or error;
4. the expected transition;
5. the deterministic check that would prevent recurrence.
