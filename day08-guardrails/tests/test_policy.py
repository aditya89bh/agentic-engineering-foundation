import importlib.util
import unittest
from pathlib import Path


BASE = Path(__file__).resolve().parents[1] / "solution"


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, BASE / file)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


policy_mod = load("policy_test", "policy.py")


class PolicyTests(unittest.TestCase):
    def setUp(self):
        self.engine = policy_mod.PolicyEngine()
        self.state = {
            "inspected_supplier_ids": ["SUP-002"],
            "rejected_supplier_ids": [],
        }

    def po(self, total=5000, supplier="SUP-002"):
        return {
            "name": "CREATE_PURCHASE_ORDER",
            "arguments": {"supplier_id": supplier, "total_value": total},
        }

    def test_read_action_allowed(self):
        result = self.engine.evaluate({"name": "SEARCH_SUPPLIERS", "arguments": {}}, "researcher", self.state)
        self.assertEqual(result.result, "ALLOW")

    def test_researcher_cannot_create_po(self):
        result = self.engine.evaluate(self.po(), "researcher", self.state)
        self.assertEqual(result.result, "DENY")

    def test_uninspected_supplier_denied(self):
        result = self.engine.evaluate(self.po(supplier="SUP-999"), "procurement_manager", self.state)
        self.assertEqual(result.result, "DENY")

    def test_small_po_allowed(self):
        result = self.engine.evaluate(self.po(9000), "procurement_manager", self.state)
        self.assertEqual(result.result, "ALLOW")

    def test_medium_po_requires_manager_approval(self):
        result = self.engine.evaluate(self.po(20000), "procurement_manager", self.state)
        self.assertEqual(result.result, "REQUIRE_APPROVAL")
        self.assertEqual(result.required_role, "procurement_manager")

    def test_large_po_requires_finance_approval(self):
        result = self.engine.evaluate(self.po(80000), "procurement_manager", self.state)
        self.assertEqual(result.required_role, "finance_approver")

    def test_rejected_supplier_denied(self):
        self.state["rejected_supplier_ids"] = ["SUP-002"]
        result = self.engine.evaluate(self.po(), "procurement_manager", self.state)
        self.assertEqual(result.result, "DENY")


if __name__ == "__main__":
    unittest.main()
