from dataclasses import dataclass


@dataclass
class AgentError:
    type: str
    component: str
    message: str
    retryable: bool
    attempt: int = 1
