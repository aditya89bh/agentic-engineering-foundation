"""Starter: convert procurement text into validated structured requirements.

Run:
    python day02-structured-outputs/starter/requirement_extractor.py \
      "Need 100 aluminum brackets below ₹500 within 14 days"
"""

from __future__ import annotations

import json
import sys
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, ValidationError


class SupplierRequirement(BaseModel):
    """TODO: complete the schema and constraints."""

    model_config = ConfigDict(extra="forbid")

    component: str = Field(min_length=1)
    quantity: int = Field(gt=0)
    max_unit_price: float = Field(gt=0)
    currency: Literal["INR", "USD", "EUR"]
    max_lead_days: int | None = Field(default=None, gt=0)


def mock_extract(text: str) -> dict:
    """Return intentionally simple extracted data.

    Day 2 focuses on the contract and validation boundary. Replace this mock
    extractor with a model later if instructed.
    """
    lowered = text.lower()

    # TODO: improve these deterministic extraction rules.
    result = {
        "component": "aluminum brackets" if "aluminum" in lowered else "",
        "quantity": 100 if "100" in lowered else None,
        "max_unit_price": 500 if "500" in lowered else None,
        "currency": "INR" if "₹" in text or "inr" in lowered else None,
        "max_lead_days": 14 if "14" in lowered or "two weeks" in lowered else None,
    }
    return result


def validate_requirement(data: dict) -> SupplierRequirement:
    """TODO: validate data through the Pydantic model."""
    return SupplierRequirement.model_validate(data)


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: requirement_extractor.py \"procurement request\"")
        return 1

    text = sys.argv[1]
    extracted = mock_extract(text)

    print("Extracted:")
    print(json.dumps(extracted, indent=2, ensure_ascii=False))

    try:
        requirement = validate_requirement(extracted)
    except ValidationError as exc:
        print("\nValidation failed:")
        print(exc)
        return 2

    print("\nValidated:")
    print(requirement.model_dump_json(indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
