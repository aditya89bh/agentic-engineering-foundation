class ContextManager:
    def build(self, state, requirements, decision_type, memories=None):
        context = {
            "goal": {
                "component": requirements.component,
                "quantity": requirements.quantity,
                "max_unit_price": requirements.max_unit_price,
                "max_lead_days": requirements.max_lead_days,
                "certification": requirements.certification,
            },
            "status": state.status,
        }

        if decision_type == "SEARCH":
            context["available_tools"] = ["SEARCH_SUPPLIERS"]
        elif decision_type == "INSPECT":
            context["available_tools"] = ["INSPECT_SUPPLIER", "CHECK_CERTIFICATION"]
            context["candidates"] = state.candidates
        elif decision_type == "COMPARE":
            context["available_tools"] = ["CALCULATE_LANDED_COST"]
            context["inspected"] = state.inspected
        elif decision_type == "FINISH":
            context["available_tools"] = []
            context["recommendation"] = state.recommendation

        if memories:
            context["relevant_memory"] = memories

        return context
