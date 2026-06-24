class StableAPI:
    @staticmethod
    def success(data):
        return {
            "status": "success",
            "data": data,
        }

    @staticmethod
    def failed(msg):
        return {
            "status": "failed",
            "error": msg,
        }
