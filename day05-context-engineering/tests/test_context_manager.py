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


data = load("context_data", "context_data.py")
manager_mod = load("context_manager", "context_manager.py")


class ContextManagerTests(unittest.TestCase):
    def setUp(self):
        self.manager = manager_mod.ContextManager()
        self.state = data.SAMPLE_STATE

    def test_latest_requirement_wins(self):
        context = self.manager.build(self.state, "COMPARE")
        self.assertEqual(context["requirements"]["max_unit_price"], 550)

    def test_irrelevant_chat_removed(self):
        context = self.manager.build(self.state, "COMPARE")
        self.assertTrue(all(event["type"] != "chat" for event in context["history"]))

    def test_compare_gets_only_compare_tools(self):
        context = self.manager.build(self.state, "COMPARE")
        self.assertEqual(context["available_tools"], ["CALCULATE_LANDED_COST"])

    def test_inspected_data_is_compressed(self):
        context = self.manager.build(self.state, "COMPARE")
        self.assertEqual(context["evidence"]["count"], 2)
        self.assertEqual(context["evidence"]["best_price"], 445)

    def test_unknown_decision_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.build(self.state, "UNKNOWN")


if __name__ == "__main__":
    unittest.main()
