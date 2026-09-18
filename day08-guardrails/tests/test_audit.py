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


audit_mod = load("audit_test", "audit_log.py")


class AuditLogTests(unittest.TestCase):
    def test_records_timestamp_and_event(self):
        log = audit_mod.AuditLog()
        entry = log.record("POLICY_DECISION", {"decision": "ALLOW"})
        self.assertIn("timestamp", entry)
        self.assertEqual(entry["event_type"], "POLICY_DECISION")

    def test_keeps_multiple_entries(self):
        log = audit_mod.AuditLog()
        log.record("A", {})
        log.record("B", {})
        self.assertEqual(len(log.entries), 2)


if __name__ == "__main__":
    unittest.main()
