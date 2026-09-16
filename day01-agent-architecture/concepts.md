# Day 1 Concepts

## 1. LLM vs workflow vs agent

An **LLM application** calls a model to transform input into output. A summarizer that sends one document and returns one summary is an LLM application; it has no multi-step control loop.

A **deterministic workflow** follows a path written in code. Given the same state, it selects the same next step. An invoice system might validate fields, look up a purchase order, route by amount, and request approval.

An **agent** is a goal-directed system that repeatedly observes state, chooses among available actions, acts on an environment, and adapts later actions based on what it observes. In modern AI agents, one or more of those decisions are typically delegated to a learned model.

A **hybrid** places bounded model-driven choices inside deterministic control flow. Most production systems are hybrids: a model resolves ambiguity while code validates actions, controls access, executes tools, preserves state, and enforces limits.

```text
Single LLM call:  input ──► model ──► output

Workflow:         input ──► step A ──► step B ──► output
                                └── fixed branches ──┘

Agent:            goal ──► [observe → choose → act]
                                  ▲             │
                                  └── state ◄───┘
                                         │
                                      stopping
```

A system can choose actions dynamically without being an AI agent. The engineering question is whether a goal-directed controller adapts its actions from observations, and whether a learned model participates in ambiguous decisions.

## 2. Anatomy of an agent

| Part | Engineering question | Supplier example |
| --- | --- | --- |
| Goal | What outcome defines success? | Recommend an aluminum-bracket supplier below ₹500/unit |
| Model / policy | What component handles ambiguous judgment? | Deterministic policy first; LLM policy second |
| Context | What information is available for this decision? | Goal, tool results, constraints, and action history |
| State | What changes and must survive between steps? | Candidates, inspected records, step count, recommendation |
| Tools | What actions may the controller request? | Search and inspect |
| Environment | Where do actions have effects and observations arise? | Mock supplier catalog; later, real databases or APIs |
| Policy / constraints | What actions and outcomes are allowed? | Valid action names, ₹500 cap, approval before contacting vendors |
| Stopping condition | When must execution end? | Recommendation produced, no candidates, or maximum steps reached |

Keep these parts explicit. A dictionary is enough for a first state representation:

```python
state = {
    "goal": "Find aluminum brackets below ₹500/unit",
    "step": 0,
    "candidates": [],
    "inspected": [],
    "recommendation": None,
    "done": False,
}
```

## 3. An agent is a software system

The model is one component, not the entire agent. The surrounding system owns validation, authentication, persistence, tool execution, logging, retries, budgets, approvals, and failure handling.

```text
                    ┌──────── policy / constraints ────────┐
user goal ──► controller ──► decision component ──► action │
                 ▲                              │           │
                 │                              ▼           │
               state ◄──── observation ◄──── environment   │
                 └──────── logs / limits / approvals ──────┘
```

This separation makes the system testable. You can replace a model decision with a fixed action in a unit test, or replace a real tool with mock data.

## 4. The execution loop

The minimal loop is **observe → decide → validate → act → update → check**:

```python
while not state["done"] and state["step"] < MAX_STEPS:
    action = choose_action(state)       # deterministic or model-driven
    validate_action(action)             # deterministic safety boundary
    observation = execute(action)       # deterministic tool boundary
    update_state(state, action, observation)
    state["step"] += 1
```

The decision component can change without changing the rest of the runtime.

## 5. Actions and observations

An **action** is a structured request from the decision component to the environment. An **observation** is the environment's result.

```python
from typing import Literal, TypedDict

class Action(TypedDict, total=False):
    name: Literal["SEARCH", "INSPECT", "FINISH"]
    supplier_id: str
```

Example values:

```python
action = {"name": "INSPECT", "supplier_id": "SUP-002"}
observation = {"found": True, "unit_price": 445, "lead_days": 9}
```

Treat actions and observations as data with known shapes. Do not let free-form model text directly trigger arbitrary code or shell commands.

## 6. Agent state

State is the durable record needed for the next decision. It may contain facts, progress, history, budgets, and terminal status. Context is what you select from that state, plus other sources, for a particular decision.

Useful state invariants include:

- `0 <= step <= MAX_STEPS`
- every inspected supplier came from search results;
- `done` is true when a terminal condition has been reached;
- an action history entry is appended exactly once per executed step.

State should be inspectable. Hidden state makes failures difficult to reproduce.

## 7. Deterministic vs agentic decisions

Use a model when the input is ambiguous: interpreting “suitable,” choosing which candidate deserves more research, or synthesizing tradeoffs. Use deterministic code when the rule is certain: validating an action name, comparing a numeric price, checking permission, or enforcing `MAX_STEPS`.

```python
# Ambiguous: a model may weigh these tradeoffs.
best_candidate = choose_candidate(price, lead_time, quality_notes)

# Certain: code enforces the hard budget.
eligible = candidate["unit_price"] <= max_unit_price
```

> **Use models for ambiguity. Use deterministic software for certainty.**

## 8. Control flow

Control flow answers which component owns the next transition. In a workflow, the program usually owns it. In an agent, a policy or model chooses from allowed actions, but the controller still validates and executes that choice.

```text
START
  │
  ▼
SEARCH ── no results ─────────────► FINISH(no match)
  │ results
  ▼
INSPECT ── more candidates ───────► INSPECT
  │ enough evidence
  ▼
FINISH(recommendation)
```

The available actions define the capability boundary. Narrow, typed actions are easier to test and secure.

## 9. Stopping conditions

Every loop needs both success and safety stops:

- a recommendation has enough evidence;
- search returned no candidates;
- a human rejected or cancelled the task;
- the time, cost, or step budget was exhausted;
- an unrecoverable error occurred.

`MAX_STEPS` is a safety net, not the definition of success. Reaching it should produce a clear incomplete result rather than pretending the goal was achieved.

## 10. Autonomy spectrum

Autonomy is not binary.

```text
manual ── assistive ── approval-gated ── bounded autonomous ── open-ended
          draft only     asks before       acts inside strict     broad action
                         side effects       tools and limits       authority
```

Choose the least autonomy that achieves the goal. A research agent may search and rank automatically but require human approval before emailing a supplier, spending money, or changing a system of record.

## 11. Stage A vs Stage B

Day 1 uses the same runtime twice.

### Stage A: deterministic policy

```text
state → Python policy → action → validator → tool → observation
```

This is intentionally closer to a stateful controller than a learned AI agent. Its purpose is to expose the mechanics clearly.

### Stage B: LLM policy

```text
state → LLM policy → JSON action → validator → tool → observation
```

Only the decision component changes. The LLM does not execute tools directly, mutate state directly, or bypass stopping rules.

This comparison is the technical lesson: **agent engineering is the design of the entire execution system, not merely the model prompt.**

## Design checklist

Before implementing an agent, answer:

1. What exact state is passed between steps?
2. What actions are allowed, and how are arguments validated?
3. Which decisions genuinely require ambiguity handling?
4. What does the environment return for each action?
5. What are the success, failure, and safety stopping conditions?
6. Which side effects require human approval?
7. What logs make a bad transition reproducible?
8. What happens if the model returns malformed or invalid output?
