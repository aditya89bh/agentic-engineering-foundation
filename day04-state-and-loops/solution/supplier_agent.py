from __future__ import annotations

from controller import run_agent
from state import AgentState


def main() -> None:
    state = AgentState(
        goal="Find the best eligible supplier",
        candidates=["SUP-001", "SUP-002", "SUP-004"],
    )

    result = run_agent(state)

    print(f"Status: {result.status}")
    print(f"Steps: {result.step}")
    print(f"Inspected: {result.inspected}")
    print(f"Recommendation: {result.recommendation}")
    print(f"Stop reason: {result.stop_reason}")


if __name__ == "__main__":
    main()
