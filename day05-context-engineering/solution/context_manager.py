from __future__ import annotations

from typing import Any

MAX_CONTEXT_ITEMS = 8

TOOL_ROUTES = {
    "SEARCH": ["SEARCH_SUPPLIERS"],
    "INSPECT": ["INSPECT_SUPPLIER", "CHECK_CERTIFICATION"],
    "COMPARE": ["CALCULATE_LANDED_COST"],
    "FINISH": [],
}


class ContextManager:
    def latest_requirements(self, state: dict[str, Any]) -> dict[str, Any]:
        requirements = dict(state.get("requirements", {}))
        latest = {}

        for event in state.get("history", []):
            if event.get("type") == "requirement":
                field = event.get("field")
                version = event.get("version", 0)
                previous = latest.get(field)
                if previous is None or version >= previous["version"]:
                    latest[field] = {"value": event.get("value"), "version": version}

        for field, payload in latest.items():
            requirements[field] = payload["value"]

        return requirements

    def relevant_history(self, state: dict[str, Any], decision_type: str):
        allowed = {
            "SEARCH": {"requirement"},
            "INSPECT": {"requirement", "tool"},
            "COMPARE": {"requirement", "tool"},
            "FINISH": {"requirement", "tool"},
        }.get(decision_type, set())

        seen = set()
        result = []

        for event in state.get("history", []):
            if event.get("type") not in allowed:
                continue
            key = tuple(sorted(event.items()))
            if key in seen:
                continue
            seen.add(key)
            result.append(event)

        return result[-4:]

    def compress_inspected(self, inspected):
        if not inspected:
            return {"count": 0, "suppliers": []}
        best_price = min(item["unit_price"] for item in inspected)
        return {
            "count": len(inspected),
            "best_price": best_price,
            "suppliers": inspected,
        }

    def build(self, state: dict[str, Any], decision_type: str) -> dict[str, Any]:
        if decision_type not in TOOL_ROUTES:
            raise ValueError(f"Unknown decision type: {decision_type}")

        context = {
            "goal": state.get("goal"),
            "status": state.get("status"),
            "requirements": self.latest_requirements(state),
            "available_tools": TOOL_ROUTES[decision_type],
            "history": self.relevant_history(state, decision_type),
        }

        if decision_type == "SEARCH":
            context["candidate_count"] = len(state.get("candidates", []))
        elif decision_type == "INSPECT":
            context["candidates"] = state.get("candidates", [])
            context["inspected_ids"] = [item["id"] for item in state.get("inspected", [])]
        elif decision_type in {"COMPARE", "FINISH"}:
            context["evidence"] = self.compress_inspected(state.get("inspected", []))

        if len(context) > MAX_CONTEXT_ITEMS:
            raise ValueError("Context budget exceeded")

        return context
