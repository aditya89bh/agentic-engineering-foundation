from __future__ import annotations

import time
from typing import Callable, Any

from errors import AgentError, PermanentToolError, RetryableToolError


class ReliableExecutor:
    def __init__(self, max_attempts=3, base_delay=0.0, sleeper=time.sleep):
        if max_attempts < 1:
            raise ValueError("max_attempts must be >= 1")
        self.max_attempts = max_attempts
        self.base_delay = base_delay
        self.sleeper = sleeper
        self.failure_log = []

    def _log(self, error: AgentError):
        self.failure_log.append(error.as_dict())

    def execute(
        self,
        operation: Callable[[], Any],
        *,
        component="operation",
        fallback: Callable[[], Any] | None = None,
    ):
        for attempt in range(1, self.max_attempts + 1):
            try:
                value = operation()
                return {
                    "status": "COMPLETED",
                    "value": value,
                    "attempts": attempt,
                    "fallback_used": False,
                }
            except RetryableToolError as exc:
                error = AgentError(
                    type="RETRYABLE_TOOL_ERROR",
                    component=component,
                    message=str(exc),
                    retryable=True,
                    attempt=attempt,
                )
                self._log(error)

                if attempt < self.max_attempts:
                    delay = self.base_delay * (2 ** (attempt - 1))
                    self.sleeper(delay)
                    continue
                break
            except PermanentToolError as exc:
                error = AgentError(
                    type="PERMANENT_TOOL_ERROR",
                    component=component,
                    message=str(exc),
                    retryable=False,
                    attempt=attempt,
                )
                self._log(error)
                return {
                    "status": "FAILED",
                    "error": error.as_dict(),
                    "attempts": attempt,
                    "fallback_used": False,
                }

        if fallback is not None:
            try:
                value = fallback()
                return {
                    "status": "PARTIAL_SUCCESS",
                    "value": value,
                    "attempts": self.max_attempts,
                    "fallback_used": True,
                }
            except Exception as exc:
                error = AgentError(
                    type="FALLBACK_FAILED",
                    component=component,
                    message=str(exc),
                    retryable=False,
                    attempt=self.max_attempts,
                )
                self._log(error)
                return {
                    "status": "NEEDS_HUMAN",
                    "error": error.as_dict(),
                    "attempts": self.max_attempts,
                    "fallback_used": True,
                }

        return {
            "status": "FAILED",
            "error": self.failure_log[-1] if self.failure_log else None,
            "attempts": self.max_attempts,
            "fallback_used": False,
        }
