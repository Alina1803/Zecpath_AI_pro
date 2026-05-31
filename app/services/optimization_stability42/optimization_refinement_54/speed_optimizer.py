import time


class SpeedOptimizer:

    def benchmark(self, function):

        start = time.time()

        function()

        end = time.time()

        return {

            "execution_time":
                round(end - start, 4),

            "status":
                "Optimized"
        }