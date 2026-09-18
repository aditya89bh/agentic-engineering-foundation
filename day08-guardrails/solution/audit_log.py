from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone


class AuditLog:
    def __init__(self):
        self.entries = []

    def record(self, event_type: str, payload: dict):
        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "event_type": event_type,
            **deepcopy(payload),
        }
        self.entries.append(entry)
        return deepcopy(entry)
