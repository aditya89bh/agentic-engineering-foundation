# Agentic Engineering Foundation

A 10-day technical foundation course for university students who want to build agentic systems as software systems. The course emphasizes architecture, state, control flow, tools, reliability, safety, and evaluation—not AI-product literacy or framework tutorials.

> **Current status:** Day 1 is complete. Days 2–10 contain roadmap placeholders only.

## Who this course is for

Students who can read and write basic Python and are comfortable using a terminal. Prior experience with machine learning, LLM APIs, or agent frameworks is not required.

## Prerequisites

- Basic Python: functions, dictionaries, lists, loops, and conditionals
- Basic command-line usage
- A GitHub account for Codespaces and submissions
- Git fundamentals: clone, branch, commit, and push

No API key is required for Day 1.

## Engineering principle

> **Use models for ambiguity. Use deterministic software for certainty.**

Models can interpret an open-ended goal or choose among valid actions. Ordinary software should validate those actions, enforce limits, execute tools, preserve state, and decide whether hard constraints have been satisfied.

## 10-day overview

| Day | Topic | Engineering focus |
| --- | --- | --- |
| 1 | Agent Architecture and the Execution Loop | State, actions, observations, and stopping |
| 2 | Structured Outputs and Schema Design | Machine-readable contracts |
| 3 | Tools and Function Calling | Safe capability boundaries |
| 4 | State Machines and Agent Loops | Explicit transitions and control flow |
| 5 | Context Engineering | Selecting useful working context |
| 6 | Memory Systems | Durable and retrievable state |
| 7 | Reliability and Failure Engineering | Recovery, retries, and observability |
| 8 | Guardrails and Human-in-the-Loop | Constraints and approval gates |
| 9 | Agent Evaluation and Testing | Behavioral tests and metrics |
| 10 | Capstone Engineering Project | End-to-end system design |

See [course-map.md](course-map.md) for learning outcomes and the progression.

## Repository structure

- `setup/` — Codespaces, local setup, and API-key safety
- `dayXX-*/` — concepts, exercises, starter code, solutions, and projects
- `resources/` — shared references added as the course develops
- `.devcontainer/` — Python 3.11 Codespaces configuration

Day 1 keeps model selection behind a simple policy function. This exposes the agent loop without requiring an LLM or hiding control flow inside an agent framework.

## Start in GitHub Codespaces

1. Open this repository on GitHub.
2. Select **Code → Codespaces → Create codespace on main**.
3. Wait for the terminal to finish setting up.
4. Run:

   ```bash
   python day01-agent-architecture/solution/agent_loop.py
   ```

For more detail, see [setup/codespaces.md](setup/codespaces.md). For a local environment, see [setup/local-setup.md](setup/local-setup.md).

## How to work and submit

1. Fork the course repository or use the repository assigned by your instructor.
2. Create a branch such as `day01-your-name`.
3. Complete work in the relevant `starter/` and `exercises/` files. Do not modify the provided `solution/` until after review.
4. Run the program and record important test cases.
5. Commit with a descriptive message and push your branch.
6. Open a pull request containing:
   - a short design summary;
   - commands used to verify the work;
   - known limitations or failure cases;
   - screenshots only when they add evidence.

## Framework policy

The foundation deliberately does not use LangGraph, CrewAI, AutoGen, or similar agent frameworks. Students first learn the loop those tools orchestrate so they can later evaluate frameworks from engineering principles.

## License

Course content and code are available under the [MIT License](LICENSE).
