from __future__ import annotations


class EvalRunner:
    def __init__(self, agent, graders):
        self.agent = agent
        self.graders = graders

    def run_case(self, case):
        result, trace = self.agent(case)

        grades = {
            name: grader(result, trace, case)
            for name, grader in self.graders.items()
        }

        return {
            "case_id": case["id"],
            "success": all(grades.values()),
            "grades": grades,
            "metrics": {
                "steps": len(trace),
                "tool_calls": sum(1 for step in trace if step.get("action")),
                "policy_violations": 0 if grades.get("forbidden_tool", True) else 1,
            },
            "result": result,
            "trace": trace,
            "tags": case.get("tags", []),
        }

    def run_suite(self, cases):
        results = [self.run_case(case) for case in cases]
        total = len(results)
        passed = sum(1 for item in results if item["success"])

        avg_steps = (
            sum(item["metrics"]["steps"] for item in results) / total
            if total else 0
        )

        return {
            "total_cases": total,
            "passed": passed,
            "failed": total - passed,
            "task_success_rate": passed / total if total else 0,
            "average_steps": avg_steps,
            "results": results,
        }
