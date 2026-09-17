# Failure Cases

Structured output can fail at several different layers. Diagnose the layer before deciding how to recover.

## Invalid JSON

**Symptom:** the parser cannot decode the model response.

**Example:**

```text
{ component: aluminum brackets }
```

**Response:** retry with a stricter output instruction or reject the response. Do not use string slicing as a permanent parser.

## Missing required field

**Symptom:** schema validation fails because a required field is absent.

**Example:** quantity or max price is missing.

**Response:** ask the user when the value is business-critical. Do not silently invent it.

## Wrong type

**Symptom:** a field has an unexpected representation, such as `"fifty"` instead of `50`.

**Response:** repair only when conversion is deterministic and unambiguous. Otherwise retry or clarify.

## Constraint violation

**Symptom:** the type is correct but the value is impossible or forbidden.

Examples:

- negative quantity;
- zero lead time when the schema requires a positive value;
- negative price.

**Response:** reject and surface the validation error.

## Unsupported enum value

**Symptom:** the model returns a value outside the contract, such as `"rupees"` where only `INR`, `USD`, or `EUR` are permitted.

**Response:** normalize only if the mapping is explicit and deterministic. Otherwise reject.

## Extra field

**Symptom:** the model expands the contract with fields the application did not request.

**Response:** prefer strict schemas for action-driving data. Reject unexpected fields instead of letting the model redefine the interface.

## Structurally valid but semantically wrong

**Symptom:** the object passes schema validation but misrepresents the user's request.

Example: user requested 50 units, output contains 500.

**Response:** schema validation cannot solve this alone. Use extraction tests, source-grounded checks, confirmation for high-impact fields, or evaluation datasets.

## Ambiguous source request

**Symptom:** required values were never supplied by the user.

Example:

```text
Need some brackets soon. Keep the price reasonable.
```

**Response:** ask for clarification rather than generating plausible numbers.

## Recovery decision

For every failure, choose explicitly among:

```text
repair → retry → reject → clarify
```

The safest recovery is the one that introduces the least unsupported information.
