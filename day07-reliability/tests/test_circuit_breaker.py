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


breaker_mod = load("circuit_breaker_test", "circuit_breaker.py")


class FakeClock:
    def __init__(self):
        self.now = 0

    def __call__(self):
        return self.now


class CircuitBreakerTests(unittest.TestCase):
    def test_opens_after_threshold(self):
        clock = FakeClock()
        breaker = breaker_mod.CircuitBreaker(2, 10, clock)
        breaker.record_failure()
        breaker.record_failure()
        self.assertEqual(breaker.state, "OPEN")

    def test_open_circuit_blocks_call(self):
        clock = FakeClock()
        breaker = breaker_mod.CircuitBreaker(1, 10, clock)
        breaker.record_failure()
        with self.assertRaises(breaker_mod.CircuitOpenError):
            breaker.allow_call()

    def test_moves_to_half_open_after_recovery_window(self):
        clock = FakeClock()
        breaker = breaker_mod.CircuitBreaker(1, 10, clock)
        breaker.record_failure()
        clock.now = 11
        self.assertTrue(breaker.allow_call())
        self.assertEqual(breaker.state, "HALF_OPEN")

    def test_success_closes_circuit(self):
        clock = FakeClock()
        breaker = breaker_mod.CircuitBreaker(1, 10, clock)
        breaker.record_failure()
        clock.now = 11
        breaker.allow_call()
        breaker.record_success()
        self.assertEqual(breaker.state, "CLOSED")


if __name__ == "__main__":
    unittest.main()
