# Day 2: Structured Outputs and Schema Design

## Objective

By the end of Day 2, you should be able to turn ambiguous natural-language requests into validated machine-readable data, define explicit schemas, detect malformed outputs, and decide when software should repair, retry, reject, or ask the user for clarification.

## Learning outcomes

You will be able to:

- explain why free-form model output is fragile in software systems;
- represent requirements as JSON and typed Python objects;
- define required, optional, constrained, and enumerated fields;
- validate structured data with Pydantic;
- distinguish syntax errors, schema errors, and semantic ambiguity;
- handle malformed model output safely;
- connect validated requirements to the Day 1 agent runtime.

## Suggested session plan

1. Read [concepts.md](concepts.md).
2. Complete [Design the Schema](exercises/design-schema.md).
3. Complete [Break the Schema](exercises/break-schema.md).
4. Implement the TODOs in [starter/requirement_extractor.py](starter/requirement_extractor.py).
5. Compare with [solution/requirement_extractor.py](solution/requirement_extractor.py).
6. Run the unit tests in [tests/](tests/).
7. Explore [failure-cases.md](failure-cases.md).
8. Build the [Requirement Extraction Service](project.md).

## Run the solution

From the repository root:

```bash
python -m pip install -r day02-structured-outputs/requirements.txt
python day02-structured-outputs/solution/requirement_extractor.py \
  "Need 100 aluminum brackets below ₹500 within 14 days"
python -m unittest discover day02-structured-outputs/tests -v
```

## Core mental model

```text
Natural language
      ↓
     LLM
      ↓
Structured output
      ↓
   Validator
      ↓
Application logic
```

A schema is not just documentation. It is an executable contract between a probabilistic model and deterministic software.
