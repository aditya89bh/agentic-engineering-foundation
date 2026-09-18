# Day 6 Concepts

## 1. State vs memory

State belongs to the current execution. Memory survives beyond it.

```text
State  = information needed for the current run
Memory = information retained for future runs
```

Not everything in state deserves to become memory.

## 2. Why agents need memory

Useful memory can preserve:

- user preferences;
- past decisions;
- previous failures;
- rejected options;
- successful suppliers;
- recurring constraints;
- stable facts;
- prior task outcomes.

Without memory, each new run starts from zero.

## 3. Memory types

### Working memory

Temporary task information such as current candidates and latest observations.

### Episodic memory

Past experiences, such as a supplier rejection or a failed delivery.

### Semantic memory

Stable knowledge, such as a supplier certification.

### Decision memory

A record of what decision was made and why.

## 4. Memory write policy

A memory should usually be stored only when it is:

- likely to matter in a future task;
- stable enough to be useful;
- sourced;
- trustworthy enough;
- allowed to be retained.

Avoid storing duplicate observations, transient errors, irrelevant chat, and unverified assumptions.

## 5. Memory schema

Useful fields include:

```text
id
type
subject
content
source
confidence
created_at
expires_at
tags
```

The schema should make provenance and freshness explicit.

## 6. Persistence

Day 6 uses SQLite because it is persistent, queryable, local, and requires no external infrastructure.

## 7. Memory store abstraction

The agent should depend on an interface rather than a specific database.

```python
class MemoryStore:
    def write(self, record):
        ...

    def get_by_subject(self, subject):
        ...

    def search(self, query):
        ...
```

## 8. Retrieval

Memory is only useful when retrieval is selective.

Examples:

- subject lookup;
- keyword search;
- type filter;
- confidence filter;
- freshness filter.

## 9. Retrieval relevance

Ask: **which memories can change the current decision?**

A previous supplier rejection may matter for a sourcing task. An unrelated travel plan does not.

## 10. Memory into context

Correct pipeline:

```text
Memory Store
    ↓
Retrieval
    ↓
Filtering
    ↓
Context Manager
    ↓
Model
```

Do not dump the full memory store into the prompt.

## 11. Memory conflicts

When old and new facts conflict, use an explicit precedence policy.

Example:

```text
live verified observation
> recent verified memory
> older memory
> inferred memory
```

## 12. Freshness

Different facts age differently.

```text
certification → relatively stable
price         → volatile
inventory     → highly volatile
```

Freshness should affect whether a memory is trusted.

## 13. Confidence

Do not treat these equally:

- verified fact;
- user preference;
- model inference;
- speculation.

Confidence and source should travel with the memory.

## 14. Separate write and read policies

Write policy asks:

> Should this be stored?

Read policy asks:

> Should this be retrieved now?

These are separate decisions.

## 15. Embeddings

Embeddings can support semantic retrieval, but Day 6 keeps the implementation deterministic first. The important idea is selective retrieval, not a specific vector database.

## 16. Memory failure modes

Common failures include:

- storing everything;
- retrieving everything;
- stale memory;
- duplicate memory;
- conflicting memory;
- false memory;
- missing provenance;
- low-confidence memory treated as fact;
- irrelevant retrieval;
- memory poisoning.

The engineering question is not just whether the system can remember, but whether it remembers the right thing and trusts it appropriately.
