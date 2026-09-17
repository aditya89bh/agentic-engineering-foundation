# Course Map

The course moves from one transparent execution loop to a tested, constrained agentic system. Each day adds an engineering capability rather than a new framework.

| Day | Module | Students will be able to… | Status |
| --- | --- | --- | --- |
| 1 | Agent Architecture and the Execution Loop | Distinguish agents from workflows and implement a bounded loop with explicit state | Complete |
| 2 | Structured Outputs and Schema Design | Define, validate, and recover machine-readable model outputs | Complete |
| 3 | Tools and Function Calling | Design tool contracts and safely execute model-selected actions | Planned |
| 4 | State Machines and Agent Loops | Model transitions, retries, branches, and terminal states | Planned |
| 5 | Context Engineering | Assemble relevant context under quality and token constraints | Planned |
| 6 | Memory Systems | Separate working, episodic, and durable memory | Planned |
| 7 | Reliability and Failure Engineering | Observe failures and add timeouts, retries, fallbacks, and idempotency | Planned |
| 8 | Guardrails and Human-in-the-Loop | Enforce policy and place approval gates around consequential actions | Planned |
| 9 | Agent Evaluation and Testing | Build task sets, graders, traces, and regression checks | Planned |
| 10 | Capstone Engineering Project | Design, build, evaluate, and present a complete agentic system | Planned |

## Progression

```text
architecture → contracts → tools → state → context → memory
            → reliability → guardrails → evaluation → capstone
```

Day 1 establishes the execution runtime: a controller chooses an action, the environment returns an observation, and deterministic code updates state and enforces stopping rules.

Day 2 adds explicit machine-readable contracts between model interpretation and application logic using schemas, validation, and recovery policies.
