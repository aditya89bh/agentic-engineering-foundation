from __future__ import annotations

import hashlib
import json
import uuid
from copy import deepcopy
from datetime import datetime, timezone


def action_fingerprint(action: dict) -> str:
    payload = json.dumps(action, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


class ApprovalQueue:
    def __init__(self):
        self.requests = {}

    def submit(self, action: dict, required_role: str):
        request_id = str(uuid.uuid4())
        record = {
            "id": request_id,
            "status": "PENDING",
            "action": deepcopy(action),
            "fingerprint": action_fingerprint(action),
            "required_role": required_role,
            "approver": None,
            "created_at": datetime.now(timezone.utc).isoformat(),
        }
        self.requests[request_id] = record
        return deepcopy(record)

    def _resolve(self, request_id: str, approver: dict, status: str):
        if request_id not in self.requests:
            raise KeyError("approval request not found")

        request = self.requests[request_id]
        if request["status"] != "PENDING":
            raise ValueError("approval request is no longer pending")

        if approver.get("role") != request["required_role"]:
            raise PermissionError("approver does not have required role")

        request["status"] = status
        request["approver"] = dict(approver)
        request["resolved_at"] = datetime.now(timezone.utc).isoformat()
        return deepcopy(request)

    def approve(self, request_id: str, approver: dict):
        return self._resolve(request_id, approver, "APPROVED")

    def reject(self, request_id: str, approver: dict):
        return self._resolve(request_id, approver, "REJECTED")

    def is_approved_for(self, request_id: str, action: dict) -> bool:
        request = self.requests.get(request_id)
        if not request or request["status"] != "APPROVED":
            return False
        return request["fingerprint"] == action_fingerprint(action)
