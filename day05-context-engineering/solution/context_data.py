SAMPLE_STATE = {
    "goal": "Find aluminum brackets below ₹550/unit.",
    "status": "COMPARING",
    "requirements": {
        "component": "aluminum brackets",
        "max_unit_price": 550,
    },
    "candidates": ["SUP-001", "SUP-002", "SUP-003"],
    "inspected": [
        {"id": "SUP-001", "unit_price": 480, "quality": 4.5, "lead_days": 12},
        {"id": "SUP-002", "unit_price": 445, "quality": 4.8, "lead_days": 9},
    ],
    "history": [
        {"type": "requirement", "field": "max_unit_price", "value": 500, "version": 1},
        {"type": "tool", "name": "SEARCH_SUPPLIERS", "result_count": 3},
        {"type": "chat", "text": "thanks"},
        {"type": "requirement", "field": "max_unit_price", "value": 550, "version": 2},
        {"type": "tool", "name": "INSPECT_SUPPLIER", "supplier_id": "SUP-002"},
    ],
}
