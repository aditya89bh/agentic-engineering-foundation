"""Tests for Day 3 validation and dispatch."""

import importlib.util
import sys
import unittest
from pathlib import Path

SOLUTION = Path(__file__).resolve().parents[1] / "solution"
sys.path.insert(0, str(SOLUTION))
MODULE = SOLUTION / "tool_router.py"
SPEC = importlib.util.spec_from_file_location("day03_router", MODULE)
router = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(router)


class ToolRouterTests(unittest.TestCase):
    def test_unknown_tool_is_rejected(self):
        error = router.validate_tool_call({"name": "DELETE_SUPPLIER", "arguments": {}})
        self.assertIsNotNone(error)

    def test_missing_argument_is_rejected(self):
        error = router.validate_tool_call({"name": "INSPECT_SUPPLIER", "arguments": {}})
        self.assertIsNotNone(error)

    def test_wrong_argument_type_is_rejected(self):
        call = {
            "name": "SEARCH_SUPPLIERS",
            "arguments": {"component": "aluminum brackets", "max_unit_price": "cheap"},
        }
        self.assertIsNotNone(router.validate_tool_call(call))

    def test_valid_call_dispatches(self):
        call = {
            "name": "INSPECT_SUPPLIER",
            "arguments": {"supplier_id": "SUP-002"},
        }
        result = router.dispatch_tool(call)
        self.assertEqual(result["id"], "SUP-002")


if __name__ == "__main__":
    unittest.main()
