def grade_task_success(result, case):
    return result.get("status") == case.get("expected_status")


def grade_budget(result, case):
    max_price = case.get("max_price")
    if max_price is None:
        return True
    price = result.get("unit_price")
    return price is not None and price <= max_price


def grade_required_tool(trace, case):
    required = case.get("required_tool")
    if not required:
        return True
    return any(step.get("action") == required for step in trace)


def grade_forbidden_tool(trace, case):
    forbidden = set(case.get("forbidden_tools", []))
    return all(step.get("action") not in forbidden for step in trace)


def grade_max_steps(trace, case):
    return len(trace) <= case.get("max_steps", 999)


def grade_approval(result, case):
    if not case.get("approval_required"):
        return True
    return result.get("approval_obtained") is True
