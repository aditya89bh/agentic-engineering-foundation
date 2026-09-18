# Day 8 Concepts

## 1. Capability vs permission

An agent may technically be able to call a tool while still being prohibited from using it.

Guardrails are the deterministic control layer between proposed action and execution.

## 2. Read vs write actions

Read-only examples:

- search suppliers;
- inspect supplier;
- retrieve certification;
- calculate landed cost.

Consequential examples:

- email supplier;
- update records;
- create purchase order;
- approve payment;
- delete data.

Consequential actions need stronger controls.

## 3. Permission levels

A simple classification:

```text
READ
COMPUTE
WRITE
HIGH_RISK
```

## 4. Policy engine

Hard rules should live in code rather than prompts.

Examples:

- only procurement managers can create purchase orders;
- high-value purchases require approval;
- a supplier must be inspected before PO creation;
- deleted suppliers cannot be contacted.

## 5. Three policy outcomes

Use:

```text
ALLOW
DENY
REQUIRE_APPROVAL
```

This is more expressive than a boolean permission check.

## 6. Human approval gates

Approval is a controlled state transition, not merely a user interface step.

```text
WAITING_FOR_APPROVAL
   ├── approved → EXECUTE
   ├── rejected → REPLAN
   └── timeout → CANCELLED
```

## 7. Approval context

Approval requests should contain:

- exact proposed action;
- exact arguments;
- expected impact;
- supporting evidence;
- reason;
- alternatives when relevant.

Avoid vague “approve this agent” permissions.

## 8. Approval scope

Approval should bind to a specific action and its arguments.

If quantity, price, supplier, or tool changes, previous approval should no longer apply.

## 9. Role-based access control

Example roles:

```text
researcher
procurement_manager
finance_approver
admin
```

Roles determine which action classes a person can authorize.

## 10. Argument-level constraints

Tool permission alone is not enough.

For example, CREATE_PURCHASE_ORDER may be:

- allowed below a threshold;
- approval-required above a threshold;
- denied when the supplier was not inspected.

## 11. Correct order

```text
model proposes action
→ validate schema
→ evaluate policy
→ obtain approval if needed
→ execute
```

Never execute first and check policy afterward.

## 12. Rejection handling

Human rejection should not cause the agent to silently repeat the same request.

Valid next steps include:

- replan;
- choose another supplier;
- reduce scope;
- ask for clarification;
- stop.

## 13. Approval timeout

Pending approvals need a bounded lifecycle. A request that never receives a response should transition to a safe terminal state.

## 14. Audit logging

Consequential operations should record:

- timestamp;
- actor;
- proposed action;
- arguments;
- policy decision;
- policy reason;
- approver;
- approval result;
- execution result.

## 15. Layered guardrails

Useful layers include:

```text
schema guardrail
permission guardrail
policy guardrail
approval guardrail
execution guardrail
audit guardrail
```

No one layer replaces the others.
