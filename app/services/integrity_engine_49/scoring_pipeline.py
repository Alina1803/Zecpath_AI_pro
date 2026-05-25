from app.services.integrity_engine_49.event_aggregator import (aggregate_events)

from app.services.integrity_engine_49.pattern_engine import (detect_patterns)

from app.services.integrity_engine_49.scoring_engine import (calculate_integrity_score)

from app.services.integrity_engine_49.risk_engine import (risk_flagging)

from app.services.integrity_engine_49.warning_engine import (generate_warning)

from app.services.integrity_engine_49.dashboard_payload import (recruiter_payload)


def integrity_pipeline(data):

    events = aggregate_events(data)

    patterns = detect_patterns(events)

    score = calculate_integrity_score(events)

    risk = risk_flagging(score)

    warnings = generate_warning(events)

    result = recruiter_payload(
        candidate_id="C4001",
        score=score,
        risk=risk,
        patterns=patterns,
        warnings=warnings
    )

    return result