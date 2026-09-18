class RetryableError(Exception):
    pass


class ReliableExecutor:
    def __init__(self, max_attempts=3):
        self.max_attempts = max_attempts

    def execute(self, operation, fallback=None):
        last_error = None
        for attempt in range(1, self.max_attempts + 1):
            try:
                return {"status":"COMPLETED","value":operation(),"attempts":attempt}
            except RetryableError as exc:
                last_error = str(exc)

        if fallback:
            return {"status":"PARTIAL_SUCCESS","value":fallback(),"attempts":self.max_attempts}

        return {"status":"FAILED","error":last_error,"attempts":self.max_attempts}
