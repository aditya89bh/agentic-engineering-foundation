# Course Map

The course moves from one transparent execution loop to a tested, constrained agentic system. Each day adds an engineering capability rather than a new framework.

| Day | Module | Students will be able to… | Status |
| --- | --- | --- | --- |
| 1 | Agent Architecture and the Execution Loop | Distinguish agents from workflows and implement a bounded loop with explicit state | Complete |
| 2 | Structured Outputs and Schema Design | Define, validate, and recover machine-readable model outputs | Complete |
| 3 | Tools and Function Calling | Design tool contracts and safely execute model-selected actions | Complete |
| 4 | State Machines and Agent Loops | Model transitions, retries, branches, checkpoints, and terminal states | Complete |
| 5 | Context Engineering | Select, route, compress, and budget decision-specific model context | Complete |
| 6 | Memory Systems | Design persistent memory, write/read policies, and relevant retrieval | Complete |
| 7 | Reliability and Failure Engineering | Classify failures and implement bounded retries, fallbacks, circuit breakers, and structured failure handling | Complete |
| 8 | Guardrails and Human-in-the-Loop | Enforce permissions, policy decisions, approval gates, and auditable human control | Complete |
| 9 | Agent Evaluation and Testing | Build task sets, graders, traces, aggregate metrics, and regression checks | Complete |
| 10 | Capstone Engineering Project | Design, build, evaluate, and present a complete agentic system | Planned |

## Progression

```text
architecture → contracts → tools → state → context → memory
            → reliability → guardrails → evaluation → capstone
```

Day 1 establishes the execution runtime: a controller chooses an action, the environment returns an observation, and deterministic code updates state and enforces stopping rules.

Day 2 adds explicit machine-readable contracts between model interpretation and application logic using schemas, validation, and recovery policies.

Day 3 adds controlled capabilities through tool contracts, argument validation, a registry, a dispatcher, and explicit observations.

Day 4 makes multi-step behavior explicit through finite states, legal transitions, branching, retry budgets, invariants, checkpoints, and terminal conditions.

Day 5 separates state from context and adds relevance filtering, context routing, deterministic compression, bounded budgets, provenance, and conflict handling.

Day 6 adds durable memory with explicit schemas, SQLite persistence, write/read policies, confidence, freshness, provenance, duplicate prevention, and selective retrieval.

Day 7 adds failure taxonomy, retry classification, bounded retries, backoff, fallbacks, circuit-breaker behavior, structured error logs, and partial-success handling.

Day 8 adds deterministic permissions, role-based and argument-level policies, scoped human approvals, approval state transitions, and audit logging.

Day 9 adds structured evaluation datasets, deterministic graders, execution traces, component/trajectory/outcome evaluation, aggregate metrics, failure categorization, and regression testing.
