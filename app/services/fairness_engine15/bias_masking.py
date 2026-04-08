SENSITIVE_FIELDS = [
    "name",
    "gender",
    "age",
    "dob",
    "photo",
    "marital_status",
    "nationality"
]


def mask_sensitive_fields(candidate):
    """
    Remove sensitive attributes from recruiter view.
    """
    for field in SENSITIVE_FIELDS:
        if field in candidate:
            del candidate[field]

    return candidate