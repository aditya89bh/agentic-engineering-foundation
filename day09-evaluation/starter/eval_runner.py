class EvalRunner:
    def __init__(self, agent, graders):
        self.agent = agent
        self.graders = graders

    def run_case(self, case):
        # TODO 1: run the agent
        # TODO 2: collect result and trace
        # TODO 3: execute graders
        # TODO 4: return structured metrics
        raise NotImplementedError

    def run_suite(self, cases):
        # TODO: run all cases and aggregate results
        raise NotImplementedError
