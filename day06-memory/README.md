# Day 6: Memory Systems

## Objective

By the end of Day 6, students should be able to distinguish state from memory, design working, episodic, semantic, and decision memory, implement a persistent SQLite-backed memory store, and define explicit memory write and retrieval policies.

## Learning outcomes

Students will be able to:

- separate execution state from durable memory;
- classify working, episodic, semantic, and decision memory;
- define a memory schema with provenance, confidence, and freshness;
- persist memory in SQLite;
- implement memory write and read policies;
- retrieve only relevant memories;
- handle stale, duplicate, conflicting, and low-confidence memories;
- inject retrieved memory into context rather than directly into model calls.

## Suggested flow

1. Read [concepts.md](concepts.md).
2. Complete [Memory Write Policy](exercises/memory-write-policy.md).
3. Complete [Memory Retrieval](exercises/memory-retrieval.md).
4. Implement [starter/memory_store.py](starter/memory_store.py).
5. Compare with the reference implementation.
6. Run the tests.
7. Build the [Memory-Aware Supplier Agent](project.md).
8. Review [failure-cases.md](failure-cases.md).

## Run the reference implementation

```bash
python day06-memory/solution/supplier_agent.py
python -m unittest discover day06-memory/tests -v
```

## Core mental model

```text
Past Runs
   ↓
Memory Store
   ↓
Retrieval Policy
   ↓
Context Manager
   ↓
Current Decision
```

> Memory is a source. Context is the selected view.
