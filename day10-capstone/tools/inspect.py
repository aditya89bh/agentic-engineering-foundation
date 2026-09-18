from search import SUPPLIERS


def inspect_supplier(supplier_id: str):
    for supplier in SUPPLIERS:
        if supplier["id"] == supplier_id:
            return dict(supplier)
    raise ValueError("supplier not found")


def check_certification(supplier_id: str, certification: str):
    supplier = inspect_supplier(supplier_id)
    return supplier.get("certification") == certification
