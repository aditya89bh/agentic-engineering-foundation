from context_data import SAMPLE_STATE

MAX_CONTEXT_ITEMS = 8

TOOL_ROUTES = {
    "SEARCH": ["SEARCH_SUPPLIERS"],
    "INSPECT": ["INSPECT_SUPPLIER", "CHECK_CERTIFICATION"],
    "COMPARE": ["CALCULATE_LANDED_COST"],
    "FINISH": [],
}


class ContextManager:
    def build(self, state, decision_type):
        # TODO 1: include goal and current requirements
        # TODO 2: route only tools relevant to decision_type
        # TODO 3: include only information needed for the decision
        # TODO 4: remove irrelevant history
        # TODO 5: enforce MAX_CONTEXT_ITEMS
        return {}


if __name__ == "__main__":
    manager = ContextManager()
    print(manager.build(SAMPLE_STATE, "COMPARE"))
