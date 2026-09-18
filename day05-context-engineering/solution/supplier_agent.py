from context_data import SAMPLE_STATE
from context_manager import ContextManager


def choose_decision_type(state):
    status = state["status"]
    if status == "SEARCHING":
        return "SEARCH"
    if status == "INSPECTING":
        return "INSPECT"
    if status == "COMPARING":
        return "COMPARE"
    return "FINISH"


def main():
    manager = ContextManager()
    decision_type = choose_decision_type(SAMPLE_STATE)
    context = manager.build(SAMPLE_STATE, decision_type)

    print("Decision type:", decision_type)
    print("Selected context:")
    for key, value in context.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
