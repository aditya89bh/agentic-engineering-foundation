# Exercise 2: Break the Schema

## Goal

Classify invalid structured data and decide the correct recovery strategy.

Use these categories:

- syntax error;
- missing required field;
- type error;
- constraint violation;
- unsupported value;
- semantic ambiguity;
- extra field.

Then choose one response:

- repair;
- retry;
- reject;
- ask the user.

## Cases

1. `{"component":"aluminum brackets","quantity":-5,"max_unit_price":500,"currency":"INR"}`
2. `{"component":"aluminum brackets","quantity":"fifty","max_unit_price":500,"currency":"INR"}`
3. `{"component":"aluminum brackets","quantity":50,"currency":"INR"}`
4. `{"component":"aluminum brackets","quantity":50,"max_unit_price":500,"currency":"rupees"}`
5. `{ component: aluminum brackets }`
6. `{"component":"aluminum brackets","quantity":50,"max_unit_price":"500","currency":"INR"}`
7. `{"component":"aluminum brackets","quantity":50,"max_unit_price":500,"currency":"INR","preferred_supplier":"Apex"}`
8. `{"component":"aluminum brackets","quantity":50,"max_unit_price":500,"currency":"INR","max_lead_days":0}`
9. User says: `Need some brackets soon. Keep the price reasonable.`
10. Model returns valid data but extracts quantity 500 when the user requested 50.

## Worksheet

| Case | Failure type | Repair / retry / reject / clarify | Why? |
| --- | --- | --- | --- |
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |
| 6 |  |  |  |
| 7 |  |  |  |
| 8 |  |  |  |
| 9 |  |  |  |
| 10 |  |  |  |

## Discussion

Validation catches structural errors. It does not prove that the extracted meaning matches the user's intent. Case 10 is structurally valid but semantically wrong.
