ROLE_KEYWORDS = {
    "chartered accountant": [
        "accounting","financial reporting","auditing","taxation","gst",
        "income tax","balance sheet","financial statements","compliance",
        "statutory audit","internal audit","ifrs","gaap","financial analysis"
    ],
    "accountant": [
        "bookkeeping","journal entries","ledger","tally","accounts payable",
        "accounts receivable","reconciliation","financial statements"
    ],
    "auditor": [
        "internal audit","statutory audit","risk assessment",
        "compliance","financial audit","control testing"
    ]
}

def role_similarity(candidate_role, target_role):
    candidate_role = candidate_role.lower()
    target_role = target_role.lower()

    c_keywords = set()
    t_keywords = set()

    for role, keywords in ROLE_KEYWORDS.items():
        if role in candidate_role:
            c_keywords.update(keywords)
        if role in target_role:
            t_keywords.update(keywords)

    if not c_keywords or not t_keywords:
        return 0.2

    return round(len(c_keywords & t_keywords) / len(t_keywords), 2)