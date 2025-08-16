def get_risk_level(score):
    if score >= 40:
        return "Critical"
    elif score >= 30:
        return "High"
    elif score >= 20:
        return "Medium"
    else:
        return "Low"
