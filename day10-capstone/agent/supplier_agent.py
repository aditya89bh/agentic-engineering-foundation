from pathlib import Path
import sys

BASE = Path(__file__).resolve().parents[1]
for p in [BASE, BASE/"tools", BASE/"context", BASE/"memory", BASE/"reliability", BASE/"governance"]:
    sys.path.insert(0, str(p))

from requirements import SupplierRequirement
from state import AgentState
from search import search_suppliers
from inspect import inspect_supplier
from cost import calculate_landed_cost
from context_manager import ContextManager
from memory_store import MemoryStore
from audit import AuditLog


def run_agent(requirements: SupplierRequirement):
    requirements.validate()
    state = AgentState()
    context_manager = ContextManager()
    memory = MemoryStore()
    audit = AuditLog()

    state.transition("SEARCHING")
    state.step += 1
    context_manager.build(state, requirements, "SEARCH")
    state.candidates = search_suppliers(requirements.component, requirements.max_unit_price)

    if not state.candidates:
        state.transition("FAILED")
        state.stop_reason = "No eligible suppliers"
        return state, audit.entries

    state.transition("INSPECTING")
    for candidate in state.candidates:
        state.step += 1
        state.inspected.append(inspect_supplier(candidate["id"]))

    state.transition("COMPARING")
    eligible = [
        s for s in state.inspected
        if (requirements.max_lead_days is None or s["lead_days"] <= requirements.max_lead_days)
        and (requirements.certification is None or s["certification"] == requirements.certification)
    ]

    if not eligible:
        state.transition("FAILED")
        state.stop_reason = "No supplier satisfies all constraints"
        return state, audit.entries

    best = min(eligible, key=lambda s: s["unit_price"])
    best["landed_cost"] = calculate_landed_cost(best["unit_price"], requirements.quantity)
    state.recommendation = best
    memory.write(best["id"], "decision", "Selected as best eligible supplier", "capstone")
    audit.record("RECOMMENDATION", best)

    state.transition("COMPLETED")
    state.stop_reason = "Best eligible supplier selected"
    return state, audit.entries


def main():
    req = SupplierRequirement(
        component="aluminum brackets",
        quantity=100,
        max_unit_price=500,
        max_lead_days=14,
        certification="ISO 9001",
    )
    state, audit = run_agent(req)
    print("Status:", state.status)
    print("Recommendation:", state.recommendation)
    print("Audit entries:", len(audit))


if __name__ == "__main__":
    main()
