# Day 1: Agent Architecture and the Execution Loop

## Objective

By the end of Day 1, you should understand what makes a system agentic and be able to build a bounded agent runtime in Python, then replace its deterministic decision policy with an LLM while keeping validation, tools, state updates, and stopping rules under application control.

## Learning outcomes

You will be able to:

- classify an LLM application, workflow, agent, or hybrid system;
- identify the goal, model, context, state, tools, environment, policy, and stopping condition;
- trace actions and observations through an execution loop;
- separate ambiguous decisions from deterministic enforcement;
- implement and debug a bounded command-line agent runtime;
- test core agent behavior with repeatable unit tests;
- replace a deterministic policy with an LLM without giving the model unrestricted execution authority.

## Two-stage build

Day 1 deliberately separates the runtime from the model.

### Stage A: deterministic runtime

Build and understand:

```text
state → policy → action → validation → tool → observation → state
```

The policy is deterministic so you can debug the execution architecture without model variability.

### Stage B: LLM policy

Keep the runtime unchanged and replace only the decision component:

```text
state → LLM → action → validation → tool → observation → state
```

This demonstrates a core engineering idea: the LLM is a replaceable decision component inside a larger controlled system.

## Suggested session plan

1. Read [concepts.md](concepts.md).
2. Complete [Agent or Not?](exercises/agent-or-workflow.md).
3. Complete [Design an Agent on Paper](exercises/design-an-agent.md).
4. Implement the TODOs in [starter/agent_loop.py](starter/agent_loop.py).
5. Compare with the deterministic reference in [solution/agent_loop.py](solution/agent_loop.py).
6. Run the unit tests in [tests/](tests/).
7. Test failure paths using [failure-cases.md](failure-cases.md).
8. Run the optional model-driven version in [solution/llm_agent_loop.py](solution/llm_agent_loop.py).
9. Build the [CLI Supplier Research Agent](project.md).

## Run the deterministic examples

From the repository root:

```bash
python day01-agent-architecture/starter/agent_loop.py
python day01-agent-architecture/solution/agent_loop.py
python -m unittest discover day01-agent-architecture/tests -v
```

These require no network connection or API key.

## Run the optional LLM policy

Install the small Day 1 optional dependency:

```bash
python -m pip install -r day01-agent-architecture/requirements-llm.txt
```

Then configure an API key and a model available to your account:

```bash
export OPENAI_API_KEY="..."
export OPENAI_MODEL="your-model-name"
python day01-agent-architecture/solution/llm_agent_loop.py
```

The LLM version intentionally asks the model for plain JSON and validates it in Python. Day 2 will show how structured outputs and schemas improve this boundary.
