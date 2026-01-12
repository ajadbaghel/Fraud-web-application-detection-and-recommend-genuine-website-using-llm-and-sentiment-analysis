from sentiment import analyze_sentiment
from fraud_logic import check_fraud


sentiment = analyze_sentiment("This website is fake and unsafe")
result = check_fraud("http://fakebank-login.com", sentiment)

print(sentiment)
print(result)