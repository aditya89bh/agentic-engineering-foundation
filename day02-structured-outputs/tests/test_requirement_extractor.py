"""Tests for Day 2 structured requirement validation."""

from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

from pydantic import ValidationError

MODULE_PATH = Path(__file__).resolve().parents[1] / "solution" / "requirement_extractor.py"
SPEC = importlib.util.spec_from_file_location("day02_requirement_extractor", MODULE_PATH)
module = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(module)


class RequirementExtractorTests(unittest.TestCase):
    def test_valid_requirement(self):
        item = module.SupplierRequirement.model_validate(
            {
                "component": "aluminum brackets",
                "quantity": 100,
                "max_unit_price": 500,
                "currency": "INR",
                "max_lead_days": 14,
            }
        )
        self.assertEqual(item.quantity, 100)

    def test_negative_quantity_rejected(self):
        with self.assertRaises(ValidationError):
            module.SupplierRequirement.model_validate(
                {
                    "component": "aluminum brackets",
                    "quantity": -5,
                    "max_unit_price": 500,
                    "currency": "INR",
                }
            )

    def test_missing_required_field_rejected(self):
        with self.assertRaises(ValidationError):
            module.SupplierRequirement.model_validate(
                {
                    "component": "aluminum brackets",
                    "quantity": 100,
                    "currency": "INR",
                }
            )

    def test_unsupported_currency_rejected(self):
        with self.assertRaises(ValidationError):
            module.SupplierRequirement.model_validate(
                {
                    "component": "aluminum brackets",
                    "quantity": 100,
                    "max_unit_price": 500,
                    "currency": "GBP",
                }
            )

    def test_extra_field_rejected(self):
        with self.assertRaises(ValidationError):
            module.SupplierRequirement.model_validate(
                {
                    "component": "aluminum brackets",
                    "quantity": 100,
                    "max_unit_price": 500,
                    "currency": "INR",
                    "preferred_supplier": "Apex",
                }
            )

    def test_malformed_json_rejected(self):
        with self.assertRaises(json.JSONDecodeError):
            module.parse_and_validate_json('{"component": "aluminum brackets"')

    def test_optional_lead_time_can_be_missing(self):
        item = module.SupplierRequirement.model_validate(
            {
                "component": "aluminum brackets",
                "quantity": 100,
                "max_unit_price": 500,
                "currency": "INR",
            }
        )
        self.assertIsNone(item.max_lead_days)


if __name__ == "__main__":
    unittest.main()
