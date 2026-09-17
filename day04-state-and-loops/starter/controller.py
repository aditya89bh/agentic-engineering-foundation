from __future__ import annotations

from state import AgentState, TERMINAL_STATES, VALID_TRANSITIONS, validate_invariants

MAX_STEPS = 10
MAX_RETRIES = 2


def transition(state: AgentState, next_status: str) -> None:
    # TODO: reject transitions that are not in VALID_TRANSITIONS[state.status].
    # TODO: update state.status only after validation.
    pass


def run_agent(state: AgentState) -> AgentState:
    while state.status not in TERMINAL_STATES and state.step < MAX_STEPS:
        state.step += 1

        # TODO: implement a simple deterministic controller:
        # START -> SEARCHING
        # SEARCHING -> INSPECTING if candidates exist, else FAILED
        # INSPECTING -> INSPECTING while uninspected candidates remain
        # INSPECTING -> COMPARING when all candidates are inspected
        # COMPARING -> COMPLETED after selecting a recommendation

        validate_invariants(state, MAX_STEPS, MAX_RETRIES)

    if state.status not in TERMINAL_STATES:
        state.status = "FAILED"
        state.stop_reason = "Maximum step budget reached"

    return state
