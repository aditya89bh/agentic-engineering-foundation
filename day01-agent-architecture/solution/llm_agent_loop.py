"""Stage B: use an LLM only to propose the next action.

The runtime still owns validation, tool execution, state updates, and stopping.
This example intentionally parses plain JSON so Day 2 can later demonstrate why
schema-constrained structured outputs are a stronger interface.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any

from openai import OpenAI

# Reuse the deterministic runtime implementation rather than duplicating tools
# and state logic.
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import agent_loop as runtime  # noqa: E402


def compact_state(state: runtime.State) -> dict[str, Any]:
    """Expose only the information needed for the next decision."""
    return {
        "goal": state["goal"],
        "step": state["step"],
        "candidates": state["candidates"],
        "inspected": state["inspected"],
        "history": state["history"],
    }


def choose_action_with_llm(
    state: runtime.State,
    client: OpenAI,
    model: str,
) -> dict[str, Any]:
    """Ask the model to propose exactly one next action."""
    prompt = f"""
You are the decision component inside a bounded supplier-research agent.

Available actions:
- SEARCH
- INSPECT, with supplier_id
- FINISH

Rules:
1. Search before inspecting.
2. Inspect available candidates before finishing.
3. Never invent supplier IDs.
4. Return only one JSON object.
5. Valid shapes are:
   {{"name":"SEARCH"}}
   {{"name":"INSPECT","supplier_id":"SUP-001"}}
   {{"name":"FINISH"}}

Current state:
{json.dumps(compact_state(state), ensure_ascii=False)}
""".strip()

    response = client.responses.create(model=model, input=prompt)
    raw = response.output_text.strip()

    try:
        action = json.loads(raw)
    except json.JSONDecodeError as exc:
        return {
            "name": "__INVALID__",
            "parse_error": f"Model returned invalid JSON: {exc}",
            "raw_output": raw,
        }

    if not isinstance(action, dict):
        return {
            "name": "__INVALID__",
            "parse_error": "Model output must be a JSON object",
            "raw_output": raw,
        }

    return action


def run_llm_agent(component: str = "aluminum brackets", max_unit_price: int = 500):
    model = os.environ.get("OPENAI_MODEL")
    if not model:
        raise RuntimeError(
            "Set OPENAI_MODEL to a model available to your API account."
        )

    client = OpenAI()
    state = runtime.initial_state(component, max_unit_price)
    print(f"Goal: {state['goal']}")

    while not state["done"] and state["step"] < runtime.MAX_STEPS:
        state["step"] += 1
        action = choose_action_with_llm(state, client, model)

        print(f"\nStep {state['step']}/{runtime.MAX_STEPS}")
        print(f"  Proposed action: {action}")

        validation_error = runtime.validate_action(action)
        if validation_error:
            state["done"] = True
            state["stop_reason"] = f"Invalid model action: {validation_error}"
            state["history"].append(
                {"action": action, "observation": {"error": validation_error}}
            )
            print(f"  Rejected: {validation_error}")
            break

        observation = runtime.execute_action(action, state)
        print(f"  Observation: {observation}")
        runtime.update_state(state, action, observation)

    if not state["done"]:
        state["done"] = True
        state["stop_reason"] = (
            f"Maximum step count ({runtime.MAX_STEPS}) reached"
        )

    print("\nRun complete")
    print(f"  Stop reason: {state['stop_reason']}")
    print(f"  Recommendation: {state['recommendation'] or 'none'}")
    return state


if __name__ == "__main__":
    run_llm_agent()
