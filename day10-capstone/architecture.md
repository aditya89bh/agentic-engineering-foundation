# Capstone Architecture

```text
User Request
     ↓
Requirement Extraction
     ↓
Structured Schema
     ↓
Agent State Machine
     ↓
Context Manager
     ↓
Decision Policy
     ↓
Tool Selection
     ↓
Policy Check
     ↓
Tool Execution
     ↓
Observation
     ↓
State Update
     ↓
Memory Read / Write
     ↓
Evaluation Trace
```

## Required contracts

- SupplierRequirement
- ToolCall
- ToolResult
- AgentState
- MemoryRecord
- PolicyDecision
- EvaluationResult

## Required states

- START
- SEARCHING
- INSPECTING
- COMPARING
- WAITING_FOR_APPROVAL
- COMPLETED
- FAILED
- NEEDS_HUMAN

## Required tools

- SEARCH_SUPPLIERS
- INSPECT_SUPPLIER
- CALCULATE_LANDED_COST

Recommended:

- CHECK_CERTIFICATION
- CREATE_PURCHASE_ORDER
