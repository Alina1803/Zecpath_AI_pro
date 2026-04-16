def validate(candidate):
    required = ["is_ca", "experience", "gst_experience"]

    for r in required:
        if r not in candidate:
            return False

    return True