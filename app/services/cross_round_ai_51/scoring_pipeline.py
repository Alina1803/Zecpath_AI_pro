from app.services.cross_round_ai_51.cross_round_engine import (
    get_weights,
    calculate_final_score)

from app.services.cross_round_ai_51.hiring_fit_engine import (hiring_fit)

from app.services.cross_round_ai_51.normalization_engine import (normalize_scores)

from app.services.cross_round_ai_51.explainability_engine import (explain_scores)

from app.services.cross_round_ai_51.decision_engine import (hiring_decision)

from app.services.cross_round_ai_51.analytics_engine import (candidate_strength)

from app.services.cross_round_ai_51.recruiter_report import (recruiter_summary)

from app.services.cross_round_ai_51.benchmarking_engine import (benchmark_score)

from app.services.cross_round_ai_51.ranking_engine import (rank_candidate)


def aggregation_pipeline(data):

    scores = {

        "ats": data.ats,

        "screening": data.screening,

        "hr": data.hr,

        "technical": data.technical,

        "machine_test": data.machine_test
    }

    normalized_scores = normalize_scores(scores)

    weights = get_weights(data.role_type)

    final_score = calculate_final_score(
        normalized_scores,
        weights
    )

    ranking = rank_candidate(final_score)

    return {

        "candidate_id": data.candidate_id,

        "role_type": data.role_type,

        "normalized_scores": normalized_scores,

        "weights": weights,

        "final_score": final_score,

        "decision": hiring_decision(final_score),

        "hiring_fit": hiring_fit(final_score),

        "benchmark": benchmark_score(final_score),

        "ranking": ranking,

        "analytics": candidate_strength(
            normalized_scores
        ),

        "explanation": explain_scores(
            normalized_scores
        ),

        "recruiter_summary": recruiter_summary(
            data.candidate_id,
            final_score
        )
    }