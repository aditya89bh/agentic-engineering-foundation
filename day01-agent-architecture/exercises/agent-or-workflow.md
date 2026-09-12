# Exercise 1: Agent or Not?

## Goal

Classify each system as one of:

- **LLM application** — a model transforms input to output without a multi-step action loop;
- **deterministic workflow** — code follows predefined steps and branches;
- **agent** — the system chooses its next action at runtime in pursuit of a goal;
- **hybrid** — deterministic control surrounds one or more agentic decisions.

Classification depends on architecture, not the product label. State your assumptions.

## Systems

| # | System | Your classification | Evidence: who chooses the next action? |
| --- | --- | --- | --- |
| 1 | A document summarizer makes one model call and returns the answer. |  |  |
| 2 | A chatbot answers each message but cannot call tools or pursue work across turns. |  |  |
| 3 | An invoice system validates required fields, matches a purchase order, and routes invoices above ₹50,000 for approval using fixed rules. |  |  |
| 4 | A travel planner searches flights, compares hotels, revises its plan when options are unavailable, and stops when it has an itinerary within budget. |  |  |
| 5 | A supplier research system lets a model choose search queries and candidates, while code enforces an approved vendor list and requires a person before outreach. |  |  |
| 6 | A calculator parses an expression and applies arithmetic operations. |  |  |
| 7 | A customer-support system classifies a request, follows a fixed refund decision table, and asks a model only to draft the final reply. |  |  |
| 8 | A customer-support system diagnoses a problem, chooses among account tools, observes results, and escalates when it cannot resolve the issue. |  |  |

## Questions

1. Which systems contain an LLM but are not agents?
2. Which system would change classification if its “next action” were selected by a model instead of a fixed rule?
3. For each agent or hybrid, name one stopping condition and one safety constraint.
4. Can a system be agentic without an LLM? Give a short argument.

## Instructor discussion guide

Suggested classifications: 1 LLM application; 2 LLM application; 3 deterministic workflow; 4 agent; 5 hybrid; 6 deterministic workflow; 7 hybrid; 8 agent or hybrid depending on whether the controller adds deterministic approval and routing rules.

Defend alternatives by describing the actual control flow. A marketing name such as “AI assistant” is not architectural evidence.
