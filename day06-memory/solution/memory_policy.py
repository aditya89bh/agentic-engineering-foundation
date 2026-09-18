from __future__ import annotations

from datetime import datetime, timezone

from memory_schema import MemoryRecord


ALLOWED_TYPES = {"episodic", "semantic", "decision", "preference"}


def should_write(record: MemoryRecord) -> bool:
    if record.type not in ALLOWED_TYPES:
        return False
    if not record.source:
        return False
    if record.confidence < 0.5:
        return False
    if len(record.content.strip()) < 3:
        return False
    return True


def should_retrieve(record: MemoryRecord, subject: str | None = None) -> bool:
    if subject and record.subject != subject:
        return False
    if record.confidence < 0.5:
        return False
    if record.expires_at:
        expiry = datetime.fromisoformat(record.expires_at)
        if expiry <= datetime.now(timezone.utc):
            return False
    return True
