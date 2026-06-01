from datetime import datetime


class ConsentManager:

    def capture_consent(
        self,
        candidate_id
    ):

        return {

            "candidate_id":
                candidate_id,

            "consent":
                True,

            "timestamp":
                datetime.utcnow().isoformat()
        }