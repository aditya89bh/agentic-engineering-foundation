# Day 1: Agent Architecture and the Execution Loop

## Objective

By the end of Day 1, you should understand what makes a system agentic and be able to build a simple agent loop in Python without an agent framework.

## Learning outcomes

You will be able to:

- classify an LLM application, workflow, agent, or hybrid system;
- identify the goal, model, context, state, tools, environment, policy, and stopping condition;
- trace actions and observations through an execution loop;
- separate ambiguous decisions from deterministic enforcement;
- implement and debug a bounded command-line agent.

## Suggested session plan

1. Read [concepts.md](concepts.md).
2. Complete [Agent or Not?](exercises/agent-or-workflow.md).
3. Complete [Design an Agent on Paper](exercises/design-an-agent.md).
4. Implement the TODOs in [starter/agent_loop.py](starter/agent_loop.py).
5. Test failure paths using [failure-cases.md](failure-cases.md).
6. Compare with [solution/agent_loop.py](solution/agent_loop.py).
7. Build the [CLI Supplier Research Agent](project.md).

## Run the examples

From the repository root:

```bash
python day01-agent-architecture/starter/agent_loop.py
python day01-agent-architecture/solution/agent_loop.py
```

No network connection, API key, or external framework is required.
