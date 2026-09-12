# Exercise 2: Design an Agent on Paper

## Problem

Design a system that finds suitable suppliers for an industrial component. Do not write code yet. Make the execution contract precise enough that another engineer could implement it.

## Design worksheet

### 1. Goal

Write one measurable goal. Include the component, quantity, budget, location or delivery constraint, and minimum evidence required for a recommendation.

### 2. Inputs

List required and optional inputs. What happens when quantity, currency, specification, or deadline is missing?

### 3. Available tools

For every tool, define its inputs, output, possible errors, and side effects.

| Tool | Inputs | Observation | Failure modes | Side effect? |
| --- | --- | --- | --- | --- |
| Search suppliers |  |  |  |  |
| Inspect supplier |  |  |  |  |
|  |  |  |  |  |

### 4. State

Define the state fields carried between steps. Include progress, evidence, budgets, action history, and terminal status.

### 5. Possible actions

Start with `SEARCH`, `INSPECT`, and `FINISH`. Add an action only if it provides a distinct capability. Specify valid arguments for each action.

### 6. Environment

Where does supplier data come from? Which parts are under your control? What may change between two actions?

### 7. Stopping conditions

Define at least:

- one successful stop;
- one no-result stop;
- one safety or budget stop;
- one unrecoverable-error stop.

### 8. Human approval points

Mark steps where the system proposes rather than acts. Consider outreach, sharing specifications, accepting terms, placing orders, and spending money.

## Trace one run

Complete at least five transitions or stop earlier if your design reaches a valid terminal state.

| Step | State summary | Chosen action | Observation | State update |
| --- | --- | --- | --- | --- |
| 0 | Goal received |  |  |  |
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |

## Review questions

1. Which choices are ambiguous enough to justify a model?
2. Which constraints must remain deterministic?
3. Can every action be reconstructed from the log?
4. Can the design loop forever? Show the exact safeguard.
