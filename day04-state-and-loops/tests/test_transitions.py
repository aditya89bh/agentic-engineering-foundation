from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

SOLUTION = Path(__file__).resolve().parents[1] / "solution"
sys.path.insert(0, str(SOLUTION))

from state import AgentState, validate_invariants
from controller import transition, MAX_RETRIES, MAX_STEPS


class TransitionTests(unittest.TestCase):
    def test_valid_transition(self):
        state = AgentState(goal="x")
        transition(state, "SEARCHING")
        self.assertEqual(state.status, "SEARCHING")

    def test_invalid_transition_rejected(self):
        state = AgentState(goal="x")
        with self.assertRaises(ValueError):
            transition(state, "COMPARING")

    def test_terminal_state_cannot_transition(self):
        state = AgentState(goal="x", status="COMPLETED", recommendation="SUP-001")
        with self.assertRaises(ValueError):
            transition(state, "SEARCHING")

    def test_completed_requires_recommendation(self):
        state = AgentState(goal="x", status="COMPLETED")
        with self.assertRaises(ValueError):
            validate_invariants(state, MAX_STEPS, MAX_RETRIES)

    def test_inspected_must_be_candidate(self):
        state = AgentState(goal="x", candidates=["SUP-001"], inspected=["SUP-999"])
        with self.assertRaises(ValueError):
            validate_invariants(state, MAX_STEPS, MAX_RETRIES)


if __name__ == "__main__":
    unittest.main()
