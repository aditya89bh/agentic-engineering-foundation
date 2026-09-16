"""A framework-free CLI supplier research runtime for Day 1.

Stage A uses a deterministic policy. Day 1 later replaces only choose_action()
with an LLM policy while keeping validation, tool execution, state transitions,
and stopping conditions deterministic.
"""

from __future__ import annotations

import argparse
from typing import Any, Literal, TypedDict

MAX_STEPS = 8
VALID_ACTIONS = {"SEARCH", "INSPECT", "FINISH"}

SUPPLIERS = [
    {
        "id": "SUP-001",
        "name": "Apex Components",
        "product": "aluminum brackets",
        "unit_price": 480,
        "lead_days": 12,
        "quality_score": 4.5,
        "location": "Pune",
    },
    {
        "id": "SUP-002",
        "name": "Bharat Fabrication",
        "product": "aluminum brackets",
        "unit_price": 445,
        "lead_days": 9,
        "quality_score": 4.8,
        "location": "Ahmedabad",
    },
    {
        "id": "SUP-003",
        "name": "Omni Metalworks",
        "product": "aluminum brackets",
        "unit_price": 525,
        "lead_days": 6,
        "quality_score": 4.7,
        "location": "Chennai",
    },
    {
        "id": "SUP-004",
        "name": "Precision Industrial",
        "product": "steel brackets",
        "unit_price": 390,
        "lead_days": 7,
        "quality_score": 4.6,
        "location": "Mumbai",
    },
]


class Action(TypedDict, total=False):
    """Structured action proposed by the decision component."""

    name: Literal["SEARCH", "INSPECT", "FINISH"]
    supplier_id: str


State = dict[str, Any]
Observation = dict[str, Any]


def initial_state(component: str, max_unit_price: int) -> State:
    return {
        "goal": f"Find a supplier for {component} below ₹{max_unit_price}/unit.",
        "component": component.lower().strip(),
        "max_unit_price": max_unit_price,
        "step": 0,
        "candidates": [],
        "inspected": [],
        "history": [],
        "recommendation": None,
        "done": False,
        "stop_reason": None,
    }


def search_suppliers(component: str, max_unit_price: int) -> list[dict[str, Any]]:
    return [
        supplier
        for supplier in SUPPLIERS
        if component in supplier["product"].lower()
        and supplier["unit_price"] <= max_unit_price
    ]


def inspect_supplier(supplier_id: str) -> dict[str, Any] | None:
    return next(
        (supplier for supplier in SUPPLIERS if supplier["id"] == supplier_id),
        None,
    )


def choose_recommendation(inspected: list[dict[str, Any]]) -> dict[str, Any] | None:
    if not inspected:
        return None
    return min(
        inspected,
        key=lambda supplier: (
            -supplier["quality_score"],
            supplier["unit_price"],
            supplier["lead_days"],
        ),
    )


def choose_action(state: State) -> Action:
    """Deterministic Stage A policy: search, inspect each candidate, then finish."""
    has_searched = any(item["action"]["name"] == "SEARCH" for item in state["history"])
    if not has_searched:
        return {"name": "SEARCH"}

    inspected_ids = {supplier["id"] for supplier in state["inspected"]}
    for candidate in state["candidates"]:
        if candidate["id"] not in inspected_ids:
            return {"name": "INSPECT", "supplier_id": candidate["id"]}

    return {"name": "FINISH"}


def validate_action(action: dict[str, Any]) -> str | None:
    name = action.get("name")
    if name not in VALID_ACTIONS:
        return f"Action must be one of {sorted(VALID_ACTIONS)}; received {name!r}"
    if name == "INSPECT" and not action.get("supplier_id"):
        return "INSPECT requires a non-empty supplier_id"
    return None


def execute_action(action: Action, state: State) -> Observation:
    if action["name"] == "SEARCH":
        matches = search_suppliers(state["component"], state["max_unit_price"])
        return {"suppliers": matches, "count": len(matches)}

    if action["name"] == "INSPECT":
        supplier = inspect_supplier(action["supplier_id"])
        if supplier is None:
            return {"error": f"Supplier {action['supplier_id']!r} was not found"}
        return {"supplier": supplier}

    return {"finished": True}


def update_state(state: State, action: Action, observation: Observation) -> None:
    name = action["name"]

    if "error" in observation:
        state["done"] = True
        state["stop_reason"] = observation["error"]
    elif name == "SEARCH":
        state["candidates"] = observation["suppliers"]
    elif name == "INSPECT":
        supplier = observation["supplier"]
        if supplier["id"] not in {item["id"] for item in state["inspected"]}:
            state["inspected"].append(supplier)
    elif name == "FINISH":
        state["recommendation"] = choose_recommendation(state["inspected"])
        state["done"] = True
        state["stop_reason"] = (
            "Recommendation produced"
            if state["recommendation"]
            else "No suppliers matched the component and price constraints"
        )

    state["history"].append({"action": action, "observation": observation})


def run_agent(component: str, max_unit_price: int) -> State:
    state = initial_state(component, max_unit_price)
    print(f"Goal: {state['goal']}")

    while not state["done"] and state["step"] < MAX_STEPS:
        state["step"] += 1
        action = choose_action(state)
        print(f"\nStep {state['step']}/{MAX_STEPS}")
        print(f"  Action: {action}")

        validation_error = validate_action(action)
        if validation_error:
            state["done"] = True
            state["stop_reason"] = f"Invalid action: {validation_error}"
            state["history"].append(
                {"action": action, "observation": {"error": validation_error}}
            )
            print(f"  Error: {validation_error}")
            break

        observation = execute_action(action, state)
        print(f"  Observation: {observation}")
        update_state(state, action, observation)

    if not state["done"]:
        state["done"] = True
        state["stop_reason"] = f"Maximum step count ({MAX_STEPS}) reached"

    print("\nRun complete")
    print(f"  Stop reason: {state['stop_reason']}")
    if state["recommendation"]:
        supplier = state["recommendation"]
        print(
            "  Recommendation: "
            f"{supplier['name']} ({supplier['id']}) | "
            f"₹{supplier['unit_price']}/unit | "
            f"quality {supplier['quality_score']}/5 | "
            f"{supplier['lead_days']}-day lead time"
        )
    else:
        print("  Recommendation: none")

    return state


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Research mock component suppliers.")
    parser.add_argument("--component", default="aluminum brackets")
    parser.add_argument("--max-price", type=int, default=500)
    args = parser.parse_args()
    if args.max_price < 0:
        parser.error("--max-price must be zero or greater")
    return args


if __name__ == "__main__":
    cli_args = parse_args()
    run_agent(cli_args.component, cli_args.max_price)
