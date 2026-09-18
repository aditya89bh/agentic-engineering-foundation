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


runner_mod = load("eval_runner_test", "eval_runner.py")


class EvalRunnerTests(unittest.TestCase):
    def agent(self, case):
        return {"status": case["expected_status"]}, [{"action": "SEARCH"}]

    def test_run_case(self):
        graders = {
            "status": lambda result, trace, case: result["status"] == case["expected_status"],
        }
        runner = runner_mod.EvalRunner(self.agent, graders)
        result = runner.run_case({"id": "C1", "expected_status": "COMPLETED"})
        self.assertTrue(result["success"])
        self.assertEqual(result["metrics"]["steps"], 1)

    def test_run_suite_aggregates(self):
        graders = {
            "status": lambda result, trace, case: result["status"] == case["expected_status"],
        }
        runner = runner_mod.EvalRunner(self.agent, graders)
        report = runner.run_suite([
            {"id": "C1", "expected_status": "COMPLETED"},
            {"id": "C2", "expected_status": "COMPLETED"},
        ])
        self.assertEqual(report["total_cases"], 2)
        self.assertEqual(report["passed"], 2)
        self.assertEqual(report["task_success_rate"], 1.0)


if __name__ == "__main__":
    unittest.main()
