from __future__ import annotations

from state import AgentState, TERMINAL_STATES, VALID_TRANSITIONS, validate_invariants

MAX_STEPS = 10
MAX_RETRIES = 2


def transition(state: AgentState, next_status: str) -> None:
    allowed = VALID_TRANSITIONS[state.status]
    if next_status not in allowed:
        raise ValueError(f"Invalid transition: {state.status} -> {next_status}")
    state.status = next_status


def run_agent(state: AgentState) -> AgentState:
    while state.status not in TERMINAL_STATES and state.step < MAX_STEPS:
        state.step += 1

        if state.status == "START":
            transition(state, "SEARCHING")

        elif state.status == "SEARCHING":
            if state.candidates:
                transition(state, "INSPECTING")
            else:
                transition(state, "FAILED")
                state.stop_reason = "No eligible suppliers"

        elif state.status == "INSPECTING":
            remaining = [x for x in state.candidates if x not in state.inspected]
            if remaining:
                state.inspected.append(remaining[0])
                if len(state.inspected) < len(state.candidates):
                    transition(state, "INSPECTING")
                else:
                    transition(state, "COMPARING")
            else:
                transition(state, "COMPARING")

        elif state.status == "COMPARING":
            if not state.inspected:
                transition(state, "FAILED")
                state.stop_reason = "No inspected suppliers"
            else:
                state.recommendation = state.inspected[0]
                transition(state, "COMPLETED")
                state.stop_reason = "Recommendation produced"

        validate_invariants(state, MAX_STEPS, MAX_RETRIES)

    if state.status not in TERMINAL_STATES:
        state.status = "FAILED"
        state.stop_reason = "Maximum step budget reached"

    return state
