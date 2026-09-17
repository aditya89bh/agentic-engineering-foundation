# Exercise 2: Valid or Invalid Tool Call?

Classify each request as valid, invalid tool, invalid arguments, unsupported capability, or dangerous side effect.

## Cases

```json
{
  "name": "INSPECT_SUPPLIER",
  "arguments": {}
}
```

```json
{
  "name": "SEARCH_SUPPLIERS",
  "arguments": {
    "component": "aluminum brackets",
    "max_unit_price": "cheap"
  }
}
```

```json
{
  "name": "DELETE_SUPPLIER",
  "arguments": {
    "supplier_id": "SUP-001"
  }
}
```

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

## Questions

1. Which calls fail before tool execution?
2. Which calls request a capability outside the registry?
3. Which calls could create side effects?
4. What deterministic check should block each invalid request?
