# Exercise 1: Design the Schema

## Goal

Convert ambiguous procurement requests into explicit data contracts before writing code.

For each request, define:

- fields;
- types;
- required vs optional;
- constraints;
- allowed values;
- what requires clarification.

## Requests

1. Need 50 stainless-steel gears, ₹800 max each, delivery within 10 days.
2. Looking for aluminum enclosures, around 200 pieces, preferably under €12 each.
3. Need bearings for a prototype. Budget is flexible but delivery is urgent.
4. Source 500 injection-molded housings in India. Supplier must be ISO 9001 certified.
5. Need a vendor for machined brackets. Quantity is not decided yet.

## Worksheet

| Field | Type | Required? | Constraint | Missing-value behavior |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

## Questions

1. Which fields should never be guessed?
2. Which optional fields can safely be null?
3. Which constraints belong in code rather than in the model prompt?
4. What information would block downstream supplier search if missing?
5. Should the schema allow fields the application does not understand? Why?
