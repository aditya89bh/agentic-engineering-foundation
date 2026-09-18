# Day 8: Guardrails and Human-in-the-Loop

## Objective

By the end of Day 8, students should be able to design permission boundaries, deterministic policy checks, approval gates, explicit approval state, and audit trails around consequential agent actions.

## Learning outcomes

Students will be able to:

- distinguish capability from permission;
- classify tools by action risk;
- implement ALLOW, DENY, and REQUIRE_APPROVAL outcomes;
- apply role-based and argument-level policy checks;
- represent approval as explicit agent state;
- build a basic approval queue;
- prevent approval reuse across changed actions;
- record consequential actions in an audit log.

## Suggested flow

1. Read [concepts.md](concepts.md).
2. Complete [Classify Actions](exercises/classify-actions.md).
3. Complete [Design Policy](exercises/design-policy.md).
4. Implement [starter/policy.py](starter/policy.py).
5. Implement [starter/approval_queue.py](starter/approval_queue.py).
6. Compare with the reference implementation.
7. Run the tests.
8. Build the [Governed Supplier Agent](project.md).
9. Review [failure-cases.md](failure-cases.md).

## Run the reference implementation

```bash
python day08-guardrails/solution/supplier_agent.py
python -m unittest discover day08-guardrails/tests -v
```

## Core mental model

```text
Agent proposes action
        ↓
Schema validation
        ↓
Policy check
        ↓
ALLOW / DENY / REQUIRE_APPROVAL
        ↓
Human approval if needed
        ↓
Execution
        ↓
Audit log
```

> Capability answers “can the system do this?” Permission answers “should it be allowed to?”
