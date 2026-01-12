def recommend_site(url):
    url = url.lower()

    if "bank" in url:
        return "https://www.onlinesbi.sbi"
    elif "amazon" in url:
        return "https://www.amazon.in"
    elif "flipkart" in url:
        return "https://www.flipkart.com"
    else:
        return "https://www.google.com"
