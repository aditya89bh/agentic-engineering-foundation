from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

Status = Literal[
    "START",
    "SEARCHING",
    "INSPECTING",
    "COMPARING",
    "COMPLETED",
    "FAILED",
    "NEEDS_HUMAN",
]


@dataclass
class AgentState:
    goal: str
    status: Status = "START"
    step: int = 0
    retry_count: int = 0
    candidates: list[str] = field(default_factory=list)
    inspected: list[str] = field(default_factory=list)
    recommendation: str | None = None
    stop_reason: str | None = None


TERMINAL_STATES = {"COMPLETED", "FAILED", "NEEDS_HUMAN"}

VALID_TRANSITIONS = {
    "START": {"SEARCHING"},
    "SEARCHING": {"INSPECTING", "FAILED"},
    "INSPECTING": {"INSPECTING", "COMPARING", "FAILED"},
    "COMPARING": {"COMPLETED", "FAILED", "NEEDS_HUMAN"},
    "COMPLETED": set(),
    "FAILED": set(),
    "NEEDS_HUMAN": set(),
}


def validate_invariants(state: AgentState, max_steps: int, max_retries: int) -> None:
    # TODO: enforce step and retry budgets.
    # TODO: inspected suppliers must be a subset of candidates.
    # TODO: COMPLETED requires a recommendation.
    pass
