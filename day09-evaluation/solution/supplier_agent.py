def run_case(case):
    request = case["request"]
    trace = []
    result = {
        "status": "COMPLETED",
        "unit_price": case.get("simulated_price", 450),
        "approval_obtained": not case.get("approval_required", False),
    }

    if case.get("tool_failure"):
        trace.append({"step": 1, "action": "SEARCH_SUPPLIERS", "status": "FAILED"})
        trace.append({"step": 2, "action": "SEARCH_SUPPLIERS", "status": "RETRY_SUCCESS"})
    else:
        trace.append({"step": 1, "action": "SEARCH_SUPPLIERS", "status": "OK"})

    if case.get("required_tool") == "INSPECT_SUPPLIER":
        trace.append({"step": len(trace) + 1, "action": "INSPECT_SUPPLIER", "supplier_id": "SUP-002"})

    if case.get("approval_required"):
        trace.append({"step": len(trace) + 1, "action": "REQUEST_APPROVAL", "status": "PENDING"})
        result["approval_obtained"] = case.get("simulate_approval", True)

    if case.get("force_failure"):
        result["status"] = "FAILED"

    result["request"] = request
    return result, trace
