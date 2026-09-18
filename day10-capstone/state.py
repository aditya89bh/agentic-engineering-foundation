from dataclasses import dataclass, field


TERMINAL = {"COMPLETED", "FAILED", "NEEDS_HUMAN"}

VALID_TRANSITIONS = {
    "START": {"SEARCHING"},
    "SEARCHING": {"INSPECTING", "FAILED"},
    "INSPECTING": {"COMPARING", "FAILED"},
    "COMPARING": {"WAITING_FOR_APPROVAL", "COMPLETED", "FAILED"},
    "WAITING_FOR_APPROVAL": {"COMPLETED", "FAILED", "NEEDS_HUMAN"},
    "COMPLETED": set(),
    "FAILED": set(),
    "NEEDS_HUMAN": set(),
}


@dataclass
class AgentState:
    status: str = "START"
    step: int = 0
    candidates: list[dict] = field(default_factory=list)
    inspected: list[dict] = field(default_factory=list)
    recommendation: dict | None = None
    stop_reason: str | None = None

    def transition(self, next_status: str):
        if next_status not in VALID_TRANSITIONS[self.status]:
            raise ValueError(f"Invalid transition: {self.status} -> {next_status}")
        self.status = next_status
