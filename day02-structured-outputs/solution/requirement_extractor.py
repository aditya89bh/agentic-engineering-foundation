"""Reference solution for Day 2 structured outputs and schema validation."""

from __future__ import annotations

import json
import re
import sys
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, ValidationError


class SupplierRequirement(BaseModel):
    model_config = ConfigDict(extra="forbid")

    component: str = Field(min_length=1)
    quantity: int = Field(gt=0)
    max_unit_price: float = Field(gt=0)
    currency: Literal["INR", "USD", "EUR"]
    max_lead_days: int | None = Field(default=None, gt=0)


def detect_currency(text: str) -> str | None:
    lowered = text.lower()
    if "₹" in text or "inr" in lowered:
        return "INR"
    if "$" in text or "usd" in lowered:
        return "USD"
    if "€" in text or "eur" in lowered:
        return "EUR"
    return None


def extract_number_before(text: str, phrase: str) -> int | None:
    match = re.search(rf"(\d+)\s+{re.escape(phrase)}", text.lower())
    return int(match.group(1)) if match else None


def extract_price(text: str) -> float | None:
    patterns = [
        r"(?:₹|inr\s*)(\d+(?:\.\d+)?)",
        r"(?:€|eur\s*)(\d+(?:\.\d+)?)",
        r"(?:\$|usd\s*)(\d+(?:\.\d+)?)",
        r"(?:below|under|max(?:imum)?)\s+(?:₹|€|\$)?\s*(\d+(?:\.\d+)?)",
    ]
    for pattern in patterns:
        match = re.search(pattern, text.lower())
        if match:
            return float(match.group(1))
    return None


def extract_lead_days(text: str) -> int | None:
    lowered = text.lower()
    match = re.search(r"within\s+(\d+)\s+days?", lowered)
    if match:
        return int(match.group(1))
    if "within two weeks" in lowered or "within 2 weeks" in lowered:
        return 14
    return None


def extract_component(text: str) -> str | None:
    lowered = text.lower()
    known_components = [
        "aluminum brackets",
        "stainless-steel gears",
        "stainless steel gears",
        "aluminum enclosures",
        "bearings",
        "injection-molded housings",
        "machined brackets",
    ]
    for component in known_components:
        if component in lowered:
            return component
    return None


def extract_requirement(text: str) -> dict:
    """Deterministic extractor used to isolate schema engineering from LLM behavior."""
    component = extract_component(text)

    quantity_match = re.search(
        r"(?:need|source|looking for)\s+(\d+)\s+", text.lower()
    )
    quantity = int(quantity_match.group(1)) if quantity_match else None

    return {
        "component": component,
        "quantity": quantity,
        "max_unit_price": extract_price(text),
        "currency": detect_currency(text),
        "max_lead_days": extract_lead_days(text),
    }


def validate_requirement(data: dict) -> SupplierRequirement:
    return SupplierRequirement.model_validate(data)


def parse_and_validate_json(raw: str) -> SupplierRequirement:
    """Show the boundary a model response would pass through."""
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise TypeError("Structured output must be a JSON object")
    return validate_requirement(data)


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: requirement_extractor.py \"procurement request\"")
        return 1

    text = sys.argv[1]
    extracted = extract_requirement(text)

    print("Extracted:")
    print(json.dumps(extracted, indent=2, ensure_ascii=False))

    try:
        requirement = validate_requirement(extracted)
    except ValidationError as exc:
        print("\nValidation failed. Do not guess missing business-critical values:")
        print(exc)
        return 2

    print("\nValidated:")
    print(requirement.model_dump_json(indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
