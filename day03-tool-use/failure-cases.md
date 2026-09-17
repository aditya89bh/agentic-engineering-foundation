# Day 3 Failure Cases

Use these cases to separate model-selection failures from tool-boundary failures.

## Unknown tool

The model proposes a capability that is not in the registry.

**Defense:** reject before execution.

## Missing argument

A valid tool is selected but a required argument is absent.

**Defense:** validate required fields before dispatch.

## Incorrect argument type

Example: `max_unit_price="cheap"`.

**Defense:** schema or deterministic type validation.

## Invalid supplier ID

The call shape is valid, but the requested supplier does not exist.

**Defense:** return or raise a clear execution error. Do not pretend the lookup succeeded.

## Empty result

`SEARCH_SUPPLIERS` executes correctly but returns no matches.

**Defense:** treat empty as a valid observation, not an exception.

## Tool exception

The underlying function raises an error.

**Defense:** preserve the error category and log the attempted call.

## Repeated tool call

The agent keeps requesting the same inspection without learning from the result.

**Defense:** store tool history and detect unnecessary repetition.

## Permission violation

A tool is valid but outside the capability set allowed for the current agent.

**Defense:** check permissions before dispatch.

## Malformed model tool request

The model returns prose, malformed JSON, or an unexpected structure.

**Defense:** parse and validate before execution.

## Result contract changes

A tool that previously returned `unit_price` stops returning it.

**Defense:** validate observations and fail explicitly at the boundary.

## Debugging questions

For each failure, identify:

1. Did the decision component choose badly?
2. Was the tool call invalid?
3. Did the tool itself fail?
4. Was the observation malformed?
5. What deterministic check should contain the failure?
