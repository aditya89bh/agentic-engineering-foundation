# Mini-Project: Fault-Tolerant Supplier Agent

Extend the supplier system so dependencies can fail intentionally and the runtime handles those failures predictably.

## Injected failures

Examples:

- temporary supplier API timeout;
- malformed tool result;
- unavailable cache;
- invalid supplier ID;
- repeated service failures.

## Required final statuses

- COMPLETED
- PARTIAL_SUCCESS
- FAILED
- NEEDS_HUMAN

## Required engineering properties

- failure taxonomy;
- structured errors;
- retryability classification;
- bounded retry limit;
- backoff;
- timeout policy;
- fallback mechanism;
- circuit breaker basics;
- idempotency awareness;
- failure budgets;
- partial-success state;
- structured failure logging;
- at least 10 tests.

## Acceptance checks

1. transient failures retry within a fixed budget;
2. permanent failures do not retry;
3. retry exhaustion can activate a fallback;
4. fallback failure returns NEEDS_HUMAN;
5. failure logs record component, type, attempt, and retryability;
6. circuit breaker opens after repeated failures;
7. circuit breaker can move to HALF_OPEN;
8. successful probe closes the circuit;
9. partial success is distinguishable from full success;
10. side-effecting retries require an idempotency strategy.

## Reflection

Explain why a system with more retries can be less reliable. Give one example where stopping immediately is safer than retrying.
