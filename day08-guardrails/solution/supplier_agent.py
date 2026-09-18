from approval_queue import ApprovalQueue
from audit_log import AuditLog
from policy import PolicyEngine


def execute_purchase_order(action):
    return {
        "status": "CREATED",
        "purchase_order_id": "PO-1001",
        "supplier_id": action["arguments"]["supplier_id"],
        "total_value": action["arguments"]["total_value"],
    }


def main():
    state = {
        "inspected_supplier_ids": ["SUP-002"],
        "rejected_supplier_ids": [],
    }

    actor_role = "procurement_manager"
    action = {
        "name": "CREATE_PURCHASE_ORDER",
        "arguments": {
            "supplier_id": "SUP-002",
            "quantity": 100,
            "unit_price": 445,
            "total_value": 44500,
        },
    }

    policy = PolicyEngine()
    approvals = ApprovalQueue()
    audit = AuditLog()

    decision = policy.evaluate(action, actor_role, state)
    audit.record("POLICY_DECISION", {
        "action": action,
        "actor_role": actor_role,
        "decision": decision.result,
        "reason": decision.reason,
    })

    if decision.result == "DENY":
        print("Action denied:", decision.reason)
        return

    if decision.result == "REQUIRE_APPROVAL":
        request = approvals.submit(action, decision.required_role)
        audit.record("APPROVAL_REQUESTED", {"request": request})

        approved = approvals.approve(
            request["id"],
            {"id": "USER-42", "role": decision.required_role},
        )
        audit.record("APPROVAL_RESOLVED", {"request": approved})

        if not approvals.is_approved_for(request["id"], action):
            print("Approval no longer matches action")
            return

    result = execute_purchase_order(action)
    audit.record("ACTION_EXECUTED", {"action": action, "result": result})

    print("Execution result:")
    print(result)

    print("\nAudit log:")
    for entry in audit.entries:
        print(entry)


if __name__ == "__main__":
    main()
