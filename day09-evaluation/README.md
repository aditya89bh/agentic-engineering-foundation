# Day 9: Agent Evaluation and Testing

## Objective

By the end of Day 9, students should be able to define explicit success criteria, build evaluation datasets, inspect execution traces, grade component and trajectory behavior, and run repeatable regression evaluations.

## Learning outcomes

Students will be able to:

- distinguish component, trajectory, and outcome evaluation;
- define measurable success criteria before testing;
- build a structured evaluation dataset;
- implement deterministic graders;
- inspect execution traces;
- measure tool selection, argument accuracy, constraint adherence, recovery, and policy behavior;
- aggregate metrics across cases;
- categorize failures by subsystem;
- compare system versions using the same evaluation suite.

## Suggested flow

1. Read [concepts.md](concepts.md).
2. Complete [Write Eval Cases](exercises/write-eval-cases.md).
3. Complete [Grade a Trace](exercises/grade-trace.md).
4. Implement [starter/graders.py](starter/graders.py).
5. Implement [starter/eval_runner.py](starter/eval_runner.py).
6. Run the reference evaluation suite.
7. Inspect the generated report.
8. Build the [Agent Evaluation Suite](project.md).
9. Review [failure-cases.md](failure-cases.md).

## Run the reference implementation

```bash
python day09-evaluation/solution/report.py
python -m unittest discover day09-evaluation/tests -v
```

## Core mental model

```text
Component evaluation
        ↓
Trajectory evaluation
        ↓
Outcome evaluation
```

> A correct final answer does not automatically mean the agent executed well.
