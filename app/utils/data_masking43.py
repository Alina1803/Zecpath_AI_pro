def mask_data(data):
    if "email" in data:
        data["email"] = "***masked***"
    if "phone" in data:
        data["phone"] = "***masked***"
    return data