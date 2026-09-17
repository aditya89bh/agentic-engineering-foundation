"""Starter tools for Day 3."""

SUPPLIERS = [
    {"id": "SUP-001", "name": "Apex Components", "product": "aluminum brackets", "unit_price": 480, "shipping": 30},
    {"id": "SUP-002", "name": "Bharat Fabrication", "product": "aluminum brackets", "unit_price": 445, "shipping": 42},
    {"id": "SUP-003", "name": "Precision Industrial", "product": "steel brackets", "unit_price": 390, "shipping": 35},
]


def search_suppliers(component: str, max_unit_price: float):
    # TODO: return suppliers matching component and hard price constraint.
    raise NotImplementedError


def inspect_supplier(supplier_id: str):
    # TODO: return exactly one supplier or raise a clear error.
    raise NotImplementedError


def calculate_landed_cost(unit_price: float, shipping: float, tax_rate: float = 0.18):
    # TODO: return base cost, shipping, tax amount, and landed cost.
    raise NotImplementedError
