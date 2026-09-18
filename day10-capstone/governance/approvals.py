class ApprovalQueue:
    def __init__(self):
        self.pending = {}

    def submit(self, request_id, action, required_role):
        self.pending[request_id] = {
            "action": action,
            "required_role": required_role,
            "status": "PENDING",
        }

    def approve(self, request_id, approver_role):
        request = self.pending[request_id]
        if approver_role != request["required_role"]:
            raise PermissionError("wrong approver role")
        request["status"] = "APPROVED"
        return request
