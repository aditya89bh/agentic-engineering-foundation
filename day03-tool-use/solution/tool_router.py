"""Reference tool registry, validation, and dispatcher for Day 3."""

from tools import calculate_landed_cost, inspect_supplier, search_suppliers

TOOLS = {
    "SEARCH_SUPPLIERS": search_suppliers,
    "INSPECT_SUPPLIER": inspect_supplier,
    "CALCULATE_LANDED_COST": calculate_landed_cost,
}

REQUIRED_ARGUMENTS = {
    "SEARCH_SUPPLIERS": {"component", "max_unit_price"},
    "INSPECT_SUPPLIER": {"supplier_id"},
    "CALCULATE_LANDED_COST": {"unit_price", "shipping"},
}

TOOL_PERMISSIONS = {
    "SEARCH_SUPPLIERS": "read",
    "INSPECT_SUPPLIER": "read",
    "CALCULATE_LANDED_COST": "compute",
}


def validate_tool_call(call: dict) -> str | None:
    if not isinstance(call, dict):
        return "Tool call must be an object"

    name = call.get("name")
    arguments = call.get("arguments")

    if name not in TOOLS:
        return f"Unknown tool: {name!r}"
    if not isinstance(arguments, dict):
        return "arguments must be an object"

    missing = REQUIRED_ARGUMENTS[name] - set(arguments)
    if missing:
        return f"Missing required arguments: {sorted(missing)}"

    if name == "SEARCH_SUPPLIERS":
        if not isinstance(arguments["component"], str):
            return "component must be a string"
        if not isinstance(arguments["max_unit_price"], (int, float)):
            return "max_unit_price must be numeric"

    if name == "INSPECT_SUPPLIER":
        if not isinstance(arguments["supplier_id"], str):
            return "supplier_id must be a string"

    if name == "CALCULATE_LANDED_COST":
        for field in ("unit_price", "shipping"):
            if not isinstance(arguments[field], (int, float)):
                return f"{field} must be numeric"
        if "tax_rate" in arguments and not isinstance(arguments["tax_rate"], (int, float)):
            return "tax_rate must be numeric"

    return None


def dispatch_tool(call: dict):
    error = validate_tool_call(call)
    if error:
        raise ValueError(error)

    tool = TOOLS[call["name"]]
    return tool(**call["arguments"])
