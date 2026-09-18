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


errors = load("errors_failure", "errors.py")
executor_mod = load("reliable_executor_failure", "reliable_executor.py")


class FailureTests(unittest.TestCase):
    def test_failure_is_logged(self):
        def operation():
            raise errors.RetryableToolError("timeout")

        executor = executor_mod.ReliableExecutor(max_attempts=1, base_delay=0)
        executor.execute(operation, component="SEARCH")
        self.assertEqual(len(executor.failure_log), 1)
        self.assertEqual(executor.failure_log[0]["component"], "SEARCH")

    def test_retryable_flag_is_true(self):
        def operation():
            raise errors.RetryableToolError("timeout")

        executor = executor_mod.ReliableExecutor(max_attempts=1, base_delay=0)
        executor.execute(operation)
        self.assertTrue(executor.failure_log[0]["retryable"])

    def test_permanent_flag_is_false(self):
        def operation():
            raise errors.PermanentToolError("invalid")

        executor = executor_mod.ReliableExecutor(max_attempts=3, base_delay=0)
        executor.execute(operation)
        self.assertFalse(executor.failure_log[0]["retryable"])

    def test_success_has_no_failure_log(self):
        executor = executor_mod.ReliableExecutor(max_attempts=3, base_delay=0)
        result = executor.execute(lambda: 42)
        self.assertEqual(result["value"], 42)
        self.assertEqual(executor.failure_log, [])


if __name__ == "__main__":
    unittest.main()
