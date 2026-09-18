# Exercise 2: Design a Recovery Policy

Design a policy for each error:

- TOOL_TIMEOUT
- RATE_LIMIT
- INVALID_ARGUMENT
- SERVICE_UNAVAILABLE
- PERMISSION_DENIED
- MALFORMED_MODEL_OUTPUT

For each define:

- retry?;
- maximum attempts;
- backoff?;
- fallback?;
- terminal outcome.

Then answer:

1. Which errors must never be retried?
2. Which retries require idempotency protection?
3. When should the system return NEEDS_HUMAN rather than FAILED?
