import datetime

class AuditLogger:

    def log_event(
        self,
        event_type,
        candidate_id,
        data
    ):

        return {

            "event_type": event_type,

            "candidate_id": candidate_id,

            "data": data,

            "timestamp":
                datetime.datetime.utcnow().isoformat()
        }