from config import *

def apply_rules(user_data):
    score = RISK_SCORE_MIN
    reasons = []

    if user_data['failed_logins'] >= FAILED_LOGIN_THRESHOLD:
        score += 15
        reasons.append("Excessive failed logins")

    if user_data['login_hour'] < 6 or user_data['login_hour'] > 20:
        score += 10
        reasons.append("Unusual login time")

    if user_data['sensitive_file_accesses'] >= SENSITIVE_FILE_THRESHOLD:
        score += 15
        reasons.append("Frequent access to sensitive files")

    return min(score, RISK_SCORE_MAX), reasons
