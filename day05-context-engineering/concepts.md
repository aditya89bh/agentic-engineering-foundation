# Day 5 Concepts

## 1. What is context?

Context is the information supplied to the model for a specific decision. It may contain system instructions, the user goal, current state, recent observations, tool descriptions, retrieved knowledge, constraints, summaries, and prior decisions.

## 2. State vs context vs memory

- **State**: current execution data.
- **Context**: selected information for the current model call.
- **Memory**: information retained beyond the immediate execution.

A large state object should not automatically become a large prompt.

## 3. Why sending everything is poor engineering

Blindly forwarding all available information increases token cost, latency, contradiction risk, stale information, distraction, and attack surface.

More context does not automatically improve decisions.

## 4. Context layers

A useful structure is:

```text
System Context
Task Context
State Context
Tool Context
Retrieved Context
Recent History
```

## 5. Context budget

Treat context as a bounded resource.

```python
MAX_CONTEXT_CHARS = 5000
```

The exact measure may later be tokens, but the engineering idea is the same: selection must happen before model invocation.

## 6. Prioritization

A simple priority order:

1. hard constraints;
2. current goal;
3. current state;
4. latest relevant observations;
5. available tool definitions;
6. older history.

Ask: **what information can change the next action?**

## 7. Relevance filtering

Filter history by decision needs rather than forwarding every event.

```python
def relevant_events(history, allowed_types):
    return [event for event in history if event["type"] in allowed_types]
```

## 8. Recency vs relevance

The newest fact is not always the most useful fact.

A recent “thanks” is less important than an older hard budget constraint.

## 9. Deterministic compression

Prefer code-based compression for structured information.

Instead of 20 observations:

```json
{
  "searched": 8,
  "eligible": 3,
  "inspected": 2,
  "best_price": 445
}
```

Use model summarization only where semantic compression is genuinely needed.

## 10. Summarization risks

Summaries can lose constraints, invent details, become stale, or hide omissions. A summary is a derived view, not ground truth.

## 11. Context pollution

Common pollution sources:

- duplicate observations;
- unrelated user turns;
- stale assumptions;
- obsolete tool outputs;
- failed actions;
- verbose traces;
- irrelevant retrieved documents.

Good context is relevant, current, sufficient, and bounded.

## 12. Context routing

Different decisions need different information.

```text
SEARCH  → goal + hard requirements + search tools
INSPECT → candidate + requirements + inspection tools
COMPARE → inspected evidence + comparison criteria
FINISH  → recommendation + evidence + stop condition
```

## 13. Tool-aware context

Do not expose every tool on every turn. Narrow the available action surface to the current state.

## 14. Provenance

Track where facts came from.

```json
{
  "field": "max_unit_price",
  "value": 500,
  "source": "user_requirement",
  "version": 1
}
```

Provenance supports debugging, trust, conflict handling, and later memory systems.

## 15. Conflicting facts

Example:

```text
Earlier budget: ₹500
Later budget: ₹550
```

Use an explicit policy such as:

```text
newer explicit user instruction
> older explicit user instruction
> inferred value
```

Do not let conflicts be resolved implicitly.

## 16. Context manager responsibility

A context manager should:

- select relevant fields;
- route decision-specific data;
- remove duplicates;
- prefer current facts;
- compress structured history;
- enforce budget;
- preserve provenance;
- expose only relevant tools.

The model consumes context. The application decides how context is assembled.
