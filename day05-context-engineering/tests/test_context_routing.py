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


data = load("context_data2", "context_data.py")
manager_mod = load("context_manager2", "context_manager.py")


class ContextRoutingTests(unittest.TestCase):
    def setUp(self):
        self.manager = manager_mod.ContextManager()

    def test_search_context_excludes_inspection_evidence(self):
        context = self.manager.build(data.SAMPLE_STATE, "SEARCH")
        self.assertNotIn("evidence", context)

    def test_inspect_context_includes_candidates(self):
        context = self.manager.build(data.SAMPLE_STATE, "INSPECT")
        self.assertIn("candidates", context)

    def test_finish_context_has_no_tools(self):
        context = self.manager.build(data.SAMPLE_STATE, "FINISH")
        self.assertEqual(context["available_tools"], [])

    def test_compare_context_contains_requirements(self):
        context = self.manager.build(data.SAMPLE_STATE, "COMPARE")
        self.assertIn("requirements", context)

    def test_history_is_bounded(self):
        context = self.manager.build(data.SAMPLE_STATE, "COMPARE")
        self.assertLessEqual(len(context["history"]), 4)


if __name__ == "__main__":
    unittest.main()
