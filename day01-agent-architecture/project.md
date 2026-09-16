# Mini-Project: CLI Supplier Research Agent

Build a command-line supplier research system in two stages.

## Example input

```text
Find a supplier for aluminum brackets below ₹500/unit.
```

## Stage A: deterministic runtime

The program should:

1. accept or define the goal;
2. maintain explicit execution state;
3. choose only from predefined `SEARCH`, `INSPECT`, and `FINISH` actions;
4. execute multiple steps against mock supplier data;
5. inspect candidate details before recommending one;
6. produce an evidence-based recommendation or a clear no-match result;
7. stop correctly on success, failure, or `MAX_STEPS`.

## Stage B: LLM decision policy

Replace only the action-selection policy with an LLM.

The LLM may propose the next action, but Python must still:

- validate the action name and required arguments;
- enforce `MAX_STEPS`;
- execute tools;
- update state;
- reject malformed output;
- prevent unsupported capabilities.

The purpose is to compare a deterministic controller with a model-driven decision component while keeping the same runtime boundary.

## Required engineering properties

- No agent framework
- Explicit state
- A visible step counter and action log
- Typed or clearly documented action shape
- Action validation before execution
- A finite stopping condition
- Graceful handling of an empty search result
- State that can explain why the final supplier was selected
- Repeatable tests for core failure paths

## Suggested milestones

1. Make `SEARCH` filter by component and maximum unit price.
2. Make `INSPECT` retrieve one supplier and record it once.
3. Implement a deterministic policy that searches, inspects candidates, then finishes.
4. Choose the best eligible supplier using stated ranking rules.
5. Add invalid-action and maximum-step tests.
6. Run the supplied unit tests.
7. Replace the policy with an LLM and compare the trace.
8. Record at least one malformed or invalid model action and show how the validator contains it.

## Acceptance checks

Run at least these scenarios:

- aluminum brackets below ₹500/unit returns an inspected, eligible supplier;
- an impossible component or price returns no match;
- an invalid action is rejected;
- the loop cannot exceed `MAX_STEPS`;
- repeated inspection does not corrupt state;
- the LLM cannot execute an action outside the allowlist.

## Reflection

In your pull request, answer:

1. Which parts of the runtime remain deterministic when an LLM is added?
2. What new failure modes appear when the deterministic policy is replaced by a model?
3. Why should the model propose actions rather than execute arbitrary code directly?
4. Where would you add human approval before connecting this system to real procurement infrastructure?
