# Day 3: Tools and Function Calling

## Objective

By the end of Day 3, students should understand how tools differ from prompts, how to define explicit tool contracts, how model-selected actions are validated and dispatched, and how to build a multi-tool agent without an agent framework.

## Learning outcomes

Students will be able to:

- explain the role of tools in an agentic system;
- design narrow tool contracts with explicit inputs and outputs;
- represent tool calls as structured data;
- validate tool names and arguments before execution;
- build a tool registry and dispatcher;
- distinguish read-only, compute, and side-effecting tools;
- handle invalid calls, empty results, and tool failures;
- connect tool execution back into the agent loop from Day 1.

## Suggested session plan

1. Read [concepts.md](concepts.md).
2. Complete [Design Better Tools](exercises/design-tools.md).
3. Complete [Valid or Invalid Tool Call?](exercises/validate-tool-calls.md).
4. Implement [starter/tools.py](starter/tools.py).
5. Implement [starter/tool_router.py](starter/tool_router.py).
6. Compare against the reference implementation in [solution/](solution/).
7. Run the tests in [tests/](tests/).
8. Explore [failure-cases.md](failure-cases.md).
9. Build the [Multi-Tool Supplier Research Agent](project.md).

## Core architecture

```text
Goal
 ↓
Agent decision
 ↓
Structured tool call
 ↓
Argument validation
 ↓
Dispatcher
 ↓
Tool
 ↓
Observation
 ↓
State update
```

The model never receives unrestricted Python execution. It proposes a tool call. Application code decides whether that call is valid and executable.

## Run the reference implementation

From the repository root:

```bash
python day03-tool-use/solution/supplier_agent.py
python -m unittest discover day03-tool-use/tests -v
```
