# Mini-Project: CLI Supplier Research Agent

Build a command-line agent that researches mock suppliers and recommends an eligible option.

## Example input

```text
Find a supplier for aluminum brackets below ₹500/unit.
```

## Expected behavior

The program should:

1. accept or define the goal;
2. maintain explicit execution state;
3. choose only from predefined `SEARCH`, `INSPECT`, and `FINISH` actions;
4. execute multiple steps against mock supplier data;
5. inspect candidate details before recommending one;
6. produce an evidence-based recommendation or a clear no-match result;
7. stop correctly on success, failure, or `MAX_STEPS`.

## Required engineering properties

- No agent framework and no required external API
- A visible step counter and action log
- Action validation before execution
- A finite stopping condition
- Graceful handling of an empty search result
- State that can explain why the final supplier was selected

## Suggested milestones

1. Make `SEARCH` filter by component and maximum unit price.
2. Make `INSPECT` retrieve one supplier and record it once.
3. Implement a policy that searches, inspects candidates, then finishes.
4. Choose the best eligible supplier using stated ranking rules.
5. Add invalid-action and maximum-step tests.

## Acceptance checks

Run at least these scenarios:

- aluminum brackets below ₹500/unit returns an inspected, eligible supplier;
- an impossible component or price returns no match;
- an invalid action is rejected;
- the loop cannot exceed `MAX_STEPS`;
- repeated inspection does not corrupt state.

## Reflection

In your pull request, identify which parts of your program could later be model-driven and which must remain deterministic. Explain one human approval point you would add before connecting the agent to real procurement systems.
