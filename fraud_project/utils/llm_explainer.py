import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_result(url, sentiment, result):
    """
    Uses ChatGPT (LLM) to explain the result.
    Falls back to rule-based explanation if API fails.
    """

    prompt = f"""
You are a cybersecurity expert.

Website URL: {url}
User sentiment: {sentiment}
Detection result: {result}

Explain clearly in simple English why this website is classified as such.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4
        )
        return response.choices[0].message.content

    except Exception:
        # -------- FALLBACK --------
        explanation = ""

        if result == "Fraud Website":
            explanation += "This website is likely fraudulent because:\n"

            if "http://" in url:
                explanation += "- The website does not use secure HTTPS.\n"

            if len(url) > 30:
                explanation += "- The URL is unusually long, which is common in phishing sites.\n"

            if sentiment == "Negative":
                explanation += "- User reviews show negative sentiment indicating unsafe experience.\n"

        else:
            explanation = "This website appears to be genuine based on URL structure and user sentiment."

        return explanation
