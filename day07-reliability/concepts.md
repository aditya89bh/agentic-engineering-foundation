# Day 7 Concepts

## 1. Failure taxonomy

Useful categories:

- model failure;
- tool failure;
- state failure;
- memory failure;
- context failure;
- infrastructure failure;
- policy failure.

Reliability starts by identifying what actually failed.

## 2. Transient vs permanent failures

Transient failures may succeed later:

- rate limits;
- network timeouts;
- temporary service outages;
- database locks.

Permanent failures usually will not improve through repetition:

- invalid IDs;
- unsupported tools;
- malformed schemas;
- permission denial;
- business-rule violations.

## 3. Retry policy

A retry policy defines:

- retryable error types;
- maximum attempts;
- delay;
- backoff strategy;
- terminal behavior.

Retries must be bounded.

## 4. Backoff

A simple exponential policy:

```text
attempt 1 → 1 unit
attempt 2 → 2 units
attempt 3 → 4 units
```

Backoff reduces pressure on an already failing dependency.

## 5. Timeouts

External calls need time bounds. A call without a timeout can become an infinite wait.

## 6. Fallbacks

Retry repeats the same approach.

Fallback changes the approach.

Examples:

- live API → cached data;
- semantic search → keyword search;
- primary model → secondary model;
- unavailable live price → human review.

## 7. Circuit breaker

Three states:

```text
CLOSED    → normal execution
OPEN      → calls blocked after repeated failures
HALF_OPEN → one probe is allowed to test recovery
```

A circuit breaker protects the rest of the system from repeatedly calling a failing dependency.

## 8. Idempotency

Retries are safe only when repeating an action is safe.

A repeated read is usually safe. A repeated purchase-order creation may not be.

Use stable request IDs or deduplication for side-effecting actions.

## 9. Failure budgets

Useful limits include:

- max model retries;
- max tool retries;
- max total steps;
- max consecutive failures;
- max cost.

Local recovery must still obey global limits.

## 10. Structured errors

Prefer machine-readable errors:

```json
{
  "type": "TOOL_TIMEOUT",
  "component": "SEARCH_SUPPLIERS",
  "retryable": true,
  "attempt": 2,
  "message": "supplier API timed out"
}
```

## 11. Failure logs

Useful fields:

- timestamp;
- component;
- error type;
- attempt;
- retryable;
- fallback used;
- final outcome.

## 12. Recovery policy

Example:

```text
TOOL_TIMEOUT
→ retry up to 3 attempts
→ fallback to cache
→ NEEDS_HUMAN if cache unavailable
```

Compare:

```text
INVALID_ARGUMENT
→ no retry
→ validation failure
```

## 13. Partial success

A task can produce useful work without fully succeeding.

Example:

```text
10 suppliers requested
7 inspected successfully
3 unavailable
→ PARTIAL_SUCCESS
```

## 14. Graceful degradation

A system should be explicit when it is operating with weaker evidence or reduced capabilities.

## 15. Reliability is system design

A reliable agent combines:

```text
validation
+ bounded retries
+ timeouts
+ fallbacks
+ safe transitions
+ structured errors
+ logs
+ tests
```

A better prompt alone does not provide these guarantees.
