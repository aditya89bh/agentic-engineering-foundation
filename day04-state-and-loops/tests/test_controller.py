from __future__ import annotations

import sys
import unittest
from pathlib import Path

SOLUTION = Path(__file__).resolve().parents[1] / "solution"
sys.path.insert(0, str(SOLUTION))

from controller import run_agent, MAX_STEPS
from state import AgentState


class ControllerTests(unittest.TestCase):
    def test_successful_run_completes(self):
        state = AgentState(goal="x", candidates=["SUP-001", "SUP-002"])
        result = run_agent(state)
        self.assertEqual(result.status, "COMPLETED")
        self.assertIsNotNone(result.recommendation)

    def test_empty_search_path_fails(self):
        state = AgentState(goal="x", candidates=[])
        result = run_agent(state)
        self.assertEqual(result.status, "FAILED")
        self.assertIn("No eligible suppliers", result.stop_reason)

    def test_all_candidates_are_inspected_before_completion(self):
        state = AgentState(goal="x", candidates=["SUP-001", "SUP-002", "SUP-003"])
        result = run_agent(state)
        self.assertEqual(set(result.inspected), set(result.candidates))

    def test_terminal_run_stays_within_budget(self):
        state = AgentState(goal="x", candidates=["SUP-001"])
        result = run_agent(state)
        self.assertLessEqual(result.step, MAX_STEPS)


if __name__ == "__main__":
    unittest.main()
