import json
from pathlib import Path

from eval_runner import EvalRunner
from supplier_agent import run_case


def wrap_result_grader(fn):
    return lambda result, trace, case: fn(result, case)


def wrap_trace_grader(fn):
    return lambda result, trace, case: fn(trace, case)


def load_graders():
    import graders

    return {
        "task_success": wrap_result_grader(graders.grade_task_success),
        "budget": wrap_result_grader(graders.grade_budget),
        "required_tool": wrap_trace_grader(graders.grade_required_tool),
        "forbidden_tool": wrap_trace_grader(graders.grade_forbidden_tool),
        "max_steps": wrap_trace_grader(graders.grade_max_steps),
        "approval": wrap_result_grader(graders.grade_approval),
    }


def main():
    cases_path = Path(__file__).resolve().parents[1] / "evals" / "supplier_cases.json"
    cases = json.loads(cases_path.read_text())

    runner = EvalRunner(run_case, load_graders())
    report = runner.run_suite(cases)

    print(f"Total cases: {report['total_cases']}")
    print(f"Passed: {report['passed']}")
    print(f"Failed: {report['failed']}")
    print(f"Task success rate: {report['task_success_rate']:.1%}")
    print(f"Average steps: {report['average_steps']:.2f}")

    if report["failed"]:
        print("\nFailed cases:")
        for item in report["results"]:
            if not item["success"]:
                failed = [name for name, ok in item["grades"].items() if not ok]
                print(f"  {item['case_id']}: {', '.join(failed)}")


if __name__ == "__main__":
    main()
