# Day 3 Concepts

## 1. What is a tool?

A tool is a callable capability exposed to the agent. Examples include searching suppliers, inspecting a supplier, calculating landed cost, checking inventory, or querying a database.

```text
User Goal
   ↓
Agent
   ↓
Choose Tool
   ↓
Validate Arguments
   ↓
Execute Tool
   ↓
Return Observation
   ↓
Agent Continues
```

A prompt asks a model to reason. A tool lets the system retrieve information or act on an environment.

## 2. Tool contracts

Every tool should define:

- name;
- purpose;
- input arguments;
- argument types;
- required fields;
- return shape;
- expected errors;
- side effects.

Example:

```python
def search_suppliers(component: str, max_unit_price: float) -> list[dict]:
    ...
```

Narrow tools are easier to validate, test, secure, and explain.

## 3. Tool schemas

A tool invocation is structured data:

```json
{
  "name": "INSPECT_SUPPLIER",
  "arguments": {
    "supplier_id": "SUP-002"
  }
}
```

The tool call should be validated before execution.

```text
Model output
    ↓
Tool-call schema
    ↓
Argument validation
    ↓
Dispatcher
    ↓
Function
```

## 4. Tool registry

Instead of a large conditional tree, keep tools in a registry:

```python
TOOLS = {
    "SEARCH_SUPPLIERS": search_suppliers,
    "INSPECT_SUPPLIER": inspect_supplier,
    "CALCULATE_LANDED_COST": calculate_landed_cost,
}
```

The registry makes capability boundaries visible and testable.

## 5. Dispatcher

The dispatcher is a controlled execution boundary:

```python
def dispatch_tool(call):
    if call.name not in TOOLS:
        raise InvalidToolError()
    return TOOLS[call.name](**call.arguments)
```

The model proposes a tool name and arguments. The application decides whether execution is allowed.

## 6. Tool selection

For the supplier agent, expose:

- `SEARCH_SUPPLIERS`
- `INSPECT_SUPPLIER`
- `CALCULATE_LANDED_COST`

Example execution:

```text
SEARCH_SUPPLIERS
      ↓
SUP-001, SUP-002
      ↓
INSPECT_SUPPLIER(SUP-002)
      ↓
base price = ₹445
      ↓
CALCULATE_LANDED_COST
      ↓
₹487
      ↓
FINISH
```

## 7. Tool results are observations

Prefer explicit results:

```python
{
    "supplier_id": "SUP-002",
    "unit_price": 445,
    "shipping": 42,
}
```

Then update agent state separately. Do not let tools mutate unrelated state silently.

## 8. Failure categories

Students should distinguish:

```text
Invalid Tool Call
Tool Execution Failure
Valid Empty Result
Successful Result
```

These have different recovery paths.

## 9. Read-only, compute, and side-effecting tools

Read-only:

- `SEARCH_SUPPLIERS`
- `INSPECT_SUPPLIER`
- `CHECK_INVENTORY`

Compute:

- `CALCULATE_LANDED_COST`

Side-effecting:

- `EMAIL_SUPPLIER`
- `CREATE_PURCHASE_ORDER`
- `UPDATE_DATABASE`

Tool access is capability access. More tools mean more power and more risk.

## 10. Permissions

A simple permission map can make capabilities explicit:

```python
TOOL_PERMISSIONS = {
    "SEARCH_SUPPLIERS": "read",
    "INSPECT_SUPPLIER": "read",
    "CALCULATE_LANDED_COST": "compute",
    "EMAIL_SUPPLIER": "write",
}
```

Day 3 stays primarily read-only. Approval gates arrive later in the course.

## 11. Function calling with a model

The model should receive:

- current goal;
- current state;
- available tool definitions.

It should return a structured tool call. Python then validates and executes it.

```json
{
  "name": "CALCULATE_LANDED_COST",
  "arguments": {
    "unit_price": 445,
    "shipping": 42,
    "tax_rate": 0.18
  }
}
```

The model chooses. The runtime controls.

## Design checklist

For every tool, answer:

1. What exact capability does it expose?
2. What arguments are required?
3. What is the return shape?
4. What failures can occur?
5. Is the tool read-only, compute, or side-effecting?
6. Which permission level is required?
7. How will the runtime log the call and result?
