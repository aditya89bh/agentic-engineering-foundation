from dataclasses import dataclass


@dataclass(frozen=True)
class SupplierRequirement:
    component: str
    quantity: int
    max_unit_price: float
    max_lead_days: int | None = None
    certification: str | None = None

    def validate(self):
        if not self.component.strip():
            raise ValueError("component is required")
        if self.quantity <= 0:
            raise ValueError("quantity must be positive")
        if self.max_unit_price <= 0:
            raise ValueError("max_unit_price must be positive")
        if self.max_lead_days is not None and self.max_lead_days <= 0:
            raise ValueError("max_lead_days must be positive")
        return self
