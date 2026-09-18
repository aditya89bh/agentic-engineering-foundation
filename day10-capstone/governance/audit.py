from datetime import datetime, timezone


class AuditLog:
    def __init__(self):
        self.entries = []

    def record(self, event, payload):
        self.entries.append({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "event": event,
            "payload": payload,
        })
