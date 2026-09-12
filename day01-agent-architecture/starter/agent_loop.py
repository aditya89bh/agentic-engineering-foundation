"""Starter: a small, framework-free supplier research agent.

Run from the repository root:
    python day01-agent-architecture/starter/agent_loop.py
"""

MAX_STEPS = 8
VALID_ACTIONS = {"SEARCH", "INSPECT", "FINISH"}

SUPPLIERS = [
    {
        "id": "SUP-001",
        "name": "Apex Components",
        "product": "aluminum brackets",
        "unit_price": 480,
        "lead_days": 12,
    },
    {
        "id": "SUP-002",
        "name": "Bharat Fabrication",
        "product": "aluminum brackets",
        "unit_price": 445,
        "lead_days": 9,
    },
    {
        "id": "SUP-003",
        "name": "Precision Industrial",
        "product": "steel brackets",
        "unit_price": 390,
        "lead_days": 7,
    },
]


def initial_state():
    """Create all mutable state in one visible place."""
    return {
        "goal": "Find a supplier for aluminum brackets below ₹500/unit.",
        "component": "aluminum brackets",
        "max_unit_price": 500,
        "step": 0,
        "candidates": [],
        "inspected": [],
        "history": [],
        "recommendation": None,
        "done": False,
        "stop_reason": None,
    }


def choose_action(state):
    """Choose the next action from the current state.

    A later course version could isolate an LLM here. The controller and tools
    should remain deterministic.
    """
    if not state["candidates"]:
        return {"name": "SEARCH"}

    # TODO: Return INSPECT for a candidate that has not been inspected.
    # Hint: compare candidate IDs with records in state["inspected"].

    # TODO: Once enough evidence exists, select a recommendation before FINISH.
    return {"name": "FINISH"}


def execute_action(action, state):
    """Execute one allowed action and return an observation."""
    if action["name"] == "SEARCH":
        # TODO: Filter SUPPLIERS by component and max_unit_price.
        return {"suppliers": list(SUPPLIERS)}

    if action["name"] == "INSPECT":
        # TODO: Look up action["supplier_id"] and return its full record.
        return {"error": "INSPECT is not implemented yet"}

    if action["name"] == "FINISH":
        return {"finished": True}

    return {"error": "Unknown action"}


def update_state(state, action, observation):
    """Apply an observation to state."""
    if action["name"] == "SEARCH":
        state["candidates"] = observation.get("suppliers", [])
    elif action["name"] == "INSPECT" and "supplier" in observation:
        state["inspected"].append(observation["supplier"])
    elif action["name"] == "FINISH":
        state["done"] = True
        state["stop_reason"] = "Policy selected FINISH"

    state["history"].append({"action": action, "observation": observation})
    return state


def run_agent():
    state = initial_state()
    print(f"Goal: {state['goal']}")

    while not state["done"] and state["step"] < MAX_STEPS:
        state["step"] += 1
        action = choose_action(state)
        print(f"Step {state['step']}: {action}")

        if action.get("name") not in VALID_ACTIONS:
            state["done"] = True
            state["stop_reason"] = f"Invalid action: {action}"
            break

        observation = execute_action(action, state)
        print(f"  Observation: {observation}")
        state = update_state(state, action, observation)

    if not state["done"]:
        state["done"] = True
        state["stop_reason"] = f"Maximum of {MAX_STEPS} steps reached"

    print(f"Stopped: {state['stop_reason']}")
    print(f"Recommendation: {state['recommendation'] or 'Not available yet'}")
    return state


if __name__ == "__main__":
    run_agent()
