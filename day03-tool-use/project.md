# Mini-Project: Multi-Tool Supplier Research Agent

Extend the Day 1 and Day 2 system so the agent can safely use multiple tools.

## Pipeline

```text
Natural-language request
        ↓
Requirement schema
        ↓
Agent runtime
        ↓
Tool selection
        ↓
Tool dispatcher
        ↓
Observation
        ↓
State update
        ↓
Next tool / finish
```

## Required tools

- `SEARCH_SUPPLIERS`
- `INSPECT_SUPPLIER`
- `CALCULATE_LANDED_COST`

Optional extensions:

- `CHECK_CERTIFICATION`
- `CHECK_INVENTORY`

## Required engineering properties

Your project should include:

- a tool registry;
- explicit tool contracts;
- structured tool calls;
- argument validation;
- a dispatcher;
- read-only vs compute classification;
- error handling;
- unknown-tool rejection;
- tool result logging;
- at least three tools;
- at least ten tests across normal and failure paths.

## Acceptance checks

Demonstrate that:

1. valid tool calls execute successfully;
2. unknown tools are rejected before execution;
3. missing and malformed arguments are rejected;
4. an invalid supplier ID is handled clearly;
5. empty search results do not crash the runtime;
6. landed cost is computed deterministically;
7. repeated calls can be identified from history;
8. the agent cannot call a tool outside its allowed registry.

## Reflection

In your pull request, explain:

1. why the model should propose a tool call rather than execute arbitrary code;
2. which tools are safe to expose automatically;
3. which tools would require approval if connected to a real procurement system;
4. whether a failure came from tool selection, validation, execution, or observation handling.

## Bridge to Day 4

By the end of Day 3, the agent can understand requirements, choose capabilities, execute them, and process observations. Day 4 makes the execution path itself explicit through state machines, branches, retries, and terminal states.
