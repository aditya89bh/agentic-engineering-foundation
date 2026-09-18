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


graders = load("graders_test", "graders.py")


class GraderTests(unittest.TestCase):
    def test_task_success(self):
        self.assertTrue(graders.grade_task_success({"status": "COMPLETED"}, {"expected_status": "COMPLETED"}))

    def test_budget(self):
        self.assertTrue(graders.grade_budget({"unit_price": 450}, {"max_price": 500}))
        self.assertFalse(graders.grade_budget({"unit_price": 550}, {"max_price": 500}))

    def test_required_tool(self):
        trace = [{"action": "SEARCH_SUPPLIERS"}, {"action": "INSPECT_SUPPLIER"}]
        self.assertTrue(graders.grade_required_tool(trace, {"required_tool": "INSPECT_SUPPLIER"}))

    def test_forbidden_tool(self):
        trace = [{"action": "SEARCH_SUPPLIERS"}]
        self.assertTrue(graders.grade_forbidden_tool(trace, {"forbidden_tools": ["DELETE_SUPPLIER_RECORD"]}))

    def test_max_steps(self):
        trace = [{"action": "A"}, {"action": "B"}]
        self.assertTrue(graders.grade_max_steps(trace, {"max_steps": 2}))

    def test_approval(self):
        self.assertTrue(graders.grade_approval({"approval_obtained": True}, {"approval_required": True}))
        self.assertTrue(graders.grade_approval({}, {"approval_required": False}))


if __name__ == "__main__":
    unittest.main()
