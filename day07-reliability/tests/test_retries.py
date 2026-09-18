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


errors = load("errors_retry", "errors.py")
executor_mod = load("reliable_executor_retry", "reliable_executor.py")


class RetryTests(unittest.TestCase):
    def test_transient_failure_retries_then_succeeds(self):
        calls = {"n": 0}

        def operation():
            calls["n"] += 1
            if calls["n"] < 3:
                raise errors.RetryableToolError("timeout")
            return "ok"

        executor = executor_mod.ReliableExecutor(max_attempts=3, base_delay=0)
        result = executor.execute(operation)
        self.assertEqual(result["status"], "COMPLETED")
        self.assertEqual(result["attempts"], 3)

    def test_retry_budget_is_bounded(self):
        def operation():
            raise errors.RetryableToolError("timeout")

        executor = executor_mod.ReliableExecutor(max_attempts=2, base_delay=0)
        result = executor.execute(operation)
        self.assertEqual(result["status"], "FAILED")
        self.assertEqual(result["attempts"], 2)

    def test_permanent_failure_is_not_retried(self):
        calls = {"n": 0}

        def operation():
            calls["n"] += 1
            raise errors.PermanentToolError("bad id")

        executor = executor_mod.ReliableExecutor(max_attempts=3, base_delay=0)
        result = executor.execute(operation)
        self.assertEqual(calls["n"], 1)
        self.assertEqual(result["status"], "FAILED")

    def test_fallback_used_after_retry_exhaustion(self):
        def operation():
            raise errors.RetryableToolError("down")

        executor = executor_mod.ReliableExecutor(max_attempts=2, base_delay=0)
        result = executor.execute(operation, fallback=lambda: "cache")
        self.assertEqual(result["status"], "PARTIAL_SUCCESS")
        self.assertTrue(result["fallback_used"])

    def test_fallback_failure_requires_human(self):
        def operation():
            raise errors.RetryableToolError("down")

        def fallback():
            raise RuntimeError("cache unavailable")

        executor = executor_mod.ReliableExecutor(max_attempts=1, base_delay=0)
        result = executor.execute(operation, fallback=fallback)
        self.assertEqual(result["status"], "NEEDS_HUMAN")


if __name__ == "__main__":
    unittest.main()
