# Mini-Project: Memory-Aware Supplier Agent

Extend the supplier agent so useful information can survive across runs.

## Expected flow

```text
Current Requirement
       ↓
Retrieve Relevant Memories
       ↓
Context Manager
       ↓
Agent Decision
       ↓
New Observation
       ↓
Memory Write Policy
       ↓
Memory Store
```

## Required engineering properties

- persistent SQLite memory;
- memory schema;
- episodic, semantic, decision, and preference examples;
- explicit write policy;
- explicit retrieval policy;
- confidence;
- provenance;
- timestamps;
- freshness or expiry;
- duplicate detection;
- metadata filtering;
- state/context/memory separation;
- at least 10 tests.

## Acceptance checks

1. a rejection is persisted across runs;
2. duplicate memory IDs are rejected;
3. stale memory can be detected;
4. low-confidence records are not automatically trusted;
5. retrieval can filter by subject;
6. irrelevant memories stay out of context;
7. conflicting memories follow a documented precedence rule;
8. missing source prevents a memory from being written;
9. memory-store failures are surfaced rather than silently ignored;
10. the agent can explain which retrieved memory affected a decision.

## Reflection

Explain one piece of state that should not become durable memory. Explain one type of memory that should expire automatically and why.
