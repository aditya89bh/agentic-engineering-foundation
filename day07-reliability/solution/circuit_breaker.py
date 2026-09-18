from __future__ import annotations

import time


class CircuitOpenError(RuntimeError):
    pass


class CircuitBreaker:
    def __init__(self, failure_threshold=3, recovery_seconds=30, clock=time.monotonic):
        self.failure_threshold = failure_threshold
        self.recovery_seconds = recovery_seconds
        self.clock = clock
        self.failure_count = 0
        self.state = "CLOSED"
        self.opened_at = None

    def allow_call(self):
        if self.state != "OPEN":
            return True

        if self.clock() - self.opened_at >= self.recovery_seconds:
            self.state = "HALF_OPEN"
            return True

        raise CircuitOpenError("circuit is open")

    def record_success(self):
        self.failure_count = 0
        self.state = "CLOSED"
        self.opened_at = None

    def record_failure(self):
        self.failure_count += 1
        if self.failure_count >= self.failure_threshold:
            self.state = "OPEN"
            self.opened_at = self.clock()
