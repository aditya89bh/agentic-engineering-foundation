# Agentic Engineering Foundation

A 10-day technical foundation course for university students who want to build agentic systems as software systems. The course emphasizes architecture, state, control flow, tools, context, memory, reliability, safety, evaluation, and testing rather than AI-product literacy or framework tutorials.

> **Current status:** Days 1–10 are complete.

## Who this course is for

Students who can read and write basic Python and are comfortable using a terminal. Prior experience with machine learning, LLM APIs, or agent frameworks is not required.

## Prerequisites

- Basic Python: functions, dictionaries, lists, loops, and conditionals
- Basic command-line usage
- A GitHub account for Codespaces and submissions
- Git fundamentals: clone, branch, commit, and push

The core Day 1 runtime requires no API key. An optional second-stage exercise replaces the deterministic decision policy with an LLM and requires an API key.

## Engineering principle

> **Use models for ambiguity. Use deterministic software for certainty.**

Models can interpret open-ended goals or choose among valid actions. Ordinary software should validate those actions, enforce limits, execute tools, preserve state, assemble context, manage memory, recover from failures, enforce policy, require approval where needed, and evaluate behavior with repeatable tests.

## 10-day overview

| Day | Topic | Engineering focus |
| --- | --- | --- |
| 1 | Agent Architecture and the Execution Loop | Runtime, state, actions, observations, stopping, and model boundary |
| 2 | Structured Outputs and Schema Design | Machine-readable contracts and validation |
| 3 | Tools and Function Calling | Safe capability boundaries, dispatch, and tool observations |
| 4 | State Machines and Agent Loops | Explicit transitions, branches, retries, terminal states, and checkpoints |
| 5 | Context Engineering | Selection, routing, compression, provenance, and context budgets |
| 6 | Memory Systems | Persistent memory, write/read policy, confidence, freshness, and retrieval |
| 7 | Reliability and Failure Engineering | Failure taxonomy, bounded retries, backoff, fallbacks, circuit breakers, and failure logs |
| 8 | Guardrails and Human-in-the-Loop | Permission boundaries, policy checks, approval gates, and audit trails |
| 9 | Agent Evaluation and Testing | Component, trajectory, outcome, regression, and metric-driven evaluation |
| 10 | Capstone Engineering Project | End-to-end integration, debugging, evaluation, and presentation |

See [course-map.md](course-map.md) for learning outcomes and the progression.

## Repository structure

- `setup/` — Codespaces, local setup, and API-key safety
- `dayXX-*/` — concepts, exercises, starter code, solutions, tests, and projects
- `resources/` — shared references added as the course develops
- `.devcontainer/` — Python 3.11 Codespaces configuration

## Course progression

```text
Day 1  architecture
Day 2  contracts
Day 3  tools
Day 4  state
Day 5  context
Day 6  memory
Day 7  reliability
Day 8  guardrails
Day 9  evaluation
Day 10 capstone integration
```

The final capstone integrates:

```text
request
→ structured requirement
→ state machine
→ context manager
→ decision
→ tool
→ observation
→ memory
→ reliability
→ policy / approval
→ audit
→ evaluation
```

## Start in GitHub Codespaces

1. Open this repository on GitHub.
2. Select **Code → Codespaces → Create codespace on main**.
3. Wait for the terminal to finish setting up.
4. Run the relevant day from its README.

Day 10 capstone:

```bash
python day10-capstone/agent/supplier_agent.py
python -m unittest discover day10-capstone/tests -v
```

For the optional Day 1 LLM policy, follow [Day 1](day01-agent-architecture/README.md) and [API key safety](setup/api-keys.md).

For more detail, see [setup/codespaces.md](setup/codespaces.md). For a local environment, see [setup/local-setup.md](setup/local-setup.md).

## How to work and submit

1. Fork the course repository or use the repository assigned by your instructor.
2. Create a branch such as `day10-your-name`.
3. Complete work in the relevant starter, exercises, or capstone files.
4. Run the program and record important test cases.
5. Run the relevant automated tests.
6. Commit with a descriptive message and push your branch.
7. Open a pull request containing a design summary, verification commands, evaluation evidence, and known limitations.

## Framework policy

The foundation deliberately does not use LangGraph, CrewAI, AutoGen, or similar agent frameworks. Students first learn the runtime those tools orchestrate so they can later evaluate frameworks from engineering principles.

## License

Course content and code are available under the [MIT License](LICENSE).
