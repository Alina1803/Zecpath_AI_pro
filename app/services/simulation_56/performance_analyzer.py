import time


class PerformanceAnalyzer:

    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):

        duration = time.time() - self.start_time

        return {"execution_time": round(duration, 3)}
