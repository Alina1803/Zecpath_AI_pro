# ----------------------------------------
# Risk Classification Engine
# ----------------------------------------

def risk_flagging(score):

    if score < 50:
        return "High Risk"

    elif score < 75:
        return "Moderate Risk"

    return "Low Risk"