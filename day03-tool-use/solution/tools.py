"""Reference tools for Day 3."""

SUPPLIERS = [
    {"id": "SUP-001", "name": "Apex Components", "product": "aluminum brackets", "unit_price": 480, "shipping": 30},
    {"id": "SUP-002", "name": "Bharat Fabrication", "product": "aluminum brackets", "unit_price": 445, "shipping": 42},
    {"id": "SUP-003", "name": "Precision Industrial", "product": "steel brackets", "unit_price": 390, "shipping": 35},
]


def search_suppliers(component: str, max_unit_price: float) -> list[dict]:
    return [
        supplier for supplier in SUPPLIERS
        if component.lower() in supplier["product"].lower()
        and supplier["unit_price"] <= max_unit_price
    ]


def inspect_supplier(supplier_id: str) -> dict:
    for supplier in SUPPLIERS:
        if supplier["id"] == supplier_id:
            return supplier
    raise ValueError(f"Unknown supplier_id: {supplier_id}")


def calculate_landed_cost(unit_price: float, shipping: float, tax_rate: float = 0.18) -> dict:
    if unit_price < 0 or shipping < 0 or tax_rate < 0:
        raise ValueError("Cost inputs must be non-negative")
    subtotal = unit_price + shipping
    tax_amount = round(subtotal * tax_rate, 2)
    return {
        "unit_price": unit_price,
        "shipping": shipping,
        "tax_rate": tax_rate,
        "tax_amount": tax_amount,
        "landed_cost": round(subtotal + tax_amount, 2),
    }
