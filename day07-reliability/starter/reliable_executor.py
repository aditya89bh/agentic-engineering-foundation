from errors import AgentError


class ReliableExecutor:
    def __init__(self, max_attempts=3):
        self.max_attempts = max_attempts

    def execute(self, operation, fallback=None):
        # TODO 1: call operation
        # TODO 2: classify retryable failures
        # TODO 3: retry only within max_attempts
        # TODO 4: apply backoff
        # TODO 5: use fallback if configured
        # TODO 6: return structured outcome and failure log
        raise NotImplementedError
