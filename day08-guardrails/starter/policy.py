from dataclasses import dataclass


@dataclass
class PolicyDecision:
    result: str
    reason: str
    required_role: str | None = None


class PolicyEngine:
    def evaluate(self, action, actor_role, state):
        # TODO 1: classify the action
        # TODO 2: enforce role permissions
        # TODO 3: enforce supplier inspection requirements
        # TODO 4: apply value thresholds
        # TODO 5: return ALLOW, DENY, or REQUIRE_APPROVAL
        raise NotImplementedError
