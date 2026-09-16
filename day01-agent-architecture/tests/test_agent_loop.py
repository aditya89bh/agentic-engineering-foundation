"""Repeatable tests for the Day 1 deterministic runtime."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch

MODULE_PATH = (
    Path(__file__).resolve().parents[1] / "solution" / "agent_loop.py"
)
SPEC = importlib.util.spec_from_file_location("day01_agent_loop", MODULE_PATH)
agent = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(agent)


class AgentLoopTests(unittest.TestCase):
    def test_search_returns_only_eligible_suppliers(self):
        matches = agent.search_suppliers("aluminum brackets", 500)
        self.assertEqual({item["id"] for item in matches}, {"SUP-001", "SUP-002"})

    def test_no_match_stops_cleanly(self):
        state = agent.run_agent("titanium gears", 100)
        self.assertTrue(state["done"])
        self.assertIsNone(state["recommendation"])
        self.assertIn("No suppliers matched", state["stop_reason"])

    def test_invalid_action_is_rejected(self):
        self.assertIsNotNone(agent.validate_action({"name": "EMAIL"}))
        self.assertIsNotNone(agent.validate_action({"name": "INSPECT"}))

    def test_repeated_inspection_does_not_duplicate_state(self):
        state = agent.initial_state("aluminum brackets", 500)
        supplier = agent.SUPPLIERS[0]
        observation = {"supplier": supplier}
        action = {"name": "INSPECT", "supplier_id": supplier["id"]}

        agent.update_state(state, action, observation)
        agent.update_state(state, action, observation)

        self.assertEqual(len(state["inspected"]), 1)

    def test_runtime_never_exceeds_max_steps(self):
        with patch.object(agent, "choose_action", return_value={"name": "SEARCH"}):
            state = agent.run_agent("aluminum brackets", 500)

        self.assertEqual(state["step"], agent.MAX_STEPS)
        self.assertIn("Maximum step count", state["stop_reason"])


if __name__ == "__main__":
    unittest.main()
