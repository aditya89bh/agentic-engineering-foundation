from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PolicyDecision:
    result: str
    reason: str
    required_role: str | None = None


TOOL_LEVELS = {
    "SEARCH_SUPPLIERS": "READ",
    "INSPECT_SUPPLIER": "READ",
    "CALCULATE_LANDED_COST": "COMPUTE",
    "EMAIL_SUPPLIER": "WRITE",
    "CREATE_PURCHASE_ORDER": "HIGH_RISK",
    "DELETE_SUPPLIER_RECORD": "HIGH_RISK",
}


class PolicyEngine:
    def evaluate(self, action: dict, actor_role: str, state: dict) -> PolicyDecision:
        name = action.get("name")
        args = action.get("arguments", {})

        if name not in TOOL_LEVELS:
            return PolicyDecision("DENY", "Unknown or unsupported tool")

        if name in {"SEARCH_SUPPLIERS", "INSPECT_SUPPLIER", "CALCULATE_LANDED_COST"}:
            return PolicyDecision("ALLOW", "Read or compute action")

        if name == "DELETE_SUPPLIER_RECORD":
            if actor_role != "admin":
                return PolicyDecision("DENY", "Only admins may delete supplier records")
            return PolicyDecision("REQUIRE_APPROVAL", "Destructive action", "admin")

        if name == "EMAIL_SUPPLIER":
            if actor_role not in {"procurement_manager", "admin"}:
                return PolicyDecision("DENY", "Role cannot contact suppliers")
            return PolicyDecision("ALLOW", "Authorized write action")

        if name == "CREATE_PURCHASE_ORDER":
            if actor_role not in {"procurement_manager", "finance_approver", "admin"}:
                return PolicyDecision("DENY", "Role cannot create purchase orders")

            supplier_id = args.get("supplier_id")
            inspected = set(state.get("inspected_supplier_ids", []))
            if supplier_id not in inspected:
                return PolicyDecision("DENY", "Supplier must be inspected before PO creation")

            if supplier_id in set(state.get("rejected_supplier_ids", [])):
                return PolicyDecision("DENY", "Supplier is currently rejected")

            total_value = float(args.get("total_value", 0))
            if total_value < 10000:
                return PolicyDecision("ALLOW", "Order is below approval threshold")
            if total_value <= 50000:
                return PolicyDecision(
                    "REQUIRE_APPROVAL",
                    "Order requires procurement-manager approval",
                    "procurement_manager",
                )
            return PolicyDecision(
                "REQUIRE_APPROVAL",
                "High-value order requires finance approval",
                "finance_approver",
            )

        return PolicyDecision("DENY", "No policy matched")
