from errors import RetryableToolError
from reliable_executor import ReliableExecutor


class FlakySupplierSearch:
    def __init__(self):
        self.calls = 0

    def __call__(self):
        self.calls += 1
        if self.calls < 3:
            raise RetryableToolError("supplier API timed out")
        return [
            {"id": "SUP-001", "unit_price": 480},
            {"id": "SUP-002", "unit_price": 445},
        ]


def cached_suppliers():
    return [{"id": "SUP-CACHED", "unit_price": 495, "source": "cache"}]


def main():
    executor = ReliableExecutor(max_attempts=3, base_delay=0)
    operation = FlakySupplierSearch()

    result = executor.execute(
        operation,
        component="SEARCH_SUPPLIERS",
        fallback=cached_suppliers,
    )

    print("Final result:")
    print(result)

    print("\nFailure log:")
    for entry in executor.failure_log:
        print(entry)


if __name__ == "__main__":
    main()
