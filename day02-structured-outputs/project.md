# Mini-Project: Requirement Extraction Service

Build a small service that converts procurement requests into validated supplier requirements.

## Example input

```text
Need 100 aluminum brackets below ₹500 within 14 days.
```

## Expected output

```json
{
  "component": "aluminum brackets",
  "quantity": 100,
  "max_unit_price": 500,
  "currency": "INR",
  "max_lead_days": 14
}
```

## Required features

- natural-language input;
- an explicit `SupplierRequirement` schema;
- required and optional fields;
- deterministic validation;
- readable validation errors;
- rejection of unexpected fields;
- malformed-response handling;
- at least 10 test cases.

## Engineering requirements

The extraction component may be deterministic or model-driven, but the contract must remain owned by the application.

Your program must distinguish:

```text
syntax error
schema error
semantic ambiguity
```

For invalid outputs, document when the system should:

```text
repair / retry / reject / ask the user
```

## Suggested milestones

1. Define the schema before writing extraction logic.
2. Validate manually created objects.
3. Add constraints for quantity, price, lead time, and currency.
4. Reject unexpected fields.
5. Parse JSON and validate it through the same model.
6. Add malformed and ambiguous cases.
7. Build at least 10 automated tests.
8. Connect the validated object conceptually to the Day 1 supplier agent input.

## Acceptance checks

Include tests for:

- valid complete input;
- optional lead time missing;
- missing quantity;
- negative price;
- negative quantity;
- unsupported currency;
- extra field;
- malformed JSON;
- numeric value represented incorrectly;
- ambiguous source request.

## Deliverables

- schema implementation;
- CLI extractor;
- tests;
- failure analysis;
- short README or pull-request note explaining the recovery policy.

## Bridge to Day 3

Day 2 gives the agent a reliable input contract.

Day 3 asks what happens after the agent understands the request: how can it safely call external capabilities and execute model-selected tools?
