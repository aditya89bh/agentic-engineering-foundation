# Day 7: Reliability and Failure Engineering

## Objective

By the end of Day 7, students should be able to classify failures, distinguish transient from permanent errors, implement bounded retries and backoff, use fallbacks and circuit breakers, and produce structured failure evidence.

## Learning outcomes

Students will be able to:

- classify model, tool, state, memory, context, infrastructure, and policy failures;
- distinguish retryable from non-retryable errors;
- implement bounded retries and backoff;
- enforce timeouts around external work;
- use fallbacks when retrying the same approach is no longer useful;
- explain why retries require idempotency;
- implement a basic circuit breaker;
- represent partial success explicitly;
- log failures in a structured form.

## Suggested flow

1. Read [concepts.md](concepts.md).
2. Complete [Classify Failures](exercises/classify-failures.md).
3. Complete [Recovery Policy](exercises/recovery-policy.md).
4. Implement [starter/reliable_executor.py](starter/reliable_executor.py).
5. Compare with the reference implementation.
6. Run the tests.
7. Build the [Fault-Tolerant Supplier Agent](project.md).
8. Review [failure-cases.md](failure-cases.md).

## Run the reference implementation

```bash
python day07-reliability/solution/supplier_agent.py
python -m unittest discover day07-reliability/tests -v
```

## Core mental model

```text
Failure
  ↓
Classify
  ↓
Retryable?
├── Yes → bounded retry → fallback if needed
└── No  → fail safely / human review
```

> Reliability is not trying forever. Reliability is failing predictably and recovering within explicit limits.
