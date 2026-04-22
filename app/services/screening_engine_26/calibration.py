def calibrate(score):
    # normalize + adjust bias
    if score > 85:
        score -= 2  # avoid inflation
    elif score < 40:
        score += 3  # avoid harsh penalty

    return round(score, 2)