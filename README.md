# Agentic Engineering Foundation

A 10-day technical foundation course for university students who want to build agentic systems as software systems. The course emphasizes architecture, state, control flow, tools, reliability, safety, and evaluation rather than AI-product literacy or framework tutorials.

> **Current status:** Days 1–4 are complete. Days 5–10 contain roadmap placeholders only.

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

Models can interpret an open-ended goal or choose among valid actions. Ordinary software should validate those actions, enforce limits, execute tools, preserve state, and decide whether hard constraints have been satisfied.

## 10-day overview

| Day | Topic | Engineering focus |
| --- | --- | --- |
| 1 | Agent Architecture and the Execution Loop | Runtime, state, actions, observations, stopping, and model boundary |
| 2 | Structured Outputs and Schema Design | Machine-readable contracts and validation |
| 3 | Tools and Function Calling | Safe capability boundaries, dispatch, and tool observations |
| 4 | State Machines and Agent Loops | Explicit transitions, branches, retries, terminal states, and checkpoints |
| 5 | Context Engineering | Selecting useful working context |
| 6 | Memory Systems | Durable and retrievable state |
| 7 | Reliability and Failure Engineering | Recovery, retries, and observability |
| 8 | Guardrails and Human-in-the-Loop | Constraints and approval gates |
| 9 | Agent Evaluation and Testing | Behavioral tests and metrics |
| 10 | Capstone Engineering Project | End-to-end system design |

See [course-map.md](course-map.md) for learning outcomes and the progression.

## Repository structure

- `setup/` — Codespaces, local setup, and API-key safety
- `dayXX-*/` — concepts, exercises, starter code, solutions, tests, and projects
- `resources/` — shared references added as the course develops
- `.devcontainer/` — Python 3.11 Codespaces configuration

Day 1 establishes a bounded runtime:

```text
state → decision policy → validated action → tool → observation
```

Day 2 adds the model/application contract:

```text
natural language → structured output → schema validation → application logic
```

Day 3 adds controlled capabilities:

```text
agent decision → structured tool call → validation → dispatcher → tool → observation
```

Day 4 makes execution explicit:

```text
state → legal transition → branch / loop / retry → terminal state
```

## Start in GitHub Codespaces

1. Open this repository on GitHub.
2. Select **Code → Codespaces → Create codespace on main**.
3. Wait for the terminal to finish setting up.
4. Run the relevant day from its README.

Day 4 reference implementation:

```bash
python day04-state-and-loops/solution/supplier_agent.py
python -m unittest discover day04-state-and-loops/tests -v
```

For the optional Day 1 LLM policy, follow [Day 1](day01-agent-architecture/README.md) and [API key safety](setup/api-keys.md).

For more detail, see [setup/codespaces.md](setup/codespaces.md). For a local environment, see [setup/local-setup.md](setup/local-setup.md).

## How to work and submit

1. Fork the course repository or use the repository assigned by your instructor.
2. Create a branch such as `day04-your-name`.
3. Complete work in the relevant `starter/` and `exercises/` files. Do not modify the provided `solution/` until after review.
4. Run the program and record important test cases.
5. Run the relevant automated tests.
6. Commit with a descriptive message and push your branch.
7. Open a pull request containing a short design summary, verification commands, and known limitations or failure cases.

## Framework policy

The foundation deliberately does not use LangGraph, CrewAI, AutoGen, or similar agent frameworks. Students first learn the runtime those tools orchestrate so they can later evaluate frameworks from engineering principles.

## License

Course content and code are available under the [MIT License](LICENSE).
