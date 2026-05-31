import json


class ExportManager:

    @staticmethod
    def export_json(report, filename="report53.json"):

        with open(filename, "w") as file:

            json.dump(
                report,
                file,
                indent=4
            )

        return filename