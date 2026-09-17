"""Starter dispatcher for Day 3."""

from tools import calculate_landed_cost, inspect_supplier, search_suppliers

TOOLS = {
    "SEARCH_SUPPLIERS": search_suppliers,
    "INSPECT_SUPPLIER": inspect_supplier,
    "CALCULATE_LANDED_COST": calculate_landed_cost,
}

TOOL_PERMISSIONS = {
    "SEARCH_SUPPLIERS": "read",
    "INSPECT_SUPPLIER": "read",
    "CALCULATE_LANDED_COST": "compute",
}


def validate_tool_call(call: dict) -> str | None:
    # TODO: validate tool name and required argument shapes.
    return None


def dispatch_tool(call: dict):
    # TODO: reject invalid calls, then execute the registered function.
    raise NotImplementedError
