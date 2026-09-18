import importlib.util
import sys
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))

req_spec = importlib.util.spec_from_file_location("requirements_cap", BASE/"requirements.py")
req_mod = importlib.util.module_from_spec(req_spec); req_spec.loader.exec_module(req_mod)

agent_spec = importlib.util.spec_from_file_location("supplier_agent_cap", BASE/"agent"/"supplier_agent.py")
agent_mod = importlib.util.module_from_spec(agent_spec); agent_spec.loader.exec_module(agent_mod)


class CapstoneTests(unittest.TestCase):
    def test_happy_path(self):
        req = req_mod.SupplierRequirement("aluminum brackets",100,500,14,"ISO 9001")
        state, _ = agent_mod.run_agent(req)
        self.assertEqual(state.status, "COMPLETED")
        self.assertEqual(state.recommendation["id"], "SUP-002")

    def test_budget_failure(self):
        req = req_mod.SupplierRequirement("aluminum brackets",100,400)
        state, _ = agent_mod.run_agent(req)
        self.assertEqual(state.status, "FAILED")

    def test_lead_time_failure(self):
        req = req_mod.SupplierRequirement("aluminum brackets",100,500,5)
        state, _ = agent_mod.run_agent(req)
        self.assertEqual(state.status, "FAILED")

    def test_validation_rejects_negative_quantity(self):
        req = req_mod.SupplierRequirement("aluminum brackets",-1,500)
        with self.assertRaises(ValueError):
            req.validate()

    def test_audit_written_on_success(self):
        req = req_mod.SupplierRequirement("aluminum brackets",100,500)
        state, audit = agent_mod.run_agent(req)
        self.assertEqual(state.status, "COMPLETED")
        self.assertTrue(audit)


if __name__ == "__main__":
    unittest.main()
