import json


class SimulationReportGenerator:

    @staticmethod
    def generate(report, path):

        with open(path, "w") as fp:
            json.dump(report, fp, indent=4)
