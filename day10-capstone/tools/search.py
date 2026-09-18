SUPPLIERS = [
    {"id":"SUP-001","component":"aluminum brackets","unit_price":480,"lead_days":12,"certification":"ISO 9001"},
    {"id":"SUP-002","component":"aluminum brackets","unit_price":445,"lead_days":9,"certification":"ISO 9001"},
    {"id":"SUP-003","component":"aluminum brackets","unit_price":520,"lead_days":7,"certification":"ISO 9001"},
]


def search_suppliers(component: str, max_unit_price: float):
    return [
        s for s in SUPPLIERS
        if s["component"] == component and s["unit_price"] <= max_unit_price
    ]
