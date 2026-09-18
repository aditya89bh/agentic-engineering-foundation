from dataclasses import dataclass, asdict


class RetryableToolError(Exception):
    pass


class PermanentToolError(Exception):
    pass


@dataclass(frozen=True)
class AgentError:
    type: str
    component: str
    message: str
    retryable: bool
    attempt: int

    def as_dict(self):
        return asdict(self)
