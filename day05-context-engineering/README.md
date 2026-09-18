# Day 5: Context Engineering

## Objective

By the end of Day 5, students should be able to separate state from context and build a context manager that selects, prioritizes, compresses, and routes information into an agent decision.

## Learning outcomes

Students will be able to:

- distinguish state, context, and memory;
- build decision-specific context;
- filter irrelevant and stale information;
- apply simple recency and relevance rules;
- enforce a context budget;
- compress structured data deterministically;
- route only relevant tool definitions;
- track provenance and resolve conflicting facts.

## Suggested flow

1. Read [concepts.md](concepts.md).
2. Complete [Select Context](exercises/select-context.md).
3. Complete [Context Pollution](exercises/context-pollution.md).
4. Implement [starter/context_manager.py](starter/context_manager.py).
5. Run the reference implementation.
6. Run the tests.
7. Build the [Context-Aware Supplier Agent](project.md).
8. Review [failure-cases.md](failure-cases.md).

## Run the reference implementation

```bash
python day05-context-engineering/solution/supplier_agent.py
python -m unittest discover day05-context-engineering/tests -v
```

## Core mental model

```text
State + History + Tools + Retrieved Data
                ↓
         Context Manager
                ↓
        Selected Context
                ↓
              Model
```

> State is everything the system knows. Context is what the model sees right now.
