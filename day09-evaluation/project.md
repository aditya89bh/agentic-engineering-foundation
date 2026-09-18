# Mini-Project: Agent Evaluation Suite

Build a repeatable evaluation harness for the supplier agent developed across Days 1–8.

## Dataset

Minimum 20 cases:

- 5 standard tasks;
- 4 ambiguity cases;
- 3 missing-data cases;
- 3 failure-injection cases;
- 2 memory/context cases;
- 2 approval/policy cases;
- 1 adversarial case.

## Required metrics

At minimum:

- task success rate;
- constraint adherence;
- tool selection accuracy;
- tool argument accuracy;
- average steps;
- recovery success;
- policy violations.

Optional:

- latency;
- model calls;
- token usage;
- estimated cost.

## Required engineering properties

- structured evaluation dataset;
- deterministic graders;
- execution traces;
- component evaluation;
- trajectory evaluation;
- outcome evaluation;
- failure categorization;
- aggregate metrics;
- regression comparison;
- at least 20 cases;
- at least 10 automated tests.

## Acceptance checks

1. every case has an explicit expected outcome;
2. objective checks use deterministic graders;
3. traces are stored for failed cases;
4. required tools can be graded;
5. forbidden tools can be graded;
6. max-step constraints can be graded;
7. approval behavior can be graded;
8. aggregate pass rate is computed;
9. failures can be grouped by subsystem;
10. the same suite can be reused after a system change.

## Reflection

Explain why a correct final answer can still represent a poor agent run. Explain why changing a prompt without rerunning the evaluation suite is weak engineering practice.
