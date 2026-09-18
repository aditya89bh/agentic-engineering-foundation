def evaluate_purchase_order(actor_role: str, total_value: float, inspected: bool):
    if actor_role not in {"procurement_manager", "finance_approver", "admin"}:
        return {"result":"DENY","reason":"role cannot create purchase orders","required_role":None}
    if not inspected:
        return {"result":"DENY","reason":"supplier must be inspected","required_role":None}
    if total_value < 10000:
        return {"result":"ALLOW","reason":"below approval threshold","required_role":None}
    if total_value <= 50000:
        return {"result":"REQUIRE_APPROVAL","reason":"manager approval required","required_role":"procurement_manager"}
    return {"result":"REQUIRE_APPROVAL","reason":"finance approval required","required_role":"finance_approver"}
