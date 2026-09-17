from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
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


def validate_invariants(state: AgentState, max_steps: int, max_retries: int) -> None:
    if state.step > max_steps:
        raise ValueError("step budget exceeded")
    if state.retry_count > max_retries:
        raise ValueError("retry budget exceeded")
    if not set(state.inspected).issubset(set(state.candidates)):
        raise ValueError("inspected suppliers must be candidates")
    if state.status == "COMPLETED" and not state.recommendation:
        raise ValueError("COMPLETED requires a recommendation")


def save_state(state: AgentState, path: str | Path) -> None:
    Path(path).write_text(json.dumps(asdict(state), indent=2), encoding="utf-8")


def load_state(path: str | Path) -> AgentState:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return AgentState(**data)
