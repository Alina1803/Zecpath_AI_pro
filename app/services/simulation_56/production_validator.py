import os


class ProductionValidator:

    @staticmethod
    def validate():

        checks = {"logging": False, "reports": False, "retry_handler": False}

        checks["logging"] = os.path.exists("logs")

        checks["reports"] = os.path.exists("reports")

        checks["retry_handler"] = os.path.exists("app/services/retry_handler.py")

        checks["ready"] = all(checks.values())

        return checks
