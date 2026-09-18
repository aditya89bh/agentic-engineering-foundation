# Mini-Project: Governed Supplier Agent

Extend the supplier agent with a consequential tool:

```text
CREATE_PURCHASE_ORDER
```

## Expected flow

```text
Agent proposes PO
      ↓
Schema validation
      ↓
Policy engine
      ↓
ALLOW / DENY / REQUIRE_APPROVAL
      ↓
Human approval if required
      ↓
Execute
      ↓
Audit log
```

## Required engineering properties

- permission classes;
- deterministic policy engine;
- ALLOW / DENY / REQUIRE_APPROVAL outcomes;
- role-based access;
- argument-level constraints;
- approval queue;
- explicit waiting-for-approval state;
- approve/reject transitions;
- approval scope bound to exact action arguments;
- timeout policy;
- audit log;
- at least 10 tests.

## Acceptance checks

1. researchers cannot create purchase orders;
2. uninspected suppliers cannot receive purchase orders;
3. small orders can be allowed directly;
4. medium orders require procurement approval;
5. high-value orders require finance approval;
6. wrong-role approvers are rejected;
7. changed action arguments invalidate old approval;
8. rejected or resolved approvals cannot be reused;
9. write actions execute only after policy and approval checks;
10. audit logs record policy, approval, and execution events.

## Reflection

Explain why broad approval such as “let the agent handle procurement” is weaker than approving one specific action. Give one example where a policy should DENY rather than REQUIRE_APPROVAL.
