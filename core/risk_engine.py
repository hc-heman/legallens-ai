def score_clause(text):
    score = 0
    t = text.lower()

    if "terminate at any time" in t:
        score += 30
    if "penalty" in t or "liquidated damages" in t:
        score += 25
    if "indemnify" in t:
        score += 20
    if "sole discretion" in t:
        score += 15
    if "jurisdiction" in t and "india" not in t:
        score += 10

    level = "Low"
    if score > 60:
        level = "High"
    elif score > 30:
        level = "Medium"

    return score, level
