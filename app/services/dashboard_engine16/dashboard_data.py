def prepare_dashboard_rows(candidates):
    rows = []

    for candidate in candidates:
        rows.append({
            "file_name": candidate["file_name"],
            "rank": candidate["rank"],
            "decision": candidate["decision"],
            "final_score": candidate["scores"]["final_score"],
            "normalized_score": candidate["scores"].get("normalized_score", 0)
        })

    return rows