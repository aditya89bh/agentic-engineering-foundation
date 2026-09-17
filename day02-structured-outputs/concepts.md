# Day 2 Concepts

## 1. Why free-form text breaks software

LLMs naturally produce language. Software needs predictable structure.

A response such as:

```text
The buyer needs around 100 aluminum brackets under ₹500 each.
```

is readable by a person but awkward for downstream code. A structured representation is easier to validate and execute:

```json
{
  "component": "aluminum brackets",
  "quantity": 100,
  "max_unit_price": 500,
  "currency": "INR"
}
```

The engineering goal is to create a reliable boundary between probabilistic interpretation and deterministic application logic.

## 2. JSON as the first contract

JSON gives software a machine-readable representation using:

- objects;
- arrays;
- strings;
- numbers;
- booleans;
- null values.

JSON alone is not enough. Valid JSON can still contain missing, wrongly typed, or nonsensical data.

## 3. Natural language to structured requirements

Input:

```text
I need 100 aluminum brackets below ₹500 each, preferably delivered within two weeks.
```

Target representation:

```json
{
  "component": "aluminum brackets",
  "quantity": 100,
  "max_unit_price": 500,
  "currency": "INR",
  "max_lead_days": 14
}
```

This object can become a reliable input to the Day 1 supplier agent.

## 4. Schema design

A schema defines what valid data looks like.

| Field | Type | Required? | Constraint |
| --- | --- | --- | --- |
| component | string | yes | non-empty |
| quantity | integer | yes | > 0 |
| max_unit_price | number | yes | > 0 |
| currency | enum | yes | INR, USD, EUR |
| max_lead_days | integer | no | > 0 |

A schema answers four questions:

1. Which fields may exist?
2. Which fields must exist?
3. What type must each field have?
4. What values are acceptable?

## 5. Typed Python models

Plain dictionaries are flexible but weakly constrained. Typed models make assumptions explicit.

```python
from pydantic import BaseModel, Field
from typing import Literal

class SupplierRequirement(BaseModel):
    component: str = Field(min_length=1)
    quantity: int = Field(gt=0)
    max_unit_price: float = Field(gt=0)
    currency: Literal["INR", "USD", "EUR"]
    max_lead_days: int | None = Field(default=None, gt=0)
```

Now invalid data fails before it reaches downstream logic.

## 6. Three levels of correctness

These are different:

```text
syntactically valid
        ≠
schema valid
        ≠
semantically correct
```

Example:

```json
{
  "component": "aluminum brackets",
  "quantity": 100,
  "max_unit_price": 500,
  "currency": "INR"
}
```

This may be syntactically valid and schema valid. But if the user actually said 1000 units, it is semantically wrong.

Validation cannot guarantee truth. It guarantees that data obeys the contract.

## 7. Common output failures

### Syntax error

```text
{ component: aluminum brackets }
```

### Missing field

```json
{
  "component": "aluminum brackets"
}
```

### Wrong type

```json
{
  "quantity": "many"
}
```

### Constraint violation

```json
{
  "quantity": -20
}
```

### Semantic ambiguity

```text
Need some brackets soon and keep the price reasonable.
```

The final case cannot be fixed by type validation alone.

## 8. Repair, retry, reject, or clarify

When output is invalid, the application needs an explicit policy.

```text
Invalid output
     ↓
Can deterministic code repair it safely?
   ↙                     ↘
 yes                     no
 ↓                        ↓
repair          retry / reject / clarify
```

Safe repair example:

```text
"500" → 500
```

Potentially unsafe guess:

```text
currency missing → assume INR
```

Do not silently invent business-critical information.

## 9. Structured model output

Day 1 used:

```text
LLM → text/JSON → parser → validator
```

Day 2 introduces:

```text
LLM
 ↓
defined schema
 ↓
structured result
 ↓
validated object
 ↓
application logic
```

The model interprets ambiguity. The schema defines allowed representation. The validator checks the contract. The application decides what happens next.

## 10. Extra fields and strictness

Suppose the model returns:

```json
{
  "component": "aluminum brackets",
  "quantity": 100,
  "max_unit_price": 500,
  "currency": "INR",
  "supplier_recommendation": "Apex Components"
}
```

The last field was never requested. Strict schemas can reject extra fields so the model cannot expand its own contract.

## 11. Design principle

> **The LLM should interpret the request. The application should own the contract.**

This principle becomes essential on Day 3, when structured model decisions begin triggering real tools.

## Design checklist

Before accepting model-generated data, ask:

1. What fields are required?
2. Which are optional?
3. What values are constrained?
4. Are extra fields allowed?
5. Which errors can be repaired deterministically?
6. Which missing values require user clarification?
7. What should happen after validation fails?
8. How will this object be consumed downstream?
