from dataclasses import dataclass, asdict
from typing import Optional


@dataclass(frozen=True)
class MemoryRecord:
    id: str
    type: str
    subject: str
    content: str
    source: str
    confidence: float
    created_at: str
    expires_at: Optional[str] = None

    def as_dict(self):
        return asdict(self)
