from flask import Flask, render_template, request
import sys
import os

# utils folder ko path me add karna
sys.path.append(os.path.join(os.path.dirname(__file__), "utils"))

import sentiment
import fraud_logic
import recommendation
import llm_explainer

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():
    url = request.form["url"]
    review = request.form.get("review", "")

    # 👇 agar user ne review nahi diya
    auto_review = False
    if review.strip() == "":
        review = f"This website {url} may be risky or unsafe. Users should be cautious."
        auto_review = True

    sentiment_result = sentiment.analyze_sentiment(review)
    result = fraud_logic.check_fraud(url, sentiment_result)

    # recommendation
    recommended = None
    if result == "Fraud Website":
        recommended = recommendation.recommend_site(url)

    # explanation (LLM / logic based)
    explanation = llm_explainer.explain_result(
        url,
        sentiment_result,
        result
    )

    return render_template(
        "result.html",
        sentiment=sentiment_result,
        result=result,
        url=url,
        recommended=recommended,
        explanation=explanation
    )


if __name__ == "__main__":
    app.run(debug=True)
