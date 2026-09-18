class ApprovalQueue:
    def __init__(self):
        self.requests = {}

    def submit(self, request):
        # TODO: store a pending approval request
        raise NotImplementedError

    def approve(self, request_id, approver):
        # TODO: approve only the exact pending request
        raise NotImplementedError

    def reject(self, request_id, approver):
        # TODO: reject only the exact pending request
        raise NotImplementedError
