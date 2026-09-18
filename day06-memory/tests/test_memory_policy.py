import importlib.util
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path


BASE = Path(__file__).resolve().parents[1] / "solution"


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, BASE / file)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


schema = load("memory_schema_policy", "memory_schema.py")
policy = load("memory_policy", "memory_policy.py")


class MemoryPolicyTests(unittest.TestCase):
    def record(self, **overrides):
        values = {
            "id": "MEM-1",
            "type": "decision",
            "subject": "SUP-017",
            "content": "Rejected for repeated delivery delays",
            "source": "supplier_evaluation",
            "confidence": 1.0,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "expires_at": None,
        }
        values.update(overrides)
        return schema.MemoryRecord(**values)

    def test_good_memory_is_written(self):
        self.assertTrue(policy.should_write(self.record()))

    def test_low_confidence_not_written(self):
        self.assertFalse(policy.should_write(self.record(confidence=0.2)))

    def test_missing_source_not_written(self):
        self.assertFalse(policy.should_write(self.record(source="")))

    def test_expired_memory_not_retrieved(self):
        expiry = (datetime.now(timezone.utc) - timedelta(days=1)).isoformat()
        self.assertFalse(policy.should_retrieve(self.record(expires_at=expiry)))

    def test_wrong_subject_not_retrieved(self):
        self.assertFalse(policy.should_retrieve(self.record(), subject="SUP-002"))


if __name__ == "__main__":
    unittest.main()
