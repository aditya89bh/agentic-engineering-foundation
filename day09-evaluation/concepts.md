# Day 9 Concepts

## 1. Why agent evaluation is different

Traditional software often looks like:

```text
input → function → output
```

An agent may execute many intermediate decisions before producing a final outcome.

That means evaluation must inspect both:

- the result;
- the path used to reach it.

## 2. Three evaluation levels

### Component evaluation

Check individual subsystems such as:

- requirement extraction;
- tool selection;
- argument generation;
- context routing;
- memory retrieval;
- policy decisions.

### Trajectory evaluation

Check the sequence of actions:

- unnecessary steps;
- repeated calls;
- invalid actions;
- retry behavior;
- approval handling.

### Outcome evaluation

Check whether the task actually succeeded.

## 3. Define success before testing

Avoid vague judgments such as “the agent seems good.”

Use explicit criteria:

```text
correct supplier selected
AND budget respected
AND required certification satisfied
AND no unauthorized tool executed
```

## 4. Evaluation case schema

Each test case should contain:

```text
id
request
expected outcome
expected status
constraints
tags
```

## 5. Golden dataset

A useful small evaluation set should include more than happy paths.

Day 9 uses 20 cases across:

- standard tasks;
- ambiguity;
- missing information;
- tool failures;
- memory/context edge cases;
- approval/policy cases;
- adversarial behavior.

## 6. Task success rate

```text
successful tasks / total tasks
```

Useful, but not sufficient by itself.

## 7. Tool selection accuracy

Measure whether the agent chose the correct tool for the step.

## 8. Tool argument accuracy

A correct tool with wrong arguments is still a failure.

## 9. Constraint adherence

Evaluate hard requirements separately:

- price limits;
- required certifications;
- inspected supplier requirement;
- rejected supplier exclusion;
- approval requirement.

## 10. Trajectory quality

A trace can reach the right result inefficiently.

Examples:

- repeated search;
- duplicate inspection;
- unnecessary retries;
- redundant tool calls.

Useful metrics include:

- total steps;
- tool calls;
- repeated actions;
- invalid actions.

## 11. Recovery evaluation

Inject failures and verify the intended recovery path:

```text
failure → retry → success
```

or:

```text
failure → retry exhausted → fallback
```

## 12. Guardrail evaluation

Governance behavior belongs in the evaluation suite.

Examples:

- researcher attempts CREATE_PURCHASE_ORDER → DENY;
- high-value order → REQUIRE_APPROVAL;
- changed action after approval → reject approval reuse.

## 13. Memory evaluation

Check both retrieval and use:

- relevant memory retrieved?;
- irrelevant memory excluded?;
- stale memory rejected?;
- retrieved memory affected decision correctly?

## 14. Context evaluation

Useful checks include:

- latest constraint included;
- stale constraint excluded;
- relevant tools included;
- irrelevant history excluded;
- context budget respected.

## 15. Execution traces

Each run should emit a structured trace containing:

- case ID;
- steps;
- actions;
- tool arguments;
- statuses;
- retries;
- final outcome.

Traces are debugging artifacts.

## 16. Deterministic graders

Use code when truth is objective.

Examples:

- budget respected;
- expected status;
- required tool used;
- forbidden tool absent;
- max step limit;
- approval obtained.

## 17. LLM-as-judge

LLM graders can help with semantic qualities such as relevance or explanation quality, but they are not ground truth.

Potential limitations:

- inconsistency;
- prompt sensitivity;
- model bias;
- position bias.

Day 9 keeps LLM judging optional.

## 18. Evaluation dimensions

Useful per-run metrics:

```text
task_success
tool_accuracy
argument_accuracy
constraint_adherence
steps
retries
recovery_success
policy_violations
latency
token_usage
```

## 19. Cost and latency

Two agents can both succeed while one uses far more steps, model calls, or tool calls.

Engineering quality includes efficiency.

## 20. Regression testing

The correct workflow is:

```text
agent v1
→ evaluation suite
→ system change
→ agent v2
→ same evaluation suite
→ compare
```

Never judge a system change from one anecdotal example.

## 21. Failure categorization

Group failures by subsystem:

- requirement extraction;
- tool selection;
- tool arguments;
- context;
- memory;
- recovery;
- policy;
- final reasoning.

Fix the subsystem that actually failed.

## 22. Evaluation report

A report should contain:

- total cases;
- passed;
- failed;
- aggregate metrics;
- failure categories;
- examples of failed traces;
- proposed fixes.
