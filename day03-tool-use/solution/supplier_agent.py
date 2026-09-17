"""Simple multi-tool supplier research agent for Day 3."""

from tool_router import dispatch_tool


def run_agent():
    state = {
        "goal": "Find an aluminum bracket supplier below ₹500 and calculate landed cost.",
        "candidates": [],
        "inspected": [],
        "landed_costs": {},
        "history": [],
        "done": False,
    }

    calls = [
        {
            "name": "SEARCH_SUPPLIERS",
            "arguments": {"component": "aluminum brackets", "max_unit_price": 500},
        }
    ]

    while calls and not state["done"]:
        call = calls.pop(0)
        result = dispatch_tool(call)
        state["history"].append({"call": call, "result": result})

        if call["name"] == "SEARCH_SUPPLIERS":
            state["candidates"] = result
            for supplier in result:
                calls.append({
                    "name": "INSPECT_SUPPLIER",
                    "arguments": {"supplier_id": supplier["id"]},
                })

        elif call["name"] == "INSPECT_SUPPLIER":
            state["inspected"].append(result)
            calls.append({
                "name": "CALCULATE_LANDED_COST",
                "arguments": {
                    "unit_price": result["unit_price"],
                    "shipping": result["shipping"],
                },
            })

        elif call["name"] == "CALCULATE_LANDED_COST":
            supplier = state["inspected"][len(state["landed_costs"])]
            state["landed_costs"][supplier["id"]] = result["landed_cost"]
            if len(state["landed_costs"]) == len(state["candidates"]):
                state["done"] = True

    print("Tool trace:")
    for item in state["history"]:
        print(item)

    print("\nLanded costs:")
    print(state["landed_costs"])
    return state


if __name__ == "__main__":
    run_agent()
