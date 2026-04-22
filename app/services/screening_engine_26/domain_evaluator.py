CA_KEY_TERMS = {
    "gst": ["gst", "input tax credit", "returns", "gstr"],
    "audit": ["audit", "verification", "compliance"],
    "tax": ["income tax", "deductions", "filing"]
}


def domain_score(answer, domain_data):

    score = 0

    for domain, details in domain_data.items():
        for keyword in details["keywords"]:
            if keyword in answer.lower():
                score += details.get("weight", 1)

    return min(score, 10)