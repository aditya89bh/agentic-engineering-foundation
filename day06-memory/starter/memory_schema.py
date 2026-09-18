from dataclasses import dataclass
from typing import Optional


@dataclass
class MemoryRecord:
    id: str
    type: str
    subject: str
    content: str
    source: str
    confidence: float
    created_at: str
    expires_at: Optional[str] = None
