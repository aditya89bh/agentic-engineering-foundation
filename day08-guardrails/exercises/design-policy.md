# Exercise 2: Design the Policy

Convert these business rules into explicit policy logic:

1. orders below ₹10,000 can be executed by a procurement manager;
2. orders from ₹10,000 to ₹50,000 require manager approval;
3. orders above ₹50,000 require finance approval;
4. a purchase order cannot be created for an uninspected supplier;
5. a researcher may search and inspect but cannot create purchase orders;
6. rejected suppliers cannot be used without explicit override.

For every rule, define:

- inputs;
- outcome: ALLOW, DENY, or REQUIRE_APPROVAL;
- reason;
- required approver if applicable.
