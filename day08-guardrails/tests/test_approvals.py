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


approval_mod = load("approval_test", "approval_queue.py")


class ApprovalTests(unittest.TestCase):
    def setUp(self):
        self.queue = approval_mod.ApprovalQueue()
        self.action = {
            "name": "CREATE_PURCHASE_ORDER",
            "arguments": {"supplier_id": "SUP-002", "total_value": 44500},
        }

    def test_submit_creates_pending_request(self):
        request = self.queue.submit(self.action, "procurement_manager")
        self.assertEqual(request["status"], "PENDING")

    def test_correct_role_can_approve(self):
        request = self.queue.submit(self.action, "procurement_manager")
        result = self.queue.approve(request["id"], {"id": "U1", "role": "procurement_manager"})
        self.assertEqual(result["status"], "APPROVED")

    def test_wrong_role_cannot_approve(self):
        request = self.queue.submit(self.action, "finance_approver")
        with self.assertRaises(PermissionError):
            self.queue.approve(request["id"], {"id": "U1", "role": "procurement_manager"})

    def test_reused_approval_rejected(self):
        request = self.queue.submit(self.action, "procurement_manager")
        self.queue.approve(request["id"], {"id": "U1", "role": "procurement_manager"})
        with self.assertRaises(ValueError):
            self.queue.approve(request["id"], {"id": "U1", "role": "procurement_manager"})

    def test_changed_action_invalidates_approval(self):
        request = self.queue.submit(self.action, "procurement_manager")
        self.queue.approve(request["id"], {"id": "U1", "role": "procurement_manager"})
        changed = {
            "name": "CREATE_PURCHASE_ORDER",
            "arguments": {"supplier_id": "SUP-002", "total_value": 49999},
        }
        self.assertFalse(self.queue.is_approved_for(request["id"], changed))


if __name__ == "__main__":
    unittest.main()
