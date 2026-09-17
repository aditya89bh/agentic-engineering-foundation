# Exercise 1: Design Better Tools

## Goal

Redesign vague capabilities into narrow, testable tool contracts.

Start with:

```text
supplier_tool()
procurement_tool()
check_data()
do_search()
```

For each replacement tool, define:

- name;
- purpose;
- inputs;
- output;
- failure cases;
- permission level;
- whether it has side effects.

## Example worksheet

| Tool | Purpose | Inputs | Output | Failures | Permission |
| --- | --- | --- | --- | --- | --- |
| `SEARCH_SUPPLIERS` | Find candidates matching hard constraints | component, max_unit_price | list of supplier summaries | empty result | read |
| `INSPECT_SUPPLIER` | Fetch one supplier record | supplier_id | supplier record | unknown ID | read |

## Review questions

1. Which proposed tools are still too broad?
2. Which tool arguments should be schema validated?
3. Which tools should never be exposed without approval?
4. Which tools can be tested with deterministic fixtures?
