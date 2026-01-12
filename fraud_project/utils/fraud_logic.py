def check_fraud(url, sentiment):
    score = 0

    if "http://" in url:
        score += 1
    if len(url) > 30:
        score += 1
    if sentiment == "Negative":
        score += 2

    if score >= 3:
        return "Fraud Website"
    else:
        return "Genuine Website"