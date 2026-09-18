# Day 10: Capstone Engineering Project

## Capstone

**Supplier Intelligence Agent**

Day 10 integrates the complete foundation course into one engineered system. It introduces almost no new theory. The focus is integration, debugging, evaluation, and presentation.

## Objective

Build a supplier intelligence agent that can:

- parse a natural-language procurement request;
- validate structured requirements;
- search, inspect, and compare suppliers;
- use explicit state transitions;
- assemble decision-specific context;
- retrieve and write persistent memory;
- recover from failures;
- enforce policy and approval requirements;
- produce audit evidence;
- run against a repeatable evaluation suite.

## Minimum acceptance criteria

The capstone is complete only if it includes:

- schema-validated input;
- 3+ tools;
- explicit state machine;
- max-step stopping;
- context routing;
- persistent memory;
- retry/fallback logic;
- policy protection for consequential actions;
- scoped approval;
- audit logging;
- 20+ evaluation cases;
- failure categorization;
- automated tests;
- documented limitations.

## Suggested Day 10 flow

1. Review [architecture.md](architecture.md).
2. Assemble the read-only supplier workflow.
3. Add memory and reliability.
4. Add policy and approval.
5. Run the evaluation suite.
6. Inspect at least three failures.
7. Complete [failure-analysis.md](failure-analysis.md).
8. Run the final demo from [demo.md](demo.md).

## Run

```bash
python day10-capstone/agent/supplier_agent.py
python -m unittest discover day10-capstone/tests -v
```
