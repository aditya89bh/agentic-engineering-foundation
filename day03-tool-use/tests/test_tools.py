"""Tests for Day 3 tools."""

import importlib.util
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / "solution" / "tools.py"
SPEC = importlib.util.spec_from_file_location("day03_tools", MODULE)
tools = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(tools)


class ToolTests(unittest.TestCase):
    def test_search_filters_component_and_price(self):
        result = tools.search_suppliers("aluminum brackets", 500)
        self.assertEqual({item["id"] for item in result}, {"SUP-001", "SUP-002"})

    def test_inspect_unknown_supplier_fails(self):
        with self.assertRaises(ValueError):
            tools.inspect_supplier("SUP-999")

    def test_landed_cost_is_calculated(self):
        result = tools.calculate_landed_cost(445, 42, 0.18)
        self.assertEqual(result["landed_cost"], 574.66)

    def test_negative_cost_is_rejected(self):
        with self.assertRaises(ValueError):
            tools.calculate_landed_cost(-1, 10)


if __name__ == "__main__":
    unittest.main()
